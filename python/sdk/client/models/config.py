# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Config(object):
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
        'job_config': 'PredictionJobConfig',
        'image_ref': 'str',
        'service_account_name': 'str',
        'resource_request': 'PredictionJobResourceRequest',
        'env_vars': 'list[EnvVar]'
    }

    attribute_map = {
        'job_config': 'job_config',
        'image_ref': 'image_ref',
        'service_account_name': 'service_account_name',
        'resource_request': 'resource_request',
        'env_vars': 'env_vars'
    }

    def __init__(self, job_config=None, image_ref=None, service_account_name=None, resource_request=None, env_vars=None):  # noqa: E501
        """Config - a model defined in Swagger"""  # noqa: E501
        self._job_config = None
        self._image_ref = None
        self._service_account_name = None
        self._resource_request = None
        self._env_vars = None
        self.discriminator = None
        if job_config is not None:
            self.job_config = job_config
        if image_ref is not None:
            self.image_ref = image_ref
        if service_account_name is not None:
            self.service_account_name = service_account_name
        if resource_request is not None:
            self.resource_request = resource_request
        if env_vars is not None:
            self.env_vars = env_vars

    @property
    def job_config(self):
        """Gets the job_config of this Config.  # noqa: E501


        :return: The job_config of this Config.  # noqa: E501
        :rtype: PredictionJobConfig
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        """Sets the job_config of this Config.


        :param job_config: The job_config of this Config.  # noqa: E501
        :type: PredictionJobConfig
        """

        self._job_config = job_config

    @property
    def image_ref(self):
        """Gets the image_ref of this Config.  # noqa: E501


        :return: The image_ref of this Config.  # noqa: E501
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this Config.


        :param image_ref: The image_ref of this Config.  # noqa: E501
        :type: str
        """

        self._image_ref = image_ref

    @property
    def service_account_name(self):
        """Gets the service_account_name of this Config.  # noqa: E501


        :return: The service_account_name of this Config.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this Config.


        :param service_account_name: The service_account_name of this Config.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

    @property
    def resource_request(self):
        """Gets the resource_request of this Config.  # noqa: E501


        :return: The resource_request of this Config.  # noqa: E501
        :rtype: PredictionJobResourceRequest
        """
        return self._resource_request

    @resource_request.setter
    def resource_request(self, resource_request):
        """Sets the resource_request of this Config.


        :param resource_request: The resource_request of this Config.  # noqa: E501
        :type: PredictionJobResourceRequest
        """

        self._resource_request = resource_request

    @property
    def env_vars(self):
        """Gets the env_vars of this Config.  # noqa: E501


        :return: The env_vars of this Config.  # noqa: E501
        :rtype: list[EnvVar]
        """
        return self._env_vars

    @env_vars.setter
    def env_vars(self, env_vars):
        """Sets the env_vars of this Config.


        :param env_vars: The env_vars of this Config.  # noqa: E501
        :type: list[EnvVar]
        """

        self._env_vars = env_vars

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
        if issubclass(Config, dict):
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
        if not isinstance(other, Config):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
