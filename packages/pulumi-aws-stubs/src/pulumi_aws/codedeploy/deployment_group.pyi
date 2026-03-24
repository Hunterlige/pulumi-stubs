

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeploymentGroupArgs', 'DeploymentGroup']
@pulumi.input_type
class DeploymentGroupArgs:
    def __init__(__self__, *, app_name: pulumi.Input[_builtins.str], deployment_group_name: pulumi.Input[_builtins.str], service_role_arn: pulumi.Input[_builtins.str], alarm_configuration: Optional[pulumi.Input[DeploymentGroupAlarmConfigurationArgs]] = ..., auto_rollback_configuration: Optional[pulumi.Input[DeploymentGroupAutoRollbackConfigurationArgs]] = ..., autoscaling_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., blue_green_deployment_config: Optional[pulumi.Input[DeploymentGroupBlueGreenDeploymentConfigArgs]] = ..., deployment_config_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_style: Optional[pulumi.Input[DeploymentGroupDeploymentStyleArgs]] = ..., ec2_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagFilterArgs]]]] = ..., ec2_tag_sets: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagSetArgs]]]] = ..., ecs_service: Optional[pulumi.Input[DeploymentGroupEcsServiceArgs]] = ..., load_balancer_info: Optional[pulumi.Input[DeploymentGroupLoadBalancerInfoArgs]] = ..., on_premises_instance_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupOnPremisesInstanceTagFilterArgs]]]] = ..., outdated_instances_strategy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., termination_hook_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., trigger_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupTriggerConfigurationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_name.setter
    def app_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentGroupName")
    def deployment_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @deployment_group_name.setter
    def deployment_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_role_arn.setter
    def service_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmConfiguration")
    def alarm_configuration(self) -> Optional[pulumi.Input[DeploymentGroupAlarmConfigurationArgs]]:
        
        ...
    
    @alarm_configuration.setter
    def alarm_configuration(self, value: Optional[pulumi.Input[DeploymentGroupAlarmConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRollbackConfiguration")
    def auto_rollback_configuration(self) -> Optional[pulumi.Input[DeploymentGroupAutoRollbackConfigurationArgs]]:
        
        ...
    
    @auto_rollback_configuration.setter
    def auto_rollback_configuration(self, value: Optional[pulumi.Input[DeploymentGroupAutoRollbackConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroups")
    def autoscaling_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @autoscaling_groups.setter
    def autoscaling_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blueGreenDeploymentConfig")
    def blue_green_deployment_config(self) -> Optional[pulumi.Input[DeploymentGroupBlueGreenDeploymentConfigArgs]]:
        
        ...
    
    @blue_green_deployment_config.setter
    def blue_green_deployment_config(self, value: Optional[pulumi.Input[DeploymentGroupBlueGreenDeploymentConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfigName")
    def deployment_config_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_config_name.setter
    def deployment_config_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStyle")
    def deployment_style(self) -> Optional[pulumi.Input[DeploymentGroupDeploymentStyleArgs]]:
        
        ...
    
    @deployment_style.setter
    def deployment_style(self, value: Optional[pulumi.Input[DeploymentGroupDeploymentStyleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2TagFilters")
    def ec2_tag_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagFilterArgs]]]]:
        
        ...
    
    @ec2_tag_filters.setter
    def ec2_tag_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagFilterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2TagSets")
    def ec2_tag_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagSetArgs]]]]:
        
        ...
    
    @ec2_tag_sets.setter
    def ec2_tag_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagSetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ecsService")
    def ecs_service(self) -> Optional[pulumi.Input[DeploymentGroupEcsServiceArgs]]:
        
        ...
    
    @ecs_service.setter
    def ecs_service(self, value: Optional[pulumi.Input[DeploymentGroupEcsServiceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerInfo")
    def load_balancer_info(self) -> Optional[pulumi.Input[DeploymentGroupLoadBalancerInfoArgs]]:
        
        ...
    
    @load_balancer_info.setter
    def load_balancer_info(self, value: Optional[pulumi.Input[DeploymentGroupLoadBalancerInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremisesInstanceTagFilters")
    def on_premises_instance_tag_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupOnPremisesInstanceTagFilterArgs]]]]:
        
        ...
    
    @on_premises_instance_tag_filters.setter
    def on_premises_instance_tag_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupOnPremisesInstanceTagFilterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outdatedInstancesStrategy")
    def outdated_instances_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outdated_instances_strategy.setter
    def outdated_instances_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationHookEnabled")
    def termination_hook_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @termination_hook_enabled.setter
    def termination_hook_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerConfigurations")
    def trigger_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupTriggerConfigurationArgs]]]]:
        
        ...
    
    @trigger_configurations.setter
    def trigger_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupTriggerConfigurationArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _DeploymentGroupState:
    def __init__(__self__, *, alarm_configuration: Optional[pulumi.Input[DeploymentGroupAlarmConfigurationArgs]] = ..., app_name: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_rollback_configuration: Optional[pulumi.Input[DeploymentGroupAutoRollbackConfigurationArgs]] = ..., autoscaling_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., blue_green_deployment_config: Optional[pulumi.Input[DeploymentGroupBlueGreenDeploymentConfigArgs]] = ..., compute_platform: Optional[pulumi.Input[_builtins.str]] = ..., deployment_config_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_group_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment_group_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_style: Optional[pulumi.Input[DeploymentGroupDeploymentStyleArgs]] = ..., ec2_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagFilterArgs]]]] = ..., ec2_tag_sets: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagSetArgs]]]] = ..., ecs_service: Optional[pulumi.Input[DeploymentGroupEcsServiceArgs]] = ..., load_balancer_info: Optional[pulumi.Input[DeploymentGroupLoadBalancerInfoArgs]] = ..., on_premises_instance_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupOnPremisesInstanceTagFilterArgs]]]] = ..., outdated_instances_strategy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., termination_hook_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., trigger_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupTriggerConfigurationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmConfiguration")
    def alarm_configuration(self) -> Optional[pulumi.Input[DeploymentGroupAlarmConfigurationArgs]]:
        
        ...
    
    @alarm_configuration.setter
    def alarm_configuration(self, value: Optional[pulumi.Input[DeploymentGroupAlarmConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_name.setter
    def app_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRollbackConfiguration")
    def auto_rollback_configuration(self) -> Optional[pulumi.Input[DeploymentGroupAutoRollbackConfigurationArgs]]:
        
        ...
    
    @auto_rollback_configuration.setter
    def auto_rollback_configuration(self, value: Optional[pulumi.Input[DeploymentGroupAutoRollbackConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroups")
    def autoscaling_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @autoscaling_groups.setter
    def autoscaling_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blueGreenDeploymentConfig")
    def blue_green_deployment_config(self) -> Optional[pulumi.Input[DeploymentGroupBlueGreenDeploymentConfigArgs]]:
        
        ...
    
    @blue_green_deployment_config.setter
    def blue_green_deployment_config(self, value: Optional[pulumi.Input[DeploymentGroupBlueGreenDeploymentConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computePlatform")
    def compute_platform(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compute_platform.setter
    def compute_platform(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfigName")
    def deployment_config_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_config_name.setter
    def deployment_config_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentGroupId")
    def deployment_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_group_id.setter
    def deployment_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentGroupName")
    def deployment_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_group_name.setter
    def deployment_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStyle")
    def deployment_style(self) -> Optional[pulumi.Input[DeploymentGroupDeploymentStyleArgs]]:
        
        ...
    
    @deployment_style.setter
    def deployment_style(self, value: Optional[pulumi.Input[DeploymentGroupDeploymentStyleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2TagFilters")
    def ec2_tag_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagFilterArgs]]]]:
        
        ...
    
    @ec2_tag_filters.setter
    def ec2_tag_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagFilterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2TagSets")
    def ec2_tag_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagSetArgs]]]]:
        
        ...
    
    @ec2_tag_sets.setter
    def ec2_tag_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupEc2TagSetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ecsService")
    def ecs_service(self) -> Optional[pulumi.Input[DeploymentGroupEcsServiceArgs]]:
        
        ...
    
    @ecs_service.setter
    def ecs_service(self, value: Optional[pulumi.Input[DeploymentGroupEcsServiceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerInfo")
    def load_balancer_info(self) -> Optional[pulumi.Input[DeploymentGroupLoadBalancerInfoArgs]]:
        
        ...
    
    @load_balancer_info.setter
    def load_balancer_info(self, value: Optional[pulumi.Input[DeploymentGroupLoadBalancerInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremisesInstanceTagFilters")
    def on_premises_instance_tag_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupOnPremisesInstanceTagFilterArgs]]]]:
        
        ...
    
    @on_premises_instance_tag_filters.setter
    def on_premises_instance_tag_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupOnPremisesInstanceTagFilterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outdatedInstancesStrategy")
    def outdated_instances_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outdated_instances_strategy.setter
    def outdated_instances_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_role_arn.setter
    def service_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationHookEnabled")
    def termination_hook_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @termination_hook_enabled.setter
    def termination_hook_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerConfigurations")
    def trigger_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupTriggerConfigurationArgs]]]]:
        
        ...
    
    @trigger_configurations.setter
    def trigger_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentGroupTriggerConfigurationArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:codedeploy/deploymentGroup:DeploymentGroup")
class DeploymentGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., alarm_configuration: Optional[pulumi.Input[Union[DeploymentGroupAlarmConfigurationArgs, DeploymentGroupAlarmConfigurationArgsDict]]] = ..., app_name: Optional[pulumi.Input[_builtins.str]] = ..., auto_rollback_configuration: Optional[pulumi.Input[Union[DeploymentGroupAutoRollbackConfigurationArgs, DeploymentGroupAutoRollbackConfigurationArgsDict]]] = ..., autoscaling_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., blue_green_deployment_config: Optional[pulumi.Input[Union[DeploymentGroupBlueGreenDeploymentConfigArgs, DeploymentGroupBlueGreenDeploymentConfigArgsDict]]] = ..., deployment_config_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_group_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_style: Optional[pulumi.Input[Union[DeploymentGroupDeploymentStyleArgs, DeploymentGroupDeploymentStyleArgsDict]]] = ..., ec2_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentGroupEc2TagFilterArgs, DeploymentGroupEc2TagFilterArgsDict]]]]] = ..., ec2_tag_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentGroupEc2TagSetArgs, DeploymentGroupEc2TagSetArgsDict]]]]] = ..., ecs_service: Optional[pulumi.Input[Union[DeploymentGroupEcsServiceArgs, DeploymentGroupEcsServiceArgsDict]]] = ..., load_balancer_info: Optional[pulumi.Input[Union[DeploymentGroupLoadBalancerInfoArgs, DeploymentGroupLoadBalancerInfoArgsDict]]] = ..., on_premises_instance_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentGroupOnPremisesInstanceTagFilterArgs, DeploymentGroupOnPremisesInstanceTagFilterArgsDict]]]]] = ..., outdated_instances_strategy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., termination_hook_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., trigger_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentGroupTriggerConfigurationArgs, DeploymentGroupTriggerConfigurationArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeploymentGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., alarm_configuration: Optional[pulumi.Input[Union[DeploymentGroupAlarmConfigurationArgs, DeploymentGroupAlarmConfigurationArgsDict]]] = ..., app_name: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_rollback_configuration: Optional[pulumi.Input[Union[DeploymentGroupAutoRollbackConfigurationArgs, DeploymentGroupAutoRollbackConfigurationArgsDict]]] = ..., autoscaling_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., blue_green_deployment_config: Optional[pulumi.Input[Union[DeploymentGroupBlueGreenDeploymentConfigArgs, DeploymentGroupBlueGreenDeploymentConfigArgsDict]]] = ..., compute_platform: Optional[pulumi.Input[_builtins.str]] = ..., deployment_config_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_group_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment_group_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_style: Optional[pulumi.Input[Union[DeploymentGroupDeploymentStyleArgs, DeploymentGroupDeploymentStyleArgsDict]]] = ..., ec2_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentGroupEc2TagFilterArgs, DeploymentGroupEc2TagFilterArgsDict]]]]] = ..., ec2_tag_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentGroupEc2TagSetArgs, DeploymentGroupEc2TagSetArgsDict]]]]] = ..., ecs_service: Optional[pulumi.Input[Union[DeploymentGroupEcsServiceArgs, DeploymentGroupEcsServiceArgsDict]]] = ..., load_balancer_info: Optional[pulumi.Input[Union[DeploymentGroupLoadBalancerInfoArgs, DeploymentGroupLoadBalancerInfoArgsDict]]] = ..., on_premises_instance_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentGroupOnPremisesInstanceTagFilterArgs, DeploymentGroupOnPremisesInstanceTagFilterArgsDict]]]]] = ..., outdated_instances_strategy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., termination_hook_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., trigger_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentGroupTriggerConfigurationArgs, DeploymentGroupTriggerConfigurationArgsDict]]]]] = ...) -> DeploymentGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmConfiguration")
    def alarm_configuration(self) -> pulumi.Output[Optional[outputs.DeploymentGroupAlarmConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRollbackConfiguration")
    def auto_rollback_configuration(self) -> pulumi.Output[Optional[outputs.DeploymentGroupAutoRollbackConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroups")
    def autoscaling_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blueGreenDeploymentConfig")
    def blue_green_deployment_config(self) -> pulumi.Output[outputs.DeploymentGroupBlueGreenDeploymentConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computePlatform")
    def compute_platform(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfigName")
    def deployment_config_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentGroupId")
    def deployment_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentGroupName")
    def deployment_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStyle")
    def deployment_style(self) -> pulumi.Output[Optional[outputs.DeploymentGroupDeploymentStyle]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2TagFilters")
    def ec2_tag_filters(self) -> pulumi.Output[Optional[Sequence[outputs.DeploymentGroupEc2TagFilter]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2TagSets")
    def ec2_tag_sets(self) -> pulumi.Output[Optional[Sequence[outputs.DeploymentGroupEc2TagSet]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ecsService")
    def ecs_service(self) -> pulumi.Output[Optional[outputs.DeploymentGroupEcsService]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerInfo")
    def load_balancer_info(self) -> pulumi.Output[Optional[outputs.DeploymentGroupLoadBalancerInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremisesInstanceTagFilters")
    def on_premises_instance_tag_filters(self) -> pulumi.Output[Optional[Sequence[outputs.DeploymentGroupOnPremisesInstanceTagFilter]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outdatedInstancesStrategy")
    def outdated_instances_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationHookEnabled")
    def termination_hook_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerConfigurations")
    def trigger_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.DeploymentGroupTriggerConfiguration]]]:
        
        ...
    


