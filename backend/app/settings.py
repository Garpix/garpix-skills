from garpixcms.settings import *  # noqa
from garpix_user.settings import GARPIX_USER_NOTIFY_EVENTS

DEBUG_FRONTEND = env.bool('DEBUG_FRONTEND', False)  # noqa

NOTIFY_EVENTS.update(GARPIX_USER_NOTIFY_EVENTS)  # noqa

MIGRATION_MODULES.update({  # noqa:F405
    'fcm_django': 'app.migrations.fcm_django',
    'social_django': 'app.migrations.social_django',
})

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'frontend', 'build', 'static-backend'),  # noqa
] + STATICFILES_DIRS  # noqa

GARPIX_USER = {
    'USE_EMAIL_CONFIRMATION': True,
    'USE_PHONE_CONFIRMATION': False,
    'USE_EMAIL_RESTORE_PASSWORD': True,
    'USE_PHONE_RESTORE_PASSWORD': False,
    'CONFIRM_EMAIL_CODE_LENGTH': 25,
    'CONFIRM_EMAIL_CODE_LIFE_TIME': 1,
    'USE_PREREGISTRATION_EMAIL_CONFIRMATION': False,
    'USE_PREREGISTRATION_PHONE_CONFIRMATION': False,
    'USE_EMAIL_LINK_CONFIRMATION': True,
    'EMAIL_CONFIRMATION_LINK_REDIRECT': '/email_confirmation'
}

TEST_COVERAGE_RATE = 40
