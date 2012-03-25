from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig

from zope.configuration.xmlconfig import ConfigurationError
class OptiluxTheme(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        #Load ZCML
        import optilux.theme
        try:
            #import pdb; pdb.set_trace()
            xmlconfig.file('configure.zcml', optilux.theme, context=configurationContext)
        except ConfigurationError, e:
            xmlconfig.file('configure.zcml', optilux.theme, context=configurationContext)
            #import pdb; pdb.set_trace()
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'optilux.theme:default')

OPTILUX_THEME_FIXTURE = OptiluxTheme()
OPTILUX_THEME_INTEGRATION_TESTING = IntegrationTesting(bases=(OPTILUX_THEME_FIXTURE,), name="OptiluxTheme:Integration")
OPTILUX_THEME_FUNCTIONAL_TESTING = FunctionalTesting(bases=(OPTILUX_THEME_FIXTURE,), name="OptiluxTheme:Functional")