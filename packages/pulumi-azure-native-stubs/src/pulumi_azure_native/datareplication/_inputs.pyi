import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AzStackHCIClusterPropertiesArgs",
    "AzStackHCIClusterPropertiesArgsDict",
    "AzStackHCIFabricModelCustomPropertiesArgs",
    "AzStackHCIFabricModelCustomPropertiesArgsDict",
    "ConnectionDetailsArgs",
    "ConnectionDetailsArgsDict",
    "DraModelPropertiesArgs",
    "DraModelPropertiesArgsDict",
    "FabricAgentModelPropertiesArgs",
    "FabricAgentModelPropertiesArgsDict",
    "FabricModelPropertiesArgs",
    "FabricModelPropertiesArgsDict",
    "GroupConnectivityInformationArgs",
    "GroupConnectivityInformationArgsDict",
    "HyperVMigrateFabricModelCustomPropertiesArgs",
    "HyperVMigrateFabricModelCustomPropertiesArgsDict",
    "HyperVToAzStackHCIDiskInputArgs",
    "HyperVToAzStackHCIDiskInputArgsDict",
    "HyperVToAzStackHCINicInputArgs",
    "HyperVToAzStackHCINicInputArgsDict",
    "HyperVToAzStackHCIPolicyModelCustomPropertiesArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "IdentityModelArgs",
    "IdentityModelArgsDict",
    "PolicyModelPropertiesArgs",
    "PolicyModelPropertiesArgsDict",
    "PrivateEndpointConnectionProxyPropertiesArgs",
    "PrivateEndpointConnectionProxyPropertiesArgsDict",
    "PrivateEndpointConnectionResponsePropertiesArgs",
    ...,
    "PrivateEndpointArgs",
    "PrivateEndpointArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "PrivateLinkServiceConnectionArgs",
    "PrivateLinkServiceConnectionArgsDict",
    "PrivateLinkServiceProxyArgs",
    "PrivateLinkServiceProxyArgsDict",
    "ProtectedItemDynamicMemoryConfigArgs",
    "ProtectedItemDynamicMemoryConfigArgsDict",
    "ProtectedItemModelPropertiesArgs",
    "ProtectedItemModelPropertiesArgsDict",
    "RemotePrivateEndpointConnectionArgs",
    "RemotePrivateEndpointConnectionArgsDict",
    "RemotePrivateEndpointArgs",
    "RemotePrivateEndpointArgsDict",
    "ReplicationExtensionModelPropertiesArgs",
    "ReplicationExtensionModelPropertiesArgsDict",
    "StorageContainerPropertiesArgs",
    "StorageContainerPropertiesArgsDict",
    "VMwareDraModelCustomPropertiesArgs",
    "VMwareDraModelCustomPropertiesArgsDict",
    "VMwareFabricAgentModelCustomPropertiesArgs",
    "VMwareFabricAgentModelCustomPropertiesArgsDict",
    "VMwareMigrateFabricModelCustomPropertiesArgs",
    "VMwareMigrateFabricModelCustomPropertiesArgsDict",
    "VMwareToAzStackHCIDiskInputArgs",
    "VMwareToAzStackHCIDiskInputArgsDict",
    "VMwareToAzStackHCINicInputArgs",
    "VMwareToAzStackHCINicInputArgsDict",
    "VMwareToAzStackHCIPolicyModelCustomPropertiesArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "VaultModelPropertiesArgs",
    "VaultModelPropertiesArgsDict",
]

class AzStackHCIClusterPropertiesArgsDict(TypedDict):
    cluster_name: pulumi.Input[_builtins.str]
    resource_name: pulumi.Input[_builtins.str]
    storage_account_name: pulumi.Input[_builtins.str]
    storage_containers: pulumi.Input[
        Sequence[pulumi.Input[StorageContainerPropertiesArgsDict]]
    ]

@pulumi.input_type
class AzStackHCIClusterPropertiesArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        resource_name: pulumi.Input[_builtins.str],
        storage_account_name: pulumi.Input[_builtins.str],
        storage_containers: pulumi.Input[
            Sequence[pulumi.Input[StorageContainerPropertiesArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @storage_account_name.setter
    def storage_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageContainers")
    def storage_containers(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[StorageContainerPropertiesArgs]]]: ...
    @storage_containers.setter
    def storage_containers(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[StorageContainerPropertiesArgs]]],
    ): ...

class AzStackHCIFabricModelCustomPropertiesArgsDict(TypedDict):
    az_stack_hci_site_id: pulumi.Input[_builtins.str]
    cluster: pulumi.Input[AzStackHCIClusterPropertiesArgsDict]
    instance_type: pulumi.Input[_builtins.str]
    migration_solution_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzStackHCIFabricModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        az_stack_hci_site_id: pulumi.Input[_builtins.str],
        cluster: pulumi.Input[AzStackHCIClusterPropertiesArgs],
        instance_type: pulumi.Input[_builtins.str],
        migration_solution_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azStackHciSiteId")
    def az_stack_hci_site_id(self) -> pulumi.Input[_builtins.str]: ...
    @az_stack_hci_site_id.setter
    def az_stack_hci_site_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[AzStackHCIClusterPropertiesArgs]: ...
    @cluster.setter
    def cluster(self, value: pulumi.Input[AzStackHCIClusterPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="migrationSolutionId")
    def migration_solution_id(self) -> pulumi.Input[_builtins.str]: ...
    @migration_solution_id.setter
    def migration_solution_id(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionDetailsArgsDict(TypedDict):
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    link_identifier: NotRequired[pulumi.Input[_builtins.str]]
    member_name: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionDetailsArgs:
    def __init__(
        __self__,
        *,
        group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        link_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        member_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkIdentifier")
    def link_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @link_identifier.setter
    def link_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memberName")
    def member_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @member_name.setter
    def member_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DraModelPropertiesArgsDict(TypedDict):
    authentication_identity: pulumi.Input[IdentityModelArgsDict]
    custom_properties: pulumi.Input[VMwareDraModelCustomPropertiesArgsDict]
    machine_id: pulumi.Input[_builtins.str]
    machine_name: pulumi.Input[_builtins.str]
    resource_access_identity: pulumi.Input[IdentityModelArgsDict]

@pulumi.input_type
class DraModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        authentication_identity: pulumi.Input[IdentityModelArgs],
        custom_properties: pulumi.Input[VMwareDraModelCustomPropertiesArgs],
        machine_id: pulumi.Input[_builtins.str],
        machine_name: pulumi.Input[_builtins.str],
        resource_access_identity: pulumi.Input[IdentityModelArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationIdentity")
    def authentication_identity(self) -> pulumi.Input[IdentityModelArgs]: ...
    @authentication_identity.setter
    def authentication_identity(self, value: pulumi.Input[IdentityModelArgs]): ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> pulumi.Input[VMwareDraModelCustomPropertiesArgs]: ...
    @custom_properties.setter
    def custom_properties(
        self, value: pulumi.Input[VMwareDraModelCustomPropertiesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> pulumi.Input[_builtins.str]: ...
    @machine_id.setter
    def machine_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> pulumi.Input[_builtins.str]: ...
    @machine_name.setter
    def machine_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessIdentity")
    def resource_access_identity(self) -> pulumi.Input[IdentityModelArgs]: ...
    @resource_access_identity.setter
    def resource_access_identity(self, value: pulumi.Input[IdentityModelArgs]): ...

class FabricAgentModelPropertiesArgsDict(TypedDict):
    authentication_identity: pulumi.Input[IdentityModelArgsDict]
    custom_properties: pulumi.Input[VMwareFabricAgentModelCustomPropertiesArgsDict]
    machine_id: pulumi.Input[_builtins.str]
    machine_name: pulumi.Input[_builtins.str]
    resource_access_identity: pulumi.Input[IdentityModelArgsDict]

@pulumi.input_type
class FabricAgentModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        authentication_identity: pulumi.Input[IdentityModelArgs],
        custom_properties: pulumi.Input[VMwareFabricAgentModelCustomPropertiesArgs],
        machine_id: pulumi.Input[_builtins.str],
        machine_name: pulumi.Input[_builtins.str],
        resource_access_identity: pulumi.Input[IdentityModelArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationIdentity")
    def authentication_identity(self) -> pulumi.Input[IdentityModelArgs]: ...
    @authentication_identity.setter
    def authentication_identity(self, value: pulumi.Input[IdentityModelArgs]): ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(
        self,
    ) -> pulumi.Input[VMwareFabricAgentModelCustomPropertiesArgs]: ...
    @custom_properties.setter
    def custom_properties(
        self, value: pulumi.Input[VMwareFabricAgentModelCustomPropertiesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> pulumi.Input[_builtins.str]: ...
    @machine_id.setter
    def machine_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> pulumi.Input[_builtins.str]: ...
    @machine_name.setter
    def machine_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessIdentity")
    def resource_access_identity(self) -> pulumi.Input[IdentityModelArgs]: ...
    @resource_access_identity.setter
    def resource_access_identity(self, value: pulumi.Input[IdentityModelArgs]): ...

class FabricModelPropertiesArgsDict(TypedDict):
    custom_properties: pulumi.Input[
        Union[
            AzStackHCIFabricModelCustomPropertiesArgsDict,
            HyperVMigrateFabricModelCustomPropertiesArgsDict,
            VMwareMigrateFabricModelCustomPropertiesArgsDict,
        ]
    ]

@pulumi.input_type
class FabricModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        custom_properties: pulumi.Input[
            Union[
                AzStackHCIFabricModelCustomPropertiesArgs,
                HyperVMigrateFabricModelCustomPropertiesArgs,
                VMwareMigrateFabricModelCustomPropertiesArgs,
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(
        self,
    ) -> pulumi.Input[
        Union[
            AzStackHCIFabricModelCustomPropertiesArgs,
            HyperVMigrateFabricModelCustomPropertiesArgs,
            VMwareMigrateFabricModelCustomPropertiesArgs,
        ]
    ]: ...
    @custom_properties.setter
    def custom_properties(
        self,
        value: pulumi.Input[
            Union[
                AzStackHCIFabricModelCustomPropertiesArgs,
                HyperVMigrateFabricModelCustomPropertiesArgs,
                VMwareMigrateFabricModelCustomPropertiesArgs,
            ]
        ],
    ): ...

class GroupConnectivityInformationArgsDict(TypedDict):
    customer_visible_fqdns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    internal_fqdn: NotRequired[pulumi.Input[_builtins.str]]
    member_name: NotRequired[pulumi.Input[_builtins.str]]
    private_link_service_arm_region: NotRequired[pulumi.Input[_builtins.str]]
    redirect_map_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupConnectivityInformationArgs:
    def __init__(
        __self__,
        *,
        customer_visible_fqdns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        internal_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        member_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_service_arm_region: Optional[pulumi.Input[_builtins.str]] = ...,
        redirect_map_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerVisibleFqdns")
    def customer_visible_fqdns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @customer_visible_fqdns.setter
    def customer_visible_fqdns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="internalFqdn")
    def internal_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @internal_fqdn.setter
    def internal_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memberName")
    def member_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @member_name.setter
    def member_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceArmRegion")
    def private_link_service_arm_region(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_service_arm_region.setter
    def private_link_service_arm_region(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectMapId")
    def redirect_map_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redirect_map_id.setter
    def redirect_map_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HyperVMigrateFabricModelCustomPropertiesArgsDict(TypedDict):
    hyper_v_site_id: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    migration_solution_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class HyperVMigrateFabricModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        hyper_v_site_id: pulumi.Input[_builtins.str],
        instance_type: pulumi.Input[_builtins.str],
        migration_solution_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hyperVSiteId")
    def hyper_v_site_id(self) -> pulumi.Input[_builtins.str]: ...
    @hyper_v_site_id.setter
    def hyper_v_site_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="migrationSolutionId")
    def migration_solution_id(self) -> pulumi.Input[_builtins.str]: ...
    @migration_solution_id.setter
    def migration_solution_id(self, value: pulumi.Input[_builtins.str]): ...

class HyperVToAzStackHCIDiskInputArgsDict(TypedDict):
    disk_file_format: pulumi.Input[_builtins.str]
    disk_id: pulumi.Input[_builtins.str]
    disk_size_gb: pulumi.Input[_builtins.float]
    is_os_disk: pulumi.Input[_builtins.bool]
    is_dynamic: NotRequired[pulumi.Input[_builtins.bool]]
    storage_container_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HyperVToAzStackHCIDiskInputArgs:
    def __init__(
        __self__,
        *,
        disk_file_format: pulumi.Input[_builtins.str],
        disk_id: pulumi.Input[_builtins.str],
        disk_size_gb: pulumi.Input[_builtins.float],
        is_os_disk: pulumi.Input[_builtins.bool],
        is_dynamic: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_container_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskFileFormat")
    def disk_file_format(self) -> pulumi.Input[_builtins.str]: ...
    @disk_file_format.setter
    def disk_file_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Input[_builtins.str]: ...
    @disk_id.setter
    def disk_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> pulumi.Input[_builtins.float]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="isOsDisk")
    def is_os_disk(self) -> pulumi.Input[_builtins.bool]: ...
    @is_os_disk.setter
    def is_os_disk(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="isDynamic")
    def is_dynamic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_dynamic.setter
    def is_dynamic(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageContainerId")
    def storage_container_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_container_id.setter
    def storage_container_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HyperVToAzStackHCINicInputArgsDict(TypedDict):
    nic_id: pulumi.Input[_builtins.str]
    selection_type_for_failover: pulumi.Input[Union[_builtins.str, VMNicSelection]]
    target_network_id: pulumi.Input[_builtins.str]
    test_network_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class HyperVToAzStackHCINicInputArgs:
    def __init__(
        __self__,
        *,
        nic_id: pulumi.Input[_builtins.str],
        selection_type_for_failover: pulumi.Input[Union[_builtins.str, VMNicSelection]],
        target_network_id: pulumi.Input[_builtins.str],
        test_network_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> pulumi.Input[_builtins.str]: ...
    @nic_id.setter
    def nic_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="selectionTypeForFailover")
    def selection_type_for_failover(
        self,
    ) -> pulumi.Input[Union[_builtins.str, VMNicSelection]]: ...
    @selection_type_for_failover.setter
    def selection_type_for_failover(
        self, value: pulumi.Input[Union[_builtins.str, VMNicSelection]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_network_id.setter
    def target_network_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> pulumi.Input[_builtins.str]: ...
    @test_network_id.setter
    def test_network_id(self, value: pulumi.Input[_builtins.str]): ...

class HyperVToAzStackHCIPolicyModelCustomPropertiesArgsDict(TypedDict):
    app_consistent_frequency_in_minutes: pulumi.Input[_builtins.int]
    crash_consistent_frequency_in_minutes: pulumi.Input[_builtins.int]
    instance_type: pulumi.Input[_builtins.str]
    recovery_point_history_in_minutes: pulumi.Input[_builtins.int]

@pulumi.input_type
class HyperVToAzStackHCIPolicyModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        app_consistent_frequency_in_minutes: pulumi.Input[_builtins.int],
        crash_consistent_frequency_in_minutes: pulumi.Input[_builtins.int],
        instance_type: pulumi.Input[_builtins.str],
        recovery_point_history_in_minutes: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @app_consistent_frequency_in_minutes.setter
    def app_consistent_frequency_in_minutes(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @crash_consistent_frequency_in_minutes.setter
    def crash_consistent_frequency_in_minutes(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistoryInMinutes")
    def recovery_point_history_in_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @recovery_point_history_in_minutes.setter
    def recovery_point_history_in_minutes(self, value: pulumi.Input[_builtins.int]): ...

class HyperVToAzStackHCIProtectedItemModelCustomPropertiesArgsDict(TypedDict):
    custom_location_region: pulumi.Input[_builtins.str]
    disks_to_include: pulumi.Input[
        Sequence[pulumi.Input[HyperVToAzStackHCIDiskInputArgsDict]]
    ]
    fabric_discovery_machine_id: pulumi.Input[_builtins.str]
    hyper_v_generation: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    nics_to_include: pulumi.Input[
        Sequence[pulumi.Input[HyperVToAzStackHCINicInputArgsDict]]
    ]
    run_as_account_id: pulumi.Input[_builtins.str]
    source_dra_name: pulumi.Input[_builtins.str]
    storage_container_id: pulumi.Input[_builtins.str]
    target_arc_cluster_custom_location_id: pulumi.Input[_builtins.str]
    target_dra_name: pulumi.Input[_builtins.str]
    target_hci_cluster_id: pulumi.Input[_builtins.str]
    target_resource_group_id: pulumi.Input[_builtins.str]
    dynamic_memory_config: NotRequired[
        pulumi.Input[ProtectedItemDynamicMemoryConfigArgsDict]
    ]
    is_dynamic_ram: NotRequired[pulumi.Input[_builtins.bool]]
    target_cpu_cores: NotRequired[pulumi.Input[_builtins.int]]
    target_memory_in_mega_bytes: NotRequired[pulumi.Input[_builtins.int]]
    target_network_id: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_name: NotRequired[pulumi.Input[_builtins.str]]
    test_network_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HyperVToAzStackHCIProtectedItemModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        custom_location_region: pulumi.Input[_builtins.str],
        disks_to_include: pulumi.Input[
            Sequence[pulumi.Input[HyperVToAzStackHCIDiskInputArgs]]
        ],
        fabric_discovery_machine_id: pulumi.Input[_builtins.str],
        hyper_v_generation: pulumi.Input[_builtins.str],
        instance_type: pulumi.Input[_builtins.str],
        nics_to_include: pulumi.Input[
            Sequence[pulumi.Input[HyperVToAzStackHCINicInputArgs]]
        ],
        run_as_account_id: pulumi.Input[_builtins.str],
        source_dra_name: pulumi.Input[_builtins.str],
        storage_container_id: pulumi.Input[_builtins.str],
        target_arc_cluster_custom_location_id: pulumi.Input[_builtins.str],
        target_dra_name: pulumi.Input[_builtins.str],
        target_hci_cluster_id: pulumi.Input[_builtins.str],
        target_resource_group_id: pulumi.Input[_builtins.str],
        dynamic_memory_config: Optional[
            pulumi.Input[ProtectedItemDynamicMemoryConfigArgs]
        ] = ...,
        is_dynamic_ram: Optional[pulumi.Input[_builtins.bool]] = ...,
        target_cpu_cores: Optional[pulumi.Input[_builtins.int]] = ...,
        target_memory_in_mega_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        target_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        test_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customLocationRegion")
    def custom_location_region(self) -> pulumi.Input[_builtins.str]: ...
    @custom_location_region.setter
    def custom_location_region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="disksToInclude")
    def disks_to_include(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[HyperVToAzStackHCIDiskInputArgs]]]: ...
    @disks_to_include.setter
    def disks_to_include(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[HyperVToAzStackHCIDiskInputArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fabricDiscoveryMachineId")
    def fabric_discovery_machine_id(self) -> pulumi.Input[_builtins.str]: ...
    @fabric_discovery_machine_id.setter
    def fabric_discovery_machine_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> pulumi.Input[_builtins.str]: ...
    @hyper_v_generation.setter
    def hyper_v_generation(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nicsToInclude")
    def nics_to_include(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[HyperVToAzStackHCINicInputArgs]]]: ...
    @nics_to_include.setter
    def nics_to_include(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[HyperVToAzStackHCINicInputArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @run_as_account_id.setter
    def run_as_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceDraName")
    def source_dra_name(self) -> pulumi.Input[_builtins.str]: ...
    @source_dra_name.setter
    def source_dra_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageContainerId")
    def storage_container_id(self) -> pulumi.Input[_builtins.str]: ...
    @storage_container_id.setter
    def storage_container_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetArcClusterCustomLocationId")
    def target_arc_cluster_custom_location_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_arc_cluster_custom_location_id.setter
    def target_arc_cluster_custom_location_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDraName")
    def target_dra_name(self) -> pulumi.Input[_builtins.str]: ...
    @target_dra_name.setter
    def target_dra_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetHciClusterId")
    def target_hci_cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_hci_cluster_id.setter
    def target_hci_cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupId")
    def target_resource_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_resource_group_id.setter
    def target_resource_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryConfig")
    def dynamic_memory_config(
        self,
    ) -> Optional[pulumi.Input[ProtectedItemDynamicMemoryConfigArgs]]: ...
    @dynamic_memory_config.setter
    def dynamic_memory_config(
        self, value: Optional[pulumi.Input[ProtectedItemDynamicMemoryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isDynamicRam")
    def is_dynamic_ram(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_dynamic_ram.setter
    def is_dynamic_ram(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="targetCpuCores")
    def target_cpu_cores(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_cpu_cores.setter
    def target_cpu_cores(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetMemoryInMegaBytes")
    def target_memory_in_mega_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_memory_in_mega_bytes.setter
    def target_memory_in_mega_bytes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_network_id.setter
    def target_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmName")
    def target_vm_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vm_name.setter
    def target_vm_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_network_id.setter
    def test_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HyperVToAzStackHCIReplicationExtensionModelCustomPropertiesArgsDict(TypedDict):
    az_stack_hci_fabric_arm_id: pulumi.Input[_builtins.str]
    hyper_v_fabric_arm_id: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_sas_secret_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HyperVToAzStackHCIReplicationExtensionModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        az_stack_hci_fabric_arm_id: pulumi.Input[_builtins.str],
        hyper_v_fabric_arm_id: pulumi.Input[_builtins.str],
        instance_type: pulumi.Input[_builtins.str],
        storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_sas_secret_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azStackHciFabricArmId")
    def az_stack_hci_fabric_arm_id(self) -> pulumi.Input[_builtins.str]: ...
    @az_stack_hci_fabric_arm_id.setter
    def az_stack_hci_fabric_arm_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hyperVFabricArmId")
    def hyper_v_fabric_arm_id(self) -> pulumi.Input[_builtins.str]: ...
    @hyper_v_fabric_arm_id.setter
    def hyper_v_fabric_arm_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountSasSecretName")
    def storage_account_sas_secret_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_sas_secret_name.setter
    def storage_account_sas_secret_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class IdentityModelArgsDict(TypedDict):
    aad_authority: pulumi.Input[_builtins.str]
    application_id: pulumi.Input[_builtins.str]
    audience: pulumi.Input[_builtins.str]
    object_id: pulumi.Input[_builtins.str]
    tenant_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class IdentityModelArgs:
    def __init__(
        __self__,
        *,
        aad_authority: pulumi.Input[_builtins.str],
        application_id: pulumi.Input[_builtins.str],
        audience: pulumi.Input[_builtins.str],
        object_id: pulumi.Input[_builtins.str],
        tenant_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadAuthority")
    def aad_authority(self) -> pulumi.Input[_builtins.str]: ...
    @aad_authority.setter
    def aad_authority(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[_builtins.str]: ...
    @application_id.setter
    def application_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> pulumi.Input[_builtins.str]: ...
    @audience.setter
    def audience(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Input[_builtins.str]: ...
    @object_id.setter
    def object_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): ...

class PolicyModelPropertiesArgsDict(TypedDict):
    custom_properties: pulumi.Input[
        Union[
            HyperVToAzStackHCIPolicyModelCustomPropertiesArgsDict,
            VMwareToAzStackHCIPolicyModelCustomPropertiesArgsDict,
        ]
    ]

@pulumi.input_type
class PolicyModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        custom_properties: pulumi.Input[
            Union[
                HyperVToAzStackHCIPolicyModelCustomPropertiesArgs,
                VMwareToAzStackHCIPolicyModelCustomPropertiesArgs,
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(
        self,
    ) -> pulumi.Input[
        Union[
            HyperVToAzStackHCIPolicyModelCustomPropertiesArgs,
            VMwareToAzStackHCIPolicyModelCustomPropertiesArgs,
        ]
    ]: ...
    @custom_properties.setter
    def custom_properties(
        self,
        value: pulumi.Input[
            Union[
                HyperVToAzStackHCIPolicyModelCustomPropertiesArgs,
                VMwareToAzStackHCIPolicyModelCustomPropertiesArgs,
            ]
        ],
    ): ...

class PrivateEndpointConnectionProxyPropertiesArgsDict(TypedDict):
    remote_private_endpoint: NotRequired[pulumi.Input[RemotePrivateEndpointArgsDict]]

@pulumi.input_type
class PrivateEndpointConnectionProxyPropertiesArgs:
    def __init__(
        __self__,
        *,
        remote_private_endpoint: Optional[
            pulumi.Input[RemotePrivateEndpointArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="remotePrivateEndpoint")
    def remote_private_endpoint(
        self,
    ) -> Optional[pulumi.Input[RemotePrivateEndpointArgs]]: ...
    @remote_private_endpoint.setter
    def remote_private_endpoint(
        self, value: Optional[pulumi.Input[RemotePrivateEndpointArgs]]
    ): ...

class PrivateEndpointConnectionResponsePropertiesArgsDict(TypedDict):
    private_endpoint: NotRequired[pulumi.Input[PrivateEndpointArgsDict]]
    private_link_service_connection_state: NotRequired[
        pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]
    ]

@pulumi.input_type
class PrivateEndpointConnectionResponsePropertiesArgs:
    def __init__(
        __self__,
        *,
        private_endpoint: Optional[pulumi.Input[PrivateEndpointArgs]] = ...,
        private_link_service_connection_state: Optional[
            pulumi.Input[PrivateLinkServiceConnectionStateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input[PrivateEndpointArgs]]: ...
    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input[PrivateEndpointArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]
    ): ...

class PrivateEndpointArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointConnectionStatus]]
        ],
    ): ...

class PrivateLinkServiceConnectionArgsDict(TypedDict):
    group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    request_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateLinkServiceConnectionArgs:
    def __init__(
        __self__,
        *,
        group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        request_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @group_ids.setter
    def group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateLinkServiceProxyArgsDict(TypedDict):
    group_connectivity_information: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[GroupConnectivityInformationArgsDict]]]
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]
    remote_private_endpoint_connection: NotRequired[
        pulumi.Input[RemotePrivateEndpointConnectionArgsDict]
    ]
    remote_private_link_service_connection_state: NotRequired[
        pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]
    ]

@pulumi.input_type
class PrivateLinkServiceProxyArgs:
    def __init__(
        __self__,
        *,
        group_connectivity_information: Optional[
            pulumi.Input[Sequence[pulumi.Input[GroupConnectivityInformationArgs]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_private_endpoint_connection: Optional[
            pulumi.Input[RemotePrivateEndpointConnectionArgs]
        ] = ...,
        remote_private_link_service_connection_state: Optional[
            pulumi.Input[PrivateLinkServiceConnectionStateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupConnectivityInformation")
    def group_connectivity_information(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GroupConnectivityInformationArgs]]]
    ]: ...
    @group_connectivity_information.setter
    def group_connectivity_information(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GroupConnectivityInformationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remotePrivateEndpointConnection")
    def remote_private_endpoint_connection(
        self,
    ) -> Optional[pulumi.Input[RemotePrivateEndpointConnectionArgs]]: ...
    @remote_private_endpoint_connection.setter
    def remote_private_endpoint_connection(
        self, value: Optional[pulumi.Input[RemotePrivateEndpointConnectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="remotePrivateLinkServiceConnectionState")
    def remote_private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]: ...
    @remote_private_link_service_connection_state.setter
    def remote_private_link_service_connection_state(
        self, value: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]
    ): ...

class ProtectedItemDynamicMemoryConfigArgsDict(TypedDict):
    maximum_memory_in_mega_bytes: pulumi.Input[_builtins.float]
    minimum_memory_in_mega_bytes: pulumi.Input[_builtins.float]
    target_memory_buffer_percentage: pulumi.Input[_builtins.int]

@pulumi.input_type
class ProtectedItemDynamicMemoryConfigArgs:
    def __init__(
        __self__,
        *,
        maximum_memory_in_mega_bytes: pulumi.Input[_builtins.float],
        minimum_memory_in_mega_bytes: pulumi.Input[_builtins.float],
        target_memory_buffer_percentage: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumMemoryInMegaBytes")
    def maximum_memory_in_mega_bytes(self) -> pulumi.Input[_builtins.float]: ...
    @maximum_memory_in_mega_bytes.setter
    def maximum_memory_in_mega_bytes(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="minimumMemoryInMegaBytes")
    def minimum_memory_in_mega_bytes(self) -> pulumi.Input[_builtins.float]: ...
    @minimum_memory_in_mega_bytes.setter
    def minimum_memory_in_mega_bytes(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="targetMemoryBufferPercentage")
    def target_memory_buffer_percentage(self) -> pulumi.Input[_builtins.int]: ...
    @target_memory_buffer_percentage.setter
    def target_memory_buffer_percentage(self, value: pulumi.Input[_builtins.int]): ...

class ProtectedItemModelPropertiesArgsDict(TypedDict):
    custom_properties: pulumi.Input[
        Union[
            HyperVToAzStackHCIProtectedItemModelCustomPropertiesArgsDict,
            VMwareToAzStackHCIProtectedItemModelCustomPropertiesArgsDict,
        ]
    ]
    policy_name: pulumi.Input[_builtins.str]
    replication_extension_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ProtectedItemModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        custom_properties: pulumi.Input[
            Union[
                HyperVToAzStackHCIProtectedItemModelCustomPropertiesArgs,
                VMwareToAzStackHCIProtectedItemModelCustomPropertiesArgs,
            ]
        ],
        policy_name: pulumi.Input[_builtins.str],
        replication_extension_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(
        self,
    ) -> pulumi.Input[
        Union[
            HyperVToAzStackHCIProtectedItemModelCustomPropertiesArgs,
            VMwareToAzStackHCIProtectedItemModelCustomPropertiesArgs,
        ]
    ]: ...
    @custom_properties.setter
    def custom_properties(
        self,
        value: pulumi.Input[
            Union[
                HyperVToAzStackHCIProtectedItemModelCustomPropertiesArgs,
                VMwareToAzStackHCIProtectedItemModelCustomPropertiesArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Input[_builtins.str]: ...
    @policy_name.setter
    def policy_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="replicationExtensionName")
    def replication_extension_name(self) -> pulumi.Input[_builtins.str]: ...
    @replication_extension_name.setter
    def replication_extension_name(self, value: pulumi.Input[_builtins.str]): ...

class RemotePrivateEndpointConnectionArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RemotePrivateEndpointConnectionArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RemotePrivateEndpointArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    connection_details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ConnectionDetailsArgsDict]]]
    ]
    manual_private_link_service_connections: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgsDict]]]
    ]
    private_link_service_connections: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgsDict]]]
    ]
    private_link_service_proxies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceProxyArgsDict]]]
    ]

@pulumi.input_type
class RemotePrivateEndpointArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        connection_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionDetailsArgs]]]
        ] = ...,
        manual_private_link_service_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
        ] = ...,
        private_link_service_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
        ] = ...,
        private_link_service_proxies: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceProxyArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectionDetails")
    def connection_details(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConnectionDetailsArgs]]]]: ...
    @connection_details.setter
    def connection_details(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectionDetailsArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
    ]: ...
    @manual_private_link_service_connections.setter
    def manual_private_link_service_connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnections")
    def private_link_service_connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
    ]: ...
    @private_link_service_connections.setter
    def private_link_service_connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceProxies")
    def private_link_service_proxies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceProxyArgs]]]
    ]: ...
    @private_link_service_proxies.setter
    def private_link_service_proxies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceProxyArgs]]]
        ],
    ): ...

class ReplicationExtensionModelPropertiesArgsDict(TypedDict):
    custom_properties: pulumi.Input[
        Union[
            HyperVToAzStackHCIReplicationExtensionModelCustomPropertiesArgsDict,
            VMwareToAzStackHCIReplicationExtensionModelCustomPropertiesArgsDict,
        ]
    ]

@pulumi.input_type
class ReplicationExtensionModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        custom_properties: pulumi.Input[
            Union[
                HyperVToAzStackHCIReplicationExtensionModelCustomPropertiesArgs,
                VMwareToAzStackHCIReplicationExtensionModelCustomPropertiesArgs,
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(
        self,
    ) -> pulumi.Input[
        Union[
            HyperVToAzStackHCIReplicationExtensionModelCustomPropertiesArgs,
            VMwareToAzStackHCIReplicationExtensionModelCustomPropertiesArgs,
        ]
    ]: ...
    @custom_properties.setter
    def custom_properties(
        self,
        value: pulumi.Input[
            Union[
                HyperVToAzStackHCIReplicationExtensionModelCustomPropertiesArgs,
                VMwareToAzStackHCIReplicationExtensionModelCustomPropertiesArgs,
            ]
        ],
    ): ...

class StorageContainerPropertiesArgsDict(TypedDict):
    cluster_shared_volume_path: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class StorageContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        cluster_shared_volume_path: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterSharedVolumePath")
    def cluster_shared_volume_path(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_shared_volume_path.setter
    def cluster_shared_volume_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class VMwareDraModelCustomPropertiesArgsDict(TypedDict):
    bios_id: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    mars_authentication_identity: pulumi.Input[IdentityModelArgsDict]

@pulumi.input_type
class VMwareDraModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        bios_id: pulumi.Input[_builtins.str],
        instance_type: pulumi.Input[_builtins.str],
        mars_authentication_identity: pulumi.Input[IdentityModelArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> pulumi.Input[_builtins.str]: ...
    @bios_id.setter
    def bios_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="marsAuthenticationIdentity")
    def mars_authentication_identity(self) -> pulumi.Input[IdentityModelArgs]: ...
    @mars_authentication_identity.setter
    def mars_authentication_identity(self, value: pulumi.Input[IdentityModelArgs]): ...

class VMwareFabricAgentModelCustomPropertiesArgsDict(TypedDict):
    bios_id: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    mars_authentication_identity: pulumi.Input[IdentityModelArgsDict]

@pulumi.input_type
class VMwareFabricAgentModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        bios_id: pulumi.Input[_builtins.str],
        instance_type: pulumi.Input[_builtins.str],
        mars_authentication_identity: pulumi.Input[IdentityModelArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> pulumi.Input[_builtins.str]: ...
    @bios_id.setter
    def bios_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="marsAuthenticationIdentity")
    def mars_authentication_identity(self) -> pulumi.Input[IdentityModelArgs]: ...
    @mars_authentication_identity.setter
    def mars_authentication_identity(self, value: pulumi.Input[IdentityModelArgs]): ...

class VMwareMigrateFabricModelCustomPropertiesArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    migration_solution_id: pulumi.Input[_builtins.str]
    vmware_site_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class VMwareMigrateFabricModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        migration_solution_id: pulumi.Input[_builtins.str],
        vmware_site_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="migrationSolutionId")
    def migration_solution_id(self) -> pulumi.Input[_builtins.str]: ...
    @migration_solution_id.setter
    def migration_solution_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareSiteId")
    def vmware_site_id(self) -> pulumi.Input[_builtins.str]: ...
    @vmware_site_id.setter
    def vmware_site_id(self, value: pulumi.Input[_builtins.str]): ...

class VMwareToAzStackHCIDiskInputArgsDict(TypedDict):
    disk_file_format: pulumi.Input[_builtins.str]
    disk_id: pulumi.Input[_builtins.str]
    disk_size_gb: pulumi.Input[_builtins.float]
    is_os_disk: pulumi.Input[_builtins.bool]
    is_dynamic: NotRequired[pulumi.Input[_builtins.bool]]
    storage_container_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareToAzStackHCIDiskInputArgs:
    def __init__(
        __self__,
        *,
        disk_file_format: pulumi.Input[_builtins.str],
        disk_id: pulumi.Input[_builtins.str],
        disk_size_gb: pulumi.Input[_builtins.float],
        is_os_disk: pulumi.Input[_builtins.bool],
        is_dynamic: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_container_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskFileFormat")
    def disk_file_format(self) -> pulumi.Input[_builtins.str]: ...
    @disk_file_format.setter
    def disk_file_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Input[_builtins.str]: ...
    @disk_id.setter
    def disk_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> pulumi.Input[_builtins.float]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="isOsDisk")
    def is_os_disk(self) -> pulumi.Input[_builtins.bool]: ...
    @is_os_disk.setter
    def is_os_disk(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="isDynamic")
    def is_dynamic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_dynamic.setter
    def is_dynamic(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageContainerId")
    def storage_container_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_container_id.setter
    def storage_container_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareToAzStackHCINicInputArgsDict(TypedDict):
    label: pulumi.Input[_builtins.str]
    nic_id: pulumi.Input[_builtins.str]
    selection_type_for_failover: pulumi.Input[Union[_builtins.str, VMNicSelection]]
    target_network_id: pulumi.Input[_builtins.str]
    test_network_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class VMwareToAzStackHCINicInputArgs:
    def __init__(
        __self__,
        *,
        label: pulumi.Input[_builtins.str],
        nic_id: pulumi.Input[_builtins.str],
        selection_type_for_failover: pulumi.Input[Union[_builtins.str, VMNicSelection]],
        target_network_id: pulumi.Input[_builtins.str],
        test_network_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> pulumi.Input[_builtins.str]: ...
    @label.setter
    def label(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> pulumi.Input[_builtins.str]: ...
    @nic_id.setter
    def nic_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="selectionTypeForFailover")
    def selection_type_for_failover(
        self,
    ) -> pulumi.Input[Union[_builtins.str, VMNicSelection]]: ...
    @selection_type_for_failover.setter
    def selection_type_for_failover(
        self, value: pulumi.Input[Union[_builtins.str, VMNicSelection]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_network_id.setter
    def target_network_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> pulumi.Input[_builtins.str]: ...
    @test_network_id.setter
    def test_network_id(self, value: pulumi.Input[_builtins.str]): ...

class VMwareToAzStackHCIPolicyModelCustomPropertiesArgsDict(TypedDict):
    app_consistent_frequency_in_minutes: pulumi.Input[_builtins.int]
    crash_consistent_frequency_in_minutes: pulumi.Input[_builtins.int]
    instance_type: pulumi.Input[_builtins.str]
    recovery_point_history_in_minutes: pulumi.Input[_builtins.int]

@pulumi.input_type
class VMwareToAzStackHCIPolicyModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        app_consistent_frequency_in_minutes: pulumi.Input[_builtins.int],
        crash_consistent_frequency_in_minutes: pulumi.Input[_builtins.int],
        instance_type: pulumi.Input[_builtins.str],
        recovery_point_history_in_minutes: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @app_consistent_frequency_in_minutes.setter
    def app_consistent_frequency_in_minutes(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @crash_consistent_frequency_in_minutes.setter
    def crash_consistent_frequency_in_minutes(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistoryInMinutes")
    def recovery_point_history_in_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @recovery_point_history_in_minutes.setter
    def recovery_point_history_in_minutes(self, value: pulumi.Input[_builtins.int]): ...

class VMwareToAzStackHCIProtectedItemModelCustomPropertiesArgsDict(TypedDict):
    custom_location_region: pulumi.Input[_builtins.str]
    disks_to_include: pulumi.Input[
        Sequence[pulumi.Input[VMwareToAzStackHCIDiskInputArgsDict]]
    ]
    fabric_discovery_machine_id: pulumi.Input[_builtins.str]
    hyper_v_generation: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    nics_to_include: pulumi.Input[
        Sequence[pulumi.Input[VMwareToAzStackHCINicInputArgsDict]]
    ]
    run_as_account_id: pulumi.Input[_builtins.str]
    source_dra_name: pulumi.Input[_builtins.str]
    storage_container_id: pulumi.Input[_builtins.str]
    target_arc_cluster_custom_location_id: pulumi.Input[_builtins.str]
    target_dra_name: pulumi.Input[_builtins.str]
    target_hci_cluster_id: pulumi.Input[_builtins.str]
    target_resource_group_id: pulumi.Input[_builtins.str]
    dynamic_memory_config: NotRequired[
        pulumi.Input[ProtectedItemDynamicMemoryConfigArgsDict]
    ]
    is_dynamic_ram: NotRequired[pulumi.Input[_builtins.bool]]
    perform_auto_resync: NotRequired[pulumi.Input[_builtins.bool]]
    target_cpu_cores: NotRequired[pulumi.Input[_builtins.int]]
    target_memory_in_mega_bytes: NotRequired[pulumi.Input[_builtins.int]]
    target_network_id: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_name: NotRequired[pulumi.Input[_builtins.str]]
    test_network_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareToAzStackHCIProtectedItemModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        custom_location_region: pulumi.Input[_builtins.str],
        disks_to_include: pulumi.Input[
            Sequence[pulumi.Input[VMwareToAzStackHCIDiskInputArgs]]
        ],
        fabric_discovery_machine_id: pulumi.Input[_builtins.str],
        hyper_v_generation: pulumi.Input[_builtins.str],
        instance_type: pulumi.Input[_builtins.str],
        nics_to_include: pulumi.Input[
            Sequence[pulumi.Input[VMwareToAzStackHCINicInputArgs]]
        ],
        run_as_account_id: pulumi.Input[_builtins.str],
        source_dra_name: pulumi.Input[_builtins.str],
        storage_container_id: pulumi.Input[_builtins.str],
        target_arc_cluster_custom_location_id: pulumi.Input[_builtins.str],
        target_dra_name: pulumi.Input[_builtins.str],
        target_hci_cluster_id: pulumi.Input[_builtins.str],
        target_resource_group_id: pulumi.Input[_builtins.str],
        dynamic_memory_config: Optional[
            pulumi.Input[ProtectedItemDynamicMemoryConfigArgs]
        ] = ...,
        is_dynamic_ram: Optional[pulumi.Input[_builtins.bool]] = ...,
        perform_auto_resync: Optional[pulumi.Input[_builtins.bool]] = ...,
        target_cpu_cores: Optional[pulumi.Input[_builtins.int]] = ...,
        target_memory_in_mega_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        target_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        test_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customLocationRegion")
    def custom_location_region(self) -> pulumi.Input[_builtins.str]: ...
    @custom_location_region.setter
    def custom_location_region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="disksToInclude")
    def disks_to_include(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[VMwareToAzStackHCIDiskInputArgs]]]: ...
    @disks_to_include.setter
    def disks_to_include(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[VMwareToAzStackHCIDiskInputArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fabricDiscoveryMachineId")
    def fabric_discovery_machine_id(self) -> pulumi.Input[_builtins.str]: ...
    @fabric_discovery_machine_id.setter
    def fabric_discovery_machine_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> pulumi.Input[_builtins.str]: ...
    @hyper_v_generation.setter
    def hyper_v_generation(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nicsToInclude")
    def nics_to_include(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[VMwareToAzStackHCINicInputArgs]]]: ...
    @nics_to_include.setter
    def nics_to_include(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[VMwareToAzStackHCINicInputArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @run_as_account_id.setter
    def run_as_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceDraName")
    def source_dra_name(self) -> pulumi.Input[_builtins.str]: ...
    @source_dra_name.setter
    def source_dra_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageContainerId")
    def storage_container_id(self) -> pulumi.Input[_builtins.str]: ...
    @storage_container_id.setter
    def storage_container_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetArcClusterCustomLocationId")
    def target_arc_cluster_custom_location_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_arc_cluster_custom_location_id.setter
    def target_arc_cluster_custom_location_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDraName")
    def target_dra_name(self) -> pulumi.Input[_builtins.str]: ...
    @target_dra_name.setter
    def target_dra_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetHciClusterId")
    def target_hci_cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_hci_cluster_id.setter
    def target_hci_cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupId")
    def target_resource_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_resource_group_id.setter
    def target_resource_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryConfig")
    def dynamic_memory_config(
        self,
    ) -> Optional[pulumi.Input[ProtectedItemDynamicMemoryConfigArgs]]: ...
    @dynamic_memory_config.setter
    def dynamic_memory_config(
        self, value: Optional[pulumi.Input[ProtectedItemDynamicMemoryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isDynamicRam")
    def is_dynamic_ram(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_dynamic_ram.setter
    def is_dynamic_ram(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="performAutoResync")
    def perform_auto_resync(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @perform_auto_resync.setter
    def perform_auto_resync(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="targetCpuCores")
    def target_cpu_cores(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_cpu_cores.setter
    def target_cpu_cores(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetMemoryInMegaBytes")
    def target_memory_in_mega_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_memory_in_mega_bytes.setter
    def target_memory_in_mega_bytes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_network_id.setter
    def target_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmName")
    def target_vm_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vm_name.setter
    def target_vm_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_network_id.setter
    def test_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareToAzStackHCIReplicationExtensionModelCustomPropertiesArgsDict(TypedDict):
    az_stack_hci_fabric_arm_id: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    vmware_fabric_arm_id: pulumi.Input[_builtins.str]
    storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_sas_secret_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareToAzStackHCIReplicationExtensionModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        az_stack_hci_fabric_arm_id: pulumi.Input[_builtins.str],
        instance_type: pulumi.Input[_builtins.str],
        vmware_fabric_arm_id: pulumi.Input[_builtins.str],
        storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_sas_secret_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azStackHciFabricArmId")
    def az_stack_hci_fabric_arm_id(self) -> pulumi.Input[_builtins.str]: ...
    @az_stack_hci_fabric_arm_id.setter
    def az_stack_hci_fabric_arm_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareFabricArmId")
    def vmware_fabric_arm_id(self) -> pulumi.Input[_builtins.str]: ...
    @vmware_fabric_arm_id.setter
    def vmware_fabric_arm_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountSasSecretName")
    def storage_account_sas_secret_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_sas_secret_name.setter
    def storage_account_sas_secret_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class VaultModelPropertiesArgsDict(TypedDict):
    vault_type: NotRequired[pulumi.Input[Union[_builtins.str, ReplicationVaultType]]]

@pulumi.input_type
class VaultModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        vault_type: Optional[
            pulumi.Input[Union[_builtins.str, ReplicationVaultType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vaultType")
    def vault_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ReplicationVaultType]]]: ...
    @vault_type.setter
    def vault_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ReplicationVaultType]]]
    ): ...
