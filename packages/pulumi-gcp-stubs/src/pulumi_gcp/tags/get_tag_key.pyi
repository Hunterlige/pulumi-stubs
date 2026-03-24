import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTagKeyResult",
    "AwaitableGetTagKeyResult",
    "get_tag_key",
    "get_tag_key_output",
]

@pulumi.output_type
class GetTagKeyResult:
    def __init__(
        __self__,
        allowed_values_regex=...,
        create_time=...,
        description=...,
        id=...,
        name=...,
        namespaced_name=...,
        parent=...,
        short_name=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedValuesRegex")
    def allowed_values_regex(self) -> _builtins.str: ...
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
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="namespacedName")
    def namespaced_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetTagKeyResult(GetTagKeyResult):
    def __await__(self): ...

def get_tag_key(
    parent: Optional[_builtins.str] = ...,
    short_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTagKeyResult: ...
def get_tag_key_output(
    parent: Optional[pulumi.Input[_builtins.str]] = ...,
    short_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTagKeyResult]: ...
