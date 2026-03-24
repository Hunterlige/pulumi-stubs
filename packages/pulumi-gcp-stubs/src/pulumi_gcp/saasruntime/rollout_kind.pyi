import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RolloutKindArgs", "RolloutKind"]

@pulumi.input_type
class RolloutKindArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        rollout_kind_id: pulumi.Input[_builtins.str],
        unit_kind: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        error_budget: Optional[pulumi.Input[RolloutKindErrorBudgetArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_orchestration_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        unit_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        update_unit_kind_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutKindId")
    def rollout_kind_id(self) -> pulumi.Input[_builtins.str]: ...
    @rollout_kind_id.setter
    def rollout_kind_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> pulumi.Input[_builtins.str]: ...
    @unit_kind.setter
    def unit_kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorBudget")
    def error_budget(self) -> Optional[pulumi.Input[RolloutKindErrorBudgetArgs]]: ...
    @error_budget.setter
    def error_budget(
        self, value: Optional[pulumi.Input[RolloutKindErrorBudgetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutOrchestrationStrategy")
    def rollout_orchestration_strategy(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_orchestration_strategy.setter
    def rollout_orchestration_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="unitFilter")
    def unit_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit_filter.setter
    def unit_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateUnitKindStrategy")
    def update_unit_kind_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_unit_kind_strategy.setter
    def update_unit_kind_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _RolloutKindState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        error_budget: Optional[pulumi.Input[RolloutKindErrorBudgetArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        rollout_kind_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_orchestration_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        unit_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        unit_kind: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        update_unit_kind_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_annotations.setter
    def effective_annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorBudget")
    def error_budget(self) -> Optional[pulumi.Input[RolloutKindErrorBudgetArgs]]: ...
    @error_budget.setter
    def error_budget(
        self, value: Optional[pulumi.Input[RolloutKindErrorBudgetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rolloutKindId")
    def rollout_kind_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_kind_id.setter
    def rollout_kind_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutOrchestrationStrategy")
    def rollout_orchestration_strategy(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_orchestration_strategy.setter
    def rollout_orchestration_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="unitFilter")
    def unit_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit_filter.setter
    def unit_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit_kind.setter
    def unit_kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateUnitKindStrategy")
    def update_unit_kind_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_unit_kind_strategy.setter
    def update_unit_kind_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("gcp:saasruntime/rolloutKind:RolloutKind")
class RolloutKind(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        error_budget: Optional[
            pulumi.Input[
                Union[RolloutKindErrorBudgetArgs, RolloutKindErrorBudgetArgsDict]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_kind_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_orchestration_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        unit_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        unit_kind: Optional[pulumi.Input[_builtins.str]] = ...,
        update_unit_kind_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RolloutKindArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        error_budget: Optional[
            pulumi.Input[
                Union[RolloutKindErrorBudgetArgs, RolloutKindErrorBudgetArgsDict]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        rollout_kind_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_orchestration_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        unit_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        unit_kind: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        update_unit_kind_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RolloutKind: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="errorBudget")
    def error_budget(
        self,
    ) -> pulumi.Output[Optional[outputs.RolloutKindErrorBudget]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutKindId")
    def rollout_kind_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutOrchestrationStrategy")
    def rollout_orchestration_strategy(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unitFilter")
    def unit_filter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateUnitKindStrategy")
    def update_unit_kind_strategy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
