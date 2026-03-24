import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPeeringAttachmentResult",
    "AwaitableGetPeeringAttachmentResult",
    "get_peering_attachment",
    "get_peering_attachment_output",
]

@pulumi.output_type
class GetPeeringAttachmentResult:
    def __init__(
        __self__,
        arn=...,
        filters=...,
        id=...,
        peer_account_id=...,
        peer_region=...,
        peer_transit_gateway_id=...,
        region=...,
        state=...,
        tags=...,
        transit_gateway_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetPeeringAttachmentFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerAccountId")
    def peer_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerTransitGatewayId")
    def peer_transit_gateway_id(self) -> _builtins.str: ...
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
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str: ...

class AwaitableGetPeeringAttachmentResult(GetPeeringAttachmentResult):
    def __await__(self): ...

def get_peering_attachment(
    filters: Optional[
        Sequence[
            Union[GetPeeringAttachmentFilterArgs, GetPeeringAttachmentFilterArgsDict]
        ]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPeeringAttachmentResult: ...
def get_peering_attachment_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetPeeringAttachmentFilterArgs,
                        GetPeeringAttachmentFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPeeringAttachmentResult]: ...
