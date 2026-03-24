

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
__all__ = ['MultiRegionClusterArgs', 'MultiRegionCluster']
@pulumi.input_type
class MultiRegionClusterArgs:
    def __init__(__self__, *, multi_region_cluster_name_suffix: pulumi.Input[_builtins.str], node_type: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., num_shards: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[MultiRegionClusterTimeoutsArgs]] = ..., tls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., update_strategy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionClusterNameSuffix")
    def multi_region_cluster_name_suffix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @multi_region_cluster_name_suffix.setter
    def multi_region_cluster_name_suffix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionParameterGroupName")
    def multi_region_parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @multi_region_parameter_group_name.setter
    def multi_region_parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numShards")
    def num_shards(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_shards.setter
    def num_shards(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[MultiRegionClusterTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[MultiRegionClusterTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsEnabled")
    def tls_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @tls_enabled.setter
    def tls_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @update_strategy.setter
    def update_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _MultiRegionClusterState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_cluster_name_suffix: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., num_shards: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[MultiRegionClusterTimeoutsArgs]] = ..., tls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., update_strategy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionClusterName")
    def multi_region_cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @multi_region_cluster_name.setter
    def multi_region_cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionClusterNameSuffix")
    def multi_region_cluster_name_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @multi_region_cluster_name_suffix.setter
    def multi_region_cluster_name_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionParameterGroupName")
    def multi_region_parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @multi_region_parameter_group_name.setter
    def multi_region_parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numShards")
    def num_shards(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_shards.setter
    def num_shards(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[MultiRegionClusterTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[MultiRegionClusterTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsEnabled")
    def tls_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @tls_enabled.setter
    def tls_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @update_strategy.setter
    def update_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:memorydb/multiRegionCluster:MultiRegionCluster")
class MultiRegionCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_cluster_name_suffix: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., num_shards: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[MultiRegionClusterTimeoutsArgs, MultiRegionClusterTimeoutsArgsDict]]] = ..., tls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., update_strategy: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MultiRegionClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_cluster_name_suffix: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., num_shards: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[MultiRegionClusterTimeoutsArgs, MultiRegionClusterTimeoutsArgsDict]]] = ..., tls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., update_strategy: Optional[pulumi.Input[_builtins.str]] = ...) -> MultiRegionCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionClusterName")
    def multi_region_cluster_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionClusterNameSuffix")
    def multi_region_cluster_name_suffix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionParameterGroupName")
    def multi_region_parameter_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numShards")
    def num_shards(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.MultiRegionClusterTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsEnabled")
    def tls_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    


