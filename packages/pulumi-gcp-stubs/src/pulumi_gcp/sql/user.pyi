

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UserArgs', 'User']
@pulumi.input_type
class UserArgs:
    def __init__(__self__, *, instance: pulumi.Input[_builtins.str], database_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., password_policy: Optional[pulumi.Input[UserPasswordPolicyArgs]] = ..., password_wo: Optional[pulumi.Input[_builtins.str]] = ..., password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseRoles")
    def database_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @database_roles.setter
    def database_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordPolicy")
    def password_policy(self) -> Optional[pulumi.Input[UserPasswordPolicyArgs]]:
        ...
    
    @password_policy.setter
    def password_policy(self, value: Optional[pulumi.Input[UserPasswordPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_wo.setter
    def password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @password_wo_version.setter
    def password_wo_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _UserState:
    def __init__(__self__, *, database_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., iam_email: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., password_policy: Optional[pulumi.Input[UserPasswordPolicyArgs]] = ..., password_wo: Optional[pulumi.Input[_builtins.str]] = ..., password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., sql_server_user_details: Optional[pulumi.Input[Sequence[pulumi.Input[UserSqlServerUserDetailArgs]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseRoles")
    def database_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @database_roles.setter
    def database_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamEmail")
    def iam_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_email.setter
    def iam_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordPolicy")
    def password_policy(self) -> Optional[pulumi.Input[UserPasswordPolicyArgs]]:
        ...
    
    @password_policy.setter
    def password_policy(self, value: Optional[pulumi.Input[UserPasswordPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_wo.setter
    def password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @password_wo_version.setter
    def password_wo_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerUserDetails")
    def sql_server_user_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserSqlServerUserDetailArgs]]]]:
        ...
    
    @sql_server_user_details.setter
    def sql_server_user_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserSqlServerUserDetailArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:sql/user:User")
class User(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., database_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., password_policy: Optional[pulumi.Input[Union[UserPasswordPolicyArgs, UserPasswordPolicyArgsDict]]] = ..., password_wo: Optional[pulumi.Input[_builtins.str]] = ..., password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., database_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., iam_email: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., password_policy: Optional[pulumi.Input[Union[UserPasswordPolicyArgs, UserPasswordPolicyArgsDict]]] = ..., password_wo: Optional[pulumi.Input[_builtins.str]] = ..., password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., sql_server_user_details: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UserSqlServerUserDetailArgs, UserSqlServerUserDetailArgsDict]]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> User:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseRoles")
    def database_roles(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamEmail")
    def iam_email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordPolicy")
    def password_policy(self) -> pulumi.Output[Optional[outputs.UserPasswordPolicy]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerUserDetails")
    def sql_server_user_details(self) -> pulumi.Output[Sequence[outputs.UserSqlServerUserDetail]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


