import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualServiceResult",
    "AwaitableGetVirtualServiceResult",
    "get_virtual_service",
    "get_virtual_service_output",
]

@pulumi.output_type
class GetVirtualServiceResult:
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
    def specs(self) -> Sequence[outputs.GetVirtualServiceSpecResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetVirtualServiceResult(GetVirtualServiceResult):
    def __await__(self): ...

def get_virtual_service(
    mesh_name: Optional[_builtins.str] = ...,
    mesh_owner: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualServiceResult: ...
def get_virtual_service_output(
    mesh_name: Optional[pulumi.Input[_builtins.str]] = ...,
    mesh_owner: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualServiceResult]: ...
