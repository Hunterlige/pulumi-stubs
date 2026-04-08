import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSchemaRegistryResult",
    "AwaitableGetSchemaRegistryResult",
    "get_schema_registry",
    "get_schema_registry_output",
]

@pulumi.output_type
class GetSchemaRegistryResult:
    def __init__(
        __self__,
        azure_api_version=...,
        created_at_utc=...,
        e_tag=...,
        group_properties=...,
        id=...,
        location=...,
        name=...,
        schema_compatibility=...,
        schema_type=...,
        system_data=...,
        type=...,
        updated_at_utc=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAtUtc")
    def created_at_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupProperties")
    def group_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
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
    @pulumi.getter(name="schemaCompatibility")
    def schema_compatibility(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedAtUtc")
    def updated_at_utc(self) -> _builtins.str: ...

class AwaitableGetSchemaRegistryResult(GetSchemaRegistryResult):
    def __await__(self): ...

def get_schema_registry(
    namespace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    schema_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSchemaRegistryResult: ...
def get_schema_registry_output(
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    schema_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSchemaRegistryResult]: ...
