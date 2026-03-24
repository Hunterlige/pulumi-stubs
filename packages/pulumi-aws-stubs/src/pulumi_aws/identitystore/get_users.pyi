

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUsersResult', 'AwaitableGetUsersResult', 'get_users', 'get_users_output']
@pulumi.output_type
class GetUsersResult:
    
    def __init__(__self__, id=..., identity_store_id=..., region=..., users=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> Sequence[outputs.GetUsersUserResult]:
        
        ...
    


class AwaitableGetUsersResult(GetUsersResult):
    def __await__(self): # -> Generator[Never, Any, GetUsersResult]:
        ...
    


def get_users(identity_store_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUsersResult:
    
    ...

def get_users_output(identity_store_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUsersResult]:
    
    ...

