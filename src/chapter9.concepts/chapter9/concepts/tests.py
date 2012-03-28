import unittest as unittest

from chapter9.concepts.testing_fixture_setup \
    import CH9_INTEGRATION_TESTING

class TestSetup(unittest.TestCase):
    layer = CH9_INTEGRATION_TESTING
    def test_portal_title(self):
        portal = self.layer['portal']
        self.assertTrue(True)