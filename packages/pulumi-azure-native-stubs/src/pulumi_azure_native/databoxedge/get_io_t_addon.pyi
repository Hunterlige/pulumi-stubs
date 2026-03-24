

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIoTAddonResult', 'AwaitableGetIoTAddonResult', 'get_io_t_addon', 'get_io_t_addon_output']
@pulumi.output_type
class GetIoTAddonResult:
    
    def __init__(__self__, azure_api_version=..., host_platform=..., host_platform_type=..., id=..., io_t_device_details=..., io_t_edge_device_details=..., kind=..., name=..., provisioning_state=..., system_data=..., type=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ioTDeviceDetails")
    def io_t_device_details(self) -> outputs.IoTDeviceInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ioTEdgeDeviceDetails")
    def io_t_edge_device_details(self) -> outputs.IoTDeviceInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIoTAddonResult(GetIoTAddonResult):
    def __await__(self): # -> Generator[Never, Any, GetIoTAddonResult]:
        ...
    


def get_io_t_addon(addon_name: Optional[_builtins.str] = ..., device_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., role_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIoTAddonResult:
    
    ...

def get_io_t_addon_output(addon_name: Optional[pulumi.Input[_builtins.str]] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., role_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIoTAddonResult]:
    
    ...

