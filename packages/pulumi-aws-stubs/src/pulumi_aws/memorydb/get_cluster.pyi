

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClusterResult', 'AwaitableGetClusterResult', 'get_cluster', 'get_cluster_output']
@pulumi.output_type
class GetClusterResult:
    
    def __init__(__self__, acl_name=..., arn=..., auto_minor_version_upgrade=..., cluster_endpoints=..., data_tiering=..., description=..., engine=..., engine_patch_version=..., engine_version=..., final_snapshot_name=..., id=..., ip_discovery=..., kms_key_arn=..., maintenance_window=..., name=..., network_type=..., node_type=..., num_replicas_per_shard=..., num_shards=..., parameter_group_name=..., port=..., region=..., security_group_ids=..., shards=..., snapshot_retention_limit=..., snapshot_window=..., sns_topic_arn=..., subnet_group_name=..., tags=..., tls_enabled=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclName")
    def acl_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpoints")
    def cluster_endpoints(self) -> Sequence[outputs.GetClusterClusterEndpointResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTiering")
    def data_tiering(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enginePatchVersion")
    def engine_patch_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalSnapshotName")
    def final_snapshot_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numReplicasPerShard")
    def num_replicas_per_shard(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numShards")
    def num_shards(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shards(self) -> Sequence[outputs.GetClusterShardResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsEnabled")
    def tls_enabled(self) -> _builtins.bool:
        
        ...
    


class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetClusterResult]:
        ...
    


def get_cluster(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClusterResult:
    
    ...

def get_cluster_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClusterResult]:
    
    ...

