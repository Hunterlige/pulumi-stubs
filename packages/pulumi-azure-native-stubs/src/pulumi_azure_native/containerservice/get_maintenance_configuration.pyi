import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMaintenanceConfigurationResult",
    "AwaitableGetMaintenanceConfigurationResult",
    "get_maintenance_configuration",
    "get_maintenance_configuration_output",
]

@pulumi.output_type
class GetMaintenanceConfigurationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        maintenance_window=...,
        name=...,
        not_allowed_time=...,
        system_data=...,
        time_in_week=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[outputs.MaintenanceWindowResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="notAllowedTime")
    def not_allowed_time(self) -> Optional[Sequence[outputs.TimeSpanResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="timeInWeek")
    def time_in_week(self) -> Optional[Sequence[outputs.TimeInWeekResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetMaintenanceConfigurationResult(GetMaintenanceConfigurationResult):
    def __await__(self): ...

def get_maintenance_configuration(
    config_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMaintenanceConfigurationResult: ...
def get_maintenance_configuration_output(
    config_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMaintenanceConfigurationResult]: ...
