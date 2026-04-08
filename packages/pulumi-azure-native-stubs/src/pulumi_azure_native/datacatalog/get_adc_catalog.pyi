import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetADCCatalogResult",
    "AwaitableGetADCCatalogResult",
    "get_adc_catalog",
    "get_adc_catalog_output",
]

@pulumi.output_type
class GetADCCatalogResult:
    def __init__(
        __self__,
        admins=...,
        azure_api_version=...,
        enable_automatic_unit_adjustment=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        sku=...,
        successfully_provisioned=...,
        tags=...,
        type=...,
        units=...,
        users=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def admins(self) -> Optional[Sequence[outputs.PrincipalsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUnitAdjustment")
    def enable_automatic_unit_adjustment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="successfullyProvisioned")
    def successfully_provisioned(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def users(self) -> Optional[Sequence[outputs.PrincipalsResponse]]: ...

class AwaitableGetADCCatalogResult(GetADCCatalogResult):
    def __await__(self): ...

def get_adc_catalog(
    catalog_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetADCCatalogResult: ...
def get_adc_catalog_output(
    catalog_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetADCCatalogResult]: ...
