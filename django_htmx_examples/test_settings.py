from django.contrib.auth.hashers import BasePasswordHasher

from .settings import *  # noqa

# An in-memory database should be good enough for now.
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}


# Make sure that tests are never sending real emails.
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"


PASSWORD_HASHERS = ("project.testing_settings.SimplePasswordHasher",)

# Whitenoise does not play well with tz_detect because tests don't run collectstatic.
# Override back to the default storage for testing.
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# This eliminates the warning about a missing staticfiles directory.
WHITENOISE_AUTOREFRESH = True