import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecurityGroupRuleArgs", "SecurityGroupRule"]

@pulumi.input_type
class SecurityGroupRuleArgs:
    def __init__(
        __self__,
        *,
        from_port: pulumi.Input[_builtins.int],
        protocol: pulumi.Input[Union[_builtins.str, ProtocolType]],
        security_group_id: pulumi.Input[_builtins.str],
        to_port: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        prefix_list_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        self: Optional[pulumi.Input[_builtins.bool]] = ...,
        source_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]: ...
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[Union[_builtins.str, ProtocolType]]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[Union[_builtins.str, ProtocolType]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @security_group_id.setter
    def security_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]: ...
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cidr_blocks.setter
    def cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ipv6_cidr_blocks.setter
    def ipv6_cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prefix_list_ids.setter
    def prefix_list_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @self.setter
    def self(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_security_group_id.setter
    def source_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _SecurityGroupRuleState:
    def __init__(
        __self__,
        *,
        cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        prefix_list_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protocol: Optional[pulumi.Input[Union[_builtins.str, ProtocolType]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        self: Optional[pulumi.Input[_builtins.bool]] = ...,
        source_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cidr_blocks.setter
    def cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ipv6_cidr_blocks.setter
    def ipv6_cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prefix_list_ids.setter
    def prefix_list_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtocolType]]]: ...
    @protocol.setter
    def protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtocolType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_group_id.setter
    def security_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupRuleId")
    def security_group_rule_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_group_rule_id.setter
    def security_group_rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @self.setter
    def self(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_security_group_id.setter
    def source_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:ec2/securityGroupRule:SecurityGroupRule")
class SecurityGroupRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        prefix_list_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protocol: Optional[pulumi.Input[Union[_builtins.str, ProtocolType]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        self: Optional[pulumi.Input[_builtins.bool]] = ...,
        source_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecurityGroupRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        prefix_list_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protocol: Optional[pulumi.Input[Union[_builtins.str, ProtocolType]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        self: Optional[pulumi.Input[_builtins.bool]] = ...,
        source_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SecurityGroupRule: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupRuleId")
    def security_group_rule_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def self(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
