

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LogDeliveryDestinationPolicyArgs', 'LogDeliveryDestinationPolicy']
@pulumi.input_type
class LogDeliveryDestinationPolicyArgs:
    def __init__(__self__, *, delivery_destination_name: pulumi.Input[_builtins.str], delivery_destination_policy: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryDestinationName")
    def delivery_destination_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @delivery_destination_name.setter
    def delivery_destination_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryDestinationPolicy")
    def delivery_destination_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @delivery_destination_policy.setter
    def delivery_destination_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _LogDeliveryDestinationPolicyState:
    def __init__(__self__, *, delivery_destination_name: Optional[pulumi.Input[_builtins.str]] = ..., delivery_destination_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryDestinationName")
    def delivery_destination_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delivery_destination_name.setter
    def delivery_destination_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryDestinationPolicy")
    def delivery_destination_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delivery_destination_policy.setter
    def delivery_destination_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class LogDeliveryDestinationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., delivery_destination_name: Optional[pulumi.Input[_builtins.str]] = ..., delivery_destination_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LogDeliveryDestinationPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., delivery_destination_name: Optional[pulumi.Input[_builtins.str]] = ..., delivery_destination_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> LogDeliveryDestinationPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryDestinationName")
    def delivery_destination_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryDestinationPolicy")
    def delivery_destination_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


