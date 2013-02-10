arf-0.7

-------------------------------------------------------------------------------
Introduction

arf provides an abstraction of Abuse Reporting Format (ARF) emails, the 
standard format for feedback loop (FBL) reports as defined in 
https://tools.ietf.org/html/rfc5965.

-------------------------------------------------------------------------------
Installation

The arf module is shipped as a distutils package. To install the library,
unpace the distribution archive and run:

	$ python setup.py install

-------------------------------------------------------------------------------
Usage

ARF(string_representing_the_arf)

or more simply

process_arf("/path/to/arf_message")
