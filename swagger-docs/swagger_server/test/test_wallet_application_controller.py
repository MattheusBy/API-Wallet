# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.v1_balance_body import V1BalanceBody  # noqa: E501
from swagger_server.models.v1_balance_body1 import V1BalanceBody1  # noqa: E501
from swagger_server.models.v1_transactions_body import V1TransactionsBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWalletApplicationController(BaseTestCase):
    """WalletApplicationController integration test stubs"""

    def test_a_piv1_balance_get(self):
        """Test case for a_piv1_balance_get

        
        """
        response = self.client.open(
            '//API/v1/balance',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_a_piv1_balance_post(self):
        """Test case for a_piv1_balance_post

        
        """
        body = V1BalanceBody1()
        response = self.client.open(
            '//API/v1/balance',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_a_piv1_balance_put(self):
        """Test case for a_piv1_balance_put

        
        """
        body = V1BalanceBody()
        response = self.client.open(
            '//API/v1/balance',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_a_piv1_transactions_post(self):
        """Test case for a_piv1_transactions_post

        
        """
        body = V1TransactionsBody()
        response = self.client.open(
            '//API/v1/transactions',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_a_piv1_transactions_transaction_id_delete(self):
        """Test case for a_piv1_transactions_transaction_id_delete

        
        """
        response = self.client.open(
            '//API/v1/transactions/{transaction_id}'.format(transaction_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_a_piv1_transactions_transaction_id_get(self):
        """Test case for a_piv1_transactions_transaction_id_get

        
        """
        response = self.client.open(
            '//API/v1/transactions/{transaction_id}'.format(transaction_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_a_piv1_transactions_transaction_id_put(self):
        """Test case for a_piv1_transactions_transaction_id_put

        
        """
        response = self.client.open(
            '//API/v1/transactions/{transaction_id}'.format(transaction_id=789),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
