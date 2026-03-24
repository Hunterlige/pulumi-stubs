

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HciEdgeDeviceJobArgs', 'HciEdgeDeviceJob']
@pulumi.input_type
class HciEdgeDeviceJobArgs:
    def __init__(__self__, *, edge_device_name: pulumi.Input[_builtins.str], kind: pulumi.Input[_builtins.str], properties: pulumi.Input[Union[HciCollectLogJobPropertiesArgs, HciRemoteSupportJobPropertiesArgs]], resource_uri: pulumi.Input[_builtins.str], jobs_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeDeviceName")
    def edge_device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @edge_device_name.setter
    def edge_device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union[HciCollectLogJobPropertiesArgs, HciRemoteSupportJobPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[Union[HciCollectLogJobPropertiesArgs, HciRemoteSupportJobPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobsName")
    def jobs_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @jobs_name.setter
    def jobs_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:azurestackhci:HciEdgeDeviceJob")
class HciEdgeDeviceJob(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., edge_device_name: Optional[pulumi.Input[_builtins.str]] = ..., jobs_name: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[Union[HciCollectLogJobPropertiesArgs, HciCollectLogJobPropertiesArgsDict], Union[HciRemoteSupportJobPropertiesArgs, HciRemoteSupportJobPropertiesArgsDict]]]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HciEdgeDeviceJobArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> HciEdgeDeviceJob:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


