import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "KxClusterAutoScalingConfigurationArgs",
    "KxClusterAutoScalingConfigurationArgsDict",
    "KxClusterCacheStorageConfigurationArgs",
    "KxClusterCacheStorageConfigurationArgsDict",
    "KxClusterCapacityConfigurationArgs",
    "KxClusterCapacityConfigurationArgsDict",
    "KxClusterCodeArgs",
    "KxClusterCodeArgsDict",
    "KxClusterDatabaseArgs",
    "KxClusterDatabaseArgsDict",
    "KxClusterDatabaseCacheConfigurationArgs",
    "KxClusterDatabaseCacheConfigurationArgsDict",
    "KxClusterSavedownStorageConfigurationArgs",
    "KxClusterSavedownStorageConfigurationArgsDict",
    "KxClusterScalingGroupConfigurationArgs",
    "KxClusterScalingGroupConfigurationArgsDict",
    "KxClusterTickerplantLogConfigurationArgs",
    "KxClusterTickerplantLogConfigurationArgsDict",
    "KxClusterVpcConfigurationArgs",
    "KxClusterVpcConfigurationArgsDict",
    "KxDataviewSegmentConfigurationArgs",
    "KxDataviewSegmentConfigurationArgsDict",
    "KxEnvironmentCustomDnsConfigurationArgs",
    "KxEnvironmentCustomDnsConfigurationArgsDict",
    "KxEnvironmentTransitGatewayConfigurationArgs",
    "KxEnvironmentTransitGatewayConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "KxVolumeAttachedClusterArgs",
    "KxVolumeAttachedClusterArgsDict",
    "KxVolumeNas1ConfigurationArgs",
    "KxVolumeNas1ConfigurationArgsDict",
]

class KxClusterAutoScalingConfigurationArgsDict(TypedDict):
    auto_scaling_metric: pulumi.Input[_builtins.str]
    max_node_count: pulumi.Input[_builtins.int]
    metric_target: pulumi.Input[_builtins.float]
    min_node_count: pulumi.Input[_builtins.int]
    scale_in_cooldown_seconds: pulumi.Input[_builtins.float]
    scale_out_cooldown_seconds: pulumi.Input[_builtins.float]
    ...

@pulumi.input_type
class KxClusterAutoScalingConfigurationArgs:
    def __init__(
        __self__,
        *,
        auto_scaling_metric: pulumi.Input[_builtins.str],
        max_node_count: pulumi.Input[_builtins.int],
        metric_target: pulumi.Input[_builtins.float],
        min_node_count: pulumi.Input[_builtins.int],
        scale_in_cooldown_seconds: pulumi.Input[_builtins.float],
        scale_out_cooldown_seconds: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingMetric")
    def auto_scaling_metric(self) -> pulumi.Input[_builtins.str]: ...
    @auto_scaling_metric.setter
    def auto_scaling_metric(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_node_count.setter
    def max_node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="metricTarget")
    def metric_target(self) -> pulumi.Input[_builtins.float]: ...
    @metric_target.setter
    def metric_target(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_node_count.setter
    def min_node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scaleInCooldownSeconds")
    def scale_in_cooldown_seconds(self) -> pulumi.Input[_builtins.float]: ...
    @scale_in_cooldown_seconds.setter
    def scale_in_cooldown_seconds(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="scaleOutCooldownSeconds")
    def scale_out_cooldown_seconds(self) -> pulumi.Input[_builtins.float]: ...
    @scale_out_cooldown_seconds.setter
    def scale_out_cooldown_seconds(self, value: pulumi.Input[_builtins.float]): ...

class KxClusterCacheStorageConfigurationArgsDict(TypedDict):
    size: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class KxClusterCacheStorageConfigurationArgs:
    def __init__(
        __self__,
        *,
        size: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]: ...
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class KxClusterCapacityConfigurationArgsDict(TypedDict):
    node_count: pulumi.Input[_builtins.int]
    node_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class KxClusterCapacityConfigurationArgs:
    def __init__(
        __self__,
        *,
        node_count: pulumi.Input[_builtins.int],
        node_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Input[_builtins.int]: ...
    @node_count.setter
    def node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Input[_builtins.str]: ...
    @node_type.setter
    def node_type(self, value: pulumi.Input[_builtins.str]): ...

class KxClusterCodeArgsDict(TypedDict):
    s3_bucket: pulumi.Input[_builtins.str]
    s3_key: pulumi.Input[_builtins.str]
    s3_object_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class KxClusterCodeArgs:
    def __init__(
        __self__,
        *,
        s3_bucket: pulumi.Input[_builtins.str],
        s3_key: pulumi.Input[_builtins.str],
        s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket.setter
    def s3_bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> pulumi.Input[_builtins.str]: ...
    @s3_key.setter
    def s3_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3ObjectVersion")
    def s3_object_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_object_version.setter
    def s3_object_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KxClusterDatabaseArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    cache_configurations: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[KxClusterDatabaseCacheConfigurationArgsDict]]
        ]
    ]
    changeset_id: NotRequired[pulumi.Input[_builtins.str]]
    dataview_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class KxClusterDatabaseArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        cache_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KxClusterDatabaseCacheConfigurationArgs]]
            ]
        ] = ...,
        changeset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dataview_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cacheConfigurations")
    def cache_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KxClusterDatabaseCacheConfigurationArgs]]]
    ]: ...
    @cache_configurations.setter
    def cache_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KxClusterDatabaseCacheConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="changesetId")
    def changeset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @changeset_id.setter
    def changeset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataviewName")
    def dataview_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataview_name.setter
    def dataview_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KxClusterDatabaseCacheConfigurationArgsDict(TypedDict):
    cache_type: pulumi.Input[_builtins.str]
    db_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class KxClusterDatabaseCacheConfigurationArgs:
    def __init__(
        __self__,
        *,
        cache_type: pulumi.Input[_builtins.str],
        db_paths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheType")
    def cache_type(self) -> pulumi.Input[_builtins.str]: ...
    @cache_type.setter
    def cache_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dbPaths")
    def db_paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @db_paths.setter
    def db_paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class KxClusterSavedownStorageConfigurationArgsDict(TypedDict):
    size: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    volume_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class KxClusterSavedownStorageConfigurationArgs:
    def __init__(
        __self__,
        *,
        size: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KxClusterScalingGroupConfigurationArgsDict(TypedDict):
    memory_reservation: pulumi.Input[_builtins.int]
    node_count: pulumi.Input[_builtins.int]
    scaling_group_name: pulumi.Input[_builtins.str]
    cpu: NotRequired[pulumi.Input[_builtins.float]]
    memory_limit: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class KxClusterScalingGroupConfigurationArgs:
    def __init__(
        __self__,
        *,
        memory_reservation: pulumi.Input[_builtins.int],
        node_count: pulumi.Input[_builtins.int],
        scaling_group_name: pulumi.Input[_builtins.str],
        cpu: Optional[pulumi.Input[_builtins.float]] = ...,
        memory_limit: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryReservation")
    def memory_reservation(self) -> pulumi.Input[_builtins.int]: ...
    @memory_reservation.setter
    def memory_reservation(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Input[_builtins.int]: ...
    @node_count.setter
    def node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scalingGroupName")
    def scaling_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @scaling_group_name.setter
    def scaling_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryLimit")
    def memory_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_limit.setter
    def memory_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class KxClusterTickerplantLogConfigurationArgsDict(TypedDict):
    tickerplant_log_volumes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class KxClusterTickerplantLogConfigurationArgs:
    def __init__(
        __self__,
        *,
        tickerplant_log_volumes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tickerplantLogVolumes")
    def tickerplant_log_volumes(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @tickerplant_log_volumes.setter
    def tickerplant_log_volumes(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class KxClusterVpcConfigurationArgsDict(TypedDict):
    ip_address_type: pulumi.Input[_builtins.str]
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class KxClusterVpcConfigurationArgs:
    def __init__(
        __self__,
        *,
        ip_address_type: pulumi.Input[_builtins.str],
        security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vpc_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> pulumi.Input[_builtins.str]: ...
    @ip_address_type.setter
    def ip_address_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...

class KxDataviewSegmentConfigurationArgsDict(TypedDict):
    db_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    volume_name: pulumi.Input[_builtins.str]
    on_demand: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class KxDataviewSegmentConfigurationArgs:
    def __init__(
        __self__,
        *,
        db_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        volume_name: pulumi.Input[_builtins.str],
        on_demand: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbPaths")
    def db_paths(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @db_paths.setter
    def db_paths(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Input[_builtins.str]: ...
    @volume_name.setter
    def volume_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="onDemand")
    def on_demand(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @on_demand.setter
    def on_demand(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class KxEnvironmentCustomDnsConfigurationArgsDict(TypedDict):
    custom_dns_server_ip: pulumi.Input[_builtins.str]
    custom_dns_server_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class KxEnvironmentCustomDnsConfigurationArgs:
    def __init__(
        __self__,
        *,
        custom_dns_server_ip: pulumi.Input[_builtins.str],
        custom_dns_server_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customDnsServerIp")
    def custom_dns_server_ip(self) -> pulumi.Input[_builtins.str]: ...
    @custom_dns_server_ip.setter
    def custom_dns_server_ip(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customDnsServerName")
    def custom_dns_server_name(self) -> pulumi.Input[_builtins.str]: ...
    @custom_dns_server_name.setter
    def custom_dns_server_name(self, value: pulumi.Input[_builtins.str]): ...

class KxEnvironmentTransitGatewayConfigurationArgsDict(TypedDict):
    routable_cidr_space: pulumi.Input[_builtins.str]
    transit_gateway_id: pulumi.Input[_builtins.str]
    attachment_network_acl_configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class KxEnvironmentTransitGatewayConfigurationArgs:
    def __init__(
        __self__,
        *,
        routable_cidr_space: pulumi.Input[_builtins.str],
        transit_gateway_id: pulumi.Input[_builtins.str],
        attachment_network_acl_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routableCidrSpace")
    def routable_cidr_space(self) -> pulumi.Input[_builtins.str]: ...
    @routable_cidr_space.setter
    def routable_cidr_space(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Input[_builtins.str]: ...
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="attachmentNetworkAclConfigurations")
    def attachment_network_acl_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @attachment_network_acl_configurations.setter
    def attachment_network_acl_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...

class KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationArgsDict(
    TypedDict
):
    cidr_block: pulumi.Input[_builtins.str]
    protocol: pulumi.Input[_builtins.str]
    rule_action: pulumi.Input[_builtins.str]
    rule_number: pulumi.Input[_builtins.int]
    icmp_type_code: NotRequired[
        pulumi.Input[
            KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationIcmpTypeCodeArgsDict
        ]
    ]
    port_range: NotRequired[
        pulumi.Input[
            KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationPortRangeArgsDict
        ]
    ]
    ...

@pulumi.input_type
class KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationArgs:
    def __init__(
        __self__,
        *,
        cidr_block: pulumi.Input[_builtins.str],
        protocol: pulumi.Input[_builtins.str],
        rule_action: pulumi.Input[_builtins.str],
        rule_number: pulumi.Input[_builtins.int],
        icmp_type_code: Optional[
            pulumi.Input[
                KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationIcmpTypeCodeArgs
            ]
        ] = ...,
        port_range: Optional[
            pulumi.Input[
                KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationPortRangeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Input[_builtins.str]: ...
    @cidr_block.setter
    def cidr_block(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Input[_builtins.str]: ...
    @rule_action.setter
    def rule_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> pulumi.Input[_builtins.int]: ...
    @rule_number.setter
    def rule_number(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="icmpTypeCode")
    def icmp_type_code(
        self,
    ) -> Optional[
        pulumi.Input[
            KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationIcmpTypeCodeArgs
        ]
    ]: ...
    @icmp_type_code.setter
    def icmp_type_code(
        self,
        value: Optional[
            pulumi.Input[
                KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationIcmpTypeCodeArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="portRange")
    def port_range(
        self,
    ) -> Optional[
        pulumi.Input[
            KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationPortRangeArgs
        ]
    ]: ...
    @port_range.setter
    def port_range(
        self,
        value: Optional[
            pulumi.Input[
                KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationPortRangeArgs
            ]
        ],
    ): ...

class KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationIcmpTypeCodeArgsDict(
    TypedDict
):
    code: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationIcmpTypeCodeArgs:
    def __init__(
        __self__,
        *,
        code: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Input[_builtins.int]: ...
    @code.setter
    def code(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.int]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.int]): ...

class KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationPortRangeArgsDict(
    TypedDict
):
    from_: pulumi.Input[_builtins.int]
    to: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class KxEnvironmentTransitGatewayConfigurationAttachmentNetworkAclConfigurationPortRangeArgs:
    def __init__(
        __self__, *, from_: pulumi.Input[_builtins.int], to: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[_builtins.int]: ...
    @from_.setter
    def from_(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> pulumi.Input[_builtins.int]: ...
    @to.setter
    def to(self, value: pulumi.Input[_builtins.int]): ...

class KxVolumeAttachedClusterArgsDict(TypedDict):
    cluster_name: pulumi.Input[_builtins.str]
    cluster_status: pulumi.Input[_builtins.str]
    cluster_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class KxVolumeAttachedClusterArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        cluster_status: pulumi.Input[_builtins.str],
        cluster_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterStatus")
    def cluster_status(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_status.setter
    def cluster_status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_type.setter
    def cluster_type(self, value: pulumi.Input[_builtins.str]): ...

class KxVolumeNas1ConfigurationArgsDict(TypedDict):
    size: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class KxVolumeNas1ConfigurationArgs:
    def __init__(
        __self__,
        *,
        size: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]: ...
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
