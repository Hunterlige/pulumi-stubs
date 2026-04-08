import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecurityRuleResult",
    "AwaitableGetSecurityRuleResult",
    "get_security_rule",
    "get_security_rule_output",
]

@pulumi.output_type
class GetSecurityRuleResult:
    def __init__(
        __self__,
        access=...,
        azure_api_version=...,
        description=...,
        destination_address_prefix=...,
        destination_address_prefixes=...,
        destination_application_security_groups=...,
        destination_port_range=...,
        destination_port_ranges=...,
        direction=...,
        etag=...,
        id=...,
        name=...,
        priority=...,
        protocol=...,
        provisioning_state=...,
        source_address_prefix=...,
        source_address_prefixes=...,
        source_application_security_groups=...,
        source_port_range=...,
        source_port_ranges=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def access(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationAddressPrefix")
    def destination_address_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationAddressPrefixes")
    def destination_address_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationApplicationSecurityGroups")
    def destination_application_security_groups(
        self,
    ) -> Optional[Sequence[outputs.ApplicationSecurityGroupResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefix")
    def source_address_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefixes")
    def source_address_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceApplicationSecurityGroups")
    def source_application_security_groups(
        self,
    ) -> Optional[Sequence[outputs.ApplicationSecurityGroupResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

class AwaitableGetSecurityRuleResult(GetSecurityRuleResult):
    def __await__(self): ...

def get_security_rule(
    network_security_group_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    security_rule_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecurityRuleResult: ...
def get_security_rule_output(
    network_security_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    security_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecurityRuleResult]: ...
