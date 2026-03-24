import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetObjectSignedUrlResult",
    "AwaitableGetObjectSignedUrlResult",
    "get_object_signed_url",
    "get_object_signed_url_output",
]

@pulumi.output_type
class GetObjectSignedUrlResult:
    def __init__(
        __self__,
        bucket=...,
        content_md5=...,
        content_type=...,
        credentials=...,
        duration=...,
        extension_headers=...,
        http_method=...,
        id=...,
        path=...,
        signed_url=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contentMd5")
    def content_md5(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extensionHeaders")
    def extension_headers(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signedUrl")
    def signed_url(self) -> _builtins.str: ...

class AwaitableGetObjectSignedUrlResult(GetObjectSignedUrlResult):
    def __await__(self): ...

def get_object_signed_url(
    bucket: Optional[_builtins.str] = ...,
    content_md5: Optional[_builtins.str] = ...,
    content_type: Optional[_builtins.str] = ...,
    credentials: Optional[_builtins.str] = ...,
    duration: Optional[_builtins.str] = ...,
    extension_headers: Optional[Mapping[str, _builtins.str]] = ...,
    http_method: Optional[_builtins.str] = ...,
    path: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetObjectSignedUrlResult: ...
def get_object_signed_url_output(
    bucket: Optional[pulumi.Input[_builtins.str]] = ...,
    content_md5: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    content_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    credentials: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    duration: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    extension_headers: Optional[
        pulumi.Input[Optional[Mapping[str, _builtins.str]]]
    ] = ...,
    http_method: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    path: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetObjectSignedUrlResult]: ...
