# -*- coding utf8 -*-
from plone.locking.interfaces import IRefreshableLockable
from yaco.structuralcontent.interfaces import STRUCTURALCONTENT_LOCK

try:
    # Zope 2
    from webdav.LockItem import MAXTIMEOUT
except ImportError:
    # Zope 4
    from OFS.LockItem import MAXTIMEOUT


__all__ = ["lockContext", "unlockContext", "isLocked"]


def lockContext(context):
    lockable = IRefreshableLockable(context)
    lockable.lock(STRUCTURALCONTENT_LOCK)
    token = lockable.lock_info()[0]["token"]
    lock = lockable.context.wl_getLock(token)
    lock.setTimeout(MAXTIMEOUT)


def unlockContext(context):
    lockable = IRefreshableLockable(context)
    lockable.unlock(STRUCTURALCONTENT_LOCK)


def isLocked(context):
    lockable = IRefreshableLockable(context)
    lockable.locked()
