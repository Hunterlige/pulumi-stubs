import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetResolverFirewallDomainListResult",
    "AwaitableGetResolverFirewallDomainListResult",
    "get_resolver_firewall_domain_list",
    "get_resolver_firewall_domain_list_output",
]

@pulumi.output_type
class GetResolverFirewallDomainListResult:
    def __init__(
        __self__,
        arn=...,
        creation_time=...,
        creator_request_id=...,
        domain_count=...,
        firewall_domain_list_id=...,
        id=...,
        managed_owner_name=...,
        modification_time=...,
        name=...,
        region=...,
        status=...,
        status_message=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creatorRequestId")
    def creator_request_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainCount")
    def domain_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="firewallDomainListId")
    def firewall_domain_list_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedOwnerName")
    def managed_owner_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modificationTime")
    def modification_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str: ...

class AwaitableGetResolverFirewallDomainListResult(GetResolverFirewallDomainListResult):
    def __await__(self): ...

def get_resolver_firewall_domain_list(
    firewall_domain_list_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetResolverFirewallDomainListResult: ...
def get_resolver_firewall_domain_list_output(
    firewall_domain_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetResolverFirewallDomainListResult]: ...
