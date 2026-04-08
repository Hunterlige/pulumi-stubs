import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListIntegrationAccountKeyVaultKeysResult",
    "AwaitableListIntegrationAccountKeyVaultKeysResult",
    "list_integration_account_key_vault_keys",
    "list_integration_account_key_vault_keys_output",
]

@pulumi.output_type
class ListIntegrationAccountKeyVaultKeysResult:
    def __init__(__self__, skip_token=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.KeyVaultKeyResponse]]: ...

class AwaitableListIntegrationAccountKeyVaultKeysResult(
    ListIntegrationAccountKeyVaultKeysResult
):
    def __await__(self): ...

def list_integration_account_key_vault_keys(
    integration_account_name: Optional[_builtins.str] = ...,
    key_vault: Optional[Union[KeyVaultReference, KeyVaultReferenceDict]] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    skip_token: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListIntegrationAccountKeyVaultKeysResult: ...
def list_integration_account_key_vault_keys_output(
    integration_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    key_vault: Optional[
        pulumi.Input[Union[KeyVaultReference, KeyVaultReferenceDict]]
    ] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListIntegrationAccountKeyVaultKeysResult]: ...
