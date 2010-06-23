# -*- coding: utf-8 -*-
import unittest

#from zope.testing import doctestunit
#from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_product():
    """Set up the package and its dependencies."""

    fiveconfigure.debug_mode = True
    import yaco.structuralcontent
    zcml.load_config('configure.zcml', yaco.structuralcontent)
    fiveconfigure.debug_mode = False

setup_product()
ptc.setupPloneSite(products=['yaco.structuralcontent'])

def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='yaco.structuralcontent',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='yaco.structuralcontent.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'README.txt', package='yaco.structuralcontent',
            test_class=ptc.FunctionalTestCase),

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='yaco.structuralcontent',
        #    test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
