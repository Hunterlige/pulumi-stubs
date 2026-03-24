

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStudentResult', 'AwaitableGetStudentResult', 'get_student', 'get_student_output']
@pulumi.output_type
class GetStudentResult:
    
    def __init__(__self__, azure_api_version=..., budget=..., effective_date=..., email=..., expiration_date=..., first_name=..., id=..., last_name=..., name=..., role=..., status=..., subscription_alias=..., subscription_id=..., subscription_invite_last_sent_date=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def budget(self) -> outputs.AmountResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveDate")
    def effective_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionAlias")
    def subscription_alias(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionInviteLastSentDate")
    def subscription_invite_last_sent_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetStudentResult(GetStudentResult):
    def __await__(self): # -> Generator[Never, Any, GetStudentResult]:
        ...
    


def get_student(billing_account_name: Optional[_builtins.str] = ..., billing_profile_name: Optional[_builtins.str] = ..., invoice_section_name: Optional[_builtins.str] = ..., student_alias: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStudentResult:
    
    ...

def get_student_output(billing_account_name: Optional[pulumi.Input[_builtins.str]] = ..., billing_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., invoice_section_name: Optional[pulumi.Input[_builtins.str]] = ..., student_alias: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStudentResult]:
    
    ...

