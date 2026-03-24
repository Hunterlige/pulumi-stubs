import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkAclRuleArgs", "NetworkAclRule"]

@pulumi.input_type
class NetworkAclRuleArgs:
    def __init__(
        __self__,
        *,
        network_acl_id: pulumi.Input[_builtins.str],
        protocol: pulumi.Input[_builtins.str],
        rule_action: pulumi.Input[_builtins.str],
        rule_number: pulumi.Input[_builtins.int],
        cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        egress: Optional[pulumi.Input[_builtins.bool]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        icmp_code: Optional[pulumi.Input[_builtins.int]] = ...,
        icmp_type: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAclId")
    def network_acl_id(self) -> pulumi.Input[_builtins.str]: ...
    @network_acl_id.setter
    def network_acl_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Input[_builtins.str]: ...
    @rule_action.setter
    def rule_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> pulumi.Input[_builtins.int]: ...
    @rule_number.setter
    def rule_number(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @icmp_code.setter
    def icmp_code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @icmp_type.setter
    def icmp_type(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _NetworkAclRuleState:
    def __init__(
        __self__,
        *,
        cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        egress: Optional[pulumi.Input[_builtins.bool]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        icmp_code: Optional[pulumi.Input[_builtins.int]] = ...,
        icmp_type: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        network_acl_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_action: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_number: Optional[pulumi.Input[_builtins.int]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @icmp_code.setter
    def icmp_code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @icmp_type.setter
    def icmp_type(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkAclId")
    def network_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_acl_id.setter
    def network_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_action.setter
    def rule_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rule_number.setter
    def rule_number(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("aws:ec2/networkAclRule:NetworkAclRule")
class NetworkAclRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        egress: Optional[pulumi.Input[_builtins.bool]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        icmp_code: Optional[pulumi.Input[_builtins.int]] = ...,
        icmp_type: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        network_acl_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_action: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_number: Optional[pulumi.Input[_builtins.int]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkAclRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        egress: Optional[pulumi.Input[_builtins.bool]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        icmp_code: Optional[pulumi.Input[_builtins.int]] = ...,
        icmp_type: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        network_acl_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_action: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_number: Optional[pulumi.Input[_builtins.int]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> NetworkAclRule: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def egress(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="networkAclId")
    def network_acl_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
