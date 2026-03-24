

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEnvironmentsResult', 'AwaitableGetEnvironmentsResult', 'get_environments', 'get_environments_output']
@pulumi.output_type
class GetEnvironmentsResult:
    
    def __init__(__self__, application_id=..., environment_ids=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentIds")
    def environment_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetEnvironmentsResult(GetEnvironmentsResult):
    def __await__(self): # -> Generator[Never, Any, GetEnvironmentsResult]:
        ...
    


def get_environments(application_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEnvironmentsResult:
    
    ...

def get_environments_output(application_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEnvironmentsResult]:
    
    ...

