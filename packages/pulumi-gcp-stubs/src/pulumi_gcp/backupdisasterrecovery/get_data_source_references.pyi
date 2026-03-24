import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDataSourceReferencesResult",
    "AwaitableGetDataSourceReferencesResult",
    "get_data_source_references",
    "get_data_source_references_output",
]

@pulumi.output_type
class GetDataSourceReferencesResult:
    def __init__(
        __self__,
        data_source_references=...,
        id=...,
        location=...,
        project=...,
        resource_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceReferences")
    def data_source_references(
        self,
    ) -> Sequence[outputs.GetDataSourceReferencesDataSourceReferenceResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    @_utilities.deprecated(...)
    def resource_type(self) -> Optional[_builtins.str]: ...

class AwaitableGetDataSourceReferencesResult(GetDataSourceReferencesResult):
    def __await__(self): ...

def get_data_source_references(
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    resource_type: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDataSourceReferencesResult: ...
def get_data_source_references_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDataSourceReferencesResult]: ...
