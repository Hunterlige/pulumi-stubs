

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PrivateEndpointConnectionArgs', 'PrivateEndpointConnection']
@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(__self__, *, registry_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], private_endpoint: Optional[pulumi.Input[PrivateEndpointArgs]] = ..., private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., private_link_service_connection_state: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @registry_name.setter
    def registry_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input[PrivateEndpointArgs]]:
        
        ...
    
    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input[PrivateEndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnectionName")
    def private_endpoint_connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_endpoint_connection_name.setter
    def private_endpoint_connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]:
        
        ...
    
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class PrivateEndpointConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., private_endpoint: Optional[pulumi.Input[Union[PrivateEndpointArgs, PrivateEndpointArgsDict]]] = ..., private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., private_link_service_connection_state: Optional[pulumi.Input[Union[PrivateLinkServiceConnectionStateArgs, PrivateLinkServiceConnectionStateArgsDict]]] = ..., registry_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PrivateEndpointConnectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> PrivateEndpointConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> pulumi.Output[Optional[outputs.PrivateEndpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Output[Optional[outputs.PrivateLinkServiceConnectionStateResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


