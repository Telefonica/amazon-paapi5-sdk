# coding: utf-8

"""
  Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.

  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at

      http://www.apache.org/licenses/LICENSE-2.0

  or in the "license" file accompanying this file. This file is distributed
  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
  express or implied. See the License for the specific language governing
  permissions and limitations under the License.
"""


"""
    ProductAdvertisingAPI

    https://webservices.amazon.com/paapi5/documentation/index.html  # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from paapi5_python_sdk.models.offer_price import OfferPrice  # noqa: F401,E501
from paapi5_python_sdk.models.unit_based_attribute import UnitBasedAttribute  # noqa: F401,E501


class DurationPrice(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'price': 'OfferPrice',
        'duration': 'UnitBasedAttribute'
    }

    attribute_map = {
        'price': 'Price',
        'duration': 'Duration'
    }

    def __init__(self, price=None, duration=None):  # noqa: E501
        """DurationPrice - a model defined in Swagger"""  # noqa: E501

        self._price = None
        self._duration = None
        self.discriminator = None

        if price is not None:
            self.price = price
        if duration is not None:
            self.duration = duration

    @property
    def price(self):
        """Gets the price of this DurationPrice.  # noqa: E501


        :return: The price of this DurationPrice.  # noqa: E501
        :rtype: OfferPrice
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this DurationPrice.


        :param price: The price of this DurationPrice.  # noqa: E501
        :type: OfferPrice
        """

        self._price = price

    @property
    def duration(self):
        """Gets the duration of this DurationPrice.  # noqa: E501


        :return: The duration of this DurationPrice.  # noqa: E501
        :rtype: UnitBasedAttribute
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DurationPrice.


        :param duration: The duration of this DurationPrice.  # noqa: E501
        :type: UnitBasedAttribute
        """

        self._duration = duration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DurationPrice, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DurationPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
