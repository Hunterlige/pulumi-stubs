

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResourcePolicyResult', 'AwaitableGetResourcePolicyResult', 'get_resource_policy', 'get_resource_policy_output']
@pulumi.output_type
class GetResourcePolicyResult:
    
    def __init__(__self__, description=..., disk_consistency_group_policies=..., group_placement_policies=..., id=..., instance_schedule_policies=..., name=..., project=..., region=..., self_link=..., snapshot_schedule_policies=..., workload_policies=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConsistencyGroupPolicies")
    def disk_consistency_group_policies(self) -> Sequence[outputs.GetResourcePolicyDiskConsistencyGroupPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupPlacementPolicies")
    def group_placement_policies(self) -> Sequence[outputs.GetResourcePolicyGroupPlacementPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSchedulePolicies")
    def instance_schedule_policies(self) -> Sequence[outputs.GetResourcePolicyInstanceSchedulePolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotSchedulePolicies")
    def snapshot_schedule_policies(self) -> Sequence[outputs.GetResourcePolicySnapshotSchedulePolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadPolicies")
    def workload_policies(self) -> Sequence[outputs.GetResourcePolicyWorkloadPolicyResult]:
        ...
    


class AwaitableGetResourcePolicyResult(GetResourcePolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetResourcePolicyResult]:
        ...
    


def get_resource_policy(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResourcePolicyResult:
    
    ...

def get_resource_policy_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResourcePolicyResult]:
    
    ...

