import connexion
import six

from swagger_server.models.auth_users_body import AuthUsersBody  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.users_activation_body import UsersActivationBody  # noqa: E501
from swagger_server.models.users_me_body import UsersMeBody  # noqa: E501
from swagger_server.models.users_me_body1 import UsersMeBody1  # noqa: E501
from swagger_server.models.users_me_body2 import UsersMeBody2  # noqa: E501
from swagger_server.models.users_resend_activation_body import UsersResendActivationBody  # noqa: E501
from swagger_server.models.users_reset_password_body import UsersResetPasswordBody  # noqa: E501
from swagger_server.models.users_set_password_body import UsersSetPasswordBody  # noqa: E501
from swagger_server import util


def auth_users_activation_post(body):  # noqa: E501
    """auth_users_activation_post

    activate new user. Realize in frontend (Djoser docs https://djoser.readthedocs.io/en/latest/base_endpoints.html#user-create) # noqa: E501

    :param body: contains user&#x27;s id
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UsersActivationBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_users_get():  # noqa: E501
    """auth_users_get

    return all users. Allows admin only # noqa: E501


    :rtype: InlineResponse201
    """
    return 'do some magic!'


def auth_users_me_delete(body):  # noqa: E501
    """auth_users_me_delete

    delete current user # noqa: E501

    :param body: contains user&#x27;s data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = UsersMeBody1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_users_me_get():  # noqa: E501
    """auth_users_me_get

    return information about current user # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def auth_users_me_patch(body):  # noqa: E501
    """auth_users_me_patch

    update user&#x27;s email or other required fields # noqa: E501

    :param body: contains user&#x27;s data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = UsersMeBody2.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_users_me_put(body):  # noqa: E501
    """auth_users_me_put

    update user&#x27;s email and others required fields # noqa: E501

    :param body: contains user&#x27;s data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = UsersMeBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_users_post(body):  # noqa: E501
    """auth_users_post

    create new user # noqa: E501

    :param body: contains user&#x27;s data
    :type body: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        body = AuthUsersBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_users_resend_activation_post(body):  # noqa: E501
    """auth_users_resend_activation_post

    resend to user email link to activate account # noqa: E501

    :param body: contains user&#x27;s id
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UsersResendActivationBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_users_reset_password_post(body):  # noqa: E501
    """auth_users_reset_password_post

    reset user&#x27;s password # noqa: E501

    :param body: contains user&#x27;s data
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UsersResetPasswordBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_users_set_password_post(body):  # noqa: E501
    """auth_users_set_password_post

    set new user&#x27;s password # noqa: E501

    :param body: contains user&#x27;s data
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UsersSetPasswordBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
