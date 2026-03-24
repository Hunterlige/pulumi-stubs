import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVpcAttachmentResult",
    "AwaitableGetVpcAttachmentResult",
    "get_vpc_attachment",
    "get_vpc_attachment_output",
]

@pulumi.output_type
class GetVpcAttachmentResult:
    def __init__(
        __self__,
        appliance_mode_support=...,
        arn=...,
        dns_support=...,
        filters=...,
        id=...,
        ipv6_support=...,
        region=...,
        security_group_referencing_support=...,
        subnet_ids=...,
        tags=...,
        transit_gateway_id=...,
        vpc_id=...,
        vpc_owner_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applianceModeSupport")
    def appliance_mode_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpcAttachmentFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Support")
    def ipv6_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcOwnerId")
    def vpc_owner_id(self) -> _builtins.str: ...

class AwaitableGetVpcAttachmentResult(GetVpcAttachmentResult):
    def __await__(self): ...

def get_vpc_attachment(
    filters: Optional[
        Sequence[Union[GetVpcAttachmentFilterArgs, GetVpcAttachmentFilterArgsDict]]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVpcAttachmentResult: ...
def get_vpc_attachment_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[GetVpcAttachmentFilterArgs, GetVpcAttachmentFilterArgsDict]
                ]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVpcAttachmentResult]: ...
