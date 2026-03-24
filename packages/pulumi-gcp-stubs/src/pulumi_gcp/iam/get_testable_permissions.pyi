import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTestablePermissionsResult",
    "AwaitableGetTestablePermissionsResult",
    "get_testable_permissions",
    "get_testable_permissions_output",
]

@pulumi.output_type
class GetTestablePermissionsResult:
    def __init__(
        __self__,
        custom_support_level=...,
        full_resource_name=...,
        id=...,
        permissions=...,
        stages=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customSupportLevel")
    def custom_support_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fullResourceName")
    def full_resource_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Sequence[outputs.GetTestablePermissionsPermissionResult]: ...
    @_builtins.property
    @pulumi.getter
    def stages(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetTestablePermissionsResult(GetTestablePermissionsResult):
    def __await__(self): ...

def get_testable_permissions(
    custom_support_level: Optional[_builtins.str] = ...,
    full_resource_name: Optional[_builtins.str] = ...,
    stages: Optional[Sequence[_builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTestablePermissionsResult: ...
def get_testable_permissions_output(
    custom_support_level: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    full_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    stages: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTestablePermissionsResult]: ...
