import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecurityGroupIngressRuleArgs", "SecurityGroupIngressRule"]

@pulumi.input_type
class SecurityGroupIngressRuleArgs:
    def __init__(
        __self__,
        *,
        ip_protocol: pulumi.Input[_builtins.str],
        security_group_id: pulumi.Input[_builtins.str],
        cidr_ipv4: Optional[pulumi.Input[_builtins.str]] = ...,
        cidr_ipv6: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        referenced_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Input[_builtins.str]: ...
    @ip_protocol.setter
    def ip_protocol(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @security_group_id.setter
    def security_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cidrIpv4")
    def cidr_ipv4(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr_ipv4.setter
    def cidr_ipv4(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cidrIpv6")
    def cidr_ipv6(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr_ipv6.setter
    def cidr_ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="referencedSecurityGroupId")
    def referenced_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @referenced_security_group_id.setter
    def referenced_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _SecurityGroupIngressRuleState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cidr_ipv4: Optional[pulumi.Input[_builtins.str]] = ...,
        cidr_ipv6: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        referenced_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cidrIpv4")
    def cidr_ipv4(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr_ipv4.setter
    def cidr_ipv4(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cidrIpv6")
    def cidr_ipv6(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr_ipv6.setter
    def cidr_ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_protocol.setter
    def ip_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="referencedSecurityGroupId")
    def referenced_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @referenced_security_group_id.setter
    def referenced_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token(...)
class SecurityGroupIngressRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cidr_ipv4: Optional[pulumi.Input[_builtins.str]] = ...,
        cidr_ipv6: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        referenced_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecurityGroupIngressRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cidr_ipv4: Optional[pulumi.Input[_builtins.str]] = ...,
        cidr_ipv6: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        referenced_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> SecurityGroupIngressRule: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cidrIpv4")
    def cidr_ipv4(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cidrIpv6")
    def cidr_ipv6(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="referencedSecurityGroupId")
    def referenced_security_group_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
