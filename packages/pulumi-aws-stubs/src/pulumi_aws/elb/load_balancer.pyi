import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LoadBalancerArgs", "LoadBalancer"]

@pulumi.input_type
class LoadBalancerArgs:
    def __init__(
        __self__,
        *,
        listeners: pulumi.Input[Sequence[pulumi.Input[LoadBalancerListenerArgs]]],
        access_logs: Optional[pulumi.Input[LoadBalancerAccessLogsArgs]] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        connection_draining: Optional[pulumi.Input[_builtins.bool]] = ...,
        connection_draining_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        cross_zone_load_balancing: Optional[pulumi.Input[_builtins.bool]] = ...,
        desync_mitigation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check: Optional[pulumi.Input[LoadBalancerHealthCheckArgs]] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        internal: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        source_security_group: Optional[pulumi.Input[_builtins.str]] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def listeners(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[LoadBalancerListenerArgs]]]: ...
    @listeners.setter
    def listeners(
        self, value: pulumi.Input[Sequence[pulumi.Input[LoadBalancerListenerArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> Optional[pulumi.Input[LoadBalancerAccessLogsArgs]]: ...
    @access_logs.setter
    def access_logs(
        self, value: Optional[pulumi.Input[LoadBalancerAccessLogsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionDraining")
    def connection_draining(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @connection_draining.setter
    def connection_draining(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionDrainingTimeout")
    def connection_draining_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_draining_timeout.setter
    def connection_draining_timeout(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crossZoneLoadBalancing")
    def cross_zone_load_balancing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cross_zone_load_balancing.setter
    def cross_zone_load_balancing(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="desyncMitigationMode")
    def desync_mitigation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desync_mitigation_mode.setter
    def desync_mitigation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input[LoadBalancerHealthCheckArgs]]: ...
    @health_check.setter
    def health_check(
        self, value: Optional[pulumi.Input[LoadBalancerHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instances.setter
    def instances(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def internal(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @internal.setter
    def internal(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="sourceSecurityGroup")
    def source_security_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_security_group.setter
    def source_security_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.input_type
class _LoadBalancerState:
    def __init__(
        __self__,
        *,
        access_logs: Optional[pulumi.Input[LoadBalancerAccessLogsArgs]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        connection_draining: Optional[pulumi.Input[_builtins.bool]] = ...,
        connection_draining_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        cross_zone_load_balancing: Optional[pulumi.Input[_builtins.bool]] = ...,
        desync_mitigation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check: Optional[pulumi.Input[LoadBalancerHealthCheckArgs]] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        internal: Optional[pulumi.Input[_builtins.bool]] = ...,
        listeners: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoadBalancerListenerArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        source_security_group: Optional[pulumi.Input[_builtins.str]] = ...,
        source_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
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
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionDraining")
    def connection_draining(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @connection_draining.setter
    def connection_draining(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionDrainingTimeout")
    def connection_draining_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_draining_timeout.setter
    def connection_draining_timeout(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crossZoneLoadBalancing")
    def cross_zone_load_balancing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cross_zone_load_balancing.setter
    def cross_zone_load_balancing(
        self, value: Optional[pulumi.Input[_builtins.bool]]
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
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input[LoadBalancerHealthCheckArgs]]: ...
    @health_check.setter
    def health_check(
        self, value: Optional[pulumi.Input[LoadBalancerHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instances.setter
    def instances(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def internal(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @internal.setter
    def internal(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def listeners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerListenerArgs]]]]: ...
    @listeners.setter
    def listeners(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerListenerArgs]]]],
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="sourceSecurityGroup")
    def source_security_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_security_group.setter
    def source_security_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_security_group_id.setter
    def source_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:elb/loadBalancer:LoadBalancer")
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
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        connection_draining: Optional[pulumi.Input[_builtins.bool]] = ...,
        connection_draining_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        cross_zone_load_balancing: Optional[pulumi.Input[_builtins.bool]] = ...,
        desync_mitigation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check: Optional[
            pulumi.Input[
                Union[LoadBalancerHealthCheckArgs, LoadBalancerHealthCheckArgsDict]
            ]
        ] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        internal: Optional[pulumi.Input[_builtins.bool]] = ...,
        listeners: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[LoadBalancerListenerArgs, LoadBalancerListenerArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        source_security_group: Optional[pulumi.Input[_builtins.str]] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LoadBalancerArgs,
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
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        connection_draining: Optional[pulumi.Input[_builtins.bool]] = ...,
        connection_draining_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        cross_zone_load_balancing: Optional[pulumi.Input[_builtins.bool]] = ...,
        desync_mitigation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check: Optional[
            pulumi.Input[
                Union[LoadBalancerHealthCheckArgs, LoadBalancerHealthCheckArgsDict]
            ]
        ] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        internal: Optional[pulumi.Input[_builtins.bool]] = ...,
        listeners: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[LoadBalancerListenerArgs, LoadBalancerListenerArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        source_security_group: Optional[pulumi.Input[_builtins.str]] = ...,
        source_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
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
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionDraining")
    def connection_draining(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionDrainingTimeout")
    def connection_draining_timeout(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="crossZoneLoadBalancing")
    def cross_zone_load_balancing(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="desyncMitigationMode")
    def desync_mitigation_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Output[outputs.LoadBalancerHealthCheck]: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def internal(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> pulumi.Output[Sequence[outputs.LoadBalancerListener]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroup")
    def source_security_group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[_builtins.str]: ...
