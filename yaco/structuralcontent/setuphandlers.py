# -*- coding: utf8 -*-
import logging

from zope.interface import noLongerProvides
from yaco.structuralcontent.interfaces import IStructuralContent
from yaco.structuralcontent import lock

from Products.CMFCore.utils import getToolByName

def uninstallVarious(context):
    """Remove marker interfaces and locks
    """
    site = context.getSite()
    portal_catalog = getToolByName(site, 'portal_catalog')
    logger = logging.getLogger("yaco.structuralcontent")
    logger.info("Removing marker interfaces and locks")

    query = {}
    query['object_provides'] = IStructuralContent.__identifier__

    results = portal_catalog.searchResults(query)
    for brain in results:
        obj = brain.getObject()
        if IStructuralContent.providedBy(obj):
            lock.unlockContext(obj)
            noLongerProvides(obj, IStructuralContent)
            obj.reindexObject(idxs=['object_provides'])

