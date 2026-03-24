import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAttachmentResult",
    "AwaitableGetAttachmentResult",
    "get_attachment",
    "get_attachment_output",
]

@pulumi.output_type
class GetAttachmentResult:
    def __init__(
        __self__,
        arn=...,
        association_state=...,
        association_transit_gateway_route_table_id=...,
        filters=...,
        id=...,
        region=...,
        resource_id=...,
        resource_owner_id=...,
        resource_type=...,
        state=...,
        tags=...,
        transit_gateway_attachment_id=...,
        transit_gateway_id=...,
        transit_gateway_owner_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="associationState")
    def association_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="associationTransitGatewayRouteTableId")
    def association_transit_gateway_route_table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetAttachmentFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceOwnerId")
    def resource_owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayOwnerId")
    def transit_gateway_owner_id(self) -> _builtins.str: ...

class AwaitableGetAttachmentResult(GetAttachmentResult):
    def __await__(self): ...

def get_attachment(
    filters: Optional[
        Sequence[Union[GetAttachmentFilterArgs, GetAttachmentFilterArgsDict]]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    transit_gateway_attachment_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAttachmentResult: ...
def get_attachment_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetAttachmentFilterArgs, GetAttachmentFilterArgsDict]]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    transit_gateway_attachment_id: Optional[
        pulumi.Input[Optional[_builtins.str]]
    ] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAttachmentResult]: ...
