# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, username: str=None, email: str=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param id: The id of this InlineResponse200.  # noqa: E501
        :type id: int
        :param username: The username of this InlineResponse200.  # noqa: E501
        :type username: str
        :param email: The email of this InlineResponse200.  # noqa: E501
        :type email: str
        """
        self.swagger_types = {
            'id': int,
            'username': str,
            'email': str
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'email': 'email'
        }
        self._id = id
        self._username = username
        self._email = email

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this InlineResponse200.


        :return: The id of this InlineResponse200.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this InlineResponse200.


        :param id: The id of this InlineResponse200.
        :type id: int
        """

        self._id = id

    @property
    def username(self) -> str:
        """Gets the username of this InlineResponse200.


        :return: The username of this InlineResponse200.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this InlineResponse200.


        :param username: The username of this InlineResponse200.
        :type username: str
        """

        self._username = username

    @property
    def email(self) -> str:
        """Gets the email of this InlineResponse200.


        :return: The email of this InlineResponse200.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this InlineResponse200.


        :param email: The email of this InlineResponse200.
        :type email: str
        """

        self._email = email