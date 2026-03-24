

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
__all__ = ['TaskSetArgs', 'TaskSet']
@pulumi.input_type
class TaskSetArgs:
    def __init__(__self__, *, cluster: pulumi.Input[_builtins.str], service: pulumi.Input[_builtins.str], task_definition: pulumi.Input[_builtins.str], capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetCapacityProviderStrategyArgs]]]] = ..., external_id: Optional[pulumi.Input[_builtins.str]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., launch_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetLoadBalancerArgs]]]] = ..., network_configuration: Optional[pulumi.Input[TaskSetNetworkConfigurationArgs]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scale: Optional[pulumi.Input[TaskSetScaleArgs]] = ..., service_registries: Optional[pulumi.Input[TaskSetServiceRegistriesArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., wait_until_stable: Optional[pulumi.Input[_builtins.bool]] = ..., wait_until_stable_timeout: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_definition.setter
    def task_definition(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetCapacityProviderStrategyArgs]]]]:
        
        ...
    
    @capacity_provider_strategies.setter
    def capacity_provider_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetCapacityProviderStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_type.setter
    def launch_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetLoadBalancerArgs]]]]:
        
        ...
    
    @load_balancers.setter
    def load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetLoadBalancerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input[TaskSetNetworkConfigurationArgs]]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input[TaskSetNetworkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def scale(self) -> Optional[pulumi.Input[TaskSetScaleArgs]]:
        
        ...
    
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[TaskSetScaleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRegistries")
    def service_registries(self) -> Optional[pulumi.Input[TaskSetServiceRegistriesArgs]]:
        
        ...
    
    @service_registries.setter
    def service_registries(self, value: Optional[pulumi.Input[TaskSetServiceRegistriesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitUntilStable")
    def wait_until_stable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_until_stable.setter
    def wait_until_stable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitUntilStableTimeout")
    def wait_until_stable_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @wait_until_stable_timeout.setter
    def wait_until_stable_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TaskSetState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetCapacityProviderStrategyArgs]]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., external_id: Optional[pulumi.Input[_builtins.str]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., launch_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetLoadBalancerArgs]]]] = ..., network_configuration: Optional[pulumi.Input[TaskSetNetworkConfigurationArgs]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scale: Optional[pulumi.Input[TaskSetScaleArgs]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., service_registries: Optional[pulumi.Input[TaskSetServiceRegistriesArgs]] = ..., stability_status: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_definition: Optional[pulumi.Input[_builtins.str]] = ..., task_set_id: Optional[pulumi.Input[_builtins.str]] = ..., wait_until_stable: Optional[pulumi.Input[_builtins.bool]] = ..., wait_until_stable_timeout: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetCapacityProviderStrategyArgs]]]]:
        
        ...
    
    @capacity_provider_strategies.setter
    def capacity_provider_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetCapacityProviderStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_type.setter
    def launch_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetLoadBalancerArgs]]]]:
        
        ...
    
    @load_balancers.setter
    def load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TaskSetLoadBalancerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input[TaskSetNetworkConfigurationArgs]]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input[TaskSetNetworkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def scale(self) -> Optional[pulumi.Input[TaskSetScaleArgs]]:
        
        ...
    
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[TaskSetScaleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRegistries")
    def service_registries(self) -> Optional[pulumi.Input[TaskSetServiceRegistriesArgs]]:
        
        ...
    
    @service_registries.setter
    def service_registries(self, value: Optional[pulumi.Input[TaskSetServiceRegistriesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stabilityStatus")
    def stability_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stability_status.setter
    def stability_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_definition.setter
    def task_definition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskSetId")
    def task_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_set_id.setter
    def task_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitUntilStable")
    def wait_until_stable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_until_stable.setter
    def wait_until_stable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitUntilStableTimeout")
    def wait_until_stable_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @wait_until_stable_timeout.setter
    def wait_until_stable_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ecs/taskSet:TaskSet")
class TaskSet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TaskSetCapacityProviderStrategyArgs, TaskSetCapacityProviderStrategyArgsDict]]]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., external_id: Optional[pulumi.Input[_builtins.str]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., launch_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TaskSetLoadBalancerArgs, TaskSetLoadBalancerArgsDict]]]]] = ..., network_configuration: Optional[pulumi.Input[Union[TaskSetNetworkConfigurationArgs, TaskSetNetworkConfigurationArgsDict]]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scale: Optional[pulumi.Input[Union[TaskSetScaleArgs, TaskSetScaleArgsDict]]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., service_registries: Optional[pulumi.Input[Union[TaskSetServiceRegistriesArgs, TaskSetServiceRegistriesArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_definition: Optional[pulumi.Input[_builtins.str]] = ..., wait_until_stable: Optional[pulumi.Input[_builtins.bool]] = ..., wait_until_stable_timeout: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TaskSetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TaskSetCapacityProviderStrategyArgs, TaskSetCapacityProviderStrategyArgsDict]]]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., external_id: Optional[pulumi.Input[_builtins.str]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., launch_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TaskSetLoadBalancerArgs, TaskSetLoadBalancerArgsDict]]]]] = ..., network_configuration: Optional[pulumi.Input[Union[TaskSetNetworkConfigurationArgs, TaskSetNetworkConfigurationArgsDict]]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scale: Optional[pulumi.Input[Union[TaskSetScaleArgs, TaskSetScaleArgsDict]]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., service_registries: Optional[pulumi.Input[Union[TaskSetServiceRegistriesArgs, TaskSetServiceRegistriesArgsDict]]] = ..., stability_status: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_definition: Optional[pulumi.Input[_builtins.str]] = ..., task_set_id: Optional[pulumi.Input[_builtins.str]] = ..., wait_until_stable: Optional[pulumi.Input[_builtins.bool]] = ..., wait_until_stable_timeout: Optional[pulumi.Input[_builtins.str]] = ...) -> TaskSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(self) -> pulumi.Output[Optional[Sequence[outputs.TaskSetCapacityProviderStrategy]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> pulumi.Output[Optional[Sequence[outputs.TaskSetLoadBalancer]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Output[Optional[outputs.TaskSetNetworkConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> pulumi.Output[outputs.TaskSetScale]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRegistries")
    def service_registries(self) -> pulumi.Output[Optional[outputs.TaskSetServiceRegistries]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stabilityStatus")
    def stability_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskSetId")
    def task_set_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitUntilStable")
    def wait_until_stable(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitUntilStableTimeout")
    def wait_until_stable_timeout(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


