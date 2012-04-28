from zope.interface import Interface
from zope.interface import Attribute
from zope.interface import implements
from zope.interface import alsoProvides


class IBelievable(Interface):
    """An item which can be believed"""

class IUndeniable(IBelievable):
    """Something that is so believable it canot be denied"""

class IMessage(Interface):
    """A message being communicated"""
    def shout(noise_level=1):
        """Shout a message"""
    content = Attribute("Text of the message")

class StandardMessage(object):
    implements(IMessage)
    def __init__(self, content):
        self.content = content
    def shout(self, noise_level=1):
        print self.content * noise_level

class StrongMessage(StandardMessage):
    implements(IBelievable)

class ICommunicationFactory(Interface):
    """Callable which are able to provide communication devices"""

alsoProvides(StandardMessage, ICommunicationFactory)
alsoProvides(StrongMessage, ICommunicationFactory)
