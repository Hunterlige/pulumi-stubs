import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVpcPeeringConnectionsResult",
    "AwaitableGetVpcPeeringConnectionsResult",
    "get_vpc_peering_connections",
    "get_vpc_peering_connections_output",
]

@pulumi.output_type
class GetVpcPeeringConnectionsResult:
    def __init__(
        __self__, filters=..., id=..., ids=..., region=..., tags=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetVpcPeeringConnectionsFilterResult]]: ...
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

class AwaitableGetVpcPeeringConnectionsResult(GetVpcPeeringConnectionsResult):
    def __await__(self): ...

def get_vpc_peering_connections(
    filters: Optional[
        Sequence[
            Union[
                GetVpcPeeringConnectionsFilterArgs,
                GetVpcPeeringConnectionsFilterArgsDict,
            ]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVpcPeeringConnectionsResult: ...
def get_vpc_peering_connections_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetVpcPeeringConnectionsFilterArgs,
                        GetVpcPeeringConnectionsFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVpcPeeringConnectionsResult]: ...
