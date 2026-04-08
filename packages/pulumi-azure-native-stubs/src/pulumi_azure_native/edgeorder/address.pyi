import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AddressArgs", "Address"]

@pulumi.input_type
class AddressArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        address_classification: Optional[
            pulumi.Input[Union[_builtins.str, AddressClassification]]
        ] = ...,
        address_name: Optional[pulumi.Input[_builtins.str]] = ...,
        contact_details: Optional[pulumi.Input[ContactDetailsArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        shipping_address: Optional[pulumi.Input[ShippingAddressArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addressClassification")
    def address_classification(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AddressClassification]]]: ...
    @address_classification.setter
    def address_classification(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AddressClassification]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="addressName")
    def address_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_name.setter
    def address_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> Optional[pulumi.Input[ContactDetailsArgs]]: ...
    @contact_details.setter
    def contact_details(self, value: Optional[pulumi.Input[ContactDetailsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input[ShippingAddressArgs]]: ...
    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input[ShippingAddressArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:edgeorder:Address")
class Address(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        address_classification: Optional[
            pulumi.Input[Union[_builtins.str, AddressClassification]]
        ] = ...,
        address_name: Optional[pulumi.Input[_builtins.str]] = ...,
        contact_details: Optional[
            pulumi.Input[Union[ContactDetailsArgs, ContactDetailsArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        shipping_address: Optional[
            pulumi.Input[Union[ShippingAddressArgs, ShippingAddressArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AddressArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Address: ...
    @_builtins.property
    @pulumi.getter(name="addressClassification")
    def address_classification(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="addressValidationStatus")
    def address_validation_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(
        self,
    ) -> pulumi.Output[Optional[outputs.ContactDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(
        self,
    ) -> pulumi.Output[Optional[outputs.ShippingAddressResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
