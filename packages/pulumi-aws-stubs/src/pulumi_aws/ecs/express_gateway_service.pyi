

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
__all__ = ['ExpressGatewayServiceArgs', 'ExpressGatewayService']
@pulumi.input_type
class ExpressGatewayServiceArgs:
    def __init__(__self__, *, execution_role_arn: pulumi.Input[_builtins.str], infrastructure_role_arn: pulumi.Input[_builtins.str], primary_container: pulumi.Input[ExpressGatewayServicePrimaryContainerArgs], cluster: Optional[pulumi.Input[_builtins.str]] = ..., cpu: Optional[pulumi.Input[_builtins.str]] = ..., health_check_path: Optional[pulumi.Input[_builtins.str]] = ..., memory: Optional[pulumi.Input[_builtins.str]] = ..., network_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceNetworkConfigurationArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_targets: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceScalingTargetArgs]]]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ExpressGatewayServiceTimeoutsArgs]] = ..., wait_for_steady_state: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureRoleArn")
    def infrastructure_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @infrastructure_role_arn.setter
    def infrastructure_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContainer")
    def primary_container(self) -> pulumi.Input[ExpressGatewayServicePrimaryContainerArgs]:
        ...
    
    @primary_container.setter
    def primary_container(self, value: pulumi.Input[ExpressGatewayServicePrimaryContainerArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @health_check_path.setter
    def health_check_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfigurations")
    def network_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceNetworkConfigurationArgs]]]]:
        ...
    
    @network_configurations.setter
    def network_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceNetworkConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingTargets")
    def scaling_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceScalingTargetArgs]]]]:
        ...
    
    @scaling_targets.setter
    def scaling_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceScalingTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_role_arn.setter
    def task_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ExpressGatewayServiceTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ExpressGatewayServiceTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForSteadyState")
    def wait_for_steady_state(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_steady_state.setter
    def wait_for_steady_state(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _ExpressGatewayServiceState:
    def __init__(__self__, *, cluster: Optional[pulumi.Input[_builtins.str]] = ..., cpu: Optional[pulumi.Input[_builtins.str]] = ..., current_deployment: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., health_check_path: Optional[pulumi.Input[_builtins.str]] = ..., infrastructure_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., ingress_paths: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceIngressPathArgs]]]] = ..., memory: Optional[pulumi.Input[_builtins.str]] = ..., network_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceNetworkConfigurationArgs]]]] = ..., primary_container: Optional[pulumi.Input[ExpressGatewayServicePrimaryContainerArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_targets: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceScalingTargetArgs]]]] = ..., service_arn: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., service_revision_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ExpressGatewayServiceTimeoutsArgs]] = ..., wait_for_steady_state: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentDeployment")
    def current_deployment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @current_deployment.setter
    def current_deployment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @health_check_path.setter
    def health_check_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureRoleArn")
    def infrastructure_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @infrastructure_role_arn.setter
    def infrastructure_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressPaths")
    def ingress_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceIngressPathArgs]]]]:
        
        ...
    
    @ingress_paths.setter
    def ingress_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceIngressPathArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfigurations")
    def network_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceNetworkConfigurationArgs]]]]:
        ...
    
    @network_configurations.setter
    def network_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceNetworkConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContainer")
    def primary_container(self) -> Optional[pulumi.Input[ExpressGatewayServicePrimaryContainerArgs]]:
        ...
    
    @primary_container.setter
    def primary_container(self, value: Optional[pulumi.Input[ExpressGatewayServicePrimaryContainerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingTargets")
    def scaling_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceScalingTargetArgs]]]]:
        ...
    
    @scaling_targets.setter
    def scaling_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressGatewayServiceScalingTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_arn.setter
    def service_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRevisionArn")
    def service_revision_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_revision_arn.setter
    def service_revision_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_role_arn.setter
    def task_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ExpressGatewayServiceTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ExpressGatewayServiceTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForSteadyState")
    def wait_for_steady_state(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_steady_state.setter
    def wait_for_steady_state(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ExpressGatewayService(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., cpu: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., health_check_path: Optional[pulumi.Input[_builtins.str]] = ..., infrastructure_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., memory: Optional[pulumi.Input[_builtins.str]] = ..., network_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ExpressGatewayServiceNetworkConfigurationArgs, ExpressGatewayServiceNetworkConfigurationArgsDict]]]]] = ..., primary_container: Optional[pulumi.Input[Union[ExpressGatewayServicePrimaryContainerArgs, ExpressGatewayServicePrimaryContainerArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ExpressGatewayServiceScalingTargetArgs, ExpressGatewayServiceScalingTargetArgsDict]]]]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ExpressGatewayServiceTimeoutsArgs, ExpressGatewayServiceTimeoutsArgsDict]]] = ..., wait_for_steady_state: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExpressGatewayServiceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., cpu: Optional[pulumi.Input[_builtins.str]] = ..., current_deployment: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., health_check_path: Optional[pulumi.Input[_builtins.str]] = ..., infrastructure_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., ingress_paths: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ExpressGatewayServiceIngressPathArgs, ExpressGatewayServiceIngressPathArgsDict]]]]] = ..., memory: Optional[pulumi.Input[_builtins.str]] = ..., network_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ExpressGatewayServiceNetworkConfigurationArgs, ExpressGatewayServiceNetworkConfigurationArgsDict]]]]] = ..., primary_container: Optional[pulumi.Input[Union[ExpressGatewayServicePrimaryContainerArgs, ExpressGatewayServicePrimaryContainerArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ExpressGatewayServiceScalingTargetArgs, ExpressGatewayServiceScalingTargetArgsDict]]]]] = ..., service_arn: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., service_revision_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ExpressGatewayServiceTimeoutsArgs, ExpressGatewayServiceTimeoutsArgsDict]]] = ..., wait_for_steady_state: Optional[pulumi.Input[_builtins.bool]] = ...) -> ExpressGatewayService:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentDeployment")
    def current_deployment(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureRoleArn")
    def infrastructure_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressPaths")
    def ingress_paths(self) -> pulumi.Output[Sequence[outputs.ExpressGatewayServiceIngressPath]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfigurations")
    def network_configurations(self) -> pulumi.Output[Sequence[outputs.ExpressGatewayServiceNetworkConfiguration]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContainer")
    def primary_container(self) -> pulumi.Output[outputs.ExpressGatewayServicePrimaryContainer]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingTargets")
    def scaling_targets(self) -> pulumi.Output[Sequence[outputs.ExpressGatewayServiceScalingTarget]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRevisionArn")
    def service_revision_arn(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ExpressGatewayServiceTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForSteadyState")
    def wait_for_steady_state(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    


