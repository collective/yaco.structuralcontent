# -*- coding: utf-8 -*-

from zope.interface import Interface

from plone.locking.interfaces import LockType
from yaco.structuralcontent import StructuralContentMessageFactory as _

class IStructuralContent( Interface ):
    """Marker interface
    """
    pass

STRUCTURALCONTENT_LOCK = LockType( u'yaco.structuralcontent.lock',
                                    stealable=False, user_unlockable=False )
