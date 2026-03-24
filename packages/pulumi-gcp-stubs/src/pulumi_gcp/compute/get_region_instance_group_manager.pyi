import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionInstanceGroupManagerResult",
    "AwaitableGetRegionInstanceGroupManagerResult",
    "get_region_instance_group_manager",
    "get_region_instance_group_manager_output",
]

@pulumi.output_type
class GetRegionInstanceGroupManagerResult:
    def __init__(
        __self__,
        all_instances_configs=...,
        auto_healing_policies=...,
        base_instance_name=...,
        creation_timestamp=...,
        description=...,
        distribution_policy_target_shape=...,
        distribution_policy_zones=...,
        fingerprint=...,
        id=...,
        instance_flexibility_policies=...,
        instance_group=...,
        instance_group_manager_id=...,
        instance_lifecycle_policies=...,
        list_managed_instances_results=...,
        name=...,
        named_ports=...,
        params=...,
        project=...,
        region=...,
        self_link=...,
        standby_policies=...,
        stateful_disks=...,
        stateful_external_ips=...,
        stateful_internal_ips=...,
        statuses=...,
        target_pools=...,
        target_size=...,
        target_stopped_size=...,
        target_suspended_size=...,
        update_policies=...,
        versions=...,
        wait_for_instances=...,
        wait_for_instances_status=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allInstancesConfigs")
    def all_instances_configs(
        self,
    ) -> Sequence[outputs.GetRegionInstanceGroupManagerAllInstancesConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="autoHealingPolicies")
    def auto_healing_policies(
        self,
    ) -> Sequence[outputs.GetRegionInstanceGroupManagerAutoHealingPolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="baseInstanceName")
    def base_instance_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="distributionPolicyTargetShape")
    def distribution_policy_target_shape(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="distributionPolicyZones")
    def distribution_policy_zones(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceFlexibilityPolicies")
    def instance_flexibility_policies(
        self,
    ) -> Sequence[
        outputs.GetRegionInstanceGroupManagerInstanceFlexibilityPolicyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="instanceGroup")
    def instance_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerId")
    def instance_group_manager_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="instanceLifecyclePolicies")
    def instance_lifecycle_policies(
        self,
    ) -> Sequence[
        outputs.GetRegionInstanceGroupManagerInstanceLifecyclePolicyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="listManagedInstancesResults")
    def list_managed_instances_results(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namedPorts")
    def named_ports(
        self,
    ) -> Sequence[outputs.GetRegionInstanceGroupManagerNamedPortResult]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Sequence[outputs.GetRegionInstanceGroupManagerParamResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="standbyPolicies")
    def standby_policies(
        self,
    ) -> Sequence[outputs.GetRegionInstanceGroupManagerStandbyPolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="statefulDisks")
    def stateful_disks(
        self,
    ) -> Sequence[outputs.GetRegionInstanceGroupManagerStatefulDiskResult]: ...
    @_builtins.property
    @pulumi.getter(name="statefulExternalIps")
    def stateful_external_ips(
        self,
    ) -> Sequence[outputs.GetRegionInstanceGroupManagerStatefulExternalIpResult]: ...
    @_builtins.property
    @pulumi.getter(name="statefulInternalIps")
    def stateful_internal_ips(
        self,
    ) -> Sequence[outputs.GetRegionInstanceGroupManagerStatefulInternalIpResult]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Sequence[outputs.GetRegionInstanceGroupManagerStatusResult]: ...
    @_builtins.property
    @pulumi.getter(name="targetPools")
    def target_pools(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetSize")
    def target_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="targetStoppedSize")
    def target_stopped_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="targetSuspendedSize")
    def target_suspended_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="updatePolicies")
    def update_policies(
        self,
    ) -> Sequence[outputs.GetRegionInstanceGroupManagerUpdatePolicyResult]: ...
    @_builtins.property
    @pulumi.getter
    def versions(
        self,
    ) -> Sequence[outputs.GetRegionInstanceGroupManagerVersionResult]: ...
    @_builtins.property
    @pulumi.getter(name="waitForInstances")
    def wait_for_instances(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="waitForInstancesStatus")
    def wait_for_instances_status(self) -> _builtins.str: ...

class AwaitableGetRegionInstanceGroupManagerResult(GetRegionInstanceGroupManagerResult):
    def __await__(self): ...

def get_region_instance_group_manager(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    self_link: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionInstanceGroupManagerResult: ...
def get_region_instance_group_manager_output(
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    self_link: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionInstanceGroupManagerResult]: ...
