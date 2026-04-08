import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDeviceResult",
    "AwaitableGetDeviceResult",
    "get_device",
    "get_device_output",
]

@pulumi.output_type
class GetDeviceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        chip_sku=...,
        device_id=...,
        id=...,
        last_available_os_version=...,
        last_installed_os_version=...,
        last_os_update_utc=...,
        last_update_request_utc=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="chipSku")
    def chip_sku(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastAvailableOsVersion")
    def last_available_os_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastInstalledOsVersion")
    def last_installed_os_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastOsUpdateUtc")
    def last_os_update_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateRequestUtc")
    def last_update_request_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDeviceResult(GetDeviceResult):
    def __await__(self): ...

def get_device(
    catalog_name: Optional[_builtins.str] = ...,
    device_group_name: Optional[_builtins.str] = ...,
    device_name: Optional[_builtins.str] = ...,
    product_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDeviceResult: ...
def get_device_output(
    catalog_name: Optional[pulumi.Input[_builtins.str]] = ...,
    device_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    product_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDeviceResult]: ...
