import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "KxClusterAutoScalingConfiguration",
    "KxClusterCacheStorageConfiguration",
    "KxClusterCapacityConfiguration",
    "KxClusterCode",
    "KxClusterDatabase",
    "KxClusterDatabaseCacheConfiguration",
    "KxClusterSavedownStorageConfiguration",
    "KxClusterScalingGroupConfiguration",
    "KxClusterTickerplantLogConfiguration",
    "KxClusterVpcConfiguration",
    "KxDataviewSegmentConfiguration",
    "KxEnvironmentCustomDnsConfiguration",
    "KxEnvironmentTransitGatewayConfiguration",
    ...,
    ...,
    ...,
    "KxVolumeAttachedCluster",
    "KxVolumeNas1Configuration",
]

@pulumi.output_type
class KxClusterAutoScalingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_scaling_metric: _builtins.str,
        max_node_count: _builtins.int,
        metric_target: _builtins.float,
        min_node_count: _builtins.int,
        scale_in_cooldown_seconds: _builtins.float,
        scale_out_cooldown_seconds: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingMetric")
    def auto_scaling_metric(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="metricTarget")
    def metric_target(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scaleInCooldownSeconds")
    def scale_in_cooldown_seconds(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="scaleOutCooldownSeconds")
    def scale_out_cooldown_seconds(self) -> _builtins.float: ...

@pulumi.output_type
class KxClusterCacheStorageConfiguration(dict):
    def __init__(__self__, *, size: _builtins.int, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class KxClusterCapacityConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, node_count: _builtins.int, node_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str: ...

@pulumi.output_type
class KxClusterCode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_bucket: _builtins.str,
        s3_key: _builtins.str,
        s3_object_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3ObjectVersion")
    def s3_object_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KxClusterDatabase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        cache_configurations: Optional[
            Sequence[outputs.KxClusterDatabaseCacheConfiguration]
        ] = ...,
        changeset_id: Optional[_builtins.str] = ...,
        dataview_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cacheConfigurations")
    def cache_configurations(
        self,
    ) -> Optional[Sequence[outputs.KxClusterDatabaseCacheConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="changesetId")
    def changeset_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataviewName")
    def dataview_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KxClusterDatabaseCacheConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_type: _builtins.str,
        db_paths: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheType")
    def cache_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbPaths")
    def db_paths(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class KxClusterSavedownStorageConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        size: Optional[_builtins.int] = ...,
        type: Optional[_builtins.str] = ...,
        volume_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KxClusterScalingGroupConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        memory_reservation: _builtins.int,
        node_count: _builtins.int,
        scaling_group_name: _builtins.str,
        cpu: Optional[_builtins.float] = ...,
        memory_limit: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryReservation")
    def memory_reservation(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scalingGroupName")
    def scaling_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="memoryLimit")
    def memory_limit(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class KxClusterTickerplantLogConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, tickerplant_log_volumes: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tickerplantLogVolumes")
    def tickerplant_log_volumes(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class KxClusterVpcConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ip_address_type: _builtins.str,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
        vpc_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

@pulumi.output_type
class KxDataviewSegmentConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        db_paths: Sequence[_builtins.str],
        volume_name: _builtins.str,
        on_demand: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbPaths")
    def db_paths(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onDemand")
    def on_demand(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class KxEnvironmentCustomDnsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_dns_server_ip: _builtins.str,
        custom_dns_server_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customDnsServerIp")
    def custom_dns_server_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customDnsServerName")
    def custom_dns_server_name(self) -> _builtins.str: ...

@pulumi.output_type
class KxEnvironmentTransitGatewayConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        routable_cidr_space: _builtins.str,
        transit_gateway_id: _builtins.str,
        attachment_network_acl_configurations: Optional[
            Sequence[
                outputs.KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfiguration
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routableCidrSpace")
    def routable_cidr_space(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="attachmentNetworkAclConfigurations")
    def attachment_network_acl_configurations(
        self,
    ) -> Optional[
        Sequence[
            outputs.KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfiguration
        ]
    ]: ...

@pulumi.output_type
class KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cidr_block: _builtins.str,
        protocol: _builtins.str,
        rule_action: _builtins.str,
        rule_number: _builtins.int,
        icmp_type_code: Optional[
            outputs.KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationIcmpTypeCode
        ] = ...,
        port_range: Optional[
            outputs.KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationPortRange
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="icmpTypeCode")
    def icmp_type_code(
        self,
    ) -> Optional[
        outputs.KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationIcmpTypeCode
    ]: ...
    @_builtins.property
    @pulumi.getter(name="portRange")
    def port_range(
        self,
    ) -> Optional[
        outputs.KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationPortRange
    ]: ...

@pulumi.output_type
class KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationIcmpTypeCode(
    dict
):
    def __init__(__self__, *, code: _builtins.int, type: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.int: ...

@pulumi.output_type
class KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationPortRange(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int: ...

@pulumi.output_type
class KxVolumeAttachedCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_name: _builtins.str,
        cluster_status: _builtins.str,
        cluster_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterStatus")
    def cluster_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> _builtins.str: ...

@pulumi.output_type
class KxVolumeNas1Configuration(dict):
    def __init__(__self__, *, size: _builtins.int, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
