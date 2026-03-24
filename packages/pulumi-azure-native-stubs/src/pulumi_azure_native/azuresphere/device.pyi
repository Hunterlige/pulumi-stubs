

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeviceArgs', 'Device']
@pulumi.input_type
class DeviceArgs:
    def __init__(__self__, *, catalog_name: pulumi.Input[_builtins.str], device_group_name: pulumi.Input[_builtins.str], product_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], device_id: Optional[pulumi.Input[_builtins.str]] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @catalog_name.setter
    def catalog_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceGroupName")
    def device_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_group_name.setter
    def device_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @product_name.setter
    def product_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_id.setter
    def device_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:azuresphere:Device")
class Device(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., catalog_name: Optional[pulumi.Input[_builtins.str]] = ..., device_group_name: Optional[pulumi.Input[_builtins.str]] = ..., device_id: Optional[pulumi.Input[_builtins.str]] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., product_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeviceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Device:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chipSku")
    def chip_sku(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAvailableOsVersion")
    def last_available_os_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastInstalledOsVersion")
    def last_installed_os_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastOsUpdateUtc")
    def last_os_update_utc(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateRequestUtc")
    def last_update_request_utc(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


