

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeploymentConfigMinimumHealthyHosts', 'DeploymentConfigTrafficRoutingConfig', ..., ..., 'DeploymentConfigZonalConfig', ..., 'DeploymentGroupAlarmConfiguration', 'DeploymentGroupAutoRollbackConfiguration', 'DeploymentGroupBlueGreenDeploymentConfig', ..., ..., ..., 'DeploymentGroupDeploymentStyle', 'DeploymentGroupEc2TagFilter', 'DeploymentGroupEc2TagSet', 'DeploymentGroupEc2TagSetEc2TagFilter', 'DeploymentGroupEcsService', 'DeploymentGroupLoadBalancerInfo', 'DeploymentGroupLoadBalancerInfoElbInfo', 'DeploymentGroupLoadBalancerInfoTargetGroupInfo', 'DeploymentGroupLoadBalancerInfoTargetGroupPairInfo', ..., ..., ..., 'DeploymentGroupOnPremisesInstanceTagFilter', 'DeploymentGroupTriggerConfiguration']
@pulumi.output_type
class DeploymentConfigMinimumHealthyHosts(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ..., value: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DeploymentConfigTrafficRoutingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, time_based_canary: Optional[outputs.DeploymentConfigTrafficRoutingConfigTimeBasedCanary] = ..., time_based_linear: Optional[outputs.DeploymentConfigTrafficRoutingConfigTimeBasedLinear] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeBasedCanary")
    def time_based_canary(self) -> Optional[outputs.DeploymentConfigTrafficRoutingConfigTimeBasedCanary]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeBasedLinear")
    def time_based_linear(self) -> Optional[outputs.DeploymentConfigTrafficRoutingConfigTimeBasedLinear]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentConfigTrafficRoutingConfigTimeBasedCanary(dict):
    def __init__(__self__, *, interval: Optional[_builtins.int] = ..., percentage: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DeploymentConfigTrafficRoutingConfigTimeBasedLinear(dict):
    def __init__(__self__, *, interval: Optional[_builtins.int] = ..., percentage: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DeploymentConfigZonalConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, first_zone_monitor_duration_in_seconds: Optional[_builtins.int] = ..., minimum_healthy_hosts_per_zone: Optional[outputs.DeploymentConfigZonalConfigMinimumHealthyHostsPerZone] = ..., monitor_duration_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstZoneMonitorDurationInSeconds")
    def first_zone_monitor_duration_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumHealthyHostsPerZone")
    def minimum_healthy_hosts_per_zone(self) -> Optional[outputs.DeploymentConfigZonalConfigMinimumHealthyHostsPerZone]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorDurationInSeconds")
    def monitor_duration_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DeploymentConfigZonalConfigMinimumHealthyHostsPerZone(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ..., value: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupAlarmConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alarms: Optional[Sequence[_builtins.str]] = ..., enabled: Optional[_builtins.bool] = ..., ignore_poll_alarm_failure: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alarms(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignorePollAlarmFailure")
    def ignore_poll_alarm_failure(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupAutoRollbackConfiguration(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., events: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupBlueGreenDeploymentConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_ready_option: Optional[outputs.DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption] = ..., green_fleet_provisioning_option: Optional[outputs.DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption] = ..., terminate_blue_instances_on_deployment_success: Optional[outputs.DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentReadyOption")
    def deployment_ready_option(self) -> Optional[outputs.DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="greenFleetProvisioningOption")
    def green_fleet_provisioning_option(self) -> Optional[outputs.DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateBlueInstancesOnDeploymentSuccess")
    def terminate_blue_instances_on_deployment_success(self) -> Optional[outputs.DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_on_timeout: Optional[_builtins.str] = ..., wait_time_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionOnTimeout")
    def action_on_timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitTimeInMinutes")
    def wait_time_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption(dict):
    def __init__(__self__, *, action: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: Optional[_builtins.str] = ..., termination_wait_time_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationWaitTimeInMinutes")
    def termination_wait_time_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupDeploymentStyle(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_option: Optional[_builtins.str] = ..., deployment_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentOption")
    def deployment_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupEc2TagFilter(dict):
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupEc2TagSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ec2_tag_filters: Optional[Sequence[outputs.DeploymentGroupEc2TagSetEc2TagFilter]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2TagFilters")
    def ec2_tag_filters(self) -> Optional[Sequence[outputs.DeploymentGroupEc2TagSetEc2TagFilter]]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupEc2TagSetEc2TagFilter(dict):
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupEcsService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_name: _builtins.str, service_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DeploymentGroupLoadBalancerInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, elb_infos: Optional[Sequence[outputs.DeploymentGroupLoadBalancerInfoElbInfo]] = ..., target_group_infos: Optional[Sequence[outputs.DeploymentGroupLoadBalancerInfoTargetGroupInfo]] = ..., target_group_pair_info: Optional[outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfo] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elbInfos")
    def elb_infos(self) -> Optional[Sequence[outputs.DeploymentGroupLoadBalancerInfoElbInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupInfos")
    def target_group_infos(self) -> Optional[Sequence[outputs.DeploymentGroupLoadBalancerInfoTargetGroupInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupPairInfo")
    def target_group_pair_info(self) -> Optional[outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfo]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoElbInfo(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoTargetGroupInfo(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, prod_traffic_route: outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute, target_groups: Sequence[outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup], test_traffic_route: Optional[outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prodTrafficRoute")
    def prod_traffic_route(self) -> outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(self) -> Sequence[outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testTrafficRoute")
    def test_traffic_route(self) -> Optional[outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, listener_arns: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerArns")
    def listener_arns(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, listener_arns: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerArns")
    def listener_arns(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupOnPremisesInstanceTagFilter(dict):
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentGroupTriggerConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, trigger_events: Sequence[_builtins.str], trigger_name: _builtins.str, trigger_target_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerEvents")
    def trigger_events(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerName")
    def trigger_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerTargetArn")
    def trigger_target_arn(self) -> _builtins.str:
        
        ...
    


