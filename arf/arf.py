""" arf.py - Class abstract for representing ARFs as defined in RFC5965
	http://www.faqs.org/rfcs/rfc5965.html
"""
from email.parser import Parser
from email.message import Message

class ARF(object):
	""" ARF abstract
		@param arf_source - string representing the ARF source
		@core - payload of the ARF message
		@notification - the notification or 'friendly' portion of the ARF if any
		@feedback_report - the required and option fb fields, see FeedbackReport
		@original - the rfc822 headers of the original message or possibly
			the complete message, represented as email.message
	"""
	def __init__(self, arf_source):
		self.message = Parser().parsestr(arf_source)
		self.core = self.message.get_payload()
		self.notification = self.core[0].get_payload()
		self.feedback_report = Parser(FeedbackReport).parsestr(
			self.core[1].get_payload()[0].as_string())
		self.original = self.core[2].get_payload()[0]

class FeedbackReport(Message):
	""" FeedbackReport - Convenience class with methods corresponding
		to the required and optional ARF fields as defined in RFC5965
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

def process_arf(source_file):
	f = open(source_file, 'r').read()
	return ARF(f)
