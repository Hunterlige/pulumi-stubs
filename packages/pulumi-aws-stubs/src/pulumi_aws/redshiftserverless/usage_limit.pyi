import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UsageLimitArgs", "UsageLimit"]

@pulumi.input_type
class UsageLimitArgs:
    def __init__(
        __self__,
        *,
        amount: pulumi.Input[_builtins.int],
        resource_arn: pulumi.Input[_builtins.str],
        usage_type: pulumi.Input[_builtins.str],
        breach_action: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> pulumi.Input[_builtins.int]: ...
    @amount.setter
    def amount(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="usageType")
    def usage_type(self) -> pulumi.Input[_builtins.str]: ...
    @usage_type.setter
    def usage_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="breachAction")
    def breach_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @breach_action.setter
    def breach_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _UsageLimitState:
    def __init__(
        __self__,
        *,
        amount: Optional[pulumi.Input[_builtins.int]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        breach_action: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @amount.setter
    def amount(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="breachAction")
    def breach_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @breach_action.setter
    def breach_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="usageType")
    def usage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @usage_type.setter
    def usage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:redshiftserverless/usageLimit:UsageLimit")
class UsageLimit(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        amount: Optional[pulumi.Input[_builtins.int]] = ...,
        breach_action: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UsageLimitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        amount: Optional[pulumi.Input[_builtins.int]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        breach_action: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> UsageLimit: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="breachAction")
    def breach_action(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usageType")
    def usage_type(self) -> pulumi.Output[_builtins.str]: ...
