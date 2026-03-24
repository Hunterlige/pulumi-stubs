

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
__all__ = ['GlobalReplicationGroupArgs', 'GlobalReplicationGroup']
@pulumi.input_type
class GlobalReplicationGroupArgs:
    def __init__(__self__, *, global_replication_group_id_suffix: pulumi.Input[_builtins.str], primary_replication_group_id: pulumi.Input[_builtins.str], automatic_failover_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_node_type: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., global_replication_group_description: Optional[pulumi.Input[_builtins.str]] = ..., num_node_groups: Optional[pulumi.Input[_builtins.int]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalReplicationGroupIdSuffix")
    def global_replication_group_id_suffix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @global_replication_group_id_suffix.setter
    def global_replication_group_id_suffix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryReplicationGroupId")
    def primary_replication_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @primary_replication_group_id.setter
    def primary_replication_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticFailoverEnabled")
    def automatic_failover_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @automatic_failover_enabled.setter
    def automatic_failover_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeType")
    def cache_node_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_node_type.setter
    def cache_node_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="globalReplicationGroupDescription")
    def global_replication_group_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_replication_group_description.setter
    def global_replication_group_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNodeGroups")
    def num_node_groups(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_node_groups.setter
    def num_node_groups(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter_group_name.setter
    def parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _GlobalReplicationGroupState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., at_rest_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., auth_token_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., automatic_failover_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_node_type: Optional[pulumi.Input[_builtins.str]] = ..., cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ..., global_node_groups: Optional[pulumi.Input[Sequence[pulumi.Input[GlobalReplicationGroupGlobalNodeGroupArgs]]]] = ..., global_replication_group_description: Optional[pulumi.Input[_builtins.str]] = ..., global_replication_group_id: Optional[pulumi.Input[_builtins.str]] = ..., global_replication_group_id_suffix: Optional[pulumi.Input[_builtins.str]] = ..., num_node_groups: Optional[pulumi.Input[_builtins.int]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., primary_replication_group_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTokenEnabled")
    def auth_token_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auth_token_enabled.setter
    def auth_token_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticFailoverEnabled")
    def automatic_failover_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @automatic_failover_enabled.setter
    def automatic_failover_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeType")
    def cache_node_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_node_type.setter
    def cache_node_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEnabled")
    def cluster_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cluster_enabled.setter
    def cluster_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="engineVersionActual")
    def engine_version_actual(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_version_actual.setter
    def engine_version_actual(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNodeGroups")
    def global_node_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GlobalReplicationGroupGlobalNodeGroupArgs]]]]:
        
        ...
    
    @global_node_groups.setter
    def global_node_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GlobalReplicationGroupGlobalNodeGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalReplicationGroupDescription")
    def global_replication_group_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_replication_group_description.setter
    def global_replication_group_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalReplicationGroupId")
    def global_replication_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_replication_group_id.setter
    def global_replication_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalReplicationGroupIdSuffix")
    def global_replication_group_id_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_replication_group_id_suffix.setter
    def global_replication_group_id_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNodeGroups")
    def num_node_groups(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_node_groups.setter
    def num_node_groups(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter_group_name.setter
    def parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryReplicationGroupId")
    def primary_replication_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_replication_group_id.setter
    def primary_replication_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionEnabled")
    def transit_encryption_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transit_encryption_enabled.setter
    def transit_encryption_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class GlobalReplicationGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., automatic_failover_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_node_type: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., global_replication_group_description: Optional[pulumi.Input[_builtins.str]] = ..., global_replication_group_id_suffix: Optional[pulumi.Input[_builtins.str]] = ..., num_node_groups: Optional[pulumi.Input[_builtins.int]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., primary_replication_group_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GlobalReplicationGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., at_rest_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., auth_token_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., automatic_failover_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_node_type: Optional[pulumi.Input[_builtins.str]] = ..., cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ..., global_node_groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GlobalReplicationGroupGlobalNodeGroupArgs, GlobalReplicationGroupGlobalNodeGroupArgsDict]]]]] = ..., global_replication_group_description: Optional[pulumi.Input[_builtins.str]] = ..., global_replication_group_id: Optional[pulumi.Input[_builtins.str]] = ..., global_replication_group_id_suffix: Optional[pulumi.Input[_builtins.str]] = ..., num_node_groups: Optional[pulumi.Input[_builtins.int]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., primary_replication_group_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> GlobalReplicationGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTokenEnabled")
    def auth_token_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticFailoverEnabled")
    def automatic_failover_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeType")
    def cache_node_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEnabled")
    def cluster_enabled(self) -> pulumi.Output[_builtins.bool]:
        
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
    @pulumi.getter(name="engineVersionActual")
    def engine_version_actual(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNodeGroups")
    def global_node_groups(self) -> pulumi.Output[Sequence[outputs.GlobalReplicationGroupGlobalNodeGroup]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalReplicationGroupDescription")
    def global_replication_group_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalReplicationGroupId")
    def global_replication_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalReplicationGroupIdSuffix")
    def global_replication_group_id_suffix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNodeGroups")
    def num_node_groups(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryReplicationGroupId")
    def primary_replication_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionEnabled")
    def transit_encryption_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    


