import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkEndpointGroupResult",
    "AwaitableGetNetworkEndpointGroupResult",
    "get_network_endpoint_group",
    "get_network_endpoint_group_output",
]

@pulumi.output_type
class GetNetworkEndpointGroupResult:
    def __init__(
        __self__,
        default_port=...,
        description=...,
        generated_id=...,
        id=...,
        name=...,
        network=...,
        network_endpoint_type=...,
        project=...,
        self_link=...,
        size=...,
        subnetwork=...,
        zone=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultPort")
    def default_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="generatedId")
    def generated_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkEndpointType")
    def network_endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

class AwaitableGetNetworkEndpointGroupResult(GetNetworkEndpointGroupResult):
    def __await__(self): ...

def get_network_endpoint_group(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    self_link: Optional[_builtins.str] = ...,
    zone: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkEndpointGroupResult: ...
def get_network_endpoint_group_output(
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    self_link: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkEndpointGroupResult]: ...
