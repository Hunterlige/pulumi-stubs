import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCustomModelResult",
    "AwaitableGetCustomModelResult",
    "get_custom_model",
    "get_custom_model_output",
]

@pulumi.output_type
class GetCustomModelResult:
    def __init__(
        __self__,
        base_model_arn=...,
        creation_time=...,
        hyperparameters=...,
        id=...,
        job_arn=...,
        job_name=...,
        job_tags=...,
        model_arn=...,
        model_id=...,
        model_kms_key_arn=...,
        model_name=...,
        model_tags=...,
        output_data_configs=...,
        region=...,
        training_data_configs=...,
        training_metrics=...,
        validation_data_configs=...,
        validation_metrics=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseModelArn")
    def base_model_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hyperparameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobArn")
    def job_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobTags")
    def job_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelKmsKeyArn")
    def model_kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelTags")
    def model_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputDataConfigs")
    def output_data_configs(
        self,
    ) -> Sequence[outputs.GetCustomModelOutputDataConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trainingDataConfigs")
    def training_data_configs(
        self,
    ) -> Sequence[outputs.GetCustomModelTrainingDataConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="trainingMetrics")
    def training_metrics(
        self,
    ) -> Sequence[outputs.GetCustomModelTrainingMetricResult]: ...
    @_builtins.property
    @pulumi.getter(name="validationDataConfigs")
    def validation_data_configs(
        self,
    ) -> Sequence[outputs.GetCustomModelValidationDataConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="validationMetrics")
    def validation_metrics(
        self,
    ) -> Sequence[outputs.GetCustomModelValidationMetricResult]: ...

class AwaitableGetCustomModelResult(GetCustomModelResult):
    def __await__(self): ...

def get_custom_model(
    model_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCustomModelResult: ...
def get_custom_model_output(
    model_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCustomModelResult]: ...
