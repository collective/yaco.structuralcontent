# -*- coding: utf8 -*-
from Products.CMFCore.utils import getToolByName
from yaco.structuralcontent import lock
from yaco.structuralcontent.interfaces import IStructuralContent
from zope.interface import noLongerProvides

import logging


def uninstallVarious(context):
    """Remove marker interfaces and locks
    """
    site = context.getSite()
    portal_catalog = getToolByName(site, "portal_catalog")
    logger = logging.getLogger("yaco.structuralcontent")
    logger.info("Removing marker interfaces and locks")

    query = {}
    query["object_provides"] = IStructuralContent.__identifier__

    results = portal_catalog.searchResults(query)
    for brain in results:
        obj = brain.getObject()
        if IStructuralContent.providedBy(obj):
            lock.unlockContext(obj)
            noLongerProvides(obj, IStructuralContent)
            obj.reindexObject(idxs=["object_provides"])
