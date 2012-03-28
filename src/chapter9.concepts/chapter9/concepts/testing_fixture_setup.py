from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from zope.configuration import xmlconfig

class ZopeExamples(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    def setUpZope(self, app, configurationContext):
        import chapter9.concepts
        xmlconfig.file('configure.zcml', chapter9.concepts, context=configurationContext)
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'chapter9.concepts:default')
CH9_FIXTURE = ZopeExamples()
CH9_INTEGRATION_TESTING = IntegrationTesting(bases=(CH9_FIXTURE, ), name="Chapter9:Integration")