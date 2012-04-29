import unittest2 as unittest
from testing_fixture_setup import CH9_INTEGRATION_TESTING

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.content.document import ATDocument
from Acquisition import aq_parent, aq_inner, aq_base, aq_chain, aq_get


class TestContainment(unittest.TestCase):
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
    def test_more_aq_examples(self):
        acquiring = self.folder
        self.assertEqual(aq_base(acquiring), aq_base(self.portal['folder']))        
class TestAcquisiton(unittest.TestCase):
    layer = CH9_INTEGRATION_TESTING
    def setUp(self):
         self.portal = self.layer['portal']
         setRoles(self.portal, TEST_USER_ID, ('Manager',))
         self.portal.invokeFactory('Folder', 'folder', title=u"A folder")
         self.folder = self.portal['folder']
         self.portal.invokeFactory('Document', 'favorites')
         favorites = self.portal['favorites']
    def test_acquisition_chain(self):
        aq_chain_ex1 = aq_chain(self.portal.favorites)
        aq_chain_ex2 = aq_chain(self.folder.favorites)
        self.assertTrue(len(aq_chain_ex1) < len(aq_chain_ex2))
    def test_aqget(self):
        '''Explicitly aquire request variable from context.'''
        from ZPublisher.HTTPRequest import HTTPRequest
        request = aq_get(self.portal, 'REQUEST')
        self.assertTrue(isinstance(request, HTTPRequest))
    def test_manual_aq_setting(self):
        '''
        Test __of__ operator on an object that is not connected
        to an acquisition scheme
        '''
        temp_document = ATDocument('temp_document')
        chain = aq_chain(temp_document)
        self.assertEquals(len(chain), 1)
        chain1 = aq_chain(temp_document.__of__(self.portal))
        self.assertEquals(len(chain1), 4)
class TestPathTraversal(unittest.TestCase):
    layer = CH9_INTEGRATION_TESTING
    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ('Manager',))
        self.portal.invokeFactory('Folder', 'guitars')
        self.portal['guitars'].invokeFactory('Document','fender')
    def test_unrestricted_traverse(self):
        traverse_test = self.portal.unrestrictedTraverse('guitars/fender')
        self.assertTrue(isinstance(traverse_test, ATDocument))
    def test_restricted_traverse(self):
        traverse_path = '/'.join(self.portal['guitars']['fender'].getPhysicalPath())
        out = self.portal.restrictedTraverse(traverse_path)
        self.assertTrue(isinstance(out, ATDocument))
