import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListStorageAccountSasTokensResult",
    "AwaitableListStorageAccountSasTokensResult",
    "list_storage_account_sas_tokens",
    "list_storage_account_sas_tokens_output",
]

@pulumi.output_type
class ListStorageAccountSasTokensResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.SasTokenInformationResponse]: ...

class AwaitableListStorageAccountSasTokensResult(ListStorageAccountSasTokensResult):
    def __await__(self): ...

def list_storage_account_sas_tokens(
    account_name: Optional[_builtins.str] = ...,
    container_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    storage_account_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListStorageAccountSasTokensResult: ...
def list_storage_account_sas_tokens_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    container_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListStorageAccountSasTokensResult]: ...
