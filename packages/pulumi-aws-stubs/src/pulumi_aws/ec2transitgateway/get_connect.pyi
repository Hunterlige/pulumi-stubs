import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectResult",
    "AwaitableGetConnectResult",
    "get_connect",
    "get_connect_output",
]

@pulumi.output_type
class GetConnectResult:
    def __init__(
        __self__,
        filters=...,
        id=...,
        protocol=...,
        region=...,
        tags=...,
        transit_gateway_connect_id=...,
        transit_gateway_id=...,
        transport_attachment_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetConnectFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayConnectId")
    def transit_gateway_connect_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transportAttachmentId")
    def transport_attachment_id(self) -> _builtins.str: ...

class AwaitableGetConnectResult(GetConnectResult):
    def __await__(self): ...

def get_connect(
    filters: Optional[
        Sequence[Union[GetConnectFilterArgs, GetConnectFilterArgsDict]]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    transit_gateway_connect_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectResult: ...
def get_connect_output(
    filters: Optional[
        pulumi.Input[
            Optional[Sequence[Union[GetConnectFilterArgs, GetConnectFilterArgsDict]]]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    transit_gateway_connect_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectResult]: ...
