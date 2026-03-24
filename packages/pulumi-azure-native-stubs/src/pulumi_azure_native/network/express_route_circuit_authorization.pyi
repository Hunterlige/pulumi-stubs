

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExpressRouteCircuitAuthorizationInitArgs', 'ExpressRouteCircuitAuthorization']
@pulumi.input_type
class ExpressRouteCircuitAuthorizationInitArgs:
    def __init__(__self__, *, circuit_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], authorization_key: Optional[pulumi.Input[_builtins.str]] = ..., authorization_name: Optional[pulumi.Input[_builtins.str]] = ..., authorization_use_status: Optional[pulumi.Input[Union[_builtins.str, AuthorizationUseStatus]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitName")
    def circuit_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @circuit_name.setter
    def circuit_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationName")
    def authorization_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_name.setter
    def authorization_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationUseStatus")
    def authorization_use_status(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthorizationUseStatus]]]:
        
        ...
    
    @authorization_use_status.setter
    def authorization_use_status(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthorizationUseStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ExpressRouteCircuitAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authorization_key: Optional[pulumi.Input[_builtins.str]] = ..., authorization_name: Optional[pulumi.Input[_builtins.str]] = ..., authorization_use_status: Optional[pulumi.Input[Union[_builtins.str, AuthorizationUseStatus]]] = ..., circuit_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExpressRouteCircuitAuthorizationInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ExpressRouteCircuitAuthorization:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationUseStatus")
    def authorization_use_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionResourceUri")
    def connection_resource_uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


