import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIamCustomRoleResult",
    "AwaitableGetIamCustomRoleResult",
    "get_iam_custom_role",
    "get_iam_custom_role_output",
]

@pulumi.output_type
class GetIamCustomRoleResult:
    def __init__(
        __self__,
        deleted=...,
        description=...,
        id=...,
        name=...,
        org_id=...,
        permissions=...,
        role_id=...,
        stage=...,
        title=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleId")
    def role_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...

class AwaitableGetIamCustomRoleResult(GetIamCustomRoleResult):
    def __await__(self): ...

def get_iam_custom_role(
    org_id: Optional[_builtins.str] = ...,
    role_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIamCustomRoleResult: ...
def get_iam_custom_role_output(
    org_id: Optional[pulumi.Input[_builtins.str]] = ...,
    role_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIamCustomRoleResult]: ...
