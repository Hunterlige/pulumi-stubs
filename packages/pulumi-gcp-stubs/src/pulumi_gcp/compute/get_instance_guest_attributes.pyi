import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceGuestAttributesResult",
    "AwaitableGetInstanceGuestAttributesResult",
    "get_instance_guest_attributes",
    "get_instance_guest_attributes_output",
]

@pulumi.output_type
class GetInstanceGuestAttributesResult:
    def __init__(
        __self__,
        id=...,
        name=...,
        project=...,
        query_path=...,
        query_values=...,
        region=...,
        variable_key=...,
        variable_value=...,
        zone=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryPath")
    def query_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryValues")
    def query_values(
        self,
    ) -> Sequence[outputs.GetInstanceGuestAttributesQueryValueResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="variableKey")
    def variable_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="variableValue")
    def variable_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

class AwaitableGetInstanceGuestAttributesResult(GetInstanceGuestAttributesResult):
    def __await__(self): ...

def get_instance_guest_attributes(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    query_path: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    variable_key: Optional[_builtins.str] = ...,
    zone: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceGuestAttributesResult: ...
def get_instance_guest_attributes_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    query_path: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    variable_key: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceGuestAttributesResult]: ...
