# -*- coding: utf-8 -*-
from plone.locking.interfaces import LockType
from yaco.structuralcontent import StructuralContentMessageFactory as _
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IStructuralContent(Interface):
    """Marker interface
    """


class IYacoStructuralcontent(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


STRUCTURALCONTENT_LOCK = LockType(
    u"yaco.structuralcontent.lock", stealable=False, user_unlockable=False
)
