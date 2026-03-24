import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LoggingConfigurationArgs", "LoggingConfiguration"]

@pulumi.input_type
class LoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        firewall_arn: pulumi.Input[_builtins.str],
        logging_configuration: pulumi.Input[
            LoggingConfigurationLoggingConfigurationArgs
        ],
        enable_monitoring_dashboard: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="firewallArn")
    def firewall_arn(self) -> pulumi.Input[_builtins.str]: ...
    @firewall_arn.setter
    def firewall_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> pulumi.Input[LoggingConfigurationLoggingConfigurationArgs]: ...
    @logging_configuration.setter
    def logging_configuration(
        self, value: pulumi.Input[LoggingConfigurationLoggingConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableMonitoringDashboard")
    def enable_monitoring_dashboard(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_monitoring_dashboard.setter
    def enable_monitoring_dashboard(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LoggingConfigurationState:
    def __init__(
        __self__,
        *,
        enable_monitoring_dashboard: Optional[pulumi.Input[_builtins.bool]] = ...,
        firewall_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[LoggingConfigurationLoggingConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableMonitoringDashboard")
    def enable_monitoring_dashboard(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_monitoring_dashboard.setter
    def enable_monitoring_dashboard(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="firewallArn")
    def firewall_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_arn.setter
    def firewall_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> Optional[pulumi.Input[LoggingConfigurationLoggingConfigurationArgs]]: ...
    @logging_configuration.setter
    def logging_configuration(
        self,
        value: Optional[pulumi.Input[LoggingConfigurationLoggingConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class LoggingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        enable_monitoring_dashboard: Optional[pulumi.Input[_builtins.bool]] = ...,
        firewall_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[
                Union[
                    LoggingConfigurationLoggingConfigurationArgs,
                    LoggingConfigurationLoggingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LoggingConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        enable_monitoring_dashboard: Optional[pulumi.Input[_builtins.bool]] = ...,
        firewall_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[
                Union[
                    LoggingConfigurationLoggingConfigurationArgs,
                    LoggingConfigurationLoggingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LoggingConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="enableMonitoringDashboard")
    def enable_monitoring_dashboard(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="firewallArn")
    def firewall_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> pulumi.Output[outputs.LoggingConfigurationLoggingConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
