

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BillingRoleAssignmentByEnrollmentAccountArgs', 'BillingRoleAssignmentByEnrollmentAccount']
@pulumi.input_type
class BillingRoleAssignmentByEnrollmentAccountArgs:
    def __init__(__self__, *, billing_account_name: pulumi.Input[_builtins.str], enrollment_account_name: pulumi.Input[_builtins.str], billing_role_assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[BillingRoleAssignmentPropertiesArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountName")
    def billing_account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @billing_account_name.setter
    def billing_account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enrollmentAccountName")
    def enrollment_account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @enrollment_account_name.setter
    def enrollment_account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingRoleAssignmentName")
    def billing_role_assignment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @billing_role_assignment_name.setter
    def billing_role_assignment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[BillingRoleAssignmentPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[BillingRoleAssignmentPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class BillingRoleAssignmentByEnrollmentAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., billing_account_name: Optional[pulumi.Input[_builtins.str]] = ..., billing_role_assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., enrollment_account_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[BillingRoleAssignmentPropertiesArgs, BillingRoleAssignmentPropertiesArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BillingRoleAssignmentByEnrollmentAccountArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> BillingRoleAssignmentByEnrollmentAccount:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.BillingRoleAssignmentPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


