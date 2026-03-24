import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EventTargetArgs", "EventTarget"]

@pulumi.input_type
class EventTargetArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        rule: pulumi.Input[_builtins.str],
        appsync_target: Optional[pulumi.Input[EventTargetAppsyncTargetArgs]] = ...,
        batch_target: Optional[pulumi.Input[EventTargetBatchTargetArgs]] = ...,
        dead_letter_config: Optional[
            pulumi.Input[EventTargetDeadLetterConfigArgs]
        ] = ...,
        ecs_target: Optional[pulumi.Input[EventTargetEcsTargetArgs]] = ...,
        event_bus_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        http_target: Optional[pulumi.Input[EventTargetHttpTargetArgs]] = ...,
        input: Optional[pulumi.Input[_builtins.str]] = ...,
        input_path: Optional[pulumi.Input[_builtins.str]] = ...,
        input_transformer: Optional[
            pulumi.Input[EventTargetInputTransformerArgs]
        ] = ...,
        kinesis_target: Optional[pulumi.Input[EventTargetKinesisTargetArgs]] = ...,
        redshift_target: Optional[pulumi.Input[EventTargetRedshiftTargetArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_policy: Optional[pulumi.Input[EventTargetRetryPolicyArgs]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        run_command_targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[EventTargetRunCommandTargetArgs]]]
        ] = ...,
        sagemaker_pipeline_target: Optional[
            pulumi.Input[EventTargetSagemakerPipelineTargetArgs]
        ] = ...,
        sqs_target: Optional[pulumi.Input[EventTargetSqsTargetArgs]] = ...,
        target_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Input[_builtins.str]: ...
    @rule.setter
    def rule(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appsyncTarget")
    def appsync_target(
        self,
    ) -> Optional[pulumi.Input[EventTargetAppsyncTargetArgs]]: ...
    @appsync_target.setter
    def appsync_target(
        self, value: Optional[pulumi.Input[EventTargetAppsyncTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="batchTarget")
    def batch_target(self) -> Optional[pulumi.Input[EventTargetBatchTargetArgs]]: ...
    @batch_target.setter
    def batch_target(
        self, value: Optional[pulumi.Input[EventTargetBatchTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(
        self,
    ) -> Optional[pulumi.Input[EventTargetDeadLetterConfigArgs]]: ...
    @dead_letter_config.setter
    def dead_letter_config(
        self, value: Optional[pulumi.Input[EventTargetDeadLetterConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecsTarget")
    def ecs_target(self) -> Optional[pulumi.Input[EventTargetEcsTargetArgs]]: ...
    @ecs_target.setter
    def ecs_target(self, value: Optional[pulumi.Input[EventTargetEcsTargetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="eventBusName")
    def event_bus_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_bus_name.setter
    def event_bus_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="httpTarget")
    def http_target(self) -> Optional[pulumi.Input[EventTargetHttpTargetArgs]]: ...
    @http_target.setter
    def http_target(self, value: Optional[pulumi.Input[EventTargetHttpTargetArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input.setter
    def input(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputPath")
    def input_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_path.setter
    def input_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputTransformer")
    def input_transformer(
        self,
    ) -> Optional[pulumi.Input[EventTargetInputTransformerArgs]]: ...
    @input_transformer.setter
    def input_transformer(
        self, value: Optional[pulumi.Input[EventTargetInputTransformerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kinesisTarget")
    def kinesis_target(
        self,
    ) -> Optional[pulumi.Input[EventTargetKinesisTargetArgs]]: ...
    @kinesis_target.setter
    def kinesis_target(
        self, value: Optional[pulumi.Input[EventTargetKinesisTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redshiftTarget")
    def redshift_target(
        self,
    ) -> Optional[pulumi.Input[EventTargetRedshiftTargetArgs]]: ...
    @redshift_target.setter
    def redshift_target(
        self, value: Optional[pulumi.Input[EventTargetRedshiftTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[EventTargetRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(
        self, value: Optional[pulumi.Input[EventTargetRetryPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runCommandTargets")
    def run_command_targets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EventTargetRunCommandTargetArgs]]]
    ]: ...
    @run_command_targets.setter
    def run_command_targets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EventTargetRunCommandTargetArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sagemakerPipelineTarget")
    def sagemaker_pipeline_target(
        self,
    ) -> Optional[pulumi.Input[EventTargetSagemakerPipelineTargetArgs]]: ...
    @sagemaker_pipeline_target.setter
    def sagemaker_pipeline_target(
        self, value: Optional[pulumi.Input[EventTargetSagemakerPipelineTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqsTarget")
    def sqs_target(self) -> Optional[pulumi.Input[EventTargetSqsTargetArgs]]: ...
    @sqs_target.setter
    def sqs_target(self, value: Optional[pulumi.Input[EventTargetSqsTargetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EventTargetState:
    def __init__(
        __self__,
        *,
        appsync_target: Optional[pulumi.Input[EventTargetAppsyncTargetArgs]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        batch_target: Optional[pulumi.Input[EventTargetBatchTargetArgs]] = ...,
        dead_letter_config: Optional[
            pulumi.Input[EventTargetDeadLetterConfigArgs]
        ] = ...,
        ecs_target: Optional[pulumi.Input[EventTargetEcsTargetArgs]] = ...,
        event_bus_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        http_target: Optional[pulumi.Input[EventTargetHttpTargetArgs]] = ...,
        input: Optional[pulumi.Input[_builtins.str]] = ...,
        input_path: Optional[pulumi.Input[_builtins.str]] = ...,
        input_transformer: Optional[
            pulumi.Input[EventTargetInputTransformerArgs]
        ] = ...,
        kinesis_target: Optional[pulumi.Input[EventTargetKinesisTargetArgs]] = ...,
        redshift_target: Optional[pulumi.Input[EventTargetRedshiftTargetArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_policy: Optional[pulumi.Input[EventTargetRetryPolicyArgs]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        rule: Optional[pulumi.Input[_builtins.str]] = ...,
        run_command_targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[EventTargetRunCommandTargetArgs]]]
        ] = ...,
        sagemaker_pipeline_target: Optional[
            pulumi.Input[EventTargetSagemakerPipelineTargetArgs]
        ] = ...,
        sqs_target: Optional[pulumi.Input[EventTargetSqsTargetArgs]] = ...,
        target_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appsyncTarget")
    def appsync_target(
        self,
    ) -> Optional[pulumi.Input[EventTargetAppsyncTargetArgs]]: ...
    @appsync_target.setter
    def appsync_target(
        self, value: Optional[pulumi.Input[EventTargetAppsyncTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="batchTarget")
    def batch_target(self) -> Optional[pulumi.Input[EventTargetBatchTargetArgs]]: ...
    @batch_target.setter
    def batch_target(
        self, value: Optional[pulumi.Input[EventTargetBatchTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(
        self,
    ) -> Optional[pulumi.Input[EventTargetDeadLetterConfigArgs]]: ...
    @dead_letter_config.setter
    def dead_letter_config(
        self, value: Optional[pulumi.Input[EventTargetDeadLetterConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecsTarget")
    def ecs_target(self) -> Optional[pulumi.Input[EventTargetEcsTargetArgs]]: ...
    @ecs_target.setter
    def ecs_target(self, value: Optional[pulumi.Input[EventTargetEcsTargetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="eventBusName")
    def event_bus_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_bus_name.setter
    def event_bus_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="httpTarget")
    def http_target(self) -> Optional[pulumi.Input[EventTargetHttpTargetArgs]]: ...
    @http_target.setter
    def http_target(self, value: Optional[pulumi.Input[EventTargetHttpTargetArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input.setter
    def input(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputPath")
    def input_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_path.setter
    def input_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputTransformer")
    def input_transformer(
        self,
    ) -> Optional[pulumi.Input[EventTargetInputTransformerArgs]]: ...
    @input_transformer.setter
    def input_transformer(
        self, value: Optional[pulumi.Input[EventTargetInputTransformerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kinesisTarget")
    def kinesis_target(
        self,
    ) -> Optional[pulumi.Input[EventTargetKinesisTargetArgs]]: ...
    @kinesis_target.setter
    def kinesis_target(
        self, value: Optional[pulumi.Input[EventTargetKinesisTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redshiftTarget")
    def redshift_target(
        self,
    ) -> Optional[pulumi.Input[EventTargetRedshiftTargetArgs]]: ...
    @redshift_target.setter
    def redshift_target(
        self, value: Optional[pulumi.Input[EventTargetRedshiftTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[EventTargetRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(
        self, value: Optional[pulumi.Input[EventTargetRetryPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule.setter
    def rule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runCommandTargets")
    def run_command_targets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EventTargetRunCommandTargetArgs]]]
    ]: ...
    @run_command_targets.setter
    def run_command_targets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EventTargetRunCommandTargetArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sagemakerPipelineTarget")
    def sagemaker_pipeline_target(
        self,
    ) -> Optional[pulumi.Input[EventTargetSagemakerPipelineTargetArgs]]: ...
    @sagemaker_pipeline_target.setter
    def sagemaker_pipeline_target(
        self, value: Optional[pulumi.Input[EventTargetSagemakerPipelineTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqsTarget")
    def sqs_target(self) -> Optional[pulumi.Input[EventTargetSqsTargetArgs]]: ...
    @sqs_target.setter
    def sqs_target(self, value: Optional[pulumi.Input[EventTargetSqsTargetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:cloudwatch/eventTarget:EventTarget")
class EventTarget(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        appsync_target: Optional[
            pulumi.Input[
                Union[EventTargetAppsyncTargetArgs, EventTargetAppsyncTargetArgsDict]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        batch_target: Optional[
            pulumi.Input[
                Union[EventTargetBatchTargetArgs, EventTargetBatchTargetArgsDict]
            ]
        ] = ...,
        dead_letter_config: Optional[
            pulumi.Input[
                Union[
                    EventTargetDeadLetterConfigArgs, EventTargetDeadLetterConfigArgsDict
                ]
            ]
        ] = ...,
        ecs_target: Optional[
            pulumi.Input[Union[EventTargetEcsTargetArgs, EventTargetEcsTargetArgsDict]]
        ] = ...,
        event_bus_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        http_target: Optional[
            pulumi.Input[
                Union[EventTargetHttpTargetArgs, EventTargetHttpTargetArgsDict]
            ]
        ] = ...,
        input: Optional[pulumi.Input[_builtins.str]] = ...,
        input_path: Optional[pulumi.Input[_builtins.str]] = ...,
        input_transformer: Optional[
            pulumi.Input[
                Union[
                    EventTargetInputTransformerArgs, EventTargetInputTransformerArgsDict
                ]
            ]
        ] = ...,
        kinesis_target: Optional[
            pulumi.Input[
                Union[EventTargetKinesisTargetArgs, EventTargetKinesisTargetArgsDict]
            ]
        ] = ...,
        redshift_target: Optional[
            pulumi.Input[
                Union[EventTargetRedshiftTargetArgs, EventTargetRedshiftTargetArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_policy: Optional[
            pulumi.Input[
                Union[EventTargetRetryPolicyArgs, EventTargetRetryPolicyArgsDict]
            ]
        ] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        rule: Optional[pulumi.Input[_builtins.str]] = ...,
        run_command_targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EventTargetRunCommandTargetArgs,
                            EventTargetRunCommandTargetArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        sagemaker_pipeline_target: Optional[
            pulumi.Input[
                Union[
                    EventTargetSagemakerPipelineTargetArgs,
                    EventTargetSagemakerPipelineTargetArgsDict,
                ]
            ]
        ] = ...,
        sqs_target: Optional[
            pulumi.Input[Union[EventTargetSqsTargetArgs, EventTargetSqsTargetArgsDict]]
        ] = ...,
        target_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EventTargetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        appsync_target: Optional[
            pulumi.Input[
                Union[EventTargetAppsyncTargetArgs, EventTargetAppsyncTargetArgsDict]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        batch_target: Optional[
            pulumi.Input[
                Union[EventTargetBatchTargetArgs, EventTargetBatchTargetArgsDict]
            ]
        ] = ...,
        dead_letter_config: Optional[
            pulumi.Input[
                Union[
                    EventTargetDeadLetterConfigArgs, EventTargetDeadLetterConfigArgsDict
                ]
            ]
        ] = ...,
        ecs_target: Optional[
            pulumi.Input[Union[EventTargetEcsTargetArgs, EventTargetEcsTargetArgsDict]]
        ] = ...,
        event_bus_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        http_target: Optional[
            pulumi.Input[
                Union[EventTargetHttpTargetArgs, EventTargetHttpTargetArgsDict]
            ]
        ] = ...,
        input: Optional[pulumi.Input[_builtins.str]] = ...,
        input_path: Optional[pulumi.Input[_builtins.str]] = ...,
        input_transformer: Optional[
            pulumi.Input[
                Union[
                    EventTargetInputTransformerArgs, EventTargetInputTransformerArgsDict
                ]
            ]
        ] = ...,
        kinesis_target: Optional[
            pulumi.Input[
                Union[EventTargetKinesisTargetArgs, EventTargetKinesisTargetArgsDict]
            ]
        ] = ...,
        redshift_target: Optional[
            pulumi.Input[
                Union[EventTargetRedshiftTargetArgs, EventTargetRedshiftTargetArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_policy: Optional[
            pulumi.Input[
                Union[EventTargetRetryPolicyArgs, EventTargetRetryPolicyArgsDict]
            ]
        ] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        rule: Optional[pulumi.Input[_builtins.str]] = ...,
        run_command_targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EventTargetRunCommandTargetArgs,
                            EventTargetRunCommandTargetArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        sagemaker_pipeline_target: Optional[
            pulumi.Input[
                Union[
                    EventTargetSagemakerPipelineTargetArgs,
                    EventTargetSagemakerPipelineTargetArgsDict,
                ]
            ]
        ] = ...,
        sqs_target: Optional[
            pulumi.Input[Union[EventTargetSqsTargetArgs, EventTargetSqsTargetArgsDict]]
        ] = ...,
        target_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EventTarget: ...
    @_builtins.property
    @pulumi.getter(name="appsyncTarget")
    def appsync_target(
        self,
    ) -> pulumi.Output[Optional[outputs.EventTargetAppsyncTarget]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="batchTarget")
    def batch_target(
        self,
    ) -> pulumi.Output[Optional[outputs.EventTargetBatchTarget]]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(
        self,
    ) -> pulumi.Output[Optional[outputs.EventTargetDeadLetterConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="ecsTarget")
    def ecs_target(self) -> pulumi.Output[Optional[outputs.EventTargetEcsTarget]]: ...
    @_builtins.property
    @pulumi.getter(name="eventBusName")
    def event_bus_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="httpTarget")
    def http_target(self) -> pulumi.Output[Optional[outputs.EventTargetHttpTarget]]: ...
    @_builtins.property
    @pulumi.getter
    def input(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inputPath")
    def input_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inputTransformer")
    def input_transformer(
        self,
    ) -> pulumi.Output[Optional[outputs.EventTargetInputTransformer]]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisTarget")
    def kinesis_target(
        self,
    ) -> pulumi.Output[Optional[outputs.EventTargetKinesisTarget]]: ...
    @_builtins.property
    @pulumi.getter(name="redshiftTarget")
    def redshift_target(
        self,
    ) -> pulumi.Output[Optional[outputs.EventTargetRedshiftTarget]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.EventTargetRetryPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runCommandTargets")
    def run_command_targets(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.EventTargetRunCommandTarget]]]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerPipelineTarget")
    def sagemaker_pipeline_target(
        self,
    ) -> pulumi.Output[Optional[outputs.EventTargetSagemakerPipelineTarget]]: ...
    @_builtins.property
    @pulumi.getter(name="sqsTarget")
    def sqs_target(self) -> pulumi.Output[Optional[outputs.EventTargetSqsTarget]]: ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[_builtins.str]: ...
