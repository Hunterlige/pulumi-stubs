

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EncryptionPropertiesIdentityArgs', 'EncryptionPropertiesIdentityArgsDict', 'EncryptionPropertiesArgs', 'EncryptionPropertiesArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']
class EncryptionPropertiesIdentityArgsDict(TypedDict):
    
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, Type]]]


@pulumi.input_type
class EncryptionPropertiesIdentityArgs:
    def __init__(__self__, *, resource_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, Type]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, Type]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, Type]]]): # -> None:
        ...
    


class EncryptionPropertiesArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[EncryptionPropertiesIdentityArgsDict]]
    key_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EncryptionPropertiesArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[EncryptionPropertiesIdentityArgs]] = ..., key_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[EncryptionPropertiesIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[EncryptionPropertiesIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUrl")
    def key_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_url.setter
    def key_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


