import unittest

import sys
import time
import CacheConnector

class TestInitializer(unittest.TestCase):
    def testInitializerWithArgs(self):
        cc = CacheConnector.CacheConnector()
        cc[9] = 10
        self.assertEqual(cc.get(9, 100), 10)

        self.assertEqual(cc.pop(9, 'nonsense'), 10)
        self.assertEqual(cc.pop(9, 'nonsense'), 'nonsense')

    def testCallbackInvokations(self):
        cc = CacheConnector.CacheConnector()
        key, value = 'NUMA', 0x7485571
        cc.put(key, value)
        self.assertEqual(cc.get(key, value), value)

        __terminationToggle = False
        def dFuncUnchained(*args, **kwargs):
            global __terminationToggle
            for i in range(10):
                sys.stdout.write('#%d \033[92mSleeping.%s\033[00m\r'%(i, ' ' if i&1 else '.'))
                time.sleep(1)
            __terminationToggle = True
            

        self.assertEqual(cc.put(key, value, dFuncUnchained), None)

        # Expectation here is that dFuncUnchained should keep running
        # even after this test func exits, also __terminationToggle since it
        # is set to True at the end of dFuncUnchained, the assertion should hold
        self.assertEqual(__terminationToggle, False)
