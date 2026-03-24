import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PlanAssociatedAlarm",
    "PlanTimeouts",
    "PlanTrigger",
    "PlanTriggerCondition",
    "PlanWorkflow",
    "PlanWorkflowStep",
    "PlanWorkflowStepArcRoutingControlConfig",
    ...,
    ...,
    "PlanWorkflowStepCustomActionLambdaConfig",
    "PlanWorkflowStepCustomActionLambdaConfigLambda",
    "PlanWorkflowStepCustomActionLambdaConfigUngraceful",
    "PlanWorkflowStepDocumentDbConfig",
    "PlanWorkflowStepDocumentDbConfigUngraceful",
    "PlanWorkflowStepEc2AsgCapacityIncreaseConfig",
    "PlanWorkflowStepEc2AsgCapacityIncreaseConfigAsg",
    ...,
    "PlanWorkflowStepEcsCapacityIncreaseConfig",
    "PlanWorkflowStepEcsCapacityIncreaseConfigService",
    ...,
    "PlanWorkflowStepEksResourceScalingConfig",
    "PlanWorkflowStepEksResourceScalingConfigEksCluster",
    ...,
    ...,
    ...,
    "PlanWorkflowStepEksResourceScalingConfigUngraceful",
    "PlanWorkflowStepExecutionApprovalConfig",
    "PlanWorkflowStepGlobalAuroraConfig",
    "PlanWorkflowStepGlobalAuroraConfigUngraceful",
    "PlanWorkflowStepParallelConfig",
    "PlanWorkflowStepParallelConfigStep",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PlanWorkflowStepParallelConfigStepDocumentDbConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PlanWorkflowStepRegionSwitchPlanConfig",
    "PlanWorkflowStepRoute53HealthCheckConfig",
    "PlanWorkflowStepRoute53HealthCheckConfigRecordSet",
    "GetRoute53HealthChecksHealthCheckResult",
]

@pulumi.output_type
class PlanAssociatedAlarm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        alarm_type: _builtins.str,
        map_block_key: _builtins.str,
        resource_identifier: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alarmType")
    def alarm_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanTrigger(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        min_delay_minutes_between_executions: _builtins.int,
        target_region: _builtins.str,
        conditions: Optional[Sequence[outputs.PlanTriggerCondition]] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minDelayMinutesBetweenExecutions")
    def min_delay_minutes_between_executions(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="targetRegion")
    def target_region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.PlanTriggerCondition]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanTriggerCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, associated_alarm_name: _builtins.str, condition: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associatedAlarmName")
    def associated_alarm_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        workflow_target_action: _builtins.str,
        steps: Optional[Sequence[outputs.PlanWorkflowStep]] = ...,
        workflow_description: Optional[_builtins.str] = ...,
        workflow_target_region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workflowTargetAction")
    def workflow_target_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def steps(self) -> Optional[Sequence[outputs.PlanWorkflowStep]]: ...
    @_builtins.property
    @pulumi.getter(name="workflowDescription")
    def workflow_description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workflowTargetRegion")
    def workflow_target_region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStep(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        execution_block_type: _builtins.str,
        name: _builtins.str,
        arc_routing_control_configs: Optional[
            Sequence[outputs.PlanWorkflowStepArcRoutingControlConfig]
        ] = ...,
        custom_action_lambda_configs: Optional[
            Sequence[outputs.PlanWorkflowStepCustomActionLambdaConfig]
        ] = ...,
        description: Optional[_builtins.str] = ...,
        document_db_configs: Optional[
            Sequence[outputs.PlanWorkflowStepDocumentDbConfig]
        ] = ...,
        ec2_asg_capacity_increase_configs: Optional[
            Sequence[outputs.PlanWorkflowStepEc2AsgCapacityIncreaseConfig]
        ] = ...,
        ecs_capacity_increase_configs: Optional[
            Sequence[outputs.PlanWorkflowStepEcsCapacityIncreaseConfig]
        ] = ...,
        eks_resource_scaling_configs: Optional[
            Sequence[outputs.PlanWorkflowStepEksResourceScalingConfig]
        ] = ...,
        execution_approval_configs: Optional[
            Sequence[outputs.PlanWorkflowStepExecutionApprovalConfig]
        ] = ...,
        global_aurora_configs: Optional[
            Sequence[outputs.PlanWorkflowStepGlobalAuroraConfig]
        ] = ...,
        parallel_configs: Optional[
            Sequence[outputs.PlanWorkflowStepParallelConfig]
        ] = ...,
        region_switch_plan_configs: Optional[
            Sequence[outputs.PlanWorkflowStepRegionSwitchPlanConfig]
        ] = ...,
        route53_health_check_configs: Optional[
            Sequence[outputs.PlanWorkflowStepRoute53HealthCheckConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionBlockType")
    def execution_block_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="arcRoutingControlConfigs")
    def arc_routing_control_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepArcRoutingControlConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="customActionLambdaConfigs")
    def custom_action_lambda_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepCustomActionLambdaConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentDbConfigs")
    def document_db_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepDocumentDbConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="ec2AsgCapacityIncreaseConfigs")
    def ec2_asg_capacity_increase_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepEc2AsgCapacityIncreaseConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="ecsCapacityIncreaseConfigs")
    def ecs_capacity_increase_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepEcsCapacityIncreaseConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="eksResourceScalingConfigs")
    def eks_resource_scaling_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepEksResourceScalingConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="executionApprovalConfigs")
    def execution_approval_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepExecutionApprovalConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="globalAuroraConfigs")
    def global_aurora_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepGlobalAuroraConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="parallelConfigs")
    def parallel_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepParallelConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="regionSwitchPlanConfigs")
    def region_switch_plan_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepRegionSwitchPlanConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="route53HealthCheckConfigs")
    def route53_health_check_configs(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepRoute53HealthCheckConfig]]: ...

@pulumi.output_type
class PlanWorkflowStepArcRoutingControlConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
        region_and_routing_controls: Optional[
            Sequence[
                outputs.PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControl
            ]
        ] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regionAndRoutingControls")
    def region_and_routing_controls(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControl]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControl(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        region: _builtins.str,
        routing_controls: Optional[
            Sequence[
                outputs.PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlRoutingControl
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routingControls")
    def routing_controls(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlRoutingControl
        ]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlRoutingControl(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, routing_control_arn: _builtins.str, state: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routingControlArn")
    def routing_control_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepCustomActionLambdaConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        region_to_run: _builtins.str,
        retry_interval_minutes: _builtins.float,
        lambdas: Optional[
            Sequence[outputs.PlanWorkflowStepCustomActionLambdaConfigLambda]
        ] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungracefuls: Optional[
            Sequence[outputs.PlanWorkflowStepCustomActionLambdaConfigUngraceful]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regionToRun")
    def region_to_run(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retryIntervalMinutes")
    def retry_interval_minutes(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def lambdas(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepCustomActionLambdaConfigLambda]]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepCustomActionLambdaConfigUngraceful]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepCustomActionLambdaConfigLambda(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepCustomActionLambdaConfigUngraceful(dict):
    def __init__(__self__, *, behavior: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepDocumentDbConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        behavior: _builtins.str,
        database_cluster_arns: Sequence[_builtins.str],
        global_cluster_identifier: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungracefuls: Optional[
            Sequence[outputs.PlanWorkflowStepDocumentDbConfigUngraceful]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseClusterArns")
    def database_cluster_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepDocumentDbConfigUngraceful]]: ...

@pulumi.output_type
class PlanWorkflowStepDocumentDbConfigUngraceful(dict):
    def __init__(__self__, *, ungraceful: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepEc2AsgCapacityIncreaseConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: _builtins.str,
        asgs: Optional[
            Sequence[outputs.PlanWorkflowStepEc2AsgCapacityIncreaseConfigAsg]
        ] = ...,
        target_percent: Optional[_builtins.int] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungraceful: Optional[
            outputs.PlanWorkflowStepEc2AsgCapacityIncreaseConfigUngraceful
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def asgs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepEc2AsgCapacityIncreaseConfigAsg]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(
        self,
    ) -> Optional[outputs.PlanWorkflowStepEc2AsgCapacityIncreaseConfigUngraceful]: ...

@pulumi.output_type
class PlanWorkflowStepEc2AsgCapacityIncreaseConfigAsg(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepEc2AsgCapacityIncreaseConfigUngraceful(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, minimum_success_percentage: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> _builtins.int: ...

@pulumi.output_type
class PlanWorkflowStepEcsCapacityIncreaseConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: _builtins.str,
        services: Optional[
            Sequence[outputs.PlanWorkflowStepEcsCapacityIncreaseConfigService]
        ] = ...,
        target_percent: Optional[_builtins.int] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungraceful: Optional[
            outputs.PlanWorkflowStepEcsCapacityIncreaseConfigUngraceful
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepEcsCapacityIncreaseConfigService]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(
        self,
    ) -> Optional[outputs.PlanWorkflowStepEcsCapacityIncreaseConfigUngraceful]: ...

@pulumi.output_type
class PlanWorkflowStepEcsCapacityIncreaseConfigService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_arn: _builtins.str,
        service_arn: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepEcsCapacityIncreaseConfigUngraceful(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, minimum_success_percentage: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> _builtins.int: ...

@pulumi.output_type
class PlanWorkflowStepEksResourceScalingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: _builtins.str,
        target_percent: _builtins.int,
        eks_clusters: Optional[
            Sequence[outputs.PlanWorkflowStepEksResourceScalingConfigEksCluster]
        ] = ...,
        kubernetes_resource_types: Optional[
            Sequence[
                outputs.PlanWorkflowStepEksResourceScalingConfigKubernetesResourceType
            ]
        ] = ...,
        scaling_resources: Optional[
            Sequence[outputs.PlanWorkflowStepEksResourceScalingConfigScalingResource]
        ] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungracefuls: Optional[
            Sequence[outputs.PlanWorkflowStepEksResourceScalingConfigUngraceful]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="eksClusters")
    def eks_clusters(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepEksResourceScalingConfigEksCluster]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesResourceTypes")
    def kubernetes_resource_types(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepEksResourceScalingConfigKubernetesResourceType]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="scalingResources")
    def scaling_resources(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepEksResourceScalingConfigScalingResource]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepEksResourceScalingConfigUngraceful]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepEksResourceScalingConfigEksCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_arn: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepEksResourceScalingConfigKubernetesResourceType(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, api_version: _builtins.str, kind: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepEksResourceScalingConfigScalingResource(dict):
    def __init__(
        __self__,
        *,
        namespace: _builtins.str,
        resources: Optional[
            Sequence[
                outputs.PlanWorkflowStepEksResourceScalingConfigScalingResourceResource
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepEksResourceScalingConfigScalingResourceResource
        ]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepEksResourceScalingConfigScalingResourceResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        namespace: _builtins.str,
        resource_name: _builtins.str,
        hpa_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hpaName")
    def hpa_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepEksResourceScalingConfigUngraceful(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, minimum_success_percentage: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> _builtins.int: ...

@pulumi.output_type
class PlanWorkflowStepExecutionApprovalConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        approval_role: _builtins.str,
        timeout_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalRole")
    def approval_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PlanWorkflowStepGlobalAuroraConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        behavior: _builtins.str,
        database_cluster_arns: Sequence[_builtins.str],
        global_cluster_identifier: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungracefuls: Optional[
            Sequence[outputs.PlanWorkflowStepGlobalAuroraConfigUngraceful]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseClusterArns")
    def database_cluster_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepGlobalAuroraConfigUngraceful]]: ...

@pulumi.output_type
class PlanWorkflowStepGlobalAuroraConfigUngraceful(dict):
    def __init__(__self__, *, ungraceful: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfig(dict):
    def __init__(
        __self__,
        *,
        steps: Optional[Sequence[outputs.PlanWorkflowStepParallelConfigStep]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def steps(
        self,
    ) -> Optional[Sequence[outputs.PlanWorkflowStepParallelConfigStep]]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStep(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        execution_block_type: _builtins.str,
        name: _builtins.str,
        arc_routing_control_configs: Optional[
            Sequence[outputs.PlanWorkflowStepParallelConfigStepArcRoutingControlConfig]
        ] = ...,
        custom_action_lambda_configs: Optional[
            Sequence[outputs.PlanWorkflowStepParallelConfigStepCustomActionLambdaConfig]
        ] = ...,
        description: Optional[_builtins.str] = ...,
        document_db_configs: Optional[
            Sequence[outputs.PlanWorkflowStepParallelConfigStepDocumentDbConfig]
        ] = ...,
        ec2_asg_capacity_increase_configs: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfig
            ]
        ] = ...,
        ecs_capacity_increase_configs: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfig
            ]
        ] = ...,
        eks_resource_scaling_configs: Optional[
            Sequence[outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfig]
        ] = ...,
        execution_approval_configs: Optional[
            Sequence[outputs.PlanWorkflowStepParallelConfigStepExecutionApprovalConfig]
        ] = ...,
        global_aurora_configs: Optional[
            Sequence[outputs.PlanWorkflowStepParallelConfigStepGlobalAuroraConfig]
        ] = ...,
        region_switch_plan_configs: Optional[
            Sequence[outputs.PlanWorkflowStepParallelConfigStepRegionSwitchPlanConfig]
        ] = ...,
        route53_health_check_configs: Optional[
            Sequence[outputs.PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionBlockType")
    def execution_block_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="arcRoutingControlConfigs")
    def arc_routing_control_configs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepArcRoutingControlConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customActionLambdaConfigs")
    def custom_action_lambda_configs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepCustomActionLambdaConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentDbConfigs")
    def document_db_configs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepDocumentDbConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ec2AsgCapacityIncreaseConfigs")
    def ec2_asg_capacity_increase_configs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ecsCapacityIncreaseConfigs")
    def ecs_capacity_increase_configs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="eksResourceScalingConfigs")
    def eks_resource_scaling_configs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="executionApprovalConfigs")
    def execution_approval_configs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepExecutionApprovalConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="globalAuroraConfigs")
    def global_aurora_configs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepGlobalAuroraConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="regionSwitchPlanConfigs")
    def region_switch_plan_configs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepRegionSwitchPlanConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="route53HealthCheckConfigs")
    def route53_health_check_configs(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfig]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepArcRoutingControlConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
        region_and_routing_controls: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControl
            ]
        ] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regionAndRoutingControls")
    def region_and_routing_controls(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControl
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControl(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        region: _builtins.str,
        routing_controls: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlRoutingControl
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routingControls")
    def routing_controls(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlRoutingControl
        ]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlRoutingControl(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, routing_control_arn: _builtins.str, state: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routingControlArn")
    def routing_control_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepCustomActionLambdaConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        region_to_run: _builtins.str,
        retry_interval_minutes: _builtins.float,
        lambdas: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigLambda
            ]
        ] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungracefuls: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigUngraceful
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regionToRun")
    def region_to_run(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retryIntervalMinutes")
    def retry_interval_minutes(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def lambdas(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigLambda
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigUngraceful
        ]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigLambda(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigUngraceful(dict):
    def __init__(__self__, *, behavior: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepDocumentDbConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        behavior: _builtins.str,
        database_cluster_arns: Sequence[_builtins.str],
        global_cluster_identifier: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungracefuls: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepDocumentDbConfigUngraceful
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseClusterArns")
    def database_cluster_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepDocumentDbConfigUngraceful]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepDocumentDbConfigUngraceful(dict):
    def __init__(__self__, *, ungraceful: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: _builtins.str,
        asgs: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigAsg
            ]
        ] = ...,
        target_percent: Optional[_builtins.int] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungraceful: Optional[
            outputs.PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigUngraceful
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def asgs(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigAsg
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(
        self,
    ) -> Optional[
        outputs.PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigUngraceful
    ]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigAsg(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigUngraceful(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, minimum_success_percentage: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> _builtins.int: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: _builtins.str,
        services: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigService
            ]
        ] = ...,
        target_percent: Optional[_builtins.int] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungraceful: Optional[
            outputs.PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigUngraceful
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigService
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(
        self,
    ) -> Optional[
        outputs.PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigUngraceful
    ]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_arn: _builtins.str,
        service_arn: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigUngraceful(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, minimum_success_percentage: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> _builtins.int: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: _builtins.str,
        target_percent: _builtins.int,
        eks_clusters: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfigEksCluster
            ]
        ] = ...,
        kubernetes_resource_types: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfigKubernetesResourceType
            ]
        ] = ...,
        scaling_resources: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResource
            ]
        ] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungracefuls: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfigUngraceful
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="eksClusters")
    def eks_clusters(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfigEksCluster
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesResourceTypes")
    def kubernetes_resource_types(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfigKubernetesResourceType
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="scalingResources")
    def scaling_resources(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResource
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfigUngraceful
        ]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigEksCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_arn: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigKubernetesResourceType(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, api_version: _builtins.str, kind: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResource(dict):
    def __init__(
        __self__,
        *,
        namespace: _builtins.str,
        resources: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceResource
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceResource
        ]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceResource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        namespace: _builtins.str,
        resource_name: _builtins.str,
        hpa_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hpaName")
    def hpa_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigUngraceful(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, minimum_success_percentage: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> _builtins.int: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepExecutionApprovalConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        approval_role: _builtins.str,
        timeout_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalRole")
    def approval_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepGlobalAuroraConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        behavior: _builtins.str,
        database_cluster_arns: Sequence[_builtins.str],
        global_cluster_identifier: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
        ungracefuls: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepGlobalAuroraConfigUngraceful
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseClusterArns")
    def database_cluster_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepParallelConfigStepGlobalAuroraConfigUngraceful]
    ]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepGlobalAuroraConfigUngraceful(dict):
    def __init__(__self__, *, ungraceful: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepRegionSwitchPlanConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hosted_zone_id: _builtins.str,
        record_name: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
        record_sets: Optional[
            Sequence[
                outputs.PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigRecordSet
            ]
        ] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recordName")
    def record_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recordSets")
    def record_sets(
        self,
    ) -> Optional[
        Sequence[
            outputs.PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigRecordSet
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigRecordSet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, record_set_identifier: _builtins.str, region: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordSetIdentifier")
    def record_set_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

@pulumi.output_type
class PlanWorkflowStepRegionSwitchPlanConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanWorkflowStepRoute53HealthCheckConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hosted_zone_id: _builtins.str,
        record_name: _builtins.str,
        cross_account_role: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
        record_sets: Optional[
            Sequence[outputs.PlanWorkflowStepRoute53HealthCheckConfigRecordSet]
        ] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recordName")
    def record_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recordSets")
    def record_sets(
        self,
    ) -> Optional[
        Sequence[outputs.PlanWorkflowStepRoute53HealthCheckConfigRecordSet]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PlanWorkflowStepRoute53HealthCheckConfigRecordSet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, record_set_identifier: _builtins.str, region: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordSetIdentifier")
    def record_set_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

@pulumi.output_type
class GetRoute53HealthChecksHealthCheckResult(dict):
    def __init__(
        __self__,
        *,
        health_check_id: _builtins.str,
        hosted_zone_id: _builtins.str,
        record_name: _builtins.str,
        region: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recordName")
    def record_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
