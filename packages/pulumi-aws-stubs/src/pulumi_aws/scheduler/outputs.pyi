import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ScheduleFlexibleTimeWindow",
    "ScheduleTarget",
    "ScheduleTargetDeadLetterConfig",
    "ScheduleTargetEcsParameters",
    ...,
    "ScheduleTargetEcsParametersNetworkConfiguration",
    "ScheduleTargetEcsParametersPlacementConstraint",
    "ScheduleTargetEcsParametersPlacementStrategy",
    "ScheduleTargetEventbridgeParameters",
    "ScheduleTargetKinesisParameters",
    "ScheduleTargetRetryPolicy",
    "ScheduleTargetSagemakerPipelineParameters",
    ...,
    "ScheduleTargetSqsParameters",
]

@pulumi.output_type
class ScheduleFlexibleTimeWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mode: _builtins.str,
        maximum_window_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maximumWindowInMinutes")
    def maximum_window_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScheduleTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        role_arn: _builtins.str,
        dead_letter_config: Optional[outputs.ScheduleTargetDeadLetterConfig] = ...,
        ecs_parameters: Optional[outputs.ScheduleTargetEcsParameters] = ...,
        eventbridge_parameters: Optional[
            outputs.ScheduleTargetEventbridgeParameters
        ] = ...,
        input: Optional[_builtins.str] = ...,
        kinesis_parameters: Optional[outputs.ScheduleTargetKinesisParameters] = ...,
        retry_policy: Optional[outputs.ScheduleTargetRetryPolicy] = ...,
        sagemaker_pipeline_parameters: Optional[
            outputs.ScheduleTargetSagemakerPipelineParameters
        ] = ...,
        sqs_parameters: Optional[outputs.ScheduleTargetSqsParameters] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(
        self,
    ) -> Optional[outputs.ScheduleTargetDeadLetterConfig]: ...
    @_builtins.property
    @pulumi.getter(name="ecsParameters")
    def ecs_parameters(self) -> Optional[outputs.ScheduleTargetEcsParameters]: ...
    @_builtins.property
    @pulumi.getter(name="eventbridgeParameters")
    def eventbridge_parameters(
        self,
    ) -> Optional[outputs.ScheduleTargetEventbridgeParameters]: ...
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisParameters")
    def kinesis_parameters(
        self,
    ) -> Optional[outputs.ScheduleTargetKinesisParameters]: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.ScheduleTargetRetryPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerPipelineParameters")
    def sagemaker_pipeline_parameters(
        self,
    ) -> Optional[outputs.ScheduleTargetSagemakerPipelineParameters]: ...
    @_builtins.property
    @pulumi.getter(name="sqsParameters")
    def sqs_parameters(self) -> Optional[outputs.ScheduleTargetSqsParameters]: ...

@pulumi.output_type
class ScheduleTargetDeadLetterConfig(dict):
    def __init__(__self__, *, arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...

@pulumi.output_type
class ScheduleTargetEcsParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        task_definition_arn: _builtins.str,
        capacity_provider_strategies: Optional[
            Sequence[outputs.ScheduleTargetEcsParametersCapacityProviderStrategy]
        ] = ...,
        enable_ecs_managed_tags: Optional[_builtins.bool] = ...,
        enable_execute_command: Optional[_builtins.bool] = ...,
        group: Optional[_builtins.str] = ...,
        launch_type: Optional[_builtins.str] = ...,
        network_configuration: Optional[
            outputs.ScheduleTargetEcsParametersNetworkConfiguration
        ] = ...,
        placement_constraints: Optional[
            Sequence[outputs.ScheduleTargetEcsParametersPlacementConstraint]
        ] = ...,
        placement_strategies: Optional[
            Sequence[outputs.ScheduleTargetEcsParametersPlacementStrategy]
        ] = ...,
        platform_version: Optional[_builtins.str] = ...,
        propagate_tags: Optional[_builtins.str] = ...,
        reference_id: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        task_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskDefinitionArn")
    def task_definition_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(
        self,
    ) -> Optional[
        Sequence[outputs.ScheduleTargetEcsParametersCapacityProviderStrategy]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[outputs.ScheduleTargetEcsParametersNetworkConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(
        self,
    ) -> Optional[Sequence[outputs.ScheduleTargetEcsParametersPlacementConstraint]]: ...
    @_builtins.property
    @pulumi.getter(name="placementStrategies")
    def placement_strategies(
        self,
    ) -> Optional[Sequence[outputs.ScheduleTargetEcsParametersPlacementStrategy]]: ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScheduleTargetEcsParametersCapacityProviderStrategy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_provider: _builtins.str,
        base: Optional[_builtins.int] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScheduleTargetEcsParametersNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnets: Sequence[_builtins.str],
        assign_public_ip: Optional[_builtins.bool] = ...,
        security_groups: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ScheduleTargetEcsParametersPlacementConstraint(dict):
    def __init__(
        __self__, *, type: _builtins.str, expression: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduleTargetEcsParametersPlacementStrategy(dict):
    def __init__(
        __self__, *, type: _builtins.str, field: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduleTargetEventbridgeParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, detail_type: _builtins.str, source: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="detailType")
    def detail_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...

@pulumi.output_type
class ScheduleTargetKinesisParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, partition_key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> _builtins.str: ...

@pulumi.output_type
class ScheduleTargetRetryPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum_event_age_in_seconds: Optional[_builtins.int] = ...,
        maximum_retry_attempts: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScheduleTargetSagemakerPipelineParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pipeline_parameters: Optional[
            Sequence[outputs.ScheduleTargetSagemakerPipelineParametersPipelineParameter]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pipelineParameters")
    def pipeline_parameters(
        self,
    ) -> Optional[
        Sequence[outputs.ScheduleTargetSagemakerPipelineParametersPipelineParameter]
    ]: ...

@pulumi.output_type
class ScheduleTargetSagemakerPipelineParametersPipelineParameter(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ScheduleTargetSqsParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, message_group_id: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageGroupId")
    def message_group_id(self) -> Optional[_builtins.str]: ...
