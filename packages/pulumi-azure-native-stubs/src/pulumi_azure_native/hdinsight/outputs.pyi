import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationGetEndpointResponse",
    "ApplicationGetHttpsEndpointResponse",
    "ApplicationPropertiesResponse",
    "AutoscaleCapacityResponse",
    "AutoscaleRecurrenceResponse",
    "AutoscaleResponse",
    "AutoscaleScheduleResponse",
    "AutoscaleTimeAndCapacityResponse",
    "AzureMonitorSelectedConfigurationsResponse",
    "AzureMonitorTableConfigurationResponse",
    "ClientGroupInfoResponse",
    "ClusterDefinitionResponse",
    "ClusterGetPropertiesResponse",
    "ClusterIdentityResponse",
    "ComputeIsolationPropertiesResponse",
    "ComputeProfileResponse",
    "ConnectivityEndpointResponse",
    "DataDisksGroupsResponse",
    "DiskEncryptionPropertiesResponse",
    "EncryptionInTransitPropertiesResponse",
    "ErrorsResponse",
    "ExcludedServicesConfigResponse",
    "HardwareProfileResponse",
    "IPConfigurationResponse",
    "IpTagResponse",
    "KafkaRestPropertiesResponse",
    "LinuxOperatingSystemProfileResponse",
    "NetworkPropertiesResponse",
    "OsProfileResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "PrivateLinkConfigurationResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "QuotaInfoResponse",
    "ResourceIdResponse",
    "RoleResponse",
    "RuntimeScriptActionResponse",
    "ScriptActionResponse",
    "SecurityProfileResponse",
    "SshProfileResponse",
    "SshPublicKeyResponse",
    "StorageAccountResponse",
    "StorageProfileResponse",
    "SystemDataResponse",
    "UserAssignedIdentityResponse",
    "VirtualNetworkProfileResponse",
]

@pulumi.output_type
class ApplicationGetEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_port: Optional[_builtins.int] = ...,
        location: Optional[_builtins.str] = ...,
        private_ip_address: Optional[_builtins.str] = ...,
        public_port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicPort")
    def public_port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ApplicationGetHttpsEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: _builtins.str,
        public_port: _builtins.int,
        access_modes: Optional[Sequence[_builtins.str]] = ...,
        destination_port: Optional[_builtins.int] = ...,
        disable_gateway_auth: Optional[_builtins.bool] = ...,
        private_ip_address: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicPort")
    def public_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="accessModes")
    def access_modes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="disableGatewayAuth")
    def disable_gateway_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_state: _builtins.str,
        created_date: _builtins.str,
        marketplace_identifier: _builtins.str,
        provisioning_state: _builtins.str,
        application_type: Optional[_builtins.str] = ...,
        compute_profile: Optional[outputs.ComputeProfileResponse] = ...,
        errors: Optional[Sequence[outputs.ErrorsResponse]] = ...,
        https_endpoints: Optional[
            Sequence[outputs.ApplicationGetHttpsEndpointResponse]
        ] = ...,
        install_script_actions: Optional[
            Sequence[outputs.RuntimeScriptActionResponse]
        ] = ...,
        private_link_configurations: Optional[
            Sequence[outputs.PrivateLinkConfigurationResponse]
        ] = ...,
        ssh_endpoints: Optional[Sequence[outputs.ApplicationGetEndpointResponse]] = ...,
        uninstall_script_actions: Optional[
            Sequence[outputs.RuntimeScriptActionResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationState")
    def application_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="marketplaceIdentifier")
    def marketplace_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> Optional[outputs.ComputeProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[outputs.ErrorsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="httpsEndpoints")
    def https_endpoints(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGetHttpsEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="installScriptActions")
    def install_script_actions(
        self,
    ) -> Optional[Sequence[outputs.RuntimeScriptActionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkConfigurations")
    def private_link_configurations(
        self,
    ) -> Optional[Sequence[outputs.PrivateLinkConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sshEndpoints")
    def ssh_endpoints(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGetEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="uninstallScriptActions")
    def uninstall_script_actions(
        self,
    ) -> Optional[Sequence[outputs.RuntimeScriptActionResponse]]: ...

@pulumi.output_type
class AutoscaleCapacityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_instance_count: Optional[_builtins.int] = ...,
        min_instance_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AutoscaleRecurrenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schedule: Optional[Sequence[outputs.AutoscaleScheduleResponse]] = ...,
        time_zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[Sequence[outputs.AutoscaleScheduleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutoscaleResponse(dict):
    def __init__(
        __self__,
        *,
        capacity: Optional[outputs.AutoscaleCapacityResponse] = ...,
        recurrence: Optional[outputs.AutoscaleRecurrenceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[outputs.AutoscaleCapacityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[outputs.AutoscaleRecurrenceResponse]: ...

@pulumi.output_type
class AutoscaleScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        days: Optional[Sequence[_builtins.str]] = ...,
        time_and_capacity: Optional[outputs.AutoscaleTimeAndCapacityResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeAndCapacity")
    def time_and_capacity(
        self,
    ) -> Optional[outputs.AutoscaleTimeAndCapacityResponse]: ...

@pulumi.output_type
class AutoscaleTimeAndCapacityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_instance_count: Optional[_builtins.int] = ...,
        min_instance_count: Optional[_builtins.int] = ...,
        time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureMonitorSelectedConfigurationsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_version: Optional[_builtins.str] = ...,
        global_configurations: Optional[Mapping[str, _builtins.str]] = ...,
        table_list: Optional[
            Sequence[outputs.AzureMonitorTableConfigurationResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationVersion")
    def configuration_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="globalConfigurations")
    def global_configurations(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tableList")
    def table_list(
        self,
    ) -> Optional[Sequence[outputs.AzureMonitorTableConfigurationResponse]]: ...

@pulumi.output_type
class AzureMonitorTableConfigurationResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClientGroupInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_id: Optional[_builtins.str] = ...,
        group_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        blueprint: Optional[_builtins.str] = ...,
        component_version: Optional[Mapping[str, _builtins.str]] = ...,
        configurations: Optional[Any] = ...,
        kind: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def blueprint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="componentVersion")
    def component_version(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterGetPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_definition: outputs.ClusterDefinitionResponse,
        private_endpoint_connections: Sequence[
            outputs.PrivateEndpointConnectionResponse
        ],
        cluster_hdp_version: Optional[_builtins.str] = ...,
        cluster_id: Optional[_builtins.str] = ...,
        cluster_state: Optional[_builtins.str] = ...,
        cluster_version: Optional[_builtins.str] = ...,
        compute_isolation_properties: Optional[
            outputs.ComputeIsolationPropertiesResponse
        ] = ...,
        compute_profile: Optional[outputs.ComputeProfileResponse] = ...,
        connectivity_endpoints: Optional[
            Sequence[outputs.ConnectivityEndpointResponse]
        ] = ...,
        created_date: Optional[_builtins.str] = ...,
        disk_encryption_properties: Optional[
            outputs.DiskEncryptionPropertiesResponse
        ] = ...,
        encryption_in_transit_properties: Optional[
            outputs.EncryptionInTransitPropertiesResponse
        ] = ...,
        errors: Optional[Sequence[outputs.ErrorsResponse]] = ...,
        excluded_services_config: Optional[
            outputs.ExcludedServicesConfigResponse
        ] = ...,
        kafka_rest_properties: Optional[outputs.KafkaRestPropertiesResponse] = ...,
        min_supported_tls_version: Optional[_builtins.str] = ...,
        network_properties: Optional[outputs.NetworkPropertiesResponse] = ...,
        os_type: Optional[_builtins.str] = ...,
        private_link_configurations: Optional[
            Sequence[outputs.PrivateLinkConfigurationResponse]
        ] = ...,
        provisioning_state: Optional[_builtins.str] = ...,
        quota_info: Optional[outputs.QuotaInfoResponse] = ...,
        security_profile: Optional[outputs.SecurityProfileResponse] = ...,
        storage_profile: Optional[outputs.StorageProfileResponse] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterDefinition")
    def cluster_definition(self) -> outputs.ClusterDefinitionResponse: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="clusterHdpVersion")
    def cluster_hdp_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterState")
    def cluster_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeIsolationProperties")
    def compute_isolation_properties(
        self,
    ) -> Optional[outputs.ComputeIsolationPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> Optional[outputs.ComputeProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="connectivityEndpoints")
    def connectivity_endpoints(
        self,
    ) -> Optional[Sequence[outputs.ConnectivityEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionProperties")
    def disk_encryption_properties(
        self,
    ) -> Optional[outputs.DiskEncryptionPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionInTransitProperties")
    def encryption_in_transit_properties(
        self,
    ) -> Optional[outputs.EncryptionInTransitPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[outputs.ErrorsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedServicesConfig")
    def excluded_services_config(
        self,
    ) -> Optional[outputs.ExcludedServicesConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="kafkaRestProperties")
    def kafka_rest_properties(
        self,
    ) -> Optional[outputs.KafkaRestPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="minSupportedTlsVersion")
    def min_supported_tls_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProperties")
    def network_properties(self) -> Optional[outputs.NetworkPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkConfigurations")
    def private_link_configurations(
        self,
    ) -> Optional[Sequence[outputs.PrivateLinkConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="quotaInfo")
    def quota_info(self) -> Optional[outputs.QuotaInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.SecurityProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[outputs.StorageProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class ComputeIsolationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_compute_isolation: Optional[_builtins.bool] = ...,
        host_sku: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComputeIsolation")
    def enable_compute_isolation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="hostSku")
    def host_sku(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ComputeProfileResponse(dict):
    def __init__(
        __self__, *, roles: Optional[Sequence[outputs.RoleResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[outputs.RoleResponse]]: ...

@pulumi.output_type
class ConnectivityEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        private_ip_address: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataDisksGroupsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_size_gb: _builtins.int,
        storage_account_type: _builtins.str,
        disks_per_node: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disksPerNode")
    def disks_per_node(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DiskEncryptionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_algorithm: Optional[_builtins.str] = ...,
        encryption_at_host: Optional[_builtins.bool] = ...,
        key_name: Optional[_builtins.str] = ...,
        key_version: Optional[_builtins.str] = ...,
        msi_resource_id: Optional[_builtins.str] = ...,
        vault_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="msiResourceId")
    def msi_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vaultUri")
    def vault_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EncryptionInTransitPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, is_encryption_in_transit_enabled: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEncryptionInTransitEnabled")
    def is_encryption_in_transit_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ErrorsResponse(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExcludedServicesConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        excluded_services_config_id: Optional[_builtins.str] = ...,
        excluded_services_list: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludedServicesConfigId")
    def excluded_services_config_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludedServicesList")
    def excluded_services_list(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HardwareProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, vm_size: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IPConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        provisioning_state: _builtins.str,
        type: _builtins.str,
        primary: Optional[_builtins.bool] = ...,
        private_ip_address: Optional[_builtins.str] = ...,
        private_ip_allocation_method: Optional[_builtins.str] = ...,
        subnet: Optional[outputs.ResourceIdResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateIPAllocationMethod")
    def private_ip_allocation_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[outputs.ResourceIdResponse]: ...

@pulumi.output_type
class IpTagResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, ip_tag_type: _builtins.str, tag: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipTagType")
    def ip_tag_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str: ...

@pulumi.output_type
class KafkaRestPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_group_info: Optional[outputs.ClientGroupInfoResponse] = ...,
        configuration_override: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientGroupInfo")
    def client_group_info(self) -> Optional[outputs.ClientGroupInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="configurationOverride")
    def configuration_override(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class LinuxOperatingSystemProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        password: Optional[_builtins.str] = ...,
        ssh_profile: Optional[outputs.SshProfileResponse] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sshProfile")
    def ssh_profile(self) -> Optional[outputs.SshProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        outbound_dependencies_managed_type: Optional[_builtins.str] = ...,
        private_link: Optional[_builtins.str] = ...,
        public_ip_tag: Optional[outputs.IpTagResponse] = ...,
        resource_provider_connection: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outboundDependenciesManagedType")
    def outbound_dependencies_managed_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLink")
    def private_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIpTag")
    def public_ip_tag(self) -> Optional[outputs.IpTagResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceProviderConnection")
    def resource_provider_connection(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        linux_operating_system_profile: Optional[
            outputs.LinuxOperatingSystemProfileResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxOperatingSystemProfile")
    def linux_operating_system_profile(
        self,
    ) -> Optional[outputs.LinuxOperatingSystemProfileResponse]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        link_identifier: _builtins.str,
        name: _builtins.str,
        private_endpoint: outputs.PrivateEndpointResponse,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkIdentifier")
    def link_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> outputs.PrivateEndpointResponse: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStateResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateEndpointResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateLinkConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_id: _builtins.str,
        id: _builtins.str,
        ip_configurations: Sequence[outputs.IPConfigurationResponse],
        name: _builtins.str,
        provisioning_state: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Sequence[outputs.IPConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        status: _builtins.str,
        actions_required: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class QuotaInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, cores_used: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coresUsed")
    def cores_used(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ResourceIdResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        autoscale_configuration: Optional[outputs.AutoscaleResponse] = ...,
        data_disks_groups: Optional[Sequence[outputs.DataDisksGroupsResponse]] = ...,
        encrypt_data_disks: Optional[_builtins.bool] = ...,
        hardware_profile: Optional[outputs.HardwareProfileResponse] = ...,
        min_instance_count: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
        os_profile: Optional[outputs.OsProfileResponse] = ...,
        script_actions: Optional[Sequence[outputs.ScriptActionResponse]] = ...,
        target_instance_count: Optional[_builtins.int] = ...,
        v_m_group_name: Optional[_builtins.str] = ...,
        virtual_network_profile: Optional[outputs.VirtualNetworkProfileResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscaleConfiguration")
    def autoscale_configuration(self) -> Optional[outputs.AutoscaleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dataDisksGroups")
    def data_disks_groups(
        self,
    ) -> Optional[Sequence[outputs.DataDisksGroupsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptDataDisks")
    def encrypt_data_disks(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[outputs.HardwareProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[outputs.OsProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scriptActions")
    def script_actions(self) -> Optional[Sequence[outputs.ScriptActionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="targetInstanceCount")
    def target_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vMGroupName")
    def v_m_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkProfile")
    def virtual_network_profile(
        self,
    ) -> Optional[outputs.VirtualNetworkProfileResponse]: ...

@pulumi.output_type
class RuntimeScriptActionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_name: _builtins.str,
        name: _builtins.str,
        roles: Sequence[_builtins.str],
        uri: _builtins.str,
        parameters: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScriptActionResponse(dict):
    def __init__(
        __self__, *, name: _builtins.str, parameters: _builtins.str, uri: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class SecurityProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aadds_resource_id: Optional[_builtins.str] = ...,
        cluster_users_group_dns: Optional[Sequence[_builtins.str]] = ...,
        directory_type: Optional[_builtins.str] = ...,
        domain: Optional[_builtins.str] = ...,
        domain_user_password: Optional[_builtins.str] = ...,
        domain_username: Optional[_builtins.str] = ...,
        ldaps_urls: Optional[Sequence[_builtins.str]] = ...,
        msi_resource_id: Optional[_builtins.str] = ...,
        organizational_unit_dn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aaddsResourceId")
    def aadds_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterUsersGroupDNs")
    def cluster_users_group_dns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="directoryType")
    def directory_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainUserPassword")
    def domain_user_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainUsername")
    def domain_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ldapsUrls")
    def ldaps_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="msiResourceId")
    def msi_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDN")
    def organizational_unit_dn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SshProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, public_keys: Optional[Sequence[outputs.SshPublicKeyResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Optional[Sequence[outputs.SshPublicKeyResponse]]: ...

@pulumi.output_type
class SshPublicKeyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_data: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateData")
    def certificate_data(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageAccountResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container: Optional[_builtins.str] = ...,
        enable_secure_channel: Optional[_builtins.bool] = ...,
        file_system: Optional[_builtins.str] = ...,
        fileshare: Optional[_builtins.str] = ...,
        is_default: Optional[_builtins.bool] = ...,
        key: Optional[_builtins.str] = ...,
        msi_resource_id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        resource_id: Optional[_builtins.str] = ...,
        saskey: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableSecureChannel")
    def enable_secure_channel(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystem")
    def file_system(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fileshare(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="msiResourceId")
    def msi_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def saskey(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageProfileResponse(dict):
    def __init__(
        __self__,
        *,
        storageaccounts: Optional[Sequence[outputs.StorageAccountResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def storageaccounts(self) -> Optional[Sequence[outputs.StorageAccountResponse]]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        principal_id: _builtins.str,
        tenant_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNetworkProfileResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        subnet: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[_builtins.str]: ...
