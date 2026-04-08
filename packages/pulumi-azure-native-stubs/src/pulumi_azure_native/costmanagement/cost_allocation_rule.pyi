import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CostAllocationRuleArgs", "CostAllocationRule"]

@pulumi.input_type
class CostAllocationRuleArgs:
    def __init__(
        __self__,
        *,
        billing_account_id: pulumi.Input[_builtins.str],
        properties: Optional[pulumi.Input[CostAllocationRulePropertiesArgs]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @billing_account_id.setter
    def billing_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[CostAllocationRulePropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[CostAllocationRulePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:costmanagement:CostAllocationRule")
class CostAllocationRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        billing_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    CostAllocationRulePropertiesArgs,
                    CostAllocationRulePropertiesArgsDict,
                ]
            ]
        ] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CostAllocationRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CostAllocationRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.CostAllocationRulePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
