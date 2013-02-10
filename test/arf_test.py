#!/usr/bin/env python
# tests for the arf package
import sys
sys.path.insert(0, "../pkg/")
import unittest
import arf

class ARFTest(unittest.TestCase):
	def setUp(self):
		unittest.TestCase.setUp(self)
		self.arf0 = arf.proc_arf("./ex/maximum_info.txt")
	def tearDown(self):
		unittest.TestCase.tearDown(self)
	def testTrue(self):
		self.assertEqual(self.arf0.feedback_report.get_feedback_type(), "abuse")
		self.assertEqual(self.arf0.feedback_report.get_user_agent(),
			"SomeGenerator/1.0")
		self.assertEqual(self.arf0.feedback_report.get_version(), "1")
		self.assertEqual(self.arf0.feedback_report.get_original_mail_from(),
			"<somespammer@example.net>")
		self.assertEqual(self.arf0.feedback_report.get_original_envelope_id(),
			None)
		self.assertEqual(self.arf0.feedback_report.get_original_rcpt_to(),
			"<user@example.com>")
		self.assertEqual(self.arf0.feedback_report.get_arrival_date(),
			"Thu, 8 Mar 2005 14:00:00 EDT")
		self.assertEqual(self.arf0.feedback_report.get_reporting_mta(),
			"dns; mail.example.com")
		self.assertEqual(self.arf0.feedback_report.get_source_ip(),
			"192.0.2.1")
		self.assertEqual(self.arf0.feedback_report.get_reported_domain(),
			"example.net")
		self.assertEqual(self.arf0.feedback_report.get_reported_uri(),
			"http://example.net/earn_money.html")

if __name__ == "__main__":
	unittest.main()
