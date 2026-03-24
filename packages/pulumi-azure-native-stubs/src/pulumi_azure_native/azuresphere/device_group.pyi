

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
__all__ = ['DeviceGroupArgs', 'DeviceGroup']
@pulumi.input_type
class DeviceGroupArgs:
    def __init__(__self__, *, catalog_name: pulumi.Input[_builtins.str], product_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], allow_crash_dumps_collection: Optional[pulumi.Input[Union[_builtins.str, AllowCrashDumpCollection]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., device_group_name: Optional[pulumi.Input[_builtins.str]] = ..., os_feed_type: Optional[pulumi.Input[Union[_builtins.str, OSFeedType]]] = ..., regional_data_boundary: Optional[pulumi.Input[Union[_builtins.str, RegionalDataBoundary]]] = ..., update_policy: Optional[pulumi.Input[Union[_builtins.str, UpdatePolicy]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @catalog_name.setter
    def catalog_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="allowCrashDumpsCollection")
    def allow_crash_dumps_collection(self) -> Optional[pulumi.Input[Union[_builtins.str, AllowCrashDumpCollection]]]:
        
        ...
    
    @allow_crash_dumps_collection.setter
    def allow_crash_dumps_collection(self, value: Optional[pulumi.Input[Union[_builtins.str, AllowCrashDumpCollection]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceGroupName")
    def device_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_group_name.setter
    def device_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osFeedType")
    def os_feed_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OSFeedType]]]:
        
        ...
    
    @os_feed_type.setter
    def os_feed_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OSFeedType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalDataBoundary")
    def regional_data_boundary(self) -> Optional[pulumi.Input[Union[_builtins.str, RegionalDataBoundary]]]:
        
        ...
    
    @regional_data_boundary.setter
    def regional_data_boundary(self, value: Optional[pulumi.Input[Union[_builtins.str, RegionalDataBoundary]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatePolicy")
    def update_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, UpdatePolicy]]]:
        
        ...
    
    @update_policy.setter
    def update_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, UpdatePolicy]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:azuresphere:DeviceGroup")
class DeviceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_crash_dumps_collection: Optional[pulumi.Input[Union[_builtins.str, AllowCrashDumpCollection]]] = ..., catalog_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., device_group_name: Optional[pulumi.Input[_builtins.str]] = ..., os_feed_type: Optional[pulumi.Input[Union[_builtins.str, OSFeedType]]] = ..., product_name: Optional[pulumi.Input[_builtins.str]] = ..., regional_data_boundary: Optional[pulumi.Input[Union[_builtins.str, RegionalDataBoundary]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., update_policy: Optional[pulumi.Input[Union[_builtins.str, UpdatePolicy]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeviceGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DeviceGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCrashDumpsCollection")
    def allow_crash_dumps_collection(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasDeployment")
    def has_deployment(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osFeedType")
    def os_feed_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalDataBoundary")
    def regional_data_boundary(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="updatePolicy")
    def update_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


