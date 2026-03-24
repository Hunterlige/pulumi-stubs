

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ProactiveEngagementArgs', 'ProactiveEngagement']
@pulumi.input_type
class ProactiveEngagementArgs:
    def __init__(__self__, *, emergency_contacts: pulumi.Input[Sequence[pulumi.Input[ProactiveEngagementEmergencyContactArgs]]], enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emergencyContacts")
    def emergency_contacts(self) -> pulumi.Input[Sequence[pulumi.Input[ProactiveEngagementEmergencyContactArgs]]]:
        
        ...
    
    @emergency_contacts.setter
    def emergency_contacts(self, value: pulumi.Input[Sequence[pulumi.Input[ProactiveEngagementEmergencyContactArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


@pulumi.input_type
class _ProactiveEngagementState:
    def __init__(__self__, *, emergency_contacts: Optional[pulumi.Input[Sequence[pulumi.Input[ProactiveEngagementEmergencyContactArgs]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emergencyContacts")
    def emergency_contacts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProactiveEngagementEmergencyContactArgs]]]]:
        
        ...
    
    @emergency_contacts.setter
    def emergency_contacts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ProactiveEngagementEmergencyContactArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("aws:shield/proactiveEngagement:ProactiveEngagement")
class ProactiveEngagement(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., emergency_contacts: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ProactiveEngagementEmergencyContactArgs, ProactiveEngagementEmergencyContactArgsDict]]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ProactiveEngagementArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., emergency_contacts: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ProactiveEngagementEmergencyContactArgs, ProactiveEngagementEmergencyContactArgsDict]]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> ProactiveEngagement:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emergencyContacts")
    def emergency_contacts(self) -> pulumi.Output[Sequence[outputs.ProactiveEngagementEmergencyContact]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    


