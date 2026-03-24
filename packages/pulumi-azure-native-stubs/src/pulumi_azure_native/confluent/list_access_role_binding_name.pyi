

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListAccessRoleBindingNameResult', 'AwaitableListAccessRoleBindingNameResult', 'list_access_role_binding_name', 'list_access_role_binding_name_output']
@pulumi.output_type
class ListAccessRoleBindingNameResult:
    
    def __init__(__self__, data=..., kind=..., metadata=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.ConfluentListMetadataResponse]:
        
        ...
    


class AwaitableListAccessRoleBindingNameResult(ListAccessRoleBindingNameResult):
    def __await__(self): # -> Generator[Never, Any, ListAccessRoleBindingNameResult]:
        ...
    


def list_access_role_binding_name(organization_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., search_filters: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListAccessRoleBindingNameResult:
    
    ...

def list_access_role_binding_name_output(organization_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., search_filters: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListAccessRoleBindingNameResult]:
    
    ...

