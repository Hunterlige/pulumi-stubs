import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDocumentResult",
    "AwaitableGetDocumentResult",
    "get_document",
    "get_document_output",
]

@pulumi.output_type
class GetDocumentResult:
    def __init__(
        __self__,
        arn=...,
        content=...,
        document_format=...,
        document_type=...,
        document_version=...,
        id=...,
        name=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="documentFormat")
    def document_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentType")
    def document_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetDocumentResult(GetDocumentResult):
    def __await__(self): ...

def get_document(
    document_format: Optional[_builtins.str] = ...,
    document_version: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDocumentResult: ...
def get_document_output(
    document_format: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    document_version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDocumentResult]: ...
