import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPeeredDnsDomainResult",
    "AwaitableGetPeeredDnsDomainResult",
    "get_peered_dns_domain",
    "get_peered_dns_domain_output",
]

@pulumi.output_type
class GetPeeredDnsDomainResult:
    def __init__(
        __self__,
        dns_suffix=...,
        id=...,
        name=...,
        network=...,
        parent=...,
        project=...,
        service=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

class AwaitableGetPeeredDnsDomainResult(GetPeeredDnsDomainResult):
    def __await__(self): ...

def get_peered_dns_domain(
    name: Optional[_builtins.str] = ...,
    network: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    service: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPeeredDnsDomainResult: ...
def get_peered_dns_domain_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    network: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[_builtins.str]] = ...,
    service: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPeeredDnsDomainResult]: ...
