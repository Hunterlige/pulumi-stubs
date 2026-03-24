

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
__all__ = ['PrivateEndpointConnectionInitArgs', 'PrivateEndpointConnection']
@pulumi.input_type
class PrivateEndpointConnectionInitArgs:
    def __init__(__self__, *, azure_resource_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], private_endpoint: Optional[pulumi.Input[PrivateEndpointArgs]] = ..., private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., private_link_service_connection_state: Optional[pulumi.Input[ConnectionStateArgs]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ResourceProvisioningState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureResourceName")
    def azure_resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @azure_resource_name.setter
    def azure_resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="privateEndpointName")
    def private_endpoint_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_endpoint_name.setter
    def private_endpoint_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input[ConnectionStateArgs]]:
        
        ...
    
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input[ConnectionStateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ResourceProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceProvisioningState]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:powerbi:PrivateEndpointConnection")
class PrivateEndpointConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., azure_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoint: Optional[pulumi.Input[Union[PrivateEndpointArgs, PrivateEndpointArgsDict]]] = ..., private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., private_link_service_connection_state: Optional[pulumi.Input[Union[ConnectionStateArgs, ConnectionStateArgsDict]]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ResourceProvisioningState]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PrivateEndpointConnectionInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
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
    def private_link_service_connection_state(self) -> pulumi.Output[Optional[outputs.ConnectionStateResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


