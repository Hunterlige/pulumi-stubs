import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectionMonitorResult",
    "AwaitableGetConnectionMonitorResult",
    "get_connection_monitor",
    "get_connection_monitor_output",
]

@pulumi.output_type
class GetConnectionMonitorResult:
    def __init__(
        __self__,
        auto_start=...,
        azure_api_version=...,
        connection_monitor_type=...,
        destination=...,
        endpoints=...,
        etag=...,
        id=...,
        location=...,
        monitoring_interval_in_seconds=...,
        monitoring_status=...,
        name=...,
        notes=...,
        outputs=...,
        provisioning_state=...,
        source=...,
        start_time=...,
        tags=...,
        test_configurations=...,
        test_groups=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoStart")
    def auto_start(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionMonitorType")
    def connection_monitor_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[outputs.ConnectionMonitorDestinationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[Sequence[outputs.ConnectionMonitorEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringIntervalInSeconds")
    def monitoring_interval_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[Sequence[outputs.ConnectionMonitorOutputResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[outputs.ConnectionMonitorSourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="testConfigurations")
    def test_configurations(
        self,
    ) -> Optional[Sequence[outputs.ConnectionMonitorTestConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="testGroups")
    def test_groups(
        self,
    ) -> Optional[Sequence[outputs.ConnectionMonitorTestGroupResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetConnectionMonitorResult(GetConnectionMonitorResult):
    def __await__(self): ...

def get_connection_monitor(
    connection_monitor_name: Optional[_builtins.str] = ...,
    network_watcher_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectionMonitorResult: ...
def get_connection_monitor_output(
    connection_monitor_name: Optional[pulumi.Input[_builtins.str]] = ...,
    network_watcher_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectionMonitorResult]: ...
