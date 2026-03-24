import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DnsZoneArgs", "DnsZone"]

@pulumi.input_type
class DnsZoneArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        dns_zone_id: pulumi.Input[_builtins.str],
        domain: pulumi.Input[_builtins.str],
        org_id: pulumi.Input[_builtins.str],
        peering_config: pulumi.Input[DnsZonePeeringConfigArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dnsZoneId")
    def dns_zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @dns_zone_id.setter
    def dns_zone_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="peeringConfig")
    def peering_config(self) -> pulumi.Input[DnsZonePeeringConfigArgs]: ...
    @peering_config.setter
    def peering_config(self, value: pulumi.Input[DnsZonePeeringConfigArgs]): ...

@pulumi.input_type
class _DnsZoneState:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        peering_config: Optional[pulumi.Input[DnsZonePeeringConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsZoneId")
    def dns_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_zone_id.setter
    def dns_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peeringConfig")
    def peering_config(self) -> Optional[pulumi.Input[DnsZonePeeringConfigArgs]]: ...
    @peering_config.setter
    def peering_config(
        self, value: Optional[pulumi.Input[DnsZonePeeringConfigArgs]]
    ): ...

@pulumi.type_token("gcp:apigee/dnsZone:DnsZone")
class DnsZone(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        peering_config: Optional[
            pulumi.Input[Union[DnsZonePeeringConfigArgs, DnsZonePeeringConfigArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DnsZoneArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        peering_config: Optional[
            pulumi.Input[Union[DnsZonePeeringConfigArgs, DnsZonePeeringConfigArgsDict]]
        ] = ...,
    ) -> DnsZone: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsZoneId")
    def dns_zone_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peeringConfig")
    def peering_config(self) -> pulumi.Output[outputs.DnsZonePeeringConfig]: ...
