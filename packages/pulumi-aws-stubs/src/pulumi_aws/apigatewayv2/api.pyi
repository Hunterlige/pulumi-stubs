

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApiArgs', 'Api']
@pulumi.input_type
class ApiArgs:
    def __init__(__self__, *, protocol_type: pulumi.Input[_builtins.str], api_key_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., body: Optional[pulumi.Input[_builtins.str]] = ..., cors_configuration: Optional[pulumi.Input[ApiCorsConfigurationArgs]] = ..., credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_execute_api_endpoint: Optional[pulumi.Input[_builtins.bool]] = ..., fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_key: Optional[pulumi.Input[_builtins.str]] = ..., route_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol_type.setter
    def protocol_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeySelectionExpression")
    def api_key_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_key_selection_expression.setter
    def api_key_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional[pulumi.Input[ApiCorsConfigurationArgs]]:
        
        ...
    
    @cors_configuration.setter
    def cors_configuration(self, value: Optional[pulumi.Input[ApiCorsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @credentials_arn.setter
    def credentials_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_execute_api_endpoint.setter
    def disable_execute_api_endpoint(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_warnings.setter
    def fail_on_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_key.setter
    def route_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeSelectionExpression")
    def route_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_selection_expression.setter
    def route_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ApiState:
    def __init__(__self__, *, api_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., api_key_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., body: Optional[pulumi.Input[_builtins.str]] = ..., cors_configuration: Optional[pulumi.Input[ApiCorsConfigurationArgs]] = ..., credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_execute_api_endpoint: Optional[pulumi.Input[_builtins.bool]] = ..., execution_arn: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., protocol_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_key: Optional[pulumi.Input[_builtins.str]] = ..., route_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_endpoint.setter
    def api_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeySelectionExpression")
    def api_key_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_key_selection_expression.setter
    def api_key_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional[pulumi.Input[ApiCorsConfigurationArgs]]:
        
        ...
    
    @cors_configuration.setter
    def cors_configuration(self, value: Optional[pulumi.Input[ApiCorsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @credentials_arn.setter
    def credentials_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_execute_api_endpoint.setter
    def disable_execute_api_endpoint(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionArn")
    def execution_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_arn.setter
    def execution_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_warnings.setter
    def fail_on_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol_type.setter
    def protocol_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_key.setter
    def route_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeSelectionExpression")
    def route_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_selection_expression.setter
    def route_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:apigatewayv2/api:Api")
class Api(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_key_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., body: Optional[pulumi.Input[_builtins.str]] = ..., cors_configuration: Optional[pulumi.Input[Union[ApiCorsConfigurationArgs, ApiCorsConfigurationArgsDict]]] = ..., credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_execute_api_endpoint: Optional[pulumi.Input[_builtins.bool]] = ..., fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., protocol_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_key: Optional[pulumi.Input[_builtins.str]] = ..., route_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApiArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., api_key_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., body: Optional[pulumi.Input[_builtins.str]] = ..., cors_configuration: Optional[pulumi.Input[Union[ApiCorsConfigurationArgs, ApiCorsConfigurationArgsDict]]] = ..., credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_execute_api_endpoint: Optional[pulumi.Input[_builtins.bool]] = ..., execution_arn: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., protocol_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_key: Optional[pulumi.Input[_builtins.str]] = ..., route_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> Api:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeySelectionExpression")
    def api_key_selection_expression(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> pulumi.Output[Optional[outputs.ApiCorsConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionArn")
    def execution_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeSelectionExpression")
    def route_selection_expression(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


