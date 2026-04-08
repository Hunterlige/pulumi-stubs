import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AlertQueryParameterResponse",
    "AlertRulePropertiesResponse",
    "AppServicePlanConfigurationResponse",
    "ApplicationServerConfigurationResponse",
    "ApplicationServerFullResourceNamesResponse",
    "ApplicationServerVmDetailsResponse",
    "CentralServerConfigurationResponse",
    "CentralServerFullResourceNamesResponse",
    "CentralServerVmDetailsResponse",
    "ConfigurationDataResponse",
    "ConnectorErrorDefinitionResponse",
    "CreateAndMountFileShareConfigurationResponse",
    "DBBackupPolicyPropertiesResponse",
    "DailyRetentionFormatResponse",
    "DailyRetentionScheduleResponse",
    "DailyScheduleResponse",
    "DatabaseConfigurationResponse",
    "DatabaseServerFullResourceNamesResponse",
    "DatabaseVmDetailsResponse",
    "DayResponse",
    "Db2ProviderInstancePropertiesResponse",
    "DeployerVmPackagesResponse",
    "DeploymentConfigurationResponse",
    "DeploymentWithOSConfigurationResponse",
    "DiscoveryConfigurationResponse",
    "DiskConfigurationResponse",
    "DiskDetailsResponse",
    "DiskExclusionPropertiesResponse",
    "DiskSkuResponse",
    "DiskVolumeConfigurationResponse",
    "EnqueueReplicationServerPropertiesResponse",
    "EnqueueServerPropertiesResponse",
    "ErrorAdditionalInfoResponse",
    "ErrorDefinitionResponse",
    "ErrorDefinitionResponseV1",
    "ErrorDefinitionResponseV2",
    "ErrorDefinitionResponseV3",
    "ErrorDetailResponse",
    "ExcelPerformanceDataResponse",
    "ExistingRecoveryServicesVaultResponse",
    "ExtendedLocationResponse",
    "ExternalInstallationSoftwareConfigurationResponse",
    "GatewayServerPropertiesResponse",
    "HanaBackupDataResponse",
    "HanaDbProviderInstancePropertiesResponse",
    "HealthResponse",
    "HighAvailabilityConfigurationResponse",
    "HighAvailabilitySoftwareConfigurationResponse",
    "HourlyScheduleResponse",
    "ImageReferenceResponse",
    "InstantRPAdditionalDetailsResponse",
    "LinuxConfigurationResponse",
    "LoadBalancerDetailsResponse",
    "LoadBalancerResourceNamesResponse",
    "LogSchedulePolicyResponse",
    "LongTermRetentionPolicyResponse",
    "LongTermSchedulePolicyResponse",
    "ManagedRGConfigurationResponse",
    "ManagedResourceGroupConfigurationResponse",
    "ManagedServiceIdentityResponse",
    "MessageServerPropertiesResponse",
    "MonthlyRetentionScheduleResponse",
    "MountFileShareConfigurationResponse",
    "MsSqlServerProviderInstancePropertiesResponse",
    "NativePerformanceDataResponse",
    "NetworkConfigurationResponse",
    "NetworkInterfaceResourceNamesResponse",
    "NewRecoveryServicesVaultResponse",
    "OSProfileResponse",
    "OracleProviderInstancePropertiesResponse",
    "OsSapConfigurationResponse",
    ...,
    "PrometheusOsProviderInstancePropertiesResponse",
    "RetentionDurationResponse",
    "SAPAvailabilityZonePairResponse",
    "SAPDiskConfigurationResponse",
    ...,
    "SAPMigrateErrorResponse",
    "SAPMigrateErrorResponseV1",
    "SAPMigrateErrorResponseV2",
    "SAPSupportedSkuResponse",
    "SAPVirtualInstanceErrorResponse",
    "SAPVirtualInstanceIdentityResponse",
    "SSLConfigurationResponse",
    "SapLandscapeMonitorMetricThresholdsResponse",
    "SapLandscapeMonitorPropertiesGroupingResponse",
    "SapLandscapeMonitorSidMappingResponse",
    "SapNetWeaverProviderInstancePropertiesResponse",
    "ServiceInitiatedSoftwareConfigurationResponse",
    "SettingsResponse",
    "SharedStorageResourceNamesResponse",
    "SimpleRetentionPolicyResponse",
    "SimpleSchedulePolicyResponse",
    "SimpleSchedulePolicyV2Response",
    "SingleServerConfigurationResponse",
    "SingleServerFullResourceNamesResponse",
    "SkipFileShareConfigurationResponse",
    "SnapshotBackupAdditionalDetailsResponse",
    "SqlBackupDataResponse",
    "SshConfigurationResponse",
    "SshKeyPairResponse",
    "SshPublicKeyResponse",
    "StorageConfigurationResponse",
    "StorageInformationResponse",
    "SubProtectionPolicyResponse",
    "SystemDataResponse",
    "ThreeTierConfigurationResponse",
    "ThreeTierFullResourceNamesResponse",
    "TieringPolicyResponse",
    "UserAssignedIdentityPropertiesResponse",
    "UserAssignedIdentityResponse",
    "UserAssignedManagedIdentityDetailsResponse",
    "UserAssignedServiceIdentityResponse",
    "VMBackupDataResponse",
    "VMBackupPolicyPropertiesResponse",
    "VirtualMachineConfigurationResponse",
    "VirtualMachineResourceNamesResponse",
    "WeeklyRetentionFormatResponse",
    "WeeklyRetentionScheduleResponse",
    "WeeklyScheduleResponse",
    "WindowsConfigurationResponse",
    "YearlyRetentionScheduleResponse",
]

@pulumi.output_type
class AlertQueryParameterResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AlertRulePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_groups: Optional[Sequence[_builtins.str]] = ...,
        alert_query_parameters: Optional[
            Sequence[outputs.AlertQueryParameterResponse]
        ] = ...,
        auto_mitigate: Optional[_builtins.str] = ...,
        dimension: Optional[_builtins.str] = ...,
        evaluation_frequency: Optional[_builtins.int] = ...,
        failing_periods_operator: Optional[_builtins.str] = ...,
        failing_periods_to_alert: Optional[_builtins.int] = ...,
        mute_actions_duration: Optional[_builtins.int] = ...,
        severity: Optional[_builtins.int] = ...,
        status: Optional[_builtins.str] = ...,
        threshold: Optional[_builtins.int] = ...,
        threshold_operator: Optional[_builtins.str] = ...,
        window_size: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroups")
    def action_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="alertQueryParameters")
    def alert_query_parameters(
        self,
    ) -> Optional[Sequence[outputs.AlertQueryParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="autoMitigate")
    def auto_mitigate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="failingPeriodsOperator")
    def failing_periods_operator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failingPeriodsToAlert")
    def failing_periods_to_alert(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="muteActionsDuration")
    def mute_actions_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="thresholdOperator")
    def threshold_operator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AppServicePlanConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        capacity: Optional[_builtins.int] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationServerConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_count: _builtins.float,
        subnet_id: _builtins.str,
        virtual_machine_configuration: outputs.VirtualMachineConfigurationResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineConfiguration")
    def virtual_machine_configuration(
        self,
    ) -> outputs.VirtualMachineConfigurationResponse: ...

@pulumi.output_type
class ApplicationServerFullResourceNamesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_set_name: Optional[_builtins.str] = ...,
        virtual_machines: Optional[
            Sequence[outputs.VirtualMachineResourceNamesResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilitySetName")
    def availability_set_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(
        self,
    ) -> Optional[Sequence[outputs.VirtualMachineResourceNamesResponse]]: ...

@pulumi.output_type
class ApplicationServerVmDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_details: Sequence[outputs.StorageInformationResponse],
        type: _builtins.str,
        virtual_machine_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageDetails")
    def storage_details(self) -> Sequence[outputs.StorageInformationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> _builtins.str: ...

@pulumi.output_type
class CentralServerConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_count: _builtins.float,
        subnet_id: _builtins.str,
        virtual_machine_configuration: outputs.VirtualMachineConfigurationResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineConfiguration")
    def virtual_machine_configuration(
        self,
    ) -> outputs.VirtualMachineConfigurationResponse: ...

@pulumi.output_type
class CentralServerFullResourceNamesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_set_name: Optional[_builtins.str] = ...,
        load_balancer: Optional[outputs.LoadBalancerResourceNamesResponse] = ...,
        virtual_machines: Optional[
            Sequence[outputs.VirtualMachineResourceNamesResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilitySetName")
    def availability_set_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional[outputs.LoadBalancerResourceNamesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(
        self,
    ) -> Optional[Sequence[outputs.VirtualMachineResourceNamesResponse]]: ...

@pulumi.output_type
class CentralServerVmDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_details: Sequence[outputs.StorageInformationResponse],
        type: _builtins.str,
        virtual_machine_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageDetails")
    def storage_details(self) -> Sequence[outputs.StorageInformationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> _builtins.str: ...

@pulumi.output_type
class ConfigurationDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu: _builtins.int,
        cpu_in_mhz: _builtins.int,
        cpu_type: _builtins.str,
        database_type: _builtins.str,
        hardware_manufacturer: _builtins.str,
        model: _builtins.str,
        ram: _builtins.int,
        saps: _builtins.int,
        target_hana_ram_size_gb: _builtins.int,
        total_disk_iops: _builtins.int,
        total_disk_size_gb: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="cpuInMhz")
    def cpu_in_mhz(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="cpuType")
    def cpu_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hardwareManufacturer")
    def hardware_manufacturer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ram(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def saps(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="targetHanaRamSizeGB")
    def target_hana_ram_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalDiskIops")
    def total_disk_iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalDiskSizeGB")
    def total_disk_size_gb(self) -> _builtins.int: ...

@pulumi.output_type
class ConnectorErrorDefinitionResponse(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        details: Sequence[outputs.ConnectorErrorDefinitionResponse],
        message: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ConnectorErrorDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...

@pulumi.output_type
class CreateAndMountFileShareConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_type: _builtins.str,
        resource_group: Optional[_builtins.str] = ...,
        storage_account_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DBBackupPolicyPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backup_management_type: _builtins.str,
        name: _builtins.str,
        make_policy_consistent: Optional[_builtins.bool] = ...,
        protected_items_count: Optional[_builtins.int] = ...,
        resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ...,
        settings: Optional[outputs.SettingsResponse] = ...,
        sub_protection_policy: Optional[
            Sequence[outputs.SubProtectionPolicyResponse]
        ] = ...,
        work_load_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="makePolicyConsistent")
    def make_policy_consistent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.SettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="subProtectionPolicy")
    def sub_protection_policy(
        self,
    ) -> Optional[Sequence[outputs.SubProtectionPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="workLoadType")
    def work_load_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DailyRetentionFormatResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, days_of_the_month: Optional[Sequence[outputs.DayResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfTheMonth")
    def days_of_the_month(self) -> Optional[Sequence[outputs.DayResponse]]: ...

@pulumi.output_type
class DailyRetentionScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        retention_duration: Optional[outputs.RetentionDurationResponse] = ...,
        retention_times: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[outputs.RetentionDurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DailyScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, schedule_run_times: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DatabaseConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_count: _builtins.float,
        subnet_id: _builtins.str,
        virtual_machine_configuration: outputs.VirtualMachineConfigurationResponse,
        database_type: Optional[_builtins.str] = ...,
        disk_configuration: Optional[outputs.DiskConfigurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineConfiguration")
    def virtual_machine_configuration(
        self,
    ) -> outputs.VirtualMachineConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskConfiguration")
    def disk_configuration(self) -> Optional[outputs.DiskConfigurationResponse]: ...

@pulumi.output_type
class DatabaseServerFullResourceNamesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_set_name: Optional[_builtins.str] = ...,
        load_balancer: Optional[outputs.LoadBalancerResourceNamesResponse] = ...,
        virtual_machines: Optional[
            Sequence[outputs.VirtualMachineResourceNamesResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilitySetName")
    def availability_set_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional[outputs.LoadBalancerResourceNamesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(
        self,
    ) -> Optional[Sequence[outputs.VirtualMachineResourceNamesResponse]]: ...

@pulumi.output_type
class DatabaseVmDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        status: _builtins.str,
        storage_details: Sequence[outputs.StorageInformationResponse],
        virtual_machine_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageDetails")
    def storage_details(self) -> Sequence[outputs.StorageInformationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> _builtins.str: ...

@pulumi.output_type
class DayResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        date: Optional[_builtins.int] = ...,
        is_last: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="isLast")
    def is_last(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class Db2ProviderInstancePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provider_type: _builtins.str,
        db_name: Optional[_builtins.str] = ...,
        db_password: Optional[_builtins.str] = ...,
        db_password_uri: Optional[_builtins.str] = ...,
        db_port: Optional[_builtins.str] = ...,
        db_username: Optional[_builtins.str] = ...,
        hostname: Optional[_builtins.str] = ...,
        sap_sid: Optional[_builtins.str] = ...,
        ssl_certificate_uri: Optional[_builtins.str] = ...,
        ssl_preference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPassword")
    def db_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPasswordUri")
    def db_password_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPort")
    def db_port(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbUsername")
    def db_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapSid")
    def sap_sid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificateUri")
    def ssl_certificate_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslPreference")
    def ssl_preference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeployerVmPackagesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_account_id: Optional[_builtins.str] = ...,
        url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_type: _builtins.str,
        app_location: Optional[_builtins.str] = ...,
        infrastructure_configuration: Optional[Any] = ...,
        software_configuration: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="appLocation")
    def app_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureConfiguration")
    def infrastructure_configuration(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="softwareConfiguration")
    def software_configuration(self) -> Optional[Any]: ...

@pulumi.output_type
class DeploymentWithOSConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_type: _builtins.str,
        app_location: Optional[_builtins.str] = ...,
        infrastructure_configuration: Optional[Any] = ...,
        os_sap_configuration: Optional[outputs.OsSapConfigurationResponse] = ...,
        software_configuration: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="appLocation")
    def app_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureConfiguration")
    def infrastructure_configuration(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="osSapConfiguration")
    def os_sap_configuration(self) -> Optional[outputs.OsSapConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="softwareConfiguration")
    def software_configuration(self) -> Optional[Any]: ...

@pulumi.output_type
class DiscoveryConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_location: _builtins.str,
        configuration_type: _builtins.str,
        central_server_vm_id: Optional[_builtins.str] = ...,
        managed_rg_storage_account_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appLocation")
    def app_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="centralServerVmId")
    def central_server_vm_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedRgStorageAccountName")
    def managed_rg_storage_account_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DiskConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_volume_configurations: Optional[
            Mapping[str, outputs.DiskVolumeConfigurationResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskVolumeConfigurations")
    def disk_volume_configurations(
        self,
    ) -> Optional[Mapping[str, outputs.DiskVolumeConfigurationResponse]]: ...

@pulumi.output_type
class DiskDetailsResponse(dict):
    def __init__(
        __self__,
        *,
        disk_tier: Optional[_builtins.str] = ...,
        iops_read_write: Optional[_builtins.float] = ...,
        maximum_supported_disk_count: Optional[_builtins.float] = ...,
        mbps_read_write: Optional[_builtins.float] = ...,
        minimum_supported_disk_count: Optional[_builtins.float] = ...,
        size_gb: Optional[_builtins.float] = ...,
        sku: Optional[outputs.DiskSkuResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskTier")
    def disk_tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iopsReadWrite")
    def iops_read_write(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="maximumSupportedDiskCount")
    def maximum_supported_disk_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="mbpsReadWrite")
    def mbps_read_write(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="minimumSupportedDiskCount")
    def minimum_supported_disk_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="sizeGB")
    def size_gb(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.DiskSkuResponse]: ...

@pulumi.output_type
class DiskExclusionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_lun_list: Sequence[_builtins.int],
        is_inclusion_list: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskLunList")
    def disk_lun_list(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="isInclusionList")
    def is_inclusion_list(self) -> _builtins.bool: ...

@pulumi.output_type
class DiskSkuResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DiskVolumeConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: Optional[_builtins.float] = ...,
        size_gb: Optional[_builtins.float] = ...,
        sku: Optional[outputs.DiskSkuResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="sizeGB")
    def size_gb(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.DiskSkuResponse]: ...

@pulumi.output_type
class EnqueueReplicationServerPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ers_version: _builtins.str,
        health: _builtins.str,
        hostname: _builtins.str,
        instance_no: _builtins.str,
        ip_address: _builtins.str,
        kernel_patch: _builtins.str,
        kernel_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ersVersion")
    def ers_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceNo")
    def instance_no(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kernelPatch")
    def kernel_patch(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kernelVersion")
    def kernel_version(self) -> _builtins.str: ...

@pulumi.output_type
class EnqueueServerPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        health: _builtins.str,
        hostname: _builtins.str,
        ip_address: _builtins.str,
        port: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.float: ...

@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorDefinitionResponse(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        details: Sequence[outputs.ErrorDefinitionResponse],
        message: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorDefinitionResponseV1(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        details: Sequence[outputs.ErrorDefinitionResponse],
        message: _builtins.str,
        recommendation: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorDefinitionResponseV2(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        details: Sequence[outputs.ErrorDefinitionResponse],
        message: _builtins.str,
        recommendation: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorDefinitionResponseV3(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        details: Sequence[outputs.ErrorDefinitionResponse],
        message: _builtins.str,
        recommendation: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorDetailResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_info: Sequence[outputs.ErrorAdditionalInfoResponse],
        code: _builtins.str,
        details: Sequence[outputs.ErrorDetailResponse],
        message: _builtins.str,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class ExcelPerformanceDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source: _builtins.str,
        max_cpu_load: _builtins.int,
        total_source_db_size_gb: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxCpuLoad")
    def max_cpu_load(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalSourceDbSizeGB")
    def total_source_db_size_gb(self) -> _builtins.int: ...

@pulumi.output_type
class ExistingRecoveryServicesVaultResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, id: _builtins.str, vault_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vaultType")
    def vault_type(self) -> _builtins.str: ...

@pulumi.output_type
class ExtendedLocationResponse(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ExternalInstallationSoftwareConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        software_installation_type: _builtins.str,
        central_server_vm_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="softwareInstallationType")
    def software_installation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="centralServerVmId")
    def central_server_vm_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayServerPropertiesResponse(dict):
    def __init__(__self__, *, health: _builtins.str, port: _builtins.float) -> None: ...
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.float: ...

@pulumi.output_type
class HanaBackupDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backup_policy: outputs.DBBackupPolicyPropertiesResponse,
        backup_type: _builtins.str,
        hdbuserstore_key_name: _builtins.str,
        recovery_services_vault: Any,
        db_instance_snapshot_backup_policy: Optional[
            outputs.DBBackupPolicyPropertiesResponse
        ] = ...,
        instance_number: Optional[_builtins.str] = ...,
        ssl_configuration: Optional[outputs.SSLConfigurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> outputs.DBBackupPolicyPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hdbuserstoreKeyName")
    def hdbuserstore_key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recoveryServicesVault")
    def recovery_services_vault(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceSnapshotBackupPolicy")
    def db_instance_snapshot_backup_policy(
        self,
    ) -> Optional[outputs.DBBackupPolicyPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="instanceNumber")
    def instance_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslConfiguration")
    def ssl_configuration(self) -> Optional[outputs.SSLConfigurationResponse]: ...

@pulumi.output_type
class HanaDbProviderInstancePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provider_type: _builtins.str,
        db_name: Optional[_builtins.str] = ...,
        db_password: Optional[_builtins.str] = ...,
        db_password_uri: Optional[_builtins.str] = ...,
        db_username: Optional[_builtins.str] = ...,
        hostname: Optional[_builtins.str] = ...,
        instance_number: Optional[_builtins.str] = ...,
        sap_sid: Optional[_builtins.str] = ...,
        sql_port: Optional[_builtins.str] = ...,
        ssl_certificate_uri: Optional[_builtins.str] = ...,
        ssl_host_name_in_certificate: Optional[_builtins.str] = ...,
        ssl_preference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPassword")
    def db_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPasswordUri")
    def db_password_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbUsername")
    def db_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceNumber")
    def instance_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapSid")
    def sap_sid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlPort")
    def sql_port(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificateUri")
    def ssl_certificate_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslHostNameInCertificate")
    def ssl_host_name_in_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslPreference")
    def ssl_preference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HealthResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, health_state: _builtins.str, impacting_reasons: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthState")
    def health_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="impactingReasons")
    def impacting_reasons(self) -> _builtins.str: ...

@pulumi.output_type
class HighAvailabilityConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, high_availability_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="highAvailabilityType")
    def high_availability_type(self) -> _builtins.str: ...

@pulumi.output_type
class HighAvailabilitySoftwareConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fencing_client_id: _builtins.str,
        fencing_client_password: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fencingClientId")
    def fencing_client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fencingClientPassword")
    def fencing_client_password(self) -> _builtins.str: ...

@pulumi.output_type
class HourlyScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interval: Optional[_builtins.int] = ...,
        schedule_window_duration: Optional[_builtins.int] = ...,
        schedule_window_start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleWindowDuration")
    def schedule_window_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleWindowStartTime")
    def schedule_window_start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageReferenceResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        offer: Optional[_builtins.str] = ...,
        publisher: Optional[_builtins.str] = ...,
        sku: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstantRPAdditionalDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_backup_rg_name_prefix: Optional[_builtins.str] = ...,
        azure_backup_rg_name_suffix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureBackupRGNamePrefix")
    def azure_backup_rg_name_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureBackupRGNameSuffix")
    def azure_backup_rg_name_suffix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LinuxConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_type: _builtins.str,
        disable_password_authentication: Optional[_builtins.bool] = ...,
        ssh: Optional[outputs.SshConfigurationResponse] = ...,
        ssh_key_pair: Optional[outputs.SshKeyPairResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disablePasswordAuthentication")
    def disable_password_authentication(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssh(self) -> Optional[outputs.SshConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sshKeyPair")
    def ssh_key_pair(self) -> Optional[outputs.SshKeyPairResponse]: ...

@pulumi.output_type
class LoadBalancerDetailsResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class LoadBalancerResourceNamesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backend_pool_names: Optional[Sequence[_builtins.str]] = ...,
        frontend_ip_configuration_names: Optional[Sequence[_builtins.str]] = ...,
        health_probe_names: Optional[Sequence[_builtins.str]] = ...,
        load_balancer_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendPoolNames")
    def backend_pool_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="frontendIpConfigurationNames")
    def frontend_ip_configuration_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="healthProbeNames")
    def health_probe_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogSchedulePolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schedule_policy_type: _builtins.str,
        schedule_frequency_in_mins: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduleFrequencyInMins")
    def schedule_frequency_in_mins(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class LongTermRetentionPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        retention_policy_type: _builtins.str,
        daily_schedule: Optional[outputs.DailyRetentionScheduleResponse] = ...,
        monthly_schedule: Optional[outputs.MonthlyRetentionScheduleResponse] = ...,
        weekly_schedule: Optional[outputs.WeeklyRetentionScheduleResponse] = ...,
        yearly_schedule: Optional[outputs.YearlyRetentionScheduleResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicyType")
    def retention_policy_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[outputs.DailyRetentionScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(
        self,
    ) -> Optional[outputs.MonthlyRetentionScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[outputs.WeeklyRetentionScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="yearlySchedule")
    def yearly_schedule(self) -> Optional[outputs.YearlyRetentionScheduleResponse]: ...

@pulumi.output_type
class LongTermSchedulePolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, schedule_policy_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> _builtins.str: ...

@pulumi.output_type
class ManagedRGConfigurationResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagedResourceGroupConfigurationResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
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
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class MessageServerPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        health: _builtins.str,
        hostname: _builtins.str,
        http_port: _builtins.float,
        https_port: _builtins.float,
        internal_ms_port: _builtins.float,
        ip_address: _builtins.str,
        ms_port: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="internalMsPort")
    def internal_ms_port(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="msPort")
    def ms_port(self) -> _builtins.float: ...

@pulumi.output_type
class MonthlyRetentionScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        retention_duration: Optional[outputs.RetentionDurationResponse] = ...,
        retention_schedule_daily: Optional[outputs.DailyRetentionFormatResponse] = ...,
        retention_schedule_format_type: Optional[_builtins.str] = ...,
        retention_schedule_weekly: Optional[
            outputs.WeeklyRetentionFormatResponse
        ] = ...,
        retention_times: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[outputs.RetentionDurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleDaily")
    def retention_schedule_daily(
        self,
    ) -> Optional[outputs.DailyRetentionFormatResponse]: ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleFormatType")
    def retention_schedule_format_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleWeekly")
    def retention_schedule_weekly(
        self,
    ) -> Optional[outputs.WeeklyRetentionFormatResponse]: ...
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MountFileShareConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_type: _builtins.str,
        id: _builtins.str,
        private_endpoint_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointId")
    def private_endpoint_id(self) -> _builtins.str: ...

@pulumi.output_type
class MsSqlServerProviderInstancePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provider_type: _builtins.str,
        db_password: Optional[_builtins.str] = ...,
        db_password_uri: Optional[_builtins.str] = ...,
        db_port: Optional[_builtins.str] = ...,
        db_username: Optional[_builtins.str] = ...,
        hostname: Optional[_builtins.str] = ...,
        sap_sid: Optional[_builtins.str] = ...,
        ssl_certificate_uri: Optional[_builtins.str] = ...,
        ssl_preference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbPassword")
    def db_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPasswordUri")
    def db_password_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPort")
    def db_port(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbUsername")
    def db_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapSid")
    def sap_sid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificateUri")
    def ssl_certificate_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslPreference")
    def ssl_preference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NativePerformanceDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, data_source: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...

@pulumi.output_type
class NetworkConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, is_secondary_ip_enabled: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isSecondaryIpEnabled")
    def is_secondary_ip_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class NetworkInterfaceResourceNamesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, network_interface_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceName")
    def network_interface_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NewRecoveryServicesVaultResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        resource_group: _builtins.str,
        vault_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vaultType")
    def vault_type(self) -> _builtins.str: ...

@pulumi.output_type
class OSProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_password: Optional[_builtins.str] = ...,
        admin_username: Optional[_builtins.str] = ...,
        os_configuration: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osConfiguration")
    def os_configuration(self) -> Optional[Any]: ...

@pulumi.output_type
class OracleProviderInstancePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provider_type: _builtins.str,
        db_name: Optional[_builtins.str] = ...,
        db_password: Optional[_builtins.str] = ...,
        db_password_uri: Optional[_builtins.str] = ...,
        db_port: Optional[_builtins.str] = ...,
        db_username: Optional[_builtins.str] = ...,
        hostname: Optional[_builtins.str] = ...,
        sap_sid: Optional[_builtins.str] = ...,
        ssl_certificate_uri: Optional[_builtins.str] = ...,
        ssl_preference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPassword")
    def db_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPasswordUri")
    def db_password_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPort")
    def db_port(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbUsername")
    def db_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapSid")
    def sap_sid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificateUri")
    def ssl_certificate_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslPreference")
    def ssl_preference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsSapConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deployer_vm_packages: Optional[outputs.DeployerVmPackagesResponse] = ...,
        sap_fqdn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deployerVmPackages")
    def deployer_vm_packages(self) -> Optional[outputs.DeployerVmPackagesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sapFqdn")
    def sap_fqdn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrometheusHaClusterProviderInstancePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provider_type: _builtins.str,
        cluster_name: Optional[_builtins.str] = ...,
        hostname: Optional[_builtins.str] = ...,
        prometheus_url: Optional[_builtins.str] = ...,
        sid: Optional[_builtins.str] = ...,
        ssl_certificate_uri: Optional[_builtins.str] = ...,
        ssl_preference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="prometheusUrl")
    def prometheus_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificateUri")
    def ssl_certificate_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslPreference")
    def ssl_preference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrometheusOsProviderInstancePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provider_type: _builtins.str,
        prometheus_url: Optional[_builtins.str] = ...,
        sap_sid: Optional[_builtins.str] = ...,
        ssl_certificate_uri: Optional[_builtins.str] = ...,
        ssl_preference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="prometheusUrl")
    def prometheus_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapSid")
    def sap_sid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificateUri")
    def ssl_certificate_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslPreference")
    def ssl_preference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RetentionDurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: Optional[_builtins.int] = ...,
        duration_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="durationType")
    def duration_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SAPAvailabilityZonePairResponse(dict):
    def __init__(
        __self__,
        *,
        zone_a: Optional[_builtins.float] = ...,
        zone_b: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="zoneA")
    def zone_a(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="zoneB")
    def zone_b(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class SAPDiskConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        recommended_configuration: Optional[
            outputs.DiskVolumeConfigurationResponse
        ] = ...,
        supported_configurations: Optional[Sequence[outputs.DiskDetailsResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recommendedConfiguration")
    def recommended_configuration(
        self,
    ) -> Optional[outputs.DiskVolumeConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="supportedConfigurations")
    def supported_configurations(
        self,
    ) -> Optional[Sequence[outputs.DiskDetailsResponse]]: ...

@pulumi.output_type
class SAPInstallWithoutOSConfigSoftwareConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bom_url: _builtins.str,
        sap_bits_storage_account_id: _builtins.str,
        software_installation_type: _builtins.str,
        software_version: _builtins.str,
        high_availability_software_configuration: Optional[
            outputs.HighAvailabilitySoftwareConfigurationResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bomUrl")
    def bom_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sapBitsStorageAccountId")
    def sap_bits_storage_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="softwareInstallationType")
    def software_installation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="softwareVersion")
    def software_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="highAvailabilitySoftwareConfiguration")
    def high_availability_software_configuration(
        self,
    ) -> Optional[outputs.HighAvailabilitySoftwareConfigurationResponse]: ...

@pulumi.output_type
class SAPMigrateErrorResponse(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        details: Sequence[outputs.ErrorDefinitionResponseV1],
        message: _builtins.str,
        recommendation: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDefinitionResponseV1]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...

@pulumi.output_type
class SAPMigrateErrorResponseV1(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        details: Sequence[outputs.ErrorDefinitionResponseV2],
        message: _builtins.str,
        recommendation: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDefinitionResponseV2]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...

@pulumi.output_type
class SAPMigrateErrorResponseV2(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        details: Sequence[outputs.ErrorDefinitionResponseV3],
        message: _builtins.str,
        recommendation: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDefinitionResponseV3]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...

@pulumi.output_type
class SAPSupportedSkuResponse(dict):
    def __init__(
        __self__,
        *,
        is_app_server_certified: Optional[_builtins.bool] = ...,
        is_database_certified: Optional[_builtins.bool] = ...,
        vm_sku: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isAppServerCertified")
    def is_app_server_certified(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isDatabaseCertified")
    def is_database_certified(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="vmSku")
    def vm_sku(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SAPVirtualInstanceErrorResponse(dict):
    def __init__(
        __self__, *, properties: Optional[outputs.ErrorDefinitionResponse] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.ErrorDefinitionResponse]: ...

@pulumi.output_type
class SAPVirtualInstanceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class SSLConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ssl_crypto_provider: Optional[_builtins.str] = ...,
        ssl_host_name_in_certificate: Optional[_builtins.str] = ...,
        ssl_key_store: Optional[_builtins.str] = ...,
        ssl_trust_store: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sslCryptoProvider")
    def ssl_crypto_provider(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslHostNameInCertificate")
    def ssl_host_name_in_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslKeyStore")
    def ssl_key_store(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslTrustStore")
    def ssl_trust_store(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SapLandscapeMonitorMetricThresholdsResponse(dict):
    def __init__(
        __self__,
        *,
        green: Optional[_builtins.float] = ...,
        name: Optional[_builtins.str] = ...,
        red: Optional[_builtins.float] = ...,
        yellow: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def green(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def red(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def yellow(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class SapLandscapeMonitorPropertiesGroupingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        landscape: Optional[
            Sequence[outputs.SapLandscapeMonitorSidMappingResponse]
        ] = ...,
        sap_application: Optional[
            Sequence[outputs.SapLandscapeMonitorSidMappingResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def landscape(
        self,
    ) -> Optional[Sequence[outputs.SapLandscapeMonitorSidMappingResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sapApplication")
    def sap_application(
        self,
    ) -> Optional[Sequence[outputs.SapLandscapeMonitorSidMappingResponse]]: ...

@pulumi.output_type
class SapLandscapeMonitorSidMappingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        top_sid: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="topSid")
    def top_sid(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SapNetWeaverProviderInstancePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provider_type: _builtins.str,
        sap_client_id: Optional[_builtins.str] = ...,
        sap_host_file_entries: Optional[Sequence[_builtins.str]] = ...,
        sap_hostname: Optional[_builtins.str] = ...,
        sap_instance_nr: Optional[_builtins.str] = ...,
        sap_password: Optional[_builtins.str] = ...,
        sap_password_uri: Optional[_builtins.str] = ...,
        sap_port_number: Optional[_builtins.str] = ...,
        sap_sid: Optional[_builtins.str] = ...,
        sap_username: Optional[_builtins.str] = ...,
        ssl_certificate_uri: Optional[_builtins.str] = ...,
        ssl_preference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sapClientId")
    def sap_client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapHostFileEntries")
    def sap_host_file_entries(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sapHostname")
    def sap_hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapInstanceNr")
    def sap_instance_nr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapPassword")
    def sap_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapPasswordUri")
    def sap_password_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapPortNumber")
    def sap_port_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapSid")
    def sap_sid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapUsername")
    def sap_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificateUri")
    def ssl_certificate_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslPreference")
    def ssl_preference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceInitiatedSoftwareConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bom_url: _builtins.str,
        sap_bits_storage_account_id: _builtins.str,
        sap_fqdn: _builtins.str,
        software_installation_type: _builtins.str,
        software_version: _builtins.str,
        ssh_private_key: _builtins.str,
        high_availability_software_configuration: Optional[
            outputs.HighAvailabilitySoftwareConfigurationResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bomUrl")
    def bom_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sapBitsStorageAccountId")
    def sap_bits_storage_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sapFqdn")
    def sap_fqdn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="softwareInstallationType")
    def software_installation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="softwareVersion")
    def software_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sshPrivateKey")
    def ssh_private_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="highAvailabilitySoftwareConfiguration")
    def high_availability_software_configuration(
        self,
    ) -> Optional[outputs.HighAvailabilitySoftwareConfigurationResponse]: ...

@pulumi.output_type
class SettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_compression: Optional[_builtins.bool] = ...,
        issqlcompression: Optional[_builtins.bool] = ...,
        time_zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCompression")
    def is_compression(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def issqlcompression(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SharedStorageResourceNamesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        shared_storage_account_name: Optional[_builtins.str] = ...,
        shared_storage_account_private_end_point_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sharedStorageAccountName")
    def shared_storage_account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedStorageAccountPrivateEndPointName")
    def shared_storage_account_private_end_point_name(
        self,
    ) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SimpleRetentionPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        retention_policy_type: _builtins.str,
        retention_duration: Optional[outputs.RetentionDurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicyType")
    def retention_policy_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[outputs.RetentionDurationResponse]: ...

@pulumi.output_type
class SimpleSchedulePolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schedule_policy_type: _builtins.str,
        hourly_schedule: Optional[outputs.HourlyScheduleResponse] = ...,
        schedule_run_days: Optional[Sequence[_builtins.str]] = ...,
        schedule_run_frequency: Optional[_builtins.str] = ...,
        schedule_run_times: Optional[Sequence[_builtins.str]] = ...,
        schedule_weekly_frequency: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[outputs.HourlyScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunDays")
    def schedule_run_days(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunFrequency")
    def schedule_run_frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleWeeklyFrequency")
    def schedule_weekly_frequency(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SimpleSchedulePolicyV2Response(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schedule_policy_type: _builtins.str,
        daily_schedule: Optional[outputs.DailyScheduleResponse] = ...,
        hourly_schedule: Optional[outputs.HourlyScheduleResponse] = ...,
        schedule_run_frequency: Optional[_builtins.str] = ...,
        weekly_schedule: Optional[outputs.WeeklyScheduleResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[outputs.DailyScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[outputs.HourlyScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunFrequency")
    def schedule_run_frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[outputs.WeeklyScheduleResponse]: ...

@pulumi.output_type
class SingleServerConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_resource_group: _builtins.str,
        deployment_type: _builtins.str,
        subnet_id: _builtins.str,
        virtual_machine_configuration: outputs.VirtualMachineConfigurationResponse,
        custom_resource_names: Optional[
            outputs.SingleServerFullResourceNamesResponse
        ] = ...,
        database_type: Optional[_builtins.str] = ...,
        db_disk_configuration: Optional[outputs.DiskConfigurationResponse] = ...,
        network_configuration: Optional[outputs.NetworkConfigurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appResourceGroup")
    def app_resource_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineConfiguration")
    def virtual_machine_configuration(
        self,
    ) -> outputs.VirtualMachineConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="customResourceNames")
    def custom_resource_names(
        self,
    ) -> Optional[outputs.SingleServerFullResourceNamesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbDiskConfiguration")
    def db_disk_configuration(self) -> Optional[outputs.DiskConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[outputs.NetworkConfigurationResponse]: ...

@pulumi.output_type
class SingleServerFullResourceNamesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        naming_pattern_type: _builtins.str,
        virtual_machine: Optional[outputs.VirtualMachineResourceNamesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namingPatternType")
    def naming_pattern_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(
        self,
    ) -> Optional[outputs.VirtualMachineResourceNamesResponse]: ...

@pulumi.output_type
class SkipFileShareConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, configuration_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str: ...

@pulumi.output_type
class SnapshotBackupAdditionalDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instant_rp_details: Optional[_builtins.str] = ...,
        instant_rp_retention_range_in_days: Optional[_builtins.int] = ...,
        user_assigned_managed_identity_details: Optional[
            outputs.UserAssignedManagedIdentityDetailsResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instantRPDetails")
    def instant_rp_details(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instantRpRetentionRangeInDays")
    def instant_rp_retention_range_in_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedManagedIdentityDetails")
    def user_assigned_managed_identity_details(
        self,
    ) -> Optional[outputs.UserAssignedManagedIdentityDetailsResponse]: ...

@pulumi.output_type
class SqlBackupDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backup_policy: outputs.DBBackupPolicyPropertiesResponse,
        backup_type: _builtins.str,
        recovery_services_vault: Any,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> outputs.DBBackupPolicyPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recoveryServicesVault")
    def recovery_services_vault(self) -> Any: ...

@pulumi.output_type
class SshConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, public_keys: Optional[Sequence[outputs.SshPublicKeyResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Optional[Sequence[outputs.SshPublicKeyResponse]]: ...

@pulumi.output_type
class SshKeyPairResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_key: Optional[_builtins.str] = ...,
        public_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SshPublicKeyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_data: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, transport_file_share_configuration: Optional[Any] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transportFileShareConfiguration")
    def transport_file_share_configuration(self) -> Optional[Any]: ...

@pulumi.output_type
class StorageInformationResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class SubProtectionPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        policy_type: Optional[_builtins.str] = ...,
        retention_policy: Optional[Any] = ...,
        schedule_policy: Optional[Any] = ...,
        snapshot_backup_additional_details: Optional[
            outputs.SnapshotBackupAdditionalDetailsResponse
        ] = ...,
        tiering_policy: Optional[Mapping[str, outputs.TieringPolicyResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotBackupAdditionalDetails")
    def snapshot_backup_additional_details(
        self,
    ) -> Optional[outputs.SnapshotBackupAdditionalDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(
        self,
    ) -> Optional[Mapping[str, outputs.TieringPolicyResponse]]: ...

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
class ThreeTierConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_resource_group: _builtins.str,
        application_server: outputs.ApplicationServerConfigurationResponse,
        central_server: outputs.CentralServerConfigurationResponse,
        database_server: outputs.DatabaseConfigurationResponse,
        deployment_type: _builtins.str,
        custom_resource_names: Optional[
            outputs.ThreeTierFullResourceNamesResponse
        ] = ...,
        high_availability_config: Optional[
            outputs.HighAvailabilityConfigurationResponse
        ] = ...,
        network_configuration: Optional[outputs.NetworkConfigurationResponse] = ...,
        storage_configuration: Optional[outputs.StorageConfigurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appResourceGroup")
    def app_resource_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationServer")
    def application_server(self) -> outputs.ApplicationServerConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="centralServer")
    def central_server(self) -> outputs.CentralServerConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="databaseServer")
    def database_server(self) -> outputs.DatabaseConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customResourceNames")
    def custom_resource_names(
        self,
    ) -> Optional[outputs.ThreeTierFullResourceNamesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="highAvailabilityConfig")
    def high_availability_config(
        self,
    ) -> Optional[outputs.HighAvailabilityConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[outputs.NetworkConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(
        self,
    ) -> Optional[outputs.StorageConfigurationResponse]: ...

@pulumi.output_type
class ThreeTierFullResourceNamesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        naming_pattern_type: _builtins.str,
        application_server: Optional[
            outputs.ApplicationServerFullResourceNamesResponse
        ] = ...,
        central_server: Optional[outputs.CentralServerFullResourceNamesResponse] = ...,
        database_server: Optional[
            outputs.DatabaseServerFullResourceNamesResponse
        ] = ...,
        shared_storage: Optional[outputs.SharedStorageResourceNamesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namingPatternType")
    def naming_pattern_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationServer")
    def application_server(
        self,
    ) -> Optional[outputs.ApplicationServerFullResourceNamesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="centralServer")
    def central_server(
        self,
    ) -> Optional[outputs.CentralServerFullResourceNamesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="databaseServer")
    def database_server(
        self,
    ) -> Optional[outputs.DatabaseServerFullResourceNamesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sharedStorage")
    def shared_storage(
        self,
    ) -> Optional[outputs.SharedStorageResourceNamesResponse]: ...

@pulumi.output_type
class TieringPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        duration: Optional[_builtins.int] = ...,
        duration_type: Optional[_builtins.str] = ...,
        tiering_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="durationType")
    def duration_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tieringMode")
    def tiering_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAssignedIdentityPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        principal_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

@pulumi.output_type
class UserAssignedManagedIdentityDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identity_arm_id: Optional[_builtins.str] = ...,
        identity_name: Optional[_builtins.str] = ...,
        user_assigned_identity_properties: Optional[
            outputs.UserAssignedIdentityPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityArmId")
    def identity_arm_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="identityName")
    def identity_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityProperties")
    def user_assigned_identity_properties(
        self,
    ) -> Optional[outputs.UserAssignedIdentityPropertiesResponse]: ...

@pulumi.output_type
class UserAssignedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class VMBackupDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backup_policy: outputs.VMBackupPolicyPropertiesResponse,
        backup_type: _builtins.str,
        recovery_services_vault: Any,
        disk_exclusion_properties: Optional[
            outputs.DiskExclusionPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> outputs.VMBackupPolicyPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recoveryServicesVault")
    def recovery_services_vault(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="diskExclusionProperties")
    def disk_exclusion_properties(
        self,
    ) -> Optional[outputs.DiskExclusionPropertiesResponse]: ...

@pulumi.output_type
class VMBackupPolicyPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backup_management_type: _builtins.str,
        name: _builtins.str,
        instant_rp_details: Optional[outputs.InstantRPAdditionalDetailsResponse] = ...,
        instant_rp_retention_range_in_days: Optional[_builtins.int] = ...,
        policy_type: Optional[_builtins.str] = ...,
        protected_items_count: Optional[_builtins.int] = ...,
        resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ...,
        retention_policy: Optional[Any] = ...,
        schedule_policy: Optional[Any] = ...,
        tiering_policy: Optional[Mapping[str, outputs.TieringPolicyResponse]] = ...,
        time_zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instantRPDetails")
    def instant_rp_details(
        self,
    ) -> Optional[outputs.InstantRPAdditionalDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="instantRpRetentionRangeInDays")
    def instant_rp_retention_range_in_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(
        self,
    ) -> Optional[Mapping[str, outputs.TieringPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualMachineConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_reference: outputs.ImageReferenceResponse,
        os_profile: outputs.OSProfileResponse,
        vm_size: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> outputs.ImageReferenceResponse: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> outputs.OSProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualMachineResourceNamesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_disk_names: Optional[Mapping[str, Sequence[_builtins.str]]] = ...,
        host_name: Optional[_builtins.str] = ...,
        network_interfaces: Optional[
            Sequence[outputs.NetworkInterfaceResourceNamesResponse]
        ] = ...,
        os_disk_name: Optional[_builtins.str] = ...,
        vm_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskNames")
    def data_disk_names(self) -> Optional[Mapping[str, Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[Sequence[outputs.NetworkInterfaceResourceNamesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="osDiskName")
    def os_disk_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmName")
    def vm_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WeeklyRetentionFormatResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        days_of_the_week: Optional[Sequence[_builtins.str]] = ...,
        weeks_of_the_month: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfTheWeek")
    def days_of_the_week(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="weeksOfTheMonth")
    def weeks_of_the_month(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class WeeklyRetentionScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        days_of_the_week: Optional[Sequence[_builtins.str]] = ...,
        retention_duration: Optional[outputs.RetentionDurationResponse] = ...,
        retention_times: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfTheWeek")
    def days_of_the_week(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[outputs.RetentionDurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class WeeklyScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schedule_run_days: Optional[Sequence[_builtins.str]] = ...,
        schedule_run_times: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunDays")
    def schedule_run_days(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class WindowsConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, os_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str: ...

@pulumi.output_type
class YearlyRetentionScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        months_of_year: Optional[Sequence[_builtins.str]] = ...,
        retention_duration: Optional[outputs.RetentionDurationResponse] = ...,
        retention_schedule_daily: Optional[outputs.DailyRetentionFormatResponse] = ...,
        retention_schedule_format_type: Optional[_builtins.str] = ...,
        retention_schedule_weekly: Optional[
            outputs.WeeklyRetentionFormatResponse
        ] = ...,
        retention_times: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monthsOfYear")
    def months_of_year(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[outputs.RetentionDurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleDaily")
    def retention_schedule_daily(
        self,
    ) -> Optional[outputs.DailyRetentionFormatResponse]: ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleFormatType")
    def retention_schedule_format_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleWeekly")
    def retention_schedule_weekly(
        self,
    ) -> Optional[outputs.WeeklyRetentionFormatResponse]: ...
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[Sequence[_builtins.str]]: ...
