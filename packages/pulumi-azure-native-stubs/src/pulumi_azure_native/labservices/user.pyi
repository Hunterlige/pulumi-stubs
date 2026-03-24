

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UserArgs', 'User']
@pulumi.input_type
class UserArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], lab_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], additional_usage_quota: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labName")
    def lab_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lab_name.setter
    def lab_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalUsageQuota")
    def additional_usage_quota(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @additional_usage_quota.setter
    def additional_usage_quota(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:labservices:User")
class User(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_usage_quota: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., lab_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> User:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalUsageQuota")
    def additional_usage_quota(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitationSent")
    def invitation_sent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitationState")
    def invitation_state(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="registrationState")
    def registration_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceOperationError")
    def resource_operation_error(self) -> pulumi.Output[outputs.ResourceOperationErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalUsage")
    def total_usage(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


