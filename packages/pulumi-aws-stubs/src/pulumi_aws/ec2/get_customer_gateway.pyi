import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCustomerGatewayResult",
    "AwaitableGetCustomerGatewayResult",
    "get_customer_gateway",
    "get_customer_gateway_output",
]

@pulumi.output_type
class GetCustomerGatewayResult:
    def __init__(
        __self__,
        arn=...,
        bgp_asn=...,
        bgp_asn_extended=...,
        certificate_arn=...,
        device_name=...,
        filters=...,
        id=...,
        ip_address=...,
        region=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="bgpAsnExtended")
    def bgp_asn_extended(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetCustomerGatewayFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetCustomerGatewayResult(GetCustomerGatewayResult):
    def __await__(self): ...

def get_customer_gateway(
    filters: Optional[
        Sequence[Union[GetCustomerGatewayFilterArgs, GetCustomerGatewayFilterArgsDict]]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCustomerGatewayResult: ...
def get_customer_gateway_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetCustomerGatewayFilterArgs, GetCustomerGatewayFilterArgsDict
                    ]
                ]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCustomerGatewayResult]: ...
