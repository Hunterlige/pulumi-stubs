import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebAppDiagnosticLogsConfigurationArgs", "WebAppDiagnosticLogsConfiguration"]

@pulumi.input_type
class WebAppDiagnosticLogsConfigurationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        application_logs: Optional[pulumi.Input[ApplicationLogsConfigArgs]] = ...,
        detailed_error_messages: Optional[pulumi.Input[EnabledConfigArgs]] = ...,
        failed_requests_tracing: Optional[pulumi.Input[EnabledConfigArgs]] = ...,
        http_logs: Optional[pulumi.Input[HttpLogsConfigArgs]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationLogs")
    def application_logs(self) -> Optional[pulumi.Input[ApplicationLogsConfigArgs]]: ...
    @application_logs.setter
    def application_logs(
        self, value: Optional[pulumi.Input[ApplicationLogsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="detailedErrorMessages")
    def detailed_error_messages(self) -> Optional[pulumi.Input[EnabledConfigArgs]]: ...
    @detailed_error_messages.setter
    def detailed_error_messages(
        self, value: Optional[pulumi.Input[EnabledConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failedRequestsTracing")
    def failed_requests_tracing(self) -> Optional[pulumi.Input[EnabledConfigArgs]]: ...
    @failed_requests_tracing.setter
    def failed_requests_tracing(
        self, value: Optional[pulumi.Input[EnabledConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpLogs")
    def http_logs(self) -> Optional[pulumi.Input[HttpLogsConfigArgs]]: ...
    @http_logs.setter
    def http_logs(self, value: Optional[pulumi.Input[HttpLogsConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:web:WebAppDiagnosticLogsConfiguration")
class WebAppDiagnosticLogsConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_logs: Optional[
            pulumi.Input[
                Union[ApplicationLogsConfigArgs, ApplicationLogsConfigArgsDict]
            ]
        ] = ...,
        detailed_error_messages: Optional[
            pulumi.Input[Union[EnabledConfigArgs, EnabledConfigArgsDict]]
        ] = ...,
        failed_requests_tracing: Optional[
            pulumi.Input[Union[EnabledConfigArgs, EnabledConfigArgsDict]]
        ] = ...,
        http_logs: Optional[
            pulumi.Input[Union[HttpLogsConfigArgs, HttpLogsConfigArgsDict]]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebAppDiagnosticLogsConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WebAppDiagnosticLogsConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="applicationLogs")
    def application_logs(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationLogsConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="detailedErrorMessages")
    def detailed_error_messages(
        self,
    ) -> pulumi.Output[Optional[outputs.EnabledConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="failedRequestsTracing")
    def failed_requests_tracing(
        self,
    ) -> pulumi.Output[Optional[outputs.EnabledConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="httpLogs")
    def http_logs(self) -> pulumi.Output[Optional[outputs.HttpLogsConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
