

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetKeyHandlesResult', 'AwaitableGetKeyHandlesResult', 'get_key_handles', 'get_key_handles_output']
@pulumi.output_type
class GetKeyHandlesResult:
    
    def __init__(__self__, id=..., key_handles=..., location=..., project=..., resource_type_selector=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyHandles")
    def key_handles(self) -> Sequence[outputs.GetKeyHandlesKeyHandleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypeSelector")
    def resource_type_selector(self) -> _builtins.str:
        
        ...
    


class AwaitableGetKeyHandlesResult(GetKeyHandlesResult):
    def __await__(self): # -> Generator[Never, Any, GetKeyHandlesResult]:
        ...
    


def get_key_handles(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., resource_type_selector: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetKeyHandlesResult:
    
    ...

def get_key_handles_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_type_selector: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetKeyHandlesResult]:
    
    ...

