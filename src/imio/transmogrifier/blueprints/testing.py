# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import imio.transmogrifier.blueprints


class ImioTransmogrifierBlueprintsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=imio.transmogrifier.blueprints)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'imio.transmogrifier.blueprints:default')


IMIO_TRANSMOGRIFIER_BLUEPRINTS_FIXTURE = ImioTransmogrifierBlueprintsLayer()


IMIO_TRANSMOGRIFIER_BLUEPRINTS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IMIO_TRANSMOGRIFIER_BLUEPRINTS_FIXTURE,),
    name='ImioTransmogrifierBlueprintsLayer:IntegrationTesting'
)


IMIO_TRANSMOGRIFIER_BLUEPRINTS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IMIO_TRANSMOGRIFIER_BLUEPRINTS_FIXTURE,),
    name='ImioTransmogrifierBlueprintsLayer:FunctionalTesting'
)


IMIO_TRANSMOGRIFIER_BLUEPRINTS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        IMIO_TRANSMOGRIFIER_BLUEPRINTS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ImioTransmogrifierBlueprintsLayer:AcceptanceTesting'
)
