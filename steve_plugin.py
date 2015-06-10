# sample enemies of carlotta plugin

import logging
logging.basicConfig(filename='eoc_plugin.log', level=logging.DEBUG)
log = logging.getLogger("plugin")

log.debug("plugin instantiated")

PLUGIN_INTERFACE_VERSION = "1"

def send_mail_to_subscribers_hook(mail_text):
    log.debug("received the following from eoc:\n\n%s" % mail_text)
    return mail_text


def test():
    print "running tests..."
    assert PLUGIN_INTERFACE_VERSION == "1"
    new_email = send_mail_to_subscribers_hook("any old email")
    assert new_email != None
    print "all tests passed!"
    
if __name__ == "__main__":
    test()