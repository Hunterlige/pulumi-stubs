import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

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
    def __init__(__self__, id=..., odb_networks=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="odbNetworks")
    def odb_networks(self) -> Sequence[outputs.GetNetworksOdbNetworkResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetNetworksResult(GetNetworksResult):
    def __await__(self): ...

def get_networks(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetNetworksResult: ...
def get_networks_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworksResult]: ...
