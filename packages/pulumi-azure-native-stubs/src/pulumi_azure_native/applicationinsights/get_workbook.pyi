import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkbookResult",
    "AwaitableGetWorkbookResult",
    "get_workbook",
    "get_workbook_output",
]

@pulumi.output_type
class GetWorkbookResult:
    def __init__(
        __self__,
        azure_api_version=...,
        category=...,
        description=...,
        display_name=...,
        etag=...,
        id=...,
        identity=...,
        kind=...,
        location=...,
        name=...,
        revision=...,
        serialized_data=...,
        source_id=...,
        storage_uri=...,
        system_data=...,
        tags=...,
        time_modified=...,
        type=...,
        user_id=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.WorkbookResourceResponseIdentity]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serializedData")
    def serialized_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

class AwaitableGetWorkbookResult(GetWorkbookResult):
    def __await__(self): ...

def get_workbook(
    can_fetch_content: Optional[_builtins.bool] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkbookResult: ...
def get_workbook_output(
    can_fetch_content: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkbookResult]: ...
