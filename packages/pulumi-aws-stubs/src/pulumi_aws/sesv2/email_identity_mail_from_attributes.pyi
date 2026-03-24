

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EmailIdentityMailFromAttributesArgs', 'EmailIdentityMailFromAttributes']
@pulumi.input_type
class EmailIdentityMailFromAttributesArgs:
    def __init__(__self__, *, email_identity: pulumi.Input[_builtins.str], behavior_on_mx_failure: Optional[pulumi.Input[_builtins.str]] = ..., mail_from_domain: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email_identity.setter
    def email_identity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="behaviorOnMxFailure")
    def behavior_on_mx_failure(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @behavior_on_mx_failure.setter
    def behavior_on_mx_failure(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mailFromDomain")
    def mail_from_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mail_from_domain.setter
    def mail_from_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _EmailIdentityMailFromAttributesState:
    def __init__(__self__, *, behavior_on_mx_failure: Optional[pulumi.Input[_builtins.str]] = ..., email_identity: Optional[pulumi.Input[_builtins.str]] = ..., mail_from_domain: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="behaviorOnMxFailure")
    def behavior_on_mx_failure(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @behavior_on_mx_failure.setter
    def behavior_on_mx_failure(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email_identity.setter
    def email_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mailFromDomain")
    def mail_from_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mail_from_domain.setter
    def mail_from_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class EmailIdentityMailFromAttributes(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., behavior_on_mx_failure: Optional[pulumi.Input[_builtins.str]] = ..., email_identity: Optional[pulumi.Input[_builtins.str]] = ..., mail_from_domain: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EmailIdentityMailFromAttributesArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., behavior_on_mx_failure: Optional[pulumi.Input[_builtins.str]] = ..., email_identity: Optional[pulumi.Input[_builtins.str]] = ..., mail_from_domain: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> EmailIdentityMailFromAttributes:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="behaviorOnMxFailure")
    def behavior_on_mx_failure(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mailFromDomain")
    def mail_from_domain(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


