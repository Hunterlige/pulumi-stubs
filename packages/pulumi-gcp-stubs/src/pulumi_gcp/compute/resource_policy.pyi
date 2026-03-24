

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResourcePolicyArgs', 'ResourcePolicy']
@pulumi.input_type
class ResourcePolicyArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., disk_consistency_group_policy: Optional[pulumi.Input[ResourcePolicyDiskConsistencyGroupPolicyArgs]] = ..., group_placement_policy: Optional[pulumi.Input[ResourcePolicyGroupPlacementPolicyArgs]] = ..., instance_schedule_policy: Optional[pulumi.Input[ResourcePolicyInstanceSchedulePolicyArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_schedule_policy: Optional[pulumi.Input[ResourcePolicySnapshotSchedulePolicyArgs]] = ..., workload_policy: Optional[pulumi.Input[ResourcePolicyWorkloadPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConsistencyGroupPolicy")
    def disk_consistency_group_policy(self) -> Optional[pulumi.Input[ResourcePolicyDiskConsistencyGroupPolicyArgs]]:
        
        ...
    
    @disk_consistency_group_policy.setter
    def disk_consistency_group_policy(self, value: Optional[pulumi.Input[ResourcePolicyDiskConsistencyGroupPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupPlacementPolicy")
    def group_placement_policy(self) -> Optional[pulumi.Input[ResourcePolicyGroupPlacementPolicyArgs]]:
        
        ...
    
    @group_placement_policy.setter
    def group_placement_policy(self, value: Optional[pulumi.Input[ResourcePolicyGroupPlacementPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSchedulePolicy")
    def instance_schedule_policy(self) -> Optional[pulumi.Input[ResourcePolicyInstanceSchedulePolicyArgs]]:
        
        ...
    
    @instance_schedule_policy.setter
    def instance_schedule_policy(self, value: Optional[pulumi.Input[ResourcePolicyInstanceSchedulePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="snapshotSchedulePolicy")
    def snapshot_schedule_policy(self) -> Optional[pulumi.Input[ResourcePolicySnapshotSchedulePolicyArgs]]:
        
        ...
    
    @snapshot_schedule_policy.setter
    def snapshot_schedule_policy(self, value: Optional[pulumi.Input[ResourcePolicySnapshotSchedulePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadPolicy")
    def workload_policy(self) -> Optional[pulumi.Input[ResourcePolicyWorkloadPolicyArgs]]:
        
        ...
    
    @workload_policy.setter
    def workload_policy(self, value: Optional[pulumi.Input[ResourcePolicyWorkloadPolicyArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ResourcePolicyState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., disk_consistency_group_policy: Optional[pulumi.Input[ResourcePolicyDiskConsistencyGroupPolicyArgs]] = ..., group_placement_policy: Optional[pulumi.Input[ResourcePolicyGroupPlacementPolicyArgs]] = ..., instance_schedule_policy: Optional[pulumi.Input[ResourcePolicyInstanceSchedulePolicyArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_schedule_policy: Optional[pulumi.Input[ResourcePolicySnapshotSchedulePolicyArgs]] = ..., workload_policy: Optional[pulumi.Input[ResourcePolicyWorkloadPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConsistencyGroupPolicy")
    def disk_consistency_group_policy(self) -> Optional[pulumi.Input[ResourcePolicyDiskConsistencyGroupPolicyArgs]]:
        
        ...
    
    @disk_consistency_group_policy.setter
    def disk_consistency_group_policy(self, value: Optional[pulumi.Input[ResourcePolicyDiskConsistencyGroupPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupPlacementPolicy")
    def group_placement_policy(self) -> Optional[pulumi.Input[ResourcePolicyGroupPlacementPolicyArgs]]:
        
        ...
    
    @group_placement_policy.setter
    def group_placement_policy(self, value: Optional[pulumi.Input[ResourcePolicyGroupPlacementPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSchedulePolicy")
    def instance_schedule_policy(self) -> Optional[pulumi.Input[ResourcePolicyInstanceSchedulePolicyArgs]]:
        
        ...
    
    @instance_schedule_policy.setter
    def instance_schedule_policy(self, value: Optional[pulumi.Input[ResourcePolicyInstanceSchedulePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="snapshotSchedulePolicy")
    def snapshot_schedule_policy(self) -> Optional[pulumi.Input[ResourcePolicySnapshotSchedulePolicyArgs]]:
        
        ...
    
    @snapshot_schedule_policy.setter
    def snapshot_schedule_policy(self, value: Optional[pulumi.Input[ResourcePolicySnapshotSchedulePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadPolicy")
    def workload_policy(self) -> Optional[pulumi.Input[ResourcePolicyWorkloadPolicyArgs]]:
        
        ...
    
    @workload_policy.setter
    def workload_policy(self, value: Optional[pulumi.Input[ResourcePolicyWorkloadPolicyArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/resourcePolicy:ResourcePolicy")
class ResourcePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_consistency_group_policy: Optional[pulumi.Input[Union[ResourcePolicyDiskConsistencyGroupPolicyArgs, ResourcePolicyDiskConsistencyGroupPolicyArgsDict]]] = ..., group_placement_policy: Optional[pulumi.Input[Union[ResourcePolicyGroupPlacementPolicyArgs, ResourcePolicyGroupPlacementPolicyArgsDict]]] = ..., instance_schedule_policy: Optional[pulumi.Input[Union[ResourcePolicyInstanceSchedulePolicyArgs, ResourcePolicyInstanceSchedulePolicyArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_schedule_policy: Optional[pulumi.Input[Union[ResourcePolicySnapshotSchedulePolicyArgs, ResourcePolicySnapshotSchedulePolicyArgsDict]]] = ..., workload_policy: Optional[pulumi.Input[Union[ResourcePolicyWorkloadPolicyArgs, ResourcePolicyWorkloadPolicyArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ResourcePolicyArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_consistency_group_policy: Optional[pulumi.Input[Union[ResourcePolicyDiskConsistencyGroupPolicyArgs, ResourcePolicyDiskConsistencyGroupPolicyArgsDict]]] = ..., group_placement_policy: Optional[pulumi.Input[Union[ResourcePolicyGroupPlacementPolicyArgs, ResourcePolicyGroupPlacementPolicyArgsDict]]] = ..., instance_schedule_policy: Optional[pulumi.Input[Union[ResourcePolicyInstanceSchedulePolicyArgs, ResourcePolicyInstanceSchedulePolicyArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_schedule_policy: Optional[pulumi.Input[Union[ResourcePolicySnapshotSchedulePolicyArgs, ResourcePolicySnapshotSchedulePolicyArgsDict]]] = ..., workload_policy: Optional[pulumi.Input[Union[ResourcePolicyWorkloadPolicyArgs, ResourcePolicyWorkloadPolicyArgsDict]]] = ...) -> ResourcePolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConsistencyGroupPolicy")
    def disk_consistency_group_policy(self) -> pulumi.Output[Optional[outputs.ResourcePolicyDiskConsistencyGroupPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupPlacementPolicy")
    def group_placement_policy(self) -> pulumi.Output[Optional[outputs.ResourcePolicyGroupPlacementPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSchedulePolicy")
    def instance_schedule_policy(self) -> pulumi.Output[Optional[outputs.ResourcePolicyInstanceSchedulePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="snapshotSchedulePolicy")
    def snapshot_schedule_policy(self) -> pulumi.Output[Optional[outputs.ResourcePolicySnapshotSchedulePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadPolicy")
    def workload_policy(self) -> pulumi.Output[Optional[outputs.ResourcePolicyWorkloadPolicy]]:
        
        ...
    


