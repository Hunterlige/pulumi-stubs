import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OrderArgs", "Order"]

@pulumi.input_type
class OrderArgs:
    def __init__(
        __self__,
        *,
        contact_information: pulumi.Input[ContactDetailsArgs],
        device_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        shipment_type: Optional[pulumi.Input[Union[_builtins.str, ShipmentType]]] = ...,
        shipping_address: Optional[pulumi.Input[AddressArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactInformation")
    def contact_information(self) -> pulumi.Input[ContactDetailsArgs]: ...
    @contact_information.setter
    def contact_information(self, value: pulumi.Input[ContactDetailsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]: ...
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="shipmentType")
    def shipment_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ShipmentType]]]: ...
    @shipment_type.setter
    def shipment_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ShipmentType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input[AddressArgs]]: ...
    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input[AddressArgs]]): ...

@pulumi.type_token("azure-native:databoxedge:Order")
class Order(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        contact_information: Optional[
            pulumi.Input[Union[ContactDetailsArgs, ContactDetailsArgsDict]]
        ] = ...,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        shipment_type: Optional[pulumi.Input[Union[_builtins.str, ShipmentType]]] = ...,
        shipping_address: Optional[
            pulumi.Input[Union[AddressArgs, AddressArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OrderArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Order: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactInformation")
    def contact_information(self) -> pulumi.Output[outputs.ContactDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="currentStatus")
    def current_status(self) -> pulumi.Output[outputs.OrderStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryTrackingInfo")
    def delivery_tracking_info(
        self,
    ) -> pulumi.Output[Sequence[outputs.TrackingInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orderHistory")
    def order_history(self) -> pulumi.Output[Sequence[outputs.OrderStatusResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="orderId")
    def order_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="returnTrackingInfo")
    def return_tracking_info(
        self,
    ) -> pulumi.Output[Sequence[outputs.TrackingInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shipmentType")
    def shipment_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> pulumi.Output[Optional[outputs.AddressResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
