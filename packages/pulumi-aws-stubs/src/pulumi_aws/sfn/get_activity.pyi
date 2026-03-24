

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetActivityResult', 'AwaitableGetActivityResult', 'get_activity', 'get_activity_output']
@pulumi.output_type
class GetActivityResult:
    
    def __init__(__self__, arn=..., creation_date=..., id=..., name=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str:
        
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
    


class AwaitableGetActivityResult(GetActivityResult):
    def __await__(self): # -> Generator[Never, Any, GetActivityResult]:
        ...
    


def get_activity(arn: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetActivityResult:
    
    ...

def get_activity_output(arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetActivityResult]:
    
    ...

