

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEmailIdentityResult', 'AwaitableGetEmailIdentityResult', 'get_email_identity', 'get_email_identity_output']
@pulumi.output_type
class GetEmailIdentityResult:
    
    def __init__(__self__, arn=..., configuration_set_name=..., dkim_signing_attributes=..., email_identity=..., id=..., identity_type=..., region=..., tags=..., verification_status=..., verified_for_sending_status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dkimSigningAttributes")
    def dkim_signing_attributes(self) -> Sequence[outputs.GetEmailIdentityDkimSigningAttributeResult]:
        
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
    @pulumi.getter(name="identityType")
    def identity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verificationStatus")
    def verification_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedForSendingStatus")
    def verified_for_sending_status(self) -> _builtins.bool:
        
        ...
    


class AwaitableGetEmailIdentityResult(GetEmailIdentityResult):
    def __await__(self): # -> Generator[Never, Any, GetEmailIdentityResult]:
        ...
    


def get_email_identity(email_identity: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEmailIdentityResult:
    
    ...

def get_email_identity_output(email_identity: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEmailIdentityResult]:
    
    ...

