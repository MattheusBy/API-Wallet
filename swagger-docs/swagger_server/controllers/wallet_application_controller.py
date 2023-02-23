import connexion
import six

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.v1_balance_body import V1BalanceBody  # noqa: E501
from swagger_server.models.v1_balance_body1 import V1BalanceBody1  # noqa: E501
from swagger_server.models.v1_transactions_body import V1TransactionsBody  # noqa: E501
from swagger_server import util


def a_piv1_balance_get():  # noqa: E501
    """a_piv1_balance_get

    return information about user&#x27;s balance # noqa: E501


    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def a_piv1_balance_post(body):  # noqa: E501
    """a_piv1_balance_post

    set balance after register # noqa: E501

    :param body: contains user&#x27;s balance
    :type body: dict | bytes

    :rtype: V1BalanceBody1
    """
    if connexion.request.is_json:
        body = V1BalanceBody1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def a_piv1_balance_put(body):  # noqa: E501
    """a_piv1_balance_put

    change current user&#x27;s balance # noqa: E501

    :param body: contains new user&#x27;s balance
    :type body: dict | bytes

    :rtype: V1BalanceBody
    """
    if connexion.request.is_json:
        body = V1BalanceBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def a_piv1_transactions_post(body):  # noqa: E501
    """a_piv1_transactions_post

    create new user&#x27;s entry # noqa: E501

    :param body: should contains category, description, kind, amount
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    if connexion.request.is_json:
        body = V1TransactionsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def a_piv1_transactions_transaction_id_delete(transaction_id):  # noqa: E501
    """a_piv1_transactions_transaction_id_delete

    return information about user&#x27;s balance # noqa: E501

    :param transaction_id: Transaction ID
    :type transaction_id: int

    :rtype: InlineResponse2003
    """
    return 'do some magic!'


def a_piv1_transactions_transaction_id_get(transaction_id):  # noqa: E501
    """a_piv1_transactions_transaction_id_get

    return information about user&#x27;s balance # noqa: E501

    :param transaction_id: Transaction ID
    :type transaction_id: int

    :rtype: InlineResponse2003
    """
    return 'do some magic!'


def a_piv1_transactions_transaction_id_put(transaction_id):  # noqa: E501
    """a_piv1_transactions_transaction_id_put

    return information about user&#x27;s balance # noqa: E501

    :param transaction_id: Transaction ID
    :type transaction_id: int

    :rtype: InlineResponse2003
    """
    return 'do some magic!'
