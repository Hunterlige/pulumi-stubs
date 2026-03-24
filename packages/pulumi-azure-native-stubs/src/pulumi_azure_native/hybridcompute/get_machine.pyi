

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMachineResult', 'AwaitableGetMachineResult', 'get_machine', 'get_machine_output']
@pulumi.output_type
class GetMachineResult:
    
    def __init__(__self__, ad_fqdn=..., agent_configuration=..., agent_upgrade=..., agent_version=..., azure_api_version=..., client_public_key=..., cloud_metadata=..., detected_properties=..., display_name=..., dns_fqdn=..., domain_name=..., error_details=..., extensions=..., id=..., identity=..., kind=..., last_status_change=..., license_profile=..., location=..., location_data=..., machine_fqdn=..., mssql_discovered=..., name=..., network_profile=..., os_edition=..., os_name=..., os_profile=..., os_sku=..., os_type=..., os_version=..., parent_cluster_resource_id=..., private_link_scope_resource_id=..., provisioning_state=..., resources=..., service_statuses=..., status=..., system_data=..., tags=..., type=..., vm_id=..., vm_uuid=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adFqdn")
    def ad_fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(self) -> outputs.AgentConfigurationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentUpgrade")
    def agent_upgrade(self) -> Optional[outputs.AgentUpgradeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientPublicKey")
    def client_public_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudMetadata")
    def cloud_metadata(self) -> Optional[outputs.CloudMetadataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectedProperties")
    def detected_properties(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsFqdn")
    def dns_fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> Sequence[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[Sequence[outputs.MachineExtensionInstanceViewResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStatusChange")
    def last_status_change(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseProfile")
    def license_profile(self) -> Optional[outputs.LicenseProfileMachineInstanceViewResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationData")
    def location_data(self) -> Optional[outputs.LocationDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineFqdn")
    def machine_fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mssqlDiscovered")
    def mssql_discovered(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> outputs.NetworkProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osEdition")
    def os_edition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[outputs.OSProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osSku")
    def os_sku(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentClusterResourceId")
    def parent_cluster_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[outputs.MachineExtensionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceStatuses")
    def service_statuses(self) -> Optional[outputs.ServiceStatusesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmUuid")
    def vm_uuid(self) -> _builtins.str:
        
        ...
    


class AwaitableGetMachineResult(GetMachineResult):
    def __await__(self): # -> Generator[Never, Any, GetMachineResult]:
        ...
    


def get_machine(expand: Optional[_builtins.str] = ..., machine_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMachineResult:
    
    ...

def get_machine_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., machine_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMachineResult]:
    
    ...

