import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterAutoscalingSettingsArgs",
    "ClusterAutoscalingSettingsArgsDict",
    "ClusterAutoscalingSettingsAutoscalingPolicyArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterDatastoreMountConfigArgs",
    "ClusterDatastoreMountConfigArgsDict",
    "ClusterDatastoreMountConfigDatastoreNetworkArgs",
    ...,
    "ClusterNodeTypeConfigArgs",
    "ClusterNodeTypeConfigArgsDict",
    "DatastoreNfsDatastoreArgs",
    "DatastoreNfsDatastoreArgsDict",
    "DatastoreNfsDatastoreGoogleFileServiceArgs",
    "DatastoreNfsDatastoreGoogleFileServiceArgsDict",
    "DatastoreNfsDatastoreThirdPartyFileServiceArgs",
    "DatastoreNfsDatastoreThirdPartyFileServiceArgsDict",
    "ExternalAccessRuleDestinationIpRangeArgs",
    "ExternalAccessRuleDestinationIpRangeArgsDict",
    "ExternalAccessRuleSourceIpRangeArgs",
    "ExternalAccessRuleSourceIpRangeArgsDict",
    "NetworkPolicyExternalIpArgs",
    "NetworkPolicyExternalIpArgsDict",
    "NetworkPolicyInternetAccessArgs",
    "NetworkPolicyInternetAccessArgsDict",
    "NetworkVpcNetworkArgs",
    "NetworkVpcNetworkArgsDict",
    "PrivateCloudHcxArgs",
    "PrivateCloudHcxArgsDict",
    "PrivateCloudManagementClusterArgs",
    "PrivateCloudManagementClusterArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PrivateCloudManagementClusterNodeTypeConfigArgs",
    ...,
    ...,
    ...,
    "PrivateCloudNetworkConfigArgs",
    "PrivateCloudNetworkConfigArgsDict",
    "PrivateCloudNsxArgs",
    "PrivateCloudNsxArgsDict",
    "PrivateCloudVcenterArgs",
    "PrivateCloudVcenterArgsDict",
    "SubnetDhcpAddressRangeArgs",
    "SubnetDhcpAddressRangeArgsDict",
]

class ClusterAutoscalingSettingsArgsDict(TypedDict):
    autoscaling_policies: pulumi.Input[
        Sequence[pulumi.Input[ClusterAutoscalingSettingsAutoscalingPolicyArgsDict]]
    ]
    cool_down_period: NotRequired[pulumi.Input[_builtins.str]]
    max_cluster_node_count: NotRequired[pulumi.Input[_builtins.int]]
    min_cluster_node_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterAutoscalingSettingsArgs:
    def __init__(
        __self__,
        *,
        autoscaling_policies: pulumi.Input[
            Sequence[pulumi.Input[ClusterAutoscalingSettingsAutoscalingPolicyArgs]]
        ],
        cool_down_period: Optional[pulumi.Input[_builtins.str]] = ...,
        max_cluster_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_cluster_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicies")
    def autoscaling_policies(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ClusterAutoscalingSettingsAutoscalingPolicyArgs]]
    ]: ...
    @autoscaling_policies.setter
    def autoscaling_policies(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ClusterAutoscalingSettingsAutoscalingPolicyArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="coolDownPeriod")
    def cool_down_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cool_down_period.setter
    def cool_down_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxClusterNodeCount")
    def max_cluster_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_cluster_node_count.setter
    def max_cluster_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minClusterNodeCount")
    def min_cluster_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_cluster_node_count.setter
    def min_cluster_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterAutoscalingSettingsAutoscalingPolicyArgsDict(TypedDict):
    autoscale_policy_id: pulumi.Input[_builtins.str]
    node_type_id: pulumi.Input[_builtins.str]
    scale_out_size: pulumi.Input[_builtins.int]
    consumed_memory_thresholds: NotRequired[
        pulumi.Input[
            ClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgsDict
        ]
    ]
    cpu_thresholds: NotRequired[
        pulumi.Input[ClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgsDict]
    ]
    storage_thresholds: NotRequired[
        pulumi.Input[
            ClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgsDict
        ]
    ]

@pulumi.input_type
class ClusterAutoscalingSettingsAutoscalingPolicyArgs:
    def __init__(
        __self__,
        *,
        autoscale_policy_id: pulumi.Input[_builtins.str],
        node_type_id: pulumi.Input[_builtins.str],
        scale_out_size: pulumi.Input[_builtins.int],
        consumed_memory_thresholds: Optional[
            pulumi.Input[
                ClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgs
            ]
        ] = ...,
        cpu_thresholds: Optional[
            pulumi.Input[ClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgs]
        ] = ...,
        storage_thresholds: Optional[
            pulumi.Input[
                ClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalePolicyId")
    def autoscale_policy_id(self) -> pulumi.Input[_builtins.str]: ...
    @autoscale_policy_id.setter
    def autoscale_policy_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> pulumi.Input[_builtins.str]: ...
    @node_type_id.setter
    def node_type_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scaleOutSize")
    def scale_out_size(self) -> pulumi.Input[_builtins.int]: ...
    @scale_out_size.setter
    def scale_out_size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="consumedMemoryThresholds")
    def consumed_memory_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgs
        ]
    ]: ...
    @consumed_memory_thresholds.setter
    def consumed_memory_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                ClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cpuThresholds")
    def cpu_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[ClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgs]
    ]: ...
    @cpu_thresholds.setter
    def cpu_thresholds(
        self,
        value: Optional[
            pulumi.Input[ClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageThresholds")
    def storage_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[ClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgs]
    ]: ...
    @storage_thresholds.setter
    def storage_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                ClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgs
            ]
        ],
    ): ...

class ClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgsDict(
    TypedDict
):
    scale_in: pulumi.Input[_builtins.int]
    scale_out: pulumi.Input[_builtins.int]

@pulumi.input_type
class ClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgs:
    def __init__(
        __self__,
        *,
        scale_in: pulumi.Input[_builtins.int],
        scale_out: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> pulumi.Input[_builtins.int]: ...
    @scale_in.setter
    def scale_in(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> pulumi.Input[_builtins.int]: ...
    @scale_out.setter
    def scale_out(self, value: pulumi.Input[_builtins.int]): ...

class ClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgsDict(TypedDict):
    scale_in: pulumi.Input[_builtins.int]
    scale_out: pulumi.Input[_builtins.int]

@pulumi.input_type
class ClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgs:
    def __init__(
        __self__,
        *,
        scale_in: pulumi.Input[_builtins.int],
        scale_out: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> pulumi.Input[_builtins.int]: ...
    @scale_in.setter
    def scale_in(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> pulumi.Input[_builtins.int]: ...
    @scale_out.setter
    def scale_out(self, value: pulumi.Input[_builtins.int]): ...

class ClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgsDict(TypedDict):
    scale_in: pulumi.Input[_builtins.int]
    scale_out: pulumi.Input[_builtins.int]

@pulumi.input_type
class ClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgs:
    def __init__(
        __self__,
        *,
        scale_in: pulumi.Input[_builtins.int],
        scale_out: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> pulumi.Input[_builtins.int]: ...
    @scale_in.setter
    def scale_in(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> pulumi.Input[_builtins.int]: ...
    @scale_out.setter
    def scale_out(self, value: pulumi.Input[_builtins.int]): ...

class ClusterDatastoreMountConfigArgsDict(TypedDict):
    datastore: pulumi.Input[_builtins.str]
    datastore_network: pulumi.Input[ClusterDatastoreMountConfigDatastoreNetworkArgsDict]
    access_mode: NotRequired[pulumi.Input[_builtins.str]]
    file_share: NotRequired[pulumi.Input[_builtins.str]]
    ignore_colocation: NotRequired[pulumi.Input[_builtins.bool]]
    nfs_version: NotRequired[pulumi.Input[_builtins.str]]
    servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterDatastoreMountConfigArgs:
    def __init__(
        __self__,
        *,
        datastore: pulumi.Input[_builtins.str],
        datastore_network: pulumi.Input[
            ClusterDatastoreMountConfigDatastoreNetworkArgs
        ],
        access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_colocation: Optional[pulumi.Input[_builtins.bool]] = ...,
        nfs_version: Optional[pulumi.Input[_builtins.str]] = ...,
        servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> pulumi.Input[_builtins.str]: ...
    @datastore.setter
    def datastore(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="datastoreNetwork")
    def datastore_network(
        self,
    ) -> pulumi.Input[ClusterDatastoreMountConfigDatastoreNetworkArgs]: ...
    @datastore_network.setter
    def datastore_network(
        self, value: pulumi.Input[ClusterDatastoreMountConfigDatastoreNetworkArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_mode.setter
    def access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileShare")
    def file_share(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_share.setter
    def file_share(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreColocation")
    def ignore_colocation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_colocation.setter
    def ignore_colocation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="nfsVersion")
    def nfs_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nfs_version.setter
    def nfs_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @servers.setter
    def servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterDatastoreMountConfigDatastoreNetworkArgsDict(TypedDict):
    subnet: pulumi.Input[_builtins.str]
    connection_count: NotRequired[pulumi.Input[_builtins.int]]
    mtu: NotRequired[pulumi.Input[_builtins.int]]
    network_peering: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterDatastoreMountConfigDatastoreNetworkArgs:
    def __init__(
        __self__,
        *,
        subnet: pulumi.Input[_builtins.str],
        connection_count: Optional[pulumi.Input[_builtins.int]] = ...,
        mtu: Optional[pulumi.Input[_builtins.int]] = ...,
        network_peering: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> pulumi.Input[_builtins.str]: ...
    @subnet.setter
    def subnet(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectionCount")
    def connection_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_count.setter
    def connection_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="networkPeering")
    def network_peering(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_peering.setter
    def network_peering(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeTypeConfigArgsDict(TypedDict):
    node_count: pulumi.Input[_builtins.int]
    node_type_id: pulumi.Input[_builtins.str]
    custom_core_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterNodeTypeConfigArgs:
    def __init__(
        __self__,
        *,
        node_count: pulumi.Input[_builtins.int],
        node_type_id: pulumi.Input[_builtins.str],
        custom_core_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Input[_builtins.int]: ...
    @node_count.setter
    def node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> pulumi.Input[_builtins.str]: ...
    @node_type_id.setter
    def node_type_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customCoreCount")
    def custom_core_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @custom_core_count.setter
    def custom_core_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DatastoreNfsDatastoreArgsDict(TypedDict):
    google_file_service: NotRequired[
        pulumi.Input[DatastoreNfsDatastoreGoogleFileServiceArgsDict]
    ]
    third_party_file_service: NotRequired[
        pulumi.Input[DatastoreNfsDatastoreThirdPartyFileServiceArgsDict]
    ]

@pulumi.input_type
class DatastoreNfsDatastoreArgs:
    def __init__(
        __self__,
        *,
        google_file_service: Optional[
            pulumi.Input[DatastoreNfsDatastoreGoogleFileServiceArgs]
        ] = ...,
        third_party_file_service: Optional[
            pulumi.Input[DatastoreNfsDatastoreThirdPartyFileServiceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="googleFileService")
    def google_file_service(
        self,
    ) -> Optional[pulumi.Input[DatastoreNfsDatastoreGoogleFileServiceArgs]]: ...
    @google_file_service.setter
    def google_file_service(
        self, value: Optional[pulumi.Input[DatastoreNfsDatastoreGoogleFileServiceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="thirdPartyFileService")
    def third_party_file_service(
        self,
    ) -> Optional[pulumi.Input[DatastoreNfsDatastoreThirdPartyFileServiceArgs]]: ...
    @third_party_file_service.setter
    def third_party_file_service(
        self,
        value: Optional[pulumi.Input[DatastoreNfsDatastoreThirdPartyFileServiceArgs]],
    ): ...

class DatastoreNfsDatastoreGoogleFileServiceArgsDict(TypedDict):
    filestore_instance: NotRequired[pulumi.Input[_builtins.str]]
    netapp_volume: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatastoreNfsDatastoreGoogleFileServiceArgs:
    def __init__(
        __self__,
        *,
        filestore_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        netapp_volume: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filestoreInstance")
    def filestore_instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filestore_instance.setter
    def filestore_instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="netappVolume")
    def netapp_volume(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @netapp_volume.setter
    def netapp_volume(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatastoreNfsDatastoreThirdPartyFileServiceArgsDict(TypedDict):
    file_share: pulumi.Input[_builtins.str]
    network: pulumi.Input[_builtins.str]
    servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class DatastoreNfsDatastoreThirdPartyFileServiceArgs:
    def __init__(
        __self__,
        *,
        file_share: pulumi.Input[_builtins.str],
        network: pulumi.Input[_builtins.str],
        servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileShare")
    def file_share(self) -> pulumi.Input[_builtins.str]: ...
    @file_share.setter
    def file_share(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def servers(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @servers.setter
    def servers(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ExternalAccessRuleDestinationIpRangeArgsDict(TypedDict):
    external_address: NotRequired[pulumi.Input[_builtins.str]]
    ip_address_range: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExternalAccessRuleDestinationIpRangeArgs:
    def __init__(
        __self__,
        *,
        external_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address_range: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalAddress")
    def external_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_address.setter
    def external_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressRange")
    def ip_address_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_range.setter
    def ip_address_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExternalAccessRuleSourceIpRangeArgsDict(TypedDict):
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    ip_address_range: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExternalAccessRuleSourceIpRangeArgs:
    def __init__(
        __self__,
        *,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address_range: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressRange")
    def ip_address_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_range.setter
    def ip_address_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkPolicyExternalIpArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkPolicyExternalIpArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkPolicyInternetAccessArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkPolicyInternetAccessArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkVpcNetworkArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkVpcNetworkArgs:
    def __init__(
        __self__,
        *,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateCloudHcxArgsDict(TypedDict):
    fqdn: NotRequired[pulumi.Input[_builtins.str]]
    internal_ip: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateCloudHcxArgs:
    def __init__(
        __self__,
        *,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        internal_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @internal_ip.setter
    def internal_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateCloudManagementClusterArgsDict(TypedDict):
    cluster_id: pulumi.Input[_builtins.str]
    autoscaling_settings: NotRequired[
        pulumi.Input[PrivateCloudManagementClusterAutoscalingSettingsArgsDict]
    ]
    node_type_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PrivateCloudManagementClusterNodeTypeConfigArgsDict]]
        ]
    ]
    stretched_cluster_config: NotRequired[
        pulumi.Input[PrivateCloudManagementClusterStretchedClusterConfigArgsDict]
    ]

@pulumi.input_type
class PrivateCloudManagementClusterArgs:
    def __init__(
        __self__,
        *,
        cluster_id: pulumi.Input[_builtins.str],
        autoscaling_settings: Optional[
            pulumi.Input[PrivateCloudManagementClusterAutoscalingSettingsArgs]
        ] = ...,
        node_type_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PrivateCloudManagementClusterNodeTypeConfigArgs]]
            ]
        ] = ...,
        stretched_cluster_config: Optional[
            pulumi.Input[PrivateCloudManagementClusterStretchedClusterConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingSettings")
    def autoscaling_settings(
        self,
    ) -> Optional[
        pulumi.Input[PrivateCloudManagementClusterAutoscalingSettingsArgs]
    ]: ...
    @autoscaling_settings.setter
    def autoscaling_settings(
        self,
        value: Optional[
            pulumi.Input[PrivateCloudManagementClusterAutoscalingSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PrivateCloudManagementClusterNodeTypeConfigArgs]]
        ]
    ]: ...
    @node_type_configs.setter
    def node_type_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PrivateCloudManagementClusterNodeTypeConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stretchedClusterConfig")
    def stretched_cluster_config(
        self,
    ) -> Optional[
        pulumi.Input[PrivateCloudManagementClusterStretchedClusterConfigArgs]
    ]: ...
    @stretched_cluster_config.setter
    def stretched_cluster_config(
        self,
        value: Optional[
            pulumi.Input[PrivateCloudManagementClusterStretchedClusterConfigArgs]
        ],
    ): ...

class PrivateCloudManagementClusterAutoscalingSettingsArgsDict(TypedDict):
    autoscaling_policies: pulumi.Input[
        Sequence[
            pulumi.Input[
                PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyArgsDict
            ]
        ]
    ]
    cool_down_period: NotRequired[pulumi.Input[_builtins.str]]
    max_cluster_node_count: NotRequired[pulumi.Input[_builtins.int]]
    min_cluster_node_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class PrivateCloudManagementClusterAutoscalingSettingsArgs:
    def __init__(
        __self__,
        *,
        autoscaling_policies: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyArgs
                ]
            ]
        ],
        cool_down_period: Optional[pulumi.Input[_builtins.str]] = ...,
        max_cluster_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_cluster_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicies")
    def autoscaling_policies(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyArgs
            ]
        ]
    ]: ...
    @autoscaling_policies.setter
    def autoscaling_policies(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="coolDownPeriod")
    def cool_down_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cool_down_period.setter
    def cool_down_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxClusterNodeCount")
    def max_cluster_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_cluster_node_count.setter
    def max_cluster_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minClusterNodeCount")
    def min_cluster_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_cluster_node_count.setter
    def min_cluster_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyArgsDict(
    TypedDict
):
    autoscale_policy_id: pulumi.Input[_builtins.str]
    node_type_id: pulumi.Input[_builtins.str]
    scale_out_size: pulumi.Input[_builtins.int]
    consumed_memory_thresholds: NotRequired[
        pulumi.Input[
            PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgsDict
        ]
    ]
    cpu_thresholds: NotRequired[
        pulumi.Input[
            PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgsDict
        ]
    ]
    storage_thresholds: NotRequired[
        pulumi.Input[
            PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgsDict
        ]
    ]

@pulumi.input_type
class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyArgs:
    def __init__(
        __self__,
        *,
        autoscale_policy_id: pulumi.Input[_builtins.str],
        node_type_id: pulumi.Input[_builtins.str],
        scale_out_size: pulumi.Input[_builtins.int],
        consumed_memory_thresholds: Optional[
            pulumi.Input[
                PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgs
            ]
        ] = ...,
        cpu_thresholds: Optional[
            pulumi.Input[
                PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgs
            ]
        ] = ...,
        storage_thresholds: Optional[
            pulumi.Input[
                PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalePolicyId")
    def autoscale_policy_id(self) -> pulumi.Input[_builtins.str]: ...
    @autoscale_policy_id.setter
    def autoscale_policy_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> pulumi.Input[_builtins.str]: ...
    @node_type_id.setter
    def node_type_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scaleOutSize")
    def scale_out_size(self) -> pulumi.Input[_builtins.int]: ...
    @scale_out_size.setter
    def scale_out_size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="consumedMemoryThresholds")
    def consumed_memory_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgs
        ]
    ]: ...
    @consumed_memory_thresholds.setter
    def consumed_memory_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cpuThresholds")
    def cpu_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgs
        ]
    ]: ...
    @cpu_thresholds.setter
    def cpu_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageThresholds")
    def storage_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgs
        ]
    ]: ...
    @storage_thresholds.setter
    def storage_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgs
            ]
        ],
    ): ...

class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgsDict(
    TypedDict
):
    scale_in: pulumi.Input[_builtins.int]
    scale_out: pulumi.Input[_builtins.int]

@pulumi.input_type
class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholdsArgs:
    def __init__(
        __self__,
        *,
        scale_in: pulumi.Input[_builtins.int],
        scale_out: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> pulumi.Input[_builtins.int]: ...
    @scale_in.setter
    def scale_in(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> pulumi.Input[_builtins.int]: ...
    @scale_out.setter
    def scale_out(self, value: pulumi.Input[_builtins.int]): ...

class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgsDict(
    TypedDict
):
    scale_in: pulumi.Input[_builtins.int]
    scale_out: pulumi.Input[_builtins.int]

@pulumi.input_type
class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyCpuThresholdsArgs:
    def __init__(
        __self__,
        *,
        scale_in: pulumi.Input[_builtins.int],
        scale_out: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> pulumi.Input[_builtins.int]: ...
    @scale_in.setter
    def scale_in(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> pulumi.Input[_builtins.int]: ...
    @scale_out.setter
    def scale_out(self, value: pulumi.Input[_builtins.int]): ...

class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgsDict(
    TypedDict
):
    scale_in: pulumi.Input[_builtins.int]
    scale_out: pulumi.Input[_builtins.int]

@pulumi.input_type
class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyStorageThresholdsArgs:
    def __init__(
        __self__,
        *,
        scale_in: pulumi.Input[_builtins.int],
        scale_out: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> pulumi.Input[_builtins.int]: ...
    @scale_in.setter
    def scale_in(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> pulumi.Input[_builtins.int]: ...
    @scale_out.setter
    def scale_out(self, value: pulumi.Input[_builtins.int]): ...

class PrivateCloudManagementClusterNodeTypeConfigArgsDict(TypedDict):
    node_count: pulumi.Input[_builtins.int]
    node_type_id: pulumi.Input[_builtins.str]
    custom_core_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class PrivateCloudManagementClusterNodeTypeConfigArgs:
    def __init__(
        __self__,
        *,
        node_count: pulumi.Input[_builtins.int],
        node_type_id: pulumi.Input[_builtins.str],
        custom_core_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Input[_builtins.int]: ...
    @node_count.setter
    def node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> pulumi.Input[_builtins.str]: ...
    @node_type_id.setter
    def node_type_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customCoreCount")
    def custom_core_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @custom_core_count.setter
    def custom_core_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PrivateCloudManagementClusterStretchedClusterConfigArgsDict(TypedDict):
    preferred_location: NotRequired[pulumi.Input[_builtins.str]]
    secondary_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateCloudManagementClusterStretchedClusterConfigArgs:
    def __init__(
        __self__,
        *,
        preferred_location: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredLocation")
    def preferred_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_location.setter
    def preferred_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryLocation")
    def secondary_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_location.setter
    def secondary_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateCloudNetworkConfigArgsDict(TypedDict):
    management_cidr: pulumi.Input[_builtins.str]
    dns_server_ip: NotRequired[pulumi.Input[_builtins.str]]
    management_ip_address_layout_version: NotRequired[pulumi.Input[_builtins.int]]
    vmware_engine_network: NotRequired[pulumi.Input[_builtins.str]]
    vmware_engine_network_canonical: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateCloudNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        management_cidr: pulumi.Input[_builtins.str],
        dns_server_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        management_ip_address_layout_version: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        vmware_engine_network: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network_canonical: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managementCidr")
    def management_cidr(self) -> pulumi.Input[_builtins.str]: ...
    @management_cidr.setter
    def management_cidr(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dnsServerIp")
    def dns_server_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_server_ip.setter
    def dns_server_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managementIpAddressLayoutVersion")
    def management_ip_address_layout_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @management_ip_address_layout_version.setter
    def management_ip_address_layout_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vmware_engine_network.setter
    def vmware_engine_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetworkCanonical")
    def vmware_engine_network_canonical(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vmware_engine_network_canonical.setter
    def vmware_engine_network_canonical(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PrivateCloudNsxArgsDict(TypedDict):
    fqdn: NotRequired[pulumi.Input[_builtins.str]]
    internal_ip: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateCloudNsxArgs:
    def __init__(
        __self__,
        *,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        internal_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @internal_ip.setter
    def internal_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateCloudVcenterArgsDict(TypedDict):
    fqdn: NotRequired[pulumi.Input[_builtins.str]]
    internal_ip: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateCloudVcenterArgs:
    def __init__(
        __self__,
        *,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        internal_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @internal_ip.setter
    def internal_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubnetDhcpAddressRangeArgsDict(TypedDict):
    first_address: NotRequired[pulumi.Input[_builtins.str]]
    last_address: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubnetDhcpAddressRangeArgs:
    def __init__(
        __self__,
        *,
        first_address: Optional[pulumi.Input[_builtins.str]] = ...,
        last_address: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="firstAddress")
    def first_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @first_address.setter
    def first_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastAddress")
    def last_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_address.setter
    def last_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
