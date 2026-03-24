import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CostCategoryArgs", "CostCategory"]

@pulumi.input_type
class CostCategoryArgs:
    def __init__(
        __self__,
        *,
        rule_version: pulumi.Input[_builtins.str],
        rules: pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleArgs]]],
        default_value: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_start: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        split_charge_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[CostCategorySplitChargeRuleArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleVersion")
    def rule_version(self) -> pulumi.Input[_builtins.str]: ...
    @rule_version.setter
    def rule_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleArgs]]]: ...
    @rules.setter
    def rules(
        self, value: pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveStart")
    def effective_start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effective_start.setter
    def effective_start(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="splitChargeRules")
    def split_charge_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CostCategorySplitChargeRuleArgs]]]
    ]: ...
    @split_charge_rules.setter
    def split_charge_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CostCategorySplitChargeRuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _CostCategoryState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_value: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_end: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_start: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_version: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleArgs]]]
        ] = ...,
        split_charge_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[CostCategorySplitChargeRuleArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveEnd")
    def effective_end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effective_end.setter
    def effective_end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveStart")
    def effective_start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effective_start.setter
    def effective_start(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleVersion")
    def rule_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_version.setter
    def rule_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="splitChargeRules")
    def split_charge_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CostCategorySplitChargeRuleArgs]]]
    ]: ...
    @split_charge_rules.setter
    def split_charge_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CostCategorySplitChargeRuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:costexplorer/costCategory:CostCategory")
class CostCategory(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        default_value: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_start: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_version: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[CostCategoryRuleArgs, CostCategoryRuleArgsDict]]
                ]
            ]
        ] = ...,
        split_charge_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CostCategorySplitChargeRuleArgs,
                            CostCategorySplitChargeRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CostCategoryArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_value: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_end: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_start: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_version: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[CostCategoryRuleArgs, CostCategoryRuleArgsDict]]
                ]
            ]
        ] = ...,
        split_charge_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CostCategorySplitChargeRuleArgs,
                            CostCategorySplitChargeRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> CostCategory: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveEnd")
    def effective_end(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveStart")
    def effective_start(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleVersion")
    def rule_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence[outputs.CostCategoryRule]]: ...
    @_builtins.property
    @pulumi.getter(name="splitChargeRules")
    def split_charge_rules(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.CostCategorySplitChargeRule]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
