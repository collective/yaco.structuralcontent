==============================================================================
Test Structural Content use
==============================================================================

Create the browser object we'll be using.

    >>> from Products.Five.testbrowser import Browser
    >>> from DateTime.DateTime import DateTime
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()
    >>> browser.handleErrors = False
    >>> self.portal.error_log._ignored_exceptions = ()

Log in into the site as manager.

    >>> from Products.PloneTestCase.setup import portal_owner, default_user, default_password
    >>> login_url = portal_url + '/login_form'
    >>> browser.open(login_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> "You are now logged in" in browser.contents
    True

Create a container object named 'folder0' in the portal root

    >>> browser.open(portal_url)
    >>> browser.getLink('Add new').click()
    >>> browser.getControl('Folder').click()
    >>> browser.getControl('Add').click()
    >>> browser.getControl(name='title').value = 'Picasso'
    >>> browser.getControl('Save').click()
    >>> "Changes saved" in browser.contents
    True

    >>> folder0_url = browser.url

Lock the 'folder0' object as structural content

    >>> # browser.getLink('Actions')
    >>> browser.getLink('Lock').click()
    >>> "Lock this object as 'Structural content'" in browser.contents
    True

Confirm the action

    >>> browser.getControl('Save').click()
    >>> "The content was locked as 'Structual content'. This object can't be modified unless it is unlocked previously" in browser.contents
    True

We can add a new object inside the locked folder? let see

    >>> browser.getLink('Add new').click()
    >>> browser.getControl('Page').click()
    >>> browser.getControl('Add').click()
    >>> browser.getControl(name='title').value = 'Gernica'
    >>> browser.getControl('Save').click()
    >>> "Changes saved" in browser.contents
    True

Yes we can, and it's could be edited too

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'Minotauro'
    >>> browser.getControl('Save').click()
    >>> "Changes saved" in browser.contents
    True

Ok, let see the locked 'folder0' object, this should display a portal message with information about the lock

    >>> browser.open(folder0_url)
    >>> "Locked" in browser.contents
    True

    >>> "This Object is locked as 'Structural content'. For this reason can't be edited, deleted or modified in any way" in browser.contents
    True

That is true? Lets try to edit

    >>> browser.getLink('Edit').click()
    Traceback (most recent call last):
    ...
    LinkNotFoundError

The 'Edit' link is not present, but we can try accesing whit the url and change the title

    >>> folder0_edit_url = folder0_url + '/edit'
    >>> browser.open(folder0_edit_url)
    >>> browser.getControl(name='title').value = 'Garcia Lorca'
    Traceback (most recent call last):
    ...
    LookupError: name 'title'

The field for the title input is not there.


Ok, lets go back to the folder0_url and try to delete it

    >>> browser.open(folder0_url)
    >>> browser.getLink('Delete').click()
    >>> browser.getControl('Delete').click()
    >>> "Error" in browser.contents
    True
    >>> "Picasso is locked and cannot be deleted" in browser.contents
    True

And can't be cut

    >>> browser.open(folder0_url)
    >>> browser.getLink('Cut').click()
    >>> "Error" in browser.contents
    True
    >>> "Picasso is locked and cannot be cut" in browser.contents
    True

We can try to rename too, but it's not posible

    >>> browser.getLink('Rename').click()
    >>> browser.getControl('New Short Name').value = 'garcia-lorca'
    >>> browser.getControl('New Title').value = 'Garcia Lorca'
    >>> browser.getControl('Rename All').click()
    Traceback (most recent call last):
    ...
    NotFound: ...

    # This is a bug in plone? why redirect if wasn't posible rename the object?
    >>> # "The following item(s) could not be renamed: /picasso" in browser.contents
    # True
