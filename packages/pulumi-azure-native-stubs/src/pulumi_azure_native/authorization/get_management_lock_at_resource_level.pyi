import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagementLockAtResourceLevelResult",
    "AwaitableGetManagementLockAtResourceLevelResult",
    "get_management_lock_at_resource_level",
    "get_management_lock_at_resource_level_output",
]

@pulumi.output_type
class GetManagementLockAtResourceLevelResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        level=...,
        name=...,
        notes=...,
        owners=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def owners(self) -> Optional[Sequence[outputs.ManagementLockOwnerResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetManagementLockAtResourceLevelResult(
    GetManagementLockAtResourceLevelResult
):
    def __await__(self): ...

def get_management_lock_at_resource_level(
    api_version: Optional[_builtins.str] = ...,
    lock_name: Optional[_builtins.str] = ...,
    parent_resource_path: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    resource_provider_namespace: Optional[_builtins.str] = ...,
    resource_type: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagementLockAtResourceLevelResult: ...
def get_management_lock_at_resource_level_output(
    api_version: Optional[pulumi.Input[_builtins.str]] = ...,
    lock_name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent_resource_path: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_provider_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagementLockAtResourceLevelResult]: ...
