import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstanceMaintenancePolicy",
    "InstanceMaintenancePolicyWeeklyMaintenanceWindow",
    ...,
    "InstanceMaintenanceSchedule",
    "InstanceMemcacheNode",
    "InstanceMemcacheParameters",
    "InstanceNodeConfig",
    "GetInstanceMaintenancePolicyResult",
    ...,
    ...,
    "GetInstanceMaintenanceScheduleResult",
    "GetInstanceMemcacheNodeResult",
    "GetInstanceMemcacheParameterResult",
    "GetInstanceNodeConfigResult",
]

@pulumi.output_type
class InstanceMaintenancePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        weekly_maintenance_windows: Sequence[
            outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindow
        ],
        create_time: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(
        self,
    ) -> Sequence[outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindow]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        duration: _builtins.str,
        start_time: outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime: ...

@pulumi.output_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InstanceMaintenanceSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time: Optional[_builtins.str] = ...,
        schedule_deadline_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceMemcacheNode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: Optional[_builtins.str] = ...,
        node_id: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        state: Optional[_builtins.str] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceMemcacheParameters(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        params: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class InstanceNodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cpu_count: _builtins.int, memory_size_mb: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeMb")
    def memory_size_mb(self) -> _builtins.int: ...

@pulumi.output_type
class GetInstanceMaintenancePolicyResult(dict):
    def __init__(
        __self__,
        *,
        create_time: _builtins.str,
        description: _builtins.str,
        update_time: _builtins.str,
        weekly_maintenance_windows: Sequence[
            outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(
        self,
    ) -> Sequence[
        outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowResult
    ]: ...

@pulumi.output_type
class GetInstanceMaintenancePolicyWeeklyMaintenanceWindowResult(dict):
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        duration: _builtins.str,
        start_times: Sequence[
            outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Sequence[
        outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult
    ]: ...

@pulumi.output_type
class GetInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult(dict):
    def __init__(
        __self__,
        *,
        hours: _builtins.int,
        minutes: _builtins.int,
        nanos: _builtins.int,
        seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetInstanceMaintenanceScheduleResult(dict):
    def __init__(
        __self__,
        *,
        end_time: _builtins.str,
        schedule_deadline_time: _builtins.str,
        start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceMemcacheNodeResult(dict):
    def __init__(
        __self__,
        *,
        host: _builtins.str,
        node_id: _builtins.str,
        port: _builtins.int,
        state: _builtins.str,
        zone: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceMemcacheParameterResult(dict):
    def __init__(
        __self__, *, id: _builtins.str, params: Mapping[str, _builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetInstanceNodeConfigResult(dict):
    def __init__(
        __self__, *, cpu_count: _builtins.int, memory_size_mb: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeMb")
    def memory_size_mb(self) -> _builtins.int: ...
