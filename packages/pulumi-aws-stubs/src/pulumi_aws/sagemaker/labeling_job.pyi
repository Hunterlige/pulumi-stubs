import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LabelingJobArgs", "LabelingJob"]

@pulumi.input_type
class LabelingJobArgs:
    def __init__(
        __self__,
        *,
        human_task_config: pulumi.Input[LabelingJobHumanTaskConfigArgs],
        input_config: pulumi.Input[LabelingJobInputConfigArgs],
        label_attribute_name: pulumi.Input[_builtins.str],
        labeling_job_name: pulumi.Input[_builtins.str],
        output_config: pulumi.Input[LabelingJobOutputConfigArgs],
        role_arn: pulumi.Input[_builtins.str],
        label_category_config_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        labeling_job_algorithms_config: Optional[
            pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stopping_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[LabelingJobStoppingConditionArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="humanTaskConfig")
    def human_task_config(self) -> pulumi.Input[LabelingJobHumanTaskConfigArgs]: ...
    @human_task_config.setter
    def human_task_config(
        self, value: pulumi.Input[LabelingJobHumanTaskConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputConfig")
    def input_config(self) -> pulumi.Input[LabelingJobInputConfigArgs]: ...
    @input_config.setter
    def input_config(self, value: pulumi.Input[LabelingJobInputConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="labelAttributeName")
    def label_attribute_name(self) -> pulumi.Input[_builtins.str]: ...
    @label_attribute_name.setter
    def label_attribute_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="labelingJobName")
    def labeling_job_name(self) -> pulumi.Input[_builtins.str]: ...
    @labeling_job_name.setter
    def labeling_job_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> pulumi.Input[LabelingJobOutputConfigArgs]: ...
    @output_config.setter
    def output_config(self, value: pulumi.Input[LabelingJobOutputConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="labelCategoryConfigS3Uri")
    def label_category_config_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label_category_config_s3_uri.setter
    def label_category_config_s3_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="labelingJobAlgorithmsConfig")
    def labeling_job_algorithms_config(
        self,
    ) -> Optional[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigArgs]]: ...
    @labeling_job_algorithms_config.setter
    def labeling_job_algorithms_config(
        self, value: Optional[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stoppingConditions")
    def stopping_conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LabelingJobStoppingConditionArgs]]]
    ]: ...
    @stopping_conditions.setter
    def stopping_conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LabelingJobStoppingConditionArgs]]]
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
class _LabelingJobState:
    def __init__(
        __self__,
        *,
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        human_task_config: Optional[pulumi.Input[LabelingJobHumanTaskConfigArgs]] = ...,
        input_config: Optional[pulumi.Input[LabelingJobInputConfigArgs]] = ...,
        job_reference_code: Optional[pulumi.Input[_builtins.str]] = ...,
        label_attribute_name: Optional[pulumi.Input[_builtins.str]] = ...,
        label_category_config_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        label_counters: Optional[
            pulumi.Input[Sequence[pulumi.Input[LabelingJobLabelCounterArgs]]]
        ] = ...,
        labeling_job_algorithms_config: Optional[
            pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigArgs]
        ] = ...,
        labeling_job_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        labeling_job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labeling_job_status: Optional[pulumi.Input[_builtins.str]] = ...,
        output_config: Optional[pulumi.Input[LabelingJobOutputConfigArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stopping_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[LabelingJobStoppingConditionArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="humanTaskConfig")
    def human_task_config(
        self,
    ) -> Optional[pulumi.Input[LabelingJobHumanTaskConfigArgs]]: ...
    @human_task_config.setter
    def human_task_config(
        self, value: Optional[pulumi.Input[LabelingJobHumanTaskConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputConfig")
    def input_config(self) -> Optional[pulumi.Input[LabelingJobInputConfigArgs]]: ...
    @input_config.setter
    def input_config(
        self, value: Optional[pulumi.Input[LabelingJobInputConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobReferenceCode")
    def job_reference_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_reference_code.setter
    def job_reference_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labelAttributeName")
    def label_attribute_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label_attribute_name.setter
    def label_attribute_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labelCategoryConfigS3Uri")
    def label_category_config_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label_category_config_s3_uri.setter
    def label_category_config_s3_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="labelCounters")
    def label_counters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LabelingJobLabelCounterArgs]]]
    ]: ...
    @label_counters.setter
    def label_counters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LabelingJobLabelCounterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="labelingJobAlgorithmsConfig")
    def labeling_job_algorithms_config(
        self,
    ) -> Optional[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigArgs]]: ...
    @labeling_job_algorithms_config.setter
    def labeling_job_algorithms_config(
        self, value: Optional[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="labelingJobArn")
    def labeling_job_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @labeling_job_arn.setter
    def labeling_job_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labelingJobName")
    def labeling_job_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @labeling_job_name.setter
    def labeling_job_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labelingJobStatus")
    def labeling_job_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @labeling_job_status.setter
    def labeling_job_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> Optional[pulumi.Input[LabelingJobOutputConfigArgs]]: ...
    @output_config.setter
    def output_config(
        self, value: Optional[pulumi.Input[LabelingJobOutputConfigArgs]]
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
    @pulumi.getter(name="stoppingConditions")
    def stopping_conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LabelingJobStoppingConditionArgs]]]
    ]: ...
    @stopping_conditions.setter
    def stopping_conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LabelingJobStoppingConditionArgs]]]
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

@pulumi.type_token("aws:sagemaker/labelingJob:LabelingJob")
class LabelingJob(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        human_task_config: Optional[
            pulumi.Input[
                Union[
                    LabelingJobHumanTaskConfigArgs, LabelingJobHumanTaskConfigArgsDict
                ]
            ]
        ] = ...,
        input_config: Optional[
            pulumi.Input[
                Union[LabelingJobInputConfigArgs, LabelingJobInputConfigArgsDict]
            ]
        ] = ...,
        label_attribute_name: Optional[pulumi.Input[_builtins.str]] = ...,
        label_category_config_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        labeling_job_algorithms_config: Optional[
            pulumi.Input[
                Union[
                    LabelingJobLabelingJobAlgorithmsConfigArgs,
                    LabelingJobLabelingJobAlgorithmsConfigArgsDict,
                ]
            ]
        ] = ...,
        labeling_job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_config: Optional[
            pulumi.Input[
                Union[LabelingJobOutputConfigArgs, LabelingJobOutputConfigArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stopping_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LabelingJobStoppingConditionArgs,
                            LabelingJobStoppingConditionArgsDict,
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
        args: LabelingJobArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        human_task_config: Optional[
            pulumi.Input[
                Union[
                    LabelingJobHumanTaskConfigArgs, LabelingJobHumanTaskConfigArgsDict
                ]
            ]
        ] = ...,
        input_config: Optional[
            pulumi.Input[
                Union[LabelingJobInputConfigArgs, LabelingJobInputConfigArgsDict]
            ]
        ] = ...,
        job_reference_code: Optional[pulumi.Input[_builtins.str]] = ...,
        label_attribute_name: Optional[pulumi.Input[_builtins.str]] = ...,
        label_category_config_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        label_counters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LabelingJobLabelCounterArgs, LabelingJobLabelCounterArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        labeling_job_algorithms_config: Optional[
            pulumi.Input[
                Union[
                    LabelingJobLabelingJobAlgorithmsConfigArgs,
                    LabelingJobLabelingJobAlgorithmsConfigArgsDict,
                ]
            ]
        ] = ...,
        labeling_job_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        labeling_job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labeling_job_status: Optional[pulumi.Input[_builtins.str]] = ...,
        output_config: Optional[
            pulumi.Input[
                Union[LabelingJobOutputConfigArgs, LabelingJobOutputConfigArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stopping_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LabelingJobStoppingConditionArgs,
                            LabelingJobStoppingConditionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> LabelingJob: ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="humanTaskConfig")
    def human_task_config(
        self,
    ) -> pulumi.Output[outputs.LabelingJobHumanTaskConfig]: ...
    @_builtins.property
    @pulumi.getter(name="inputConfig")
    def input_config(self) -> pulumi.Output[outputs.LabelingJobInputConfig]: ...
    @_builtins.property
    @pulumi.getter(name="jobReferenceCode")
    def job_reference_code(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labelAttributeName")
    def label_attribute_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labelCategoryConfigS3Uri")
    def label_category_config_s3_uri(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="labelCounters")
    def label_counters(
        self,
    ) -> pulumi.Output[Sequence[outputs.LabelingJobLabelCounter]]: ...
    @_builtins.property
    @pulumi.getter(name="labelingJobAlgorithmsConfig")
    def labeling_job_algorithms_config(
        self,
    ) -> pulumi.Output[Optional[outputs.LabelingJobLabelingJobAlgorithmsConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="labelingJobArn")
    def labeling_job_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labelingJobName")
    def labeling_job_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labelingJobStatus")
    def labeling_job_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> pulumi.Output[outputs.LabelingJobOutputConfig]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stoppingConditions")
    def stopping_conditions(
        self,
    ) -> pulumi.Output[Sequence[outputs.LabelingJobStoppingCondition]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
