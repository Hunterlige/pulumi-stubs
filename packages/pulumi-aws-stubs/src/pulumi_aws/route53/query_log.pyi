import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["QueryLogArgs", "QueryLog"]

@pulumi.input_type
class QueryLogArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_log_group_arn: pulumi.Input[_builtins.str],
        zone_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> pulumi.Input[_builtins.str]: ...
    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @zone_id.setter
    def zone_id(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _QueryLogState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:route53/queryLog:QueryLog")
class QueryLog(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: QueryLogArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> QueryLog: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[_builtins.str]: ...
