

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
__all__ = ['HubRouteTableArgs', 'HubRouteTable']
@pulumi.input_type
class HubRouteTableArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], virtual_hub_name: pulumi.Input[_builtins.str], id: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., route_table_name: Optional[pulumi.Input[_builtins.str]] = ..., routes: Optional[pulumi.Input[Sequence[pulumi.Input[HubRouteArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @virtual_hub_name.setter
    def virtual_hub_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableName")
    def route_table_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_table_name.setter
    def route_table_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HubRouteArgs]]]]:
        
        ...
    
    @routes.setter
    def routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HubRouteArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:HubRouteTable")
class HubRouteTable(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., route_table_name: Optional[pulumi.Input[_builtins.str]] = ..., routes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[HubRouteArgs, HubRouteArgsDict]]]]] = ..., virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HubRouteTableArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> HubRouteTable:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedConnections")
    def associated_connections(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    def labels(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagatingConnections")
    def propagating_connections(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> pulumi.Output[Optional[Sequence[outputs.HubRouteResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


