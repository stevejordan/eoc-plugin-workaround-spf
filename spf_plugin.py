# sample enemies of carlotta plugin

import logging
import os
import email

log_file_name = os.path.dirname(os.path.abspath(__file__)) + '/eoc_plugin.log'
logging.basicConfig(filename=log_file_name, level=logging.DEBUG)
log = logging.getLogger("plugin")

log.debug("plugin instantiated")

PLUGIN_INTERFACE_VERSION = "1"

def send_mail_to_subscribers_hook(list_, mail_text):
    log.debug(dir(list_))
    log.debug("received the following from eoc:\n\n%s" % mail_text)
    message = email.message_from_string(mail_text)
    if SenderVerify.is_dmarc_restrictive_sender(message):
        transformer = MessageTransformer(list_)
        transformer.transform(message)
    return mail_text

class MessageTransformer(object):
    _list = None
    _message = None
    _original_sender = None

    def __init__(self, list_):
        self._list = list_

    def transform(self, message):
        self._message = message
        self._original_sender = message.get('From')
        self._replace_from_field_with_list_address()
        self._add_explanation_text()
        return self._message
    
    def _replace_from_field_with_list_address(self):
        list_address = self._list.name
        self._message.replace_header('From', list_address)
    
    def _add_explanation_text(self):
        explanation = '''
        Originally sent by %s
        ''' % self._original_sender
        self._message.set_payload(
            explanation + self._message.get_payload()
        )
        
class SenderVerify(object):
    '''class used to perform tests on sender to determine if action need be taken'''
    dmarc_restrictive_domains = [
        'yahoo.com', 'yahoo.co.uk'
    ]
    @classmethod
    def is_dmarc_restrictive_sender(cls, sender_address):
        for domain in cls.dmarc_restrictive_domains:
            if domain in sender_address:
                return True
        return False