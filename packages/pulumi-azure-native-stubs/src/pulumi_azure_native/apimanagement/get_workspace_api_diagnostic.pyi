import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkspaceApiDiagnosticResult",
    "AwaitableGetWorkspaceApiDiagnosticResult",
    "get_workspace_api_diagnostic",
    "get_workspace_api_diagnostic_output",
]

@pulumi.output_type
class GetWorkspaceApiDiagnosticResult:
    def __init__(
        __self__,
        always_log=...,
        azure_api_version=...,
        backend=...,
        frontend=...,
        http_correlation_protocol=...,
        id=...,
        log_client_ip=...,
        logger_id=...,
        metrics=...,
        name=...,
        operation_name_format=...,
        sampling=...,
        type=...,
        verbosity=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alwaysLog")
    def always_log(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def backend(self) -> Optional[outputs.PipelineDiagnosticSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def frontend(self) -> Optional[outputs.PipelineDiagnosticSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="httpCorrelationProtocol")
    def http_correlation_protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logClientIp")
    def log_client_ip(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="loggerId")
    def logger_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="operationNameFormat")
    def operation_name_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sampling(self) -> Optional[outputs.SamplingSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def verbosity(self) -> Optional[_builtins.str]: ...

class AwaitableGetWorkspaceApiDiagnosticResult(GetWorkspaceApiDiagnosticResult):
    def __await__(self): ...

def get_workspace_api_diagnostic(
    api_id: Optional[_builtins.str] = ...,
    diagnostic_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    workspace_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkspaceApiDiagnosticResult: ...
def get_workspace_api_diagnostic_output(
    api_id: Optional[pulumi.Input[_builtins.str]] = ...,
    diagnostic_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkspaceApiDiagnosticResult]: ...
