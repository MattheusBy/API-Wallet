# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from swagger_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_auth_users_activation_post(self):
        """Test case for auth_users_activation_post

        
        """
        body = UsersActivationBody()
        response = self.client.open(
            '//auth/users/activation',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_users_get(self):
        """Test case for auth_users_get

        
        """
        response = self.client.open(
            '//auth/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_users_me_delete(self):
        """Test case for auth_users_me_delete

        
        """
        body = UsersMeBody1()
        response = self.client.open(
            '//auth/users/me',
            method='DELETE',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_users_me_get(self):
        """Test case for auth_users_me_get

        
        """
        response = self.client.open(
            '//auth/users/me',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_users_me_patch(self):
        """Test case for auth_users_me_patch

        
        """
        body = UsersMeBody2()
        response = self.client.open(
            '//auth/users/me',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_users_me_put(self):
        """Test case for auth_users_me_put

        
        """
        body = UsersMeBody()
        response = self.client.open(
            '//auth/users/me',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_users_post(self):
        """Test case for auth_users_post

        
        """
        body = AuthUsersBody()
        response = self.client.open(
            '//auth/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_users_resend_activation_post(self):
        """Test case for auth_users_resend_activation_post

        
        """
        body = UsersResendActivationBody()
        response = self.client.open(
            '//auth/users/resend_activation',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_users_reset_password_post(self):
        """Test case for auth_users_reset_password_post

        
        """
        body = UsersResetPasswordBody()
        response = self.client.open(
            '//auth/users/reset_password',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_users_set_password_post(self):
        """Test case for auth_users_set_password_post

        
        """
        body = UsersSetPasswordBody()
        response = self.client.open(
            '//auth/users/set_password',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
