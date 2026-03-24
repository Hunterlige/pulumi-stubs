import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAutokeyConfigResult",
    "AwaitableGetAutokeyConfigResult",
    "get_autokey_config",
    "get_autokey_config_output",
]

@pulumi.output_type
class GetAutokeyConfigResult:
    def __init__(__self__, etag=..., folder=..., id=..., key_project=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def folder(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyProject")
    def key_project(self) -> _builtins.str: ...

class AwaitableGetAutokeyConfigResult(GetAutokeyConfigResult):
    def __await__(self): ...

def get_autokey_config(
    folder: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetAutokeyConfigResult: ...
def get_autokey_config_output(
    folder: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAutokeyConfigResult]: ...
