import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ResolverEndpointArgs", "ResolverEndpoint"]

@pulumi.input_type
class ResolverEndpointArgs:
    def __init__(
        __self__,
        *,
        direction: pulumi.Input[_builtins.str],
        ip_addresses: pulumi.Input[
            Sequence[pulumi.Input[ResolverEndpointIpAddressArgs]]
        ],
        security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolver_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        rni_enhanced_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_name_server_metrics_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Input[_builtins.str]: ...
    @direction.setter
    def direction(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ResolverEndpointIpAddressArgs]]]: ...
    @ip_addresses.setter
    def ip_addresses(
        self, value: pulumi.Input[Sequence[pulumi.Input[ResolverEndpointIpAddressArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocols(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @protocols.setter
    def protocols(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resolverEndpointType")
    def resolver_endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resolver_endpoint_type.setter
    def resolver_endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rniEnhancedMetricsEnabled")
    def rni_enhanced_metrics_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @rni_enhanced_metrics_enabled.setter
    def rni_enhanced_metrics_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
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
    @pulumi.getter(name="targetNameServerMetricsEnabled")
    def target_name_server_metrics_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @target_name_server_metrics_enabled.setter
    def target_name_server_metrics_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.input_type
class _ResolverEndpointState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        direction: Optional[pulumi.Input[_builtins.str]] = ...,
        host_vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResolverEndpointIpAddressArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolver_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        rni_enhanced_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_name_server_metrics_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostVpcId")
    def host_vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_vpc_id.setter
    def host_vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResolverEndpointIpAddressArgs]]]
    ]: ...
    @ip_addresses.setter
    def ip_addresses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResolverEndpointIpAddressArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocols(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @protocols.setter
    def protocols(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resolverEndpointType")
    def resolver_endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resolver_endpoint_type.setter
    def resolver_endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rniEnhancedMetricsEnabled")
    def rni_enhanced_metrics_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @rni_enhanced_metrics_enabled.setter
    def rni_enhanced_metrics_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
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
    @pulumi.getter(name="targetNameServerMetricsEnabled")
    def target_name_server_metrics_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @target_name_server_metrics_enabled.setter
    def target_name_server_metrics_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.type_token("aws:route53/resolverEndpoint:ResolverEndpoint")
class ResolverEndpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        direction: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_addresses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ResolverEndpointIpAddressArgs,
                            ResolverEndpointIpAddressArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolver_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        rni_enhanced_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_name_server_metrics_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ResolverEndpointArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        direction: Optional[pulumi.Input[_builtins.str]] = ...,
        host_vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_addresses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ResolverEndpointIpAddressArgs,
                            ResolverEndpointIpAddressArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolver_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        rni_enhanced_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_name_server_metrics_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> ResolverEndpoint: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostVpcId")
    def host_vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> pulumi.Output[Sequence[outputs.ResolverEndpointIpAddress]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resolverEndpointType")
    def resolver_endpoint_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rniEnhancedMetricsEnabled")
    def rni_enhanced_metrics_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetNameServerMetricsEnabled")
    def target_name_server_metrics_enabled(self) -> pulumi.Output[_builtins.bool]: ...
