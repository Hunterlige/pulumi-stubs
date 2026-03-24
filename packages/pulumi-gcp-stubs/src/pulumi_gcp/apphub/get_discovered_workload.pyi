

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDiscoveredWorkloadResult', 'AwaitableGetDiscoveredWorkloadResult', 'get_discovered_workload', 'get_discovered_workload_output']
@pulumi.output_type
class GetDiscoveredWorkloadResult:
    
    def __init__(__self__, id=..., location=..., name=..., project=..., workload_properties=..., workload_references=..., workload_uri=...) -> None:
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
    @pulumi.getter(name="workloadProperties")
    def workload_properties(self) -> Sequence[outputs.GetDiscoveredWorkloadWorkloadPropertyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadReferences")
    def workload_references(self) -> Sequence[outputs.GetDiscoveredWorkloadWorkloadReferenceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadUri")
    def workload_uri(self) -> _builtins.str:
        ...
    


class AwaitableGetDiscoveredWorkloadResult(GetDiscoveredWorkloadResult):
    def __await__(self): # -> Generator[Never, Any, GetDiscoveredWorkloadResult]:
        ...
    


def get_discovered_workload(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., workload_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDiscoveredWorkloadResult:
    
    ...

def get_discovered_workload_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., workload_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDiscoveredWorkloadResult]:
    
    ...

