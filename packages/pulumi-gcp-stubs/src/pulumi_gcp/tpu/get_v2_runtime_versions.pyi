

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetV2RuntimeVersionsResult', 'AwaitableGetV2RuntimeVersionsResult', 'get_v2_runtime_versions', 'get_v2_runtime_versions_output']
@pulumi.output_type
class GetV2RuntimeVersionsResult:
    
    def __init__(__self__, id=..., project=..., versions=..., zone=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        ...
    


class AwaitableGetV2RuntimeVersionsResult(GetV2RuntimeVersionsResult):
    def __await__(self): # -> Generator[Never, Any, GetV2RuntimeVersionsResult]:
        ...
    


def get_v2_runtime_versions(project: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetV2RuntimeVersionsResult:
    
    ...

def get_v2_runtime_versions_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetV2RuntimeVersionsResult]:
    
    ...

