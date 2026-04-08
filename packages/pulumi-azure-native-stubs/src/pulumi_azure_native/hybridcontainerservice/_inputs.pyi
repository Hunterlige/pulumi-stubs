import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AADProfileArgs",
    "AADProfileArgsDict",
    "AddonProfilesArgs",
    "AddonProfilesArgsDict",
    "AgentPoolExtendedLocationArgs",
    "AgentPoolExtendedLocationArgsDict",
    "AgentPoolProvisioningStatusErrorArgs",
    "AgentPoolProvisioningStatusErrorArgsDict",
    "AgentPoolProvisioningStatusProvisioningStatusArgs",
    ...,
    "AgentPoolProvisioningStatusStatusArgs",
    "AgentPoolProvisioningStatusStatusArgsDict",
    "ArcAgentProfileArgs",
    "ArcAgentProfileArgsDict",
    "CloudProviderProfileInfraNetworkProfileArgs",
    "CloudProviderProfileInfraNetworkProfileArgsDict",
    "CloudProviderProfileInfraStorageProfileArgs",
    "CloudProviderProfileInfraStorageProfileArgsDict",
    "CloudProviderProfileArgs",
    "CloudProviderProfileArgsDict",
    ...,
    ...,
    "ControlPlaneProfileArgs",
    "ControlPlaneProfileArgsDict",
    "ExtendedLocationArgs",
    "ExtendedLocationArgsDict",
    "HttpProxyConfigArgs",
    "HttpProxyConfigArgsDict",
    "LinuxProfilePropertiesPublicKeysArgs",
    "LinuxProfilePropertiesPublicKeysArgsDict",
    "LinuxProfilePropertiesSshArgs",
    "LinuxProfilePropertiesSshArgsDict",
    "LinuxProfilePropertiesArgs",
    "LinuxProfilePropertiesArgsDict",
    "LoadBalancerProfileArgs",
    "LoadBalancerProfileArgsDict",
    "NamedAgentPoolProfileArgs",
    "NamedAgentPoolProfileArgsDict",
    "NetworkProfileArgs",
    "NetworkProfileArgsDict",
    "ProvisionedClusterIdentityArgs",
    "ProvisionedClusterIdentityArgsDict",
    "ProvisionedClustersAllPropertiesArgs",
    "ProvisionedClustersAllPropertiesArgsDict",
    "ProvisionedClustersCommonPropertiesFeaturesArgs",
    ...,
    "ProvisionedClustersExtendedLocationArgs",
    "ProvisionedClustersExtendedLocationArgsDict",
    "StorageSpacesExtendedLocationArgs",
    "StorageSpacesExtendedLocationArgsDict",
    "StorageSpacesPropertiesErrorArgs",
    "StorageSpacesPropertiesErrorArgsDict",
    "StorageSpacesPropertiesHciStorageProfileArgs",
    "StorageSpacesPropertiesHciStorageProfileArgsDict",
    "StorageSpacesPropertiesProvisioningStatusArgs",
    "StorageSpacesPropertiesProvisioningStatusArgsDict",
    "StorageSpacesPropertiesStatusArgs",
    "StorageSpacesPropertiesStatusArgsDict",
    "StorageSpacesPropertiesVmwareStorageProfileArgs",
    ...,
    "StorageSpacesPropertiesArgs",
    "StorageSpacesPropertiesArgsDict",
    "VirtualNetworksExtendedLocationArgs",
    "VirtualNetworksExtendedLocationArgsDict",
    "VirtualNetworksPropertiesHciArgs",
    "VirtualNetworksPropertiesHciArgsDict",
    "VirtualNetworksPropertiesInfraVnetProfileArgs",
    "VirtualNetworksPropertiesInfraVnetProfileArgsDict",
    "VirtualNetworksPropertiesNetworkCloudArgs",
    "VirtualNetworksPropertiesNetworkCloudArgsDict",
    "VirtualNetworksPropertiesVipPoolArgs",
    "VirtualNetworksPropertiesVipPoolArgsDict",
    "VirtualNetworksPropertiesVmipPoolArgs",
    "VirtualNetworksPropertiesVmipPoolArgsDict",
    "VirtualNetworksPropertiesVmwareArgs",
    "VirtualNetworksPropertiesVmwareArgsDict",
    "VirtualNetworksPropertiesArgs",
    "VirtualNetworksPropertiesArgsDict",
    "WindowsProfileArgs",
    "WindowsProfileArgsDict",
]

class AADProfileArgsDict(TypedDict):
    admin_group_object_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    client_app_id: NotRequired[pulumi.Input[_builtins.str]]
    enable_azure_rbac: NotRequired[pulumi.Input[_builtins.bool]]
    managed: NotRequired[pulumi.Input[_builtins.bool]]
    server_app_id: NotRequired[pulumi.Input[_builtins.str]]
    server_app_secret: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AADProfileArgs:
    def __init__(
        __self__,
        *,
        admin_group_object_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        client_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_azure_rbac: Optional[pulumi.Input[_builtins.bool]] = ...,
        managed: Optional[pulumi.Input[_builtins.bool]] = ...,
        server_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        server_app_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminGroupObjectIDs")
    def admin_group_object_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @admin_group_object_ids.setter
    def admin_group_object_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientAppID")
    def client_app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_app_id.setter
    def client_app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAzureRbac")
    def enable_azure_rbac(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_azure_rbac.setter
    def enable_azure_rbac(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def managed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @managed.setter
    def managed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serverAppID")
    def server_app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_app_id.setter
    def server_app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverAppSecret")
    def server_app_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_app_secret.setter
    def server_app_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantID")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AddonProfilesArgsDict(TypedDict):
    config: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AddonProfilesArgs:
    def __init__(
        __self__,
        *,
        config: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @config.setter
    def config(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentPoolExtendedLocationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentPoolExtendedLocationArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentPoolProvisioningStatusErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentPoolProvisioningStatusErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentPoolProvisioningStatusProvisioningStatusArgsDict(TypedDict):
    error: NotRequired[pulumi.Input[AgentPoolProvisioningStatusErrorArgsDict]]
    operation_id: NotRequired[pulumi.Input[_builtins.str]]
    phase: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentPoolProvisioningStatusProvisioningStatusArgs:
    def __init__(
        __self__,
        *,
        error: Optional[pulumi.Input[AgentPoolProvisioningStatusErrorArgs]] = ...,
        operation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        phase: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[AgentPoolProvisioningStatusErrorArgs]]: ...
    @error.setter
    def error(
        self, value: Optional[pulumi.Input[AgentPoolProvisioningStatusErrorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operation_id.setter
    def operation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def phase(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phase.setter
    def phase(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentPoolProvisioningStatusStatusArgsDict(TypedDict):
    error_message: NotRequired[pulumi.Input[_builtins.str]]
    provisioning_status: NotRequired[
        pulumi.Input[AgentPoolProvisioningStatusProvisioningStatusArgsDict]
    ]
    ready_replicas: NotRequired[pulumi.Input[_builtins.int]]
    replicas: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AgentPoolProvisioningStatusStatusArgs:
    def __init__(
        __self__,
        *,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_status: Optional[
            pulumi.Input[AgentPoolProvisioningStatusProvisioningStatusArgs]
        ] = ...,
        ready_replicas: Optional[pulumi.Input[_builtins.int]] = ...,
        replicas: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatus")
    def provisioning_status(
        self,
    ) -> Optional[pulumi.Input[AgentPoolProvisioningStatusProvisioningStatusArgs]]: ...
    @provisioning_status.setter
    def provisioning_status(
        self,
        value: Optional[
            pulumi.Input[AgentPoolProvisioningStatusProvisioningStatusArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="readyReplicas")
    def ready_replicas(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ready_replicas.setter
    def ready_replicas(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ArcAgentProfileArgsDict(TypedDict):
    agent_auto_upgrade: NotRequired[
        pulumi.Input[Union[_builtins.str, AutoUpgradeOptions]]
    ]
    agent_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ArcAgentProfileArgs:
    def __init__(
        __self__,
        *,
        agent_auto_upgrade: Optional[
            pulumi.Input[Union[_builtins.str, AutoUpgradeOptions]]
        ] = ...,
        agent_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentAutoUpgrade")
    def agent_auto_upgrade(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AutoUpgradeOptions]]]: ...
    @agent_auto_upgrade.setter
    def agent_auto_upgrade(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AutoUpgradeOptions]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_version.setter
    def agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudProviderProfileInfraNetworkProfileArgsDict(TypedDict):
    vnet_subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CloudProviderProfileInfraNetworkProfileArgs:
    def __init__(
        __self__,
        *,
        vnet_subnet_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vnetSubnetIds")
    def vnet_subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vnet_subnet_ids.setter
    def vnet_subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CloudProviderProfileInfraStorageProfileArgsDict(TypedDict):
    storage_space_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CloudProviderProfileInfraStorageProfileArgs:
    def __init__(
        __self__,
        *,
        storage_space_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageSpaceIds")
    def storage_space_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_space_ids.setter
    def storage_space_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CloudProviderProfileArgsDict(TypedDict):
    infra_network_profile: NotRequired[
        pulumi.Input[CloudProviderProfileInfraNetworkProfileArgsDict]
    ]
    infra_storage_profile: NotRequired[
        pulumi.Input[CloudProviderProfileInfraStorageProfileArgsDict]
    ]

@pulumi.input_type
class CloudProviderProfileArgs:
    def __init__(
        __self__,
        *,
        infra_network_profile: Optional[
            pulumi.Input[CloudProviderProfileInfraNetworkProfileArgs]
        ] = ...,
        infra_storage_profile: Optional[
            pulumi.Input[CloudProviderProfileInfraStorageProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infraNetworkProfile")
    def infra_network_profile(
        self,
    ) -> Optional[pulumi.Input[CloudProviderProfileInfraNetworkProfileArgs]]: ...
    @infra_network_profile.setter
    def infra_network_profile(
        self, value: Optional[pulumi.Input[CloudProviderProfileInfraNetworkProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="infraStorageProfile")
    def infra_storage_profile(
        self,
    ) -> Optional[pulumi.Input[CloudProviderProfileInfraStorageProfileArgs]]: ...
    @infra_storage_profile.setter
    def infra_storage_profile(
        self, value: Optional[pulumi.Input[CloudProviderProfileInfraStorageProfileArgs]]
    ): ...

class ControlPlaneEndpointProfileControlPlaneEndpointArgsDict(TypedDict):
    host_ip: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ControlPlaneEndpointProfileControlPlaneEndpointArgs:
    def __init__(
        __self__,
        *,
        host_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostIP")
    def host_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_ip.setter
    def host_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ControlPlaneProfileArgsDict(TypedDict):
    availability_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cloud_provider_profile: NotRequired[pulumi.Input[CloudProviderProfileArgsDict]]
    control_plane_endpoint: NotRequired[
        pulumi.Input[ControlPlaneEndpointProfileControlPlaneEndpointArgsDict]
    ]
    count: NotRequired[pulumi.Input[_builtins.int]]
    linux_profile: NotRequired[pulumi.Input[LinuxProfilePropertiesArgsDict]]
    max_count: NotRequired[pulumi.Input[_builtins.int]]
    max_pods: NotRequired[pulumi.Input[_builtins.int]]
    min_count: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, Mode]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    node_image_version: NotRequired[pulumi.Input[_builtins.str]]
    node_labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_taints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    os_type: NotRequired[pulumi.Input[Union[_builtins.str, OsType]]]
    vm_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ControlPlaneProfileArgs:
    def __init__(
        __self__,
        *,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cloud_provider_profile: Optional[pulumi.Input[CloudProviderProfileArgs]] = ...,
        control_plane_endpoint: Optional[
            pulumi.Input[ControlPlaneEndpointProfileControlPlaneEndpointArgs]
        ] = ...,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        linux_profile: Optional[pulumi.Input[LinuxProfilePropertiesArgs]] = ...,
        max_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_pods: Optional[pulumi.Input[_builtins.int]] = ...,
        min_count: Optional[pulumi.Input[_builtins.int]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, Mode]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_image_version: Optional[pulumi.Input[_builtins.str]] = ...,
        node_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        node_taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        os_type: Optional[pulumi.Input[Union[_builtins.str, OsType]]] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudProviderProfile")
    def cloud_provider_profile(
        self,
    ) -> Optional[pulumi.Input[CloudProviderProfileArgs]]: ...
    @cloud_provider_profile.setter
    def cloud_provider_profile(
        self, value: Optional[pulumi.Input[CloudProviderProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneEndpoint")
    def control_plane_endpoint(
        self,
    ) -> Optional[
        pulumi.Input[ControlPlaneEndpointProfileControlPlaneEndpointArgs]
    ]: ...
    @control_plane_endpoint.setter
    def control_plane_endpoint(
        self,
        value: Optional[
            pulumi.Input[ControlPlaneEndpointProfileControlPlaneEndpointArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> Optional[pulumi.Input[LinuxProfilePropertiesArgs]]: ...
    @linux_profile.setter
    def linux_profile(
        self, value: Optional[pulumi.Input[LinuxProfilePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_count.setter
    def max_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods.setter
    def max_pods(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_count.setter
    def min_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, Mode]]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, Mode]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_image_version.setter
    def node_image_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeLabels")
    def node_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @node_labels.setter
    def node_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeTaints")
    def node_taints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @node_taints.setter
    def node_taints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OsType]]]: ...
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OsType]]]): ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExtendedLocationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]

@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]
    ): ...

class HttpProxyConfigArgsDict(TypedDict):
    http_proxy: NotRequired[pulumi.Input[_builtins.str]]
    https_proxy: NotRequired[pulumi.Input[_builtins.str]]
    no_proxy: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    trusted_ca: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HttpProxyConfigArgs:
    def __init__(
        __self__,
        *,
        http_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
        https_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
        no_proxy: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        trusted_ca: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpProxy")
    def http_proxy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_proxy.setter
    def http_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @https_proxy.setter
    def https_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="noProxy")
    def no_proxy(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @no_proxy.setter
    def no_proxy(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trustedCa")
    def trusted_ca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trusted_ca.setter
    def trusted_ca(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LinuxProfilePropertiesPublicKeysArgsDict(TypedDict):
    key_data: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LinuxProfilePropertiesPublicKeysArgs:
    def __init__(
        __self__, *, key_data: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_data.setter
    def key_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LinuxProfilePropertiesSshArgsDict(TypedDict):
    public_keys: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LinuxProfilePropertiesPublicKeysArgsDict]]]
    ]

@pulumi.input_type
class LinuxProfilePropertiesSshArgs:
    def __init__(
        __self__,
        *,
        public_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[LinuxProfilePropertiesPublicKeysArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LinuxProfilePropertiesPublicKeysArgs]]]
    ]: ...
    @public_keys.setter
    def public_keys(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LinuxProfilePropertiesPublicKeysArgs]]]
        ],
    ): ...

class LinuxProfilePropertiesArgsDict(TypedDict):
    admin_username: NotRequired[pulumi.Input[_builtins.str]]
    ssh: NotRequired[pulumi.Input[LinuxProfilePropertiesSshArgsDict]]

@pulumi.input_type
class LinuxProfilePropertiesArgs:
    def __init__(
        __self__,
        *,
        admin_username: Optional[pulumi.Input[_builtins.str]] = ...,
        ssh: Optional[pulumi.Input[LinuxProfilePropertiesSshArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ssh(self) -> Optional[pulumi.Input[LinuxProfilePropertiesSshArgs]]: ...
    @ssh.setter
    def ssh(self, value: Optional[pulumi.Input[LinuxProfilePropertiesSshArgs]]): ...

class LoadBalancerProfileArgsDict(TypedDict):
    availability_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cloud_provider_profile: NotRequired[pulumi.Input[CloudProviderProfileArgsDict]]
    count: NotRequired[pulumi.Input[_builtins.int]]
    linux_profile: NotRequired[pulumi.Input[LinuxProfilePropertiesArgsDict]]
    max_count: NotRequired[pulumi.Input[_builtins.int]]
    max_pods: NotRequired[pulumi.Input[_builtins.int]]
    min_count: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, Mode]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    node_image_version: NotRequired[pulumi.Input[_builtins.str]]
    node_labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_taints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    os_type: NotRequired[pulumi.Input[Union[_builtins.str, OsType]]]
    vm_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LoadBalancerProfileArgs:
    def __init__(
        __self__,
        *,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cloud_provider_profile: Optional[pulumi.Input[CloudProviderProfileArgs]] = ...,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        linux_profile: Optional[pulumi.Input[LinuxProfilePropertiesArgs]] = ...,
        max_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_pods: Optional[pulumi.Input[_builtins.int]] = ...,
        min_count: Optional[pulumi.Input[_builtins.int]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, Mode]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_image_version: Optional[pulumi.Input[_builtins.str]] = ...,
        node_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        node_taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        os_type: Optional[pulumi.Input[Union[_builtins.str, OsType]]] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudProviderProfile")
    def cloud_provider_profile(
        self,
    ) -> Optional[pulumi.Input[CloudProviderProfileArgs]]: ...
    @cloud_provider_profile.setter
    def cloud_provider_profile(
        self, value: Optional[pulumi.Input[CloudProviderProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> Optional[pulumi.Input[LinuxProfilePropertiesArgs]]: ...
    @linux_profile.setter
    def linux_profile(
        self, value: Optional[pulumi.Input[LinuxProfilePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_count.setter
    def max_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods.setter
    def max_pods(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_count.setter
    def min_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, Mode]]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, Mode]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_image_version.setter
    def node_image_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeLabels")
    def node_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @node_labels.setter
    def node_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeTaints")
    def node_taints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @node_taints.setter
    def node_taints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OsType]]]: ...
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OsType]]]): ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamedAgentPoolProfileArgsDict(TypedDict):
    availability_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cloud_provider_profile: NotRequired[pulumi.Input[CloudProviderProfileArgsDict]]
    count: NotRequired[pulumi.Input[_builtins.int]]
    max_count: NotRequired[pulumi.Input[_builtins.int]]
    max_pods: NotRequired[pulumi.Input[_builtins.int]]
    min_count: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, Mode]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    node_image_version: NotRequired[pulumi.Input[_builtins.str]]
    node_labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_taints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    os_type: NotRequired[pulumi.Input[Union[_builtins.str, OsType]]]
    vm_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamedAgentPoolProfileArgs:
    def __init__(
        __self__,
        *,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cloud_provider_profile: Optional[pulumi.Input[CloudProviderProfileArgs]] = ...,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_pods: Optional[pulumi.Input[_builtins.int]] = ...,
        min_count: Optional[pulumi.Input[_builtins.int]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, Mode]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_image_version: Optional[pulumi.Input[_builtins.str]] = ...,
        node_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        node_taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        os_type: Optional[pulumi.Input[Union[_builtins.str, OsType]]] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudProviderProfile")
    def cloud_provider_profile(
        self,
    ) -> Optional[pulumi.Input[CloudProviderProfileArgs]]: ...
    @cloud_provider_profile.setter
    def cloud_provider_profile(
        self, value: Optional[pulumi.Input[CloudProviderProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_count.setter
    def max_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods.setter
    def max_pods(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_count.setter
    def min_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, Mode]]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, Mode]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_image_version.setter
    def node_image_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeLabels")
    def node_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @node_labels.setter
    def node_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeTaints")
    def node_taints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @node_taints.setter
    def node_taints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OsType]]]: ...
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OsType]]]): ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkProfileArgsDict(TypedDict):
    dns_service_ip: NotRequired[pulumi.Input[_builtins.str]]
    load_balancer_profile: NotRequired[pulumi.Input[LoadBalancerProfileArgsDict]]
    load_balancer_sku: NotRequired[pulumi.Input[Union[_builtins.str, LoadBalancerSku]]]
    network_policy: NotRequired[pulumi.Input[Union[_builtins.str, NetworkPolicy]]]
    pod_cidr: NotRequired[pulumi.Input[_builtins.str]]
    pod_cidrs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    service_cidr: NotRequired[pulumi.Input[_builtins.str]]
    service_cidrs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class NetworkProfileArgs:
    def __init__(
        __self__,
        *,
        dns_service_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancer_profile: Optional[pulumi.Input[LoadBalancerProfileArgs]] = ...,
        load_balancer_sku: Optional[
            pulumi.Input[Union[_builtins.str, LoadBalancerSku]]
        ] = ...,
        network_policy: Optional[
            pulumi.Input[Union[_builtins.str, NetworkPolicy]]
        ] = ...,
        pod_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        pod_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        service_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        service_cidrs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServiceIP")
    def dns_service_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_service_ip.setter
    def dns_service_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerProfile")
    def load_balancer_profile(
        self,
    ) -> Optional[pulumi.Input[LoadBalancerProfileArgs]]: ...
    @load_balancer_profile.setter
    def load_balancer_profile(
        self, value: Optional[pulumi.Input[LoadBalancerProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerSku")
    def load_balancer_sku(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LoadBalancerSku]]]: ...
    @load_balancer_sku.setter
    def load_balancer_sku(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LoadBalancerSku]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkPolicy")
    def network_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NetworkPolicy]]]: ...
    @network_policy.setter
    def network_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkPolicy]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="podCidr")
    def pod_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pod_cidr.setter
    def pod_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="podCidrs")
    def pod_cidrs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @pod_cidrs.setter
    def pod_cidrs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceCidr")
    def service_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_cidr.setter
    def service_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceCidrs")
    def service_cidrs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @service_cidrs.setter
    def service_cidrs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ProvisionedClusterIdentityArgsDict(TypedDict):
    type: pulumi.Input[ResourceIdentityType]

@pulumi.input_type
class ProvisionedClusterIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[ResourceIdentityType]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[ResourceIdentityType]: ...
    @type.setter
    def type(self, value: pulumi.Input[ResourceIdentityType]): ...

class ProvisionedClustersAllPropertiesArgsDict(TypedDict):
    aad_profile: NotRequired[pulumi.Input[AADProfileArgsDict]]
    addon_profiles: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[AddonProfilesArgsDict]]]
    ]
    agent_pool_profiles: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NamedAgentPoolProfileArgsDict]]]
    ]
    cloud_provider_profile: NotRequired[pulumi.Input[CloudProviderProfileArgsDict]]
    control_plane: NotRequired[pulumi.Input[ControlPlaneProfileArgsDict]]
    enable_rbac: NotRequired[pulumi.Input[_builtins.bool]]
    features: NotRequired[
        pulumi.Input[ProvisionedClustersCommonPropertiesFeaturesArgsDict]
    ]
    http_proxy_config: NotRequired[pulumi.Input[HttpProxyConfigArgsDict]]
    kubernetes_version: NotRequired[pulumi.Input[_builtins.str]]
    linux_profile: NotRequired[pulumi.Input[LinuxProfilePropertiesArgsDict]]
    network_profile: NotRequired[pulumi.Input[NetworkProfileArgsDict]]
    node_resource_group: NotRequired[pulumi.Input[_builtins.str]]
    windows_profile: NotRequired[pulumi.Input[WindowsProfileArgsDict]]

@pulumi.input_type
class ProvisionedClustersAllPropertiesArgs:
    def __init__(
        __self__,
        *,
        aad_profile: Optional[pulumi.Input[AADProfileArgs]] = ...,
        addon_profiles: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[AddonProfilesArgs]]]
        ] = ...,
        agent_pool_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[NamedAgentPoolProfileArgs]]]
        ] = ...,
        cloud_provider_profile: Optional[pulumi.Input[CloudProviderProfileArgs]] = ...,
        control_plane: Optional[pulumi.Input[ControlPlaneProfileArgs]] = ...,
        enable_rbac: Optional[pulumi.Input[_builtins.bool]] = ...,
        features: Optional[
            pulumi.Input[ProvisionedClustersCommonPropertiesFeaturesArgs]
        ] = ...,
        http_proxy_config: Optional[pulumi.Input[HttpProxyConfigArgs]] = ...,
        kubernetes_version: Optional[pulumi.Input[_builtins.str]] = ...,
        linux_profile: Optional[pulumi.Input[LinuxProfilePropertiesArgs]] = ...,
        network_profile: Optional[pulumi.Input[NetworkProfileArgs]] = ...,
        node_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        windows_profile: Optional[pulumi.Input[WindowsProfileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadProfile")
    def aad_profile(self) -> Optional[pulumi.Input[AADProfileArgs]]: ...
    @aad_profile.setter
    def aad_profile(self, value: Optional[pulumi.Input[AADProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="addonProfiles")
    def addon_profiles(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[AddonProfilesArgs]]]]: ...
    @addon_profiles.setter
    def addon_profiles(
        self,
        value: Optional[pulumi.Input[Mapping[str, pulumi.Input[AddonProfilesArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NamedAgentPoolProfileArgs]]]]: ...
    @agent_pool_profiles.setter
    def agent_pool_profiles(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NamedAgentPoolProfileArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudProviderProfile")
    def cloud_provider_profile(
        self,
    ) -> Optional[pulumi.Input[CloudProviderProfileArgs]]: ...
    @cloud_provider_profile.setter
    def cloud_provider_profile(
        self, value: Optional[pulumi.Input[CloudProviderProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[pulumi.Input[ControlPlaneProfileArgs]]: ...
    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input[ControlPlaneProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="enableRbac")
    def enable_rbac(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_rbac.setter
    def enable_rbac(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> Optional[pulumi.Input[ProvisionedClustersCommonPropertiesFeaturesArgs]]: ...
    @features.setter
    def features(
        self,
        value: Optional[pulumi.Input[ProvisionedClustersCommonPropertiesFeaturesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(self) -> Optional[pulumi.Input[HttpProxyConfigArgs]]: ...
    @http_proxy_config.setter
    def http_proxy_config(self, value: Optional[pulumi.Input[HttpProxyConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kubernetes_version.setter
    def kubernetes_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> Optional[pulumi.Input[LinuxProfilePropertiesArgs]]: ...
    @linux_profile.setter
    def linux_profile(
        self, value: Optional[pulumi.Input[LinuxProfilePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[NetworkProfileArgs]]: ...
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[NetworkProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeResourceGroup")
    def node_resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_resource_group.setter
    def node_resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="windowsProfile")
    def windows_profile(self) -> Optional[pulumi.Input[WindowsProfileArgs]]: ...
    @windows_profile.setter
    def windows_profile(self, value: Optional[pulumi.Input[WindowsProfileArgs]]): ...

class ProvisionedClustersCommonPropertiesFeaturesArgsDict(TypedDict):
    arc_agent_profile: NotRequired[pulumi.Input[ArcAgentProfileArgsDict]]

@pulumi.input_type
class ProvisionedClustersCommonPropertiesFeaturesArgs:
    def __init__(
        __self__,
        *,
        arc_agent_profile: Optional[pulumi.Input[ArcAgentProfileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="arcAgentProfile")
    def arc_agent_profile(self) -> Optional[pulumi.Input[ArcAgentProfileArgs]]: ...
    @arc_agent_profile.setter
    def arc_agent_profile(self, value: Optional[pulumi.Input[ArcAgentProfileArgs]]): ...

class ProvisionedClustersExtendedLocationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProvisionedClustersExtendedLocationArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageSpacesExtendedLocationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageSpacesExtendedLocationArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageSpacesPropertiesErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageSpacesPropertiesErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageSpacesPropertiesHciStorageProfileArgsDict(TypedDict):
    moc_group: NotRequired[pulumi.Input[_builtins.str]]
    moc_location: NotRequired[pulumi.Input[_builtins.str]]
    moc_storage_container: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageSpacesPropertiesHciStorageProfileArgs:
    def __init__(
        __self__,
        *,
        moc_group: Optional[pulumi.Input[_builtins.str]] = ...,
        moc_location: Optional[pulumi.Input[_builtins.str]] = ...,
        moc_storage_container: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mocGroup")
    def moc_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @moc_group.setter
    def moc_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mocLocation")
    def moc_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @moc_location.setter
    def moc_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mocStorageContainer")
    def moc_storage_container(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @moc_storage_container.setter
    def moc_storage_container(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageSpacesPropertiesProvisioningStatusArgsDict(TypedDict):
    error: NotRequired[pulumi.Input[StorageSpacesPropertiesErrorArgsDict]]
    operation_id: NotRequired[pulumi.Input[_builtins.str]]
    phase: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageSpacesPropertiesProvisioningStatusArgs:
    def __init__(
        __self__,
        *,
        error: Optional[pulumi.Input[StorageSpacesPropertiesErrorArgs]] = ...,
        operation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        phase: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[StorageSpacesPropertiesErrorArgs]]: ...
    @error.setter
    def error(
        self, value: Optional[pulumi.Input[StorageSpacesPropertiesErrorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operation_id.setter
    def operation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def phase(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phase.setter
    def phase(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageSpacesPropertiesStatusArgsDict(TypedDict):
    provisioning_status: NotRequired[
        pulumi.Input[StorageSpacesPropertiesProvisioningStatusArgsDict]
    ]

@pulumi.input_type
class StorageSpacesPropertiesStatusArgs:
    def __init__(
        __self__,
        *,
        provisioning_status: Optional[
            pulumi.Input[StorageSpacesPropertiesProvisioningStatusArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatus")
    def provisioning_status(
        self,
    ) -> Optional[pulumi.Input[StorageSpacesPropertiesProvisioningStatusArgs]]: ...
    @provisioning_status.setter
    def provisioning_status(
        self,
        value: Optional[pulumi.Input[StorageSpacesPropertiesProvisioningStatusArgs]],
    ): ...

class StorageSpacesPropertiesVmwareStorageProfileArgsDict(TypedDict):
    datacenter: NotRequired[pulumi.Input[_builtins.str]]
    datastore: NotRequired[pulumi.Input[_builtins.str]]
    folder: NotRequired[pulumi.Input[_builtins.str]]
    resource_pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageSpacesPropertiesVmwareStorageProfileArgs:
    def __init__(
        __self__,
        *,
        datacenter: Optional[pulumi.Input[_builtins.str]] = ...,
        datastore: Optional[pulumi.Input[_builtins.str]] = ...,
        folder: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datastore.setter
    def datastore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourcePool")
    def resource_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_pool.setter
    def resource_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageSpacesPropertiesArgsDict(TypedDict):
    hci_storage_profile: NotRequired[
        pulumi.Input[StorageSpacesPropertiesHciStorageProfileArgsDict]
    ]
    status: NotRequired[pulumi.Input[StorageSpacesPropertiesStatusArgsDict]]
    vmware_storage_profile: NotRequired[
        pulumi.Input[StorageSpacesPropertiesVmwareStorageProfileArgsDict]
    ]

@pulumi.input_type
class StorageSpacesPropertiesArgs:
    def __init__(
        __self__,
        *,
        hci_storage_profile: Optional[
            pulumi.Input[StorageSpacesPropertiesHciStorageProfileArgs]
        ] = ...,
        status: Optional[pulumi.Input[StorageSpacesPropertiesStatusArgs]] = ...,
        vmware_storage_profile: Optional[
            pulumi.Input[StorageSpacesPropertiesVmwareStorageProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hciStorageProfile")
    def hci_storage_profile(
        self,
    ) -> Optional[pulumi.Input[StorageSpacesPropertiesHciStorageProfileArgs]]: ...
    @hci_storage_profile.setter
    def hci_storage_profile(
        self,
        value: Optional[pulumi.Input[StorageSpacesPropertiesHciStorageProfileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[StorageSpacesPropertiesStatusArgs]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[StorageSpacesPropertiesStatusArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmwareStorageProfile")
    def vmware_storage_profile(
        self,
    ) -> Optional[pulumi.Input[StorageSpacesPropertiesVmwareStorageProfileArgs]]: ...
    @vmware_storage_profile.setter
    def vmware_storage_profile(
        self,
        value: Optional[pulumi.Input[StorageSpacesPropertiesVmwareStorageProfileArgs]],
    ): ...

class VirtualNetworksExtendedLocationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNetworksExtendedLocationArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworksPropertiesHciArgsDict(TypedDict):
    moc_group: NotRequired[pulumi.Input[_builtins.str]]
    moc_location: NotRequired[pulumi.Input[_builtins.str]]
    moc_vnet_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNetworksPropertiesHciArgs:
    def __init__(
        __self__,
        *,
        moc_group: Optional[pulumi.Input[_builtins.str]] = ...,
        moc_location: Optional[pulumi.Input[_builtins.str]] = ...,
        moc_vnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mocGroup")
    def moc_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @moc_group.setter
    def moc_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mocLocation")
    def moc_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @moc_location.setter
    def moc_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mocVnetName")
    def moc_vnet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @moc_vnet_name.setter
    def moc_vnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworksPropertiesInfraVnetProfileArgsDict(TypedDict):
    hci: NotRequired[pulumi.Input[VirtualNetworksPropertiesHciArgsDict]]
    network_cloud: NotRequired[
        pulumi.Input[VirtualNetworksPropertiesNetworkCloudArgsDict]
    ]
    vmware: NotRequired[pulumi.Input[VirtualNetworksPropertiesVmwareArgsDict]]

@pulumi.input_type
class VirtualNetworksPropertiesInfraVnetProfileArgs:
    def __init__(
        __self__,
        *,
        hci: Optional[pulumi.Input[VirtualNetworksPropertiesHciArgs]] = ...,
        network_cloud: Optional[
            pulumi.Input[VirtualNetworksPropertiesNetworkCloudArgs]
        ] = ...,
        vmware: Optional[pulumi.Input[VirtualNetworksPropertiesVmwareArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hci(self) -> Optional[pulumi.Input[VirtualNetworksPropertiesHciArgs]]: ...
    @hci.setter
    def hci(self, value: Optional[pulumi.Input[VirtualNetworksPropertiesHciArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="networkCloud")
    def network_cloud(
        self,
    ) -> Optional[pulumi.Input[VirtualNetworksPropertiesNetworkCloudArgs]]: ...
    @network_cloud.setter
    def network_cloud(
        self, value: Optional[pulumi.Input[VirtualNetworksPropertiesNetworkCloudArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def vmware(self) -> Optional[pulumi.Input[VirtualNetworksPropertiesVmwareArgs]]: ...
    @vmware.setter
    def vmware(
        self, value: Optional[pulumi.Input[VirtualNetworksPropertiesVmwareArgs]]
    ): ...

class VirtualNetworksPropertiesNetworkCloudArgsDict(TypedDict):
    network_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNetworksPropertiesNetworkCloudArgs:
    def __init__(
        __self__, *, network_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworksPropertiesVipPoolArgsDict(TypedDict):
    end_ip: NotRequired[pulumi.Input[_builtins.str]]
    start_ip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNetworksPropertiesVipPoolArgs:
    def __init__(
        __self__,
        *,
        end_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        start_ip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endIP")
    def end_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_ip.setter
    def end_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startIP")
    def start_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_ip.setter
    def start_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworksPropertiesVmipPoolArgsDict(TypedDict):
    end_ip: NotRequired[pulumi.Input[_builtins.str]]
    start_ip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNetworksPropertiesVmipPoolArgs:
    def __init__(
        __self__,
        *,
        end_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        start_ip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endIP")
    def end_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_ip.setter
    def end_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startIP")
    def start_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_ip.setter
    def start_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworksPropertiesVmwareArgsDict(TypedDict):
    segment_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNetworksPropertiesVmwareArgs:
    def __init__(
        __self__, *, segment_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @segment_name.setter
    def segment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworksPropertiesArgsDict(TypedDict):
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    gateway: NotRequired[pulumi.Input[_builtins.str]]
    infra_vnet_profile: NotRequired[
        pulumi.Input[VirtualNetworksPropertiesInfraVnetProfileArgsDict]
    ]
    ip_address_prefix: NotRequired[pulumi.Input[_builtins.str]]
    vip_pool: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualNetworksPropertiesVipPoolArgsDict]]]
    ]
    vmip_pool: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualNetworksPropertiesVmipPoolArgsDict]]]
    ]

@pulumi.input_type
class VirtualNetworksPropertiesArgs:
    def __init__(
        __self__,
        *,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        infra_vnet_profile: Optional[
            pulumi.Input[VirtualNetworksPropertiesInfraVnetProfileArgs]
        ] = ...,
        ip_address_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        vip_pool: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNetworksPropertiesVipPoolArgs]]]
        ] = ...,
        vmip_pool: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNetworksPropertiesVmipPoolArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="infraVnetProfile")
    def infra_vnet_profile(
        self,
    ) -> Optional[pulumi.Input[VirtualNetworksPropertiesInfraVnetProfileArgs]]: ...
    @infra_vnet_profile.setter
    def infra_vnet_profile(
        self,
        value: Optional[pulumi.Input[VirtualNetworksPropertiesInfraVnetProfileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressPrefix")
    def ip_address_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_prefix.setter
    def ip_address_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vipPool")
    def vip_pool(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VirtualNetworksPropertiesVipPoolArgs]]]
    ]: ...
    @vip_pool.setter
    def vip_pool(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNetworksPropertiesVipPoolArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmipPool")
    def vmip_pool(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VirtualNetworksPropertiesVmipPoolArgs]]]
    ]: ...
    @vmip_pool.setter
    def vmip_pool(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNetworksPropertiesVmipPoolArgs]]]
        ],
    ): ...

class WindowsProfileArgsDict(TypedDict):
    admin_password: NotRequired[pulumi.Input[_builtins.str]]
    admin_username: NotRequired[pulumi.Input[_builtins.str]]
    enable_csi_proxy: NotRequired[pulumi.Input[_builtins.bool]]
    license_type: NotRequired[pulumi.Input[Union[_builtins.str, LicenseType]]]

@pulumi.input_type
class WindowsProfileArgs:
    def __init__(
        __self__,
        *,
        admin_password: Optional[pulumi.Input[_builtins.str]] = ...,
        admin_username: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_csi_proxy: Optional[pulumi.Input[_builtins.bool]] = ...,
        license_type: Optional[pulumi.Input[Union[_builtins.str, LicenseType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_password.setter
    def admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableCsiProxy")
    def enable_csi_proxy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_csi_proxy.setter
    def enable_csi_proxy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LicenseType]]]: ...
    @license_type.setter
    def license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LicenseType]]]
    ): ...
