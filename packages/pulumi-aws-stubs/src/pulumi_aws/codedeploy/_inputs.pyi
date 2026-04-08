import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DeploymentConfigMinimumHealthyHostsArgs",
    "DeploymentConfigMinimumHealthyHostsArgsDict",
    "DeploymentConfigTrafficRoutingConfigArgs",
    "DeploymentConfigTrafficRoutingConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "DeploymentConfigZonalConfigArgs",
    "DeploymentConfigZonalConfigArgsDict",
    ...,
    ...,
    "DeploymentGroupAlarmConfigurationArgs",
    "DeploymentGroupAlarmConfigurationArgsDict",
    "DeploymentGroupAutoRollbackConfigurationArgs",
    "DeploymentGroupAutoRollbackConfigurationArgsDict",
    "DeploymentGroupBlueGreenDeploymentConfigArgs",
    "DeploymentGroupBlueGreenDeploymentConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DeploymentGroupDeploymentStyleArgs",
    "DeploymentGroupDeploymentStyleArgsDict",
    "DeploymentGroupEc2TagFilterArgs",
    "DeploymentGroupEc2TagFilterArgsDict",
    "DeploymentGroupEc2TagSetArgs",
    "DeploymentGroupEc2TagSetArgsDict",
    "DeploymentGroupEc2TagSetEc2TagFilterArgs",
    "DeploymentGroupEc2TagSetEc2TagFilterArgsDict",
    "DeploymentGroupEcsServiceArgs",
    "DeploymentGroupEcsServiceArgsDict",
    "DeploymentGroupLoadBalancerInfoArgs",
    "DeploymentGroupLoadBalancerInfoArgsDict",
    "DeploymentGroupLoadBalancerInfoElbInfoArgs",
    "DeploymentGroupLoadBalancerInfoElbInfoArgsDict",
    "DeploymentGroupLoadBalancerInfoTargetGroupInfoArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DeploymentGroupOnPremisesInstanceTagFilterArgs",
    "DeploymentGroupOnPremisesInstanceTagFilterArgsDict",
    "DeploymentGroupTriggerConfigurationArgs",
    "DeploymentGroupTriggerConfigurationArgsDict",
]

class DeploymentConfigMinimumHealthyHostsArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeploymentConfigMinimumHealthyHostsArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DeploymentConfigTrafficRoutingConfigArgsDict(TypedDict):
    time_based_canary: NotRequired[
        pulumi.Input[DeploymentConfigTrafficRoutingConfigTimeBasedCanaryArgsDict]
    ]
    time_based_linear: NotRequired[
        pulumi.Input[DeploymentConfigTrafficRoutingConfigTimeBasedLinearArgsDict]
    ]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeploymentConfigTrafficRoutingConfigArgs:
    def __init__(
        __self__,
        *,
        time_based_canary: Optional[
            pulumi.Input[DeploymentConfigTrafficRoutingConfigTimeBasedCanaryArgs]
        ] = ...,
        time_based_linear: Optional[
            pulumi.Input[DeploymentConfigTrafficRoutingConfigTimeBasedLinearArgs]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeBasedCanary")
    def time_based_canary(
        self,
    ) -> Optional[
        pulumi.Input[DeploymentConfigTrafficRoutingConfigTimeBasedCanaryArgs]
    ]: ...
    @time_based_canary.setter
    def time_based_canary(
        self,
        value: Optional[
            pulumi.Input[DeploymentConfigTrafficRoutingConfigTimeBasedCanaryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeBasedLinear")
    def time_based_linear(
        self,
    ) -> Optional[
        pulumi.Input[DeploymentConfigTrafficRoutingConfigTimeBasedLinearArgs]
    ]: ...
    @time_based_linear.setter
    def time_based_linear(
        self,
        value: Optional[
            pulumi.Input[DeploymentConfigTrafficRoutingConfigTimeBasedLinearArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentConfigTrafficRoutingConfigTimeBasedCanaryArgsDict(TypedDict):
    interval: NotRequired[pulumi.Input[_builtins.int]]
    percentage: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeploymentConfigTrafficRoutingConfigTimeBasedCanaryArgs:
    def __init__(
        __self__,
        *,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DeploymentConfigTrafficRoutingConfigTimeBasedLinearArgsDict(TypedDict):
    interval: NotRequired[pulumi.Input[_builtins.int]]
    percentage: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeploymentConfigTrafficRoutingConfigTimeBasedLinearArgs:
    def __init__(
        __self__,
        *,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DeploymentConfigZonalConfigArgsDict(TypedDict):
    first_zone_monitor_duration_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    minimum_healthy_hosts_per_zone: NotRequired[
        pulumi.Input[DeploymentConfigZonalConfigMinimumHealthyHostsPerZoneArgsDict]
    ]
    monitor_duration_in_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeploymentConfigZonalConfigArgs:
    def __init__(
        __self__,
        *,
        first_zone_monitor_duration_in_seconds: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        minimum_healthy_hosts_per_zone: Optional[
            pulumi.Input[DeploymentConfigZonalConfigMinimumHealthyHostsPerZoneArgs]
        ] = ...,
        monitor_duration_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="firstZoneMonitorDurationInSeconds")
    def first_zone_monitor_duration_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @first_zone_monitor_duration_in_seconds.setter
    def first_zone_monitor_duration_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minimumHealthyHostsPerZone")
    def minimum_healthy_hosts_per_zone(
        self,
    ) -> Optional[
        pulumi.Input[DeploymentConfigZonalConfigMinimumHealthyHostsPerZoneArgs]
    ]: ...
    @minimum_healthy_hosts_per_zone.setter
    def minimum_healthy_hosts_per_zone(
        self,
        value: Optional[
            pulumi.Input[DeploymentConfigZonalConfigMinimumHealthyHostsPerZoneArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitorDurationInSeconds")
    def monitor_duration_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @monitor_duration_in_seconds.setter
    def monitor_duration_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class DeploymentConfigZonalConfigMinimumHealthyHostsPerZoneArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeploymentConfigZonalConfigMinimumHealthyHostsPerZoneArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DeploymentGroupAlarmConfigurationArgsDict(TypedDict):
    alarms: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ignore_poll_alarm_failure: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DeploymentGroupAlarmConfigurationArgs:
    def __init__(
        __self__,
        *,
        alarms: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_poll_alarm_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alarms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @alarms.setter
    def alarms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ignorePollAlarmFailure")
    def ignore_poll_alarm_failure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_poll_alarm_failure.setter
    def ignore_poll_alarm_failure(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DeploymentGroupAutoRollbackConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeploymentGroupAutoRollbackConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @events.setter
    def events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DeploymentGroupBlueGreenDeploymentConfigArgsDict(TypedDict):
    deployment_ready_option: NotRequired[
        pulumi.Input[
            DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionArgsDict
        ]
    ]
    green_fleet_provisioning_option: NotRequired[
        pulumi.Input[
            DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionArgsDict
        ]
    ]
    terminate_blue_instances_on_deployment_success: NotRequired[
        pulumi.Input[
            DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessArgsDict
        ]
    ]

@pulumi.input_type
class DeploymentGroupBlueGreenDeploymentConfigArgs:
    def __init__(
        __self__,
        *,
        deployment_ready_option: Optional[
            pulumi.Input[
                DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionArgs
            ]
        ] = ...,
        green_fleet_provisioning_option: Optional[
            pulumi.Input[
                DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionArgs
            ]
        ] = ...,
        terminate_blue_instances_on_deployment_success: Optional[
            pulumi.Input[
                DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deploymentReadyOption")
    def deployment_ready_option(
        self,
    ) -> Optional[
        pulumi.Input[DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionArgs]
    ]: ...
    @deployment_ready_option.setter
    def deployment_ready_option(
        self,
        value: Optional[
            pulumi.Input[
                DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="greenFleetProvisioningOption")
    def green_fleet_provisioning_option(
        self,
    ) -> Optional[
        pulumi.Input[
            DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionArgs
        ]
    ]: ...
    @green_fleet_provisioning_option.setter
    def green_fleet_provisioning_option(
        self,
        value: Optional[
            pulumi.Input[
                DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="terminateBlueInstancesOnDeploymentSuccess")
    def terminate_blue_instances_on_deployment_success(
        self,
    ) -> Optional[
        pulumi.Input[
            DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessArgs
        ]
    ]: ...
    @terminate_blue_instances_on_deployment_success.setter
    def terminate_blue_instances_on_deployment_success(
        self,
        value: Optional[
            pulumi.Input[
                DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessArgs
            ]
        ],
    ): ...

class DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionArgsDict(TypedDict):
    action_on_timeout: NotRequired[pulumi.Input[_builtins.str]]
    wait_time_in_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionArgs:
    def __init__(
        __self__,
        *,
        action_on_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        wait_time_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionOnTimeout")
    def action_on_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_on_timeout.setter
    def action_on_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="waitTimeInMinutes")
    def wait_time_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @wait_time_in_minutes.setter
    def wait_time_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionArgsDict(
    TypedDict
):
    action: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionArgs:
    def __init__(
        __self__, *, action: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessArgsDict(
    TypedDict
):
    action: NotRequired[pulumi.Input[_builtins.str]]
    termination_wait_time_in_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        termination_wait_time_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="terminationWaitTimeInMinutes")
    def termination_wait_time_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @termination_wait_time_in_minutes.setter
    def termination_wait_time_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class DeploymentGroupDeploymentStyleArgsDict(TypedDict):
    deployment_option: NotRequired[pulumi.Input[_builtins.str]]
    deployment_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeploymentGroupDeploymentStyleArgs:
    def __init__(
        __self__,
        *,
        deployment_option: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deploymentOption")
    def deployment_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_option.setter
    def deployment_option(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentGroupEc2TagFilterArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeploymentGroupEc2TagFilterArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentGroupEc2TagSetArgsDict(TypedDict):
    ec2_tag_filters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DeploymentGroupEc2TagSetEc2TagFilterArgsDict]]
        ]
    ]

@pulumi.input_type
class DeploymentGroupEc2TagSetArgs:
    def __init__(
        __self__,
        *,
        ec2_tag_filters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DeploymentGroupEc2TagSetEc2TagFilterArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ec2TagFilters")
    def ec2_tag_filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagSetEc2TagFilterArgs]]]
    ]: ...
    @ec2_tag_filters.setter
    def ec2_tag_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DeploymentGroupEc2TagSetEc2TagFilterArgs]]
            ]
        ],
    ): ...

class DeploymentGroupEc2TagSetEc2TagFilterArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeploymentGroupEc2TagSetEc2TagFilterArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentGroupEcsServiceArgsDict(TypedDict):
    cluster_name: pulumi.Input[_builtins.str]
    service_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class DeploymentGroupEcsServiceArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...

class DeploymentGroupLoadBalancerInfoArgsDict(TypedDict):
    elb_infos: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DeploymentGroupLoadBalancerInfoElbInfoArgsDict]]
        ]
    ]
    target_group_infos: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[DeploymentGroupLoadBalancerInfoTargetGroupInfoArgsDict]
            ]
        ]
    ]
    target_group_pair_info: NotRequired[
        pulumi.Input[DeploymentGroupLoadBalancerInfoTargetGroupPairInfoArgsDict]
    ]

@pulumi.input_type
class DeploymentGroupLoadBalancerInfoArgs:
    def __init__(
        __self__,
        *,
        elb_infos: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DeploymentGroupLoadBalancerInfoElbInfoArgs]]
            ]
        ] = ...,
        target_group_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[DeploymentGroupLoadBalancerInfoTargetGroupInfoArgs]
                ]
            ]
        ] = ...,
        target_group_pair_info: Optional[
            pulumi.Input[DeploymentGroupLoadBalancerInfoTargetGroupPairInfoArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="elbInfos")
    def elb_infos(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DeploymentGroupLoadBalancerInfoElbInfoArgs]]]
    ]: ...
    @elb_infos.setter
    def elb_infos(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DeploymentGroupLoadBalancerInfoElbInfoArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetGroupInfos")
    def target_group_infos(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[DeploymentGroupLoadBalancerInfoTargetGroupInfoArgs]]
        ]
    ]: ...
    @target_group_infos.setter
    def target_group_infos(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[DeploymentGroupLoadBalancerInfoTargetGroupInfoArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetGroupPairInfo")
    def target_group_pair_info(
        self,
    ) -> Optional[
        pulumi.Input[DeploymentGroupLoadBalancerInfoTargetGroupPairInfoArgs]
    ]: ...
    @target_group_pair_info.setter
    def target_group_pair_info(
        self,
        value: Optional[
            pulumi.Input[DeploymentGroupLoadBalancerInfoTargetGroupPairInfoArgs]
        ],
    ): ...

class DeploymentGroupLoadBalancerInfoElbInfoArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeploymentGroupLoadBalancerInfoElbInfoArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentGroupLoadBalancerInfoTargetGroupInfoArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeploymentGroupLoadBalancerInfoTargetGroupInfoArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoArgsDict(TypedDict):
    prod_traffic_route: pulumi.Input[
        DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteArgsDict
    ]
    target_groups: pulumi.Input[
        Sequence[
            pulumi.Input[
                DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupArgsDict
            ]
        ]
    ]
    test_traffic_route: NotRequired[
        pulumi.Input[
            DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteArgsDict
        ]
    ]

@pulumi.input_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoArgs:
    def __init__(
        __self__,
        *,
        prod_traffic_route: pulumi.Input[
            DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteArgs
        ],
        target_groups: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupArgs
                ]
            ]
        ],
        test_traffic_route: Optional[
            pulumi.Input[
                DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="prodTrafficRoute")
    def prod_traffic_route(
        self,
    ) -> pulumi.Input[
        DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteArgs
    ]: ...
    @prod_traffic_route.setter
    def prod_traffic_route(
        self,
        value: pulumi.Input[
            DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupArgs
            ]
        ]
    ]: ...
    @target_groups.setter
    def target_groups(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="testTrafficRoute")
    def test_traffic_route(
        self,
    ) -> Optional[
        pulumi.Input[
            DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteArgs
        ]
    ]: ...
    @test_traffic_route.setter
    def test_traffic_route(
        self,
        value: Optional[
            pulumi.Input[
                DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteArgs
            ]
        ],
    ): ...

class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteArgsDict(
    TypedDict
):
    listener_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteArgs:
    def __init__(
        __self__, *, listener_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="listenerArns")
    def listener_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @listener_arns.setter
    def listener_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteArgsDict(
    TypedDict
):
    listener_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteArgs:
    def __init__(
        __self__, *, listener_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="listenerArns")
    def listener_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @listener_arns.setter
    def listener_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class DeploymentGroupOnPremisesInstanceTagFilterArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeploymentGroupOnPremisesInstanceTagFilterArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentGroupTriggerConfigurationArgsDict(TypedDict):
    trigger_events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    trigger_name: pulumi.Input[_builtins.str]
    trigger_target_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class DeploymentGroupTriggerConfigurationArgs:
    def __init__(
        __self__,
        *,
        trigger_events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        trigger_name: pulumi.Input[_builtins.str],
        trigger_target_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="triggerEvents")
    def trigger_events(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @trigger_events.setter
    def trigger_events(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="triggerName")
    def trigger_name(self) -> pulumi.Input[_builtins.str]: ...
    @trigger_name.setter
    def trigger_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="triggerTargetArn")
    def trigger_target_arn(self) -> pulumi.Input[_builtins.str]: ...
    @trigger_target_arn.setter
    def trigger_target_arn(self, value: pulumi.Input[_builtins.str]): ...
