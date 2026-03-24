

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PhoneNumberContactFlowAssociationArgs', 'PhoneNumberContactFlowAssociation']
@pulumi.input_type
class PhoneNumberContactFlowAssociationArgs:
    def __init__(__self__, *, contact_flow_id: pulumi.Input[_builtins.str], instance_id: pulumi.Input[_builtins.str], phone_number_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactFlowId")
    def contact_flow_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @contact_flow_id.setter
    def contact_flow_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumberId")
    def phone_number_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number_id.setter
    def phone_number_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _PhoneNumberContactFlowAssociationState:
    def __init__(__self__, *, contact_flow_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., phone_number_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactFlowId")
    def contact_flow_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_flow_id.setter
    def contact_flow_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumberId")
    def phone_number_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_number_id.setter
    def phone_number_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class PhoneNumberContactFlowAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., contact_flow_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., phone_number_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PhoneNumberContactFlowAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., contact_flow_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., phone_number_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> PhoneNumberContactFlowAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactFlowId")
    def contact_flow_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumberId")
    def phone_number_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


