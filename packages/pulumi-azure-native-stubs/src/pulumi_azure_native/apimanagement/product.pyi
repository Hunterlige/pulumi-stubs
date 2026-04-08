import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProductArgs", "Product"]

@pulumi.input_type
class ProductArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        approval_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        product_id: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[ProductState]] = ...,
        subscription_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        subscriptions_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        terms: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="approvalRequired")
    def approval_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @approval_required.setter
    def approval_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[ProductState]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[ProductState]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionRequired")
    def subscription_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @subscription_required.setter
    def subscription_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionsLimit")
    def subscriptions_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @subscriptions_limit.setter
    def subscriptions_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def terms(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @terms.setter
    def terms(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:apimanagement:Product")
class Product(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        approval_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        product_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[ProductState]] = ...,
        subscription_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        subscriptions_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        terms: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProductArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Product: ...
    @_builtins.property
    @pulumi.getter(name="approvalRequired")
    def approval_required(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionRequired")
    def subscription_required(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionsLimit")
    def subscriptions_limit(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def terms(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
