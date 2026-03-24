import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ClassificationJobArgs", "ClassificationJob"]

@pulumi.input_type
class ClassificationJobArgs:
    def __init__(
        __self__,
        *,
        job_type: pulumi.Input[_builtins.str],
        s3_job_definition: pulumi.Input[ClassificationJobS3JobDefinitionArgs],
        custom_data_identifier_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_run: Optional[pulumi.Input[_builtins.bool]] = ...,
        job_status: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sampling_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        schedule_frequency: Optional[
            pulumi.Input[ClassificationJobScheduleFrequencyArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_type.setter
    def job_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3JobDefinition")
    def s3_job_definition(
        self,
    ) -> pulumi.Input[ClassificationJobS3JobDefinitionArgs]: ...
    @s3_job_definition.setter
    def s3_job_definition(
        self, value: pulumi.Input[ClassificationJobS3JobDefinitionArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customDataIdentifierIds")
    def custom_data_identifier_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_data_identifier_ids.setter
    def custom_data_identifier_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialRun")
    def initial_run(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @initial_run.setter
    def initial_run(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="jobStatus")
    def job_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_status.setter
    def job_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samplingPercentage")
    def sampling_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sampling_percentage.setter
    def sampling_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleFrequency")
    def schedule_frequency(
        self,
    ) -> Optional[pulumi.Input[ClassificationJobScheduleFrequencyArgs]]: ...
    @schedule_frequency.setter
    def schedule_frequency(
        self, value: Optional[pulumi.Input[ClassificationJobScheduleFrequencyArgs]]
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
class _ClassificationJobState:
    def __init__(
        __self__,
        *,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_data_identifier_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_run: Optional[pulumi.Input[_builtins.bool]] = ...,
        job_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        job_status: Optional[pulumi.Input[_builtins.str]] = ...,
        job_type: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_job_definition: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionArgs]
        ] = ...,
        sampling_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        schedule_frequency: Optional[
            pulumi.Input[ClassificationJobScheduleFrequencyArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_paused_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClassificationJobUserPausedDetailArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customDataIdentifierIds")
    def custom_data_identifier_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_data_identifier_ids.setter
    def custom_data_identifier_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialRun")
    def initial_run(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @initial_run.setter
    def initial_run(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="jobArn")
    def job_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_arn.setter
    def job_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobStatus")
    def job_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_status.setter
    def job_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_type.setter
    def job_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3JobDefinition")
    def s3_job_definition(
        self,
    ) -> Optional[pulumi.Input[ClassificationJobS3JobDefinitionArgs]]: ...
    @s3_job_definition.setter
    def s3_job_definition(
        self, value: Optional[pulumi.Input[ClassificationJobS3JobDefinitionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="samplingPercentage")
    def sampling_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sampling_percentage.setter
    def sampling_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleFrequency")
    def schedule_frequency(
        self,
    ) -> Optional[pulumi.Input[ClassificationJobScheduleFrequencyArgs]]: ...
    @schedule_frequency.setter
    def schedule_frequency(
        self, value: Optional[pulumi.Input[ClassificationJobScheduleFrequencyArgs]]
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
    @_builtins.property
    @pulumi.getter(name="userPausedDetails")
    def user_paused_details(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClassificationJobUserPausedDetailArgs]]]
    ]: ...
    @user_paused_details.setter
    def user_paused_details(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClassificationJobUserPausedDetailArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:macie2/classificationJob:ClassificationJob")
class ClassificationJob(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        custom_data_identifier_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_run: Optional[pulumi.Input[_builtins.bool]] = ...,
        job_status: Optional[pulumi.Input[_builtins.str]] = ...,
        job_type: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_job_definition: Optional[
            pulumi.Input[
                Union[
                    ClassificationJobS3JobDefinitionArgs,
                    ClassificationJobS3JobDefinitionArgsDict,
                ]
            ]
        ] = ...,
        sampling_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        schedule_frequency: Optional[
            pulumi.Input[
                Union[
                    ClassificationJobScheduleFrequencyArgs,
                    ClassificationJobScheduleFrequencyArgsDict,
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
        args: ClassificationJobArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_data_identifier_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_run: Optional[pulumi.Input[_builtins.bool]] = ...,
        job_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        job_status: Optional[pulumi.Input[_builtins.str]] = ...,
        job_type: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_job_definition: Optional[
            pulumi.Input[
                Union[
                    ClassificationJobS3JobDefinitionArgs,
                    ClassificationJobS3JobDefinitionArgsDict,
                ]
            ]
        ] = ...,
        sampling_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        schedule_frequency: Optional[
            pulumi.Input[
                Union[
                    ClassificationJobScheduleFrequencyArgs,
                    ClassificationJobScheduleFrequencyArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_paused_details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClassificationJobUserPausedDetailArgs,
                            ClassificationJobUserPausedDetailArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> ClassificationJob: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customDataIdentifierIds")
    def custom_data_identifier_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="initialRun")
    def initial_run(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="jobArn")
    def job_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobStatus")
    def job_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3JobDefinition")
    def s3_job_definition(
        self,
    ) -> pulumi.Output[outputs.ClassificationJobS3JobDefinition]: ...
    @_builtins.property
    @pulumi.getter(name="samplingPercentage")
    def sampling_percentage(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleFrequency")
    def schedule_frequency(
        self,
    ) -> pulumi.Output[outputs.ClassificationJobScheduleFrequency]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userPausedDetails")
    def user_paused_details(
        self,
    ) -> pulumi.Output[Sequence[outputs.ClassificationJobUserPausedDetail]]: ...
