import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDiagnosticServiceResult",
    "AwaitableGetDiagnosticServiceResult",
    "get_diagnostic_service",
    "get_diagnostic_service_output",
]

@pulumi.output_type
class GetDiagnosticServiceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_export_frequency_seconds=...,
        extended_location=...,
        id=...,
        image=...,
        location=...,
        log_format=...,
        log_level=...,
        max_data_storage_size=...,
        metrics_port=...,
        name=...,
        open_telemetry_traces_collector_addr=...,
        provisioning_state=...,
        stale_data_timeout_seconds=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataExportFrequencySeconds")
    def data_export_frequency_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationPropertyResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> outputs.ContainerImageResponse: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDataStorageSize")
    def max_data_storage_size(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="metricsPort")
    def metrics_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="openTelemetryTracesCollectorAddr")
    def open_telemetry_traces_collector_addr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="staleDataTimeoutSeconds")
    def stale_data_timeout_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDiagnosticServiceResult(GetDiagnosticServiceResult):
    def __await__(self): ...

def get_diagnostic_service(
    diagnostic_service_name: Optional[_builtins.str] = ...,
    mq_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDiagnosticServiceResult: ...
def get_diagnostic_service_output(
    diagnostic_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    mq_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDiagnosticServiceResult]: ...
