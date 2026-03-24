import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccountArgs", "Account"]

@pulumi.input_type
class AccountArgs:
    def __init__(
        __self__,
        *,
        auto_enable_controls: Optional[pulumi.Input[_builtins.bool]] = ...,
        control_finding_generator: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_default_standards: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnableControls")
    def auto_enable_controls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_enable_controls.setter
    def auto_enable_controls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="controlFindingGenerator")
    def control_finding_generator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @control_finding_generator.setter
    def control_finding_generator(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDefaultStandards")
    def enable_default_standards(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_default_standards.setter
    def enable_default_standards(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AccountState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_enable_controls: Optional[pulumi.Input[_builtins.bool]] = ...,
        control_finding_generator: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_default_standards: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoEnableControls")
    def auto_enable_controls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_enable_controls.setter
    def auto_enable_controls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="controlFindingGenerator")
    def control_finding_generator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @control_finding_generator.setter
    def control_finding_generator(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDefaultStandards")
    def enable_default_standards(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_default_standards.setter
    def enable_default_standards(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:securityhub/account:Account")
class Account(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_enable_controls: Optional[pulumi.Input[_builtins.bool]] = ...,
        control_finding_generator: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_default_standards: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AccountArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_enable_controls: Optional[pulumi.Input[_builtins.bool]] = ...,
        control_finding_generator: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_default_standards: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Account: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoEnableControls")
    def auto_enable_controls(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="controlFindingGenerator")
    def control_finding_generator(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableDefaultStandards")
    def enable_default_standards(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
