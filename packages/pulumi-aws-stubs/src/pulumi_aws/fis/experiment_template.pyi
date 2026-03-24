import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ExperimentTemplateArgs", "ExperimentTemplate"]

@pulumi.input_type
class ExperimentTemplateArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateActionArgs]]],
        description: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        stop_conditions: pulumi.Input[
            Sequence[pulumi.Input[ExperimentTemplateStopConditionArgs]]
        ],
        experiment_options: Optional[
            pulumi.Input[ExperimentTemplateExperimentOptionsArgs]
        ] = ...,
        experiment_report_configuration: Optional[
            pulumi.Input[ExperimentTemplateExperimentReportConfigurationArgs]
        ] = ...,
        log_configuration: Optional[
            pulumi.Input[ExperimentTemplateLogConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateActionArgs]]]: ...
    @actions.setter
    def actions(
        self, value: pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateActionArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stopConditions")
    def stop_conditions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateStopConditionArgs]]]: ...
    @stop_conditions.setter
    def stop_conditions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ExperimentTemplateStopConditionArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="experimentOptions")
    def experiment_options(
        self,
    ) -> Optional[pulumi.Input[ExperimentTemplateExperimentOptionsArgs]]: ...
    @experiment_options.setter
    def experiment_options(
        self, value: Optional[pulumi.Input[ExperimentTemplateExperimentOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="experimentReportConfiguration")
    def experiment_report_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ExperimentTemplateExperimentReportConfigurationArgs]
    ]: ...
    @experiment_report_configuration.setter
    def experiment_report_configuration(
        self,
        value: Optional[
            pulumi.Input[ExperimentTemplateExperimentReportConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(
        self,
    ) -> Optional[pulumi.Input[ExperimentTemplateLogConfigurationArgs]]: ...
    @log_configuration.setter
    def log_configuration(
        self, value: Optional[pulumi.Input[ExperimentTemplateLogConfigurationArgs]]
    ): ...
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
    def targets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetArgs]]]
    ]: ...
    @targets.setter
    def targets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetArgs]]]
        ],
    ): ...

@pulumi.input_type
class _ExperimentTemplateState:
    def __init__(
        __self__,
        *,
        actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateActionArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        experiment_options: Optional[
            pulumi.Input[ExperimentTemplateExperimentOptionsArgs]
        ] = ...,
        experiment_report_configuration: Optional[
            pulumi.Input[ExperimentTemplateExperimentReportConfigurationArgs]
        ] = ...,
        log_configuration: Optional[
            pulumi.Input[ExperimentTemplateLogConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stop_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateStopConditionArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateActionArgs]]]
    ]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="experimentOptions")
    def experiment_options(
        self,
    ) -> Optional[pulumi.Input[ExperimentTemplateExperimentOptionsArgs]]: ...
    @experiment_options.setter
    def experiment_options(
        self, value: Optional[pulumi.Input[ExperimentTemplateExperimentOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="experimentReportConfiguration")
    def experiment_report_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ExperimentTemplateExperimentReportConfigurationArgs]
    ]: ...
    @experiment_report_configuration.setter
    def experiment_report_configuration(
        self,
        value: Optional[
            pulumi.Input[ExperimentTemplateExperimentReportConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(
        self,
    ) -> Optional[pulumi.Input[ExperimentTemplateLogConfigurationArgs]]: ...
    @log_configuration.setter
    def log_configuration(
        self, value: Optional[pulumi.Input[ExperimentTemplateLogConfigurationArgs]]
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
    @pulumi.getter(name="stopConditions")
    def stop_conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateStopConditionArgs]]]
    ]: ...
    @stop_conditions.setter
    def stop_conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateStopConditionArgs]]]
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
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetArgs]]]
    ]: ...
    @targets.setter
    def targets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:fis/experimentTemplate:ExperimentTemplate")
class ExperimentTemplate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExperimentTemplateActionArgs,
                            ExperimentTemplateActionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        experiment_options: Optional[
            pulumi.Input[
                Union[
                    ExperimentTemplateExperimentOptionsArgs,
                    ExperimentTemplateExperimentOptionsArgsDict,
                ]
            ]
        ] = ...,
        experiment_report_configuration: Optional[
            pulumi.Input[
                Union[
                    ExperimentTemplateExperimentReportConfigurationArgs,
                    ExperimentTemplateExperimentReportConfigurationArgsDict,
                ]
            ]
        ] = ...,
        log_configuration: Optional[
            pulumi.Input[
                Union[
                    ExperimentTemplateLogConfigurationArgs,
                    ExperimentTemplateLogConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stop_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExperimentTemplateStopConditionArgs,
                            ExperimentTemplateStopConditionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExperimentTemplateTargetArgs,
                            ExperimentTemplateTargetArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ExperimentTemplateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExperimentTemplateActionArgs,
                            ExperimentTemplateActionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        experiment_options: Optional[
            pulumi.Input[
                Union[
                    ExperimentTemplateExperimentOptionsArgs,
                    ExperimentTemplateExperimentOptionsArgsDict,
                ]
            ]
        ] = ...,
        experiment_report_configuration: Optional[
            pulumi.Input[
                Union[
                    ExperimentTemplateExperimentReportConfigurationArgs,
                    ExperimentTemplateExperimentReportConfigurationArgsDict,
                ]
            ]
        ] = ...,
        log_configuration: Optional[
            pulumi.Input[
                Union[
                    ExperimentTemplateLogConfigurationArgs,
                    ExperimentTemplateLogConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stop_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExperimentTemplateStopConditionArgs,
                            ExperimentTemplateStopConditionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExperimentTemplateTargetArgs,
                            ExperimentTemplateTargetArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> ExperimentTemplate: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[outputs.ExperimentTemplateAction]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="experimentOptions")
    def experiment_options(
        self,
    ) -> pulumi.Output[outputs.ExperimentTemplateExperimentOptions]: ...
    @_builtins.property
    @pulumi.getter(name="experimentReportConfiguration")
    def experiment_report_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ExperimentTemplateExperimentReportConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ExperimentTemplateLogConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stopConditions")
    def stop_conditions(
        self,
    ) -> pulumi.Output[Sequence[outputs.ExperimentTemplateStopCondition]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ExperimentTemplateTarget]]]: ...
