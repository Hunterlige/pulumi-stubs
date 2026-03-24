

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAFDCustomDomainResult', 'AwaitableGetAFDCustomDomainResult', 'get_afd_custom_domain', 'get_afd_custom_domain_output']
@pulumi.output_type
class GetAFDCustomDomainResult:
    
    def __init__(__self__, azure_api_version=..., azure_dns_zone=..., deployment_status=..., domain_validation_state=..., extended_properties=..., host_name=..., id=..., name=..., pre_validated_custom_domain_resource_id=..., profile_name=..., provisioning_state=..., system_data=..., tls_settings=..., type=..., validation_properties=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDnsZone")
    def azure_dns_zone(self) -> Optional[outputs.ResourceReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainValidationState")
    def domain_validation_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preValidatedCustomDomainResourceId")
    def pre_validated_custom_domain_resource_id(self) -> Optional[outputs.ResourceReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(self) -> Optional[outputs.AFDDomainHttpsParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationProperties")
    def validation_properties(self) -> outputs.DomainValidationPropertiesResponse:
        
        ...
    


class AwaitableGetAFDCustomDomainResult(GetAFDCustomDomainResult):
    def __await__(self): # -> Generator[Never, Any, GetAFDCustomDomainResult]:
        ...
    


def get_afd_custom_domain(custom_domain_name: Optional[_builtins.str] = ..., profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAFDCustomDomainResult:
    
    ...

def get_afd_custom_domain_output(custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAFDCustomDomainResult]:
    
    ...

