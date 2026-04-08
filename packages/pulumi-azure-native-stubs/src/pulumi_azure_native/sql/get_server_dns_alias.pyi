import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServerDnsAliasResult",
    "AwaitableGetServerDnsAliasResult",
    "get_server_dns_alias",
    "get_server_dns_alias_output",
]

@pulumi.output_type
class GetServerDnsAliasResult:
    def __init__(
        __self__,
        azure_api_version=...,
        azure_dns_record=...,
        id=...,
        name=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureDnsRecord")
    def azure_dns_record(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetServerDnsAliasResult(GetServerDnsAliasResult):
    def __await__(self): ...

def get_server_dns_alias(
    dns_alias_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServerDnsAliasResult: ...
def get_server_dns_alias_output(
    dns_alias_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServerDnsAliasResult]: ...
