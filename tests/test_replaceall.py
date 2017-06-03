# -*- coding: utf-8 -*-
import unittest

from .context import replaceall


class Test_replaceall(unittest.TestCase):
    def test_replaceall_remove(self):
        testcase = replaceall("Test@String!", "@!")
        self.assertEqual(testcase, "TestString")
    def test_replaceall_single(self):
        testcase = replaceall("Test@String!", "@!", "#")
        self.assertEqual(testcase, "Test#String#")
    def test_replaceall_list(self):
        charlist = ["!","@"]
        testcase = replaceall("Test@String!", charlist, "#")
        self.assertEqual(testcase, "Test#String#")
    def test_replaceall_string(self):
        testcase = replaceall("Test#!", "#", "String")
        self.assertEqual(testcase, "TestString!")
