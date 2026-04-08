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
        name=...,
        scheduled_entries=...,
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
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduledEntries")
    def scheduled_entries(self) -> Sequence[outputs.ScheduledEntryResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetMaintenanceConfigurationResult(GetMaintenanceConfigurationResult):
    def __await__(self): ...

def get_maintenance_configuration(
    config_name: Optional[_builtins.str] = ...,
    environment_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMaintenanceConfigurationResult: ...
def get_maintenance_configuration_output(
    config_name: Optional[pulumi.Input[_builtins.str]] = ...,
    environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMaintenanceConfigurationResult]: ...
