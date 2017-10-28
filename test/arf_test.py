#!/usr/bin/env python
# tests for the arf package
import sys
sys.path.insert(0, "../arf/")
import unittest
import arf

class ARFTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.message = arf.load_arf("./resources/sample_arf_message.txt")

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_header_to_camelcase(self):
        self.assertEqual(self.message._header_to_camelcase("Return-Path"),
            "ReturnPath")

    def test_get_message_headers(self):
        message_headers = self.message.get_message_headers()
        self.assertEqual(len(message_headers), 8)

        received_headers = [i for i in message_headers if 'Received' in i]
        self.assertEqual(len(received_headers), 2)

    def test_get_feedback_report(self):
        feedback_report = self.message.get_feedback_report()
        self.assertEqual(feedback_report.get_feedback_type(), "abuse")
        self.assertEqual(feedback_report.get_user_agent(),
            "SomeGenerator/1.0")
        self.assertEqual(feedback_report.get_version(), "1")
        self.assertEqual(feedback_report.get_original_mail_from(),
            "<somespammer@example.net>")
        self.assertEqual(feedback_report.get_original_envelope_id(),
            None)
        self.assertEqual(feedback_report.get_original_rcpt_to(),
            "<user@example.com>")
        self.assertEqual(feedback_report.get_arrival_date(),
            "Thu, 8 Mar 2005 14:00:00 EDT")
        self.assertEqual(feedback_report.get_reporting_mta(),
            "dns; mail.example.com")
        self.assertEqual(feedback_report.get_source_ip(),
            "192.0.2.1")
        self.assertEqual(feedback_report.get_reported_domain(),
            "example.net")
        self.assertEqual(feedback_report.get_reported_uri(),
            "http://example.net/earn_money.html")

    def test_get_original_message_headers(self):
        message_headers = self.message.get_original_message_headers()
        self.assertEqual(len(message_headers), 8)
        

if __name__ == "__main__":
    unittest.main()
