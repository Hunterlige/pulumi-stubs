import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAppregistryAttributeGroupResult",
    "AwaitableGetAppregistryAttributeGroupResult",
    "get_appregistry_attribute_group",
    "get_appregistry_attribute_group_output",
]

@pulumi.output_type
class GetAppregistryAttributeGroupResult:
    def __init__(
        __self__,
        arn=...,
        attributes=...,
        description=...,
        id=...,
        name=...,
        region=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetAppregistryAttributeGroupResult(GetAppregistryAttributeGroupResult):
    def __await__(self): ...

def get_appregistry_attribute_group(
    arn: Optional[_builtins.str] = ...,
    id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAppregistryAttributeGroupResult: ...
def get_appregistry_attribute_group_output(
    arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAppregistryAttributeGroupResult]: ...
