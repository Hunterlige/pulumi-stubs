

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEmailIdentityMailFromAttributesResult', 'AwaitableGetEmailIdentityMailFromAttributesResult', 'get_email_identity_mail_from_attributes', 'get_email_identity_mail_from_attributes_output']
@pulumi.output_type
class GetEmailIdentityMailFromAttributesResult:
    
    def __init__(__self__, behavior_on_mx_failure=..., email_identity=..., id=..., mail_from_domain=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="behaviorOnMxFailure")
    def behavior_on_mx_failure(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mailFromDomain")
    def mail_from_domain(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetEmailIdentityMailFromAttributesResult(GetEmailIdentityMailFromAttributesResult):
    def __await__(self): # -> Generator[Never, Any, GetEmailIdentityMailFromAttributesResult]:
        ...
    


def get_email_identity_mail_from_attributes(email_identity: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEmailIdentityMailFromAttributesResult:
    
    ...

def get_email_identity_mail_from_attributes_output(email_identity: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEmailIdentityMailFromAttributesResult]:
    
    ...

