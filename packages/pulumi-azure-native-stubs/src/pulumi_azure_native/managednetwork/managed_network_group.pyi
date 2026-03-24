

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ManagedNetworkGroupArgs', 'ManagedNetworkGroup']
@pulumi.input_type
class ManagedNetworkGroupArgs:
    def __init__(__self__, *, managed_network_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], kind: Optional[pulumi.Input[Union[_builtins.str, Kind]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_network_group_name: Optional[pulumi.Input[_builtins.str]] = ..., management_groups: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]] = ..., subnets: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]] = ..., subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]] = ..., virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedNetworkName")
    def managed_network_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @managed_network_name.setter
    def managed_network_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, Kind]]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, Kind]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedNetworkGroupName")
    def managed_network_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_network_group_name.setter
    def managed_network_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]]:
        
        ...
    
    @management_groups.setter
    def management_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscriptions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]]:
        
        ...
    
    @subscriptions.setter
    def subscriptions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]]:
        
        ...
    
    @virtual_networks.setter
    def virtual_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceIdArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:managednetwork:ManagedNetworkGroup")
class ManagedNetworkGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, Kind]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_network_group_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_network_name: Optional[pulumi.Input[_builtins.str]] = ..., management_groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResourceIdArgs, ResourceIdArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., subnets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResourceIdArgs, ResourceIdArgsDict]]]]] = ..., subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResourceIdArgs, ResourceIdArgsDict]]]]] = ..., virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResourceIdArgs, ResourceIdArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagedNetworkGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ManagedNetworkGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> pulumi.Output[Optional[Sequence[outputs.ResourceIdResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Optional[Sequence[outputs.ResourceIdResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscriptions(self) -> pulumi.Output[Optional[Sequence[outputs.ResourceIdResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> pulumi.Output[Optional[Sequence[outputs.ResourceIdResponse]]]:
        
        ...
    


