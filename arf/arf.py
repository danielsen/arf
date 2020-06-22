# arf.py - Abstract classes for representing Abuse Reporting Format messages
# Copyright (C) 2020 Dan Nielsen <dnielsen@fastmail.fm>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
""" arf.py - Abstract class for representing Abuse Reporting Format (ARF)
    messages as defined in RFC5965.
    http://www.faqs.org/rfcs/rfc5965.html
"""
import json
from email.parser import Parser
from email.message import Message

class ARFMessage(object):
    """ ARF abstract
    """

    def __init__(self, arf_source):
        self._message = Parser().parsestr(arf_source)

    def _get_part(self, subtype):
        for part in self._message.walk():
            if part.get_content_subtype() == subtype:
                return part

        return None

    def _header_to_camelcase(self, field):

        def camelcase():
            while True:
                yield str.capitalize

        c = camelcase()
        return ''.join((next(c)(x) for x in field.split('-')))

    def _clean_field_value(self, field_value):
        return field_value.replace('\n', '').replace('\t', ' ')

    def _serialize_headers(self, source_headers):
        target_headers = {}
        for field, value in source_headers:
            clean_value = self._clean_field_value(value)
            json_field = self._header_to_camelcase(field)
            if json_field in target_headers:
                if isinstance(target_headers[json_field], list):
                    target_headers[json_field].append(clean_value)
                else:
                    target_headers[json_field] = [target_headers[json_field], 
                        clean_value]
            else:
                target_headers[json_field] = clean_value

        return target_headers

    def get_message_headers(self):
        """ Returns ARF message headers """
        return self._message.items()

    def get_descriptive_payload(self):
        """ Returns the descriptive or 'friendly' part of the message """
        return self._message.get_payload()[0].get_payload()

    def get_feedback_report(self):
        """ Returns the message/feedback-report part as a FeedbackReport """
        part = self._get_part('feedback-report')
        if part:
            return Parser(FeedbackReport).parsestr(
                part.get_payload()[0].as_string())

    def get_original_message_headers(self):
        """ Returns headers from the orginal message """
        part = self._get_part('rfc822')
        if part:
            return part.get_payload()[0].items()

    def get_original_message_payload(self):
        """ Returns the content of the original message """
        part = self._get_part('rfc822')
        if part:
            return part.get_payload()[0].as_string()

    def serialize_message_headers_to_json(self):
        """ Returns the ARF message headers as a JSON string """
        return json.dumps(self._serialize_headers(self.get_message_headers()))

    def serialize_original_message_headers_to_json(self):
        """ Returns the original message headers as a JSON string """
        return json.dumps(self._serialize_headers(
            self.get_original_message_headers()))

    def serialize_report(self):
        target = {}
        target['MessageHeaders'] = self._serialize_headers(
            self.get_message_headers())
        try:
            target['OriginalMessageHeaders'] = self._serialize_headers(
                self.get_original_message_headers())
        except Exception:
            target['OriginalMessageHeaders'] = {}

        try:
            target['FeedbackReport'] = self._serialize_headers(
                self.get_feedback_report().items())
        except Exception:
            target['FeedbackReport'] = {}

        return target

    def serialize_report_to_json(self):
        """ Returns the message headers and feedback-report as a JSON string """
        return json.dumps(self.serialize_report())


class FeedbackReport(Message):
    """ FeedbackReport - Convenience class with methods corresponding
        to the required and optional ARF fields as defined in RFC5965
        for mime type feedback-report
    """

    def get_feedback_type(self):
        return self.get('Feedback-Type')

    def get_user_agent(self):
        return self.get('User-Agent')

    def get_version(self):
        return self.get('Version')

    def get_original_envelope_id(self):
        return self.get('Original-Envelope-Id')

    def get_original_mail_from(self):
        return self.get('Original-Mail-From')

    def get_arrival_date(self):
        return self.get('Arrival-Date')

    def get_reporting_mta(self):
        return self.get('Reporting-MTA')

    def get_source_ip(self):
        return self.get('Source-IP')

    def get_incidents(self):
        return self.get('Incidents')

    def get_authentication_results(self):
        return self.get('Authentication-Results')

    def get_original_rcpt_to(self):
        return self.get('Original-Rcpt-To')

    def get_reported_domain(self):
        return self.get('Reported-Domain')

    def get_reported_uri(self):
        return self.get('Reported-URI')


def load_arf(source_file):
    with open(source_file, 'r') as file_handle:
        return ARFMessage(file_handle.read())
