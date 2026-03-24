import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetResolverEndpointResult",
    "AwaitableGetResolverEndpointResult",
    "get_resolver_endpoint",
    "get_resolver_endpoint_output",
]

@pulumi.output_type
class GetResolverEndpointResult:
    def __init__(
        __self__,
        arn=...,
        direction=...,
        filters=...,
        id=...,
        ip_addresses=...,
        name=...,
        protocols=...,
        region=...,
        resolver_endpoint_id=...,
        resolver_endpoint_type=...,
        rni_enhanced_metrics_enabled=...,
        status=...,
        target_name_server_metrics_enabled=...,
        vpc_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetResolverEndpointFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resolverEndpointId")
    def resolver_endpoint_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resolverEndpointType")
    def resolver_endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rniEnhancedMetricsEnabled")
    def rni_enhanced_metrics_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetNameServerMetricsEnabled")
    def target_name_server_metrics_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

class AwaitableGetResolverEndpointResult(GetResolverEndpointResult):
    def __await__(self): ...

def get_resolver_endpoint(
    filters: Optional[
        Sequence[
            Union[GetResolverEndpointFilterArgs, GetResolverEndpointFilterArgsDict]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    resolver_endpoint_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetResolverEndpointResult: ...
def get_resolver_endpoint_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetResolverEndpointFilterArgs, GetResolverEndpointFilterArgsDict
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resolver_endpoint_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetResolverEndpointResult]: ...
