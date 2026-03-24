import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOrganizationalUnitDescendantAccountsResult",
    ...,
    "get_organizational_unit_descendant_accounts",
    "get_organizational_unit_descendant_accounts_output",
]

@pulumi.output_type
class GetOrganizationalUnitDescendantAccountsResult:
    def __init__(__self__, accounts=..., id=..., parent_id=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accounts(
        self,
    ) -> Sequence[outputs.GetOrganizationalUnitDescendantAccountsAccountResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> _builtins.str: ...

class AwaitableGetOrganizationalUnitDescendantAccountsResult(
    GetOrganizationalUnitDescendantAccountsResult
):
    def __await__(self): ...

def get_organizational_unit_descendant_accounts(
    parent_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetOrganizationalUnitDescendantAccountsResult: ...
def get_organizational_unit_descendant_accounts_output(
    parent_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOrganizationalUnitDescendantAccountsResult]: ...
