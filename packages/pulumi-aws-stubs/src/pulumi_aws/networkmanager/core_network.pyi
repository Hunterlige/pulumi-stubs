

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CoreNetworkArgs', 'CoreNetwork']
@pulumi.input_type
class CoreNetworkArgs:
    def __init__(__self__, *, global_network_id: pulumi.Input[_builtins.str], base_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., base_policy_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., create_base_policy: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @global_network_id.setter
    def global_network_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicyDocument")
    def base_policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @base_policy_document.setter
    def base_policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicyRegions")
    def base_policy_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @base_policy_regions.setter
    def base_policy_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createBasePolicy")
    def create_base_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_base_policy.setter
    def create_base_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _CoreNetworkState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., base_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., base_policy_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., create_base_policy: Optional[pulumi.Input[_builtins.bool]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., edges: Optional[pulumi.Input[Sequence[pulumi.Input[CoreNetworkEdgeArgs]]]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., segments: Optional[pulumi.Input[Sequence[pulumi.Input[CoreNetworkSegmentArgs]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicyDocument")
    def base_policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @base_policy_document.setter
    def base_policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicyRegions")
    def base_policy_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @base_policy_regions.setter
    def base_policy_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createBasePolicy")
    def create_base_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_base_policy.setter
    def create_base_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def edges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CoreNetworkEdgeArgs]]]]:
        
        ...
    
    @edges.setter
    def edges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CoreNetworkEdgeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_network_id.setter
    def global_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def segments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CoreNetworkSegmentArgs]]]]:
        
        ...
    
    @segments.setter
    def segments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CoreNetworkSegmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:networkmanager/coreNetwork:CoreNetwork")
class CoreNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., base_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., base_policy_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., create_base_policy: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CoreNetworkArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., base_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., base_policy_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., create_base_policy: Optional[pulumi.Input[_builtins.bool]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., edges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CoreNetworkEdgeArgs, CoreNetworkEdgeArgsDict]]]]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., segments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CoreNetworkSegmentArgs, CoreNetworkSegmentArgsDict]]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> CoreNetwork:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicyDocument")
    def base_policy_document(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicyRegions")
    def base_policy_regions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createBasePolicy")
    def create_base_policy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edges(self) -> pulumi.Output[Sequence[outputs.CoreNetworkEdge]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def segments(self) -> pulumi.Output[Sequence[outputs.CoreNetworkSegment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


