

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
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, acl_name: pulumi.Input[_builtins.str], node_type: pulumi.Input[_builtins.str], auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., data_tiering: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., final_snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_discovery: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., num_replicas_per_shard: Optional[pulumi.Input[_builtins.int]] = ..., num_shards: Optional[pulumi.Input[_builtins.int]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ..., snapshot_window: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tls_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclName")
    def acl_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @acl_name.setter
    def acl_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTiering")
    def data_tiering(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @data_tiering.setter
    def data_tiering(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="finalSnapshotName")
    def final_snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @final_snapshot_name.setter
    def final_snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_discovery.setter
    def ip_discovery(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionClusterName")
    def multi_region_cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @multi_region_cluster_name.setter
    def multi_region_cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numReplicasPerShard")
    def num_replicas_per_shard(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_replicas_per_shard.setter
    def num_replicas_per_shard(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numShards")
    def num_shards(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_shards.setter
    def num_shards(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotArns")
    def snapshot_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @snapshot_arns.setter
    def snapshot_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshot_retention_limit.setter
    def snapshot_retention_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_window.setter
    def snapshot_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_group_name.setter
    def subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsEnabled")
    def tls_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @tls_enabled.setter
    def tls_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *, acl_name: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., cluster_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterClusterEndpointArgs]]]] = ..., data_tiering: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_patch_version: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., final_snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_discovery: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., num_replicas_per_shard: Optional[pulumi.Input[_builtins.int]] = ..., num_shards: Optional[pulumi.Input[_builtins.int]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., shards: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterShardArgs]]]] = ..., snapshot_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ..., snapshot_window: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tls_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclName")
    def acl_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acl_name.setter
    def acl_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpoints")
    def cluster_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterClusterEndpointArgs]]]]:
        ...
    
    @cluster_endpoints.setter
    def cluster_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterClusterEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTiering")
    def data_tiering(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @data_tiering.setter
    def data_tiering(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="enginePatchVersion")
    def engine_patch_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_patch_version.setter
    def engine_patch_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalSnapshotName")
    def final_snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @final_snapshot_name.setter
    def final_snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_discovery.setter
    def ip_discovery(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionClusterName")
    def multi_region_cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @multi_region_cluster_name.setter
    def multi_region_cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numReplicasPerShard")
    def num_replicas_per_shard(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_replicas_per_shard.setter
    def num_replicas_per_shard(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numShards")
    def num_shards(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_shards.setter
    def num_shards(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def shards(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterShardArgs]]]]:
        
        ...
    
    @shards.setter
    def shards(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterShardArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotArns")
    def snapshot_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @snapshot_arns.setter
    def snapshot_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshot_retention_limit.setter
    def snapshot_retention_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_window.setter
    def snapshot_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_group_name.setter
    def subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="tlsEnabled")
    def tls_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @tls_enabled.setter
    def tls_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("aws:memorydb/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., acl_name: Optional[pulumi.Input[_builtins.str]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., data_tiering: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., final_snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_discovery: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., num_replicas_per_shard: Optional[pulumi.Input[_builtins.int]] = ..., num_shards: Optional[pulumi.Input[_builtins.int]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ..., snapshot_window: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., acl_name: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., cluster_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterClusterEndpointArgs, ClusterClusterEndpointArgsDict]]]]] = ..., data_tiering: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_patch_version: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., final_snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_discovery: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., multi_region_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., num_replicas_per_shard: Optional[pulumi.Input[_builtins.int]] = ..., num_shards: Optional[pulumi.Input[_builtins.int]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., shards: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterShardArgs, ClusterShardArgsDict]]]]] = ..., snapshot_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ..., snapshot_window: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tls_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclName")
    def acl_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpoints")
    def cluster_endpoints(self) -> pulumi.Output[Sequence[outputs.ClusterClusterEndpoint]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTiering")
    def data_tiering(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
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
    @pulumi.getter(name="enginePatchVersion")
    def engine_patch_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalSnapshotName")
    def final_snapshot_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionClusterName")
    def multi_region_cluster_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numReplicasPerShard")
    def num_replicas_per_shard(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numShards")
    def num_shards(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shards(self) -> pulumi.Output[Sequence[outputs.ClusterShard]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotArns")
    def snapshot_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="tlsEnabled")
    def tls_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


