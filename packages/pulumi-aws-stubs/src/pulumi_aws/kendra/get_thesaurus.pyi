import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetThesaurusResult",
    "AwaitableGetThesaurusResult",
    "get_thesaurus",
    "get_thesaurus_output",
]

@pulumi.output_type
class GetThesaurusResult:
    def __init__(
        __self__,
        arn=...,
        created_at=...,
        description=...,
        error_message=...,
        file_size_bytes=...,
        id=...,
        index_id=...,
        name=...,
        region=...,
        role_arn=...,
        source_s3_paths=...,
        status=...,
        synonym_rule_count=...,
        tags=...,
        term_count=...,
        thesaurus_id=...,
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
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceS3Paths")
    def source_s3_paths(self) -> Sequence[outputs.GetThesaurusSourceS3PathResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="synonymRuleCount")
    def synonym_rule_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="termCount")
    def term_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="thesaurusId")
    def thesaurus_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...

class AwaitableGetThesaurusResult(GetThesaurusResult):
    def __await__(self): ...

def get_thesaurus(
    index_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    thesaurus_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetThesaurusResult: ...
def get_thesaurus_output(
    index_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    thesaurus_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetThesaurusResult]: ...
