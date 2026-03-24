

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegionInstanceGroupManagerArgs', 'RegionInstanceGroupManager']
@pulumi.input_type
class RegionInstanceGroupManagerArgs:
    def __init__(__self__, *, base_instance_name: pulumi.Input[_builtins.str], versions: pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerVersionArgs]]], all_instances_config: Optional[pulumi.Input[RegionInstanceGroupManagerAllInstancesConfigArgs]] = ..., auto_healing_policies: Optional[pulumi.Input[RegionInstanceGroupManagerAutoHealingPoliciesArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., distribution_policy_target_shape: Optional[pulumi.Input[_builtins.str]] = ..., distribution_policy_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instance_flexibility_policy: Optional[pulumi.Input[RegionInstanceGroupManagerInstanceFlexibilityPolicyArgs]] = ..., instance_lifecycle_policy: Optional[pulumi.Input[RegionInstanceGroupManagerInstanceLifecyclePolicyArgs]] = ..., list_managed_instances_results: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., named_ports: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerNamedPortArgs]]]] = ..., params: Optional[pulumi.Input[RegionInstanceGroupManagerParamsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., standby_policy: Optional[pulumi.Input[RegionInstanceGroupManagerStandbyPolicyArgs]] = ..., stateful_disks: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulDiskArgs]]]] = ..., stateful_external_ips: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulExternalIpArgs]]]] = ..., stateful_internal_ips: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulInternalIpArgs]]]] = ..., target_pools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_size: Optional[pulumi.Input[_builtins.int]] = ..., target_stopped_size: Optional[pulumi.Input[_builtins.int]] = ..., target_suspended_size: Optional[pulumi.Input[_builtins.int]] = ..., update_policy: Optional[pulumi.Input[RegionInstanceGroupManagerUpdatePolicyArgs]] = ..., wait_for_instances: Optional[pulumi.Input[_builtins.bool]] = ..., wait_for_instances_status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseInstanceName")
    def base_instance_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @base_instance_name.setter
    def base_instance_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerVersionArgs]]]:
        
        ...
    
    @versions.setter
    def versions(self, value: pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerVersionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allInstancesConfig")
    def all_instances_config(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerAllInstancesConfigArgs]]:
        
        ...
    
    @all_instances_config.setter
    def all_instances_config(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerAllInstancesConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoHealingPolicies")
    def auto_healing_policies(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerAutoHealingPoliciesArgs]]:
        
        ...
    
    @auto_healing_policies.setter
    def auto_healing_policies(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerAutoHealingPoliciesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionPolicyTargetShape")
    def distribution_policy_target_shape(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @distribution_policy_target_shape.setter
    def distribution_policy_target_shape(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionPolicyZones")
    def distribution_policy_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @distribution_policy_zones.setter
    def distribution_policy_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceFlexibilityPolicy")
    def instance_flexibility_policy(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerInstanceFlexibilityPolicyArgs]]:
        
        ...
    
    @instance_flexibility_policy.setter
    def instance_flexibility_policy(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerInstanceFlexibilityPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceLifecyclePolicy")
    def instance_lifecycle_policy(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerInstanceLifecyclePolicyArgs]]:
        
        ...
    
    @instance_lifecycle_policy.setter
    def instance_lifecycle_policy(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerInstanceLifecyclePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listManagedInstancesResults")
    def list_managed_instances_results(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @list_managed_instances_results.setter
    def list_managed_instances_results(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namedPorts")
    def named_ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerNamedPortArgs]]]]:
        
        ...
    
    @named_ports.setter
    def named_ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerNamedPortArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="standbyPolicy")
    def standby_policy(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerStandbyPolicyArgs]]:
        
        ...
    
    @standby_policy.setter
    def standby_policy(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerStandbyPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulDisks")
    def stateful_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulDiskArgs]]]]:
        
        ...
    
    @stateful_disks.setter
    def stateful_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulExternalIps")
    def stateful_external_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulExternalIpArgs]]]]:
        
        ...
    
    @stateful_external_ips.setter
    def stateful_external_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulExternalIpArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulInternalIps")
    def stateful_internal_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulInternalIpArgs]]]]:
        
        ...
    
    @stateful_internal_ips.setter
    def stateful_internal_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulInternalIpArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPools")
    def target_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_pools.setter
    def target_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSize")
    def target_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_size.setter
    def target_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetStoppedSize")
    def target_stopped_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_stopped_size.setter
    def target_stopped_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSuspendedSize")
    def target_suspended_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_suspended_size.setter
    def target_suspended_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatePolicy")
    def update_policy(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerUpdatePolicyArgs]]:
        
        ...
    
    @update_policy.setter
    def update_policy(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerUpdatePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForInstances")
    def wait_for_instances(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_instances.setter
    def wait_for_instances(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForInstancesStatus")
    def wait_for_instances_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @wait_for_instances_status.setter
    def wait_for_instances_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RegionInstanceGroupManagerState:
    def __init__(__self__, *, all_instances_config: Optional[pulumi.Input[RegionInstanceGroupManagerAllInstancesConfigArgs]] = ..., auto_healing_policies: Optional[pulumi.Input[RegionInstanceGroupManagerAutoHealingPoliciesArgs]] = ..., base_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., distribution_policy_target_shape: Optional[pulumi.Input[_builtins.str]] = ..., distribution_policy_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., instance_flexibility_policy: Optional[pulumi.Input[RegionInstanceGroupManagerInstanceFlexibilityPolicyArgs]] = ..., instance_group: Optional[pulumi.Input[_builtins.str]] = ..., instance_group_manager_id: Optional[pulumi.Input[_builtins.int]] = ..., instance_lifecycle_policy: Optional[pulumi.Input[RegionInstanceGroupManagerInstanceLifecyclePolicyArgs]] = ..., list_managed_instances_results: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., named_ports: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerNamedPortArgs]]]] = ..., params: Optional[pulumi.Input[RegionInstanceGroupManagerParamsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., standby_policy: Optional[pulumi.Input[RegionInstanceGroupManagerStandbyPolicyArgs]] = ..., stateful_disks: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulDiskArgs]]]] = ..., stateful_external_ips: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulExternalIpArgs]]]] = ..., stateful_internal_ips: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulInternalIpArgs]]]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatusArgs]]]] = ..., target_pools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_size: Optional[pulumi.Input[_builtins.int]] = ..., target_stopped_size: Optional[pulumi.Input[_builtins.int]] = ..., target_suspended_size: Optional[pulumi.Input[_builtins.int]] = ..., update_policy: Optional[pulumi.Input[RegionInstanceGroupManagerUpdatePolicyArgs]] = ..., versions: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerVersionArgs]]]] = ..., wait_for_instances: Optional[pulumi.Input[_builtins.bool]] = ..., wait_for_instances_status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allInstancesConfig")
    def all_instances_config(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerAllInstancesConfigArgs]]:
        
        ...
    
    @all_instances_config.setter
    def all_instances_config(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerAllInstancesConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoHealingPolicies")
    def auto_healing_policies(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerAutoHealingPoliciesArgs]]:
        
        ...
    
    @auto_healing_policies.setter
    def auto_healing_policies(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerAutoHealingPoliciesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseInstanceName")
    def base_instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @base_instance_name.setter
    def base_instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionPolicyTargetShape")
    def distribution_policy_target_shape(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @distribution_policy_target_shape.setter
    def distribution_policy_target_shape(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionPolicyZones")
    def distribution_policy_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @distribution_policy_zones.setter
    def distribution_policy_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceFlexibilityPolicy")
    def instance_flexibility_policy(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerInstanceFlexibilityPolicyArgs]]:
        
        ...
    
    @instance_flexibility_policy.setter
    def instance_flexibility_policy(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerInstanceFlexibilityPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroup")
    def instance_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_group.setter
    def instance_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerId")
    def instance_group_manager_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_group_manager_id.setter
    def instance_group_manager_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceLifecyclePolicy")
    def instance_lifecycle_policy(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerInstanceLifecyclePolicyArgs]]:
        
        ...
    
    @instance_lifecycle_policy.setter
    def instance_lifecycle_policy(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerInstanceLifecyclePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listManagedInstancesResults")
    def list_managed_instances_results(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @list_managed_instances_results.setter
    def list_managed_instances_results(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namedPorts")
    def named_ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerNamedPortArgs]]]]:
        
        ...
    
    @named_ports.setter
    def named_ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerNamedPortArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="standbyPolicy")
    def standby_policy(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerStandbyPolicyArgs]]:
        
        ...
    
    @standby_policy.setter
    def standby_policy(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerStandbyPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulDisks")
    def stateful_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulDiskArgs]]]]:
        
        ...
    
    @stateful_disks.setter
    def stateful_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulExternalIps")
    def stateful_external_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulExternalIpArgs]]]]:
        
        ...
    
    @stateful_external_ips.setter
    def stateful_external_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulExternalIpArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulInternalIps")
    def stateful_internal_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulInternalIpArgs]]]]:
        
        ...
    
    @stateful_internal_ips.setter
    def stateful_internal_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatefulInternalIpArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatusArgs]]]]:
        
        ...
    
    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPools")
    def target_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_pools.setter
    def target_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSize")
    def target_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_size.setter
    def target_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetStoppedSize")
    def target_stopped_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_stopped_size.setter
    def target_stopped_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSuspendedSize")
    def target_suspended_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_suspended_size.setter
    def target_suspended_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatePolicy")
    def update_policy(self) -> Optional[pulumi.Input[RegionInstanceGroupManagerUpdatePolicyArgs]]:
        
        ...
    
    @update_policy.setter
    def update_policy(self, value: Optional[pulumi.Input[RegionInstanceGroupManagerUpdatePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerVersionArgs]]]]:
        
        ...
    
    @versions.setter
    def versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionInstanceGroupManagerVersionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForInstances")
    def wait_for_instances(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_instances.setter
    def wait_for_instances(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForInstancesStatus")
    def wait_for_instances_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @wait_for_instances_status.setter
    def wait_for_instances_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RegionInstanceGroupManager(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., all_instances_config: Optional[pulumi.Input[Union[RegionInstanceGroupManagerAllInstancesConfigArgs, RegionInstanceGroupManagerAllInstancesConfigArgsDict]]] = ..., auto_healing_policies: Optional[pulumi.Input[Union[RegionInstanceGroupManagerAutoHealingPoliciesArgs, RegionInstanceGroupManagerAutoHealingPoliciesArgsDict]]] = ..., base_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., distribution_policy_target_shape: Optional[pulumi.Input[_builtins.str]] = ..., distribution_policy_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instance_flexibility_policy: Optional[pulumi.Input[Union[RegionInstanceGroupManagerInstanceFlexibilityPolicyArgs, RegionInstanceGroupManagerInstanceFlexibilityPolicyArgsDict]]] = ..., instance_lifecycle_policy: Optional[pulumi.Input[Union[RegionInstanceGroupManagerInstanceLifecyclePolicyArgs, RegionInstanceGroupManagerInstanceLifecyclePolicyArgsDict]]] = ..., list_managed_instances_results: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., named_ports: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerNamedPortArgs, RegionInstanceGroupManagerNamedPortArgsDict]]]]] = ..., params: Optional[pulumi.Input[Union[RegionInstanceGroupManagerParamsArgs, RegionInstanceGroupManagerParamsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., standby_policy: Optional[pulumi.Input[Union[RegionInstanceGroupManagerStandbyPolicyArgs, RegionInstanceGroupManagerStandbyPolicyArgsDict]]] = ..., stateful_disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerStatefulDiskArgs, RegionInstanceGroupManagerStatefulDiskArgsDict]]]]] = ..., stateful_external_ips: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerStatefulExternalIpArgs, RegionInstanceGroupManagerStatefulExternalIpArgsDict]]]]] = ..., stateful_internal_ips: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerStatefulInternalIpArgs, RegionInstanceGroupManagerStatefulInternalIpArgsDict]]]]] = ..., target_pools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_size: Optional[pulumi.Input[_builtins.int]] = ..., target_stopped_size: Optional[pulumi.Input[_builtins.int]] = ..., target_suspended_size: Optional[pulumi.Input[_builtins.int]] = ..., update_policy: Optional[pulumi.Input[Union[RegionInstanceGroupManagerUpdatePolicyArgs, RegionInstanceGroupManagerUpdatePolicyArgsDict]]] = ..., versions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerVersionArgs, RegionInstanceGroupManagerVersionArgsDict]]]]] = ..., wait_for_instances: Optional[pulumi.Input[_builtins.bool]] = ..., wait_for_instances_status: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RegionInstanceGroupManagerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., all_instances_config: Optional[pulumi.Input[Union[RegionInstanceGroupManagerAllInstancesConfigArgs, RegionInstanceGroupManagerAllInstancesConfigArgsDict]]] = ..., auto_healing_policies: Optional[pulumi.Input[Union[RegionInstanceGroupManagerAutoHealingPoliciesArgs, RegionInstanceGroupManagerAutoHealingPoliciesArgsDict]]] = ..., base_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., distribution_policy_target_shape: Optional[pulumi.Input[_builtins.str]] = ..., distribution_policy_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., instance_flexibility_policy: Optional[pulumi.Input[Union[RegionInstanceGroupManagerInstanceFlexibilityPolicyArgs, RegionInstanceGroupManagerInstanceFlexibilityPolicyArgsDict]]] = ..., instance_group: Optional[pulumi.Input[_builtins.str]] = ..., instance_group_manager_id: Optional[pulumi.Input[_builtins.int]] = ..., instance_lifecycle_policy: Optional[pulumi.Input[Union[RegionInstanceGroupManagerInstanceLifecyclePolicyArgs, RegionInstanceGroupManagerInstanceLifecyclePolicyArgsDict]]] = ..., list_managed_instances_results: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., named_ports: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerNamedPortArgs, RegionInstanceGroupManagerNamedPortArgsDict]]]]] = ..., params: Optional[pulumi.Input[Union[RegionInstanceGroupManagerParamsArgs, RegionInstanceGroupManagerParamsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., standby_policy: Optional[pulumi.Input[Union[RegionInstanceGroupManagerStandbyPolicyArgs, RegionInstanceGroupManagerStandbyPolicyArgsDict]]] = ..., stateful_disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerStatefulDiskArgs, RegionInstanceGroupManagerStatefulDiskArgsDict]]]]] = ..., stateful_external_ips: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerStatefulExternalIpArgs, RegionInstanceGroupManagerStatefulExternalIpArgsDict]]]]] = ..., stateful_internal_ips: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerStatefulInternalIpArgs, RegionInstanceGroupManagerStatefulInternalIpArgsDict]]]]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerStatusArgs, RegionInstanceGroupManagerStatusArgsDict]]]]] = ..., target_pools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_size: Optional[pulumi.Input[_builtins.int]] = ..., target_stopped_size: Optional[pulumi.Input[_builtins.int]] = ..., target_suspended_size: Optional[pulumi.Input[_builtins.int]] = ..., update_policy: Optional[pulumi.Input[Union[RegionInstanceGroupManagerUpdatePolicyArgs, RegionInstanceGroupManagerUpdatePolicyArgsDict]]] = ..., versions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionInstanceGroupManagerVersionArgs, RegionInstanceGroupManagerVersionArgsDict]]]]] = ..., wait_for_instances: Optional[pulumi.Input[_builtins.bool]] = ..., wait_for_instances_status: Optional[pulumi.Input[_builtins.str]] = ...) -> RegionInstanceGroupManager:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allInstancesConfig")
    def all_instances_config(self) -> pulumi.Output[Optional[outputs.RegionInstanceGroupManagerAllInstancesConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoHealingPolicies")
    def auto_healing_policies(self) -> pulumi.Output[Optional[outputs.RegionInstanceGroupManagerAutoHealingPolicies]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseInstanceName")
    def base_instance_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionPolicyTargetShape")
    def distribution_policy_target_shape(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionPolicyZones")
    def distribution_policy_zones(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceFlexibilityPolicy")
    def instance_flexibility_policy(self) -> pulumi.Output[Optional[outputs.RegionInstanceGroupManagerInstanceFlexibilityPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroup")
    def instance_group(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerId")
    def instance_group_manager_id(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceLifecyclePolicy")
    def instance_lifecycle_policy(self) -> pulumi.Output[outputs.RegionInstanceGroupManagerInstanceLifecyclePolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listManagedInstancesResults")
    def list_managed_instances_results(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namedPorts")
    def named_ports(self) -> pulumi.Output[Optional[Sequence[outputs.RegionInstanceGroupManagerNamedPort]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.RegionInstanceGroupManagerParams]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standbyPolicy")
    def standby_policy(self) -> pulumi.Output[outputs.RegionInstanceGroupManagerStandbyPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulDisks")
    def stateful_disks(self) -> pulumi.Output[Optional[Sequence[outputs.RegionInstanceGroupManagerStatefulDisk]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulExternalIps")
    def stateful_external_ips(self) -> pulumi.Output[Optional[Sequence[outputs.RegionInstanceGroupManagerStatefulExternalIp]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulInternalIps")
    def stateful_internal_ips(self) -> pulumi.Output[Optional[Sequence[outputs.RegionInstanceGroupManagerStatefulInternalIp]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.RegionInstanceGroupManagerStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPools")
    def target_pools(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSize")
    def target_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetStoppedSize")
    def target_stopped_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSuspendedSize")
    def target_suspended_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatePolicy")
    def update_policy(self) -> pulumi.Output[outputs.RegionInstanceGroupManagerUpdatePolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> pulumi.Output[Sequence[outputs.RegionInstanceGroupManagerVersion]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForInstances")
    def wait_for_instances(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForInstancesStatus")
    def wait_for_instances_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


