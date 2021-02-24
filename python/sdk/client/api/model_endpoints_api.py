# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from client.api_client import ApiClient


class ModelEndpointsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def models_model_id_endpoints_get(self, model_id, **kwargs):  # noqa: E501
        """List model endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_endpoints_get(model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :return: list[ModelEndpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_endpoints_get_with_http_info(model_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_endpoints_get_with_http_info(model_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_endpoints_get_with_http_info(self, model_id, **kwargs):  # noqa: E501
        """List model endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_endpoints_get_with_http_info(model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :return: list[ModelEndpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_endpoints_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_endpoints_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/endpoints', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelEndpoint]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def models_model_id_endpoints_model_endpoint_id_delete(self, model_id, model_endpoint_id, **kwargs):  # noqa: E501
        """Stop serving traffic to the model endpoint, then delete it.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_endpoints_model_endpoint_id_delete(model_id, model_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param str model_endpoint_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_endpoints_model_endpoint_id_delete_with_http_info(model_id, model_endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_endpoints_model_endpoint_id_delete_with_http_info(model_id, model_endpoint_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_endpoints_model_endpoint_id_delete_with_http_info(self, model_id, model_endpoint_id, **kwargs):  # noqa: E501
        """Stop serving traffic to the model endpoint, then delete it.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_endpoints_model_endpoint_id_delete_with_http_info(model_id, model_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param str model_endpoint_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id', 'model_endpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_endpoints_model_endpoint_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_endpoints_model_endpoint_id_delete`")  # noqa: E501
        # verify the required parameter 'model_endpoint_id' is set
        if ('model_endpoint_id' not in params or
                params['model_endpoint_id'] is None):
            raise ValueError("Missing the required parameter `model_endpoint_id` when calling `models_model_id_endpoints_model_endpoint_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501
        if 'model_endpoint_id' in params:
            path_params['model_endpoint_id'] = params['model_endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/endpoints/{model_endpoint_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def models_model_id_endpoints_model_endpoint_id_get(self, model_id, model_endpoint_id, **kwargs):  # noqa: E501
        """Get a model endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_endpoints_model_endpoint_id_get(model_id, model_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param str model_endpoint_id: (required)
        :return: ModelEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_endpoints_model_endpoint_id_get_with_http_info(model_id, model_endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_endpoints_model_endpoint_id_get_with_http_info(model_id, model_endpoint_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_endpoints_model_endpoint_id_get_with_http_info(self, model_id, model_endpoint_id, **kwargs):  # noqa: E501
        """Get a model endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_endpoints_model_endpoint_id_get_with_http_info(model_id, model_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param str model_endpoint_id: (required)
        :return: ModelEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id', 'model_endpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_endpoints_model_endpoint_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_endpoints_model_endpoint_id_get`")  # noqa: E501
        # verify the required parameter 'model_endpoint_id' is set
        if ('model_endpoint_id' not in params or
                params['model_endpoint_id'] is None):
            raise ValueError("Missing the required parameter `model_endpoint_id` when calling `models_model_id_endpoints_model_endpoint_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501
        if 'model_endpoint_id' in params:
            path_params['model_endpoint_id'] = params['model_endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/endpoints/{model_endpoint_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def models_model_id_endpoints_model_endpoint_id_put(self, model_id, model_endpoint_id, **kwargs):  # noqa: E501
        """Update model endpoint data. Mainly used to update its rule.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_endpoints_model_endpoint_id_put(model_id, model_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param str model_endpoint_id: (required)
        :param ModelEndpoint body:
        :return: ModelEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_endpoints_model_endpoint_id_put_with_http_info(model_id, model_endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_endpoints_model_endpoint_id_put_with_http_info(model_id, model_endpoint_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_endpoints_model_endpoint_id_put_with_http_info(self, model_id, model_endpoint_id, **kwargs):  # noqa: E501
        """Update model endpoint data. Mainly used to update its rule.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_endpoints_model_endpoint_id_put_with_http_info(model_id, model_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int model_id: (required)
        :param str model_endpoint_id: (required)
        :param ModelEndpoint body:
        :return: ModelEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id', 'model_endpoint_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_endpoints_model_endpoint_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_endpoints_model_endpoint_id_put`")  # noqa: E501
        # verify the required parameter 'model_endpoint_id' is set
        if ('model_endpoint_id' not in params or
                params['model_endpoint_id'] is None):
            raise ValueError("Missing the required parameter `model_endpoint_id` when calling `models_model_id_endpoints_model_endpoint_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501
        if 'model_endpoint_id' in params:
            path_params['model_endpoint_id'] = params['model_endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/endpoints/{model_endpoint_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def models_model_id_endpoints_post(self, body, model_id, **kwargs):  # noqa: E501
        """Create a model endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_endpoints_post(body, model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelEndpoint body: Model endpoint object that has to be added (required)
        :param int model_id: (required)
        :return: ModelEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.models_model_id_endpoints_post_with_http_info(body, model_id, **kwargs)  # noqa: E501
        else:
            (data) = self.models_model_id_endpoints_post_with_http_info(body, model_id, **kwargs)  # noqa: E501
            return data

    def models_model_id_endpoints_post_with_http_info(self, body, model_id, **kwargs):  # noqa: E501
        """Create a model endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.models_model_id_endpoints_post_with_http_info(body, model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelEndpoint body: Model endpoint object that has to be added (required)
        :param int model_id: (required)
        :return: ModelEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'model_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method models_model_id_endpoints_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `models_model_id_endpoints_post`")  # noqa: E501
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `models_model_id_endpoints_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/models/{model_id}/endpoints', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_project_id_model_endpoints_get(self, project_id, **kwargs):  # noqa: E501
        """List existing model endpoints for all models in particular project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_model_endpoints_get(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: Filter list of model endpoints by specific `project_id` (required)
        :param str region: Filter list of model endpoints by specific environment's `region`
        :return: list[ModelEndpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_model_endpoints_get_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_model_endpoints_get_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_model_endpoints_get_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """List existing model endpoints for all models in particular project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_model_endpoints_get_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: Filter list of model endpoints by specific `project_id` (required)
        :param str region: Filter list of model endpoints by specific environment's `region`
        :return: list[ModelEndpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_project_id_model_endpoints_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_model_endpoints_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501

        query_params = []
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/model_endpoints', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelEndpoint]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
