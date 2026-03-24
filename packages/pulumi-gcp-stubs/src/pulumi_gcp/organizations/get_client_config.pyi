import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClientConfigResult",
    "AwaitableGetClientConfigResult",
    "get_client_config",
    "get_client_config_output",
]

@pulumi.output_type
class GetClientConfigResult:
    def __init__(
        __self__,
        access_token=...,
        default_labels=...,
        id=...,
        project=...,
        region=...,
        zone=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultLabels")
    def default_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

class AwaitableGetClientConfigResult(GetClientConfigResult):
    def __await__(self): ...

def get_client_config(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClientConfigResult: ...
def get_client_config_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClientConfigResult]: ...
