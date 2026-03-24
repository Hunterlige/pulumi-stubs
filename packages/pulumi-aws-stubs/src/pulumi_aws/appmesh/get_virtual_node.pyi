import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualNodeResult",
    "AwaitableGetVirtualNodeResult",
    "get_virtual_node",
    "get_virtual_node_output",
]

@pulumi.output_type
class GetVirtualNodeResult:
    def __init__(
        __self__,
        arn=...,
        created_date=...,
        id=...,
        last_updated_date=...,
        mesh_name=...,
        mesh_owner=...,
        name=...,
        region=...,
        resource_owner=...,
        specs=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="meshName")
    def mesh_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def specs(self) -> Sequence[outputs.GetVirtualNodeSpecResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetVirtualNodeResult(GetVirtualNodeResult):
    def __await__(self): ...

def get_virtual_node(
    mesh_name: Optional[_builtins.str] = ...,
    mesh_owner: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualNodeResult: ...
def get_virtual_node_output(
    mesh_name: Optional[pulumi.Input[_builtins.str]] = ...,
    mesh_owner: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualNodeResult]: ...
