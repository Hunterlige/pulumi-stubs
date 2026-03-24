

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ManagedInstanceArgs', 'ManagedInstance']
@pulumi.input_type
class ManagedInstanceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], administrator_login: Optional[pulumi.Input[_builtins.str]] = ..., administrator_login_password: Optional[pulumi.Input[_builtins.str]] = ..., administrators: Optional[pulumi.Input[ManagedInstanceExternalAdministratorArgs]] = ..., authentication_metadata: Optional[pulumi.Input[Union[_builtins.str, AuthMetadataLookupModes]]] = ..., collation: Optional[pulumi.Input[_builtins.str]] = ..., database_format: Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceDatabaseFormat]]] = ..., dns_zone_partner: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_secondary_usage: Optional[pulumi.Input[Union[_builtins.str, HybridSecondaryUsage]]] = ..., identity: Optional[pulumi.Input[ResourceIdentityArgs]] = ..., instance_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., is_general_purpose_v2: Optional[pulumi.Input[_builtins.bool]] = ..., key_id: Optional[pulumi.Input[_builtins.str]] = ..., license_type: Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceLicenseType]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_configuration_id: Optional[pulumi.Input[_builtins.str]] = ..., managed_instance_create_mode: Optional[pulumi.Input[Union[_builtins.str, ManagedServerCreateMode]]] = ..., managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., minimal_tls_version: Optional[pulumi.Input[_builtins.str]] = ..., pricing_model: Optional[pulumi.Input[Union[_builtins.str, PricingModel]]] = ..., primary_user_assigned_identity_id: Optional[pulumi.Input[_builtins.str]] = ..., proxy_override: Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceProxyOverride]]] = ..., public_data_endpoint_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., requested_backup_storage_redundancy: Optional[pulumi.Input[Union[_builtins.str, BackupStorageRedundancy]]] = ..., restore_point_in_time: Optional[pulumi.Input[_builtins.str]] = ..., service_principal: Optional[pulumi.Input[ServicePrincipalArgs]] = ..., sku: Optional[pulumi.Input[SkuArgs]] = ..., source_managed_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., storage_i_ops: Optional[pulumi.Input[_builtins.int]] = ..., storage_size_in_gb: Optional[pulumi.Input[_builtins.int]] = ..., storage_throughput_m_bps: Optional[pulumi.Input[_builtins.int]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timezone_id: Optional[pulumi.Input[_builtins.str]] = ..., v_cores: Optional[pulumi.Input[_builtins.int]] = ..., zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @administrator_login.setter
    def administrator_login(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @administrator_login_password.setter
    def administrator_login_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def administrators(self) -> Optional[pulumi.Input[ManagedInstanceExternalAdministratorArgs]]:
        
        ...
    
    @administrators.setter
    def administrators(self, value: Optional[pulumi.Input[ManagedInstanceExternalAdministratorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMetadata")
    def authentication_metadata(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthMetadataLookupModes]]]:
        
        ...
    
    @authentication_metadata.setter
    def authentication_metadata(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthMetadataLookupModes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collation.setter
    def collation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFormat")
    def database_format(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceDatabaseFormat]]]:
        
        ...
    
    @database_format.setter
    def database_format(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceDatabaseFormat]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsZonePartner")
    def dns_zone_partner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_zone_partner.setter
    def dns_zone_partner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridSecondaryUsage")
    def hybrid_secondary_usage(self) -> Optional[pulumi.Input[Union[_builtins.str, HybridSecondaryUsage]]]:
        
        ...
    
    @hybrid_secondary_usage.setter
    def hybrid_secondary_usage(self, value: Optional[pulumi.Input[Union[_builtins.str, HybridSecondaryUsage]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ResourceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ResourceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePoolId")
    def instance_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_pool_id.setter
    def instance_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isGeneralPurposeV2")
    def is_general_purpose_v2(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_general_purpose_v2.setter
    def is_general_purpose_v2(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceLicenseType]]]:
        
        ...
    
    @license_type.setter
    def license_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceLicenseType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_configuration_id.setter
    def maintenance_configuration_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedInstanceCreateMode")
    def managed_instance_create_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedServerCreateMode]]]:
        
        ...
    
    @managed_instance_create_mode.setter
    def managed_instance_create_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedServerCreateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_instance_name.setter
    def managed_instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @minimal_tls_version.setter
    def minimal_tls_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingModel")
    def pricing_model(self) -> Optional[pulumi.Input[Union[_builtins.str, PricingModel]]]:
        
        ...
    
    @pricing_model.setter
    def pricing_model(self, value: Optional[pulumi.Input[Union[_builtins.str, PricingModel]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_user_assigned_identity_id.setter
    def primary_user_assigned_identity_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyOverride")
    def proxy_override(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceProxyOverride]]]:
        
        ...
    
    @proxy_override.setter
    def proxy_override(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceProxyOverride]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDataEndpointEnabled")
    def public_data_endpoint_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @public_data_endpoint_enabled.setter
    def public_data_endpoint_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedBackupStorageRedundancy")
    def requested_backup_storage_redundancy(self) -> Optional[pulumi.Input[Union[_builtins.str, BackupStorageRedundancy]]]:
        
        ...
    
    @requested_backup_storage_redundancy.setter
    def requested_backup_storage_redundancy(self, value: Optional[pulumi.Input[Union[_builtins.str, BackupStorageRedundancy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_point_in_time.setter
    def restore_point_in_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> Optional[pulumi.Input[ServicePrincipalArgs]]:
        
        ...
    
    @service_principal.setter
    def service_principal(self, value: Optional[pulumi.Input[ServicePrincipalArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceManagedInstanceId")
    def source_managed_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_managed_instance_id.setter
    def source_managed_instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageIOps")
    def storage_i_ops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_i_ops.setter
    def storage_i_ops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSizeInGB")
    def storage_size_in_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_size_in_gb.setter
    def storage_size_in_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageThroughputMBps")
    def storage_throughput_m_bps(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_throughput_m_bps.setter
    def storage_throughput_m_bps(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timezoneId")
    def timezone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @timezone_id.setter
    def timezone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCores")
    def v_cores(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @v_cores.setter
    def v_cores(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @zone_redundant.setter
    def zone_redundant(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:ManagedInstance")
class ManagedInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., administrator_login: Optional[pulumi.Input[_builtins.str]] = ..., administrator_login_password: Optional[pulumi.Input[_builtins.str]] = ..., administrators: Optional[pulumi.Input[Union[ManagedInstanceExternalAdministratorArgs, ManagedInstanceExternalAdministratorArgsDict]]] = ..., authentication_metadata: Optional[pulumi.Input[Union[_builtins.str, AuthMetadataLookupModes]]] = ..., collation: Optional[pulumi.Input[_builtins.str]] = ..., database_format: Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceDatabaseFormat]]] = ..., dns_zone_partner: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_secondary_usage: Optional[pulumi.Input[Union[_builtins.str, HybridSecondaryUsage]]] = ..., identity: Optional[pulumi.Input[Union[ResourceIdentityArgs, ResourceIdentityArgsDict]]] = ..., instance_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., is_general_purpose_v2: Optional[pulumi.Input[_builtins.bool]] = ..., key_id: Optional[pulumi.Input[_builtins.str]] = ..., license_type: Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceLicenseType]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_configuration_id: Optional[pulumi.Input[_builtins.str]] = ..., managed_instance_create_mode: Optional[pulumi.Input[Union[_builtins.str, ManagedServerCreateMode]]] = ..., managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., minimal_tls_version: Optional[pulumi.Input[_builtins.str]] = ..., pricing_model: Optional[pulumi.Input[Union[_builtins.str, PricingModel]]] = ..., primary_user_assigned_identity_id: Optional[pulumi.Input[_builtins.str]] = ..., proxy_override: Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceProxyOverride]]] = ..., public_data_endpoint_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., requested_backup_storage_redundancy: Optional[pulumi.Input[Union[_builtins.str, BackupStorageRedundancy]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_point_in_time: Optional[pulumi.Input[_builtins.str]] = ..., service_principal: Optional[pulumi.Input[Union[ServicePrincipalArgs, ServicePrincipalArgsDict]]] = ..., sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ..., source_managed_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., storage_i_ops: Optional[pulumi.Input[_builtins.int]] = ..., storage_size_in_gb: Optional[pulumi.Input[_builtins.int]] = ..., storage_throughput_m_bps: Optional[pulumi.Input[_builtins.int]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timezone_id: Optional[pulumi.Input[_builtins.str]] = ..., v_cores: Optional[pulumi.Input[_builtins.int]] = ..., zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagedInstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ManagedInstance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def administrators(self) -> pulumi.Output[Optional[outputs.ManagedInstanceExternalAdministratorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMetadata")
    def authentication_metadata(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentBackupStorageRedundancy")
    def current_backup_storage_redundancy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFormat")
    def database_format(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsZone")
    def dns_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalGovernanceStatus")
    def external_governance_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridSecondaryUsage")
    def hybrid_secondary_usage(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridSecondaryUsageDetected")
    def hybrid_secondary_usage_detected(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ResourceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePoolId")
    def instance_pool_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isGeneralPurposeV2")
    def is_general_purpose_v2(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingModel")
    def pricing_model(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence[outputs.ManagedInstancePecPropertyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyOverride")
    def proxy_override(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDataEndpointEnabled")
    def public_data_endpoint_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedBackupStorageRedundancy")
    def requested_backup_storage_redundancy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> pulumi.Output[Optional[outputs.ServicePrincipalResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageIOps")
    def storage_i_ops(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSizeInGB")
    def storage_size_in_gb(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageThroughputMBps")
    def storage_throughput_m_bps(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timezoneId")
    def timezone_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCores")
    def v_cores(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualClusterId")
    def virtual_cluster_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


