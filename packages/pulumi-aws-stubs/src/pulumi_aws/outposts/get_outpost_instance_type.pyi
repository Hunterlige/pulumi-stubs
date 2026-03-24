

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOutpostInstanceTypeResult', 'AwaitableGetOutpostInstanceTypeResult', 'get_outpost_instance_type', 'get_outpost_instance_type_output']
@pulumi.output_type
class GetOutpostInstanceTypeResult:
    
    def __init__(__self__, arn=..., id=..., instance_type=..., preferred_instance_types=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredInstanceTypes")
    def preferred_instance_types(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetOutpostInstanceTypeResult(GetOutpostInstanceTypeResult):
    def __await__(self): # -> Generator[Never, Any, GetOutpostInstanceTypeResult]:
        ...
    


def get_outpost_instance_type(arn: Optional[_builtins.str] = ..., instance_type: Optional[_builtins.str] = ..., preferred_instance_types: Optional[Sequence[_builtins.str]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOutpostInstanceTypeResult:
    
    ...

def get_outpost_instance_type_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., preferred_instance_types: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOutpostInstanceTypeResult]:
    
    ...

