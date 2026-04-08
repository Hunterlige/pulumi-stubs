import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceApiDiagnosticArgs", "WorkspaceApiDiagnostic"]

@pulumi.input_type
class WorkspaceApiDiagnosticArgs:
    def __init__(
        __self__,
        *,
        api_id: pulumi.Input[_builtins.str],
        logger_id: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        workspace_id: pulumi.Input[_builtins.str],
        always_log: Optional[pulumi.Input[Union[_builtins.str, AlwaysLog]]] = ...,
        backend: Optional[pulumi.Input[PipelineDiagnosticSettingsArgs]] = ...,
        diagnostic_id: Optional[pulumi.Input[_builtins.str]] = ...,
        frontend: Optional[pulumi.Input[PipelineDiagnosticSettingsArgs]] = ...,
        http_correlation_protocol: Optional[
            pulumi.Input[Union[_builtins.str, HttpCorrelationProtocol]]
        ] = ...,
        log_client_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        metrics: Optional[pulumi.Input[_builtins.bool]] = ...,
        operation_name_format: Optional[
            pulumi.Input[Union[_builtins.str, OperationNameFormat]]
        ] = ...,
        sampling: Optional[pulumi.Input[SamplingSettingsArgs]] = ...,
        verbosity: Optional[pulumi.Input[Union[_builtins.str, Verbosity]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]: ...
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="loggerId")
    def logger_id(self) -> pulumi.Input[_builtins.str]: ...
    @logger_id.setter
    def logger_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="alwaysLog")
    def always_log(self) -> Optional[pulumi.Input[Union[_builtins.str, AlwaysLog]]]: ...
    @always_log.setter
    def always_log(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AlwaysLog]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def backend(self) -> Optional[pulumi.Input[PipelineDiagnosticSettingsArgs]]: ...
    @backend.setter
    def backend(
        self, value: Optional[pulumi.Input[PipelineDiagnosticSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diagnosticId")
    def diagnostic_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @diagnostic_id.setter
    def diagnostic_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def frontend(self) -> Optional[pulumi.Input[PipelineDiagnosticSettingsArgs]]: ...
    @frontend.setter
    def frontend(
        self, value: Optional[pulumi.Input[PipelineDiagnosticSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpCorrelationProtocol")
    def http_correlation_protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HttpCorrelationProtocol]]]: ...
    @http_correlation_protocol.setter
    def http_correlation_protocol(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, HttpCorrelationProtocol]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logClientIp")
    def log_client_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @log_client_ip.setter
    def log_client_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="operationNameFormat")
    def operation_name_format(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OperationNameFormat]]]: ...
    @operation_name_format.setter
    def operation_name_format(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OperationNameFormat]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sampling(self) -> Optional[pulumi.Input[SamplingSettingsArgs]]: ...
    @sampling.setter
    def sampling(self, value: Optional[pulumi.Input[SamplingSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def verbosity(self) -> Optional[pulumi.Input[Union[_builtins.str, Verbosity]]]: ...
    @verbosity.setter
    def verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Verbosity]]]
    ): ...

@pulumi.type_token("azure-native:apimanagement:WorkspaceApiDiagnostic")
class WorkspaceApiDiagnostic(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        always_log: Optional[pulumi.Input[Union[_builtins.str, AlwaysLog]]] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        backend: Optional[
            pulumi.Input[
                Union[
                    PipelineDiagnosticSettingsArgs, PipelineDiagnosticSettingsArgsDict
                ]
            ]
        ] = ...,
        diagnostic_id: Optional[pulumi.Input[_builtins.str]] = ...,
        frontend: Optional[
            pulumi.Input[
                Union[
                    PipelineDiagnosticSettingsArgs, PipelineDiagnosticSettingsArgsDict
                ]
            ]
        ] = ...,
        http_correlation_protocol: Optional[
            pulumi.Input[Union[_builtins.str, HttpCorrelationProtocol]]
        ] = ...,
        log_client_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        logger_id: Optional[pulumi.Input[_builtins.str]] = ...,
        metrics: Optional[pulumi.Input[_builtins.bool]] = ...,
        operation_name_format: Optional[
            pulumi.Input[Union[_builtins.str, OperationNameFormat]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sampling: Optional[
            pulumi.Input[Union[SamplingSettingsArgs, SamplingSettingsArgsDict]]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        verbosity: Optional[pulumi.Input[Union[_builtins.str, Verbosity]]] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkspaceApiDiagnosticArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WorkspaceApiDiagnostic: ...
    @_builtins.property
    @pulumi.getter(name="alwaysLog")
    def always_log(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def backend(
        self,
    ) -> pulumi.Output[Optional[outputs.PipelineDiagnosticSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def frontend(
        self,
    ) -> pulumi.Output[Optional[outputs.PipelineDiagnosticSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="httpCorrelationProtocol")
    def http_correlation_protocol(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logClientIp")
    def log_client_ip(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="loggerId")
    def logger_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationNameFormat")
    def operation_name_format(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def sampling(self) -> pulumi.Output[Optional[outputs.SamplingSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def verbosity(self) -> pulumi.Output[Optional[_builtins.str]]: ...
