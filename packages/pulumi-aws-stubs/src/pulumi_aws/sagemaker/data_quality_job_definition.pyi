import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DataQualityJobDefinitionArgs", "DataQualityJobDefinition"]

@pulumi.input_type
class DataQualityJobDefinitionArgs:
    def __init__(
        __self__,
        *,
        data_quality_app_specification: pulumi.Input[
            DataQualityJobDefinitionDataQualityAppSpecificationArgs
        ],
        data_quality_job_input: pulumi.Input[
            DataQualityJobDefinitionDataQualityJobInputArgs
        ],
        data_quality_job_output_config: pulumi.Input[
            DataQualityJobDefinitionDataQualityJobOutputConfigArgs
        ],
        job_resources: pulumi.Input[DataQualityJobDefinitionJobResourcesArgs],
        role_arn: pulumi.Input[_builtins.str],
        data_quality_baseline_config: Optional[
            pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[DataQualityJobDefinitionNetworkConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stopping_condition: Optional[
            pulumi.Input[DataQualityJobDefinitionStoppingConditionArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataQualityAppSpecification")
    def data_quality_app_specification(
        self,
    ) -> pulumi.Input[DataQualityJobDefinitionDataQualityAppSpecificationArgs]: ...
    @data_quality_app_specification.setter
    def data_quality_app_specification(
        self,
        value: pulumi.Input[DataQualityJobDefinitionDataQualityAppSpecificationArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataQualityJobInput")
    def data_quality_job_input(
        self,
    ) -> pulumi.Input[DataQualityJobDefinitionDataQualityJobInputArgs]: ...
    @data_quality_job_input.setter
    def data_quality_job_input(
        self, value: pulumi.Input[DataQualityJobDefinitionDataQualityJobInputArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataQualityJobOutputConfig")
    def data_quality_job_output_config(
        self,
    ) -> pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigArgs]: ...
    @data_quality_job_output_config.setter
    def data_quality_job_output_config(
        self,
        value: pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobResources")
    def job_resources(
        self,
    ) -> pulumi.Input[DataQualityJobDefinitionJobResourcesArgs]: ...
    @job_resources.setter
    def job_resources(
        self, value: pulumi.Input[DataQualityJobDefinitionJobResourcesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataQualityBaselineConfig")
    def data_quality_baseline_config(
        self,
    ) -> Optional[
        pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigArgs]
    ]: ...
    @data_quality_baseline_config.setter
    def data_quality_baseline_config(
        self,
        value: Optional[
            pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[pulumi.Input[DataQualityJobDefinitionNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[DataQualityJobDefinitionNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> Optional[pulumi.Input[DataQualityJobDefinitionStoppingConditionArgs]]: ...
    @stopping_condition.setter
    def stopping_condition(
        self,
        value: Optional[pulumi.Input[DataQualityJobDefinitionStoppingConditionArgs]],
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
class _DataQualityJobDefinitionState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        data_quality_app_specification: Optional[
            pulumi.Input[DataQualityJobDefinitionDataQualityAppSpecificationArgs]
        ] = ...,
        data_quality_baseline_config: Optional[
            pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigArgs]
        ] = ...,
        data_quality_job_input: Optional[
            pulumi.Input[DataQualityJobDefinitionDataQualityJobInputArgs]
        ] = ...,
        data_quality_job_output_config: Optional[
            pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigArgs]
        ] = ...,
        job_resources: Optional[
            pulumi.Input[DataQualityJobDefinitionJobResourcesArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[DataQualityJobDefinitionNetworkConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stopping_condition: Optional[
            pulumi.Input[DataQualityJobDefinitionStoppingConditionArgs]
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
    @pulumi.getter(name="dataQualityAppSpecification")
    def data_quality_app_specification(
        self,
    ) -> Optional[
        pulumi.Input[DataQualityJobDefinitionDataQualityAppSpecificationArgs]
    ]: ...
    @data_quality_app_specification.setter
    def data_quality_app_specification(
        self,
        value: Optional[
            pulumi.Input[DataQualityJobDefinitionDataQualityAppSpecificationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataQualityBaselineConfig")
    def data_quality_baseline_config(
        self,
    ) -> Optional[
        pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigArgs]
    ]: ...
    @data_quality_baseline_config.setter
    def data_quality_baseline_config(
        self,
        value: Optional[
            pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataQualityJobInput")
    def data_quality_job_input(
        self,
    ) -> Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputArgs]]: ...
    @data_quality_job_input.setter
    def data_quality_job_input(
        self,
        value: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataQualityJobOutputConfig")
    def data_quality_job_output_config(
        self,
    ) -> Optional[
        pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigArgs]
    ]: ...
    @data_quality_job_output_config.setter
    def data_quality_job_output_config(
        self,
        value: Optional[
            pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobResources")
    def job_resources(
        self,
    ) -> Optional[pulumi.Input[DataQualityJobDefinitionJobResourcesArgs]]: ...
    @job_resources.setter
    def job_resources(
        self, value: Optional[pulumi.Input[DataQualityJobDefinitionJobResourcesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[pulumi.Input[DataQualityJobDefinitionNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[DataQualityJobDefinitionNetworkConfigArgs]]
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
    @pulumi.getter(name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> Optional[pulumi.Input[DataQualityJobDefinitionStoppingConditionArgs]]: ...
    @stopping_condition.setter
    def stopping_condition(
        self,
        value: Optional[pulumi.Input[DataQualityJobDefinitionStoppingConditionArgs]],
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

@pulumi.type_token(...)
class DataQualityJobDefinition(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_quality_app_specification: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionDataQualityAppSpecificationArgs,
                    DataQualityJobDefinitionDataQualityAppSpecificationArgsDict,
                ]
            ]
        ] = ...,
        data_quality_baseline_config: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionDataQualityBaselineConfigArgs,
                    DataQualityJobDefinitionDataQualityBaselineConfigArgsDict,
                ]
            ]
        ] = ...,
        data_quality_job_input: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionDataQualityJobInputArgs,
                    DataQualityJobDefinitionDataQualityJobInputArgsDict,
                ]
            ]
        ] = ...,
        data_quality_job_output_config: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionDataQualityJobOutputConfigArgs,
                    DataQualityJobDefinitionDataQualityJobOutputConfigArgsDict,
                ]
            ]
        ] = ...,
        job_resources: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionJobResourcesArgs,
                    DataQualityJobDefinitionJobResourcesArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionNetworkConfigArgs,
                    DataQualityJobDefinitionNetworkConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stopping_condition: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionStoppingConditionArgs,
                    DataQualityJobDefinitionStoppingConditionArgsDict,
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
        args: DataQualityJobDefinitionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        data_quality_app_specification: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionDataQualityAppSpecificationArgs,
                    DataQualityJobDefinitionDataQualityAppSpecificationArgsDict,
                ]
            ]
        ] = ...,
        data_quality_baseline_config: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionDataQualityBaselineConfigArgs,
                    DataQualityJobDefinitionDataQualityBaselineConfigArgsDict,
                ]
            ]
        ] = ...,
        data_quality_job_input: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionDataQualityJobInputArgs,
                    DataQualityJobDefinitionDataQualityJobInputArgsDict,
                ]
            ]
        ] = ...,
        data_quality_job_output_config: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionDataQualityJobOutputConfigArgs,
                    DataQualityJobDefinitionDataQualityJobOutputConfigArgsDict,
                ]
            ]
        ] = ...,
        job_resources: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionJobResourcesArgs,
                    DataQualityJobDefinitionJobResourcesArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionNetworkConfigArgs,
                    DataQualityJobDefinitionNetworkConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stopping_condition: Optional[
            pulumi.Input[
                Union[
                    DataQualityJobDefinitionStoppingConditionArgs,
                    DataQualityJobDefinitionStoppingConditionArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> DataQualityJobDefinition: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataQualityAppSpecification")
    def data_quality_app_specification(
        self,
    ) -> pulumi.Output[outputs.DataQualityJobDefinitionDataQualityAppSpecification]: ...
    @_builtins.property
    @pulumi.getter(name="dataQualityBaselineConfig")
    def data_quality_baseline_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.DataQualityJobDefinitionDataQualityBaselineConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dataQualityJobInput")
    def data_quality_job_input(
        self,
    ) -> pulumi.Output[outputs.DataQualityJobDefinitionDataQualityJobInput]: ...
    @_builtins.property
    @pulumi.getter(name="dataQualityJobOutputConfig")
    def data_quality_job_output_config(
        self,
    ) -> pulumi.Output[outputs.DataQualityJobDefinitionDataQualityJobOutputConfig]: ...
    @_builtins.property
    @pulumi.getter(name="jobResources")
    def job_resources(
        self,
    ) -> pulumi.Output[outputs.DataQualityJobDefinitionJobResources]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> pulumi.Output[Optional[outputs.DataQualityJobDefinitionNetworkConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> pulumi.Output[outputs.DataQualityJobDefinitionStoppingCondition]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
