

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIoTRoleResult', 'AwaitableGetIoTRoleResult', 'get_io_t_role', 'get_io_t_role_output']
@pulumi.output_type
class GetIoTRoleResult:
    
    def __init__(__self__, azure_api_version=..., compute_resource=..., host_platform=..., host_platform_type=..., id=..., io_t_device_details=..., io_t_edge_agent_info=..., io_t_edge_device_details=..., kind=..., name=..., role_status=..., share_mappings=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeResource")
    def compute_resource(self) -> Optional[outputs.ComputeResourceResponse]:
        
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
    @pulumi.getter(name="ioTEdgeAgentInfo")
    def io_t_edge_agent_info(self) -> Optional[outputs.IoTEdgeAgentInfoResponse]:
        
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
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareMappings")
    def share_mappings(self) -> Optional[Sequence[outputs.MountPointMapResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIoTRoleResult(GetIoTRoleResult):
    def __await__(self): # -> Generator[Never, Any, GetIoTRoleResult]:
        ...
    


def get_io_t_role(device_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIoTRoleResult:
    
    ...

def get_io_t_role_output(device_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIoTRoleResult]:
    
    ...

