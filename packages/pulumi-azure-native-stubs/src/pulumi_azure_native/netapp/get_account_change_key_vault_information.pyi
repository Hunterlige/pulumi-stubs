import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAccountChangeKeyVaultInformationResult",
    "AwaitableGetAccountChangeKeyVaultInformationResult",
    "get_account_change_key_vault_information",
    "get_account_change_key_vault_information_output",
]

@pulumi.output_type
class GetAccountChangeKeyVaultInformationResult:
    def __init__(
        __self__,
        key_name=...,
        key_vault_private_endpoints=...,
        key_vault_resource_id=...,
        key_vault_uri=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultPrivateEndpoints")
    def key_vault_private_endpoints(
        self,
    ) -> Optional[Sequence[outputs.KeyVaultPrivateEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceId")
    def key_vault_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]: ...

class AwaitableGetAccountChangeKeyVaultInformationResult(
    GetAccountChangeKeyVaultInformationResult
):
    def __await__(self): ...

def get_account_change_key_vault_information(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAccountChangeKeyVaultInformationResult: ...
def get_account_change_key_vault_information_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAccountChangeKeyVaultInformationResult]: ...
