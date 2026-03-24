import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RuleArgs", "Rule"]

@pulumi.input_type
class RuleArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[RuleSourceArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_modes: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuleEvaluationModeArgs]]]
        ] = ...,
        input_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[RuleScopeArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[RuleSourceArgs]: ...
    @source.setter
    def source(self, value: pulumi.Input[RuleSourceArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationModes")
    def evaluation_modes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleEvaluationModeArgs]]]]: ...
    @evaluation_modes.setter
    def evaluation_modes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RuleEvaluationModeArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_parameters.setter
    def input_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maximum_execution_frequency.setter
    def maximum_execution_frequency(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[RuleScopeArgs]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[RuleScopeArgs]]): ...
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
class _RuleState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_modes: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuleEvaluationModeArgs]]]
        ] = ...,
        input_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[RuleScopeArgs]] = ...,
        source: Optional[pulumi.Input[RuleSourceArgs]] = ...,
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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationModes")
    def evaluation_modes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleEvaluationModeArgs]]]]: ...
    @evaluation_modes.setter
    def evaluation_modes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RuleEvaluationModeArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_parameters.setter
    def input_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maximum_execution_frequency.setter
    def maximum_execution_frequency(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[RuleScopeArgs]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[RuleScopeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[RuleSourceArgs]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[RuleSourceArgs]]): ...
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

@pulumi.type_token("aws:cfg/rule:Rule")
class Rule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_modes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[RuleEvaluationModeArgs, RuleEvaluationModeArgsDict]
                    ]
                ]
            ]
        ] = ...,
        input_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[Union[RuleScopeArgs, RuleScopeArgsDict]]] = ...,
        source: Optional[pulumi.Input[Union[RuleSourceArgs, RuleSourceArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_modes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[RuleEvaluationModeArgs, RuleEvaluationModeArgsDict]
                    ]
                ]
            ]
        ] = ...,
        input_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[Union[RuleScopeArgs, RuleScopeArgsDict]]] = ...,
        source: Optional[pulumi.Input[Union[RuleSourceArgs, RuleSourceArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Rule: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="evaluationModes")
    def evaluation_modes(
        self,
    ) -> pulumi.Output[Sequence[outputs.RuleEvaluationMode]]: ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[outputs.RuleScope]]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[outputs.RuleSource]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
