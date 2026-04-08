import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSettingResult",
    "AwaitableGetSettingResult",
    "get_setting",
    "get_setting_output",
]

@pulumi.output_type
class GetSettingResult:
    def __init__(
        __self__,
        azure_api_version=...,
        cache=...,
        id=...,
        kind=...,
        name=...,
        scope=...,
        start_on=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cache(self) -> Optional[Sequence[outputs.SettingsPropertiesResponseCache]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startOn")
    def start_on(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSettingResult(GetSettingResult):
    def __await__(self): ...

def get_setting(
    setting_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSettingResult: ...
def get_setting_output(
    setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSettingResult]: ...
