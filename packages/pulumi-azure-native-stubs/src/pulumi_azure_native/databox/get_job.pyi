import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetJobResult", "AwaitableGetJobResult", "get_job", "get_job_output"]

@pulumi.output_type
class GetJobResult:
    def __init__(
        __self__,
        all_devices_lost=...,
        azure_api_version=...,
        cancellation_reason=...,
        delayed_stage=...,
        delivery_info=...,
        delivery_type=...,
        details=...,
        error=...,
        id=...,
        identity=...,
        is_cancellable=...,
        is_cancellable_without_fee=...,
        is_deletable=...,
        is_prepare_to_ship_enabled=...,
        is_shipping_address_editable=...,
        location=...,
        name=...,
        reverse_shipping_details_update=...,
        reverse_transport_preference_update=...,
        sku=...,
        start_time=...,
        status=...,
        system_data=...,
        tags=...,
        transfer_type=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allDevicesLost")
    def all_devices_lost(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cancellationReason")
    def cancellation_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="delayedStage")
    def delayed_stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> Optional[outputs.JobDeliveryInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryType")
    def delivery_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.CloudErrorResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ResourceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="isCancellable")
    def is_cancellable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isCancellableWithoutFee")
    def is_cancellable_without_fee(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isDeletable")
    def is_deletable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isPrepareToShipEnabled")
    def is_prepare_to_ship_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isShippingAddressEditable")
    def is_shipping_address_editable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reverseShippingDetailsUpdate")
    def reverse_shipping_details_update(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reverseTransportPreferenceUpdate")
    def reverse_transport_preference_update(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transferType")
    def transfer_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetJobResult(GetJobResult):
    def __await__(self): ...

def get_job(
    expand: Optional[_builtins.str] = ...,
    job_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetJobResult: ...
def get_job_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    job_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetJobResult]: ...
