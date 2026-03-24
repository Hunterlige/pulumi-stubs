

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LabArgs', 'Lab']
@pulumi.input_type
class LabArgs:
    def __init__(__self__, *, billing_account_name: pulumi.Input[_builtins.str], billing_profile_name: pulumi.Input[_builtins.str], budget_per_student: pulumi.Input[AmountArgs], description: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], expiration_date: pulumi.Input[_builtins.str], invoice_section_name: pulumi.Input[_builtins.str], currency: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountName")
    def billing_account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @billing_account_name.setter
    def billing_account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingProfileName")
    def billing_profile_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @billing_profile_name.setter
    def billing_profile_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="budgetPerStudent")
    def budget_per_student(self) -> pulumi.Input[AmountArgs]:
        
        ...
    
    @budget_per_student.setter
    def budget_per_student(self, value: pulumi.Input[AmountArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expiration_date.setter
    def expiration_date(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invoiceSectionName")
    def invoice_section_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @invoice_section_name.setter
    def invoice_section_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @currency.setter
    def currency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:education:Lab")
class Lab(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., billing_account_name: Optional[pulumi.Input[_builtins.str]] = ..., billing_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., budget_per_student: Optional[pulumi.Input[Union[AmountArgs, AmountArgsDict]]] = ..., currency: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., expiration_date: Optional[pulumi.Input[_builtins.str]] = ..., invoice_section_name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.float]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LabArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Lab:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="budgetPerStudent")
    def budget_per_student(self) -> pulumi.Output[outputs.AmountResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveDate")
    def effective_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitationCode")
    def invitation_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxStudentCount")
    def max_student_count(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalBudget")
    def total_budget(self) -> pulumi.Output[outputs.AmountResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    


