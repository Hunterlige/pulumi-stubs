

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WebAppSwiftVirtualNetworkConnectionSlotArgs', 'WebAppSwiftVirtualNetworkConnectionSlot']
@pulumi.input_type
class WebAppSwiftVirtualNetworkConnectionSlotArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], slot: pulumi.Input[_builtins.str], kind: Optional[pulumi.Input[_builtins.str]] = ..., subnet_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., swift_supported: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def slot(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @slot.setter
    def slot(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetResourceId")
    def subnet_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_resource_id.setter
    def subnet_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="swiftSupported")
    def swift_supported(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @swift_supported.setter
    def swift_supported(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class WebAppSwiftVirtualNetworkConnectionSlot(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., slot: Optional[pulumi.Input[_builtins.str]] = ..., subnet_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., swift_supported: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebAppSwiftVirtualNetworkConnectionSlotArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WebAppSwiftVirtualNetworkConnectionSlot:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetResourceId")
    def subnet_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="swiftSupported")
    def swift_supported(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


