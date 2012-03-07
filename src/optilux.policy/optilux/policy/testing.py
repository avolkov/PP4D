from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from zope.configuration import xmlconfig

class OptiluxPolicy(PloneSandboxLayer):
    def setUpZope(self, app, configurationContext):
        #load zcml
        import optilux.policy
        xmlconfig.file('configure.zcml', optilux.policy, context=configurationContext)
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'optilux.policy:default')

OPTILUX_POLICY_FIXTURE = OptiluxPolicy()
OPTILUX_POLICY_INTEGRATION_TESTING = IntegrationTesting(bases=(OPTILUX_POLICY_FIXTURE,), name="Optilux:Integration")
