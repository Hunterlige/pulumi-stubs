import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectionResult",
    "AwaitableGetConnectionResult",
    "get_connection",
    "get_connection_output",
]

@pulumi.output_type
class GetConnectionResult:
    def __init__(
        __self__,
        arn=...,
        aws_device=...,
        bandwidth=...,
        id=...,
        location=...,
        name=...,
        owner_account_id=...,
        partner_name=...,
        provider_name=...,
        region=...,
        state=...,
        tags=...,
        vlan_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def bandwidth(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> _builtins.int: ...

class AwaitableGetConnectionResult(GetConnectionResult):
    def __await__(self): ...

def get_connection(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectionResult: ...
def get_connection_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectionResult]: ...
