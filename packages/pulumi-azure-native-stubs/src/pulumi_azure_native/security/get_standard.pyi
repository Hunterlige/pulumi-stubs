import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStandardResult",
    "AwaitableGetStandardResult",
    "get_standard",
    "get_standard_output",
]

@pulumi.output_type
class GetStandardResult:
    def __init__(
        __self__,
        azure_api_version=...,
        category=...,
        components=...,
        description=...,
        display_name=...,
        etag=...,
        id=...,
        kind=...,
        location=...,
        name=...,
        standard_type=...,
        supported_clouds=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def components(
        self,
    ) -> Optional[Sequence[outputs.StandardComponentPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="standardType")
    def standard_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedClouds")
    def supported_clouds(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetStandardResult(GetStandardResult):
    def __await__(self): ...

def get_standard(
    resource_group_name: Optional[_builtins.str] = ...,
    standard_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStandardResult: ...
def get_standard_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    standard_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStandardResult]: ...
