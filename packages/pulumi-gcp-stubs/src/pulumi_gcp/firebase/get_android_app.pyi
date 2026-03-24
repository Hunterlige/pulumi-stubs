import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAndroidAppResult",
    "AwaitableGetAndroidAppResult",
    "get_android_app",
    "get_android_app_output",
]

@pulumi.output_type
class GetAndroidAppResult:
    def __init__(
        __self__,
        api_key_id=...,
        app_id=...,
        deletion_policy=...,
        display_name=...,
        etag=...,
        id=...,
        name=...,
        package_name=...,
        project=...,
        sha1_hashes=...,
        sha256_hashes=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha1Hashes")
    def sha1_hashes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha256Hashes")
    def sha256_hashes(self) -> Sequence[_builtins.str]: ...

class AwaitableGetAndroidAppResult(GetAndroidAppResult):
    def __await__(self): ...

def get_android_app(
    app_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAndroidAppResult: ...
def get_android_app_output(
    app_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAndroidAppResult]: ...
