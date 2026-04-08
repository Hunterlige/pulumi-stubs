import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPredictionResult",
    "AwaitableGetPredictionResult",
    "get_prediction",
    "get_prediction_output",
]

@pulumi.output_type
class GetPredictionResult:
    def __init__(
        __self__,
        auto_analyze=...,
        azure_api_version=...,
        description=...,
        display_name=...,
        grades=...,
        id=...,
        involved_interaction_types=...,
        involved_kpi_types=...,
        involved_relationships=...,
        mappings=...,
        name=...,
        negative_outcome_expression=...,
        positive_outcome_expression=...,
        prediction_name=...,
        primary_profile_type=...,
        provisioning_state=...,
        scope_expression=...,
        score_label=...,
        system_generated_entities=...,
        tenant_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoAnalyze")
    def auto_analyze(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def grades(self) -> Optional[Sequence[outputs.PredictionResponseGrades]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="involvedInteractionTypes")
    def involved_interaction_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="involvedKpiTypes")
    def involved_kpi_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="involvedRelationships")
    def involved_relationships(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def mappings(self) -> outputs.PredictionResponseMappings: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="negativeOutcomeExpression")
    def negative_outcome_expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="positiveOutcomeExpression")
    def positive_outcome_expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="predictionName")
    def prediction_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryProfileType")
    def primary_profile_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scopeExpression")
    def scope_expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scoreLabel")
    def score_label(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemGeneratedEntities")
    def system_generated_entities(
        self,
    ) -> outputs.PredictionResponseSystemGeneratedEntities: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPredictionResult(GetPredictionResult):
    def __await__(self): ...

def get_prediction(
    hub_name: Optional[_builtins.str] = ...,
    prediction_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPredictionResult: ...
def get_prediction_output(
    hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
    prediction_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPredictionResult]: ...
