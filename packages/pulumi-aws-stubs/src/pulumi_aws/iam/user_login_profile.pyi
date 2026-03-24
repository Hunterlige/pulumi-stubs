

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UserLoginProfileArgs', 'UserLoginProfile']
@pulumi.input_type
class UserLoginProfileArgs:
    def __init__(__self__, *, user: pulumi.Input[_builtins.str], password_length: Optional[pulumi.Input[_builtins.int]] = ..., password_reset_required: Optional[pulumi.Input[_builtins.bool]] = ..., pgp_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user.setter
    def user(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordLength")
    def password_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @password_length.setter
    def password_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordResetRequired")
    def password_reset_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @password_reset_required.setter
    def password_reset_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _UserLoginProfileState:
    def __init__(__self__, *, encrypted_password: Optional[pulumi.Input[_builtins.str]] = ..., key_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., password_length: Optional[pulumi.Input[_builtins.int]] = ..., password_reset_required: Optional[pulumi.Input[_builtins.bool]] = ..., pgp_key: Optional[pulumi.Input[_builtins.str]] = ..., user: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedPassword")
    def encrypted_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encrypted_password.setter
    def encrypted_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_fingerprint.setter
    def key_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordLength")
    def password_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @password_length.setter
    def password_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordResetRequired")
    def password_reset_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @password_reset_required.setter
    def password_reset_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:iam/userLoginProfile:UserLoginProfile")
class UserLoginProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., password_length: Optional[pulumi.Input[_builtins.int]] = ..., password_reset_required: Optional[pulumi.Input[_builtins.bool]] = ..., pgp_key: Optional[pulumi.Input[_builtins.str]] = ..., user: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserLoginProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., encrypted_password: Optional[pulumi.Input[_builtins.str]] = ..., key_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., password_length: Optional[pulumi.Input[_builtins.int]] = ..., password_reset_required: Optional[pulumi.Input[_builtins.bool]] = ..., pgp_key: Optional[pulumi.Input[_builtins.str]] = ..., user: Optional[pulumi.Input[_builtins.str]] = ...) -> UserLoginProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedPassword")
    def encrypted_password(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordLength")
    def password_length(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordResetRequired")
    def password_reset_required(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


