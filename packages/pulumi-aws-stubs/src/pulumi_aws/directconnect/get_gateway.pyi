import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGatewayResult",
    "AwaitableGetGatewayResult",
    "get_gateway",
    "get_gateway_output",
]

@pulumi.output_type
class GetGatewayResult:
    def __init__(
        __self__,
        amazon_side_asn=...,
        arn=...,
        id=...,
        name=...,
        owner_account_id=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetGatewayResult(GetGatewayResult):
    def __await__(self): ...

def get_gateway(
    name: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGatewayResult: ...
def get_gateway_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGatewayResult]: ...
