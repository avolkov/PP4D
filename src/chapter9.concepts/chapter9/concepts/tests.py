import unittest2 as unittest
from chapter9.concepts.testing_fixture_setup import CH9_INTEGRATION_TESTING

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_parent, aq_inner


class TestSetup(unittest.TestCase):
    layer = CH9_INTEGRATION_TESTING
    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ('Manager',))
        self.po = {}
        self.po['wftool'] = getToolByName(self.portal, 'portal_workflow')
        self.po['wftool'].setDefaultChain('simple_publication_workflow')
        self.portal.invokeFactory('Folder', 'folder', title=u"A folder")
        self.folder = self.portal['folder']
        name = self.folder.invokeFactory('Document', 'favorites', title=u"Favorite Guitars")
        self.obj = self.portal['folder']['favorites']
    def test_portal_folder(self):
        self.assertEqual(self.obj.getId(), 'favorites')
    def test_aquisition(self):
        self.assertEqual(aq_parent(self.obj),self.folder)
        self.assertEqual(aq_parent(aq_parent(self.obj)),self.portal)
    def test_acquisition_chain(self):
        containment_parent = aq_parent(aq_inner(self.obj))
        also_containment_parent = self.obj.aq_inner.aq_parent
        self.assertEqual(containment_parent, also_containment_parent)
        
        
        #name = self.folder.invokeFactory('Document', 'favorites', title=u"Favorite Guitars")
        #obj = portal[name]
        #import pdb; pdb.set_trace()
        #pass
        #print self.portal
        #import pdb; pdb.set_trace()
        
        #portal.folder = PortalFolder(portal)
        #name = portal.folder.invokeFactory('Document', 'favourites', RESPONSE)
    