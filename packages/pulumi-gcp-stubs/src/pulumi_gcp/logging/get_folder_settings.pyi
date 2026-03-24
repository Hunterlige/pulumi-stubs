import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFolderSettingsResult",
    "AwaitableGetFolderSettingsResult",
    "get_folder_settings",
    "get_folder_settings_output",
]

@pulumi.output_type
class GetFolderSettingsResult:
    def __init__(
        __self__,
        disable_default_sink=...,
        folder=...,
        id=...,
        kms_key_name=...,
        kms_service_account_id=...,
        logging_service_account_id=...,
        name=...,
        storage_location=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def folder(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsServiceAccountId")
    def kms_service_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="loggingServiceAccountId")
    def logging_service_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> _builtins.str: ...

class AwaitableGetFolderSettingsResult(GetFolderSettingsResult):
    def __await__(self): ...

def get_folder_settings(
    folder: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetFolderSettingsResult: ...
def get_folder_settings_output(
    folder: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFolderSettingsResult]: ...
