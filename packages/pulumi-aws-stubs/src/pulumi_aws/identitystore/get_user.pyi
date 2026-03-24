

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUserResult', 'AwaitableGetUserResult', 'get_user', 'get_user_output']
@pulumi.output_type
class GetUserResult:
    
    def __init__(__self__, addresses=..., alternate_identifier=..., display_name=..., emails=..., external_ids=..., id=..., identity_store_id=..., locale=..., names=..., nickname=..., phone_numbers=..., preferred_language=..., profile_url=..., region=..., timezone=..., title=..., user_id=..., user_name=..., user_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Sequence[outputs.GetUserAddressResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternateIdentifier")
    def alternate_identifier(self) -> Optional[outputs.GetUserAlternateIdentifierResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def emails(self) -> Sequence[outputs.GetUserEmailResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIds")
    def external_ids(self) -> Sequence[outputs.GetUserExternalIdResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locale(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[outputs.GetUserNameResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nickname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(self) -> Sequence[outputs.GetUserPhoneNumberResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredLanguage")
    def preferred_language(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileUrl")
    def profile_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetUserResult(GetUserResult):
    def __await__(self): # -> Generator[Never, Any, GetUserResult]:
        ...
    


def get_user(alternate_identifier: Optional[Union[GetUserAlternateIdentifierArgs, GetUserAlternateIdentifierArgsDict]] = ..., identity_store_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., user_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUserResult:
    
    ...

def get_user_output(alternate_identifier: Optional[pulumi.Input[Optional[Union[GetUserAlternateIdentifierArgs, GetUserAlternateIdentifierArgsDict]]]] = ..., identity_store_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., user_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUserResult]:
    
    ...

