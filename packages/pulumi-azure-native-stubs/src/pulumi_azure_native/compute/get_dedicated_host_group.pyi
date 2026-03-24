

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDedicatedHostGroupResult', 'AwaitableGetDedicatedHostGroupResult', 'get_dedicated_host_group', 'get_dedicated_host_group_output']
@pulumi.output_type
class GetDedicatedHostGroupResult:
    
    def __init__(__self__, additional_capabilities=..., azure_api_version=..., hosts=..., id=..., instance_view=..., location=..., name=..., platform_fault_domain_count=..., support_automatic_placement=..., system_data=..., tags=..., type=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional[outputs.DedicatedHostGroupPropertiesAdditionalCapabilitiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Sequence[outputs.SubResourceReadOnlyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.DedicatedHostGroupInstanceViewResponse:
        
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
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportAutomaticPlacement")
    def support_automatic_placement(self) -> Optional[_builtins.bool]:
        
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
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetDedicatedHostGroupResult(GetDedicatedHostGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetDedicatedHostGroupResult]:
        ...
    


def get_dedicated_host_group(expand: Optional[_builtins.str] = ..., host_group_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDedicatedHostGroupResult:
    
    ...

def get_dedicated_host_group_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., host_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDedicatedHostGroupResult]:
    
    ...

