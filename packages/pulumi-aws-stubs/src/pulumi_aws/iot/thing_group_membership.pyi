

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ThingGroupMembershipArgs', 'ThingGroupMembership']
@pulumi.input_type
class ThingGroupMembershipArgs:
    def __init__(__self__, *, thing_group_name: pulumi.Input[_builtins.str], thing_name: pulumi.Input[_builtins.str], override_dynamic_group: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingGroupName")
    def thing_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @thing_group_name.setter
    def thing_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingName")
    def thing_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @thing_name.setter
    def thing_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideDynamicGroup")
    def override_dynamic_group(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @override_dynamic_group.setter
    def override_dynamic_group(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ThingGroupMembershipState:
    def __init__(__self__, *, override_dynamic_group: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., thing_group_name: Optional[pulumi.Input[_builtins.str]] = ..., thing_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideDynamicGroup")
    def override_dynamic_group(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @override_dynamic_group.setter
    def override_dynamic_group(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingGroupName")
    def thing_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @thing_group_name.setter
    def thing_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingName")
    def thing_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @thing_name.setter
    def thing_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:iot/thingGroupMembership:ThingGroupMembership")
class ThingGroupMembership(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., override_dynamic_group: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., thing_group_name: Optional[pulumi.Input[_builtins.str]] = ..., thing_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ThingGroupMembershipArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., override_dynamic_group: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., thing_group_name: Optional[pulumi.Input[_builtins.str]] = ..., thing_name: Optional[pulumi.Input[_builtins.str]] = ...) -> ThingGroupMembership:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideDynamicGroup")
    def override_dynamic_group(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingGroupName")
    def thing_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingName")
    def thing_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


