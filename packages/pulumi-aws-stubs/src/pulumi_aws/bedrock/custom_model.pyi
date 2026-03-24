import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CustomModelArgs", "CustomModel"]

@pulumi.input_type
class CustomModelArgs:
    def __init__(
        __self__,
        *,
        base_model_identifier: pulumi.Input[_builtins.str],
        custom_model_name: pulumi.Input[_builtins.str],
        hyperparameters: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        job_name: pulumi.Input[_builtins.str],
        output_data_config: pulumi.Input[CustomModelOutputDataConfigArgs],
        role_arn: pulumi.Input[_builtins.str],
        training_data_config: pulumi.Input[CustomModelTrainingDataConfigArgs],
        custom_model_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customization_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[CustomModelTimeoutsArgs]] = ...,
        validation_data_config: Optional[
            pulumi.Input[CustomModelValidationDataConfigArgs]
        ] = ...,
        vpc_config: Optional[pulumi.Input[CustomModelVpcConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseModelIdentifier")
    def base_model_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @base_model_identifier.setter
    def base_model_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customModelName")
    def custom_model_name(self) -> pulumi.Input[_builtins.str]: ...
    @custom_model_name.setter
    def custom_model_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hyperparameters(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @hyperparameters.setter
    def hyperparameters(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[_builtins.str]: ...
    @job_name.setter
    def job_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="outputDataConfig")
    def output_data_config(self) -> pulumi.Input[CustomModelOutputDataConfigArgs]: ...
    @output_data_config.setter
    def output_data_config(
        self, value: pulumi.Input[CustomModelOutputDataConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingDataConfig")
    def training_data_config(
        self,
    ) -> pulumi.Input[CustomModelTrainingDataConfigArgs]: ...
    @training_data_config.setter
    def training_data_config(
        self, value: pulumi.Input[CustomModelTrainingDataConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customModelKmsKeyId")
    def custom_model_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_model_kms_key_id.setter
    def custom_model_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customizationType")
    def customization_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customization_type.setter
    def customization_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[CustomModelTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CustomModelTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="validationDataConfig")
    def validation_data_config(
        self,
    ) -> Optional[pulumi.Input[CustomModelValidationDataConfigArgs]]: ...
    @validation_data_config.setter
    def validation_data_config(
        self, value: Optional[pulumi.Input[CustomModelValidationDataConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[CustomModelVpcConfigArgs]]: ...
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[CustomModelVpcConfigArgs]]): ...

@pulumi.input_type
class _CustomModelState:
    def __init__(
        __self__,
        *,
        base_model_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_model_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_model_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_model_name: Optional[pulumi.Input[_builtins.str]] = ...,
        customization_type: Optional[pulumi.Input[_builtins.str]] = ...,
        hyperparameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        job_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        job_status: Optional[pulumi.Input[_builtins.str]] = ...,
        output_data_config: Optional[
            pulumi.Input[CustomModelOutputDataConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[CustomModelTimeoutsArgs]] = ...,
        training_data_config: Optional[
            pulumi.Input[CustomModelTrainingDataConfigArgs]
        ] = ...,
        training_metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomModelTrainingMetricArgs]]]
        ] = ...,
        validation_data_config: Optional[
            pulumi.Input[CustomModelValidationDataConfigArgs]
        ] = ...,
        validation_metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomModelValidationMetricArgs]]]
        ] = ...,
        vpc_config: Optional[pulumi.Input[CustomModelVpcConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseModelIdentifier")
    def base_model_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_model_identifier.setter
    def base_model_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customModelArn")
    def custom_model_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_model_arn.setter
    def custom_model_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customModelKmsKeyId")
    def custom_model_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_model_kms_key_id.setter
    def custom_model_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customModelName")
    def custom_model_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_model_name.setter
    def custom_model_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customizationType")
    def customization_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customization_type.setter
    def customization_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def hyperparameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @hyperparameters.setter
    def hyperparameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobArn")
    def job_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_arn.setter
    def job_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_name.setter
    def job_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobStatus")
    def job_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_status.setter
    def job_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputDataConfig")
    def output_data_config(
        self,
    ) -> Optional[pulumi.Input[CustomModelOutputDataConfigArgs]]: ...
    @output_data_config.setter
    def output_data_config(
        self, value: Optional[pulumi.Input[CustomModelOutputDataConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[CustomModelTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CustomModelTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="trainingDataConfig")
    def training_data_config(
        self,
    ) -> Optional[pulumi.Input[CustomModelTrainingDataConfigArgs]]: ...
    @training_data_config.setter
    def training_data_config(
        self, value: Optional[pulumi.Input[CustomModelTrainingDataConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trainingMetrics")
    def training_metrics(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CustomModelTrainingMetricArgs]]]
    ]: ...
    @training_metrics.setter
    def training_metrics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomModelTrainingMetricArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationDataConfig")
    def validation_data_config(
        self,
    ) -> Optional[pulumi.Input[CustomModelValidationDataConfigArgs]]: ...
    @validation_data_config.setter
    def validation_data_config(
        self, value: Optional[pulumi.Input[CustomModelValidationDataConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationMetrics")
    def validation_metrics(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CustomModelValidationMetricArgs]]]
    ]: ...
    @validation_metrics.setter
    def validation_metrics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomModelValidationMetricArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[CustomModelVpcConfigArgs]]: ...
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[CustomModelVpcConfigArgs]]): ...

@pulumi.type_token("aws:bedrock/customModel:CustomModel")
class CustomModel(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        base_model_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_model_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_model_name: Optional[pulumi.Input[_builtins.str]] = ...,
        customization_type: Optional[pulumi.Input[_builtins.str]] = ...,
        hyperparameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_data_config: Optional[
            pulumi.Input[
                Union[
                    CustomModelOutputDataConfigArgs, CustomModelOutputDataConfigArgsDict
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[CustomModelTimeoutsArgs, CustomModelTimeoutsArgsDict]]
        ] = ...,
        training_data_config: Optional[
            pulumi.Input[
                Union[
                    CustomModelTrainingDataConfigArgs,
                    CustomModelTrainingDataConfigArgsDict,
                ]
            ]
        ] = ...,
        validation_data_config: Optional[
            pulumi.Input[
                Union[
                    CustomModelValidationDataConfigArgs,
                    CustomModelValidationDataConfigArgsDict,
                ]
            ]
        ] = ...,
        vpc_config: Optional[
            pulumi.Input[Union[CustomModelVpcConfigArgs, CustomModelVpcConfigArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CustomModelArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        base_model_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_model_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_model_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_model_name: Optional[pulumi.Input[_builtins.str]] = ...,
        customization_type: Optional[pulumi.Input[_builtins.str]] = ...,
        hyperparameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        job_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        job_status: Optional[pulumi.Input[_builtins.str]] = ...,
        output_data_config: Optional[
            pulumi.Input[
                Union[
                    CustomModelOutputDataConfigArgs, CustomModelOutputDataConfigArgsDict
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[CustomModelTimeoutsArgs, CustomModelTimeoutsArgsDict]]
        ] = ...,
        training_data_config: Optional[
            pulumi.Input[
                Union[
                    CustomModelTrainingDataConfigArgs,
                    CustomModelTrainingDataConfigArgsDict,
                ]
            ]
        ] = ...,
        training_metrics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomModelTrainingMetricArgs,
                            CustomModelTrainingMetricArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        validation_data_config: Optional[
            pulumi.Input[
                Union[
                    CustomModelValidationDataConfigArgs,
                    CustomModelValidationDataConfigArgsDict,
                ]
            ]
        ] = ...,
        validation_metrics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomModelValidationMetricArgs,
                            CustomModelValidationMetricArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        vpc_config: Optional[
            pulumi.Input[Union[CustomModelVpcConfigArgs, CustomModelVpcConfigArgsDict]]
        ] = ...,
    ) -> CustomModel: ...
    @_builtins.property
    @pulumi.getter(name="baseModelIdentifier")
    def base_model_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customModelArn")
    def custom_model_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customModelKmsKeyId")
    def custom_model_kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customModelName")
    def custom_model_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customizationType")
    def customization_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hyperparameters(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="jobArn")
    def job_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobStatus")
    def job_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputDataConfig")
    def output_data_config(
        self,
    ) -> pulumi.Output[outputs.CustomModelOutputDataConfig]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.CustomModelTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="trainingDataConfig")
    def training_data_config(
        self,
    ) -> pulumi.Output[outputs.CustomModelTrainingDataConfig]: ...
    @_builtins.property
    @pulumi.getter(name="trainingMetrics")
    def training_metrics(
        self,
    ) -> pulumi.Output[Sequence[outputs.CustomModelTrainingMetric]]: ...
    @_builtins.property
    @pulumi.getter(name="validationDataConfig")
    def validation_data_config(
        self,
    ) -> pulumi.Output[Optional[outputs.CustomModelValidationDataConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="validationMetrics")
    def validation_metrics(
        self,
    ) -> pulumi.Output[Sequence[outputs.CustomModelValidationMetric]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[Optional[outputs.CustomModelVpcConfig]]: ...
