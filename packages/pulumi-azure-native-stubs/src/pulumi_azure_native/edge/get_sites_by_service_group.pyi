import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSitesByServiceGroupResult",
    "AwaitableGetSitesByServiceGroupResult",
    "get_sites_by_service_group",
    "get_sites_by_service_group_output",
]

@pulumi.output_type
class GetSitesByServiceGroupResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        properties=...,
        system_data=...,
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
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.SitePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSitesByServiceGroupResult(GetSitesByServiceGroupResult):
    def __await__(self): ...

def get_sites_by_service_group(
    servicegroup_name: Optional[_builtins.str] = ...,
    site_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSitesByServiceGroupResult: ...
def get_sites_by_service_group_output(
    servicegroup_name: Optional[pulumi.Input[_builtins.str]] = ...,
    site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSitesByServiceGroupResult]: ...
