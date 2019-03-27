# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import yaco.structuralcontent


class YacoStructuralcontent(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=yaco.structuralcontent)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "yaco.structuralcontent:default")


YACO_STRUCTURALCONTENT_FIXTURE = YacoStructuralcontent()


YACO_STRUCTURALCONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(YACO_STRUCTURALCONTENT_FIXTURE,),
    name="YacoStructuralcontent:IntegrationTesting",
)


YACO_STRUCTURALCONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(YACO_STRUCTURALCONTENT_FIXTURE,),
    name="YacoStructuralcontent:FunctionalTesting",
)


YACO_STRUCTURALCONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        YACO_STRUCTURALCONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="YacoStructuralcontent:AcceptanceTesting",
)
