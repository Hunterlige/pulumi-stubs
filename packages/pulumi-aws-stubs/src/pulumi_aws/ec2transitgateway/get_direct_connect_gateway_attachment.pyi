import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDirectConnectGatewayAttachmentResult",
    "AwaitableGetDirectConnectGatewayAttachmentResult",
    "get_direct_connect_gateway_attachment",
    "get_direct_connect_gateway_attachment_output",
]

@pulumi.output_type
class GetDirectConnectGatewayAttachmentResult:
    def __init__(
        __self__,
        arn=...,
        dx_gateway_id=...,
        filters=...,
        id=...,
        region=...,
        tags=...,
        transit_gateway_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dxGatewayId")
    def dx_gateway_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetDirectConnectGatewayAttachmentFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[_builtins.str]: ...

class AwaitableGetDirectConnectGatewayAttachmentResult(
    GetDirectConnectGatewayAttachmentResult
):
    def __await__(self): ...

def get_direct_connect_gateway_attachment(
    dx_gateway_id: Optional[_builtins.str] = ...,
    filters: Optional[
        Sequence[
            Union[
                GetDirectConnectGatewayAttachmentFilterArgs,
                GetDirectConnectGatewayAttachmentFilterArgsDict,
            ]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    transit_gateway_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDirectConnectGatewayAttachmentResult: ...
def get_direct_connect_gateway_attachment_output(
    dx_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetDirectConnectGatewayAttachmentFilterArgs,
                        GetDirectConnectGatewayAttachmentFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    transit_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDirectConnectGatewayAttachmentResult]: ...
