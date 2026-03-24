

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountPasswordPolicyArgs', 'AccountPasswordPolicy']
@pulumi.input_type
class AccountPasswordPolicyArgs:
    def __init__(__self__, *, allow_users_to_change_password: Optional[pulumi.Input[_builtins.bool]] = ..., hard_expiry: Optional[pulumi.Input[_builtins.bool]] = ..., max_password_age: Optional[pulumi.Input[_builtins.int]] = ..., minimum_password_length: Optional[pulumi.Input[_builtins.int]] = ..., password_reuse_prevention: Optional[pulumi.Input[_builtins.int]] = ..., require_lowercase_characters: Optional[pulumi.Input[_builtins.bool]] = ..., require_numbers: Optional[pulumi.Input[_builtins.bool]] = ..., require_symbols: Optional[pulumi.Input[_builtins.bool]] = ..., require_uppercase_characters: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowUsersToChangePassword")
    def allow_users_to_change_password(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_users_to_change_password.setter
    def allow_users_to_change_password(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardExpiry")
    def hard_expiry(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @hard_expiry.setter
    def hard_expiry(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPasswordAge")
    def max_password_age(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_password_age.setter
    def max_password_age(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumPasswordLength")
    def minimum_password_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minimum_password_length.setter
    def minimum_password_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordReusePrevention")
    def password_reuse_prevention(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @password_reuse_prevention.setter
    def password_reuse_prevention(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireLowercaseCharacters")
    def require_lowercase_characters(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_lowercase_characters.setter
    def require_lowercase_characters(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireNumbers")
    def require_numbers(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_numbers.setter
    def require_numbers(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireSymbols")
    def require_symbols(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_symbols.setter
    def require_symbols(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireUppercaseCharacters")
    def require_uppercase_characters(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_uppercase_characters.setter
    def require_uppercase_characters(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _AccountPasswordPolicyState:
    def __init__(__self__, *, allow_users_to_change_password: Optional[pulumi.Input[_builtins.bool]] = ..., expire_passwords: Optional[pulumi.Input[_builtins.bool]] = ..., hard_expiry: Optional[pulumi.Input[_builtins.bool]] = ..., max_password_age: Optional[pulumi.Input[_builtins.int]] = ..., minimum_password_length: Optional[pulumi.Input[_builtins.int]] = ..., password_reuse_prevention: Optional[pulumi.Input[_builtins.int]] = ..., require_lowercase_characters: Optional[pulumi.Input[_builtins.bool]] = ..., require_numbers: Optional[pulumi.Input[_builtins.bool]] = ..., require_symbols: Optional[pulumi.Input[_builtins.bool]] = ..., require_uppercase_characters: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowUsersToChangePassword")
    def allow_users_to_change_password(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_users_to_change_password.setter
    def allow_users_to_change_password(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirePasswords")
    def expire_passwords(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @expire_passwords.setter
    def expire_passwords(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardExpiry")
    def hard_expiry(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @hard_expiry.setter
    def hard_expiry(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPasswordAge")
    def max_password_age(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_password_age.setter
    def max_password_age(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumPasswordLength")
    def minimum_password_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minimum_password_length.setter
    def minimum_password_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordReusePrevention")
    def password_reuse_prevention(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @password_reuse_prevention.setter
    def password_reuse_prevention(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireLowercaseCharacters")
    def require_lowercase_characters(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_lowercase_characters.setter
    def require_lowercase_characters(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireNumbers")
    def require_numbers(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_numbers.setter
    def require_numbers(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireSymbols")
    def require_symbols(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_symbols.setter
    def require_symbols(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireUppercaseCharacters")
    def require_uppercase_characters(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_uppercase_characters.setter
    def require_uppercase_characters(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AccountPasswordPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_users_to_change_password: Optional[pulumi.Input[_builtins.bool]] = ..., hard_expiry: Optional[pulumi.Input[_builtins.bool]] = ..., max_password_age: Optional[pulumi.Input[_builtins.int]] = ..., minimum_password_length: Optional[pulumi.Input[_builtins.int]] = ..., password_reuse_prevention: Optional[pulumi.Input[_builtins.int]] = ..., require_lowercase_characters: Optional[pulumi.Input[_builtins.bool]] = ..., require_numbers: Optional[pulumi.Input[_builtins.bool]] = ..., require_symbols: Optional[pulumi.Input[_builtins.bool]] = ..., require_uppercase_characters: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[AccountPasswordPolicyArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allow_users_to_change_password: Optional[pulumi.Input[_builtins.bool]] = ..., expire_passwords: Optional[pulumi.Input[_builtins.bool]] = ..., hard_expiry: Optional[pulumi.Input[_builtins.bool]] = ..., max_password_age: Optional[pulumi.Input[_builtins.int]] = ..., minimum_password_length: Optional[pulumi.Input[_builtins.int]] = ..., password_reuse_prevention: Optional[pulumi.Input[_builtins.int]] = ..., require_lowercase_characters: Optional[pulumi.Input[_builtins.bool]] = ..., require_numbers: Optional[pulumi.Input[_builtins.bool]] = ..., require_symbols: Optional[pulumi.Input[_builtins.bool]] = ..., require_uppercase_characters: Optional[pulumi.Input[_builtins.bool]] = ...) -> AccountPasswordPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowUsersToChangePassword")
    def allow_users_to_change_password(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirePasswords")
    def expire_passwords(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardExpiry")
    def hard_expiry(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPasswordAge")
    def max_password_age(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumPasswordLength")
    def minimum_password_length(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordReusePrevention")
    def password_reuse_prevention(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireLowercaseCharacters")
    def require_lowercase_characters(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireNumbers")
    def require_numbers(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireSymbols")
    def require_symbols(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireUppercaseCharacters")
    def require_uppercase_characters(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    


