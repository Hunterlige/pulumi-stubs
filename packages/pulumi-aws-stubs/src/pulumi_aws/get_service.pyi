

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServiceResult', 'AwaitableGetServiceResult', 'get_service', 'get_service_output']
@pulumi.output_type
class GetServiceResult:
    
    def __init__(__self__, dns_name=..., id=..., partition=..., region=..., reverse_dns_name=..., reverse_dns_prefix=..., service_id=..., supported=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def partition(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseDnsName")
    def reverse_dns_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseDnsPrefix")
    def reverse_dns_prefix(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def supported(self) -> _builtins.bool:
        
        ...
    


class AwaitableGetServiceResult(GetServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetServiceResult]:
        ...
    


def get_service(dns_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., reverse_dns_name: Optional[_builtins.str] = ..., reverse_dns_prefix: Optional[_builtins.str] = ..., service_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServiceResult:
    
    ...

def get_service_output(dns_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., reverse_dns_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., reverse_dns_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., service_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServiceResult]:
    
    ...

