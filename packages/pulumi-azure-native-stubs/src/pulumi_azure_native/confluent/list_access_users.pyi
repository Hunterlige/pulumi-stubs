

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListAccessUsersResult', 'AwaitableListAccessUsersResult', 'list_access_users', 'list_access_users_output']
@pulumi.output_type
class ListAccessUsersResult:
    
    def __init__(__self__, data=..., kind=..., metadata=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[Sequence[outputs.UserRecordResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.ConfluentListMetadataResponse]:
        
        ...
    


class AwaitableListAccessUsersResult(ListAccessUsersResult):
    def __await__(self): # -> Generator[Never, Any, ListAccessUsersResult]:
        ...
    


def list_access_users(organization_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., search_filters: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListAccessUsersResult:
    
    ...

def list_access_users_output(organization_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., search_filters: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListAccessUsersResult]:
    
    ...

