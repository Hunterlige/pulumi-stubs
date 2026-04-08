import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSchemaResult",
    "AwaitableGetSchemaResult",
    "get_schema",
    "get_schema_output",
]

@pulumi.output_type
class GetSchemaResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        display_name=...,
        format=...,
        id=...,
        name=...,
        provisioning_state=...,
        schema_type=...,
        system_data=...,
        tags=...,
        type=...,
        uuid=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> _builtins.str: ...

class AwaitableGetSchemaResult(GetSchemaResult):
    def __await__(self): ...

def get_schema(
    resource_group_name: Optional[_builtins.str] = ...,
    schema_name: Optional[_builtins.str] = ...,
    schema_registry_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSchemaResult: ...
def get_schema_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    schema_name: Optional[pulumi.Input[_builtins.str]] = ...,
    schema_registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSchemaResult]: ...
