`arf-mime` provides simple abstract classes for representing and inspecting Abuse
Reporting Format (ARF) messages as defined in 
http://www.faqs.org/rfcs/rfc5965.html

### Overview 
There are two main classes included in this module; `ARFMessage` and 
`FeedbackReport`.

##### ARFMessage
Objects derived from `ARFMessage` represent a full feedback report as defined
in [Section 2 of RFC 5965](https://tools.ietf.org/html/rfc5965#section-2). Convenience
methods are provided for accessing the various sub-parts of the full message.

##### FeedbackReport
Objects derived from `FeedbackReport` represent the `message/feedback-report`
part of the full message as defined in [Section 3 of RFC 5965](https://tools.ietf.org/html/rfc5965#section-3). Convenience methods are provided to access the required and optional
fields.

### Installation
`arf-mime` is provided through PyPi and can be install with `pip`. Run 

    $ pip install arf-mime

### Usage

    import arf
    arf.ARFMessage(string representing the message)

or
    
    import arf
    arf.load_arf("/path/to/arf.file")

### Contributing and Reporting Issues

Bug reports, feature requests, and contributions are all welcome. Please open issues ans PRs as
needed. 
