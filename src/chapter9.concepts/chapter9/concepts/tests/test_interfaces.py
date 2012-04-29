import unittest2 as unittest
from testing_fixture_setup import CH9_INTEGRATION_TESTING

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from zope.interface.interface import InterfaceClass
from zope.interface import alsoProvides, noLongerProvides
import chapter9.concepts.interface_examples as IE


class TestInterfaces(unittest.TestCase):
    layer = CH9_INTEGRATION_TESTING
    def test_iface_definitions(self):
        self.assertTrue(isinstance(IE.IBelievable, InterfaceClass))
        self.assertTrue(isinstance(IE.IUndeniable, InterfaceClass))
    def test_implements(self):
        self.assertTrue(IE.IMessage.implementedBy(IE.StandardMessage))
        self.assertTrue(IE.IMessage.implementedBy(IE.StrongMessage))
        self.assertFalse(IE.IBelievable.implementedBy(IE.StandardMessage))
        self.assertTrue(IE.IBelievable.implementedBy(IE.StrongMessage))
    def test_implements_instances(self):
        fender = IE.StandardMessage("Fenders Rock!")
        strat = IE.StrongMessage("Starts are Great!")
        telecaster = IE.StrongMessage("Telecasters are awesome!")
        self.assertTrue(IE.IMessage.providedBy(fender))
        self.assertTrue(IE.IMessage.providedBy(strat))
        self.assertFalse(IE.IBelievable.providedBy(fender))
        self.assertTrue(IE.IBelievable.providedBy(strat))
        self.assertFalse(IE.IUndeniable.providedBy(telecaster))
        alsoProvides(telecaster, IE.IUndeniable)
        self.assertTrue(IE.IUndeniable.providedBy(telecaster))
        noLongerProvides(telecaster, IE.IUndeniable)
        self.assertFalse(IE.IUndeniable.providedBy(telecaster))
        self.assertFalse(IE.IUndeniable.providedBy(fender))
    def test_alsoProvides_for_classes(self):
        self.assertFalse(IE.ICommunicationFactory.implementedBy(IE.StandardMessage))
        self.assertTrue(IE.ICommunicationFactory.providedBy(IE.StandardMessage))
        self.assertTrue(IE.ICommunicationFactory.providedBy(IE.StrongMessage))