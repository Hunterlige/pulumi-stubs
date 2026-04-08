import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagedMaintenanceWindowStatusResult",
    "AwaitableGetManagedMaintenanceWindowStatusResult",
    "get_managed_maintenance_window_status",
    "get_managed_maintenance_window_status_output",
]

@pulumi.output_type
class GetManagedMaintenanceWindowStatusResult:
    def __init__(
        __self__,
        can_apply_updates=...,
        is_region_ready=...,
        is_window_active=...,
        is_window_enabled=...,
        last_window_end_time_utc=...,
        last_window_start_time_utc=...,
        last_window_status_update_at_utc=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="canApplyUpdates")
    def can_apply_updates(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isRegionReady")
    def is_region_ready(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isWindowActive")
    def is_window_active(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isWindowEnabled")
    def is_window_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="lastWindowEndTimeUTC")
    def last_window_end_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastWindowStartTimeUTC")
    def last_window_start_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastWindowStatusUpdateAtUTC")
    def last_window_status_update_at_utc(self) -> _builtins.str: ...

class AwaitableGetManagedMaintenanceWindowStatusResult(
    GetManagedMaintenanceWindowStatusResult
):
    def __await__(self): ...

def get_managed_maintenance_window_status(
    cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagedMaintenanceWindowStatusResult: ...
def get_managed_maintenance_window_status_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagedMaintenanceWindowStatusResult]: ...
