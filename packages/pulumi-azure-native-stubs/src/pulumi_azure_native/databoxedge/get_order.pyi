import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetOrderResult", "AwaitableGetOrderResult", "get_order", "get_order_output"]

@pulumi.output_type
class GetOrderResult:
    def __init__(
        __self__,
        azure_api_version=...,
        contact_information=...,
        current_status=...,
        delivery_tracking_info=...,
        id=...,
        kind=...,
        name=...,
        order_history=...,
        order_id=...,
        return_tracking_info=...,
        serial_number=...,
        shipment_type=...,
        shipping_address=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactInformation")
    def contact_information(self) -> outputs.ContactDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="currentStatus")
    def current_status(self) -> outputs.OrderStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="deliveryTrackingInfo")
    def delivery_tracking_info(self) -> Sequence[outputs.TrackingInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="orderHistory")
    def order_history(self) -> Sequence[outputs.OrderStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="orderId")
    def order_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="returnTrackingInfo")
    def return_tracking_info(self) -> Sequence[outputs.TrackingInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shipmentType")
    def shipment_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[outputs.AddressResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetOrderResult(GetOrderResult):
    def __await__(self): ...

def get_order(
    device_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOrderResult: ...
def get_order_output(
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOrderResult]: ...
