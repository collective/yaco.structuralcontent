from plone.locking.interfaces import LockType
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IStructuralContent(Interface):
    """Marker interface"""


class IYacoStructuralcontent(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


STRUCTURALCONTENT_LOCK = LockType(
    "yaco.structuralcontent.lock", stealable=False, user_unlockable=False
)
