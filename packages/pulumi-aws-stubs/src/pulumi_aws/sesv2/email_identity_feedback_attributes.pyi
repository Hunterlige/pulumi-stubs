

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EmailIdentityFeedbackAttributesArgs', 'EmailIdentityFeedbackAttributes']
@pulumi.input_type
class EmailIdentityFeedbackAttributesArgs:
    def __init__(__self__, *, email_identity: pulumi.Input[_builtins.str], email_forwarding_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email_identity.setter
    def email_identity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailForwardingEnabled")
    def email_forwarding_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @email_forwarding_enabled.setter
    def email_forwarding_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _EmailIdentityFeedbackAttributesState:
    def __init__(__self__, *, email_forwarding_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., email_identity: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailForwardingEnabled")
    def email_forwarding_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @email_forwarding_enabled.setter
    def email_forwarding_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email_identity.setter
    def email_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class EmailIdentityFeedbackAttributes(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., email_forwarding_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., email_identity: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EmailIdentityFeedbackAttributesArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., email_forwarding_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., email_identity: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> EmailIdentityFeedbackAttributes:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailForwardingEnabled")
    def email_forwarding_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


