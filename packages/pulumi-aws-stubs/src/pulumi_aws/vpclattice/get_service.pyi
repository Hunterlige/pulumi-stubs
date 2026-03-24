

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServiceResult', 'AwaitableGetServiceResult', 'get_service', 'get_service_output']
@pulumi.output_type
class GetServiceResult:
    
    def __init__(__self__, arn=..., auth_type=..., certificate_arn=..., custom_domain_name=..., dns_entries=..., id=..., name=..., region=..., service_identifier=..., status=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(self) -> Sequence[outputs.GetServiceDnsEntryResult]:
        
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
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetServiceResult(GetServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetServiceResult]:
        ...
    


def get_service(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., service_identifier: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServiceResult:
    
    ...

def get_service_output(name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., service_identifier: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServiceResult]:
    
    ...

