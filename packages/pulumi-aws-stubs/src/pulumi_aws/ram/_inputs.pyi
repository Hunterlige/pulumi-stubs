import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PermissionTimeoutsArgs",
    "PermissionTimeoutsArgsDict",
    "ResourceShareResourceShareConfigurationArgs",
    "ResourceShareResourceShareConfigurationArgsDict",
    "GetResourceShareFilterArgs",
    "GetResourceShareFilterArgsDict",
]

class PermissionTimeoutsArgsDict(TypedDict):
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PermissionTimeoutsArgs:
    def __init__(
        __self__, *, delete: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceShareResourceShareConfigurationArgsDict(TypedDict):
    retain_sharing_on_account_leave_organization: NotRequired[
        pulumi.Input[_builtins.bool]
    ]

@pulumi.input_type
class ResourceShareResourceShareConfigurationArgs:
    def __init__(
        __self__,
        *,
        retain_sharing_on_account_leave_organization: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retainSharingOnAccountLeaveOrganization")
    def retain_sharing_on_account_leave_organization(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @retain_sharing_on_account_leave_organization.setter
    def retain_sharing_on_account_leave_organization(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class GetResourceShareFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetResourceShareFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...
