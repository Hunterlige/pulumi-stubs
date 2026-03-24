import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectionsResult",
    "AwaitableGetConnectionsResult",
    "get_connections",
    "get_connections_output",
]

@pulumi.output_type
class GetConnectionsResult:
    def __init__(
        __self__, device_id=..., global_network_id=..., id=..., ids=..., tags=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

class AwaitableGetConnectionsResult(GetConnectionsResult):
    def __await__(self): ...

def get_connections(
    device_id: Optional[_builtins.str] = ...,
    global_network_id: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectionsResult: ...
def get_connections_output(
    device_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    global_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectionsResult]: ...
