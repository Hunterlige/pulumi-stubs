import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServiceResult",
    "AwaitableGetServiceResult",
    "get_service",
    "get_service_output",
]

@pulumi.output_type
class GetServiceResult:
    def __init__(
        __self__,
        arn=...,
        availability_zone_rebalancing=...,
        capacity_provider_strategies=...,
        cluster_arn=...,
        created_at=...,
        created_by=...,
        deployment_configurations=...,
        deployment_controllers=...,
        deployments=...,
        desired_count=...,
        enable_ecs_managed_tags=...,
        enable_execute_command=...,
        events=...,
        health_check_grace_period_seconds=...,
        iam_role=...,
        id=...,
        launch_type=...,
        load_balancers=...,
        network_configurations=...,
        ordered_placement_strategies=...,
        pending_count=...,
        placement_constraints=...,
        platform_family=...,
        platform_version=...,
        propagate_tags=...,
        region=...,
        running_count=...,
        scheduling_strategy=...,
        service_name=...,
        service_registries=...,
        status=...,
        tags=...,
        task_definition=...,
        task_sets=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneRebalancing")
    def availability_zone_rebalancing(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(
        self,
    ) -> Sequence[outputs.GetServiceCapacityProviderStrategyResult]: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentConfigurations")
    def deployment_configurations(
        self,
    ) -> Sequence[outputs.GetServiceDeploymentConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentControllers")
    def deployment_controllers(
        self,
    ) -> Sequence[outputs.GetServiceDeploymentControllerResult]: ...
    @_builtins.property
    @pulumi.getter
    def deployments(self) -> Sequence[outputs.GetServiceDeploymentResult]: ...
    @_builtins.property
    @pulumi.getter(name="desiredCount")
    def desired_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Sequence[outputs.GetServiceEventResult]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckGracePeriodSeconds")
    def health_check_grace_period_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="iamRole")
    def iam_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Sequence[outputs.GetServiceLoadBalancerResult]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigurations")
    def network_configurations(
        self,
    ) -> Sequence[outputs.GetServiceNetworkConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="orderedPlacementStrategies")
    def ordered_placement_strategies(
        self,
    ) -> Sequence[outputs.GetServiceOrderedPlacementStrategyResult]: ...
    @_builtins.property
    @pulumi.getter(name="pendingCount")
    def pending_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(
        self,
    ) -> Sequence[outputs.GetServicePlacementConstraintResult]: ...
    @_builtins.property
    @pulumi.getter(name="platformFamily")
    def platform_family(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runningCount")
    def running_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="schedulingStrategy")
    def scheduling_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceRegistries")
    def service_registries(
        self,
    ) -> Sequence[outputs.GetServiceServiceRegistryResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="taskSets")
    def task_sets(self) -> Sequence[outputs.GetServiceTaskSetResult]: ...

class AwaitableGetServiceResult(GetServiceResult):
    def __await__(self): ...

def get_service(
    cluster_arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServiceResult: ...
def get_service_output(
    cluster_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServiceResult]: ...
