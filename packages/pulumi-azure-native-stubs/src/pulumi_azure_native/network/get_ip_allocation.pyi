

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIpAllocationResult', 'AwaitableGetIpAllocationResult', 'get_ip_allocation', 'get_ip_allocation_output']
@pulumi.output_type
class GetIpAllocationResult:
    
    def __init__(__self__, allocation_tags=..., azure_api_version=..., etag=..., id=..., ipam_allocation_id=..., location=..., name=..., prefix=..., prefix_length=..., prefix_type=..., subnet=..., tags=..., type=..., virtual_network=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationTags")
    def allocation_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamAllocationId")
    def ipam_allocation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixLength")
    def prefix_length(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixType")
    def prefix_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> outputs.SubResourceResponse:
        
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
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> outputs.SubResourceResponse:
        
        ...
    


class AwaitableGetIpAllocationResult(GetIpAllocationResult):
    def __await__(self): # -> Generator[Never, Any, GetIpAllocationResult]:
        ...
    


def get_ip_allocation(expand: Optional[_builtins.str] = ..., ip_allocation_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIpAllocationResult:
    
    ...

def get_ip_allocation_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., ip_allocation_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIpAllocationResult]:
    
    ...

