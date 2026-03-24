import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetQuerySuggestionsBlockListResult",
    "AwaitableGetQuerySuggestionsBlockListResult",
    "get_query_suggestions_block_list",
    "get_query_suggestions_block_list_output",
]

@pulumi.output_type
class GetQuerySuggestionsBlockListResult:
    def __init__(
        __self__,
        arn=...,
        created_at=...,
        description=...,
        error_message=...,
        file_size_bytes=...,
        id=...,
        index_id=...,
        item_count=...,
        name=...,
        query_suggestions_block_list_id=...,
        region=...,
        role_arn=...,
        source_s3_paths=...,
        status=...,
        tags=...,
        updated_at=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileSizeBytes")
    def file_size_bytes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="indexId")
    def index_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="itemCount")
    def item_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="querySuggestionsBlockListId")
    def query_suggestions_block_list_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceS3Paths")
    def source_s3_paths(
        self,
    ) -> Sequence[outputs.GetQuerySuggestionsBlockListSourceS3PathResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...

class AwaitableGetQuerySuggestionsBlockListResult(GetQuerySuggestionsBlockListResult):
    def __await__(self): ...

def get_query_suggestions_block_list(
    index_id: Optional[_builtins.str] = ...,
    query_suggestions_block_list_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetQuerySuggestionsBlockListResult: ...
def get_query_suggestions_block_list_output(
    index_id: Optional[pulumi.Input[_builtins.str]] = ...,
    query_suggestions_block_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetQuerySuggestionsBlockListResult]: ...
