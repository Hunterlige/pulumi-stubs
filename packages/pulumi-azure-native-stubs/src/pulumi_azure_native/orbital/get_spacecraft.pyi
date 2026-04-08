import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSpacecraftResult",
    "AwaitableGetSpacecraftResult",
    "get_spacecraft",
    "get_spacecraft_output",
]

@pulumi.output_type
class GetSpacecraftResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        links=...,
        location=...,
        name=...,
        norad_id=...,
        system_data=...,
        tags=...,
        title_line=...,
        tle_line1=...,
        tle_line2=...,
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
    def links(self) -> Sequence[outputs.SpacecraftLinkResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="noradId")
    def norad_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="titleLine")
    def title_line(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tleLine1")
    def tle_line1(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tleLine2")
    def tle_line2(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSpacecraftResult(GetSpacecraftResult):
    def __await__(self): ...

def get_spacecraft(
    resource_group_name: Optional[_builtins.str] = ...,
    spacecraft_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSpacecraftResult: ...
def get_spacecraft_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    spacecraft_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSpacecraftResult]: ...
