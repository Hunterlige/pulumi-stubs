

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSupportedInstanceTypesResult', 'AwaitableGetSupportedInstanceTypesResult', 'get_supported_instance_types', 'get_supported_instance_types_output']
@pulumi.output_type
class GetSupportedInstanceTypesResult:
    
    def __init__(__self__, id=..., region=..., release_label=..., supported_instance_types=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedInstanceTypes")
    def supported_instance_types(self) -> Sequence[outputs.GetSupportedInstanceTypesSupportedInstanceTypeResult]:
        
        ...
    


class AwaitableGetSupportedInstanceTypesResult(GetSupportedInstanceTypesResult):
    def __await__(self): # -> Generator[Never, Any, GetSupportedInstanceTypesResult]:
        ...
    


def get_supported_instance_types(region: Optional[_builtins.str] = ..., release_label: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSupportedInstanceTypesResult:
    
    ...

def get_supported_instance_types_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., release_label: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSupportedInstanceTypesResult]:
    
    ...

