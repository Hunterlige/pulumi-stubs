import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DefaultAutoScalingConfigurationVersionArgs",
    "DefaultAutoScalingConfigurationVersion",
]

@pulumi.input_type
class DefaultAutoScalingConfigurationVersionArgs:
    def __init__(
        __self__,
        *,
        auto_scaling_configuration_arn: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> pulumi.Input[_builtins.str]: ...
    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DefaultAutoScalingConfigurationVersionState:
    def __init__(
        __self__,
        *,
        auto_scaling_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class DefaultAutoScalingConfigurationVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_scaling_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DefaultAutoScalingConfigurationVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_scaling_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DefaultAutoScalingConfigurationVersion: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
