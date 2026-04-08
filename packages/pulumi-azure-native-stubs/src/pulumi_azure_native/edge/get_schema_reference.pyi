import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSchemaReferenceResult",
    "AwaitableGetSchemaReferenceResult",
    "get_schema_reference",
    "get_schema_reference_output",
]

@pulumi.output_type
class GetSchemaReferenceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        e_tag=...,
        id=...,
        name=...,
        properties=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.SchemaReferencePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSchemaReferenceResult(GetSchemaReferenceResult):
    def __await__(self): ...

def get_schema_reference(
    resource_uri: Optional[_builtins.str] = ...,
    schema_reference_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSchemaReferenceResult: ...
def get_schema_reference_output(
    resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    schema_reference_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSchemaReferenceResult]: ...
