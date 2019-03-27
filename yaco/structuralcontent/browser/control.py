# -*- coding:utf8 -*-
from plone.app.z3cform.layout import wrap_form
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from yaco.structuralcontent import lock
from yaco.structuralcontent import StructuralContentMessageFactory as _
from yaco.structuralcontent.interfaces import IStructuralContent
from z3c.form import button
from z3c.form import field
from z3c.form import form
from zope.interface import alsoProvides
from zope.interface import noLongerProvides


class ContentControl(BrowserView):
    """ conditions for presenting various actions
    """

    __allow_access_to_unprotected_subobjects__ = 1

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def allowLock(self):
        """
        """
        return IContentish.providedBy(
            self.context
        ) and not IStructuralContent.providedBy(self.context)

    allowLock.__roles__ = None

    def allowUnlock(self):
        """
        """
        return IStructuralContent.providedBy(self.context)

    allowUnlock.__roles__ = None


class LockForm(form.Form):
    label = _(u"Lock this object as 'Structural content'")
    description = _(
        u"To lock this object as 'Structural content' click on 'Save'. "
        "If you are unsure about this action click on 'Cancel'."
    )

    @button.buttonAndHandler(_(u"Save"))
    def handleApply(self, action):
        lock.lockContext(self.context)
        alsoProvides(self.context, IStructuralContent)
        self.context.reindexObject(idxs=["object_provides"])
        plone_utils = getToolByName(self.context, "plone_utils")
        plone_utils.addPortalMessage(
            _(u"The content was locked as 'Structual content'")
        )
        self.request.response.redirect(self.context.absolute_url())

    @button.buttonAndHandler(_(u"Cancel"))
    def handleCancel(self, action):
        plone_utils = getToolByName(self.context, "plone_utils")
        plone_utils.addPortalMessage(_("Accion cancelled"))
        self.request.response.redirect(self.context.absolute_url())


LockView = wrap_form(LockForm)


class UnlockForm(form.Form):
    label = _(u"Unlock this structural content object")
    description = _(
        u"To unlock this 'Structural content' object click on 'Save'. "
        "Remember that this could generate inconsistencies in the portal. "
        "If you are unsure about this action click on 'Cancel'."
    )

    @button.buttonAndHandler(_(u"Save"))
    def handleApply(self, action):
        plone_utils = getToolByName(self.context, "plone_utils")

        if not IStructuralContent.providedBy(self.context):
            plone_utils.addPortalMessage(_("This object is not locked"), "error")
            self.request.response.redirect(self.context.absolute_url())
            return

        lock.unlockContext(self.context)
        noLongerProvides(self.context, IStructuralContent)
        self.context.reindexObject(idxs=["object_provides"])
        plone_utils.addPortalMessage(
            _(u"The object was unlocked and can now could be modified")
        )
        self.request.response.redirect(self.context.absolute_url())

    @button.buttonAndHandler(_(u"Cancel"))
    def handleCancel(self, action):
        plone_utils = getToolByName(self.context, "plone_utils")
        plone_utils.addPortalMessage(_("Accion cancelled"))
        self.request.response.redirect(self.context.absolute_url())


UnlockView = wrap_form(UnlockForm)
