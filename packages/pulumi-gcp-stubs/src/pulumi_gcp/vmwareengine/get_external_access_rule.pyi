import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetExternalAccessRuleResult",
    "AwaitableGetExternalAccessRuleResult",
    "get_external_access_rule",
    "get_external_access_rule_output",
]

@pulumi.output_type
class GetExternalAccessRuleResult:
    def __init__(
        __self__,
        action=...,
        create_time=...,
        description=...,
        destination_ip_ranges=...,
        destination_ports=...,
        id=...,
        ip_protocol=...,
        name=...,
        parent=...,
        priority=...,
        source_ip_ranges=...,
        source_ports=...,
        state=...,
        uid=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(
        self,
    ) -> Sequence[outputs.GetExternalAccessRuleDestinationIpRangeResult]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(
        self,
    ) -> Sequence[outputs.GetExternalAccessRuleSourceIpRangeResult]: ...
    @_builtins.property
    @pulumi.getter(name="sourcePorts")
    def source_ports(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetExternalAccessRuleResult(GetExternalAccessRuleResult):
    def __await__(self): ...

def get_external_access_rule(
    name: Optional[_builtins.str] = ...,
    parent: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetExternalAccessRuleResult: ...
def get_external_access_rule_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetExternalAccessRuleResult]: ...
