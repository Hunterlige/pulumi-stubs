import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProjectCmekSettingsResult",
    "AwaitableGetProjectCmekSettingsResult",
    "get_project_cmek_settings",
    "get_project_cmek_settings_output",
]

@pulumi.output_type
class GetProjectCmekSettingsResult:
    def __init__(
        __self__,
        id=...,
        kms_key_name=...,
        kms_key_version_name=...,
        name=...,
        project=...,
        service_account_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> _builtins.str: ...

class AwaitableGetProjectCmekSettingsResult(GetProjectCmekSettingsResult):
    def __await__(self): ...

def get_project_cmek_settings(
    kms_key_name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProjectCmekSettingsResult: ...
def get_project_cmek_settings_output(
    kms_key_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProjectCmekSettingsResult]: ...
