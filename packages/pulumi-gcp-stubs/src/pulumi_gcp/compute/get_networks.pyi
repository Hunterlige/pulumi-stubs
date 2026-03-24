import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworksResult",
    "AwaitableGetNetworksResult",
    "get_networks",
    "get_networks_output",
]

@pulumi.output_type
class GetNetworksResult:
    def __init__(
        __self__, id=..., networks=..., project=..., self_link=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def networks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...

class AwaitableGetNetworksResult(GetNetworksResult):
    def __await__(self): ...

def get_networks(
    project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetNetworksResult: ...
def get_networks_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworksResult]: ...
