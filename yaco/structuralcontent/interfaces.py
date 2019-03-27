# -*- coding: utf-8 -*-
from plone.locking.interfaces import LockType
from yaco.structuralcontent import StructuralContentMessageFactory as _
from zope.interface import Interface


class IStructuralContent(Interface):
    """Marker interface
    """

    pass

STRUCTURALCONTENT_LOCK = LockType(
    u"yaco.structuralcontent.lock", stealable=False, user_unlockable=False
)
