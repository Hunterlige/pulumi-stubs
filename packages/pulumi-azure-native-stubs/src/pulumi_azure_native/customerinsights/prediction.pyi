import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PredictionArgs", "Prediction"]

@pulumi.input_type
class PredictionArgs:
    def __init__(
        __self__,
        *,
        auto_analyze: pulumi.Input[_builtins.bool],
        hub_name: pulumi.Input[_builtins.str],
        mappings: pulumi.Input[PredictionMappingsArgs],
        negative_outcome_expression: pulumi.Input[_builtins.str],
        positive_outcome_expression: pulumi.Input[_builtins.str],
        primary_profile_type: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        scope_expression: pulumi.Input[_builtins.str],
        score_label: pulumi.Input[_builtins.str],
        description: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        grades: Optional[
            pulumi.Input[Sequence[pulumi.Input[PredictionGradesArgs]]]
        ] = ...,
        involved_interaction_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        involved_kpi_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        involved_relationships: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        prediction_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoAnalyze")
    def auto_analyze(self) -> pulumi.Input[_builtins.bool]: ...
    @auto_analyze.setter
    def auto_analyze(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[_builtins.str]: ...
    @hub_name.setter
    def hub_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mappings(self) -> pulumi.Input[PredictionMappingsArgs]: ...
    @mappings.setter
    def mappings(self, value: pulumi.Input[PredictionMappingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="negativeOutcomeExpression")
    def negative_outcome_expression(self) -> pulumi.Input[_builtins.str]: ...
    @negative_outcome_expression.setter
    def negative_outcome_expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="positiveOutcomeExpression")
    def positive_outcome_expression(self) -> pulumi.Input[_builtins.str]: ...
    @positive_outcome_expression.setter
    def positive_outcome_expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="primaryProfileType")
    def primary_profile_type(self) -> pulumi.Input[_builtins.str]: ...
    @primary_profile_type.setter
    def primary_profile_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scopeExpression")
    def scope_expression(self) -> pulumi.Input[_builtins.str]: ...
    @scope_expression.setter
    def scope_expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scoreLabel")
    def score_label(self) -> pulumi.Input[_builtins.str]: ...
    @score_label.setter
    def score_label(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @description.setter
    def description(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @display_name.setter
    def display_name(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def grades(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PredictionGradesArgs]]]]: ...
    @grades.setter
    def grades(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PredictionGradesArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="involvedInteractionTypes")
    def involved_interaction_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @involved_interaction_types.setter
    def involved_interaction_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="involvedKpiTypes")
    def involved_kpi_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @involved_kpi_types.setter
    def involved_kpi_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="involvedRelationships")
    def involved_relationships(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @involved_relationships.setter
    def involved_relationships(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="predictionName")
    def prediction_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prediction_name.setter
    def prediction_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:customerinsights:Prediction")
class Prediction(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_analyze: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        grades: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[PredictionGradesArgs, PredictionGradesArgsDict]]
                ]
            ]
        ] = ...,
        hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        involved_interaction_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        involved_kpi_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        involved_relationships: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        mappings: Optional[
            pulumi.Input[Union[PredictionMappingsArgs, PredictionMappingsArgsDict]]
        ] = ...,
        negative_outcome_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        positive_outcome_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        prediction_name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_profile_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        score_label: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PredictionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Prediction: ...
    @_builtins.property
    @pulumi.getter(name="autoAnalyze")
    def auto_analyze(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def grades(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PredictionResponseGrades]]]: ...
    @_builtins.property
    @pulumi.getter(name="involvedInteractionTypes")
    def involved_interaction_types(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="involvedKpiTypes")
    def involved_kpi_types(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="involvedRelationships")
    def involved_relationships(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def mappings(self) -> pulumi.Output[outputs.PredictionResponseMappings]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="negativeOutcomeExpression")
    def negative_outcome_expression(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="positiveOutcomeExpression")
    def positive_outcome_expression(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="predictionName")
    def prediction_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="primaryProfileType")
    def primary_profile_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scopeExpression")
    def scope_expression(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scoreLabel")
    def score_label(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemGeneratedEntities")
    def system_generated_entities(
        self,
    ) -> pulumi.Output[outputs.PredictionResponseSystemGeneratedEntities]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
