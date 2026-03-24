import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PlanAssociatedAlarmArgs",
    "PlanAssociatedAlarmArgsDict",
    "PlanTimeoutsArgs",
    "PlanTimeoutsArgsDict",
    "PlanTriggerArgs",
    "PlanTriggerArgsDict",
    "PlanTriggerConditionArgs",
    "PlanTriggerConditionArgsDict",
    "PlanWorkflowArgs",
    "PlanWorkflowArgsDict",
    "PlanWorkflowStepArgs",
    "PlanWorkflowStepArgsDict",
    "PlanWorkflowStepArcRoutingControlConfigArgs",
    "PlanWorkflowStepArcRoutingControlConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "PlanWorkflowStepCustomActionLambdaConfigArgs",
    "PlanWorkflowStepCustomActionLambdaConfigArgsDict",
    "PlanWorkflowStepCustomActionLambdaConfigLambdaArgs",
    ...,
    ...,
    ...,
    "PlanWorkflowStepDocumentDbConfigArgs",
    "PlanWorkflowStepDocumentDbConfigArgsDict",
    "PlanWorkflowStepDocumentDbConfigUngracefulArgs",
    "PlanWorkflowStepDocumentDbConfigUngracefulArgsDict",
    "PlanWorkflowStepEc2AsgCapacityIncreaseConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "PlanWorkflowStepEcsCapacityIncreaseConfigArgs",
    "PlanWorkflowStepEcsCapacityIncreaseConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "PlanWorkflowStepEksResourceScalingConfigArgs",
    "PlanWorkflowStepEksResourceScalingConfigArgsDict",
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
    "PlanWorkflowStepExecutionApprovalConfigArgs",
    "PlanWorkflowStepExecutionApprovalConfigArgsDict",
    "PlanWorkflowStepGlobalAuroraConfigArgs",
    "PlanWorkflowStepGlobalAuroraConfigArgsDict",
    "PlanWorkflowStepGlobalAuroraConfigUngracefulArgs",
    ...,
    "PlanWorkflowStepParallelConfigArgs",
    "PlanWorkflowStepParallelConfigArgsDict",
    "PlanWorkflowStepParallelConfigStepArgs",
    "PlanWorkflowStepParallelConfigStepArgsDict",
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
    "PlanWorkflowStepRegionSwitchPlanConfigArgs",
    "PlanWorkflowStepRegionSwitchPlanConfigArgsDict",
    "PlanWorkflowStepRoute53HealthCheckConfigArgs",
    "PlanWorkflowStepRoute53HealthCheckConfigArgsDict",
    ...,
    ...,
]

class PlanAssociatedAlarmArgsDict(TypedDict):
    alarm_type: pulumi.Input[_builtins.str]
    map_block_key: pulumi.Input[_builtins.str]
    resource_identifier: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanAssociatedAlarmArgs:
    def __init__(
        __self__,
        *,
        alarm_type: pulumi.Input[_builtins.str],
        map_block_key: pulumi.Input[_builtins.str],
        resource_identifier: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alarmType")
    def alarm_type(self) -> pulumi.Input[_builtins.str]: ...
    @alarm_type.setter
    def alarm_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> pulumi.Input[_builtins.str]: ...
    @map_block_key.setter
    def map_block_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @resource_identifier.setter
    def resource_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanTriggerArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    min_delay_minutes_between_executions: pulumi.Input[_builtins.int]
    target_region: pulumi.Input[_builtins.str]
    conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PlanTriggerConditionArgsDict]]]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanTriggerArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        min_delay_minutes_between_executions: pulumi.Input[_builtins.int],
        target_region: pulumi.Input[_builtins.str],
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanTriggerConditionArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="minDelayMinutesBetweenExecutions")
    def min_delay_minutes_between_executions(self) -> pulumi.Input[_builtins.int]: ...
    @min_delay_minutes_between_executions.setter
    def min_delay_minutes_between_executions(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetRegion")
    def target_region(self) -> pulumi.Input[_builtins.str]: ...
    @target_region.setter
    def target_region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanTriggerConditionArgs]]]]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanTriggerConditionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanTriggerConditionArgsDict(TypedDict):
    associated_alarm_name: pulumi.Input[_builtins.str]
    condition: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanTriggerConditionArgs:
    def __init__(
        __self__,
        *,
        associated_alarm_name: pulumi.Input[_builtins.str],
        condition: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associatedAlarmName")
    def associated_alarm_name(self) -> pulumi.Input[_builtins.str]: ...
    @associated_alarm_name.setter
    def associated_alarm_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Input[_builtins.str]: ...
    @condition.setter
    def condition(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowArgsDict(TypedDict):
    workflow_target_action: pulumi.Input[_builtins.str]
    steps: NotRequired[pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepArgsDict]]]]
    workflow_description: NotRequired[pulumi.Input[_builtins.str]]
    workflow_target_region: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowArgs:
    def __init__(
        __self__,
        *,
        workflow_target_action: pulumi.Input[_builtins.str],
        steps: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepArgs]]]
        ] = ...,
        workflow_description: Optional[pulumi.Input[_builtins.str]] = ...,
        workflow_target_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workflowTargetAction")
    def workflow_target_action(self) -> pulumi.Input[_builtins.str]: ...
    @workflow_target_action.setter
    def workflow_target_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def steps(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepArgs]]]]: ...
    @steps.setter
    def steps(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workflowDescription")
    def workflow_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workflow_description.setter
    def workflow_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workflowTargetRegion")
    def workflow_target_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workflow_target_region.setter
    def workflow_target_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepArgsDict(TypedDict):
    execution_block_type: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    arc_routing_control_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepArcRoutingControlConfigArgsDict]]
        ]
    ]
    custom_action_lambda_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigArgsDict]]
        ]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    document_db_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepDocumentDbConfigArgsDict]]]
    ]
    ec2_asg_capacity_increase_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigArgsDict]]
        ]
    ]
    ecs_capacity_increase_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigArgsDict]]
        ]
    ]
    eks_resource_scaling_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepEksResourceScalingConfigArgsDict]]
        ]
    ]
    execution_approval_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepExecutionApprovalConfigArgsDict]]
        ]
    ]
    global_aurora_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepGlobalAuroraConfigArgsDict]]]
    ]
    parallel_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepParallelConfigArgsDict]]]
    ]
    region_switch_plan_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepRegionSwitchPlanConfigArgsDict]]
        ]
    ]
    route53_health_check_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepRoute53HealthCheckConfigArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepArgs:
    def __init__(
        __self__,
        *,
        execution_block_type: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        arc_routing_control_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepArcRoutingControlConfigArgs]]
            ]
        ] = ...,
        custom_action_lambda_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigArgs]]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        document_db_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepDocumentDbConfigArgs]]]
        ] = ...,
        ec2_asg_capacity_increase_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigArgs]]
            ]
        ] = ...,
        ecs_capacity_increase_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigArgs]]
            ]
        ] = ...,
        eks_resource_scaling_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepEksResourceScalingConfigArgs]]
            ]
        ] = ...,
        execution_approval_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepExecutionApprovalConfigArgs]]
            ]
        ] = ...,
        global_aurora_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepGlobalAuroraConfigArgs]]]
        ] = ...,
        parallel_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepParallelConfigArgs]]]
        ] = ...,
        region_switch_plan_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepRegionSwitchPlanConfigArgs]]
            ]
        ] = ...,
        route53_health_check_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepRoute53HealthCheckConfigArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionBlockType")
    def execution_block_type(self) -> pulumi.Input[_builtins.str]: ...
    @execution_block_type.setter
    def execution_block_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="arcRoutingControlConfigs")
    def arc_routing_control_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepArcRoutingControlConfigArgs]]
        ]
    ]: ...
    @arc_routing_control_configs.setter
    def arc_routing_control_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepArcRoutingControlConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customActionLambdaConfigs")
    def custom_action_lambda_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigArgs]]
        ]
    ]: ...
    @custom_action_lambda_configs.setter
    def custom_action_lambda_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentDbConfigs")
    def document_db_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepDocumentDbConfigArgs]]]
    ]: ...
    @document_db_configs.setter
    def document_db_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepDocumentDbConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ec2AsgCapacityIncreaseConfigs")
    def ec2_asg_capacity_increase_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigArgs]]
        ]
    ]: ...
    @ec2_asg_capacity_increase_configs.setter
    def ec2_asg_capacity_increase_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecsCapacityIncreaseConfigs")
    def ecs_capacity_increase_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigArgs]]
        ]
    ]: ...
    @ecs_capacity_increase_configs.setter
    def ecs_capacity_increase_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eksResourceScalingConfigs")
    def eks_resource_scaling_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepEksResourceScalingConfigArgs]]
        ]
    ]: ...
    @eks_resource_scaling_configs.setter
    def eks_resource_scaling_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepEksResourceScalingConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionApprovalConfigs")
    def execution_approval_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepExecutionApprovalConfigArgs]]
        ]
    ]: ...
    @execution_approval_configs.setter
    def execution_approval_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepExecutionApprovalConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalAuroraConfigs")
    def global_aurora_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepGlobalAuroraConfigArgs]]]
    ]: ...
    @global_aurora_configs.setter
    def global_aurora_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepGlobalAuroraConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parallelConfigs")
    def parallel_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepParallelConfigArgs]]]
    ]: ...
    @parallel_configs.setter
    def parallel_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepParallelConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="regionSwitchPlanConfigs")
    def region_switch_plan_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepRegionSwitchPlanConfigArgs]]]
    ]: ...
    @region_switch_plan_configs.setter
    def region_switch_plan_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepRegionSwitchPlanConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="route53HealthCheckConfigs")
    def route53_health_check_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepRoute53HealthCheckConfigArgs]]
        ]
    ]: ...
    @route53_health_check_configs.setter
    def route53_health_check_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepRoute53HealthCheckConfigArgs]]
            ]
        ],
    ): ...

class PlanWorkflowStepArcRoutingControlConfigArgsDict(TypedDict):
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    region_and_routing_controls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlArgsDict
                ]
            ]
        ]
    ]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PlanWorkflowStepArcRoutingControlConfigArgs:
    def __init__(
        __self__,
        *,
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region_and_routing_controls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlArgs
                    ]
                ]
            ]
        ] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionAndRoutingControls")
    def region_and_routing_controls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlArgs
                ]
            ]
        ]
    ]: ...
    @region_and_routing_controls.setter
    def region_and_routing_controls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlArgsDict(TypedDict):
    region: pulumi.Input[_builtins.str]
    routing_controls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlArgs:
    def __init__(
        __self__,
        *,
        region: pulumi.Input[_builtins.str],
        routing_controls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routingControls")
    def routing_controls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgs
                ]
            ]
        ]
    ]: ...
    @routing_controls.setter
    def routing_controls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgs
                    ]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgsDict(
    TypedDict
):
    routing_control_arn: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgs:
    def __init__(
        __self__,
        *,
        routing_control_arn: pulumi.Input[_builtins.str],
        state: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routingControlArn")
    def routing_control_arn(self) -> pulumi.Input[_builtins.str]: ...
    @routing_control_arn.setter
    def routing_control_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]: ...
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepCustomActionLambdaConfigArgsDict(TypedDict):
    region_to_run: pulumi.Input[_builtins.str]
    retry_interval_minutes: pulumi.Input[_builtins.float]
    lambdas: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigLambdaArgsDict]
            ]
        ]
    ]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungracefuls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigUngracefulArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepCustomActionLambdaConfigArgs:
    def __init__(
        __self__,
        *,
        region_to_run: pulumi.Input[_builtins.str],
        retry_interval_minutes: pulumi.Input[_builtins.float],
        lambdas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigLambdaArgs]
                ]
            ]
        ] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungracefuls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigUngracefulArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regionToRun")
    def region_to_run(self) -> pulumi.Input[_builtins.str]: ...
    @region_to_run.setter
    def region_to_run(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retryIntervalMinutes")
    def retry_interval_minutes(self) -> pulumi.Input[_builtins.float]: ...
    @retry_interval_minutes.setter
    def retry_interval_minutes(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def lambdas(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigLambdaArgs]]
        ]
    ]: ...
    @lambdas.setter
    def lambdas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigLambdaArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigUngracefulArgs]
            ]
        ]
    ]: ...
    @ungracefuls.setter
    def ungracefuls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepCustomActionLambdaConfigUngracefulArgs]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepCustomActionLambdaConfigLambdaArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepCustomActionLambdaConfigLambdaArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepCustomActionLambdaConfigUngracefulArgsDict(TypedDict):
    behavior: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepCustomActionLambdaConfigUngracefulArgs:
    def __init__(__self__, *, behavior: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Input[_builtins.str]: ...
    @behavior.setter
    def behavior(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepDocumentDbConfigArgsDict(TypedDict):
    behavior: pulumi.Input[_builtins.str]
    database_cluster_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    global_cluster_identifier: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungracefuls: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepDocumentDbConfigUngracefulArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepDocumentDbConfigArgs:
    def __init__(
        __self__,
        *,
        behavior: pulumi.Input[_builtins.str],
        database_cluster_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        global_cluster_identifier: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungracefuls: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepDocumentDbConfigUngracefulArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Input[_builtins.str]: ...
    @behavior.setter
    def behavior(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseClusterArns")
    def database_cluster_arns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @database_cluster_arns.setter
    def database_cluster_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @global_cluster_identifier.setter
    def global_cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepDocumentDbConfigUngracefulArgs]]
        ]
    ]: ...
    @ungracefuls.setter
    def ungracefuls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepDocumentDbConfigUngracefulArgs]]
            ]
        ],
    ): ...

class PlanWorkflowStepDocumentDbConfigUngracefulArgsDict(TypedDict):
    ungraceful: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepDocumentDbConfigUngracefulArgs:
    def __init__(__self__, *, ungraceful: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(self) -> pulumi.Input[_builtins.str]: ...
    @ungraceful.setter
    def ungraceful(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepEc2AsgCapacityIncreaseConfigArgsDict(TypedDict):
    capacity_monitoring_approach: pulumi.Input[_builtins.str]
    asgs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigAsgArgsDict]
            ]
        ]
    ]
    target_percent: NotRequired[pulumi.Input[_builtins.int]]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungraceful: NotRequired[
        pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigUngracefulArgsDict]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepEc2AsgCapacityIncreaseConfigArgs:
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: pulumi.Input[_builtins.str],
        asgs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigAsgArgs]
                ]
            ]
        ] = ...,
        target_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungraceful: Optional[
            pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigUngracefulArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_monitoring_approach.setter
    def capacity_monitoring_approach(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def asgs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigAsgArgs]]
        ]
    ]: ...
    @asgs.setter
    def asgs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigAsgArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_percent.setter
    def target_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(
        self,
    ) -> Optional[
        pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigUngracefulArgs]
    ]: ...
    @ungraceful.setter
    def ungraceful(
        self,
        value: Optional[
            pulumi.Input[PlanWorkflowStepEc2AsgCapacityIncreaseConfigUngracefulArgs]
        ],
    ): ...

class PlanWorkflowStepEc2AsgCapacityIncreaseConfigAsgArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepEc2AsgCapacityIncreaseConfigAsgArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepEc2AsgCapacityIncreaseConfigUngracefulArgsDict(TypedDict):
    minimum_success_percentage: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class PlanWorkflowStepEc2AsgCapacityIncreaseConfigUngracefulArgs:
    def __init__(
        __self__, *, minimum_success_percentage: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> pulumi.Input[_builtins.int]: ...
    @minimum_success_percentage.setter
    def minimum_success_percentage(self, value: pulumi.Input[_builtins.int]): ...

class PlanWorkflowStepEcsCapacityIncreaseConfigArgsDict(TypedDict):
    capacity_monitoring_approach: pulumi.Input[_builtins.str]
    services: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigServiceArgsDict]
            ]
        ]
    ]
    target_percent: NotRequired[pulumi.Input[_builtins.int]]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungraceful: NotRequired[
        pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigUngracefulArgsDict]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepEcsCapacityIncreaseConfigArgs:
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: pulumi.Input[_builtins.str],
        services: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigServiceArgs]
                ]
            ]
        ] = ...,
        target_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungraceful: Optional[
            pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigUngracefulArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_monitoring_approach.setter
    def capacity_monitoring_approach(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigServiceArgs]]
        ]
    ]: ...
    @services.setter
    def services(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigServiceArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_percent.setter
    def target_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(
        self,
    ) -> Optional[
        pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigUngracefulArgs]
    ]: ...
    @ungraceful.setter
    def ungraceful(
        self,
        value: Optional[
            pulumi.Input[PlanWorkflowStepEcsCapacityIncreaseConfigUngracefulArgs]
        ],
    ): ...

class PlanWorkflowStepEcsCapacityIncreaseConfigServiceArgsDict(TypedDict):
    cluster_arn: pulumi.Input[_builtins.str]
    service_arn: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepEcsCapacityIncreaseConfigServiceArgs:
    def __init__(
        __self__,
        *,
        cluster_arn: pulumi.Input[_builtins.str],
        service_arn: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_arn.setter
    def cluster_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> pulumi.Input[_builtins.str]: ...
    @service_arn.setter
    def service_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepEcsCapacityIncreaseConfigUngracefulArgsDict(TypedDict):
    minimum_success_percentage: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class PlanWorkflowStepEcsCapacityIncreaseConfigUngracefulArgs:
    def __init__(
        __self__, *, minimum_success_percentage: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> pulumi.Input[_builtins.int]: ...
    @minimum_success_percentage.setter
    def minimum_success_percentage(self, value: pulumi.Input[_builtins.int]): ...

class PlanWorkflowStepEksResourceScalingConfigArgsDict(TypedDict):
    capacity_monitoring_approach: pulumi.Input[_builtins.str]
    target_percent: pulumi.Input[_builtins.int]
    eks_clusters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepEksResourceScalingConfigEksClusterArgsDict]
            ]
        ]
    ]
    kubernetes_resource_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepEksResourceScalingConfigKubernetesResourceTypeArgsDict
                ]
            ]
        ]
    ]
    scaling_resources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepEksResourceScalingConfigScalingResourceArgsDict
                ]
            ]
        ]
    ]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungracefuls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepEksResourceScalingConfigUngracefulArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepEksResourceScalingConfigArgs:
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: pulumi.Input[_builtins.str],
        target_percent: pulumi.Input[_builtins.int],
        eks_clusters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepEksResourceScalingConfigEksClusterArgs]
                ]
            ]
        ] = ...,
        kubernetes_resource_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepEksResourceScalingConfigKubernetesResourceTypeArgs
                    ]
                ]
            ]
        ] = ...,
        scaling_resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepEksResourceScalingConfigScalingResourceArgs
                    ]
                ]
            ]
        ] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungracefuls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepEksResourceScalingConfigUngracefulArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_monitoring_approach.setter
    def capacity_monitoring_approach(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> pulumi.Input[_builtins.int]: ...
    @target_percent.setter
    def target_percent(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="eksClusters")
    def eks_clusters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepEksResourceScalingConfigEksClusterArgs]
            ]
        ]
    ]: ...
    @eks_clusters.setter
    def eks_clusters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepEksResourceScalingConfigEksClusterArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kubernetesResourceTypes")
    def kubernetes_resource_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepEksResourceScalingConfigKubernetesResourceTypeArgs
                ]
            ]
        ]
    ]: ...
    @kubernetes_resource_types.setter
    def kubernetes_resource_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepEksResourceScalingConfigKubernetesResourceTypeArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scalingResources")
    def scaling_resources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepEksResourceScalingConfigScalingResourceArgs
                ]
            ]
        ]
    ]: ...
    @scaling_resources.setter
    def scaling_resources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepEksResourceScalingConfigScalingResourceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepEksResourceScalingConfigUngracefulArgs]
            ]
        ]
    ]: ...
    @ungracefuls.setter
    def ungracefuls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepEksResourceScalingConfigUngracefulArgs]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepEksResourceScalingConfigEksClusterArgsDict(TypedDict):
    cluster_arn: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepEksResourceScalingConfigEksClusterArgs:
    def __init__(
        __self__,
        *,
        cluster_arn: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_arn.setter
    def cluster_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepEksResourceScalingConfigKubernetesResourceTypeArgsDict(TypedDict):
    api_version: pulumi.Input[_builtins.str]
    kind: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepEksResourceScalingConfigKubernetesResourceTypeArgs:
    def __init__(
        __self__,
        *,
        api_version: pulumi.Input[_builtins.str],
        kind: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Input[_builtins.str]: ...
    @api_version.setter
    def api_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepEksResourceScalingConfigScalingResourceArgsDict(TypedDict):
    namespace: pulumi.Input[_builtins.str]
    resources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepEksResourceScalingConfigScalingResourceResourceArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepEksResourceScalingConfigScalingResourceArgs:
    def __init__(
        __self__,
        *,
        namespace: pulumi.Input[_builtins.str],
        resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepEksResourceScalingConfigScalingResourceResourceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepEksResourceScalingConfigScalingResourceResourceArgs
                ]
            ]
        ]
    ]: ...
    @resources.setter
    def resources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepEksResourceScalingConfigScalingResourceResourceArgs
                    ]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepEksResourceScalingConfigScalingResourceResourceArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    resource_name: pulumi.Input[_builtins.str]
    hpa_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepEksResourceScalingConfigScalingResourceResourceArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        resource_name: pulumi.Input[_builtins.str],
        hpa_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hpaName")
    def hpa_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hpa_name.setter
    def hpa_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepEksResourceScalingConfigUngracefulArgsDict(TypedDict):
    minimum_success_percentage: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class PlanWorkflowStepEksResourceScalingConfigUngracefulArgs:
    def __init__(
        __self__, *, minimum_success_percentage: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> pulumi.Input[_builtins.int]: ...
    @minimum_success_percentage.setter
    def minimum_success_percentage(self, value: pulumi.Input[_builtins.int]): ...

class PlanWorkflowStepExecutionApprovalConfigArgsDict(TypedDict):
    approval_role: pulumi.Input[_builtins.str]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PlanWorkflowStepExecutionApprovalConfigArgs:
    def __init__(
        __self__,
        *,
        approval_role: pulumi.Input[_builtins.str],
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalRole")
    def approval_role(self) -> pulumi.Input[_builtins.str]: ...
    @approval_role.setter
    def approval_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PlanWorkflowStepGlobalAuroraConfigArgsDict(TypedDict):
    behavior: pulumi.Input[_builtins.str]
    database_cluster_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    global_cluster_identifier: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungracefuls: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepGlobalAuroraConfigUngracefulArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepGlobalAuroraConfigArgs:
    def __init__(
        __self__,
        *,
        behavior: pulumi.Input[_builtins.str],
        database_cluster_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        global_cluster_identifier: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungracefuls: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepGlobalAuroraConfigUngracefulArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Input[_builtins.str]: ...
    @behavior.setter
    def behavior(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseClusterArns")
    def database_cluster_arns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @database_cluster_arns.setter
    def database_cluster_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @global_cluster_identifier.setter
    def global_cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PlanWorkflowStepGlobalAuroraConfigUngracefulArgs]]
        ]
    ]: ...
    @ungracefuls.setter
    def ungracefuls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PlanWorkflowStepGlobalAuroraConfigUngracefulArgs]]
            ]
        ],
    ): ...

class PlanWorkflowStepGlobalAuroraConfigUngracefulArgsDict(TypedDict):
    ungraceful: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepGlobalAuroraConfigUngracefulArgs:
    def __init__(__self__, *, ungraceful: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(self) -> pulumi.Input[_builtins.str]: ...
    @ungraceful.setter
    def ungraceful(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepParallelConfigArgsDict(TypedDict):
    steps: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepParallelConfigStepArgsDict]]]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigArgs:
    def __init__(
        __self__,
        *,
        steps: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepParallelConfigStepArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def steps(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepParallelConfigStepArgs]]]
    ]: ...
    @steps.setter
    def steps(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowStepParallelConfigStepArgs]]]
        ],
    ): ...

class PlanWorkflowStepParallelConfigStepArgsDict(TypedDict):
    execution_block_type: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    arc_routing_control_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepArcRoutingControlConfigArgsDict
                ]
            ]
        ]
    ]
    custom_action_lambda_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigArgsDict
                ]
            ]
        ]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    document_db_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepParallelConfigStepDocumentDbConfigArgsDict]
            ]
        ]
    ]
    ec2_asg_capacity_increase_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigArgsDict
                ]
            ]
        ]
    ]
    ecs_capacity_increase_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigArgsDict
                ]
            ]
        ]
    ]
    eks_resource_scaling_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigArgsDict
                ]
            ]
        ]
    ]
    execution_approval_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepExecutionApprovalConfigArgsDict
                ]
            ]
        ]
    ]
    global_aurora_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepGlobalAuroraConfigArgsDict
                ]
            ]
        ]
    ]
    region_switch_plan_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepRegionSwitchPlanConfigArgsDict
                ]
            ]
        ]
    ]
    route53_health_check_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepArgs:
    def __init__(
        __self__,
        *,
        execution_block_type: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        arc_routing_control_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepArcRoutingControlConfigArgs
                    ]
                ]
            ]
        ] = ...,
        custom_action_lambda_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigArgs
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        document_db_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepParallelConfigStepDocumentDbConfigArgs]
                ]
            ]
        ] = ...,
        ec2_asg_capacity_increase_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigArgs
                    ]
                ]
            ]
        ] = ...,
        ecs_capacity_increase_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigArgs
                    ]
                ]
            ]
        ] = ...,
        eks_resource_scaling_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigArgs
                    ]
                ]
            ]
        ] = ...,
        execution_approval_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepExecutionApprovalConfigArgs
                    ]
                ]
            ]
        ] = ...,
        global_aurora_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepGlobalAuroraConfigArgs
                    ]
                ]
            ]
        ] = ...,
        region_switch_plan_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepRegionSwitchPlanConfigArgs
                    ]
                ]
            ]
        ] = ...,
        route53_health_check_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionBlockType")
    def execution_block_type(self) -> pulumi.Input[_builtins.str]: ...
    @execution_block_type.setter
    def execution_block_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="arcRoutingControlConfigs")
    def arc_routing_control_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepArcRoutingControlConfigArgs
                ]
            ]
        ]
    ]: ...
    @arc_routing_control_configs.setter
    def arc_routing_control_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepArcRoutingControlConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customActionLambdaConfigs")
    def custom_action_lambda_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigArgs
                ]
            ]
        ]
    ]: ...
    @custom_action_lambda_configs.setter
    def custom_action_lambda_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentDbConfigs")
    def document_db_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepParallelConfigStepDocumentDbConfigArgs]
            ]
        ]
    ]: ...
    @document_db_configs.setter
    def document_db_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepParallelConfigStepDocumentDbConfigArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ec2AsgCapacityIncreaseConfigs")
    def ec2_asg_capacity_increase_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigArgs
                ]
            ]
        ]
    ]: ...
    @ec2_asg_capacity_increase_configs.setter
    def ec2_asg_capacity_increase_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecsCapacityIncreaseConfigs")
    def ecs_capacity_increase_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigArgs
                ]
            ]
        ]
    ]: ...
    @ecs_capacity_increase_configs.setter
    def ecs_capacity_increase_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eksResourceScalingConfigs")
    def eks_resource_scaling_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigArgs
                ]
            ]
        ]
    ]: ...
    @eks_resource_scaling_configs.setter
    def eks_resource_scaling_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionApprovalConfigs")
    def execution_approval_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepExecutionApprovalConfigArgs
                ]
            ]
        ]
    ]: ...
    @execution_approval_configs.setter
    def execution_approval_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepExecutionApprovalConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalAuroraConfigs")
    def global_aurora_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepParallelConfigStepGlobalAuroraConfigArgs]
            ]
        ]
    ]: ...
    @global_aurora_configs.setter
    def global_aurora_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepGlobalAuroraConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="regionSwitchPlanConfigs")
    def region_switch_plan_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepRegionSwitchPlanConfigArgs
                ]
            ]
        ]
    ]: ...
    @region_switch_plan_configs.setter
    def region_switch_plan_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepRegionSwitchPlanConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="route53HealthCheckConfigs")
    def route53_health_check_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigArgs
                ]
            ]
        ]
    ]: ...
    @route53_health_check_configs.setter
    def route53_health_check_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepParallelConfigStepArcRoutingControlConfigArgsDict(TypedDict):
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    region_and_routing_controls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlArgsDict
                ]
            ]
        ]
    ]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepArcRoutingControlConfigArgs:
    def __init__(
        __self__,
        *,
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region_and_routing_controls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlArgs
                    ]
                ]
            ]
        ] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionAndRoutingControls")
    def region_and_routing_controls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlArgs
                ]
            ]
        ]
    ]: ...
    @region_and_routing_controls.setter
    def region_and_routing_controls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlArgsDict(
    TypedDict
):
    region: pulumi.Input[_builtins.str]
    routing_controls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlArgs:
    def __init__(
        __self__,
        *,
        region: pulumi.Input[_builtins.str],
        routing_controls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routingControls")
    def routing_controls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgs
                ]
            ]
        ]
    ]: ...
    @routing_controls.setter
    def routing_controls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgs
                    ]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgsDict(
    TypedDict
):
    routing_control_arn: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepArcRoutingControlConfigRegionAndRoutingControlRoutingControlArgs:
    def __init__(
        __self__,
        *,
        routing_control_arn: pulumi.Input[_builtins.str],
        state: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routingControlArn")
    def routing_control_arn(self) -> pulumi.Input[_builtins.str]: ...
    @routing_control_arn.setter
    def routing_control_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]: ...
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigArgsDict(TypedDict):
    region_to_run: pulumi.Input[_builtins.str]
    retry_interval_minutes: pulumi.Input[_builtins.float]
    lambdas: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigLambdaArgsDict
                ]
            ]
        ]
    ]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungracefuls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigUngracefulArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigArgs:
    def __init__(
        __self__,
        *,
        region_to_run: pulumi.Input[_builtins.str],
        retry_interval_minutes: pulumi.Input[_builtins.float],
        lambdas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigLambdaArgs
                    ]
                ]
            ]
        ] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungracefuls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigUngracefulArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regionToRun")
    def region_to_run(self) -> pulumi.Input[_builtins.str]: ...
    @region_to_run.setter
    def region_to_run(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retryIntervalMinutes")
    def retry_interval_minutes(self) -> pulumi.Input[_builtins.float]: ...
    @retry_interval_minutes.setter
    def retry_interval_minutes(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def lambdas(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigLambdaArgs
                ]
            ]
        ]
    ]: ...
    @lambdas.setter
    def lambdas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigLambdaArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigUngracefulArgs
                ]
            ]
        ]
    ]: ...
    @ungracefuls.setter
    def ungracefuls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigUngracefulArgs
                    ]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigLambdaArgsDict(
    TypedDict
):
    arn: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigLambdaArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigUngracefulArgsDict(
    TypedDict
):
    behavior: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepCustomActionLambdaConfigUngracefulArgs:
    def __init__(__self__, *, behavior: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Input[_builtins.str]: ...
    @behavior.setter
    def behavior(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepParallelConfigStepDocumentDbConfigArgsDict(TypedDict):
    behavior: pulumi.Input[_builtins.str]
    database_cluster_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    global_cluster_identifier: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungracefuls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepDocumentDbConfigUngracefulArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepDocumentDbConfigArgs:
    def __init__(
        __self__,
        *,
        behavior: pulumi.Input[_builtins.str],
        database_cluster_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        global_cluster_identifier: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungracefuls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepDocumentDbConfigUngracefulArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Input[_builtins.str]: ...
    @behavior.setter
    def behavior(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseClusterArns")
    def database_cluster_arns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @database_cluster_arns.setter
    def database_cluster_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @global_cluster_identifier.setter
    def global_cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepDocumentDbConfigUngracefulArgs
                ]
            ]
        ]
    ]: ...
    @ungracefuls.setter
    def ungracefuls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepDocumentDbConfigUngracefulArgs
                    ]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepParallelConfigStepDocumentDbConfigUngracefulArgsDict(TypedDict):
    ungraceful: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepDocumentDbConfigUngracefulArgs:
    def __init__(__self__, *, ungraceful: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(self) -> pulumi.Input[_builtins.str]: ...
    @ungraceful.setter
    def ungraceful(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigArgsDict(TypedDict):
    capacity_monitoring_approach: pulumi.Input[_builtins.str]
    asgs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigAsgArgsDict
                ]
            ]
        ]
    ]
    target_percent: NotRequired[pulumi.Input[_builtins.int]]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungraceful: NotRequired[
        pulumi.Input[
            PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigUngracefulArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigArgs:
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: pulumi.Input[_builtins.str],
        asgs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigAsgArgs
                    ]
                ]
            ]
        ] = ...,
        target_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungraceful: Optional[
            pulumi.Input[
                PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigUngracefulArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_monitoring_approach.setter
    def capacity_monitoring_approach(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def asgs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigAsgArgs
                ]
            ]
        ]
    ]: ...
    @asgs.setter
    def asgs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigAsgArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_percent.setter
    def target_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(
        self,
    ) -> Optional[
        pulumi.Input[
            PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigUngracefulArgs
        ]
    ]: ...
    @ungraceful.setter
    def ungraceful(
        self,
        value: Optional[
            pulumi.Input[
                PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigUngracefulArgs
            ]
        ],
    ): ...

class PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigAsgArgsDict(
    TypedDict
):
    arn: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigAsgArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigUngracefulArgsDict(
    TypedDict
):
    minimum_success_percentage: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEc2AsgCapacityIncreaseConfigUngracefulArgs:
    def __init__(
        __self__, *, minimum_success_percentage: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> pulumi.Input[_builtins.int]: ...
    @minimum_success_percentage.setter
    def minimum_success_percentage(self, value: pulumi.Input[_builtins.int]): ...

class PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigArgsDict(TypedDict):
    capacity_monitoring_approach: pulumi.Input[_builtins.str]
    services: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigServiceArgsDict
                ]
            ]
        ]
    ]
    target_percent: NotRequired[pulumi.Input[_builtins.int]]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungraceful: NotRequired[
        pulumi.Input[
            PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigUngracefulArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigArgs:
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: pulumi.Input[_builtins.str],
        services: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigServiceArgs
                    ]
                ]
            ]
        ] = ...,
        target_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungraceful: Optional[
            pulumi.Input[
                PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigUngracefulArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_monitoring_approach.setter
    def capacity_monitoring_approach(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigServiceArgs
                ]
            ]
        ]
    ]: ...
    @services.setter
    def services(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigServiceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_percent.setter
    def target_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(
        self,
    ) -> Optional[
        pulumi.Input[
            PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigUngracefulArgs
        ]
    ]: ...
    @ungraceful.setter
    def ungraceful(
        self,
        value: Optional[
            pulumi.Input[
                PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigUngracefulArgs
            ]
        ],
    ): ...

class PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigServiceArgsDict(
    TypedDict
):
    cluster_arn: pulumi.Input[_builtins.str]
    service_arn: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigServiceArgs:
    def __init__(
        __self__,
        *,
        cluster_arn: pulumi.Input[_builtins.str],
        service_arn: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_arn.setter
    def cluster_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> pulumi.Input[_builtins.str]: ...
    @service_arn.setter
    def service_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigUngracefulArgsDict(
    TypedDict
):
    minimum_success_percentage: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEcsCapacityIncreaseConfigUngracefulArgs:
    def __init__(
        __self__, *, minimum_success_percentage: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> pulumi.Input[_builtins.int]: ...
    @minimum_success_percentage.setter
    def minimum_success_percentage(self, value: pulumi.Input[_builtins.int]): ...

class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigArgsDict(TypedDict):
    capacity_monitoring_approach: pulumi.Input[_builtins.str]
    target_percent: pulumi.Input[_builtins.int]
    eks_clusters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigEksClusterArgsDict
                ]
            ]
        ]
    ]
    kubernetes_resource_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigKubernetesResourceTypeArgsDict
                ]
            ]
        ]
    ]
    scaling_resources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceArgsDict
                ]
            ]
        ]
    ]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungracefuls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigUngracefulArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigArgs:
    def __init__(
        __self__,
        *,
        capacity_monitoring_approach: pulumi.Input[_builtins.str],
        target_percent: pulumi.Input[_builtins.int],
        eks_clusters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigEksClusterArgs
                    ]
                ]
            ]
        ] = ...,
        kubernetes_resource_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigKubernetesResourceTypeArgs
                    ]
                ]
            ]
        ] = ...,
        scaling_resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceArgs
                    ]
                ]
            ]
        ] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungracefuls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigUngracefulArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityMonitoringApproach")
    def capacity_monitoring_approach(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_monitoring_approach.setter
    def capacity_monitoring_approach(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetPercent")
    def target_percent(self) -> pulumi.Input[_builtins.int]: ...
    @target_percent.setter
    def target_percent(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="eksClusters")
    def eks_clusters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigEksClusterArgs
                ]
            ]
        ]
    ]: ...
    @eks_clusters.setter
    def eks_clusters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigEksClusterArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kubernetesResourceTypes")
    def kubernetes_resource_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigKubernetesResourceTypeArgs
                ]
            ]
        ]
    ]: ...
    @kubernetes_resource_types.setter
    def kubernetes_resource_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigKubernetesResourceTypeArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scalingResources")
    def scaling_resources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceArgs
                ]
            ]
        ]
    ]: ...
    @scaling_resources.setter
    def scaling_resources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigUngracefulArgs
                ]
            ]
        ]
    ]: ...
    @ungracefuls.setter
    def ungracefuls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigUngracefulArgs
                    ]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigEksClusterArgsDict(
    TypedDict
):
    cluster_arn: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigEksClusterArgs:
    def __init__(
        __self__,
        *,
        cluster_arn: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_arn.setter
    def cluster_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigKubernetesResourceTypeArgsDict(
    TypedDict
):
    api_version: pulumi.Input[_builtins.str]
    kind: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigKubernetesResourceTypeArgs:
    def __init__(
        __self__,
        *,
        api_version: pulumi.Input[_builtins.str],
        kind: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Input[_builtins.str]: ...
    @api_version.setter
    def api_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceArgsDict(
    TypedDict
):
    namespace: pulumi.Input[_builtins.str]
    resources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceResourceArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceArgs:
    def __init__(
        __self__,
        *,
        namespace: pulumi.Input[_builtins.str],
        resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceResourceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceResourceArgs
                ]
            ]
        ]
    ]: ...
    @resources.setter
    def resources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceResourceArgs
                    ]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceResourceArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    resource_name: pulumi.Input[_builtins.str]
    hpa_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigScalingResourceResourceArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        resource_name: pulumi.Input[_builtins.str],
        hpa_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hpaName")
    def hpa_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hpa_name.setter
    def hpa_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigUngracefulArgsDict(
    TypedDict
):
    minimum_success_percentage: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepEksResourceScalingConfigUngracefulArgs:
    def __init__(
        __self__, *, minimum_success_percentage: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumSuccessPercentage")
    def minimum_success_percentage(self) -> pulumi.Input[_builtins.int]: ...
    @minimum_success_percentage.setter
    def minimum_success_percentage(self, value: pulumi.Input[_builtins.int]): ...

class PlanWorkflowStepParallelConfigStepExecutionApprovalConfigArgsDict(TypedDict):
    approval_role: pulumi.Input[_builtins.str]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepExecutionApprovalConfigArgs:
    def __init__(
        __self__,
        *,
        approval_role: pulumi.Input[_builtins.str],
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalRole")
    def approval_role(self) -> pulumi.Input[_builtins.str]: ...
    @approval_role.setter
    def approval_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PlanWorkflowStepParallelConfigStepGlobalAuroraConfigArgsDict(TypedDict):
    behavior: pulumi.Input[_builtins.str]
    database_cluster_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    global_cluster_identifier: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ungracefuls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepGlobalAuroraConfigUngracefulArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepGlobalAuroraConfigArgs:
    def __init__(
        __self__,
        *,
        behavior: pulumi.Input[_builtins.str],
        database_cluster_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        global_cluster_identifier: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ungracefuls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepGlobalAuroraConfigUngracefulArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Input[_builtins.str]: ...
    @behavior.setter
    def behavior(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseClusterArns")
    def database_cluster_arns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @database_cluster_arns.setter
    def database_cluster_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @global_cluster_identifier.setter
    def global_cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ungracefuls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepGlobalAuroraConfigUngracefulArgs
                ]
            ]
        ]
    ]: ...
    @ungracefuls.setter
    def ungracefuls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepGlobalAuroraConfigUngracefulArgs
                    ]
                ]
            ]
        ],
    ): ...

class PlanWorkflowStepParallelConfigStepGlobalAuroraConfigUngracefulArgsDict(TypedDict):
    ungraceful: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepGlobalAuroraConfigUngracefulArgs:
    def __init__(__self__, *, ungraceful: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ungraceful(self) -> pulumi.Input[_builtins.str]: ...
    @ungraceful.setter
    def ungraceful(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepParallelConfigStepRegionSwitchPlanConfigArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepRegionSwitchPlanConfigArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigArgsDict(TypedDict):
    hosted_zone_id: pulumi.Input[_builtins.str]
    record_name: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    record_sets: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigRecordSetArgsDict
                ]
            ]
        ]
    ]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigArgs:
    def __init__(
        __self__,
        *,
        hosted_zone_id: pulumi.Input[_builtins.str],
        record_name: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        record_sets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigRecordSetArgs
                    ]
                ]
            ]
        ] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="recordName")
    def record_name(self) -> pulumi.Input[_builtins.str]: ...
    @record_name.setter
    def record_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recordSets")
    def record_sets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigRecordSetArgs
                ]
            ]
        ]
    ]: ...
    @record_sets.setter
    def record_sets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigRecordSetArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigRecordSetArgsDict(
    TypedDict
):
    record_set_identifier: pulumi.Input[_builtins.str]
    region: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepParallelConfigStepRoute53HealthCheckConfigRecordSetArgs:
    def __init__(
        __self__,
        *,
        record_set_identifier: pulumi.Input[_builtins.str],
        region: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordSetIdentifier")
    def record_set_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @record_set_identifier.setter
    def record_set_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...

class PlanWorkflowStepRegionSwitchPlanConfigArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanWorkflowStepRegionSwitchPlanConfigArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanWorkflowStepRoute53HealthCheckConfigArgsDict(TypedDict):
    hosted_zone_id: pulumi.Input[_builtins.str]
    record_name: pulumi.Input[_builtins.str]
    cross_account_role: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    record_sets: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepRoute53HealthCheckConfigRecordSetArgsDict]
            ]
        ]
    ]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PlanWorkflowStepRoute53HealthCheckConfigArgs:
    def __init__(
        __self__,
        *,
        hosted_zone_id: pulumi.Input[_builtins.str],
        record_name: pulumi.Input[_builtins.str],
        cross_account_role: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        record_sets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepRoute53HealthCheckConfigRecordSetArgs]
                ]
            ]
        ] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="recordName")
    def record_name(self) -> pulumi.Input[_builtins.str]: ...
    @record_name.setter
    def record_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossAccountRole")
    def cross_account_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_account_role.setter
    def cross_account_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recordSets")
    def record_sets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PlanWorkflowStepRoute53HealthCheckConfigRecordSetArgs]
            ]
        ]
    ]: ...
    @record_sets.setter
    def record_sets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PlanWorkflowStepRoute53HealthCheckConfigRecordSetArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PlanWorkflowStepRoute53HealthCheckConfigRecordSetArgsDict(TypedDict):
    record_set_identifier: pulumi.Input[_builtins.str]
    region: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanWorkflowStepRoute53HealthCheckConfigRecordSetArgs:
    def __init__(
        __self__,
        *,
        record_set_identifier: pulumi.Input[_builtins.str],
        region: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordSetIdentifier")
    def record_set_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @record_set_identifier.setter
    def record_set_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
