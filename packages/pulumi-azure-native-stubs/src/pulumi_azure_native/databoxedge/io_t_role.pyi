

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IoTRoleArgs', 'IoTRole']
@pulumi.input_type
class IoTRoleArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], host_platform: pulumi.Input[Union[_builtins.str, PlatformType]], io_t_device_details: pulumi.Input[IoTDeviceInfoArgs], io_t_edge_device_details: pulumi.Input[IoTDeviceInfoArgs], kind: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], role_status: pulumi.Input[Union[_builtins.str, RoleStatus]], compute_resource: Optional[pulumi.Input[ComputeResourceArgs]] = ..., io_t_edge_agent_info: Optional[pulumi.Input[IoTEdgeAgentInfoArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., share_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[MountPointMapArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> pulumi.Input[Union[_builtins.str, PlatformType]]:
        
        ...
    
    @host_platform.setter
    def host_platform(self, value: pulumi.Input[Union[_builtins.str, PlatformType]]): # -> None:
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
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> pulumi.Input[Union[_builtins.str, RoleStatus]]:
        
        ...
    
    @role_status.setter
    def role_status(self, value: pulumi.Input[Union[_builtins.str, RoleStatus]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeResource")
    def compute_resource(self) -> Optional[pulumi.Input[ComputeResourceArgs]]:
        
        ...
    
    @compute_resource.setter
    def compute_resource(self, value: Optional[pulumi.Input[ComputeResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ioTEdgeAgentInfo")
    def io_t_edge_agent_info(self) -> Optional[pulumi.Input[IoTEdgeAgentInfoArgs]]:
        
        ...
    
    @io_t_edge_agent_info.setter
    def io_t_edge_agent_info(self, value: Optional[pulumi.Input[IoTEdgeAgentInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareMappings")
    def share_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MountPointMapArgs]]]]:
        
        ...
    
    @share_mappings.setter
    def share_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MountPointMapArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:databoxedge:IoTRole")
class IoTRole(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., compute_resource: Optional[pulumi.Input[Union[ComputeResourceArgs, ComputeResourceArgsDict]]] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., host_platform: Optional[pulumi.Input[Union[_builtins.str, PlatformType]]] = ..., io_t_device_details: Optional[pulumi.Input[Union[IoTDeviceInfoArgs, IoTDeviceInfoArgsDict]]] = ..., io_t_edge_agent_info: Optional[pulumi.Input[Union[IoTEdgeAgentInfoArgs, IoTEdgeAgentInfoArgsDict]]] = ..., io_t_edge_device_details: Optional[pulumi.Input[Union[IoTDeviceInfoArgs, IoTDeviceInfoArgsDict]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., role_status: Optional[pulumi.Input[Union[_builtins.str, RoleStatus]]] = ..., share_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MountPointMapArgs, MountPointMapArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IoTRoleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> IoTRole:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeResource")
    def compute_resource(self) -> pulumi.Output[Optional[outputs.ComputeResourceResponse]]:
        
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
    @pulumi.getter(name="ioTEdgeAgentInfo")
    def io_t_edge_agent_info(self) -> pulumi.Output[Optional[outputs.IoTEdgeAgentInfoResponse]]:
        
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
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareMappings")
    def share_mappings(self) -> pulumi.Output[Optional[Sequence[outputs.MountPointMapResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


