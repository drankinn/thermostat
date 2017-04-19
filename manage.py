import signal
from optparse import OptionParser

import web
import sys


def run_application():
    urls = (
        '/list', 'service.views.thermostat.List',
        '/new', 'service.views.thermostat.New',
        '/view/(.+)?', 'service.views.thermostat.View',
        '/edit', 'service.views.thermostat.Edit',
        '/delete/(.+)?', 'service.views.thermostat.Delete',

    )

    app = web.application(urls, globals())
    app.run()


def run_tests():
    """
    Runs Code Coverage using pytest and pytest-cov
    """
    import sys
    from pytest import main
    args = [
        'tests',
        '--cov=service',
        '--cov-fail-under=50',
        '--cov-report', 'term',
        '-sv'
    ]
    try:
        exit_code = main(args)
    except Exception as ex:
        print(ex)
        exit_code = 1
    sys.exit(exit_code)


def handle_signals(signum, frame):
    print("exiting with code {}".format(signum))
    sys.exit(0)


def main():
    """
    Main entry point into the application. Looks for arguments
    passed in to decide to run tests or run the application
    """
    usage = "usage: python manage.py [run|test]"
    parser = OptionParser(usage)
    (options, args) = parser.parse_args()
    signal.signal(signal.SIGTERM, handle_signals)

    if 'test' in args or 'tests' in args:
        print('Running tests')
        print('--------------------------------')
        run_tests()
    else:
        run_application()


if __name__ == "__main__":
    main()
