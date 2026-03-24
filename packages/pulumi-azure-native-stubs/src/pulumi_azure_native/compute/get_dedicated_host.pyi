

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDedicatedHostResult', 'AwaitableGetDedicatedHostResult', 'get_dedicated_host', 'get_dedicated_host_output']
@pulumi.output_type
class GetDedicatedHostResult:
    
    def __init__(__self__, auto_replace_on_failure=..., azure_api_version=..., host_id=..., id=..., instance_view=..., license_type=..., location=..., name=..., platform_fault_domain=..., provisioning_state=..., provisioning_time=..., sku=..., system_data=..., tags=..., time_created=..., type=..., virtual_machines=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoReplaceOnFailure")
    def auto_replace_on_failure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.DedicatedHostInstanceViewResponse:
        
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
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformFaultDomain")
    def platform_fault_domain(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningTime")
    def provisioning_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
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
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(self) -> Sequence[outputs.SubResourceReadOnlyResponse]:
        
        ...
    


class AwaitableGetDedicatedHostResult(GetDedicatedHostResult):
    def __await__(self): # -> Generator[Never, Any, GetDedicatedHostResult]:
        ...
    


def get_dedicated_host(expand: Optional[_builtins.str] = ..., host_group_name: Optional[_builtins.str] = ..., host_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDedicatedHostResult:
    
    ...

def get_dedicated_host_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., host_group_name: Optional[pulumi.Input[_builtins.str]] = ..., host_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDedicatedHostResult]:
    
    ...

