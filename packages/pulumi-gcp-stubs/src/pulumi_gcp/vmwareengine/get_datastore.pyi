import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatastoreResult",
    "AwaitableGetDatastoreResult",
    "get_datastore",
    "get_datastore_output",
]

@pulumi.output_type
class GetDatastoreResult:
    def __init__(
        __self__,
        clusters=...,
        create_time=...,
        description=...,
        id=...,
        location=...,
        name=...,
        nfs_datastores=...,
        project=...,
        state=...,
        uid=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def clusters(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nfsDatastores")
    def nfs_datastores(self) -> Sequence[outputs.GetDatastoreNfsDatastoreResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetDatastoreResult(GetDatastoreResult):
    def __await__(self): ...

def get_datastore(
    location: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDatastoreResult: ...
def get_datastore_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatastoreResult]: ...
