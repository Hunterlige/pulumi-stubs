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
        arn_suffix=...,
        client_keep_alive=...,
        connection_logs=...,
        customer_owned_ipv4_pool=...,
        desync_mitigation_mode=...,
        dns_name=...,
        dns_record_client_routing_policy=...,
        drop_invalid_header_fields=...,
        enable_cross_zone_load_balancing=...,
        enable_deletion_protection=...,
        enable_http2=...,
        enable_tls_version_and_cipher_suite_headers=...,
        enable_waf_fail_open=...,
        enable_xff_client_port=...,
        enable_zonal_shift=...,
        enforce_security_group_inbound_rules_on_private_link_traffic=...,
        health_check_logs=...,
        id=...,
        idle_timeout=...,
        internal=...,
        ip_address_type=...,
        ipam_pools=...,
        load_balancer_type=...,
        name=...,
        preserve_host_header=...,
        region=...,
        secondary_ips_auto_assigned_per_subnet=...,
        security_groups=...,
        subnet_mappings=...,
        subnets=...,
        tags=...,
        vpc_id=...,
        xff_header_processing_mode=...,
        zone_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> outputs.GetLoadBalancerAccessLogsResult: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="arnSuffix")
    def arn_suffix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientKeepAlive")
    def client_keep_alive(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="connectionLogs")
    def connection_logs(
        self,
    ) -> Sequence[outputs.GetLoadBalancerConnectionLogResult]: ...
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="desyncMitigationMode")
    def desync_mitigation_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsRecordClientRoutingPolicy")
    def dns_record_client_routing_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dropInvalidHeaderFields")
    def drop_invalid_header_fields(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableCrossZoneLoadBalancing")
    def enable_cross_zone_load_balancing(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableDeletionProtection")
    def enable_deletion_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableTlsVersionAndCipherSuiteHeaders")
    def enable_tls_version_and_cipher_suite_headers(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableWafFailOpen")
    def enable_waf_fail_open(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableXffClientPort")
    def enable_xff_client_port(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableZonalShift")
    def enable_zonal_shift(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def enforce_security_group_inbound_rules_on_private_link_traffic(
        self,
    ) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckLogs")
    def health_check_logs(
        self,
    ) -> Sequence[outputs.GetLoadBalancerHealthCheckLogResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def internal(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipamPools")
    def ipam_pools(self) -> Sequence[outputs.GetLoadBalancerIpamPoolResult]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preserveHostHeader")
    def preserve_host_header(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryIpsAutoAssignedPerSubnet")
    def secondary_ips_auto_assigned_per_subnet(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(
        self,
    ) -> Sequence[outputs.GetLoadBalancerSubnetMappingResult]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="xffHeaderProcessingMode")
    def xff_header_processing_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> _builtins.str: ...

class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    def __await__(self): ...

def get_load_balancer(
    arn: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLoadBalancerResult: ...
def get_load_balancer_output(
    arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLoadBalancerResult]: ...
