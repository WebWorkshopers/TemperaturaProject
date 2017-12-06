"""A temperature satisfaction logging app for offices."""

import signal as _signal

from tornado.ioloop import IOLoop as _IOLoop
from tornado.log import enable_pretty_logging as _enable_pretty_logging
from tornado.web import Application as _Application


def get_app():
    """Return a new temproject application."""
    return _Application(debug=True)


def run():
    """Run the temproject application."""
    _signal.signal(
        _signal.SIGINT,
        lambda _, __: _IOLoop.current().stop()
    )

    get_app().listen(8888)
    _enable_pretty_logging()
    _IOLoop.current().start()

