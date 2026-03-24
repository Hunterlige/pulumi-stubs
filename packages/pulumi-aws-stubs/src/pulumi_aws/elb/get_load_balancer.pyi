import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLoadBalancerResult",
    "AwaitableGetLoadBalancerResult",
    "get_load_balancer",
    "get_load_balancer_output",
]

@pulumi.output_type
class GetLoadBalancerResult:
    def __init__(
        __self__,
        access_logs=...,
        arn=...,
        availability_zones=...,
        connection_draining=...,
        connection_draining_timeout=...,
        cross_zone_load_balancing=...,
        desync_mitigation_mode=...,
        dns_name=...,
        health_check=...,
        id=...,
        idle_timeout=...,
        instances=...,
        internal=...,
        listeners=...,
        name=...,
        region=...,
        security_groups=...,
        source_security_group=...,
        source_security_group_id=...,
        subnets=...,
        tags=...,
        zone_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> outputs.GetLoadBalancerAccessLogsResult: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionDraining")
    def connection_draining(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="connectionDrainingTimeout")
    def connection_draining_timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="crossZoneLoadBalancing")
    def cross_zone_load_balancing(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="desyncMitigationMode")
    def desync_mitigation_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> outputs.GetLoadBalancerHealthCheckResult: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def internal(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> Sequence[outputs.GetLoadBalancerListenerResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroup")
    def source_security_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> _builtins.str: ...

class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    def __await__(self): ...

def get_load_balancer(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLoadBalancerResult: ...
def get_load_balancer_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLoadBalancerResult]: ...
