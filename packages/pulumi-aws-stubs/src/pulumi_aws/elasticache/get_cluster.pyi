import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClusterResult",
    "AwaitableGetClusterResult",
    "get_cluster",
    "get_cluster_output",
]

@pulumi.output_type
class GetClusterResult:
    def __init__(
        __self__,
        arn=...,
        availability_zone=...,
        cache_nodes=...,
        cluster_address=...,
        cluster_id=...,
        configuration_endpoint=...,
        engine=...,
        engine_version=...,
        id=...,
        ip_discovery=...,
        log_delivery_configurations=...,
        maintenance_window=...,
        network_type=...,
        node_type=...,
        notification_topic_arn=...,
        num_cache_nodes=...,
        parameter_group_name=...,
        port=...,
        preferred_outpost_arn=...,
        region=...,
        replication_group_id=...,
        security_group_ids=...,
        snapshot_retention_limit=...,
        snapshot_window=...,
        subnet_group_name=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cacheNodes")
    def cache_nodes(self) -> Sequence[outputs.GetClusterCacheNodeResult]: ...
    @_builtins.property
    @pulumi.getter(name="clusterAddress")
    def cluster_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationEndpoint")
    def configuration_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> Sequence[outputs.GetClusterLogDeliveryConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="numCacheNodes")
    def num_cache_nodes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="preferredOutpostArn")
    def preferred_outpost_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationGroupId")
    def replication_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): ...

def get_cluster(
    cluster_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterResult: ...
def get_cluster_output(
    cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterResult]: ...
