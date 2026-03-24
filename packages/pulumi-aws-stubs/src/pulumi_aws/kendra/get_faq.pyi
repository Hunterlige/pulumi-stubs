import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetFaqResult", "AwaitableGetFaqResult", "get_faq", "get_faq_output"]

@pulumi.output_type
class GetFaqResult:
    def __init__(
        __self__,
        arn=...,
        created_at=...,
        description=...,
        error_message=...,
        faq_id=...,
        file_format=...,
        id=...,
        index_id=...,
        language_code=...,
        name=...,
        region=...,
        role_arn=...,
        s3_paths=...,
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
    @pulumi.getter(name="faqId")
    def faq_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileFormat")
    def file_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="indexId")
    def index_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> _builtins.str: ...
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
    @pulumi.getter(name="s3Paths")
    def s3_paths(self) -> Sequence[outputs.GetFaqS3PathResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...

class AwaitableGetFaqResult(GetFaqResult):
    def __await__(self): ...

def get_faq(
    faq_id: Optional[_builtins.str] = ...,
    index_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFaqResult: ...
def get_faq_output(
    faq_id: Optional[pulumi.Input[_builtins.str]] = ...,
    index_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFaqResult]: ...
