

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ServiceSpecificCredentialArgs', 'ServiceSpecificCredential']
@pulumi.input_type
class ServiceSpecificCredentialArgs:
    def __init__(__self__, *, service_name: pulumi.Input[_builtins.str], user_name: pulumi.Input[_builtins.str], credential_age_days: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialAgeDays")
    def credential_age_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @credential_age_days.setter
    def credential_age_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ServiceSpecificCredentialState:
    def __init__(__self__, *, create_date: Optional[pulumi.Input[_builtins.str]] = ..., credential_age_days: Optional[pulumi.Input[_builtins.int]] = ..., expiration_date: Optional[pulumi.Input[_builtins.str]] = ..., service_credential_alias: Optional[pulumi.Input[_builtins.str]] = ..., service_credential_secret: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., service_password: Optional[pulumi.Input[_builtins.str]] = ..., service_specific_credential_id: Optional[pulumi.Input[_builtins.str]] = ..., service_user_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_date.setter
    def create_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialAgeDays")
    def credential_age_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @credential_age_days.setter
    def credential_age_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCredentialAlias")
    def service_credential_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_credential_alias.setter
    def service_credential_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCredentialSecret")
    def service_credential_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_credential_secret.setter
    def service_credential_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePassword")
    def service_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_password.setter
    def service_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceSpecificCredentialId")
    def service_specific_credential_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_specific_credential_id.setter
    def service_specific_credential_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUserName")
    def service_user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_user_name.setter
    def service_user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ServiceSpecificCredential(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., credential_age_days: Optional[pulumi.Input[_builtins.int]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServiceSpecificCredentialArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_date: Optional[pulumi.Input[_builtins.str]] = ..., credential_age_days: Optional[pulumi.Input[_builtins.int]] = ..., expiration_date: Optional[pulumi.Input[_builtins.str]] = ..., service_credential_alias: Optional[pulumi.Input[_builtins.str]] = ..., service_credential_secret: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., service_password: Optional[pulumi.Input[_builtins.str]] = ..., service_specific_credential_id: Optional[pulumi.Input[_builtins.str]] = ..., service_user_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> ServiceSpecificCredential:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialAgeDays")
    def credential_age_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCredentialAlias")
    def service_credential_alias(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCredentialSecret")
    def service_credential_secret(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePassword")
    def service_password(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceSpecificCredentialId")
    def service_specific_credential_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUserName")
    def service_user_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


