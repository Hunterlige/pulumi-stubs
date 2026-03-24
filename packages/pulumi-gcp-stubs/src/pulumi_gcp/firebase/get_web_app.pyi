import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAppResult",
    "AwaitableGetWebAppResult",
    "get_web_app",
    "get_web_app_output",
]

@pulumi.output_type
class GetWebAppResult:
    def __init__(
        __self__,
        api_key_id=...,
        app_id=...,
        app_urls=...,
        deletion_policy=...,
        display_name=...,
        id=...,
        name=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="appUrls")
    def app_urls(self) -> Sequence[_builtins.str]: ...
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

class AwaitableGetWebAppResult(GetWebAppResult):
    def __await__(self): ...

def get_web_app(
    app_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAppResult: ...
def get_web_app_output(
    app_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAppResult]: ...
