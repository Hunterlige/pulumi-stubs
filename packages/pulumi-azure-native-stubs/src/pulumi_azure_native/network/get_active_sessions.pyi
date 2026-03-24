

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetActiveSessionsResult', 'AwaitableGetActiveSessionsResult', 'get_active_sessions', 'get_active_sessions_output']
@pulumi.output_type
class GetActiveSessionsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.BastionActiveSessionResponse]]:
        
        ...
    


class AwaitableGetActiveSessionsResult(GetActiveSessionsResult):
    def __await__(self): # -> Generator[Never, Any, GetActiveSessionsResult]:
        ...
    


def get_active_sessions(bastion_host_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetActiveSessionsResult:
    
    ...

def get_active_sessions_output(bastion_host_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetActiveSessionsResult]:
    
    ...

