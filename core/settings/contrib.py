# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from .base import *  # NOQA

# Extra installed apps
INSTALLED_APPS += (
    # any 3rd party apps
    'rest_framework',
    'rest_framework_gis',
    'rest_framework.authtoken',
    'social_django',
)

# 3rd party specific app settings

OAUTH2_PROVIDER = {
    'SCOPES': {
        'default': 'Read / write',
    },
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.SearchFilter',
                                'rest_framework.filters.OrderingFilter'),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication',
                                       'rest_framework.authentication.SessionAuthentication',
                                       'oauth2_provider.contrib.rest_framework.OAuth2Authentication',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'api.renderers.HOTExportApiRenderer',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    'DEFAULT_VERSION': '1.0',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

# OAuth login settings
SOCIAL_AUTH_OPENSTREETMAP_LOGIN_URL = '/osm/login/'
SOCIAL_AUTH_OPENSTREETMAP_KEY = os.getenv('OSM_API_KEY', '56e4WINtKE9BSzIU1JtYZufLRBp0La5zS6qHvei3')
SOCIAL_AUTH_OPENSTREETMAP_SECRET = os.getenv('OSM_API_SECRET', 'fcwFW11HB3zFDUQonYUTS3QJEQ5IAowWmISu2l93')
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/v3/#/exports/new/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/osm/error'
SOCIAL_AUTH_URL_NAMESPACE = 'osm'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_FORCE_EMAIL_VALIDATION = True
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'ui.pipeline.email_validation'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/osm/email_verify_sent/'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'ui.pipeline.require_email',
    'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.debug.debug',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details'
)
