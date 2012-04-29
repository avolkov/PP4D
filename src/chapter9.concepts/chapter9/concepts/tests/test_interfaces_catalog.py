import unittest2 as unittest
from testing_fixture_setup import CH9_INTEGRATION_TESTING

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from Products.CMFCore.utils import getToolByName

class TestInterfacesCatalog(unittest.TestCase):
    layer = CH9_INTEGRATION_TESTING
    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ('Manager',))
        self.wftool = getToolByName(self.portal, 'portal_workflow')
        self.wftool.setDefaultChain('simple_publication_workflow')
        self.portal.invokeFactory('Folder', 'folder', title=u"A folder")
        folder = self.portal['folder']
        folder.invokeFactory('Document', 'favorites', title=u"Favorite guitars")
        folder.invokeFactory('Folder', 'guitars', title=u"Guitars")
        ##Populate portal
        folder['guitars'].invokeFactory('News Item', 'strat', title=u"New Strat!")
        folder['guitars'].invokeFactory('News Item', 'tele', title=u"New Tele!", subject=('Fender',))
        folder['guitars'].invokeFactory('News Item', 'lp', title=u"News Les Paul", subject=('Guitars',))
        folder['guitars'].invokeFactory('Document', 'fender', title=u"Fender", subject=('Fender', 'Guitars',))
        folder['guitars'].invokeFactory('Image', 'jagstang', title=u"Jagstang", subject=('Fender', 'Guitars',))
        folder['guitars'].invokeFactory('Folder', 'basses', title=u"Basses")
        folder['guitars']['basses'].invokeFactory('Document', 'pbass', title=u"Precision bass")
        ##publish some of the item
        self.wftool.doActionFor(folder['guitars']['strat'], 'publish')
        self.wftool.doActionFor(folder['guitars']['lp'], 'publish')
    def test_manual_traverse(self):
        folder = self.portal['folder']
        self.assertEquals(['favorites', 'guitars'], sorted(folder.keys()))
        folder_contents = folder.values()
        self.assertEquals(folder_contents[0].portal_type, 'Document')
        self.assertEquals(folder_contents[1].Title(), 'Guitars')
    def test_catalog_traverse(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        results = catalog({'portal_type':'News Item', 'review_state':'published',})
        self.assertEquals(results[0].getPath(), '/plone/folder/guitars/strat')
        self.assertEquals(results[1].getPath(), '/plone/folder/guitars/lp')
        for brain in results:
            self.assertEquals(brain.getURL(), brain.getObject().absolute_url())
        results_keyword_index = catalog({'portal_type':('Document','News Item'), 'Subject':('Guitars', 'Fender')})
        result_id = sorted([ k.getId for k in results_keyword_index])
        self.assertEqual(['fender', 'lp', 'tele'], result_id)