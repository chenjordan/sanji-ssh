#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os
import sys
import unittest
import logging

from sanji.connection.mockup import Mockup
from sanji.message import Message

logger = logging.getLogger()

try:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')
    from ssh import Ssh
except ImportError as e:
    print "Please check the python PATH for import test module. (%s)" \
        % __file__
    exit(1)


class TestSshClass(unittest.TestCase):

    def setUp(self):
        self.ssh = Ssh(connection=Mockup())

    def tearDown(self):
        self.ssh.stop()
        self.ssh = None

    def test_get(self):
        def resp(code=200, data=None):
            self.assertEqual(code, 200)
            self.assertEqual(data, {"message": self.ssh.message})
        self.ssh.get(message=None, response=resp, test=True)

    def test_put(self):
        pass

    def test_post(self):
        pass

    def test_delete(self):
        pass

if __name__ == "__main__":
    unittest.main()
