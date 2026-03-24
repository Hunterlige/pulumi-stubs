

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAttachedVersionsResult', 'AwaitableGetAttachedVersionsResult', 'get_attached_versions', 'get_attached_versions_output']
@pulumi.output_type
class GetAttachedVersionsResult:
    
    def __init__(__self__, id=..., location=..., project=..., valid_versions=...) -> None:
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
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validVersions")
    def valid_versions(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetAttachedVersionsResult(GetAttachedVersionsResult):
    def __await__(self): # -> Generator[Never, Any, GetAttachedVersionsResult]:
        ...
    


def get_attached_versions(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAttachedVersionsResult:
    
    ...

def get_attached_versions_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAttachedVersionsResult]:
    
    ...

