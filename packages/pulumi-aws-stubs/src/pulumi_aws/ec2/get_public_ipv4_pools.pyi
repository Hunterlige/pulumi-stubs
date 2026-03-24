import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPublicIpv4PoolsResult",
    "AwaitableGetPublicIpv4PoolsResult",
    "get_public_ipv4_pools",
    "get_public_ipv4_pools_output",
]

@pulumi.output_type
class GetPublicIpv4PoolsResult:
    def __init__(
        __self__, filters=..., id=..., pool_ids=..., region=..., tags=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetPublicIpv4PoolsFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="poolIds")
    def pool_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetPublicIpv4PoolsResult(GetPublicIpv4PoolsResult):
    def __await__(self): ...

def get_public_ipv4_pools(
    filters: Optional[
        Sequence[Union[GetPublicIpv4PoolsFilterArgs, GetPublicIpv4PoolsFilterArgsDict]]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPublicIpv4PoolsResult: ...
def get_public_ipv4_pools_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetPublicIpv4PoolsFilterArgs, GetPublicIpv4PoolsFilterArgsDict
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPublicIpv4PoolsResult]: ...
