arf provides simple abstract classes for representing and inspecting Abuse
Reporting Format (ARF) messages as defined in 
http://www.faqs.org/rfcs/rfc5965.html

### Overview 
There are two main classes included in this module; `ARFMessage` and 
`FeedbackReport`.

##### ARFMessage
Objects derived from `ARFMessage` represent a full feedback report as defined
in section 2 of [rfc5965](http://www.faqs.org/rfcs/rfc5965.html). Convenience
methods are provided for accessing the various sub-parts of the full message.

##### FeedbackReport
Objects derived from `FeedbackReport` represent the `message/feedback-report`
part of the full message as defined in [rfc5965](http://www.faqs.org/rfcs/rfc5965.html). Convenience methods are provided to access the required and optional
fields.

### Installation
arf is provided as a distutils package. To install, clone the repository and
run 

    $ python setup.py install

### Usage

    import arf
    arf.ARFMessage(string representing the message)

or
    
    import arf
    arf.load_arf("/path/to/arf.file")

### Testing
To run package unit tests

    $ cd test
    $ python arf_test.py
