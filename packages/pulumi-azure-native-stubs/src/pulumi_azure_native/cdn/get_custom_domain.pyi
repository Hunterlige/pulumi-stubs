

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCustomDomainResult', 'AwaitableGetCustomDomainResult', 'get_custom_domain', 'get_custom_domain_output']
@pulumi.output_type
class GetCustomDomainResult:
    
    def __init__(__self__, azure_api_version=..., custom_https_parameters=..., custom_https_provisioning_state=..., custom_https_provisioning_substate=..., host_name=..., id=..., name=..., provisioning_state=..., resource_state=..., system_data=..., type=..., validation_data=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHttpsParameters")
    def custom_https_parameters(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHttpsProvisioningState")
    def custom_https_provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHttpsProvisioningSubstate")
    def custom_https_provisioning_substate(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetCustomDomainResult(GetCustomDomainResult):
    def __await__(self): # -> Generator[Never, Any, GetCustomDomainResult]:
        ...
    


def get_custom_domain(custom_domain_name: Optional[_builtins.str] = ..., endpoint_name: Optional[_builtins.str] = ..., profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCustomDomainResult:
    
    ...

def get_custom_domain_output(custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCustomDomainResult]:
    
    ...

