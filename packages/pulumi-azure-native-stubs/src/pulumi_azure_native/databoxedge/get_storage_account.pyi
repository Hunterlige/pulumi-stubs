import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStorageAccountResult",
    "AwaitableGetStorageAccountResult",
    "get_storage_account",
    "get_storage_account_output",
]

@pulumi.output_type
class GetStorageAccountResult:
    def __init__(
        __self__,
        azure_api_version=...,
        blob_endpoint=...,
        container_count=...,
        data_policy=...,
        description=...,
        id=...,
        name=...,
        storage_account_credential_id=...,
        storage_account_status=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="blobEndpoint")
    def blob_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerCount")
    def container_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dataPolicy")
    def data_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountStatus")
    def storage_account_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetStorageAccountResult(GetStorageAccountResult):
    def __await__(self): ...

def get_storage_account(
    device_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    storage_account_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStorageAccountResult: ...
def get_storage_account_output(
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStorageAccountResult]: ...
