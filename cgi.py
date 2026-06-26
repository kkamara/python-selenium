"""Compatibility shim for Python 3.13+ where stdlib cgi was removed.

Only the API used by this project stack (Django 4.0.x) is implemented.
"""

from email.message import Message


def parse_header(line):
    """Parse a Content-type like header.

    Returns (main_value, params_dict), matching the old cgi.parse_header shape.
    """
    message = Message()
    message["content-type"] = line

    main_value = message.get_content_type()
    params = {}

    # Skip the first item, which repeats the content type itself.
    for key, value in message.get_params()[1:]:
        params[key] = value

    return main_value, params
