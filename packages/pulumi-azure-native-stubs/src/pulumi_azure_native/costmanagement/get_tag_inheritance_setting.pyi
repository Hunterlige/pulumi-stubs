import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTagInheritanceSettingResult",
    "AwaitableGetTagInheritanceSettingResult",
    "get_tag_inheritance_setting",
    "get_tag_inheritance_setting_output",
]

@pulumi.output_type
class GetTagInheritanceSettingResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        kind=...,
        name=...,
        properties=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
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
    def properties(self) -> outputs.TagInheritancePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetTagInheritanceSettingResult(GetTagInheritanceSettingResult):
    def __await__(self): ...

def get_tag_inheritance_setting(
    scope: Optional[_builtins.str] = ...,
    type: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTagInheritanceSettingResult: ...
def get_tag_inheritance_setting_output(
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    type: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTagInheritanceSettingResult]: ...
