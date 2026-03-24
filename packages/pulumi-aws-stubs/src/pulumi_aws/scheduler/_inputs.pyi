

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ScheduleFlexibleTimeWindowArgs', 'ScheduleFlexibleTimeWindowArgsDict', 'ScheduleTargetArgs', 'ScheduleTargetArgsDict', 'ScheduleTargetDeadLetterConfigArgs', 'ScheduleTargetDeadLetterConfigArgsDict', 'ScheduleTargetEcsParametersArgs', 'ScheduleTargetEcsParametersArgsDict', ..., ..., ..., ..., 'ScheduleTargetEcsParametersPlacementConstraintArgs', ..., 'ScheduleTargetEcsParametersPlacementStrategyArgs', ..., 'ScheduleTargetEventbridgeParametersArgs', 'ScheduleTargetEventbridgeParametersArgsDict', 'ScheduleTargetKinesisParametersArgs', 'ScheduleTargetKinesisParametersArgsDict', 'ScheduleTargetRetryPolicyArgs', 'ScheduleTargetRetryPolicyArgsDict', 'ScheduleTargetSagemakerPipelineParametersArgs', 'ScheduleTargetSagemakerPipelineParametersArgsDict', ..., ..., 'ScheduleTargetSqsParametersArgs', 'ScheduleTargetSqsParametersArgsDict']
class ScheduleFlexibleTimeWindowArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]
    maximum_window_in_minutes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ScheduleFlexibleTimeWindowArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str], maximum_window_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumWindowInMinutes")
    def maximum_window_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_window_in_minutes.setter
    def maximum_window_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ScheduleTargetArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    dead_letter_config: NotRequired[pulumi.Input[ScheduleTargetDeadLetterConfigArgsDict]]
    ecs_parameters: NotRequired[pulumi.Input[ScheduleTargetEcsParametersArgsDict]]
    eventbridge_parameters: NotRequired[pulumi.Input[ScheduleTargetEventbridgeParametersArgsDict]]
    input: NotRequired[pulumi.Input[_builtins.str]]
    kinesis_parameters: NotRequired[pulumi.Input[ScheduleTargetKinesisParametersArgsDict]]
    retry_policy: NotRequired[pulumi.Input[ScheduleTargetRetryPolicyArgsDict]]
    sagemaker_pipeline_parameters: NotRequired[pulumi.Input[ScheduleTargetSagemakerPipelineParametersArgsDict]]
    sqs_parameters: NotRequired[pulumi.Input[ScheduleTargetSqsParametersArgsDict]]


@pulumi.input_type
class ScheduleTargetArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], dead_letter_config: Optional[pulumi.Input[ScheduleTargetDeadLetterConfigArgs]] = ..., ecs_parameters: Optional[pulumi.Input[ScheduleTargetEcsParametersArgs]] = ..., eventbridge_parameters: Optional[pulumi.Input[ScheduleTargetEventbridgeParametersArgs]] = ..., input: Optional[pulumi.Input[_builtins.str]] = ..., kinesis_parameters: Optional[pulumi.Input[ScheduleTargetKinesisParametersArgs]] = ..., retry_policy: Optional[pulumi.Input[ScheduleTargetRetryPolicyArgs]] = ..., sagemaker_pipeline_parameters: Optional[pulumi.Input[ScheduleTargetSagemakerPipelineParametersArgs]] = ..., sqs_parameters: Optional[pulumi.Input[ScheduleTargetSqsParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(self) -> Optional[pulumi.Input[ScheduleTargetDeadLetterConfigArgs]]:
        
        ...
    
    @dead_letter_config.setter
    def dead_letter_config(self, value: Optional[pulumi.Input[ScheduleTargetDeadLetterConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ecsParameters")
    def ecs_parameters(self) -> Optional[pulumi.Input[ScheduleTargetEcsParametersArgs]]:
        
        ...
    
    @ecs_parameters.setter
    def ecs_parameters(self, value: Optional[pulumi.Input[ScheduleTargetEcsParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventbridgeParameters")
    def eventbridge_parameters(self) -> Optional[pulumi.Input[ScheduleTargetEventbridgeParametersArgs]]:
        
        ...
    
    @eventbridge_parameters.setter
    def eventbridge_parameters(self, value: Optional[pulumi.Input[ScheduleTargetEventbridgeParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisParameters")
    def kinesis_parameters(self) -> Optional[pulumi.Input[ScheduleTargetKinesisParametersArgs]]:
        
        ...
    
    @kinesis_parameters.setter
    def kinesis_parameters(self, value: Optional[pulumi.Input[ScheduleTargetKinesisParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[ScheduleTargetRetryPolicyArgs]]:
        
        ...
    
    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input[ScheduleTargetRetryPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerPipelineParameters")
    def sagemaker_pipeline_parameters(self) -> Optional[pulumi.Input[ScheduleTargetSagemakerPipelineParametersArgs]]:
        
        ...
    
    @sagemaker_pipeline_parameters.setter
    def sagemaker_pipeline_parameters(self, value: Optional[pulumi.Input[ScheduleTargetSagemakerPipelineParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsParameters")
    def sqs_parameters(self) -> Optional[pulumi.Input[ScheduleTargetSqsParametersArgs]]:
        
        ...
    
    @sqs_parameters.setter
    def sqs_parameters(self, value: Optional[pulumi.Input[ScheduleTargetSqsParametersArgs]]): # -> None:
        ...
    


class ScheduleTargetDeadLetterConfigArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ScheduleTargetDeadLetterConfigArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ScheduleTargetEcsParametersArgsDict(TypedDict):
    task_definition_arn: pulumi.Input[_builtins.str]
    capacity_provider_strategies: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersCapacityProviderStrategyArgsDict]]]]
    enable_ecs_managed_tags: NotRequired[pulumi.Input[_builtins.bool]]
    enable_execute_command: NotRequired[pulumi.Input[_builtins.bool]]
    group: NotRequired[pulumi.Input[_builtins.str]]
    launch_type: NotRequired[pulumi.Input[_builtins.str]]
    network_configuration: NotRequired[pulumi.Input[ScheduleTargetEcsParametersNetworkConfigurationArgsDict]]
    placement_constraints: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersPlacementConstraintArgsDict]]]]
    placement_strategies: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersPlacementStrategyArgsDict]]]]
    platform_version: NotRequired[pulumi.Input[_builtins.str]]
    propagate_tags: NotRequired[pulumi.Input[_builtins.str]]
    reference_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    task_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ScheduleTargetEcsParametersArgs:
    def __init__(__self__, *, task_definition_arn: pulumi.Input[_builtins.str], capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersCapacityProviderStrategyArgs]]]] = ..., enable_ecs_managed_tags: Optional[pulumi.Input[_builtins.bool]] = ..., enable_execute_command: Optional[pulumi.Input[_builtins.bool]] = ..., group: Optional[pulumi.Input[_builtins.str]] = ..., launch_type: Optional[pulumi.Input[_builtins.str]] = ..., network_configuration: Optional[pulumi.Input[ScheduleTargetEcsParametersNetworkConfigurationArgs]] = ..., placement_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersPlacementConstraintArgs]]]] = ..., placement_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersPlacementStrategyArgs]]]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., propagate_tags: Optional[pulumi.Input[_builtins.str]] = ..., reference_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskDefinitionArn")
    def task_definition_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_definition_arn.setter
    def task_definition_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersCapacityProviderStrategyArgs]]]]:
        
        ...
    
    @capacity_provider_strategies.setter
    def capacity_provider_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersCapacityProviderStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ecs_managed_tags.setter
    def enable_ecs_managed_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_execute_command.setter
    def enable_execute_command(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group.setter
    def group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_type.setter
    def launch_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input[ScheduleTargetEcsParametersNetworkConfigurationArgs]]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input[ScheduleTargetEcsParametersNetworkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersPlacementConstraintArgs]]]]:
        
        ...
    
    @placement_constraints.setter
    def placement_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersPlacementConstraintArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementStrategies")
    def placement_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersPlacementStrategyArgs]]]]:
        
        ...
    
    @placement_strategies.setter
    def placement_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetEcsParametersPlacementStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reference_id.setter
    def reference_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @task_count.setter
    def task_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ScheduleTargetEcsParametersCapacityProviderStrategyArgsDict(TypedDict):
    capacity_provider: pulumi.Input[_builtins.str]
    base: NotRequired[pulumi.Input[_builtins.int]]
    weight: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ScheduleTargetEcsParametersCapacityProviderStrategyArgs:
    def __init__(__self__, *, capacity_provider: pulumi.Input[_builtins.str], base: Optional[pulumi.Input[_builtins.int]] = ..., weight: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @capacity_provider.setter
    def capacity_provider(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @base.setter
    def base(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ScheduleTargetEcsParametersNetworkConfigurationArgsDict(TypedDict):
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    assign_public_ip: NotRequired[pulumi.Input[_builtins.bool]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ScheduleTargetEcsParametersNetworkConfigurationArgs:
    def __init__(__self__, *, subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], assign_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @assign_public_ip.setter
    def assign_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ScheduleTargetEcsParametersPlacementConstraintArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScheduleTargetEcsParametersPlacementConstraintArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], expression: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScheduleTargetEcsParametersPlacementStrategyArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    field: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScheduleTargetEcsParametersPlacementStrategyArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], field: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScheduleTargetEventbridgeParametersArgsDict(TypedDict):
    detail_type: pulumi.Input[_builtins.str]
    source: pulumi.Input[_builtins.str]


@pulumi.input_type
class ScheduleTargetEventbridgeParametersArgs:
    def __init__(__self__, *, detail_type: pulumi.Input[_builtins.str], source: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailType")
    def detail_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @detail_type.setter
    def detail_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ScheduleTargetKinesisParametersArgsDict(TypedDict):
    partition_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class ScheduleTargetKinesisParametersArgs:
    def __init__(__self__, *, partition_key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @partition_key.setter
    def partition_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ScheduleTargetRetryPolicyArgsDict(TypedDict):
    maximum_event_age_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    maximum_retry_attempts: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ScheduleTargetRetryPolicyArgs:
    def __init__(__self__, *, maximum_event_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ScheduleTargetSagemakerPipelineParametersArgsDict(TypedDict):
    pipeline_parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetSagemakerPipelineParametersPipelineParameterArgsDict]]]]


@pulumi.input_type
class ScheduleTargetSagemakerPipelineParametersArgs:
    def __init__(__self__, *, pipeline_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetSagemakerPipelineParametersPipelineParameterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineParameters")
    def pipeline_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetSagemakerPipelineParametersPipelineParameterArgs]]]]:
        
        ...
    
    @pipeline_parameters.setter
    def pipeline_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduleTargetSagemakerPipelineParametersPipelineParameterArgs]]]]): # -> None:
        ...
    


class ScheduleTargetSagemakerPipelineParametersPipelineParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class ScheduleTargetSagemakerPipelineParametersPipelineParameterArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ScheduleTargetSqsParametersArgsDict(TypedDict):
    message_group_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScheduleTargetSqsParametersArgs:
    def __init__(__self__, *, message_group_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroupId")
    def message_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_group_id.setter
    def message_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


