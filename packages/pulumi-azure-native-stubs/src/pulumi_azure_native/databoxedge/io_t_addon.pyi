

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IoTAddonArgs', 'IoTAddon']
@pulumi.input_type
class IoTAddonArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], io_t_device_details: pulumi.Input[IoTDeviceInfoArgs], io_t_edge_device_details: pulumi.Input[IoTDeviceInfoArgs], kind: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], role_name: pulumi.Input[_builtins.str], addon_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ioTDeviceDetails")
    def io_t_device_details(self) -> pulumi.Input[IoTDeviceInfoArgs]:
        
        ...
    
    @io_t_device_details.setter
    def io_t_device_details(self, value: pulumi.Input[IoTDeviceInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ioTEdgeDeviceDetails")
    def io_t_edge_device_details(self) -> pulumi.Input[IoTDeviceInfoArgs]:
        
        ...
    
    @io_t_edge_device_details.setter
    def io_t_edge_device_details(self, value: pulumi.Input[IoTDeviceInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_name.setter
    def role_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @addon_name.setter
    def addon_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:databoxedge:IoTAddon")
class IoTAddon(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., addon_name: Optional[pulumi.Input[_builtins.str]] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., io_t_device_details: Optional[pulumi.Input[Union[IoTDeviceInfoArgs, IoTDeviceInfoArgsDict]]] = ..., io_t_edge_device_details: Optional[pulumi.Input[Union[IoTDeviceInfoArgs, IoTDeviceInfoArgsDict]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., role_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IoTAddonArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> IoTAddon:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ioTDeviceDetails")
    def io_t_device_details(self) -> pulumi.Output[outputs.IoTDeviceInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ioTEdgeDeviceDetails")
    def io_t_edge_device_details(self) -> pulumi.Output[outputs.IoTDeviceInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
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
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


