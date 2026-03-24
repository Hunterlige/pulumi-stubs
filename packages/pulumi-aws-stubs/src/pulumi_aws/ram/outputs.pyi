import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PermissionTimeouts",
    "ResourceShareResourceShareConfiguration",
    "GetResourceShareFilterResult",
]

@pulumi.output_type
class PermissionTimeouts(dict):
    def __init__(__self__, *, delete: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceShareResourceShareConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        retain_sharing_on_account_leave_organization: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retainSharingOnAccountLeaveOrganization")
    def retain_sharing_on_account_leave_organization(
        self,
    ) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GetResourceShareFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
