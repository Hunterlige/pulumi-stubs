import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNatGatewaysResult",
    "AwaitableGetNatGatewaysResult",
    "get_nat_gateways",
    "get_nat_gateways_output",
]

@pulumi.output_type
class GetNatGatewaysResult:
    def __init__(
        __self__, filters=..., id=..., ids=..., region=..., tags=..., vpc_id=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetNatGatewaysFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

class AwaitableGetNatGatewaysResult(GetNatGatewaysResult):
    def __await__(self): ...

def get_nat_gateways(
    filters: Optional[
        Sequence[Union[GetNatGatewaysFilterArgs, GetNatGatewaysFilterArgsDict]]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    vpc_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNatGatewaysResult: ...
def get_nat_gateways_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetNatGatewaysFilterArgs, GetNatGatewaysFilterArgsDict]]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNatGatewaysResult]: ...
