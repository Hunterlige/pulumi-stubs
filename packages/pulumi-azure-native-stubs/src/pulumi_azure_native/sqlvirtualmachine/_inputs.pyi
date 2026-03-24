

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AADAuthenticationSettingsArgs', 'AADAuthenticationSettingsArgsDict', 'AdditionalFeaturesServerConfigurationsArgs', 'AdditionalFeaturesServerConfigurationsArgsDict', 'AgConfigurationArgs', 'AgConfigurationArgsDict', 'AgReplicaArgs', 'AgReplicaArgsDict', 'AssessmentSettingsArgs', 'AssessmentSettingsArgsDict', 'AutoBackupSettingsArgs', 'AutoBackupSettingsArgsDict', 'AutoPatchingSettingsArgs', 'AutoPatchingSettingsArgsDict', 'KeyVaultCredentialSettingsArgs', 'KeyVaultCredentialSettingsArgsDict', 'LoadBalancerConfigurationArgs', 'LoadBalancerConfigurationArgsDict', 'MultiSubnetIpConfigurationArgs', 'MultiSubnetIpConfigurationArgsDict', 'PrivateIPAddressArgs', 'PrivateIPAddressArgsDict', 'ResourceIdentityArgs', 'ResourceIdentityArgsDict', 'SQLInstanceSettingsArgs', 'SQLInstanceSettingsArgsDict', 'SQLStorageSettingsArgs', 'SQLStorageSettingsArgsDict', 'SQLTempDbSettingsArgs', 'SQLTempDbSettingsArgsDict', 'ScheduleArgs', 'ScheduleArgsDict', 'ServerConfigurationsManagementSettingsArgs', 'ServerConfigurationsManagementSettingsArgsDict', 'SqlConnectivityUpdateSettingsArgs', 'SqlConnectivityUpdateSettingsArgsDict', 'SqlStorageUpdateSettingsArgs', 'SqlStorageUpdateSettingsArgsDict', 'SqlWorkloadTypeUpdateSettingsArgs', 'SqlWorkloadTypeUpdateSettingsArgsDict', 'StorageConfigurationSettingsArgs', 'StorageConfigurationSettingsArgsDict', 'VirtualMachineIdentityArgs', 'VirtualMachineIdentityArgsDict', 'WsfcDomainCredentialsArgs', 'WsfcDomainCredentialsArgsDict', 'WsfcDomainProfileArgs', 'WsfcDomainProfileArgsDict']
class AADAuthenticationSettingsArgsDict(TypedDict):
    
    client_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AADAuthenticationSettingsArgs:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AdditionalFeaturesServerConfigurationsArgsDict(TypedDict):
    
    is_r_services_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class AdditionalFeaturesServerConfigurationsArgs:
    def __init__(__self__, *, is_r_services_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRServicesEnabled")
    def is_r_services_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_r_services_enabled.setter
    def is_r_services_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class AgConfigurationArgsDict(TypedDict):
    
    replicas: NotRequired[pulumi.Input[Sequence[pulumi.Input[AgReplicaArgsDict]]]]


@pulumi.input_type
class AgConfigurationArgs:
    def __init__(__self__, *, replicas: Optional[pulumi.Input[Sequence[pulumi.Input[AgReplicaArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgReplicaArgs]]]]:
        
        ...
    
    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgReplicaArgs]]]]): # -> None:
        ...
    


class AgReplicaArgsDict(TypedDict):
    
    commit: NotRequired[pulumi.Input[Union[_builtins.str, Commit]]]
    failover: NotRequired[pulumi.Input[Union[_builtins.str, Failover]]]
    readable_secondary: NotRequired[pulumi.Input[Union[_builtins.str, ReadableSecondary]]]
    role: NotRequired[pulumi.Input[Union[_builtins.str, Role]]]
    sql_virtual_machine_instance_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AgReplicaArgs:
    def __init__(__self__, *, commit: Optional[pulumi.Input[Union[_builtins.str, Commit]]] = ..., failover: Optional[pulumi.Input[Union[_builtins.str, Failover]]] = ..., readable_secondary: Optional[pulumi.Input[Union[_builtins.str, ReadableSecondary]]] = ..., role: Optional[pulumi.Input[Union[_builtins.str, Role]]] = ..., sql_virtual_machine_instance_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commit(self) -> Optional[pulumi.Input[Union[_builtins.str, Commit]]]:
        
        ...
    
    @commit.setter
    def commit(self, value: Optional[pulumi.Input[Union[_builtins.str, Commit]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def failover(self) -> Optional[pulumi.Input[Union[_builtins.str, Failover]]]:
        
        ...
    
    @failover.setter
    def failover(self, value: Optional[pulumi.Input[Union[_builtins.str, Failover]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readableSecondary")
    def readable_secondary(self) -> Optional[pulumi.Input[Union[_builtins.str, ReadableSecondary]]]:
        
        ...
    
    @readable_secondary.setter
    def readable_secondary(self, value: Optional[pulumi.Input[Union[_builtins.str, ReadableSecondary]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[Union[_builtins.str, Role]]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[Union[_builtins.str, Role]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineInstanceId")
    def sql_virtual_machine_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_virtual_machine_instance_id.setter
    def sql_virtual_machine_instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AssessmentSettingsArgsDict(TypedDict):
    
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    run_immediately: NotRequired[pulumi.Input[_builtins.bool]]
    schedule: NotRequired[pulumi.Input[ScheduleArgsDict]]


@pulumi.input_type
class AssessmentSettingsArgs:
    def __init__(__self__, *, enable: Optional[pulumi.Input[_builtins.bool]] = ..., run_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., schedule: Optional[pulumi.Input[ScheduleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runImmediately")
    def run_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @run_immediately.setter
    def run_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[ScheduleArgs]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[ScheduleArgs]]): # -> None:
        ...
    


class AutoBackupSettingsArgsDict(TypedDict):
    
    backup_schedule_type: NotRequired[pulumi.Input[Union[_builtins.str, BackupScheduleType]]]
    backup_system_dbs: NotRequired[pulumi.Input[_builtins.bool]]
    days_of_week: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AutoBackupDaysOfWeek]]]]]
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    enable_encryption: NotRequired[pulumi.Input[_builtins.bool]]
    full_backup_frequency: NotRequired[pulumi.Input[Union[_builtins.str, FullBackupFrequencyType]]]
    full_backup_start_time: NotRequired[pulumi.Input[_builtins.int]]
    full_backup_window_hours: NotRequired[pulumi.Input[_builtins.int]]
    log_backup_frequency: NotRequired[pulumi.Input[_builtins.int]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    retention_period: NotRequired[pulumi.Input[_builtins.int]]
    storage_access_key: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_url: NotRequired[pulumi.Input[_builtins.str]]
    storage_container_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AutoBackupSettingsArgs:
    def __init__(__self__, *, backup_schedule_type: Optional[pulumi.Input[Union[_builtins.str, BackupScheduleType]]] = ..., backup_system_dbs: Optional[pulumi.Input[_builtins.bool]] = ..., days_of_week: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AutoBackupDaysOfWeek]]]]] = ..., enable: Optional[pulumi.Input[_builtins.bool]] = ..., enable_encryption: Optional[pulumi.Input[_builtins.bool]] = ..., full_backup_frequency: Optional[pulumi.Input[Union[_builtins.str, FullBackupFrequencyType]]] = ..., full_backup_start_time: Optional[pulumi.Input[_builtins.int]] = ..., full_backup_window_hours: Optional[pulumi.Input[_builtins.int]] = ..., log_backup_frequency: Optional[pulumi.Input[_builtins.int]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., storage_access_key: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_url: Optional[pulumi.Input[_builtins.str]] = ..., storage_container_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupScheduleType")
    def backup_schedule_type(self) -> Optional[pulumi.Input[Union[_builtins.str, BackupScheduleType]]]:
        
        ...
    
    @backup_schedule_type.setter
    def backup_schedule_type(self, value: Optional[pulumi.Input[Union[_builtins.str, BackupScheduleType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSystemDbs")
    def backup_system_dbs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @backup_system_dbs.setter
    def backup_system_dbs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AutoBackupDaysOfWeek]]]]]:
        
        ...
    
    @days_of_week.setter
    def days_of_week(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AutoBackupDaysOfWeek]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEncryption")
    def enable_encryption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_encryption.setter
    def enable_encryption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullBackupFrequency")
    def full_backup_frequency(self) -> Optional[pulumi.Input[Union[_builtins.str, FullBackupFrequencyType]]]:
        
        ...
    
    @full_backup_frequency.setter
    def full_backup_frequency(self, value: Optional[pulumi.Input[Union[_builtins.str, FullBackupFrequencyType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullBackupStartTime")
    def full_backup_start_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @full_backup_start_time.setter
    def full_backup_start_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullBackupWindowHours")
    def full_backup_window_hours(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @full_backup_window_hours.setter
    def full_backup_window_hours(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logBackupFrequency")
    def log_backup_frequency(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @log_backup_frequency.setter
    def log_backup_frequency(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccessKey")
    def storage_access_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_access_key.setter
    def storage_access_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_url.setter
    def storage_account_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerName")
    def storage_container_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_container_name.setter
    def storage_container_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AutoPatchingSettingsArgsDict(TypedDict):
    
    additional_vm_patch: NotRequired[pulumi.Input[Union[_builtins.str, AdditionalVmPatch]]]
    day_of_week: NotRequired[pulumi.Input[DayOfWeek]]
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    maintenance_window_duration: NotRequired[pulumi.Input[_builtins.int]]
    maintenance_window_starting_hour: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class AutoPatchingSettingsArgs:
    def __init__(__self__, *, additional_vm_patch: Optional[pulumi.Input[Union[_builtins.str, AdditionalVmPatch]]] = ..., day_of_week: Optional[pulumi.Input[DayOfWeek]] = ..., enable: Optional[pulumi.Input[_builtins.bool]] = ..., maintenance_window_duration: Optional[pulumi.Input[_builtins.int]] = ..., maintenance_window_starting_hour: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalVmPatch")
    def additional_vm_patch(self) -> Optional[pulumi.Input[Union[_builtins.str, AdditionalVmPatch]]]:
        
        ...
    
    @additional_vm_patch.setter
    def additional_vm_patch(self, value: Optional[pulumi.Input[Union[_builtins.str, AdditionalVmPatch]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[DayOfWeek]]:
        
        ...
    
    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[DayOfWeek]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindowDuration")
    def maintenance_window_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maintenance_window_duration.setter
    def maintenance_window_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindowStartingHour")
    def maintenance_window_starting_hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maintenance_window_starting_hour.setter
    def maintenance_window_starting_hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class KeyVaultCredentialSettingsArgsDict(TypedDict):
    
    azure_key_vault_url: NotRequired[pulumi.Input[_builtins.str]]
    credential_name: NotRequired[pulumi.Input[_builtins.str]]
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    service_principal_name: NotRequired[pulumi.Input[_builtins.str]]
    service_principal_secret: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyVaultCredentialSettingsArgs:
    def __init__(__self__, *, azure_key_vault_url: Optional[pulumi.Input[_builtins.str]] = ..., credential_name: Optional[pulumi.Input[_builtins.str]] = ..., enable: Optional[pulumi.Input[_builtins.bool]] = ..., service_principal_name: Optional[pulumi.Input[_builtins.str]] = ..., service_principal_secret: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureKeyVaultUrl")
    def azure_key_vault_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @azure_key_vault_url.setter
    def azure_key_vault_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialName")
    def credential_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @credential_name.setter
    def credential_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipalName")
    def service_principal_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_principal_name.setter
    def service_principal_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipalSecret")
    def service_principal_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_principal_secret.setter
    def service_principal_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LoadBalancerConfigurationArgsDict(TypedDict):
    
    load_balancer_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address: NotRequired[pulumi.Input[PrivateIPAddressArgsDict]]
    probe_port: NotRequired[pulumi.Input[_builtins.int]]
    public_ip_address_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    sql_virtual_machine_instances: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class LoadBalancerConfigurationArgs:
    def __init__(__self__, *, load_balancer_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_address: Optional[pulumi.Input[PrivateIPAddressArgs]] = ..., probe_port: Optional[pulumi.Input[_builtins.int]] = ..., public_ip_address_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., sql_virtual_machine_instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerResourceId")
    def load_balancer_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @load_balancer_resource_id.setter
    def load_balancer_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[PrivateIPAddressArgs]]:
        
        ...
    
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[PrivateIPAddressArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probePort")
    def probe_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @probe_port.setter
    def probe_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAddressResourceId")
    def public_ip_address_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip_address_resource_id.setter
    def public_ip_address_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineInstances")
    def sql_virtual_machine_instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @sql_virtual_machine_instances.setter
    def sql_virtual_machine_instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MultiSubnetIpConfigurationArgsDict(TypedDict):
    
    private_ip_address: pulumi.Input[PrivateIPAddressArgsDict]
    sql_virtual_machine_instance: pulumi.Input[_builtins.str]


@pulumi.input_type
class MultiSubnetIpConfigurationArgs:
    def __init__(__self__, *, private_ip_address: pulumi.Input[PrivateIPAddressArgs], sql_virtual_machine_instance: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> pulumi.Input[PrivateIPAddressArgs]:
        
        ...
    
    @private_ip_address.setter
    def private_ip_address(self, value: pulumi.Input[PrivateIPAddressArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineInstance")
    def sql_virtual_machine_instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_virtual_machine_instance.setter
    def sql_virtual_machine_instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class PrivateIPAddressArgsDict(TypedDict):
    
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    subnet_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateIPAddressArgs:
    def __init__(__self__, *, ip_address: Optional[pulumi.Input[_builtins.str]] = ..., subnet_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetResourceId")
    def subnet_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_resource_id.setter
    def subnet_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, IdentityType]]]


@pulumi.input_type
class ResourceIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]): # -> None:
        ...
    


class SQLInstanceSettingsArgsDict(TypedDict):
    
    collation: NotRequired[pulumi.Input[_builtins.str]]
    is_ifi_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_lpim_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_optimize_for_ad_hoc_workloads_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    max_dop: NotRequired[pulumi.Input[_builtins.int]]
    max_server_memory_mb: NotRequired[pulumi.Input[_builtins.int]]
    min_server_memory_mb: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SQLInstanceSettingsArgs:
    def __init__(__self__, *, collation: Optional[pulumi.Input[_builtins.str]] = ..., is_ifi_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_lpim_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_optimize_for_ad_hoc_workloads_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., max_dop: Optional[pulumi.Input[_builtins.int]] = ..., max_server_memory_mb: Optional[pulumi.Input[_builtins.int]] = ..., min_server_memory_mb: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collation.setter
    def collation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isIfiEnabled")
    def is_ifi_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_ifi_enabled.setter
    def is_ifi_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLpimEnabled")
    def is_lpim_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_lpim_enabled.setter
    def is_lpim_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOptimizeForAdHocWorkloadsEnabled")
    def is_optimize_for_ad_hoc_workloads_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_optimize_for_ad_hoc_workloads_enabled.setter
    def is_optimize_for_ad_hoc_workloads_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDop")
    def max_dop(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_dop.setter
    def max_dop(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxServerMemoryMB")
    def max_server_memory_mb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_server_memory_mb.setter
    def max_server_memory_mb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minServerMemoryMB")
    def min_server_memory_mb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_server_memory_mb.setter
    def min_server_memory_mb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SQLStorageSettingsArgsDict(TypedDict):
    
    default_file_path: NotRequired[pulumi.Input[_builtins.str]]
    luns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    use_storage_pool: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SQLStorageSettingsArgs:
    def __init__(__self__, *, default_file_path: Optional[pulumi.Input[_builtins.str]] = ..., luns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., use_storage_pool: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultFilePath")
    def default_file_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_file_path.setter
    def default_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def luns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @luns.setter
    def luns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useStoragePool")
    def use_storage_pool(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_storage_pool.setter
    def use_storage_pool(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SQLTempDbSettingsArgsDict(TypedDict):
    
    data_file_count: NotRequired[pulumi.Input[_builtins.int]]
    data_file_size: NotRequired[pulumi.Input[_builtins.int]]
    data_growth: NotRequired[pulumi.Input[_builtins.int]]
    default_file_path: NotRequired[pulumi.Input[_builtins.str]]
    log_file_size: NotRequired[pulumi.Input[_builtins.int]]
    log_growth: NotRequired[pulumi.Input[_builtins.int]]
    luns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    persist_folder: NotRequired[pulumi.Input[_builtins.bool]]
    persist_folder_path: NotRequired[pulumi.Input[_builtins.str]]
    use_storage_pool: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SQLTempDbSettingsArgs:
    def __init__(__self__, *, data_file_count: Optional[pulumi.Input[_builtins.int]] = ..., data_file_size: Optional[pulumi.Input[_builtins.int]] = ..., data_growth: Optional[pulumi.Input[_builtins.int]] = ..., default_file_path: Optional[pulumi.Input[_builtins.str]] = ..., log_file_size: Optional[pulumi.Input[_builtins.int]] = ..., log_growth: Optional[pulumi.Input[_builtins.int]] = ..., luns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., persist_folder: Optional[pulumi.Input[_builtins.bool]] = ..., persist_folder_path: Optional[pulumi.Input[_builtins.str]] = ..., use_storage_pool: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFileCount")
    def data_file_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @data_file_count.setter
    def data_file_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFileSize")
    def data_file_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @data_file_size.setter
    def data_file_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataGrowth")
    def data_growth(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @data_growth.setter
    def data_growth(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultFilePath")
    def default_file_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_file_path.setter
    def default_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logFileSize")
    def log_file_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @log_file_size.setter
    def log_file_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGrowth")
    def log_growth(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @log_growth.setter
    def log_growth(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def luns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @luns.setter
    def luns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistFolder")
    def persist_folder(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @persist_folder.setter
    def persist_folder(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistFolderPath")
    def persist_folder_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @persist_folder_path.setter
    def persist_folder_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useStoragePool")
    def use_storage_pool(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_storage_pool.setter
    def use_storage_pool(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ScheduleArgsDict(TypedDict):
    
    day_of_week: NotRequired[pulumi.Input[AssessmentDayOfWeek]]
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    monthly_occurrence: NotRequired[pulumi.Input[_builtins.int]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    weekly_interval: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *, day_of_week: Optional[pulumi.Input[AssessmentDayOfWeek]] = ..., enable: Optional[pulumi.Input[_builtins.bool]] = ..., monthly_occurrence: Optional[pulumi.Input[_builtins.int]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., weekly_interval: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[AssessmentDayOfWeek]]:
        
        ...
    
    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[AssessmentDayOfWeek]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyOccurrence")
    def monthly_occurrence(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @monthly_occurrence.setter
    def monthly_occurrence(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyInterval")
    def weekly_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weekly_interval.setter
    def weekly_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ServerConfigurationsManagementSettingsArgsDict(TypedDict):
    
    additional_features_server_configurations: NotRequired[pulumi.Input[AdditionalFeaturesServerConfigurationsArgsDict]]
    azure_ad_authentication_settings: NotRequired[pulumi.Input[AADAuthenticationSettingsArgsDict]]
    sql_connectivity_update_settings: NotRequired[pulumi.Input[SqlConnectivityUpdateSettingsArgsDict]]
    sql_instance_settings: NotRequired[pulumi.Input[SQLInstanceSettingsArgsDict]]
    sql_storage_update_settings: NotRequired[pulumi.Input[SqlStorageUpdateSettingsArgsDict]]
    sql_workload_type_update_settings: NotRequired[pulumi.Input[SqlWorkloadTypeUpdateSettingsArgsDict]]


@pulumi.input_type
class ServerConfigurationsManagementSettingsArgs:
    def __init__(__self__, *, additional_features_server_configurations: Optional[pulumi.Input[AdditionalFeaturesServerConfigurationsArgs]] = ..., azure_ad_authentication_settings: Optional[pulumi.Input[AADAuthenticationSettingsArgs]] = ..., sql_connectivity_update_settings: Optional[pulumi.Input[SqlConnectivityUpdateSettingsArgs]] = ..., sql_instance_settings: Optional[pulumi.Input[SQLInstanceSettingsArgs]] = ..., sql_storage_update_settings: Optional[pulumi.Input[SqlStorageUpdateSettingsArgs]] = ..., sql_workload_type_update_settings: Optional[pulumi.Input[SqlWorkloadTypeUpdateSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalFeaturesServerConfigurations")
    def additional_features_server_configurations(self) -> Optional[pulumi.Input[AdditionalFeaturesServerConfigurationsArgs]]:
        
        ...
    
    @additional_features_server_configurations.setter
    def additional_features_server_configurations(self, value: Optional[pulumi.Input[AdditionalFeaturesServerConfigurationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureAdAuthenticationSettings")
    def azure_ad_authentication_settings(self) -> Optional[pulumi.Input[AADAuthenticationSettingsArgs]]:
        
        ...
    
    @azure_ad_authentication_settings.setter
    def azure_ad_authentication_settings(self, value: Optional[pulumi.Input[AADAuthenticationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlConnectivityUpdateSettings")
    def sql_connectivity_update_settings(self) -> Optional[pulumi.Input[SqlConnectivityUpdateSettingsArgs]]:
        
        ...
    
    @sql_connectivity_update_settings.setter
    def sql_connectivity_update_settings(self, value: Optional[pulumi.Input[SqlConnectivityUpdateSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlInstanceSettings")
    def sql_instance_settings(self) -> Optional[pulumi.Input[SQLInstanceSettingsArgs]]:
        
        ...
    
    @sql_instance_settings.setter
    def sql_instance_settings(self, value: Optional[pulumi.Input[SQLInstanceSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlStorageUpdateSettings")
    def sql_storage_update_settings(self) -> Optional[pulumi.Input[SqlStorageUpdateSettingsArgs]]:
        
        ...
    
    @sql_storage_update_settings.setter
    def sql_storage_update_settings(self, value: Optional[pulumi.Input[SqlStorageUpdateSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlWorkloadTypeUpdateSettings")
    def sql_workload_type_update_settings(self) -> Optional[pulumi.Input[SqlWorkloadTypeUpdateSettingsArgs]]:
        
        ...
    
    @sql_workload_type_update_settings.setter
    def sql_workload_type_update_settings(self, value: Optional[pulumi.Input[SqlWorkloadTypeUpdateSettingsArgs]]): # -> None:
        ...
    


class SqlConnectivityUpdateSettingsArgsDict(TypedDict):
    
    connectivity_type: NotRequired[pulumi.Input[Union[_builtins.str, ConnectivityType]]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    sql_auth_update_password: NotRequired[pulumi.Input[_builtins.str]]
    sql_auth_update_user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SqlConnectivityUpdateSettingsArgs:
    def __init__(__self__, *, connectivity_type: Optional[pulumi.Input[Union[_builtins.str, ConnectivityType]]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., sql_auth_update_password: Optional[pulumi.Input[_builtins.str]] = ..., sql_auth_update_user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityType")
    def connectivity_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ConnectivityType]]]:
        
        ...
    
    @connectivity_type.setter
    def connectivity_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectivityType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlAuthUpdatePassword")
    def sql_auth_update_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_auth_update_password.setter
    def sql_auth_update_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlAuthUpdateUserName")
    def sql_auth_update_user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_auth_update_user_name.setter
    def sql_auth_update_user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SqlStorageUpdateSettingsArgsDict(TypedDict):
    
    disk_configuration_type: NotRequired[pulumi.Input[Union[_builtins.str, DiskConfigurationType]]]
    disk_count: NotRequired[pulumi.Input[_builtins.int]]
    starting_device_id: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SqlStorageUpdateSettingsArgs:
    def __init__(__self__, *, disk_configuration_type: Optional[pulumi.Input[Union[_builtins.str, DiskConfigurationType]]] = ..., disk_count: Optional[pulumi.Input[_builtins.int]] = ..., starting_device_id: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConfigurationType")
    def disk_configuration_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskConfigurationType]]]:
        
        ...
    
    @disk_configuration_type.setter
    def disk_configuration_type(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskConfigurationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskCount")
    def disk_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_count.setter
    def disk_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingDeviceId")
    def starting_device_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @starting_device_id.setter
    def starting_device_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SqlWorkloadTypeUpdateSettingsArgsDict(TypedDict):
    
    sql_workload_type: NotRequired[pulumi.Input[Union[_builtins.str, SqlWorkloadType]]]


@pulumi.input_type
class SqlWorkloadTypeUpdateSettingsArgs:
    def __init__(__self__, *, sql_workload_type: Optional[pulumi.Input[Union[_builtins.str, SqlWorkloadType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlWorkloadType")
    def sql_workload_type(self) -> Optional[pulumi.Input[Union[_builtins.str, SqlWorkloadType]]]:
        
        ...
    
    @sql_workload_type.setter
    def sql_workload_type(self, value: Optional[pulumi.Input[Union[_builtins.str, SqlWorkloadType]]]): # -> None:
        ...
    


class StorageConfigurationSettingsArgsDict(TypedDict):
    
    disk_configuration_type: NotRequired[pulumi.Input[Union[_builtins.str, DiskConfigurationType]]]
    enable_storage_config_blade: NotRequired[pulumi.Input[_builtins.bool]]
    sql_data_settings: NotRequired[pulumi.Input[SQLStorageSettingsArgsDict]]
    sql_log_settings: NotRequired[pulumi.Input[SQLStorageSettingsArgsDict]]
    sql_system_db_on_data_disk: NotRequired[pulumi.Input[_builtins.bool]]
    sql_temp_db_settings: NotRequired[pulumi.Input[SQLTempDbSettingsArgsDict]]
    storage_workload_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageWorkloadType]]]


@pulumi.input_type
class StorageConfigurationSettingsArgs:
    def __init__(__self__, *, disk_configuration_type: Optional[pulumi.Input[Union[_builtins.str, DiskConfigurationType]]] = ..., enable_storage_config_blade: Optional[pulumi.Input[_builtins.bool]] = ..., sql_data_settings: Optional[pulumi.Input[SQLStorageSettingsArgs]] = ..., sql_log_settings: Optional[pulumi.Input[SQLStorageSettingsArgs]] = ..., sql_system_db_on_data_disk: Optional[pulumi.Input[_builtins.bool]] = ..., sql_temp_db_settings: Optional[pulumi.Input[SQLTempDbSettingsArgs]] = ..., storage_workload_type: Optional[pulumi.Input[Union[_builtins.str, StorageWorkloadType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConfigurationType")
    def disk_configuration_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskConfigurationType]]]:
        
        ...
    
    @disk_configuration_type.setter
    def disk_configuration_type(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskConfigurationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStorageConfigBlade")
    def enable_storage_config_blade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_storage_config_blade.setter
    def enable_storage_config_blade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlDataSettings")
    def sql_data_settings(self) -> Optional[pulumi.Input[SQLStorageSettingsArgs]]:
        
        ...
    
    @sql_data_settings.setter
    def sql_data_settings(self, value: Optional[pulumi.Input[SQLStorageSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlLogSettings")
    def sql_log_settings(self) -> Optional[pulumi.Input[SQLStorageSettingsArgs]]:
        
        ...
    
    @sql_log_settings.setter
    def sql_log_settings(self, value: Optional[pulumi.Input[SQLStorageSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlSystemDbOnDataDisk")
    def sql_system_db_on_data_disk(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @sql_system_db_on_data_disk.setter
    def sql_system_db_on_data_disk(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlTempDbSettings")
    def sql_temp_db_settings(self) -> Optional[pulumi.Input[SQLTempDbSettingsArgs]]:
        
        ...
    
    @sql_temp_db_settings.setter
    def sql_temp_db_settings(self, value: Optional[pulumi.Input[SQLTempDbSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageWorkloadType")
    def storage_workload_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageWorkloadType]]]:
        
        ...
    
    @storage_workload_type.setter
    def storage_workload_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageWorkloadType]]]): # -> None:
        ...
    


class VirtualMachineIdentityArgsDict(TypedDict):
    
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, VmIdentityType]]]


@pulumi.input_type
class VirtualMachineIdentityArgs:
    def __init__(__self__, *, resource_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, VmIdentityType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, VmIdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, VmIdentityType]]]): # -> None:
        ...
    


class WsfcDomainCredentialsArgsDict(TypedDict):
    
    cluster_bootstrap_account_password: NotRequired[pulumi.Input[_builtins.str]]
    cluster_operator_account_password: NotRequired[pulumi.Input[_builtins.str]]
    sql_service_account_password: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WsfcDomainCredentialsArgs:
    def __init__(__self__, *, cluster_bootstrap_account_password: Optional[pulumi.Input[_builtins.str]] = ..., cluster_operator_account_password: Optional[pulumi.Input[_builtins.str]] = ..., sql_service_account_password: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterBootstrapAccountPassword")
    def cluster_bootstrap_account_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_bootstrap_account_password.setter
    def cluster_bootstrap_account_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterOperatorAccountPassword")
    def cluster_operator_account_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_operator_account_password.setter
    def cluster_operator_account_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServiceAccountPassword")
    def sql_service_account_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_service_account_password.setter
    def sql_service_account_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WsfcDomainProfileArgsDict(TypedDict):
    
    cluster_bootstrap_account: NotRequired[pulumi.Input[_builtins.str]]
    cluster_operator_account: NotRequired[pulumi.Input[_builtins.str]]
    cluster_subnet_type: NotRequired[pulumi.Input[Union[_builtins.str, ClusterSubnetType]]]
    domain_fqdn: NotRequired[pulumi.Input[_builtins.str]]
    file_share_witness_path: NotRequired[pulumi.Input[_builtins.str]]
    is_sql_service_account_gmsa: NotRequired[pulumi.Input[_builtins.bool]]
    ou_path: NotRequired[pulumi.Input[_builtins.str]]
    sql_service_account: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_primary_key: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WsfcDomainProfileArgs:
    def __init__(__self__, *, cluster_bootstrap_account: Optional[pulumi.Input[_builtins.str]] = ..., cluster_operator_account: Optional[pulumi.Input[_builtins.str]] = ..., cluster_subnet_type: Optional[pulumi.Input[Union[_builtins.str, ClusterSubnetType]]] = ..., domain_fqdn: Optional[pulumi.Input[_builtins.str]] = ..., file_share_witness_path: Optional[pulumi.Input[_builtins.str]] = ..., is_sql_service_account_gmsa: Optional[pulumi.Input[_builtins.bool]] = ..., ou_path: Optional[pulumi.Input[_builtins.str]] = ..., sql_service_account: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_primary_key: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterBootstrapAccount")
    def cluster_bootstrap_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_bootstrap_account.setter
    def cluster_bootstrap_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterOperatorAccount")
    def cluster_operator_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_operator_account.setter
    def cluster_operator_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSubnetType")
    def cluster_subnet_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ClusterSubnetType]]]:
        
        ...
    
    @cluster_subnet_type.setter
    def cluster_subnet_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ClusterSubnetType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainFqdn")
    def domain_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_fqdn.setter
    def domain_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShareWitnessPath")
    def file_share_witness_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_share_witness_path.setter
    def file_share_witness_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSqlServiceAccountGmsa")
    def is_sql_service_account_gmsa(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_sql_service_account_gmsa.setter
    def is_sql_service_account_gmsa(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ouPath")
    def ou_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ou_path.setter
    def ou_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServiceAccount")
    def sql_service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_service_account.setter
    def sql_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountPrimaryKey")
    def storage_account_primary_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_primary_key.setter
    def storage_account_primary_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_url.setter
    def storage_account_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


