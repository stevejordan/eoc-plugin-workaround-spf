import unittest
import spf_plugin
import email


class PluginTest(unittest.TestCase):

    _dummy_list = None

    def setUp(self):
        self._dummy_list = MockList()

    def test_plugin_interface(self):
        self.assertEquals(spf_plugin.PLUGIN_INTERFACE_VERSION, "1")

    def test_basic_message_process(self):
        new_email = spf_plugin.send_mail_to_subscribers_hook(
            self._dummy_list, "any old email"
        )
        self.assertIsNotNone(new_email)


class TestMessageTransformer(unittest.TestCase):

    _transformer = None
    _message = None
    _dummy_list = None

    def setUp(self):
        self._dummy_list = MockList()
        self._transformer = spf_plugin.MessageTransformer(
            self._dummy_list
        )

        with open('sample_msg') as message_in_file:
            self._message = email.message_from_file(message_in_file)

        self.assertIsNotNone(self._message)

    def test_from_transform(self):
        maillist_address = self._dummy_list.name
        transformed_message = self._transformer.transform(self._message)
        new_from_address = transformed_message.get('From')
        self.assertEquals(maillist_address, new_from_address)

    def test_original_sender_explanation(self):
        original_sender = self._message.get('From')
        transformed_message = self._transformer.transform(self._message)
        explanation_text = 'Originally sent by %s' % original_sender
        self.assertIn(
            explanation_text,
            transformed_message.get_payload()
        )


class SenderVerifyTest(unittest.TestCase):
    def test_dmarc_filter(self):
        verifier = spf_plugin.SenderVerify
        self.assertTrue(verifier.is_dmarc_restrictive_sender('steve@yahoo.com'))
        self.assertTrue(verifier.is_dmarc_restrictive_sender('steve@yahoo.co.uk'))
        self.assertFalse(verifier.is_dmarc_restrictive_sender('steve@example.com'))


class MockList(object):
    name = 'mock@list.com'

if __name__ == "__main__":
    unittest.main()
