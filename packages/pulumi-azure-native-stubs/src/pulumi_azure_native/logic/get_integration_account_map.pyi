import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIntegrationAccountMapResult",
    "AwaitableGetIntegrationAccountMapResult",
    "get_integration_account_map",
    "get_integration_account_map_output",
]

@pulumi.output_type
class GetIntegrationAccountMapResult:
    def __init__(
        __self__,
        azure_api_version=...,
        changed_time=...,
        content=...,
        content_link=...,
        content_type=...,
        created_time=...,
        id=...,
        location=...,
        map_type=...,
        metadata=...,
        name=...,
        parameters_schema=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> outputs.ContentLinkResponse: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mapType")
    def map_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parametersSchema")
    def parameters_schema(
        self,
    ) -> Optional[outputs.IntegrationAccountMapPropertiesResponseParametersSchema]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetIntegrationAccountMapResult(GetIntegrationAccountMapResult):
    def __await__(self): ...

def get_integration_account_map(
    integration_account_name: Optional[_builtins.str] = ...,
    map_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIntegrationAccountMapResult: ...
def get_integration_account_map_output(
    integration_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    map_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIntegrationAccountMapResult]: ...
