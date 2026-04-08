import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListStorageAccountSASResult",
    "AwaitableListStorageAccountSASResult",
    "list_storage_account_sas",
    "list_storage_account_sas_output",
]

@pulumi.output_type
class ListStorageAccountSASResult:
    def __init__(__self__, account_sas_token=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountSasToken")
    def account_sas_token(self) -> _builtins.str: ...

class AwaitableListStorageAccountSASResult(ListStorageAccountSASResult):
    def __await__(self): ...

def list_storage_account_sas(
    account_name: Optional[_builtins.str] = ...,
    i_p_address_or_range: Optional[_builtins.str] = ...,
    key_to_sign: Optional[_builtins.str] = ...,
    permissions: Optional[Union[_builtins.str, Permissions]] = ...,
    protocols: Optional[HttpProtocol] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_types: Optional[Union[_builtins.str, SignedResourceTypes]] = ...,
    services: Optional[Union[_builtins.str, Services]] = ...,
    shared_access_expiry_time: Optional[_builtins.str] = ...,
    shared_access_start_time: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListStorageAccountSASResult: ...
def list_storage_account_sas_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    i_p_address_or_range: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    key_to_sign: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    permissions: Optional[pulumi.Input[Union[_builtins.str, Permissions]]] = ...,
    protocols: Optional[pulumi.Input[Optional[HttpProtocol]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_types: Optional[
        pulumi.Input[Union[_builtins.str, SignedResourceTypes]]
    ] = ...,
    services: Optional[pulumi.Input[Union[_builtins.str, Services]]] = ...,
    shared_access_expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
    shared_access_start_time: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListStorageAccountSASResult]: ...
