import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListListSchemaResult",
    "AwaitableListListSchemaResult",
    "list_list_schema",
    "list_list_schema_output",
]

@pulumi.output_type
class ListListSchemaResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.SchemaResponse]]: ...

class AwaitableListListSchemaResult(ListListSchemaResult):
    def __await__(self): ...

def list_list_schema(
    connection_id: Optional[_builtins.str] = ...,
    content: Optional[_builtins.str] = ...,
    direction: Optional[Union[_builtins.str, SchemaDirection]] = ...,
    id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    pipeline_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    schema_type: Optional[Union[_builtins.str, SchemaType]] = ...,
    schema_uri: Optional[_builtins.str] = ...,
    status: Optional[Union[_builtins.str, SchemaStatus]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListListSchemaResult: ...
def list_list_schema_output(
    connection_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    content: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    direction: Optional[
        pulumi.Input[Optional[Union[_builtins.str, SchemaDirection]]]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    pipeline_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    schema_type: Optional[
        pulumi.Input[Optional[Union[_builtins.str, SchemaType]]]
    ] = ...,
    schema_uri: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    status: Optional[pulumi.Input[Optional[Union[_builtins.str, SchemaStatus]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListListSchemaResult]: ...
