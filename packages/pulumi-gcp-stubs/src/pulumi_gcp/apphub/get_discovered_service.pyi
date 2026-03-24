

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDiscoveredServiceResult', 'AwaitableGetDiscoveredServiceResult', 'get_discovered_service', 'get_discovered_service_output']
@pulumi.output_type
class GetDiscoveredServiceResult:
    
    def __init__(__self__, id=..., location=..., name=..., project=..., service_properties=..., service_references=..., service_uri=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProperties")
    def service_properties(self) -> Sequence[outputs.GetDiscoveredServiceServicePropertyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceReferences")
    def service_references(self) -> Sequence[outputs.GetDiscoveredServiceServiceReferenceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> _builtins.str:
        ...
    


class AwaitableGetDiscoveredServiceResult(GetDiscoveredServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetDiscoveredServiceResult]:
        ...
    


def get_discovered_service(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., service_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDiscoveredServiceResult:
    
    ...

def get_discovered_service_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., service_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDiscoveredServiceResult]:
    
    ...

