

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
__all__ = ['DedicatedCloudNodeArgs', 'DedicatedCloudNode']
@pulumi.input_type
class DedicatedCloudNodeArgs:
    def __init__(__self__, *, availability_zone_id: pulumi.Input[_builtins.str], id: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], nodes_count: pulumi.Input[_builtins.int], placement_group_id: pulumi.Input[_builtins.str], purchase_id: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], dedicated_cloud_node_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[SkuArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @availability_zone_id.setter
    def availability_zone_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodesCount")
    def nodes_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @nodes_count.setter
    def nodes_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @placement_group_id.setter
    def placement_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="purchaseId")
    def purchase_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @purchase_id.setter
    def purchase_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedCloudNodeName")
    def dedicated_cloud_node_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dedicated_cloud_node_name.setter
    def dedicated_cloud_node_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:vmwarecloudsimple:DedicatedCloudNode")
class DedicatedCloudNode(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., dedicated_cloud_node_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nodes_count: Optional[pulumi.Input[_builtins.int]] = ..., placement_group_id: Optional[pulumi.Input[_builtins.str]] = ..., purchase_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DedicatedCloudNodeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DedicatedCloudNode:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.DedicatedCloudNodePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


