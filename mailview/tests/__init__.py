from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG=True,
        INSTALLED_APPS=(
            'mailview',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            },
        },
        ROOT_URLCONF='mailview.tests.urls',
    )


from mailview.tests.tests import *  # NOQA


def run():
    import sys
    from django.test.utils import get_runner

    runner = get_runner(settings)()
    failures = runner.run_tests(('mailview',))
    sys.exit(failures)