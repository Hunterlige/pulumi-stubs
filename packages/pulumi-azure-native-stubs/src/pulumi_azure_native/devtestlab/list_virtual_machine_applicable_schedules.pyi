import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListVirtualMachineApplicableSchedulesResult",
    ...,
    "list_virtual_machine_applicable_schedules",
    "list_virtual_machine_applicable_schedules_output",
]

@pulumi.output_type
class ListVirtualMachineApplicableSchedulesResult:
    def __init__(
        __self__,
        id=...,
        lab_vms_shutdown=...,
        lab_vms_startup=...,
        location=...,
        name=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="labVmsShutdown")
    def lab_vms_shutdown(self) -> Optional[outputs.ScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="labVmsStartup")
    def lab_vms_startup(self) -> Optional[outputs.ScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableListVirtualMachineApplicableSchedulesResult(
    ListVirtualMachineApplicableSchedulesResult
):
    def __await__(self): ...

def list_virtual_machine_applicable_schedules(
    lab_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListVirtualMachineApplicableSchedulesResult: ...
def list_virtual_machine_applicable_schedules_output(
    lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListVirtualMachineApplicableSchedulesResult]: ...
