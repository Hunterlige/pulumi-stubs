

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReplicationGroupResult', 'AwaitableGetReplicationGroupResult', 'get_replication_group', 'get_replication_group_output']
@pulumi.output_type
class GetReplicationGroupResult:
    
    def __init__(__self__, arn=..., auth_token_enabled=..., automatic_failover_enabled=..., cluster_mode=..., configuration_endpoint_address=..., description=..., id=..., log_delivery_configurations=..., member_clusters=..., multi_az_enabled=..., node_group_configurations=..., node_type=..., num_cache_clusters=..., num_node_groups=..., port=..., primary_endpoint_address=..., reader_endpoint_address=..., region=..., replicas_per_node_group=..., replication_group_id=..., snapshot_retention_limit=..., snapshot_window=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTokenEnabled")
    def auth_token_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticFailoverEnabled")
    def automatic_failover_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterMode")
    def cluster_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationEndpointAddress")
    def configuration_endpoint_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfigurations")
    def log_delivery_configurations(self) -> Sequence[outputs.GetReplicationGroupLogDeliveryConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memberClusters")
    def member_clusters(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiAzEnabled")
    def multi_az_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeGroupConfigurations")
    def node_group_configurations(self) -> Sequence[outputs.GetReplicationGroupNodeGroupConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numCacheClusters")
    def num_cache_clusters(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNodeGroups")
    def num_node_groups(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryEndpointAddress")
    def primary_endpoint_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerEndpointAddress")
    def reader_endpoint_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicasPerNodeGroup")
    def replicas_per_node_group(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationGroupId")
    def replication_group_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> _builtins.str:
        
        ...
    


class AwaitableGetReplicationGroupResult(GetReplicationGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetReplicationGroupResult]:
        ...
    


def get_replication_group(region: Optional[_builtins.str] = ..., replication_group_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReplicationGroupResult:
    
    ...

def get_replication_group_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., replication_group_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReplicationGroupResult]:
    
    ...

