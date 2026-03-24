import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TargetGroupArgs", "TargetGroup"]

@pulumi.input_type
class TargetGroupArgs:
    def __init__(
        __self__,
        *,
        connection_termination: Optional[pulumi.Input[_builtins.bool]] = ...,
        deregistration_delay: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check: Optional[pulumi.Input[TargetGroupHealthCheckArgs]] = ...,
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_multi_value_headers_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        load_balancing_algorithm_type: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_anomaly_mitigation: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_cross_zone_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preserve_client_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_version: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_protocol_v2: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        slow_start: Optional[pulumi.Input[_builtins.int]] = ...,
        stickiness: Optional[pulumi.Input[TargetGroupStickinessArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_control_port: Optional[pulumi.Input[_builtins.int]] = ...,
        target_failovers: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetFailoverArgs]]]
        ] = ...,
        target_group_health: Optional[
            pulumi.Input[TargetGroupTargetGroupHealthArgs]
        ] = ...,
        target_health_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetHealthStateArgs]]]
        ] = ...,
        target_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionTermination")
    def connection_termination(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @connection_termination.setter
    def connection_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="deregistrationDelay")
    def deregistration_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @deregistration_delay.setter
    def deregistration_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input[TargetGroupHealthCheckArgs]]: ...
    @health_check.setter
    def health_check(
        self, value: Optional[pulumi.Input[TargetGroupHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaMultiValueHeadersEnabled")
    def lambda_multi_value_headers_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @lambda_multi_value_headers_enabled.setter
    def lambda_multi_value_headers_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingAlgorithmType")
    def load_balancing_algorithm_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_algorithm_type.setter
    def load_balancing_algorithm_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingAnomalyMitigation")
    def load_balancing_anomaly_mitigation(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_anomaly_mitigation.setter
    def load_balancing_anomaly_mitigation(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingCrossZoneEnabled")
    def load_balancing_cross_zone_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_cross_zone_enabled.setter
    def load_balancing_cross_zone_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="preserveClientIp")
    def preserve_client_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preserve_client_ip.setter
    def preserve_client_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol_version.setter
    def protocol_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="proxyProtocolV2")
    def proxy_protocol_v2(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @proxy_protocol_v2.setter
    def proxy_protocol_v2(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="slowStart")
    def slow_start(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @slow_start.setter
    def slow_start(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def stickiness(self) -> Optional[pulumi.Input[TargetGroupStickinessArgs]]: ...
    @stickiness.setter
    def stickiness(self, value: Optional[pulumi.Input[TargetGroupStickinessArgs]]): ...
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
    @pulumi.getter(name="targetControlPort")
    def target_control_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_control_port.setter
    def target_control_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetFailovers")
    def target_failovers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetFailoverArgs]]]
    ]: ...
    @target_failovers.setter
    def target_failovers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetFailoverArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetGroupHealth")
    def target_group_health(
        self,
    ) -> Optional[pulumi.Input[TargetGroupTargetGroupHealthArgs]]: ...
    @target_group_health.setter
    def target_group_health(
        self, value: Optional[pulumi.Input[TargetGroupTargetGroupHealthArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetHealthStates")
    def target_health_states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetHealthStateArgs]]]
    ]: ...
    @target_health_states.setter
    def target_health_states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetHealthStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _TargetGroupState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_termination: Optional[pulumi.Input[_builtins.bool]] = ...,
        deregistration_delay: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check: Optional[pulumi.Input[TargetGroupHealthCheckArgs]] = ...,
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_multi_value_headers_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        load_balancer_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        load_balancing_algorithm_type: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_anomaly_mitigation: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_cross_zone_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preserve_client_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_version: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_protocol_v2: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        slow_start: Optional[pulumi.Input[_builtins.int]] = ...,
        stickiness: Optional[pulumi.Input[TargetGroupStickinessArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_control_port: Optional[pulumi.Input[_builtins.int]] = ...,
        target_failovers: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetFailoverArgs]]]
        ] = ...,
        target_group_health: Optional[
            pulumi.Input[TargetGroupTargetGroupHealthArgs]
        ] = ...,
        target_health_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetHealthStateArgs]]]
        ] = ...,
        target_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="connectionTermination")
    def connection_termination(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @connection_termination.setter
    def connection_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="deregistrationDelay")
    def deregistration_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @deregistration_delay.setter
    def deregistration_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input[TargetGroupHealthCheckArgs]]: ...
    @health_check.setter
    def health_check(
        self, value: Optional[pulumi.Input[TargetGroupHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaMultiValueHeadersEnabled")
    def lambda_multi_value_headers_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @lambda_multi_value_headers_enabled.setter
    def lambda_multi_value_headers_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerArns")
    def load_balancer_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @load_balancer_arns.setter
    def load_balancer_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingAlgorithmType")
    def load_balancing_algorithm_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_algorithm_type.setter
    def load_balancing_algorithm_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingAnomalyMitigation")
    def load_balancing_anomaly_mitigation(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_anomaly_mitigation.setter
    def load_balancing_anomaly_mitigation(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingCrossZoneEnabled")
    def load_balancing_cross_zone_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_cross_zone_enabled.setter
    def load_balancing_cross_zone_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="preserveClientIp")
    def preserve_client_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preserve_client_ip.setter
    def preserve_client_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol_version.setter
    def protocol_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="proxyProtocolV2")
    def proxy_protocol_v2(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @proxy_protocol_v2.setter
    def proxy_protocol_v2(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="slowStart")
    def slow_start(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @slow_start.setter
    def slow_start(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def stickiness(self) -> Optional[pulumi.Input[TargetGroupStickinessArgs]]: ...
    @stickiness.setter
    def stickiness(self, value: Optional[pulumi.Input[TargetGroupStickinessArgs]]): ...
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
    @pulumi.getter(name="targetControlPort")
    def target_control_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_control_port.setter
    def target_control_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetFailovers")
    def target_failovers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetFailoverArgs]]]
    ]: ...
    @target_failovers.setter
    def target_failovers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetFailoverArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetGroupHealth")
    def target_group_health(
        self,
    ) -> Optional[pulumi.Input[TargetGroupTargetGroupHealthArgs]]: ...
    @target_group_health.setter
    def target_group_health(
        self, value: Optional[pulumi.Input[TargetGroupTargetGroupHealthArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetHealthStates")
    def target_health_states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetHealthStateArgs]]]
    ]: ...
    @target_health_states.setter
    def target_health_states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetGroupTargetHealthStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:lb/targetGroup:TargetGroup")
class TargetGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        connection_termination: Optional[pulumi.Input[_builtins.bool]] = ...,
        deregistration_delay: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check: Optional[
            pulumi.Input[
                Union[TargetGroupHealthCheckArgs, TargetGroupHealthCheckArgsDict]
            ]
        ] = ...,
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_multi_value_headers_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        load_balancing_algorithm_type: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_anomaly_mitigation: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_cross_zone_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preserve_client_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_version: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_protocol_v2: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        slow_start: Optional[pulumi.Input[_builtins.int]] = ...,
        stickiness: Optional[
            pulumi.Input[
                Union[TargetGroupStickinessArgs, TargetGroupStickinessArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_control_port: Optional[pulumi.Input[_builtins.int]] = ...,
        target_failovers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TargetGroupTargetFailoverArgs,
                            TargetGroupTargetFailoverArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        target_group_health: Optional[
            pulumi.Input[
                Union[
                    TargetGroupTargetGroupHealthArgs,
                    TargetGroupTargetGroupHealthArgsDict,
                ]
            ]
        ] = ...,
        target_health_states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TargetGroupTargetHealthStateArgs,
                            TargetGroupTargetHealthStateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        target_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[TargetGroupArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_termination: Optional[pulumi.Input[_builtins.bool]] = ...,
        deregistration_delay: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check: Optional[
            pulumi.Input[
                Union[TargetGroupHealthCheckArgs, TargetGroupHealthCheckArgsDict]
            ]
        ] = ...,
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_multi_value_headers_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        load_balancer_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        load_balancing_algorithm_type: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_anomaly_mitigation: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_cross_zone_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preserve_client_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_version: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_protocol_v2: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        slow_start: Optional[pulumi.Input[_builtins.int]] = ...,
        stickiness: Optional[
            pulumi.Input[
                Union[TargetGroupStickinessArgs, TargetGroupStickinessArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_control_port: Optional[pulumi.Input[_builtins.int]] = ...,
        target_failovers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TargetGroupTargetFailoverArgs,
                            TargetGroupTargetFailoverArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        target_group_health: Optional[
            pulumi.Input[
                Union[
                    TargetGroupTargetGroupHealthArgs,
                    TargetGroupTargetGroupHealthArgsDict,
                ]
            ]
        ] = ...,
        target_health_states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TargetGroupTargetHealthStateArgs,
                            TargetGroupTargetHealthStateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        target_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> TargetGroup: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="arnSuffix")
    def arn_suffix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionTermination")
    def connection_termination(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="deregistrationDelay")
    def deregistration_delay(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Output[outputs.TargetGroupHealthCheck]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaMultiValueHeadersEnabled")
    def lambda_multi_value_headers_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerArns")
    def load_balancer_arns(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingAlgorithmType")
    def load_balancing_algorithm_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingAnomalyMitigation")
    def load_balancing_anomaly_mitigation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingCrossZoneEnabled")
    def load_balancing_cross_zone_enabled(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="preserveClientIp")
    def preserve_client_ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="proxyProtocolV2")
    def proxy_protocol_v2(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="slowStart")
    def slow_start(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def stickiness(self) -> pulumi.Output[outputs.TargetGroupStickiness]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetControlPort")
    def target_control_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="targetFailovers")
    def target_failovers(
        self,
    ) -> pulumi.Output[Sequence[outputs.TargetGroupTargetFailover]]: ...
    @_builtins.property
    @pulumi.getter(name="targetGroupHealth")
    def target_group_health(
        self,
    ) -> pulumi.Output[outputs.TargetGroupTargetGroupHealth]: ...
    @_builtins.property
    @pulumi.getter(name="targetHealthStates")
    def target_health_states(
        self,
    ) -> pulumi.Output[Sequence[outputs.TargetGroupTargetHealthState]]: ...
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
