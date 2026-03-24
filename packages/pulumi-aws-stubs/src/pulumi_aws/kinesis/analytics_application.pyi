import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AnalyticsApplicationArgs", "AnalyticsApplication"]

@pulumi.input_type
class AnalyticsApplicationArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_logging_options: Optional[
            pulumi.Input[AnalyticsApplicationCloudwatchLoggingOptionsArgs]
        ] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        inputs: Optional[pulumi.Input[AnalyticsApplicationInputsArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        outputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationOutputArgs]]]
        ] = ...,
        reference_data_sources: Optional[
            pulumi.Input[AnalyticsApplicationReferenceDataSourcesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        start_application: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[pulumi.Input[AnalyticsApplicationCloudwatchLoggingOptionsArgs]]: ...
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(
        self,
        value: Optional[pulumi.Input[AnalyticsApplicationCloudwatchLoggingOptionsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[AnalyticsApplicationInputsArgs]]: ...
    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[AnalyticsApplicationInputsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationOutputArgs]]]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationOutputArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="referenceDataSources")
    def reference_data_sources(
        self,
    ) -> Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesArgs]]: ...
    @reference_data_sources.setter
    def reference_data_sources(
        self,
        value: Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startApplication")
    def start_application(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @start_application.setter
    def start_application(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
class _AnalyticsApplicationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_logging_options: Optional[
            pulumi.Input[AnalyticsApplicationCloudwatchLoggingOptionsArgs]
        ] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        create_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        inputs: Optional[pulumi.Input[AnalyticsApplicationInputsArgs]] = ...,
        last_update_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        outputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationOutputArgs]]]
        ] = ...,
        reference_data_sources: Optional[
            pulumi.Input[AnalyticsApplicationReferenceDataSourcesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        start_application: Optional[pulumi.Input[_builtins.bool]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[pulumi.Input[AnalyticsApplicationCloudwatchLoggingOptionsArgs]]: ...
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(
        self,
        value: Optional[pulumi.Input[AnalyticsApplicationCloudwatchLoggingOptionsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTimestamp")
    def create_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_timestamp.setter
    def create_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[AnalyticsApplicationInputsArgs]]: ...
    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[AnalyticsApplicationInputsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateTimestamp")
    def last_update_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_update_timestamp.setter
    def last_update_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationOutputArgs]]]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationOutputArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="referenceDataSources")
    def reference_data_sources(
        self,
    ) -> Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesArgs]]: ...
    @reference_data_sources.setter
    def reference_data_sources(
        self,
        value: Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startApplication")
    def start_application(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @start_application.setter
    def start_application(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token(...)
class AnalyticsApplication(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cloudwatch_logging_options: Optional[
            pulumi.Input[
                Union[
                    AnalyticsApplicationCloudwatchLoggingOptionsArgs,
                    AnalyticsApplicationCloudwatchLoggingOptionsArgsDict,
                ]
            ]
        ] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        inputs: Optional[
            pulumi.Input[
                Union[
                    AnalyticsApplicationInputsArgs, AnalyticsApplicationInputsArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        outputs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AnalyticsApplicationOutputArgs,
                            AnalyticsApplicationOutputArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        reference_data_sources: Optional[
            pulumi.Input[
                Union[
                    AnalyticsApplicationReferenceDataSourcesArgs,
                    AnalyticsApplicationReferenceDataSourcesArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        start_application: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AnalyticsApplicationArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_logging_options: Optional[
            pulumi.Input[
                Union[
                    AnalyticsApplicationCloudwatchLoggingOptionsArgs,
                    AnalyticsApplicationCloudwatchLoggingOptionsArgsDict,
                ]
            ]
        ] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        create_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        inputs: Optional[
            pulumi.Input[
                Union[
                    AnalyticsApplicationInputsArgs, AnalyticsApplicationInputsArgsDict
                ]
            ]
        ] = ...,
        last_update_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        outputs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AnalyticsApplicationOutputArgs,
                            AnalyticsApplicationOutputArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        reference_data_sources: Optional[
            pulumi.Input[
                Union[
                    AnalyticsApplicationReferenceDataSourcesArgs,
                    AnalyticsApplicationReferenceDataSourcesArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        start_application: Optional[pulumi.Input[_builtins.bool]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> AnalyticsApplication: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AnalyticsApplicationCloudwatchLoggingOptions]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createTimestamp")
    def create_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> pulumi.Output[Optional[outputs.AnalyticsApplicationInputs]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateTimestamp")
    def last_update_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.AnalyticsApplicationOutput]]]: ...
    @_builtins.property
    @pulumi.getter(name="referenceDataSources")
    def reference_data_sources(
        self,
    ) -> pulumi.Output[Optional[outputs.AnalyticsApplicationReferenceDataSources]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startApplication")
    def start_application(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.int]: ...
