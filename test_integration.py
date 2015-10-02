import sys
import os
import unittest

# requires git submodule init
sys.path.insert(0, './eoc')
from eocTests import IncomingBase, DOTDIR

PLUGIN = 'spf_plugin.py'
PLUGIN_DIR = '%s/plugins' % DOTDIR

class PluginBaseTest(IncomingBase):
    
    def setUp(self):
        super(PluginBaseTest, self).setUp()
        self._add_plugin_symlink()
        
    def _add_plugin_symlink(self):
        os.mkdir(PLUGIN_DIR)
        os.symlink(PLUGIN, '%s/%s' % (PLUGIN_DIR, PLUGIN))
        
    def tearDown(self):
        pass
    
class PluginIntegrationTests(PluginBaseTest):
    
    def test_plain_text(self):
        self.assertTrue(True)
        
if __name__ == "__main__":
    unittest.main()