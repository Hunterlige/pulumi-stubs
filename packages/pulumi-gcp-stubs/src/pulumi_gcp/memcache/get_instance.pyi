import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceResult",
    "AwaitableGetInstanceResult",
    "get_instance",
    "get_instance_output",
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(
        __self__,
        authorized_network=...,
        create_time=...,
        deletion_protection=...,
        discovery_endpoint=...,
        display_name=...,
        effective_labels=...,
        id=...,
        labels=...,
        maintenance_policies=...,
        maintenance_schedules=...,
        memcache_full_version=...,
        memcache_nodes=...,
        memcache_parameters=...,
        memcache_version=...,
        name=...,
        node_configs=...,
        node_count=...,
        project=...,
        pulumi_labels=...,
        region=...,
        reserved_ip_range_ids=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="discoveryEndpoint")
    def discovery_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenancePolicies")
    def maintenance_policies(
        self,
    ) -> Sequence[outputs.GetInstanceMaintenancePolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(
        self,
    ) -> Sequence[outputs.GetInstanceMaintenanceScheduleResult]: ...
    @_builtins.property
    @pulumi.getter(name="memcacheFullVersion")
    def memcache_full_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memcacheNodes")
    def memcache_nodes(self) -> Sequence[outputs.GetInstanceMemcacheNodeResult]: ...
    @_builtins.property
    @pulumi.getter(name="memcacheParameters")
    def memcache_parameters(
        self,
    ) -> Sequence[outputs.GetInstanceMemcacheParameterResult]: ...
    @_builtins.property
    @pulumi.getter(name="memcacheVersion")
    def memcache_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Sequence[outputs.GetInstanceNodeConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reservedIpRangeIds")
    def reserved_ip_range_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Sequence[_builtins.str]: ...

class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): ...

def get_instance(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceResult: ...
def get_instance_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceResult]: ...
