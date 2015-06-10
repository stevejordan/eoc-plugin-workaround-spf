# sample enemies of carlotta plugin

import logging
import os

log_file_name = os.path.dirname(os.path.abspath(__file__)) + '/eoc_plugin.log'
logging.basicConfig(filename=log_file_name, level=logging.DEBUG)
log = logging.getLogger("plugin")

log.debug("plugin instantiated")

PLUGIN_INTERFACE_VERSION = "1"

def send_mail_to_subscribers_hook(list_, mail_text):
    log.debug(dir(list_))
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