import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PreferencesArgs", "Preferences"]

@pulumi.input_type
class PreferencesArgs:
    def __init__(
        __self__,
        *,
        member_account_discount_visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        savings_estimation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memberAccountDiscountVisibility")
    def member_account_discount_visibility(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @member_account_discount_visibility.setter
    def member_account_discount_visibility(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="savingsEstimationMode")
    def savings_estimation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @savings_estimation_mode.setter
    def savings_estimation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PreferencesState:
    def __init__(
        __self__,
        *,
        member_account_discount_visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        savings_estimation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memberAccountDiscountVisibility")
    def member_account_discount_visibility(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @member_account_discount_visibility.setter
    def member_account_discount_visibility(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="savingsEstimationMode")
    def savings_estimation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @savings_estimation_mode.setter
    def savings_estimation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:costoptimizationhub/preferences:Preferences")
class Preferences(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        member_account_discount_visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        savings_estimation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[PreferencesArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        member_account_discount_visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        savings_estimation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Preferences: ...
    @_builtins.property
    @pulumi.getter(name="memberAccountDiscountVisibility")
    def member_account_discount_visibility(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="savingsEstimationMode")
    def savings_estimation_mode(self) -> pulumi.Output[_builtins.str]: ...
