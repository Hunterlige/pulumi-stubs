import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProjectSettingsResult",
    "AwaitableGetProjectSettingsResult",
    "get_project_settings",
    "get_project_settings_output",
]

@pulumi.output_type
class GetProjectSettingsResult:
    def __init__(
        __self__,
        disable_default_sink=...,
        id=...,
        kms_key_name=...,
        kms_service_account_id=...,
        logging_service_account_id=...,
        name=...,
        project=...,
        storage_location=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> _builtins.bool: ...
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
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> _builtins.str: ...

class AwaitableGetProjectSettingsResult(GetProjectSettingsResult):
    def __await__(self): ...

def get_project_settings(
    project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetProjectSettingsResult: ...
def get_project_settings_output(
    project: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProjectSettingsResult]: ...
