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
        activation_policy=...,
        annotations=...,
        availability_type=...,
        client_connection_configs=...,
        cluster=...,
        cluster_id=...,
        connection_pool_configs=...,
        create_time=...,
        database_flags=...,
        display_name=...,
        effective_annotations=...,
        effective_labels=...,
        gce_zone=...,
        id=...,
        instance_id=...,
        instance_type=...,
        ip_address=...,
        labels=...,
        location=...,
        machine_configs=...,
        name=...,
        network_configs=...,
        observability_configs=...,
        outbound_public_ip_addresses=...,
        project=...,
        psc_instance_configs=...,
        public_ip_address=...,
        pulumi_labels=...,
        query_insights_configs=...,
        read_pool_configs=...,
        reconciling=...,
        state=...,
        uid=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activationPolicy")
    def activation_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientConnectionConfigs")
    def client_connection_configs(
        self,
    ) -> Sequence[outputs.GetInstanceClientConnectionConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfigs")
    def connection_pool_configs(
        self,
    ) -> Sequence[outputs.GetInstanceConnectionPoolConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gceZone")
    def gce_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineConfigs")
    def machine_configs(self) -> Sequence[outputs.GetInstanceMachineConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(self) -> Sequence[outputs.GetInstanceNetworkConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="observabilityConfigs")
    def observability_configs(
        self,
    ) -> Sequence[outputs.GetInstanceObservabilityConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="outboundPublicIpAddresses")
    def outbound_public_ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscInstanceConfigs")
    def psc_instance_configs(
        self,
    ) -> Sequence[outputs.GetInstancePscInstanceConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryInsightsConfigs")
    def query_insights_configs(
        self,
    ) -> Sequence[outputs.GetInstanceQueryInsightsConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="readPoolConfigs")
    def read_pool_configs(
        self,
    ) -> Sequence[outputs.GetInstanceReadPoolConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): ...

def get_instance(
    cluster_id: Optional[_builtins.str] = ...,
    instance_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceResult: ...
def get_instance_output(
    cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
    instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceResult]: ...
