

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOutpostInstanceTypesResult', 'AwaitableGetOutpostInstanceTypesResult', 'get_outpost_instance_types', 'get_outpost_instance_types_output']
@pulumi.output_type
class GetOutpostInstanceTypesResult:
    
    def __init__(__self__, arn=..., id=..., instance_types=..., region=...) -> None:
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
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetOutpostInstanceTypesResult(GetOutpostInstanceTypesResult):
    def __await__(self): # -> Generator[Never, Any, GetOutpostInstanceTypesResult]:
        ...
    


def get_outpost_instance_types(arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOutpostInstanceTypesResult:
    
    ...

def get_outpost_instance_types_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOutpostInstanceTypesResult]:
    
    ...

