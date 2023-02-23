# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.jwt_create_body import JwtCreateBody  # noqa: E501
from swagger_server.models.jwt_verify_body import JwtVerifyBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestJWTController(BaseTestCase):
    """JWTController integration test stubs"""

    def test_auth_jwt_create_post(self):
        """Test case for auth_jwt_create_post

        
        """
        body = JwtCreateBody()
        response = self.client.open(
            '//auth/jwt/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_jwt_verify_post(self):
        """Test case for auth_jwt_verify_post

        
        """
        body = JwtVerifyBody()
        response = self.client.open(
            '//auth/jwt/verify',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
