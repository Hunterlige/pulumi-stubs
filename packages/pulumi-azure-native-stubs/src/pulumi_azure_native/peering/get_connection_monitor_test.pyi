import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectionMonitorTestResult",
    "AwaitableGetConnectionMonitorTestResult",
    "get_connection_monitor_test",
    "get_connection_monitor_test_output",
]

@pulumi.output_type
class GetConnectionMonitorTestResult:
    def __init__(
        __self__,
        azure_api_version=...,
        destination=...,
        destination_port=...,
        id=...,
        is_test_successful=...,
        name=...,
        path=...,
        provisioning_state=...,
        source_agent=...,
        test_frequency_in_sec=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isTestSuccessful")
    def is_test_successful(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceAgent")
    def source_agent(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="testFrequencyInSec")
    def test_frequency_in_sec(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetConnectionMonitorTestResult(GetConnectionMonitorTestResult):
    def __await__(self): ...

def get_connection_monitor_test(
    connection_monitor_test_name: Optional[_builtins.str] = ...,
    peering_service_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectionMonitorTestResult: ...
def get_connection_monitor_test_output(
    connection_monitor_test_name: Optional[pulumi.Input[_builtins.str]] = ...,
    peering_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectionMonitorTestResult]: ...
