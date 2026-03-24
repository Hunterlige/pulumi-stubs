import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAppConfigResult",
    "AwaitableGetWebAppConfigResult",
    "get_web_app_config",
    "get_web_app_config_output",
]

@pulumi.output_type
class GetWebAppConfigResult:
    def __init__(
        __self__,
        api_key=...,
        auth_domain=...,
        database_url=...,
        id=...,
        location_id=...,
        measurement_id=...,
        messaging_sender_id=...,
        project=...,
        storage_bucket=...,
        web_app_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authDomain")
    def auth_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseUrl")
    def database_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="measurementId")
    def measurement_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="messagingSenderId")
    def messaging_sender_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageBucket")
    def storage_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="webAppId")
    def web_app_id(self) -> _builtins.str: ...

class AwaitableGetWebAppConfigResult(GetWebAppConfigResult):
    def __await__(self): ...

def get_web_app_config(
    project: Optional[_builtins.str] = ...,
    web_app_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAppConfigResult: ...
def get_web_app_config_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    web_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAppConfigResult]: ...
