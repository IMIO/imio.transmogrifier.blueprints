# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from imio.transmogrifier.blueprints.testing import IMIO_TRANSMOGRIFIER_BLUEPRINTS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that imio.transmogrifier.blueprints is properly installed."""

    layer = IMIO_TRANSMOGRIFIER_BLUEPRINTS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if imio.transmogrifier.blueprints is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'imio.transmogrifier.blueprints'))

    def test_browserlayer(self):
        """Test that IImioTransmogrifierBlueprintsLayer is registered."""
        from imio.transmogrifier.blueprints.interfaces import (
            IImioTransmogrifierBlueprintsLayer)
        from plone.browserlayer import utils
        self.assertIn(IImioTransmogrifierBlueprintsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = IMIO_TRANSMOGRIFIER_BLUEPRINTS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['imio.transmogrifier.blueprints'])

    def test_product_uninstalled(self):
        """Test if imio.transmogrifier.blueprints is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'imio.transmogrifier.blueprints'))
