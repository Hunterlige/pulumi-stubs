

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AuthorizerArgs', 'Authorizer']
@pulumi.input_type
class AuthorizerArgs:
    def __init__(__self__, *, api_id: pulumi.Input[_builtins.str], authorizer_type: pulumi.Input[_builtins.str], authorizer_credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_payload_format_version: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., authorizer_uri: Optional[pulumi.Input[_builtins.str]] = ..., enable_simple_responses: Optional[pulumi.Input[_builtins.bool]] = ..., identity_sources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., jwt_configuration: Optional[pulumi.Input[AuthorizerJwtConfigurationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerType")
    def authorizer_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorizer_type.setter
    def authorizer_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerCredentialsArn")
    def authorizer_credentials_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_credentials_arn.setter
    def authorizer_credentials_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerPayloadFormatVersion")
    def authorizer_payload_format_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_payload_format_version.setter
    def authorizer_payload_format_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_uri.setter
    def authorizer_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSimpleResponses")
    def enable_simple_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_simple_responses.setter
    def enable_simple_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identitySources")
    def identity_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @identity_sources.setter
    def identity_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtConfiguration")
    def jwt_configuration(self) -> Optional[pulumi.Input[AuthorizerJwtConfigurationArgs]]:
        
        ...
    
    @jwt_configuration.setter
    def jwt_configuration(self, value: Optional[pulumi.Input[AuthorizerJwtConfigurationArgs]]): # -> None:
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
    


@pulumi.input_type
class _AuthorizerState:
    def __init__(__self__, *, api_id: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_payload_format_version: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., authorizer_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_uri: Optional[pulumi.Input[_builtins.str]] = ..., enable_simple_responses: Optional[pulumi.Input[_builtins.bool]] = ..., identity_sources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., jwt_configuration: Optional[pulumi.Input[AuthorizerJwtConfigurationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerCredentialsArn")
    def authorizer_credentials_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_credentials_arn.setter
    def authorizer_credentials_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerPayloadFormatVersion")
    def authorizer_payload_format_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_payload_format_version.setter
    def authorizer_payload_format_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerType")
    def authorizer_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_type.setter
    def authorizer_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_uri.setter
    def authorizer_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSimpleResponses")
    def enable_simple_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_simple_responses.setter
    def enable_simple_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identitySources")
    def identity_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @identity_sources.setter
    def identity_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtConfiguration")
    def jwt_configuration(self) -> Optional[pulumi.Input[AuthorizerJwtConfigurationArgs]]:
        
        ...
    
    @jwt_configuration.setter
    def jwt_configuration(self, value: Optional[pulumi.Input[AuthorizerJwtConfigurationArgs]]): # -> None:
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
    


@pulumi.type_token("aws:apigatewayv2/authorizer:Authorizer")
class Authorizer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_payload_format_version: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., authorizer_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_uri: Optional[pulumi.Input[_builtins.str]] = ..., enable_simple_responses: Optional[pulumi.Input[_builtins.bool]] = ..., identity_sources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., jwt_configuration: Optional[pulumi.Input[Union[AuthorizerJwtConfigurationArgs, AuthorizerJwtConfigurationArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AuthorizerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_payload_format_version: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., authorizer_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_uri: Optional[pulumi.Input[_builtins.str]] = ..., enable_simple_responses: Optional[pulumi.Input[_builtins.bool]] = ..., identity_sources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., jwt_configuration: Optional[pulumi.Input[Union[AuthorizerJwtConfigurationArgs, AuthorizerJwtConfigurationArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> Authorizer:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerCredentialsArn")
    def authorizer_credentials_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerPayloadFormatVersion")
    def authorizer_payload_format_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerType")
    def authorizer_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSimpleResponses")
    def enable_simple_responses(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identitySources")
    def identity_sources(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtConfiguration")
    def jwt_configuration(self) -> pulumi.Output[Optional[outputs.AuthorizerJwtConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


