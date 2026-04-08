import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetHyperVSiteResult",
    "AwaitableGetHyperVSiteResult",
    "get_hyper_v_site",
    "get_hyper_v_site_output",
]

@pulumi.output_type
class GetHyperVSiteResult:
    def __init__(
        __self__,
        azure_api_version=...,
        e_tag=...,
        id=...,
        location=...,
        name=...,
        properties=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.SitePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetHyperVSiteResult(GetHyperVSiteResult):
    def __await__(self): ...

def get_hyper_v_site(
    resource_group_name: Optional[_builtins.str] = ...,
    site_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetHyperVSiteResult: ...
def get_hyper_v_site_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetHyperVSiteResult]: ...
