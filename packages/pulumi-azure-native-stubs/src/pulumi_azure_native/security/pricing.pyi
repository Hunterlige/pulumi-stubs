import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PricingArgs", "Pricing"]

@pulumi.input_type
class PricingArgs:
    def __init__(
        __self__,
        *,
        pricing_tier: pulumi.Input[Union[_builtins.str, PricingTier]],
        scope_id: pulumi.Input[_builtins.str],
        enforce: Optional[pulumi.Input[Union[_builtins.str, Enforce]]] = ...,
        extensions: Optional[pulumi.Input[Sequence[pulumi.Input[ExtensionArgs]]]] = ...,
        pricing_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_plan: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pricingTier")
    def pricing_tier(self) -> pulumi.Input[Union[_builtins.str, PricingTier]]: ...
    @pricing_tier.setter
    def pricing_tier(self, value: pulumi.Input[Union[_builtins.str, PricingTier]]): ...
    @_builtins.property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> pulumi.Input[_builtins.str]: ...
    @scope_id.setter
    def scope_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[Union[_builtins.str, Enforce]]]: ...
    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[Union[_builtins.str, Enforce]]]): ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExtensionArgs]]]]: ...
    @extensions.setter
    def extensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExtensionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pricingName")
    def pricing_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pricing_name.setter
    def pricing_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subPlan")
    def sub_plan(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sub_plan.setter
    def sub_plan(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:security:Pricing")
class Pricing(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        enforce: Optional[pulumi.Input[Union[_builtins.str, Enforce]]] = ...,
        extensions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ExtensionArgs, ExtensionArgsDict]]]
            ]
        ] = ...,
        pricing_name: Optional[pulumi.Input[_builtins.str]] = ...,
        pricing_tier: Optional[pulumi.Input[Union[_builtins.str, PricingTier]]] = ...,
        scope_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_plan: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PricingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Pricing: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def deprecated(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablementTime")
    def enablement_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ExtensionResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="freeTrialRemainingTime")
    def free_trial_remaining_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def inherited(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inheritedFrom")
    def inherited_from(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pricingTier")
    def pricing_tier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replacedBy")
    def replaced_by(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourcesCoverageStatus")
    def resources_coverage_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subPlan")
    def sub_plan(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
