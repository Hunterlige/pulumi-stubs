

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagedInstanceResult', 'AwaitableGetManagedInstanceResult', 'get_managed_instance', 'get_managed_instance_output']
@pulumi.output_type
class GetManagedInstanceResult:
    
    def __init__(__self__, administrator_login=..., administrators=..., authentication_metadata=..., azure_api_version=..., collation=..., create_time=..., current_backup_storage_redundancy=..., database_format=..., dns_zone=..., external_governance_status=..., fully_qualified_domain_name=..., hybrid_secondary_usage=..., hybrid_secondary_usage_detected=..., id=..., identity=..., instance_pool_id=..., is_general_purpose_v2=..., key_id=..., license_type=..., location=..., maintenance_configuration_id=..., minimal_tls_version=..., name=..., pricing_model=..., primary_user_assigned_identity_id=..., private_endpoint_connections=..., provisioning_state=..., proxy_override=..., public_data_endpoint_enabled=..., requested_backup_storage_redundancy=..., service_principal=..., sku=..., state=..., storage_i_ops=..., storage_size_in_gb=..., storage_throughput_m_bps=..., subnet_id=..., tags=..., timezone_id=..., type=..., v_cores=..., virtual_cluster_id=..., zone_redundant=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def administrators(self) -> Optional[outputs.ManagedInstanceExternalAdministratorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMetadata")
    def authentication_metadata(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentBackupStorageRedundancy")
    def current_backup_storage_redundancy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFormat")
    def database_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsZone")
    def dns_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalGovernanceStatus")
    def external_governance_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridSecondaryUsage")
    def hybrid_secondary_usage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridSecondaryUsageDetected")
    def hybrid_secondary_usage_detected(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ResourceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePoolId")
    def instance_pool_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isGeneralPurposeV2")
    def is_general_purpose_v2(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingModel")
    def pricing_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.ManagedInstancePecPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyOverride")
    def proxy_override(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDataEndpointEnabled")
    def public_data_endpoint_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedBackupStorageRedundancy")
    def requested_backup_storage_redundancy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> Optional[outputs.ServicePrincipalResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageIOps")
    def storage_i_ops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSizeInGB")
    def storage_size_in_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageThroughputMBps")
    def storage_throughput_m_bps(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timezoneId")
    def timezone_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCores")
    def v_cores(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualClusterId")
    def virtual_cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[_builtins.bool]:
        
        ...
    


class AwaitableGetManagedInstanceResult(GetManagedInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedInstanceResult]:
        ...
    


def get_managed_instance(expand: Optional[_builtins.str] = ..., managed_instance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedInstanceResult:
    
    ...

def get_managed_instance_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedInstanceResult]:
    
    ...

