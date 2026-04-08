import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListAccessServiceAccountsResult",
    "AwaitableListAccessServiceAccountsResult",
    "list_access_service_accounts",
    "list_access_service_accounts_output",
]

@pulumi.output_type
class ListAccessServiceAccountsResult:
    def __init__(__self__, data=..., kind=..., metadata=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[Sequence[outputs.ServiceAccountRecordResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.ConfluentListMetadataResponse]: ...

class AwaitableListAccessServiceAccountsResult(ListAccessServiceAccountsResult):
    def __await__(self): ...

def list_access_service_accounts(
    organization_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    search_filters: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListAccessServiceAccountsResult: ...
def list_access_service_accounts_output(
    organization_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    search_filters: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListAccessServiceAccountsResult]: ...
