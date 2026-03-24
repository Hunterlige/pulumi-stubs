import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAppleAppResult",
    "AwaitableGetAppleAppResult",
    "get_apple_app",
    "get_apple_app_output",
]

@pulumi.output_type
class GetAppleAppResult:
    def __init__(
        __self__,
        api_key_id=...,
        app_id=...,
        app_store_id=...,
        bundle_id=...,
        deletion_policy=...,
        display_name=...,
        id=...,
        name=...,
        project=...,
        team_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="appStoreId")
    def app_store_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="teamId")
    def team_id(self) -> _builtins.str: ...

class AwaitableGetAppleAppResult(GetAppleAppResult):
    def __await__(self): ...

def get_apple_app(
    app_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAppleAppResult: ...
def get_apple_app_output(
    app_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAppleAppResult]: ...
