

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGroupResult', 'AwaitableGetGroupResult', 'get_group', 'get_group_output']
@pulumi.output_type
class GetGroupResult:
    
    def __init__(__self__, arn=..., availability_zones=..., default_cooldown=..., desired_capacity=..., desired_capacity_type=..., enabled_metrics=..., health_check_grace_period=..., health_check_type=..., id=..., instance_maintenance_policies=..., launch_configuration=..., launch_templates=..., load_balancers=..., max_instance_lifetime=..., max_size=..., min_size=..., mixed_instances_policies=..., name=..., new_instances_protected_from_scale_in=..., placement_group=..., predicted_capacity=..., region=..., service_linked_role_arn=..., status=..., suspended_processes=..., tags=..., target_group_arns=..., termination_policies=..., traffic_sources=..., vpc_zone_identifier=..., warm_pool_size=..., warm_pools=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCooldown")
    def default_cooldown(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacityType")
    def desired_capacity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledMetrics")
    def enabled_metrics(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckGracePeriod")
    def health_check_grace_period(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckType")
    def health_check_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMaintenancePolicies")
    def instance_maintenance_policies(self) -> Sequence[outputs.GetGroupInstanceMaintenancePolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchConfiguration")
    def launch_configuration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplates")
    def launch_templates(self) -> Sequence[outputs.GetGroupLaunchTemplateResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceLifetime")
    def max_instance_lifetime(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mixedInstancesPolicies")
    def mixed_instances_policies(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newInstancesProtectedFromScaleIn")
    def new_instances_protected_from_scale_in(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predictedCapacity")
    def predicted_capacity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLinkedRoleArn")
    def service_linked_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspendedProcesses")
    def suspended_processes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetGroupTagResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArns")
    def target_group_arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationPolicies")
    def termination_policies(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficSources")
    def traffic_sources(self) -> Sequence[outputs.GetGroupTrafficSourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcZoneIdentifier")
    def vpc_zone_identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmPoolSize")
    def warm_pool_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmPools")
    def warm_pools(self) -> Sequence[outputs.GetGroupWarmPoolResult]:
        
        ...
    


class AwaitableGetGroupResult(GetGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetGroupResult]:
        ...
    


def get_group(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGroupResult:
    
    ...

def get_group_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGroupResult]:
    
    ...

