import connexion
import six

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.jwt_create_body import JwtCreateBody  # noqa: E501
from swagger_server.models.jwt_verify_body import JwtVerifyBody  # noqa: E501
from swagger_server import util


def auth_jwt_create_post(body):  # noqa: E501
    """auth_jwt_create_post

    create JWT-Token for user # noqa: E501

    :param body: contains user&#x27;s data
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = JwtCreateBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_jwt_verify_post(body):  # noqa: E501
    """auth_jwt_verify_post

    verify JWT-Token for user # noqa: E501

    :param body: contains user&#x27;s data
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = JwtVerifyBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
