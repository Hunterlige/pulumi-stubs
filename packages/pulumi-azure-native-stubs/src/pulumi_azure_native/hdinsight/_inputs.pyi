import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationGetEndpointArgs",
    "ApplicationGetEndpointArgsDict",
    "ApplicationGetHttpsEndpointArgs",
    "ApplicationGetHttpsEndpointArgsDict",
    "ApplicationPropertiesArgs",
    "ApplicationPropertiesArgsDict",
    "AutoscaleCapacityArgs",
    "AutoscaleCapacityArgsDict",
    "AutoscaleRecurrenceArgs",
    "AutoscaleRecurrenceArgsDict",
    "AutoscaleScheduleArgs",
    "AutoscaleScheduleArgsDict",
    "AutoscaleTimeAndCapacityArgs",
    "AutoscaleTimeAndCapacityArgsDict",
    "AutoscaleArgs",
    "AutoscaleArgsDict",
    "AzureMonitorSelectedConfigurationsArgs",
    "AzureMonitorSelectedConfigurationsArgsDict",
    "AzureMonitorTableConfigurationArgs",
    "AzureMonitorTableConfigurationArgsDict",
    "ClientGroupInfoArgs",
    "ClientGroupInfoArgsDict",
    "ClusterCreatePropertiesArgs",
    "ClusterCreatePropertiesArgsDict",
    "ClusterDefinitionArgs",
    "ClusterDefinitionArgsDict",
    "ClusterIdentityArgs",
    "ClusterIdentityArgsDict",
    "ComputeIsolationPropertiesArgs",
    "ComputeIsolationPropertiesArgsDict",
    "ComputeProfileArgs",
    "ComputeProfileArgsDict",
    "DataDisksGroupsArgs",
    "DataDisksGroupsArgsDict",
    "DiskEncryptionPropertiesArgs",
    "DiskEncryptionPropertiesArgsDict",
    "EncryptionInTransitPropertiesArgs",
    "EncryptionInTransitPropertiesArgsDict",
    "ErrorsArgs",
    "ErrorsArgsDict",
    "HardwareProfileArgs",
    "HardwareProfileArgsDict",
    "IPConfigurationArgs",
    "IPConfigurationArgsDict",
    "IpTagArgs",
    "IpTagArgsDict",
    "KafkaRestPropertiesArgs",
    "KafkaRestPropertiesArgsDict",
    "LinuxOperatingSystemProfileArgs",
    "LinuxOperatingSystemProfileArgsDict",
    "NetworkPropertiesArgs",
    "NetworkPropertiesArgsDict",
    "OsProfileArgs",
    "OsProfileArgsDict",
    "PrivateLinkConfigurationArgs",
    "PrivateLinkConfigurationArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "ResourceIdArgs",
    "ResourceIdArgsDict",
    "RoleArgs",
    "RoleArgsDict",
    "RuntimeScriptActionArgs",
    "RuntimeScriptActionArgsDict",
    "ScriptActionArgs",
    "ScriptActionArgsDict",
    "SecurityProfileArgs",
    "SecurityProfileArgsDict",
    "SshProfileArgs",
    "SshProfileArgsDict",
    "SshPublicKeyArgs",
    "SshPublicKeyArgsDict",
    "StorageAccountArgs",
    "StorageAccountArgsDict",
    "StorageProfileArgs",
    "StorageProfileArgsDict",
    "UserAssignedIdentityArgs",
    "UserAssignedIdentityArgsDict",
    "VirtualNetworkProfileArgs",
    "VirtualNetworkProfileArgsDict",
]

class ApplicationGetEndpointArgsDict(TypedDict):
    destination_port: NotRequired[pulumi.Input[_builtins.int]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    public_port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ApplicationGetEndpointArgs:
    def __init__(
        __self__,
        *,
        destination_port: Optional[pulumi.Input[_builtins.int]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        public_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicPort")
    def public_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @public_port.setter
    def public_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ApplicationGetHttpsEndpointArgsDict(TypedDict):
    access_modes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    destination_port: NotRequired[pulumi.Input[_builtins.int]]
    disable_gateway_auth: NotRequired[pulumi.Input[_builtins.bool]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    sub_domain_suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationGetHttpsEndpointArgs:
    def __init__(
        __self__,
        *,
        access_modes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        destination_port: Optional[pulumi.Input[_builtins.int]] = ...,
        disable_gateway_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        private_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_domain_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessModes")
    def access_modes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @access_modes.setter
    def access_modes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="disableGatewayAuth")
    def disable_gateway_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_gateway_auth.setter
    def disable_gateway_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subDomainSuffix")
    def sub_domain_suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sub_domain_suffix.setter
    def sub_domain_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationPropertiesArgsDict(TypedDict):
    application_type: NotRequired[pulumi.Input[_builtins.str]]
    compute_profile: NotRequired[pulumi.Input[ComputeProfileArgsDict]]
    errors: NotRequired[pulumi.Input[Sequence[pulumi.Input[ErrorsArgsDict]]]]
    https_endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGetHttpsEndpointArgsDict]]]
    ]
    install_script_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RuntimeScriptActionArgsDict]]]
    ]
    private_link_configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkConfigurationArgsDict]]]
    ]
    ssh_endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGetEndpointArgsDict]]]
    ]
    uninstall_script_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RuntimeScriptActionArgsDict]]]
    ]

@pulumi.input_type
class ApplicationPropertiesArgs:
    def __init__(
        __self__,
        *,
        application_type: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_profile: Optional[pulumi.Input[ComputeProfileArgs]] = ...,
        errors: Optional[pulumi.Input[Sequence[pulumi.Input[ErrorsArgs]]]] = ...,
        https_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGetHttpsEndpointArgs]]]
        ] = ...,
        install_script_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuntimeScriptActionArgs]]]
        ] = ...,
        private_link_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkConfigurationArgs]]]
        ] = ...,
        ssh_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGetEndpointArgs]]]
        ] = ...,
        uninstall_script_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuntimeScriptActionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_type.setter
    def application_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> Optional[pulumi.Input[ComputeProfileArgs]]: ...
    @compute_profile.setter
    def compute_profile(self, value: Optional[pulumi.Input[ComputeProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ErrorsArgs]]]]: ...
    @errors.setter
    def errors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ErrorsArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpsEndpoints")
    def https_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGetHttpsEndpointArgs]]]
    ]: ...
    @https_endpoints.setter
    def https_endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGetHttpsEndpointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="installScriptActions")
    def install_script_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuntimeScriptActionArgs]]]]: ...
    @install_script_actions.setter
    def install_script_actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RuntimeScriptActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkConfigurations")
    def private_link_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkConfigurationArgs]]]
    ]: ...
    @private_link_configurations.setter
    def private_link_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sshEndpoints")
    def ssh_endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationGetEndpointArgs]]]]: ...
    @ssh_endpoints.setter
    def ssh_endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGetEndpointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="uninstallScriptActions")
    def uninstall_script_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuntimeScriptActionArgs]]]]: ...
    @uninstall_script_actions.setter
    def uninstall_script_actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RuntimeScriptActionArgs]]]],
    ): ...

class AutoscaleCapacityArgsDict(TypedDict):
    max_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    min_instance_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AutoscaleCapacityArgs:
    def __init__(
        __self__,
        *,
        max_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_instance_count.setter
    def max_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instance_count.setter
    def min_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AutoscaleRecurrenceArgsDict(TypedDict):
    schedule: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutoscaleScheduleArgsDict]]]
    ]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutoscaleRecurrenceArgs:
    def __init__(
        __self__,
        *,
        schedule: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutoscaleScheduleArgs]]]
        ] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schedule(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AutoscaleScheduleArgs]]]]: ...
    @schedule.setter
    def schedule(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AutoscaleScheduleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutoscaleScheduleArgsDict(TypedDict):
    days: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DaysOfWeek]]]]
    ]
    time_and_capacity: NotRequired[pulumi.Input[AutoscaleTimeAndCapacityArgsDict]]

@pulumi.input_type
class AutoscaleScheduleArgs:
    def __init__(
        __self__,
        *,
        days: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DaysOfWeek]]]]
        ] = ...,
        time_and_capacity: Optional[pulumi.Input[AutoscaleTimeAndCapacityArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DaysOfWeek]]]]
    ]: ...
    @days.setter
    def days(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DaysOfWeek]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeAndCapacity")
    def time_and_capacity(
        self,
    ) -> Optional[pulumi.Input[AutoscaleTimeAndCapacityArgs]]: ...
    @time_and_capacity.setter
    def time_and_capacity(
        self, value: Optional[pulumi.Input[AutoscaleTimeAndCapacityArgs]]
    ): ...

class AutoscaleTimeAndCapacityArgsDict(TypedDict):
    max_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    min_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutoscaleTimeAndCapacityArgs:
    def __init__(
        __self__,
        *,
        max_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_instance_count.setter
    def max_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instance_count.setter
    def min_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time.setter
    def time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutoscaleArgsDict(TypedDict):
    capacity: NotRequired[pulumi.Input[AutoscaleCapacityArgsDict]]
    recurrence: NotRequired[pulumi.Input[AutoscaleRecurrenceArgsDict]]

@pulumi.input_type
class AutoscaleArgs:
    def __init__(
        __self__,
        *,
        capacity: Optional[pulumi.Input[AutoscaleCapacityArgs]] = ...,
        recurrence: Optional[pulumi.Input[AutoscaleRecurrenceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[AutoscaleCapacityArgs]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[AutoscaleCapacityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input[AutoscaleRecurrenceArgs]]: ...
    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input[AutoscaleRecurrenceArgs]]): ...

class AzureMonitorSelectedConfigurationsArgsDict(TypedDict):
    configuration_version: NotRequired[pulumi.Input[_builtins.str]]
    global_configurations: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    table_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AzureMonitorTableConfigurationArgsDict]]]
    ]

@pulumi.input_type
class AzureMonitorSelectedConfigurationsArgs:
    def __init__(
        __self__,
        *,
        configuration_version: Optional[pulumi.Input[_builtins.str]] = ...,
        global_configurations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        table_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[AzureMonitorTableConfigurationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationVersion")
    def configuration_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_version.setter
    def configuration_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="globalConfigurations")
    def global_configurations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @global_configurations.setter
    def global_configurations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tableList")
    def table_list(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AzureMonitorTableConfigurationArgs]]]
    ]: ...
    @table_list.setter
    def table_list(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AzureMonitorTableConfigurationArgs]]]
        ],
    ): ...

class AzureMonitorTableConfigurationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureMonitorTableConfigurationArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClientGroupInfoArgsDict(TypedDict):
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    group_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClientGroupInfoArgs:
    def __init__(
        __self__,
        *,
        group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterCreatePropertiesArgsDict(TypedDict):
    cluster_definition: NotRequired[pulumi.Input[ClusterDefinitionArgsDict]]
    cluster_version: NotRequired[pulumi.Input[_builtins.str]]
    compute_isolation_properties: NotRequired[
        pulumi.Input[ComputeIsolationPropertiesArgsDict]
    ]
    compute_profile: NotRequired[pulumi.Input[ComputeProfileArgsDict]]
    disk_encryption_properties: NotRequired[
        pulumi.Input[DiskEncryptionPropertiesArgsDict]
    ]
    encryption_in_transit_properties: NotRequired[
        pulumi.Input[EncryptionInTransitPropertiesArgsDict]
    ]
    kafka_rest_properties: NotRequired[pulumi.Input[KafkaRestPropertiesArgsDict]]
    min_supported_tls_version: NotRequired[pulumi.Input[_builtins.str]]
    network_properties: NotRequired[pulumi.Input[NetworkPropertiesArgsDict]]
    os_type: NotRequired[pulumi.Input[Union[_builtins.str, OSType]]]
    private_link_configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkConfigurationArgsDict]]]
    ]
    security_profile: NotRequired[pulumi.Input[SecurityProfileArgsDict]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, Tier]]]

@pulumi.input_type
class ClusterCreatePropertiesArgs:
    def __init__(
        __self__,
        *,
        cluster_definition: Optional[pulumi.Input[ClusterDefinitionArgs]] = ...,
        cluster_version: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_isolation_properties: Optional[
            pulumi.Input[ComputeIsolationPropertiesArgs]
        ] = ...,
        compute_profile: Optional[pulumi.Input[ComputeProfileArgs]] = ...,
        disk_encryption_properties: Optional[
            pulumi.Input[DiskEncryptionPropertiesArgs]
        ] = ...,
        encryption_in_transit_properties: Optional[
            pulumi.Input[EncryptionInTransitPropertiesArgs]
        ] = ...,
        kafka_rest_properties: Optional[pulumi.Input[KafkaRestPropertiesArgs]] = ...,
        min_supported_tls_version: Optional[pulumi.Input[_builtins.str]] = ...,
        network_properties: Optional[pulumi.Input[NetworkPropertiesArgs]] = ...,
        os_type: Optional[pulumi.Input[Union[_builtins.str, OSType]]] = ...,
        private_link_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkConfigurationArgs]]]
        ] = ...,
        security_profile: Optional[pulumi.Input[SecurityProfileArgs]] = ...,
        storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ...,
        tier: Optional[pulumi.Input[Union[_builtins.str, Tier]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterDefinition")
    def cluster_definition(self) -> Optional[pulumi.Input[ClusterDefinitionArgs]]: ...
    @cluster_definition.setter
    def cluster_definition(
        self, value: Optional[pulumi.Input[ClusterDefinitionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_version.setter
    def cluster_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeIsolationProperties")
    def compute_isolation_properties(
        self,
    ) -> Optional[pulumi.Input[ComputeIsolationPropertiesArgs]]: ...
    @compute_isolation_properties.setter
    def compute_isolation_properties(
        self, value: Optional[pulumi.Input[ComputeIsolationPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> Optional[pulumi.Input[ComputeProfileArgs]]: ...
    @compute_profile.setter
    def compute_profile(self, value: Optional[pulumi.Input[ComputeProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionProperties")
    def disk_encryption_properties(
        self,
    ) -> Optional[pulumi.Input[DiskEncryptionPropertiesArgs]]: ...
    @disk_encryption_properties.setter
    def disk_encryption_properties(
        self, value: Optional[pulumi.Input[DiskEncryptionPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionInTransitProperties")
    def encryption_in_transit_properties(
        self,
    ) -> Optional[pulumi.Input[EncryptionInTransitPropertiesArgs]]: ...
    @encryption_in_transit_properties.setter
    def encryption_in_transit_properties(
        self, value: Optional[pulumi.Input[EncryptionInTransitPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kafkaRestProperties")
    def kafka_rest_properties(
        self,
    ) -> Optional[pulumi.Input[KafkaRestPropertiesArgs]]: ...
    @kafka_rest_properties.setter
    def kafka_rest_properties(
        self, value: Optional[pulumi.Input[KafkaRestPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minSupportedTlsVersion")
    def min_supported_tls_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_supported_tls_version.setter
    def min_supported_tls_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkProperties")
    def network_properties(self) -> Optional[pulumi.Input[NetworkPropertiesArgs]]: ...
    @network_properties.setter
    def network_properties(
        self, value: Optional[pulumi.Input[NetworkPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OSType]]]: ...
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OSType]]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkConfigurations")
    def private_link_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkConfigurationArgs]]]
    ]: ...
    @private_link_configurations.setter
    def private_link_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[SecurityProfileArgs]]: ...
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[SecurityProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[_builtins.str, Tier]]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[_builtins.str, Tier]]]): ...

class ClusterDefinitionArgsDict(TypedDict):
    blueprint: NotRequired[pulumi.Input[_builtins.str]]
    component_version: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    configurations: NotRequired[Any]
    kind: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterDefinitionArgs:
    def __init__(
        __self__,
        *,
        blueprint: Optional[pulumi.Input[_builtins.str]] = ...,
        component_version: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        configurations: Optional[Any] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def blueprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blueprint.setter
    def blueprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="componentVersion")
    def component_version(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @component_version.setter
    def component_version(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Any]: ...
    @configurations.setter
    def configurations(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgsDict]]]
    ]

@pulumi.input_type
class ClusterIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
    ]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
        ],
    ): ...

class ComputeIsolationPropertiesArgsDict(TypedDict):
    enable_compute_isolation: NotRequired[pulumi.Input[_builtins.bool]]
    host_sku: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ComputeIsolationPropertiesArgs:
    def __init__(
        __self__,
        *,
        enable_compute_isolation: Optional[pulumi.Input[_builtins.bool]] = ...,
        host_sku: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComputeIsolation")
    def enable_compute_isolation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_compute_isolation.setter
    def enable_compute_isolation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostSku")
    def host_sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_sku.setter
    def host_sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ComputeProfileArgsDict(TypedDict):
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[RoleArgsDict]]]]

@pulumi.input_type
class ComputeProfileArgs:
    def __init__(
        __self__,
        *,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[RoleArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoleArgs]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RoleArgs]]]]
    ): ...

class DataDisksGroupsArgsDict(TypedDict):
    disks_per_node: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DataDisksGroupsArgs:
    def __init__(
        __self__, *, disks_per_node: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disksPerNode")
    def disks_per_node(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disks_per_node.setter
    def disks_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DiskEncryptionPropertiesArgsDict(TypedDict):
    encryption_algorithm: NotRequired[
        pulumi.Input[Union[_builtins.str, JsonWebKeyEncryptionAlgorithm]]
    ]
    encryption_at_host: NotRequired[pulumi.Input[_builtins.bool]]
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    key_version: NotRequired[pulumi.Input[_builtins.str]]
    msi_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    vault_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DiskEncryptionPropertiesArgs:
    def __init__(
        __self__,
        *,
        encryption_algorithm: Optional[
            pulumi.Input[Union[_builtins.str, JsonWebKeyEncryptionAlgorithm]]
        ] = ...,
        encryption_at_host: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_version: Optional[pulumi.Input[_builtins.str]] = ...,
        msi_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vault_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, JsonWebKeyEncryptionAlgorithm]]
    ]: ...
    @encryption_algorithm.setter
    def encryption_algorithm(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, JsonWebKeyEncryptionAlgorithm]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encryption_at_host.setter
    def encryption_at_host(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="msiResourceId")
    def msi_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @msi_resource_id.setter
    def msi_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vaultUri")
    def vault_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vault_uri.setter
    def vault_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EncryptionInTransitPropertiesArgsDict(TypedDict):
    is_encryption_in_transit_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class EncryptionInTransitPropertiesArgs:
    def __init__(
        __self__,
        *,
        is_encryption_in_transit_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEncryptionInTransitEnabled")
    def is_encryption_in_transit_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_encryption_in_transit_enabled.setter
    def is_encryption_in_transit_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ErrorsArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ErrorsArgs:
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

class HardwareProfileArgsDict(TypedDict):
    vm_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HardwareProfileArgs:
    def __init__(
        __self__, *, vm_size: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IPConfigurationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    primary: NotRequired[pulumi.Input[_builtins.bool]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_allocation_method: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateIPAllocationMethod]]
    ]
    subnet: NotRequired[pulumi.Input[ResourceIdArgsDict]]

@pulumi.input_type
class IPConfigurationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        primary: Optional[pulumi.Input[_builtins.bool]] = ...,
        private_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_allocation_method: Optional[
            pulumi.Input[Union[_builtins.str, PrivateIPAllocationMethod]]
        ] = ...,
        subnet: Optional[pulumi.Input[ResourceIdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIPAllocationMethod")
    def private_ip_allocation_method(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrivateIPAllocationMethod]]]: ...
    @private_ip_allocation_method.setter
    def private_ip_allocation_method(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PrivateIPAllocationMethod]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[ResourceIdArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[ResourceIdArgs]]): ...

class IpTagArgsDict(TypedDict):
    ip_tag_type: pulumi.Input[_builtins.str]
    tag: pulumi.Input[_builtins.str]

@pulumi.input_type
class IpTagArgs:
    def __init__(
        __self__,
        *,
        ip_tag_type: pulumi.Input[_builtins.str],
        tag: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipTagType")
    def ip_tag_type(self) -> pulumi.Input[_builtins.str]: ...
    @ip_tag_type.setter
    def ip_tag_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> pulumi.Input[_builtins.str]: ...
    @tag.setter
    def tag(self, value: pulumi.Input[_builtins.str]): ...

class KafkaRestPropertiesArgsDict(TypedDict):
    client_group_info: NotRequired[pulumi.Input[ClientGroupInfoArgsDict]]
    configuration_override: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class KafkaRestPropertiesArgs:
    def __init__(
        __self__,
        *,
        client_group_info: Optional[pulumi.Input[ClientGroupInfoArgs]] = ...,
        configuration_override: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientGroupInfo")
    def client_group_info(self) -> Optional[pulumi.Input[ClientGroupInfoArgs]]: ...
    @client_group_info.setter
    def client_group_info(self, value: Optional[pulumi.Input[ClientGroupInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="configurationOverride")
    def configuration_override(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @configuration_override.setter
    def configuration_override(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class LinuxOperatingSystemProfileArgsDict(TypedDict):
    password: NotRequired[pulumi.Input[_builtins.str]]
    ssh_profile: NotRequired[pulumi.Input[SshProfileArgsDict]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LinuxOperatingSystemProfileArgs:
    def __init__(
        __self__,
        *,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        ssh_profile: Optional[pulumi.Input[SshProfileArgs]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sshProfile")
    def ssh_profile(self) -> Optional[pulumi.Input[SshProfileArgs]]: ...
    @ssh_profile.setter
    def ssh_profile(self, value: Optional[pulumi.Input[SshProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkPropertiesArgsDict(TypedDict):
    outbound_dependencies_managed_type: NotRequired[
        pulumi.Input[Union[_builtins.str, OutboundDependenciesManagedType]]
    ]
    private_link: NotRequired[pulumi.Input[Union[_builtins.str, PrivateLink]]]
    public_ip_tag: NotRequired[pulumi.Input[IpTagArgsDict]]
    resource_provider_connection: NotRequired[
        pulumi.Input[Union[_builtins.str, ResourceProviderConnection]]
    ]

@pulumi.input_type
class NetworkPropertiesArgs:
    def __init__(
        __self__,
        *,
        outbound_dependencies_managed_type: Optional[
            pulumi.Input[Union[_builtins.str, OutboundDependenciesManagedType]]
        ] = ...,
        private_link: Optional[pulumi.Input[Union[_builtins.str, PrivateLink]]] = ...,
        public_ip_tag: Optional[pulumi.Input[IpTagArgs]] = ...,
        resource_provider_connection: Optional[
            pulumi.Input[Union[_builtins.str, ResourceProviderConnection]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outboundDependenciesManagedType")
    def outbound_dependencies_managed_type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, OutboundDependenciesManagedType]]
    ]: ...
    @outbound_dependencies_managed_type.setter
    def outbound_dependencies_managed_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, OutboundDependenciesManagedType]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateLink")
    def private_link(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrivateLink]]]: ...
    @private_link.setter
    def private_link(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateLink]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIpTag")
    def public_ip_tag(self) -> Optional[pulumi.Input[IpTagArgs]]: ...
    @public_ip_tag.setter
    def public_ip_tag(self, value: Optional[pulumi.Input[IpTagArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceProviderConnection")
    def resource_provider_connection(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceProviderConnection]]]: ...
    @resource_provider_connection.setter
    def resource_provider_connection(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ResourceProviderConnection]]],
    ): ...

class OsProfileArgsDict(TypedDict):
    linux_operating_system_profile: NotRequired[
        pulumi.Input[LinuxOperatingSystemProfileArgsDict]
    ]

@pulumi.input_type
class OsProfileArgs:
    def __init__(
        __self__,
        *,
        linux_operating_system_profile: Optional[
            pulumi.Input[LinuxOperatingSystemProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxOperatingSystemProfile")
    def linux_operating_system_profile(
        self,
    ) -> Optional[pulumi.Input[LinuxOperatingSystemProfileArgs]]: ...
    @linux_operating_system_profile.setter
    def linux_operating_system_profile(
        self, value: Optional[pulumi.Input[LinuxOperatingSystemProfileArgs]]
    ): ...

class PrivateLinkConfigurationArgsDict(TypedDict):
    group_id: pulumi.Input[_builtins.str]
    ip_configurations: pulumi.Input[Sequence[pulumi.Input[IPConfigurationArgsDict]]]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class PrivateLinkConfigurationArgs:
    def __init__(
        __self__,
        *,
        group_id: pulumi.Input[_builtins.str],
        ip_configurations: pulumi.Input[Sequence[pulumi.Input[IPConfigurationArgs]]],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[_builtins.str]: ...
    @group_id.setter
    def group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[IPConfigurationArgs]]]: ...
    @ip_configurations.setter
    def ip_configurations(
        self, value: pulumi.Input[Sequence[pulumi.Input[IPConfigurationArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    status: pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        status: pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]],
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]: ...
    @status.setter
    def status(
        self,
        value: pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]],
    ): ...
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

class ResourceIdArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceIdArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RoleArgsDict(TypedDict):
    autoscale_configuration: NotRequired[pulumi.Input[AutoscaleArgsDict]]
    data_disks_groups: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DataDisksGroupsArgsDict]]]
    ]
    encrypt_data_disks: NotRequired[pulumi.Input[_builtins.bool]]
    hardware_profile: NotRequired[pulumi.Input[HardwareProfileArgsDict]]
    min_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    os_profile: NotRequired[pulumi.Input[OsProfileArgsDict]]
    script_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ScriptActionArgsDict]]]
    ]
    target_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    v_m_group_name: NotRequired[pulumi.Input[_builtins.str]]
    virtual_network_profile: NotRequired[pulumi.Input[VirtualNetworkProfileArgsDict]]

@pulumi.input_type
class RoleArgs:
    def __init__(
        __self__,
        *,
        autoscale_configuration: Optional[pulumi.Input[AutoscaleArgs]] = ...,
        data_disks_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataDisksGroupsArgs]]]
        ] = ...,
        encrypt_data_disks: Optional[pulumi.Input[_builtins.bool]] = ...,
        hardware_profile: Optional[pulumi.Input[HardwareProfileArgs]] = ...,
        min_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_profile: Optional[pulumi.Input[OsProfileArgs]] = ...,
        script_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScriptActionArgs]]]
        ] = ...,
        target_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        v_m_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_profile: Optional[
            pulumi.Input[VirtualNetworkProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscaleConfiguration")
    def autoscale_configuration(self) -> Optional[pulumi.Input[AutoscaleArgs]]: ...
    @autoscale_configuration.setter
    def autoscale_configuration(self, value: Optional[pulumi.Input[AutoscaleArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDisksGroups")
    def data_disks_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataDisksGroupsArgs]]]]: ...
    @data_disks_groups.setter
    def data_disks_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataDisksGroupsArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptDataDisks")
    def encrypt_data_disks(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encrypt_data_disks.setter
    def encrypt_data_disks(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input[HardwareProfileArgs]]: ...
    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input[HardwareProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instance_count.setter
    def min_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input[OsProfileArgs]]: ...
    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input[OsProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptActions")
    def script_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScriptActionArgs]]]]: ...
    @script_actions.setter
    def script_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScriptActionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetInstanceCount")
    def target_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_instance_count.setter
    def target_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="vMGroupName")
    def v_m_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @v_m_group_name.setter
    def v_m_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkProfile")
    def virtual_network_profile(
        self,
    ) -> Optional[pulumi.Input[VirtualNetworkProfileArgs]]: ...
    @virtual_network_profile.setter
    def virtual_network_profile(
        self, value: Optional[pulumi.Input[VirtualNetworkProfileArgs]]
    ): ...

class RuntimeScriptActionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    roles: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    uri: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RuntimeScriptActionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        roles: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        uri: pulumi.Input[_builtins.str],
        parameters: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @roles.setter
    def roles(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScriptActionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class ScriptActionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        parameters: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[_builtins.str]: ...
    @parameters.setter
    def parameters(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...

class SecurityProfileArgsDict(TypedDict):
    aadds_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    cluster_users_group_dns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    directory_type: NotRequired[pulumi.Input[Union[_builtins.str, DirectoryType]]]
    domain: NotRequired[pulumi.Input[_builtins.str]]
    domain_user_password: NotRequired[pulumi.Input[_builtins.str]]
    domain_username: NotRequired[pulumi.Input[_builtins.str]]
    ldaps_urls: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    msi_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit_dn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityProfileArgs:
    def __init__(
        __self__,
        *,
        aadds_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_users_group_dns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        directory_type: Optional[
            pulumi.Input[Union[_builtins.str, DirectoryType]]
        ] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_user_password: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_username: Optional[pulumi.Input[_builtins.str]] = ...,
        ldaps_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        msi_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_unit_dn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aaddsResourceId")
    def aadds_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aadds_resource_id.setter
    def aadds_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterUsersGroupDNs")
    def cluster_users_group_dns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cluster_users_group_dns.setter
    def cluster_users_group_dns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="directoryType")
    def directory_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DirectoryType]]]: ...
    @directory_type.setter
    def directory_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DirectoryType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainUserPassword")
    def domain_user_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_user_password.setter
    def domain_user_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainUsername")
    def domain_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_username.setter
    def domain_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ldapsUrls")
    def ldaps_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ldaps_urls.setter
    def ldaps_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="msiResourceId")
    def msi_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @msi_resource_id.setter
    def msi_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDN")
    def organizational_unit_dn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organizational_unit_dn.setter
    def organizational_unit_dn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SshProfileArgsDict(TypedDict):
    public_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgsDict]]]]

@pulumi.input_type
class SshProfileArgs:
    def __init__(
        __self__,
        *,
        public_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]]: ...
    @public_keys.setter
    def public_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]]
    ): ...

class SshPublicKeyArgsDict(TypedDict):
    certificate_data: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SshPublicKeyArgs:
    def __init__(
        __self__, *, certificate_data: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateData")
    def certificate_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_data.setter
    def certificate_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageAccountArgsDict(TypedDict):
    container: NotRequired[pulumi.Input[_builtins.str]]
    enable_secure_channel: NotRequired[pulumi.Input[_builtins.bool]]
    file_system: NotRequired[pulumi.Input[_builtins.str]]
    fileshare: NotRequired[pulumi.Input[_builtins.str]]
    is_default: NotRequired[pulumi.Input[_builtins.bool]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    msi_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    saskey: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageAccountArgs:
    def __init__(
        __self__,
        *,
        container: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_secure_channel: Optional[pulumi.Input[_builtins.bool]] = ...,
        file_system: Optional[pulumi.Input[_builtins.str]] = ...,
        fileshare: Optional[pulumi.Input[_builtins.str]] = ...,
        is_default: Optional[pulumi.Input[_builtins.bool]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        msi_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        saskey: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container.setter
    def container(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableSecureChannel")
    def enable_secure_channel(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_secure_channel.setter
    def enable_secure_channel(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystem")
    def file_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system.setter
    def file_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fileshare(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fileshare.setter
    def fileshare(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="msiResourceId")
    def msi_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @msi_resource_id.setter
    def msi_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def saskey(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @saskey.setter
    def saskey(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageProfileArgsDict(TypedDict):
    storageaccounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StorageAccountArgsDict]]]
    ]

@pulumi.input_type
class StorageProfileArgs:
    def __init__(
        __self__,
        *,
        storageaccounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[StorageAccountArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def storageaccounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[StorageAccountArgs]]]]: ...
    @storageaccounts.setter
    def storageaccounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StorageAccountArgs]]]]
    ): ...

class UserAssignedIdentityArgsDict(TypedDict):
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserAssignedIdentityArgs:
    def __init__(
        __self__, *, tenant_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworkProfileArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    subnet: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNetworkProfileArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
