import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecurityGroupRuleResult",
    "AwaitableGetSecurityGroupRuleResult",
    "get_security_group_rule",
    "get_security_group_rule_output",
]

@pulumi.output_type
class GetSecurityGroupRuleResult:
    def __init__(
        __self__,
        arn=...,
        cidr_ipv4=...,
        cidr_ipv6=...,
        description=...,
        filters=...,
        from_port=...,
        id=...,
        ip_protocol=...,
        is_egress=...,
        prefix_list_id=...,
        referenced_security_group_id=...,
        region=...,
        security_group_id=...,
        security_group_rule_id=...,
        tags=...,
        to_port=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cidrIpv4")
    def cidr_ipv4(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cidrIpv6")
    def cidr_ipv6(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetSecurityGroupRuleFilterResult]]: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isEgress")
    def is_egress(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="referencedSecurityGroupId")
    def referenced_security_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupRuleId")
    def security_group_rule_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int: ...

class AwaitableGetSecurityGroupRuleResult(GetSecurityGroupRuleResult):
    def __await__(self): ...

def get_security_group_rule(
    filters: Optional[
        Sequence[
            Union[GetSecurityGroupRuleFilterArgs, GetSecurityGroupRuleFilterArgsDict]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    security_group_rule_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecurityGroupRuleResult: ...
def get_security_group_rule_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetSecurityGroupRuleFilterArgs,
                        GetSecurityGroupRuleFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    security_group_rule_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecurityGroupRuleResult]: ...
