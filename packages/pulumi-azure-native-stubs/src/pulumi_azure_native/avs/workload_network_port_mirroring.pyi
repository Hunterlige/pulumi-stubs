

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkloadNetworkPortMirroringArgs', 'WorkloadNetworkPortMirroring']
@pulumi.input_type
class WorkloadNetworkPortMirroringArgs:
    def __init__(__self__, *, private_cloud_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], destination: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[Union[_builtins.str, PortMirroringDirectionEnum]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., port_mirroring_id: Optional[pulumi.Input[_builtins.str]] = ..., revision: Optional[pulumi.Input[_builtins.float]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[Union[_builtins.str, PortMirroringDirectionEnum]]]:
        
        ...
    
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[Union[_builtins.str, PortMirroringDirectionEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portMirroringId")
    def port_mirroring_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @port_mirroring_id.setter
    def port_mirroring_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:avs:WorkloadNetworkPortMirroring")
class WorkloadNetworkPortMirroring(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[Union[_builtins.str, PortMirroringDirectionEnum]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., port_mirroring_id: Optional[pulumi.Input[_builtins.str]] = ..., private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., revision: Optional[pulumi.Input[_builtins.float]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkloadNetworkPortMirroringArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WorkloadNetworkPortMirroring:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter
    def revision(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


