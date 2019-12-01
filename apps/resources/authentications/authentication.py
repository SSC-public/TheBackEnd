""""
Provides token authentications policies.
"""

import datetime

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from ..constants.constants import api_tokens

__all__ = ['ResourceTokenAuthentication']


def get_authorization_header(request):
    """
    get api token from request header
    """

    api_token = request.META.get('APITOKEN', '')

    return api_token


class ResourceTokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        api_token = get_authorization_header(request)

        if not api_token or api_token != api_tokens.api_token:
            raise AuthenticationFailed("Wrong Or Missing Api Token!" + "====" + api_token)

        return None