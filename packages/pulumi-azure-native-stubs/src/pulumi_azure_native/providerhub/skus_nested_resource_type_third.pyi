import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SkusNestedResourceTypeThirdArgs", "SkusNestedResourceTypeThird"]

@pulumi.input_type
class SkusNestedResourceTypeThirdArgs:
    def __init__(
        __self__,
        *,
        nested_resource_type_first: pulumi.Input[_builtins.str],
        nested_resource_type_second: pulumi.Input[_builtins.str],
        nested_resource_type_third: pulumi.Input[_builtins.str],
        provider_namespace: pulumi.Input[_builtins.str],
        resource_type: pulumi.Input[_builtins.str],
        properties: Optional[pulumi.Input[SkuResourcePropertiesArgs]] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nestedResourceTypeFirst")
    def nested_resource_type_first(self) -> pulumi.Input[_builtins.str]: ...
    @nested_resource_type_first.setter
    def nested_resource_type_first(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nestedResourceTypeSecond")
    def nested_resource_type_second(self) -> pulumi.Input[_builtins.str]: ...
    @nested_resource_type_second.setter
    def nested_resource_type_second(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nestedResourceTypeThird")
    def nested_resource_type_third(self) -> pulumi.Input[_builtins.str]: ...
    @nested_resource_type_third.setter
    def nested_resource_type_third(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="providerNamespace")
    def provider_namespace(self) -> pulumi.Input[_builtins.str]: ...
    @provider_namespace.setter
    def provider_namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[SkuResourcePropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[SkuResourcePropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class SkusNestedResourceTypeThird(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        nested_resource_type_first: Optional[pulumi.Input[_builtins.str]] = ...,
        nested_resource_type_second: Optional[pulumi.Input[_builtins.str]] = ...,
        nested_resource_type_third: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[SkuResourcePropertiesArgs, SkuResourcePropertiesArgsDict]
            ]
        ] = ...,
        provider_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SkusNestedResourceTypeThirdArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SkusNestedResourceTypeThird: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.SkuResourcePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
