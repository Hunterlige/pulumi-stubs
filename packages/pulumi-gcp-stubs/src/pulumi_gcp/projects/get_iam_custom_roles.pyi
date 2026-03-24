

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIamCustomRolesResult', 'AwaitableGetIamCustomRolesResult', 'get_iam_custom_roles', 'get_iam_custom_roles_output']
@pulumi.output_type
class GetIamCustomRolesResult:
    
    def __init__(__self__, id=..., project=..., roles=..., show_deleted=..., view=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Sequence[outputs.GetIamCustomRolesRoleResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="showDeleted")
    def show_deleted(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def view(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetIamCustomRolesResult(GetIamCustomRolesResult):
    def __await__(self): # -> Generator[Never, Any, GetIamCustomRolesResult]:
        ...
    


def get_iam_custom_roles(project: Optional[_builtins.str] = ..., show_deleted: Optional[_builtins.bool] = ..., view: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIamCustomRolesResult:
    
    ...

def get_iam_custom_roles_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., show_deleted: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., view: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIamCustomRolesResult]:
    
    ...

