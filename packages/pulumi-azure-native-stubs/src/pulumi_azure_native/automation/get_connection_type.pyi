import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectionTypeResult",
    "AwaitableGetConnectionTypeResult",
    "get_connection_type",
    "get_connection_type_output",
]

@pulumi.output_type
class GetConnectionTypeResult:
    def __init__(
        __self__,
        azure_api_version=...,
        creation_time=...,
        description=...,
        field_definitions=...,
        id=...,
        is_global=...,
        last_modified_time=...,
        name=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fieldDefinitions")
    def field_definitions(self) -> Mapping[str, outputs.FieldDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetConnectionTypeResult(GetConnectionTypeResult):
    def __await__(self): ...

def get_connection_type(
    automation_account_name: Optional[_builtins.str] = ...,
    connection_type_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectionTypeResult: ...
def get_connection_type_output(
    automation_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    connection_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectionTypeResult]: ...
