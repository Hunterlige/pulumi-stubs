import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetActivityCustomEntityQueryResult",
    "AwaitableGetActivityCustomEntityQueryResult",
    "get_activity_custom_entity_query",
    "get_activity_custom_entity_query_output",
]

@pulumi.output_type
class GetActivityCustomEntityQueryResult:
    def __init__(
        __self__,
        azure_api_version=...,
        content=...,
        created_time_utc=...,
        description=...,
        enabled=...,
        entities_filter=...,
        etag=...,
        id=...,
        input_entity_type=...,
        kind=...,
        last_modified_time_utc=...,
        name=...,
        query_definitions=...,
        required_input_fields_sets=...,
        system_data=...,
        template_name=...,
        title=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="entitiesFilter")
    def entities_filter(self) -> Optional[Mapping[str, Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputEntityType")
    def input_entity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryDefinitions")
    def query_definitions(
        self,
    ) -> Optional[outputs.ActivityEntityQueriesPropertiesResponseQueryDefinitions]: ...
    @_builtins.property
    @pulumi.getter(name="requiredInputFieldsSets")
    def required_input_fields_sets(
        self,
    ) -> Optional[Sequence[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetActivityCustomEntityQueryResult(GetActivityCustomEntityQueryResult):
    def __await__(self): ...

def get_activity_custom_entity_query(
    entity_query_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetActivityCustomEntityQueryResult: ...
def get_activity_custom_entity_query_output(
    entity_query_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetActivityCustomEntityQueryResult]: ...
