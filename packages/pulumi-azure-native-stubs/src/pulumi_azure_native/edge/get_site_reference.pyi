import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSiteReferenceResult",
    "AwaitableGetSiteReferenceResult",
    "get_site_reference",
    "get_site_reference_output",
]

@pulumi.output_type
class GetSiteReferenceResult:
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
    def properties(self) -> outputs.SiteReferencePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSiteReferenceResult(GetSiteReferenceResult):
    def __await__(self): ...

def get_site_reference(
    context_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    site_reference_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSiteReferenceResult: ...
def get_site_reference_output(
    context_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    site_reference_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSiteReferenceResult]: ...
