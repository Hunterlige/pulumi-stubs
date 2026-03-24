import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LogSubscriptionFilterArgs", "LogSubscriptionFilter"]

@pulumi.input_type
class LogSubscriptionFilterArgs:
    def __init__(
        __self__,
        *,
        destination_arn: pulumi.Input[_builtins.str],
        filter_pattern: pulumi.Input[_builtins.str],
        log_group: pulumi.Input[_builtins.str],
        apply_on_transformed_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        distribution: Optional[pulumi.Input[_builtins.str]] = ...,
        emit_system_fields: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Input[_builtins.str]: ...
    @destination_arn.setter
    def destination_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="filterPattern")
    def filter_pattern(self) -> pulumi.Input[_builtins.str]: ...
    @filter_pattern.setter
    def filter_pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> pulumi.Input[_builtins.str]: ...
    @log_group.setter
    def log_group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applyOnTransformedLogs")
    def apply_on_transformed_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_on_transformed_logs.setter
    def apply_on_transformed_logs(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distribution.setter
    def distribution(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emitSystemFields")
    def emit_system_fields(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @emit_system_fields.setter
    def emit_system_fields(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LogSubscriptionFilterState:
    def __init__(
        __self__,
        *,
        apply_on_transformed_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution: Optional[pulumi.Input[_builtins.str]] = ...,
        emit_system_fields: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        filter_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        log_group: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyOnTransformedLogs")
    def apply_on_transformed_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_on_transformed_logs.setter
    def apply_on_transformed_logs(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_arn.setter
    def destination_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distribution.setter
    def distribution(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emitSystemFields")
    def emit_system_fields(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @emit_system_fields.setter
    def emit_system_fields(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterPattern")
    def filter_pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter_pattern.setter
    def filter_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_group.setter
    def log_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class LogSubscriptionFilter(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_on_transformed_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution: Optional[pulumi.Input[_builtins.str]] = ...,
        emit_system_fields: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        filter_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        log_group: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LogSubscriptionFilterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_on_transformed_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution: Optional[pulumi.Input[_builtins.str]] = ...,
        emit_system_fields: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        filter_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        log_group: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LogSubscriptionFilter: ...
    @_builtins.property
    @pulumi.getter(name="applyOnTransformedLogs")
    def apply_on_transformed_logs(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="emitSystemFields")
    def emit_system_fields(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="filterPattern")
    def filter_pattern(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
