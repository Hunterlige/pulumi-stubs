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
        default_storage_location=...,
        id=...,
        kms_key_name=...,
        location=...,
        name=...,
        project=...,
        service_account_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultStorageLocation")
    def default_storage_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> _builtins.str: ...

class AwaitableGetProjectSettingsResult(GetProjectSettingsResult):
    def __await__(self): ...

def get_project_settings(
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProjectSettingsResult: ...
def get_project_settings_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProjectSettingsResult]: ...
