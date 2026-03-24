import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LogMetricFilterArgs", "LogMetricFilter"]

@pulumi.input_type
class LogMetricFilterArgs:
    def __init__(
        __self__,
        *,
        log_group_name: pulumi.Input[_builtins.str],
        metric_transformation: pulumi.Input[LogMetricFilterMetricTransformationArgs],
        pattern: pulumi.Input[_builtins.str],
        apply_on_transformed_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricTransformation")
    def metric_transformation(
        self,
    ) -> pulumi.Input[LogMetricFilterMetricTransformationArgs]: ...
    @metric_transformation.setter
    def metric_transformation(
        self, value: pulumi.Input[LogMetricFilterMetricTransformationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applyOnTransformedLogs")
    def apply_on_transformed_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_on_transformed_logs.setter
    def apply_on_transformed_logs(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LogMetricFilterState:
    def __init__(
        __self__,
        *,
        apply_on_transformed_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        log_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_transformation: Optional[
            pulumi.Input[LogMetricFilterMetricTransformationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyOnTransformedLogs")
    def apply_on_transformed_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_on_transformed_logs.setter
    def apply_on_transformed_logs(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricTransformation")
    def metric_transformation(
        self,
    ) -> Optional[pulumi.Input[LogMetricFilterMetricTransformationArgs]]: ...
    @metric_transformation.setter
    def metric_transformation(
        self, value: Optional[pulumi.Input[LogMetricFilterMetricTransformationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:cloudwatch/logMetricFilter:LogMetricFilter")
class LogMetricFilter(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_on_transformed_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        log_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_transformation: Optional[
            pulumi.Input[
                Union[
                    LogMetricFilterMetricTransformationArgs,
                    LogMetricFilterMetricTransformationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LogMetricFilterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_on_transformed_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        log_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_transformation: Optional[
            pulumi.Input[
                Union[
                    LogMetricFilterMetricTransformationArgs,
                    LogMetricFilterMetricTransformationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LogMetricFilter: ...
    @_builtins.property
    @pulumi.getter(name="applyOnTransformedLogs")
    def apply_on_transformed_logs(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricTransformation")
    def metric_transformation(
        self,
    ) -> pulumi.Output[outputs.LogMetricFilterMetricTransformation]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
