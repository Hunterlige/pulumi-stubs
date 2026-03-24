

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StandardsControlAssociationArgs', 'StandardsControlAssociation']
@pulumi.input_type
class StandardsControlAssociationArgs:
    def __init__(__self__, *, association_status: pulumi.Input[_builtins.str], security_control_id: pulumi.Input[_builtins.str], standards_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., updated_reason: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationStatus")
    def association_status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @association_status.setter
    def association_status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityControlId")
    def security_control_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @security_control_id.setter
    def security_control_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardsArn")
    def standards_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @standards_arn.setter
    def standards_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedReason")
    def updated_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @updated_reason.setter
    def updated_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _StandardsControlAssociationState:
    def __init__(__self__, *, association_status: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_control_id: Optional[pulumi.Input[_builtins.str]] = ..., standards_arn: Optional[pulumi.Input[_builtins.str]] = ..., updated_reason: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationStatus")
    def association_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @association_status.setter
    def association_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityControlId")
    def security_control_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_control_id.setter
    def security_control_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardsArn")
    def standards_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @standards_arn.setter
    def standards_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedReason")
    def updated_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @updated_reason.setter
    def updated_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class StandardsControlAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., association_status: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_control_id: Optional[pulumi.Input[_builtins.str]] = ..., standards_arn: Optional[pulumi.Input[_builtins.str]] = ..., updated_reason: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StandardsControlAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., association_status: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_control_id: Optional[pulumi.Input[_builtins.str]] = ..., standards_arn: Optional[pulumi.Input[_builtins.str]] = ..., updated_reason: Optional[pulumi.Input[_builtins.str]] = ...) -> StandardsControlAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationStatus")
    def association_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityControlId")
    def security_control_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardsArn")
    def standards_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedReason")
    def updated_reason(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


