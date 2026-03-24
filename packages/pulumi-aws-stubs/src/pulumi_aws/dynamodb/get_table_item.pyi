import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTableItemResult",
    "AwaitableGetTableItemResult",
    "get_table_item",
    "get_table_item_output",
]

@pulumi.output_type
class GetTableItemResult:
    def __init__(
        __self__,
        expression_attribute_names=...,
        id=...,
        item=...,
        key=...,
        projection_expression=...,
        region=...,
        table_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expressionAttributeNames")
    def expression_attribute_names(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def item(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectionExpression")
    def projection_expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...

class AwaitableGetTableItemResult(GetTableItemResult):
    def __await__(self): ...

def get_table_item(
    expression_attribute_names: Optional[Mapping[str, _builtins.str]] = ...,
    key: Optional[_builtins.str] = ...,
    projection_expression: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    table_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTableItemResult: ...
def get_table_item_output(
    expression_attribute_names: Optional[
        pulumi.Input[Optional[Mapping[str, _builtins.str]]]
    ] = ...,
    key: Optional[pulumi.Input[_builtins.str]] = ...,
    projection_expression: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    table_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTableItemResult]: ...
