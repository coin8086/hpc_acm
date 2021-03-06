# coding: utf-8

"""
    HPC Web API

    Preview  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from hpc_acm.models.node_metadata_compute import NodeMetadataCompute  # noqa: F401,E501
from hpc_acm.models.node_metadata_network import NodeMetadataNetwork  # noqa: F401,E501


class NodeMetadata(object):
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
        'compute': 'NodeMetadataCompute',
        'network': 'NodeMetadataNetwork'
    }

    attribute_map = {
        'compute': 'compute',
        'network': 'network'
    }

    def __init__(self, compute=None, network=None):  # noqa: E501
        """NodeMetadata - a model defined in Swagger"""  # noqa: E501

        self._compute = None
        self._network = None
        self.discriminator = None

        if compute is not None:
            self.compute = compute
        if network is not None:
            self.network = network

    @property
    def compute(self):
        """Gets the compute of this NodeMetadata.  # noqa: E501


        :return: The compute of this NodeMetadata.  # noqa: E501
        :rtype: NodeMetadataCompute
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """Sets the compute of this NodeMetadata.


        :param compute: The compute of this NodeMetadata.  # noqa: E501
        :type: NodeMetadataCompute
        """

        self._compute = compute

    @property
    def network(self):
        """Gets the network of this NodeMetadata.  # noqa: E501


        :return: The network of this NodeMetadata.  # noqa: E501
        :rtype: NodeMetadataNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this NodeMetadata.


        :param network: The network of this NodeMetadata.  # noqa: E501
        :type: NodeMetadataNetwork
        """

        self._network = network

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
