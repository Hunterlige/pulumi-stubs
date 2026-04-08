import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListAdminKeyResult",
    "AwaitableListAdminKeyResult",
    "list_admin_key",
    "list_admin_key_output",
]

@pulumi.output_type
class ListAdminKeyResult:
    def __init__(__self__, primary_key=..., secondary_key=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> _builtins.str: ...

class AwaitableListAdminKeyResult(ListAdminKeyResult):
    def __await__(self): ...

def list_admin_key(
    resource_group_name: Optional[_builtins.str] = ...,
    search_service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListAdminKeyResult: ...
def list_admin_key_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    search_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListAdminKeyResult]: ...
