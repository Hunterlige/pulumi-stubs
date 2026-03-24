import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstanceMaintenancePolicyArgs",
    "InstanceMaintenancePolicyArgsDict",
    ...,
    ...,
    ...,
    ...,
    "InstanceMaintenanceScheduleArgs",
    "InstanceMaintenanceScheduleArgsDict",
    "InstanceMemcacheNodeArgs",
    "InstanceMemcacheNodeArgsDict",
    "InstanceMemcacheParametersArgs",
    "InstanceMemcacheParametersArgsDict",
    "InstanceNodeConfigArgs",
    "InstanceNodeConfigArgsDict",
]

class InstanceMaintenancePolicyArgsDict(TypedDict):
    weekly_maintenance_windows: pulumi.Input[
        Sequence[pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgsDict]]
    ]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceMaintenancePolicyArgs:
    def __init__(
        __self__,
        *,
        weekly_maintenance_windows: pulumi.Input[
            Sequence[pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs]]
        ],
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs]]
    ]: ...
    @weekly_maintenance_windows.setter
    def weekly_maintenance_windows(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceMaintenancePolicyWeeklyMaintenanceWindowArgsDict(TypedDict):
    day: pulumi.Input[_builtins.str]
    duration: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[
        InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgsDict
    ]
    ...

@pulumi.input_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        day: pulumi.Input[_builtins.str],
        duration: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[
            InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.str]: ...
    @day.setter
    def day(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[_builtins.str]: ...
    @duration.setter
    def duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> pulumi.Input[
        InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs
    ]: ...
    @start_time.setter
    def start_time(
        self,
        value: pulumi.Input[
            InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs
        ],
    ): ...

class InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceMaintenanceScheduleArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    schedule_deadline_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceMaintenanceScheduleArgs:
    def __init__(
        __self__,
        *,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_deadline_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_deadline_time.setter
    def schedule_deadline_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceMemcacheNodeArgsDict(TypedDict):
    host: NotRequired[pulumi.Input[_builtins.str]]
    node_id: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceMemcacheNodeArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        node_id: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_id.setter
    def node_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceMemcacheParametersArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class InstanceMemcacheParametersArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def params(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @params.setter
    def params(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class InstanceNodeConfigArgsDict(TypedDict):
    cpu_count: pulumi.Input[_builtins.int]
    memory_size_mb: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class InstanceNodeConfigArgs:
    def __init__(
        __self__,
        *,
        cpu_count: pulumi.Input[_builtins.int],
        memory_size_mb: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> pulumi.Input[_builtins.int]: ...
    @cpu_count.setter
    def cpu_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="memorySizeMb")
    def memory_size_mb(self) -> pulumi.Input[_builtins.int]: ...
    @memory_size_mb.setter
    def memory_size_mb(self, value: pulumi.Input[_builtins.int]): ...
