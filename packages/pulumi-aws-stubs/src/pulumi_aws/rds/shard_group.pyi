

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
__all__ = ['ShardGroupArgs', 'ShardGroup']
@pulumi.input_type
class ShardGroupArgs:
    def __init__(__self__, *, db_cluster_identifier: pulumi.Input[_builtins.str], db_shard_group_identifier: pulumi.Input[_builtins.str], max_acu: pulumi.Input[_builtins.float], compute_redundancy: Optional[pulumi.Input[_builtins.int]] = ..., min_acu: Optional[pulumi.Input[_builtins.float]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[ShardGroupTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbShardGroupIdentifier")
    def db_shard_group_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @db_shard_group_identifier.setter
    def db_shard_group_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAcu")
    def max_acu(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @max_acu.setter
    def max_acu(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeRedundancy")
    def compute_redundancy(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @compute_redundancy.setter
    def compute_redundancy(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minAcu")
    def min_acu(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min_acu.setter
    def min_acu(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[ShardGroupTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ShardGroupTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ShardGroupState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., compute_redundancy: Optional[pulumi.Input[_builtins.int]] = ..., db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., db_shard_group_identifier: Optional[pulumi.Input[_builtins.str]] = ..., db_shard_group_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., max_acu: Optional[pulumi.Input[_builtins.float]] = ..., min_acu: Optional[pulumi.Input[_builtins.float]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[ShardGroupTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeRedundancy")
    def compute_redundancy(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @compute_redundancy.setter
    def compute_redundancy(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbShardGroupIdentifier")
    def db_shard_group_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_shard_group_identifier.setter
    def db_shard_group_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbShardGroupResourceId")
    def db_shard_group_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_shard_group_resource_id.setter
    def db_shard_group_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAcu")
    def max_acu(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max_acu.setter
    def max_acu(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minAcu")
    def min_acu(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min_acu.setter
    def min_acu(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ShardGroupTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ShardGroupTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:rds/shardGroup:ShardGroup")
class ShardGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., compute_redundancy: Optional[pulumi.Input[_builtins.int]] = ..., db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., db_shard_group_identifier: Optional[pulumi.Input[_builtins.str]] = ..., max_acu: Optional[pulumi.Input[_builtins.float]] = ..., min_acu: Optional[pulumi.Input[_builtins.float]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[ShardGroupTimeoutsArgs, ShardGroupTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ShardGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., compute_redundancy: Optional[pulumi.Input[_builtins.int]] = ..., db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., db_shard_group_identifier: Optional[pulumi.Input[_builtins.str]] = ..., db_shard_group_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., max_acu: Optional[pulumi.Input[_builtins.float]] = ..., min_acu: Optional[pulumi.Input[_builtins.float]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[ShardGroupTimeoutsArgs, ShardGroupTimeoutsArgsDict]]] = ...) -> ShardGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeRedundancy")
    def compute_redundancy(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbShardGroupIdentifier")
    def db_shard_group_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbShardGroupResourceId")
    def db_shard_group_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAcu")
    def max_acu(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minAcu")
    def min_acu(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
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
    def timeouts(self) -> pulumi.Output[Optional[outputs.ShardGroupTimeouts]]:
        ...
    


