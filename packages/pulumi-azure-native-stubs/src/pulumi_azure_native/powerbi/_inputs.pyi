

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AzureSkuArgs', 'AzureSkuArgsDict', 'ConnectionStateArgs', 'ConnectionStateArgsDict', 'PrivateEndpointConnectionArgs', 'PrivateEndpointConnectionArgsDict', 'PrivateEndpointArgs', 'PrivateEndpointArgsDict']
class AzureSkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, AzureSkuName]]
    tier: pulumi.Input[Union[_builtins.str, AzureSkuTier]]


@pulumi.input_type
class AzureSkuArgs:
    def __init__(__self__, *, name: pulumi.Input[Union[_builtins.str, AzureSkuName]], tier: pulumi.Input[Union[_builtins.str, AzureSkuTier]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, AzureSkuName]]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, AzureSkuName]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[_builtins.str, AzureSkuTier]]:
        
        ...
    
    @tier.setter
    def tier(self, value: pulumi.Input[Union[_builtins.str, AzureSkuTier]]): # -> None:
        ...
    


class ConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PersistedConnectionStatus]]]


@pulumi.input_type
class ConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PersistedConnectionStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PersistedConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PersistedConnectionStatus]]]): # -> None:
        ...
    


class PrivateEndpointConnectionArgsDict(TypedDict):
    private_endpoint: NotRequired[pulumi.Input[PrivateEndpointArgsDict]]
    private_link_service_connection_state: NotRequired[pulumi.Input[ConnectionStateArgsDict]]
    provisioning_state: NotRequired[pulumi.Input[Union[_builtins.str, ResourceProvisioningState]]]


@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(__self__, *, private_endpoint: Optional[pulumi.Input[PrivateEndpointArgs]] = ..., private_link_service_connection_state: Optional[pulumi.Input[ConnectionStateArgs]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ResourceProvisioningState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input[PrivateEndpointArgs]]:
        
        ...
    
    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input[PrivateEndpointArgs]]): # -> None:
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
    


class PrivateEndpointArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


