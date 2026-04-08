import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPowerShell72ModuleResult",
    "AwaitableGetPowerShell72ModuleResult",
    "get_power_shell72_module",
    "get_power_shell72_module_output",
]

@pulumi.output_type
class GetPowerShell72ModuleResult:
    def __init__(
        __self__,
        activity_count=...,
        azure_api_version=...,
        creation_time=...,
        description=...,
        error=...,
        etag=...,
        id=...,
        is_composite=...,
        is_global=...,
        last_modified_time=...,
        location=...,
        name=...,
        provisioning_state=...,
        size_in_bytes=...,
        tags=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activityCount")
    def activity_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ModuleErrorInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isComposite")
    def is_composite(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

class AwaitableGetPowerShell72ModuleResult(GetPowerShell72ModuleResult):
    def __await__(self): ...

def get_power_shell72_module(
    automation_account_name: Optional[_builtins.str] = ...,
    module_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPowerShell72ModuleResult: ...
def get_power_shell72_module_output(
    automation_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    module_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPowerShell72ModuleResult]: ...
