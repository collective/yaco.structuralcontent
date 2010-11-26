# -*- coding utf8 -*-
from plone.locking.interfaces import ILockable
from interfaces import STRUCTURALCONTENT_LOCK
from webdav.LockItem import MAXTIMEOUT

__all__ = ['lockContext', 'unlockContext', 'isLocked']

def lockContext( context ):
    lockable = ILockable(context)
    lockable.lock(STRUCTURALCONTENT_LOCK)
    token = lockable.lock_info()[0]['token']
    lock = lockable.context.wl_getLock(token)
    lock.setTimeout(MAXTIMEOUT)

def unlockContext( context ):
    lockable = ILockable(context)
    lockable.unlock(STRUCTURALCONTENT_LOCK)

def isLocked( context ):
    lockable = ILockable(context)
    lockable.locked()