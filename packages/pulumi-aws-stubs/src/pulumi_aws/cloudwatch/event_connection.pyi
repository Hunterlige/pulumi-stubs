

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EventConnectionArgs', 'EventConnection']
@pulumi.input_type
class EventConnectionArgs:
    def __init__(__self__, *, auth_parameters: pulumi.Input[EventConnectionAuthParametersArgs], authorization_type: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., invocation_connectivity_parameters: Optional[pulumi.Input[EventConnectionInvocationConnectivityParametersArgs]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authParameters")
    def auth_parameters(self) -> pulumi.Input[EventConnectionAuthParametersArgs]:
        
        ...
    
    @auth_parameters.setter
    def auth_parameters(self, value: pulumi.Input[EventConnectionAuthParametersArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorization_type.setter
    def authorization_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invocationConnectivityParameters")
    def invocation_connectivity_parameters(self) -> Optional[pulumi.Input[EventConnectionInvocationConnectivityParametersArgs]]:
        
        ...
    
    @invocation_connectivity_parameters.setter
    def invocation_connectivity_parameters(self, value: Optional[pulumi.Input[EventConnectionInvocationConnectivityParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
class _EventConnectionState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., auth_parameters: Optional[pulumi.Input[EventConnectionAuthParametersArgs]] = ..., authorization_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., invocation_connectivity_parameters: Optional[pulumi.Input[EventConnectionInvocationConnectivityParametersArgs]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authParameters")
    def auth_parameters(self) -> Optional[pulumi.Input[EventConnectionAuthParametersArgs]]:
        
        ...
    
    @auth_parameters.setter
    def auth_parameters(self, value: Optional[pulumi.Input[EventConnectionAuthParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_type.setter
    def authorization_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invocationConnectivityParameters")
    def invocation_connectivity_parameters(self) -> Optional[pulumi.Input[EventConnectionInvocationConnectivityParametersArgs]]:
        
        ...
    
    @invocation_connectivity_parameters.setter
    def invocation_connectivity_parameters(self, value: Optional[pulumi.Input[EventConnectionInvocationConnectivityParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudwatch/eventConnection:EventConnection")
class EventConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auth_parameters: Optional[pulumi.Input[Union[EventConnectionAuthParametersArgs, EventConnectionAuthParametersArgsDict]]] = ..., authorization_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., invocation_connectivity_parameters: Optional[pulumi.Input[Union[EventConnectionInvocationConnectivityParametersArgs, EventConnectionInvocationConnectivityParametersArgsDict]]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EventConnectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auth_parameters: Optional[pulumi.Input[Union[EventConnectionAuthParametersArgs, EventConnectionAuthParametersArgsDict]]] = ..., authorization_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., invocation_connectivity_parameters: Optional[pulumi.Input[Union[EventConnectionInvocationConnectivityParametersArgs, EventConnectionInvocationConnectivityParametersArgsDict]]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> EventConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authParameters")
    def auth_parameters(self) -> pulumi.Output[outputs.EventConnectionAuthParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invocationConnectivityParameters")
    def invocation_connectivity_parameters(self) -> pulumi.Output[Optional[outputs.EventConnectionInvocationConnectivityParameters]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


