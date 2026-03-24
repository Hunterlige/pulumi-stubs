import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LoadBalancerArgs", "LoadBalancer"]

@pulumi.input_type
class LoadBalancerArgs:
    def __init__(
        __self__,
        *,
        access_logs: Optional[pulumi.Input[LoadBalancerAccessLogsArgs]] = ...,
        client_keep_alive: Optional[pulumi.Input[_builtins.int]] = ...,
        connection_logs: Optional[pulumi.Input[LoadBalancerConnectionLogsArgs]] = ...,
        customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        desync_mitigation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_record_client_routing_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        drop_invalid_header_fields: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_cross_zone_load_balancing: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http2: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_tls_version_and_cipher_suite_headers: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_waf_fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_xff_client_port: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_zonal_shift: Optional[pulumi.Input[_builtins.bool]] = ...,
        enforce_security_group_inbound_rules_on_private_link_traffic: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        health_check_logs: Optional[
            pulumi.Input[LoadBalancerHealthCheckLogsArgs]
        ] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        internal: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_address_type: Optional[
            pulumi.Input[Union[_builtins.str, IpAddressType]]
        ] = ...,
        ipam_pools: Optional[pulumi.Input[LoadBalancerIpamPoolsArgs]] = ...,
        load_balancer_type: Optional[pulumi.Input[LoadBalancerType]] = ...,
        minimum_load_balancer_capacity: Optional[
            pulumi.Input[LoadBalancerMinimumLoadBalancerCapacityArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        preserve_host_header: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_ips_auto_assigned_per_subnet: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_mappings: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoadBalancerSubnetMappingArgs]]]
        ] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        xff_header_processing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> Optional[pulumi.Input[LoadBalancerAccessLogsArgs]]: ...
    @access_logs.setter
    def access_logs(
        self, value: Optional[pulumi.Input[LoadBalancerAccessLogsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientKeepAlive")
    def client_keep_alive(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @client_keep_alive.setter
    def client_keep_alive(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionLogs")
    def connection_logs(
        self,
    ) -> Optional[pulumi.Input[LoadBalancerConnectionLogsArgs]]: ...
    @connection_logs.setter
    def connection_logs(
        self, value: Optional[pulumi.Input[LoadBalancerConnectionLogsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="desyncMitigationMode")
    def desync_mitigation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desync_mitigation_mode.setter
    def desync_mitigation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsRecordClientRoutingPolicy")
    def dns_record_client_routing_policy(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_record_client_routing_policy.setter
    def dns_record_client_routing_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dropInvalidHeaderFields")
    def drop_invalid_header_fields(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @drop_invalid_header_fields.setter
    def drop_invalid_header_fields(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableCrossZoneLoadBalancing")
    def enable_cross_zone_load_balancing(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cross_zone_load_balancing.setter
    def enable_cross_zone_load_balancing(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDeletionProtection")
    def enable_deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_deletion_protection.setter
    def enable_deletion_protection(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_http2.setter
    def enable_http2(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableTlsVersionAndCipherSuiteHeaders")
    def enable_tls_version_and_cipher_suite_headers(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_tls_version_and_cipher_suite_headers.setter
    def enable_tls_version_and_cipher_suite_headers(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableWafFailOpen")
    def enable_waf_fail_open(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_waf_fail_open.setter
    def enable_waf_fail_open(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableXffClientPort")
    def enable_xff_client_port(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_xff_client_port.setter
    def enable_xff_client_port(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableZonalShift")
    def enable_zonal_shift(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_zonal_shift.setter
    def enable_zonal_shift(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def enforce_security_group_inbound_rules_on_private_link_traffic(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enforce_security_group_inbound_rules_on_private_link_traffic.setter
    def enforce_security_group_inbound_rules_on_private_link_traffic(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckLogs")
    def health_check_logs(
        self,
    ) -> Optional[pulumi.Input[LoadBalancerHealthCheckLogsArgs]]: ...
    @health_check_logs.setter
    def health_check_logs(
        self, value: Optional[pulumi.Input[LoadBalancerHealthCheckLogsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def internal(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @internal.setter
    def internal(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IpAddressType]]]: ...
    @ip_address_type.setter
    def ip_address_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IpAddressType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipamPools")
    def ipam_pools(self) -> Optional[pulumi.Input[LoadBalancerIpamPoolsArgs]]: ...
    @ipam_pools.setter
    def ipam_pools(self, value: Optional[pulumi.Input[LoadBalancerIpamPoolsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[pulumi.Input[LoadBalancerType]]: ...
    @load_balancer_type.setter
    def load_balancer_type(self, value: Optional[pulumi.Input[LoadBalancerType]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumLoadBalancerCapacity")
    def minimum_load_balancer_capacity(
        self,
    ) -> Optional[pulumi.Input[LoadBalancerMinimumLoadBalancerCapacityArgs]]: ...
    @minimum_load_balancer_capacity.setter
    def minimum_load_balancer_capacity(
        self, value: Optional[pulumi.Input[LoadBalancerMinimumLoadBalancerCapacityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preserveHostHeader")
    def preserve_host_header(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preserve_host_header.setter
    def preserve_host_header(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryIpsAutoAssignedPerSubnet")
    def secondary_ips_auto_assigned_per_subnet(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @secondary_ips_auto_assigned_per_subnet.setter
    def secondary_ips_auto_assigned_per_subnet(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LoadBalancerSubnetMappingArgs]]]
    ]: ...
    @subnet_mappings.setter
    def subnet_mappings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoadBalancerSubnetMappingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnets.setter
    def subnets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="xffHeaderProcessingMode")
    def xff_header_processing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @xff_header_processing_mode.setter
    def xff_header_processing_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _LoadBalancerState:
    def __init__(
        __self__,
        *,
        access_logs: Optional[pulumi.Input[LoadBalancerAccessLogsArgs]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        client_keep_alive: Optional[pulumi.Input[_builtins.int]] = ...,
        connection_logs: Optional[pulumi.Input[LoadBalancerConnectionLogsArgs]] = ...,
        customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        desync_mitigation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_record_client_routing_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        drop_invalid_header_fields: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_cross_zone_load_balancing: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http2: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_tls_version_and_cipher_suite_headers: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_waf_fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_xff_client_port: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_zonal_shift: Optional[pulumi.Input[_builtins.bool]] = ...,
        enforce_security_group_inbound_rules_on_private_link_traffic: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        health_check_logs: Optional[
            pulumi.Input[LoadBalancerHealthCheckLogsArgs]
        ] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        internal: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_address_type: Optional[
            pulumi.Input[Union[_builtins.str, IpAddressType]]
        ] = ...,
        ipam_pools: Optional[pulumi.Input[LoadBalancerIpamPoolsArgs]] = ...,
        load_balancer_type: Optional[pulumi.Input[LoadBalancerType]] = ...,
        minimum_load_balancer_capacity: Optional[
            pulumi.Input[LoadBalancerMinimumLoadBalancerCapacityArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        preserve_host_header: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_ips_auto_assigned_per_subnet: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_mappings: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoadBalancerSubnetMappingArgs]]]
        ] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        xff_header_processing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> Optional[pulumi.Input[LoadBalancerAccessLogsArgs]]: ...
    @access_logs.setter
    def access_logs(
        self, value: Optional[pulumi.Input[LoadBalancerAccessLogsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="arnSuffix")
    def arn_suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn_suffix.setter
    def arn_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientKeepAlive")
    def client_keep_alive(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @client_keep_alive.setter
    def client_keep_alive(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionLogs")
    def connection_logs(
        self,
    ) -> Optional[pulumi.Input[LoadBalancerConnectionLogsArgs]]: ...
    @connection_logs.setter
    def connection_logs(
        self, value: Optional[pulumi.Input[LoadBalancerConnectionLogsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="desyncMitigationMode")
    def desync_mitigation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desync_mitigation_mode.setter
    def desync_mitigation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsRecordClientRoutingPolicy")
    def dns_record_client_routing_policy(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_record_client_routing_policy.setter
    def dns_record_client_routing_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dropInvalidHeaderFields")
    def drop_invalid_header_fields(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @drop_invalid_header_fields.setter
    def drop_invalid_header_fields(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableCrossZoneLoadBalancing")
    def enable_cross_zone_load_balancing(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cross_zone_load_balancing.setter
    def enable_cross_zone_load_balancing(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDeletionProtection")
    def enable_deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_deletion_protection.setter
    def enable_deletion_protection(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_http2.setter
    def enable_http2(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableTlsVersionAndCipherSuiteHeaders")
    def enable_tls_version_and_cipher_suite_headers(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_tls_version_and_cipher_suite_headers.setter
    def enable_tls_version_and_cipher_suite_headers(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableWafFailOpen")
    def enable_waf_fail_open(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_waf_fail_open.setter
    def enable_waf_fail_open(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableXffClientPort")
    def enable_xff_client_port(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_xff_client_port.setter
    def enable_xff_client_port(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableZonalShift")
    def enable_zonal_shift(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_zonal_shift.setter
    def enable_zonal_shift(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def enforce_security_group_inbound_rules_on_private_link_traffic(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enforce_security_group_inbound_rules_on_private_link_traffic.setter
    def enforce_security_group_inbound_rules_on_private_link_traffic(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckLogs")
    def health_check_logs(
        self,
    ) -> Optional[pulumi.Input[LoadBalancerHealthCheckLogsArgs]]: ...
    @health_check_logs.setter
    def health_check_logs(
        self, value: Optional[pulumi.Input[LoadBalancerHealthCheckLogsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def internal(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @internal.setter
    def internal(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IpAddressType]]]: ...
    @ip_address_type.setter
    def ip_address_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IpAddressType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipamPools")
    def ipam_pools(self) -> Optional[pulumi.Input[LoadBalancerIpamPoolsArgs]]: ...
    @ipam_pools.setter
    def ipam_pools(self, value: Optional[pulumi.Input[LoadBalancerIpamPoolsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[pulumi.Input[LoadBalancerType]]: ...
    @load_balancer_type.setter
    def load_balancer_type(self, value: Optional[pulumi.Input[LoadBalancerType]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumLoadBalancerCapacity")
    def minimum_load_balancer_capacity(
        self,
    ) -> Optional[pulumi.Input[LoadBalancerMinimumLoadBalancerCapacityArgs]]: ...
    @minimum_load_balancer_capacity.setter
    def minimum_load_balancer_capacity(
        self, value: Optional[pulumi.Input[LoadBalancerMinimumLoadBalancerCapacityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preserveHostHeader")
    def preserve_host_header(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preserve_host_header.setter
    def preserve_host_header(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryIpsAutoAssignedPerSubnet")
    def secondary_ips_auto_assigned_per_subnet(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @secondary_ips_auto_assigned_per_subnet.setter
    def secondary_ips_auto_assigned_per_subnet(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LoadBalancerSubnetMappingArgs]]]
    ]: ...
    @subnet_mappings.setter
    def subnet_mappings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoadBalancerSubnetMappingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnets.setter
    def subnets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="xffHeaderProcessingMode")
    def xff_header_processing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @xff_header_processing_mode.setter
    def xff_header_processing_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:alb/loadBalancer:LoadBalancer")
class LoadBalancer(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_logs: Optional[
            pulumi.Input[
                Union[LoadBalancerAccessLogsArgs, LoadBalancerAccessLogsArgsDict]
            ]
        ] = ...,
        client_keep_alive: Optional[pulumi.Input[_builtins.int]] = ...,
        connection_logs: Optional[
            pulumi.Input[
                Union[
                    LoadBalancerConnectionLogsArgs, LoadBalancerConnectionLogsArgsDict
                ]
            ]
        ] = ...,
        customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        desync_mitigation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_record_client_routing_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        drop_invalid_header_fields: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_cross_zone_load_balancing: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http2: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_tls_version_and_cipher_suite_headers: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_waf_fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_xff_client_port: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_zonal_shift: Optional[pulumi.Input[_builtins.bool]] = ...,
        enforce_security_group_inbound_rules_on_private_link_traffic: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        health_check_logs: Optional[
            pulumi.Input[
                Union[
                    LoadBalancerHealthCheckLogsArgs, LoadBalancerHealthCheckLogsArgsDict
                ]
            ]
        ] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        internal: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_address_type: Optional[
            pulumi.Input[Union[_builtins.str, IpAddressType]]
        ] = ...,
        ipam_pools: Optional[
            pulumi.Input[
                Union[LoadBalancerIpamPoolsArgs, LoadBalancerIpamPoolsArgsDict]
            ]
        ] = ...,
        load_balancer_type: Optional[pulumi.Input[LoadBalancerType]] = ...,
        minimum_load_balancer_capacity: Optional[
            pulumi.Input[
                Union[
                    LoadBalancerMinimumLoadBalancerCapacityArgs,
                    LoadBalancerMinimumLoadBalancerCapacityArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        preserve_host_header: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_ips_auto_assigned_per_subnet: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LoadBalancerSubnetMappingArgs,
                            LoadBalancerSubnetMappingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        xff_header_processing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[LoadBalancerArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_logs: Optional[
            pulumi.Input[
                Union[LoadBalancerAccessLogsArgs, LoadBalancerAccessLogsArgsDict]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        client_keep_alive: Optional[pulumi.Input[_builtins.int]] = ...,
        connection_logs: Optional[
            pulumi.Input[
                Union[
                    LoadBalancerConnectionLogsArgs, LoadBalancerConnectionLogsArgsDict
                ]
            ]
        ] = ...,
        customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        desync_mitigation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_record_client_routing_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        drop_invalid_header_fields: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_cross_zone_load_balancing: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http2: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_tls_version_and_cipher_suite_headers: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_waf_fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_xff_client_port: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_zonal_shift: Optional[pulumi.Input[_builtins.bool]] = ...,
        enforce_security_group_inbound_rules_on_private_link_traffic: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        health_check_logs: Optional[
            pulumi.Input[
                Union[
                    LoadBalancerHealthCheckLogsArgs, LoadBalancerHealthCheckLogsArgsDict
                ]
            ]
        ] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        internal: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_address_type: Optional[
            pulumi.Input[Union[_builtins.str, IpAddressType]]
        ] = ...,
        ipam_pools: Optional[
            pulumi.Input[
                Union[LoadBalancerIpamPoolsArgs, LoadBalancerIpamPoolsArgsDict]
            ]
        ] = ...,
        load_balancer_type: Optional[pulumi.Input[LoadBalancerType]] = ...,
        minimum_load_balancer_capacity: Optional[
            pulumi.Input[
                Union[
                    LoadBalancerMinimumLoadBalancerCapacityArgs,
                    LoadBalancerMinimumLoadBalancerCapacityArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        preserve_host_header: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_ips_auto_assigned_per_subnet: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LoadBalancerSubnetMappingArgs,
                            LoadBalancerSubnetMappingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        xff_header_processing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LoadBalancer: ...
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(
        self,
    ) -> pulumi.Output[Optional[outputs.LoadBalancerAccessLogs]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="arnSuffix")
    def arn_suffix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientKeepAlive")
    def client_keep_alive(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionLogs")
    def connection_logs(
        self,
    ) -> pulumi.Output[Optional[outputs.LoadBalancerConnectionLogs]]: ...
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="desyncMitigationMode")
    def desync_mitigation_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsRecordClientRoutingPolicy")
    def dns_record_client_routing_policy(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dropInvalidHeaderFields")
    def drop_invalid_header_fields(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableCrossZoneLoadBalancing")
    def enable_cross_zone_load_balancing(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableDeletionProtection")
    def enable_deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableTlsVersionAndCipherSuiteHeaders")
    def enable_tls_version_and_cipher_suite_headers(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableWafFailOpen")
    def enable_waf_fail_open(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableXffClientPort")
    def enable_xff_client_port(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableZonalShift")
    def enable_zonal_shift(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def enforce_security_group_inbound_rules_on_private_link_traffic(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckLogs")
    def health_check_logs(
        self,
    ) -> pulumi.Output[Optional[outputs.LoadBalancerHealthCheckLogs]]: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def internal(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipamPools")
    def ipam_pools(self) -> pulumi.Output[Optional[outputs.LoadBalancerIpamPools]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> pulumi.Output[Optional[LoadBalancerType]]: ...
    @_builtins.property
    @pulumi.getter(name="minimumLoadBalancerCapacity")
    def minimum_load_balancer_capacity(
        self,
    ) -> pulumi.Output[Optional[outputs.LoadBalancerMinimumLoadBalancerCapacity]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preserveHostHeader")
    def preserve_host_header(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryIpsAutoAssignedPerSubnet")
    def secondary_ips_auto_assigned_per_subnet(
        self,
    ) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(
        self,
    ) -> pulumi.Output[Sequence[outputs.LoadBalancerSubnetMapping]]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="xffHeaderProcessingMode")
    def xff_header_processing_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[_builtins.str]: ...
