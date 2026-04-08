import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMonitorDefaultApplicationKeyResult",
    "AwaitableGetMonitorDefaultApplicationKeyResult",
    "get_monitor_default_application_key",
    "get_monitor_default_application_key_output",
]

@pulumi.output_type
class GetMonitorDefaultApplicationKeyResult:
    def __init__(__self__, created_by=..., key=..., name=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

class AwaitableGetMonitorDefaultApplicationKeyResult(
    GetMonitorDefaultApplicationKeyResult
):
    def __await__(self): ...

def get_monitor_default_application_key(
    monitor_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMonitorDefaultApplicationKeyResult: ...
def get_monitor_default_application_key_output(
    monitor_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMonitorDefaultApplicationKeyResult]: ...
