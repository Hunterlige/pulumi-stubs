import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSkusNestedResourceTypeThirdResult",
    "AwaitableGetSkusNestedResourceTypeThirdResult",
    "get_skus_nested_resource_type_third",
    "get_skus_nested_resource_type_third_output",
]

@pulumi.output_type
class GetSkusNestedResourceTypeThirdResult:
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
    def properties(self) -> outputs.SkuResourcePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSkusNestedResourceTypeThirdResult(
    GetSkusNestedResourceTypeThirdResult
):
    def __await__(self): ...

def get_skus_nested_resource_type_third(
    nested_resource_type_first: Optional[_builtins.str] = ...,
    nested_resource_type_second: Optional[_builtins.str] = ...,
    nested_resource_type_third: Optional[_builtins.str] = ...,
    provider_namespace: Optional[_builtins.str] = ...,
    resource_type: Optional[_builtins.str] = ...,
    sku: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSkusNestedResourceTypeThirdResult: ...
def get_skus_nested_resource_type_third_output(
    nested_resource_type_first: Optional[pulumi.Input[_builtins.str]] = ...,
    nested_resource_type_second: Optional[pulumi.Input[_builtins.str]] = ...,
    nested_resource_type_third: Optional[pulumi.Input[_builtins.str]] = ...,
    provider_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    sku: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSkusNestedResourceTypeThirdResult]: ...
