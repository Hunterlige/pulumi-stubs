import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BudgetArgs", "Budget"]

@pulumi.input_type
class BudgetArgs:
    def __init__(
        __self__,
        *,
        amount: pulumi.Input[BudgetAmountArgs],
        billing_account: pulumi.Input[_builtins.str],
        all_updates_rule: Optional[pulumi.Input[BudgetAllUpdatesRuleArgs]] = ...,
        budget_filter: Optional[pulumi.Input[BudgetBudgetFilterArgs]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ownership_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        threshold_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetThresholdRuleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> pulumi.Input[BudgetAmountArgs]: ...
    @amount.setter
    def amount(self, value: pulumi.Input[BudgetAmountArgs]): ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Input[_builtins.str]: ...
    @billing_account.setter
    def billing_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allUpdatesRule")
    def all_updates_rule(self) -> Optional[pulumi.Input[BudgetAllUpdatesRuleArgs]]: ...
    @all_updates_rule.setter
    def all_updates_rule(
        self, value: Optional[pulumi.Input[BudgetAllUpdatesRuleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="budgetFilter")
    def budget_filter(self) -> Optional[pulumi.Input[BudgetBudgetFilterArgs]]: ...
    @budget_filter.setter
    def budget_filter(self, value: Optional[pulumi.Input[BudgetBudgetFilterArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownershipScope")
    def ownership_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ownership_scope.setter
    def ownership_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="thresholdRules")
    def threshold_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetThresholdRuleArgs]]]]: ...
    @threshold_rules.setter
    def threshold_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BudgetThresholdRuleArgs]]]],
    ): ...

@pulumi.input_type
class _BudgetState:
    def __init__(
        __self__,
        *,
        all_updates_rule: Optional[pulumi.Input[BudgetAllUpdatesRuleArgs]] = ...,
        amount: Optional[pulumi.Input[BudgetAmountArgs]] = ...,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        budget_filter: Optional[pulumi.Input[BudgetBudgetFilterArgs]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ownership_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        threshold_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetThresholdRuleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allUpdatesRule")
    def all_updates_rule(self) -> Optional[pulumi.Input[BudgetAllUpdatesRuleArgs]]: ...
    @all_updates_rule.setter
    def all_updates_rule(
        self, value: Optional[pulumi.Input[BudgetAllUpdatesRuleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> Optional[pulumi.Input[BudgetAmountArgs]]: ...
    @amount.setter
    def amount(self, value: Optional[pulumi.Input[BudgetAmountArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_account.setter
    def billing_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="budgetFilter")
    def budget_filter(self) -> Optional[pulumi.Input[BudgetBudgetFilterArgs]]: ...
    @budget_filter.setter
    def budget_filter(self, value: Optional[pulumi.Input[BudgetBudgetFilterArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownershipScope")
    def ownership_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ownership_scope.setter
    def ownership_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="thresholdRules")
    def threshold_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetThresholdRuleArgs]]]]: ...
    @threshold_rules.setter
    def threshold_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BudgetThresholdRuleArgs]]]],
    ): ...

@pulumi.type_token("gcp:billing/budget:Budget")
class Budget(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        all_updates_rule: Optional[
            pulumi.Input[Union[BudgetAllUpdatesRuleArgs, BudgetAllUpdatesRuleArgsDict]]
        ] = ...,
        amount: Optional[
            pulumi.Input[Union[BudgetAmountArgs, BudgetAmountArgsDict]]
        ] = ...,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        budget_filter: Optional[
            pulumi.Input[Union[BudgetBudgetFilterArgs, BudgetBudgetFilterArgsDict]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ownership_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        threshold_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[BudgetThresholdRuleArgs, BudgetThresholdRuleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BudgetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        all_updates_rule: Optional[
            pulumi.Input[Union[BudgetAllUpdatesRuleArgs, BudgetAllUpdatesRuleArgsDict]]
        ] = ...,
        amount: Optional[
            pulumi.Input[Union[BudgetAmountArgs, BudgetAmountArgsDict]]
        ] = ...,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        budget_filter: Optional[
            pulumi.Input[Union[BudgetBudgetFilterArgs, BudgetBudgetFilterArgsDict]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ownership_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        threshold_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[BudgetThresholdRuleArgs, BudgetThresholdRuleArgsDict]
                    ]
                ]
            ]
        ] = ...,
    ) -> Budget: ...
    @_builtins.property
    @pulumi.getter(name="allUpdatesRule")
    def all_updates_rule(
        self,
    ) -> pulumi.Output[Optional[outputs.BudgetAllUpdatesRule]]: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> pulumi.Output[outputs.BudgetAmount]: ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="budgetFilter")
    def budget_filter(self) -> pulumi.Output[outputs.BudgetBudgetFilter]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownershipScope")
    def ownership_scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="thresholdRules")
    def threshold_rules(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.BudgetThresholdRule]]]: ...
