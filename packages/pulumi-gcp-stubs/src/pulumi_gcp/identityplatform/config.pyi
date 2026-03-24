

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
__all__ = ['ConfigArgs', 'Config']
@pulumi.input_type
class ConfigArgs:
    def __init__(__self__, *, authorized_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., autodelete_anonymous_users: Optional[pulumi.Input[_builtins.bool]] = ..., blocking_functions: Optional[pulumi.Input[ConfigBlockingFunctionsArgs]] = ..., client: Optional[pulumi.Input[ConfigClientArgs]] = ..., mfa: Optional[pulumi.Input[ConfigMfaArgs]] = ..., monitoring: Optional[pulumi.Input[ConfigMonitoringArgs]] = ..., multi_tenant: Optional[pulumi.Input[ConfigMultiTenantArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., quota: Optional[pulumi.Input[ConfigQuotaArgs]] = ..., sign_in: Optional[pulumi.Input[ConfigSignInArgs]] = ..., sms_region_config: Optional[pulumi.Input[ConfigSmsRegionConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedDomains")
    def authorized_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authorized_domains.setter
    def authorized_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autodeleteAnonymousUsers")
    def autodelete_anonymous_users(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @autodelete_anonymous_users.setter
    def autodelete_anonymous_users(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockingFunctions")
    def blocking_functions(self) -> Optional[pulumi.Input[ConfigBlockingFunctionsArgs]]:
        
        ...
    
    @blocking_functions.setter
    def blocking_functions(self, value: Optional[pulumi.Input[ConfigBlockingFunctionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[ConfigClientArgs]]:
        
        ...
    
    @client.setter
    def client(self, value: Optional[pulumi.Input[ConfigClientArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mfa(self) -> Optional[pulumi.Input[ConfigMfaArgs]]:
        
        ...
    
    @mfa.setter
    def mfa(self, value: Optional[pulumi.Input[ConfigMfaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[ConfigMonitoringArgs]]:
        
        ...
    
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[ConfigMonitoringArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiTenant")
    def multi_tenant(self) -> Optional[pulumi.Input[ConfigMultiTenantArgs]]:
        
        ...
    
    @multi_tenant.setter
    def multi_tenant(self, value: Optional[pulumi.Input[ConfigMultiTenantArgs]]): # -> None:
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
    def quota(self) -> Optional[pulumi.Input[ConfigQuotaArgs]]:
        
        ...
    
    @quota.setter
    def quota(self, value: Optional[pulumi.Input[ConfigQuotaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signIn")
    def sign_in(self) -> Optional[pulumi.Input[ConfigSignInArgs]]:
        
        ...
    
    @sign_in.setter
    def sign_in(self, value: Optional[pulumi.Input[ConfigSignInArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smsRegionConfig")
    def sms_region_config(self) -> Optional[pulumi.Input[ConfigSmsRegionConfigArgs]]:
        
        ...
    
    @sms_region_config.setter
    def sms_region_config(self, value: Optional[pulumi.Input[ConfigSmsRegionConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ConfigState:
    def __init__(__self__, *, authorized_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., autodelete_anonymous_users: Optional[pulumi.Input[_builtins.bool]] = ..., blocking_functions: Optional[pulumi.Input[ConfigBlockingFunctionsArgs]] = ..., client: Optional[pulumi.Input[ConfigClientArgs]] = ..., mfa: Optional[pulumi.Input[ConfigMfaArgs]] = ..., monitoring: Optional[pulumi.Input[ConfigMonitoringArgs]] = ..., multi_tenant: Optional[pulumi.Input[ConfigMultiTenantArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., quota: Optional[pulumi.Input[ConfigQuotaArgs]] = ..., sign_in: Optional[pulumi.Input[ConfigSignInArgs]] = ..., sms_region_config: Optional[pulumi.Input[ConfigSmsRegionConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedDomains")
    def authorized_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authorized_domains.setter
    def authorized_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autodeleteAnonymousUsers")
    def autodelete_anonymous_users(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @autodelete_anonymous_users.setter
    def autodelete_anonymous_users(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockingFunctions")
    def blocking_functions(self) -> Optional[pulumi.Input[ConfigBlockingFunctionsArgs]]:
        
        ...
    
    @blocking_functions.setter
    def blocking_functions(self, value: Optional[pulumi.Input[ConfigBlockingFunctionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[ConfigClientArgs]]:
        
        ...
    
    @client.setter
    def client(self, value: Optional[pulumi.Input[ConfigClientArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mfa(self) -> Optional[pulumi.Input[ConfigMfaArgs]]:
        
        ...
    
    @mfa.setter
    def mfa(self, value: Optional[pulumi.Input[ConfigMfaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[ConfigMonitoringArgs]]:
        
        ...
    
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[ConfigMonitoringArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiTenant")
    def multi_tenant(self) -> Optional[pulumi.Input[ConfigMultiTenantArgs]]:
        
        ...
    
    @multi_tenant.setter
    def multi_tenant(self, value: Optional[pulumi.Input[ConfigMultiTenantArgs]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[ConfigQuotaArgs]]:
        
        ...
    
    @quota.setter
    def quota(self, value: Optional[pulumi.Input[ConfigQuotaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signIn")
    def sign_in(self) -> Optional[pulumi.Input[ConfigSignInArgs]]:
        
        ...
    
    @sign_in.setter
    def sign_in(self, value: Optional[pulumi.Input[ConfigSignInArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smsRegionConfig")
    def sms_region_config(self) -> Optional[pulumi.Input[ConfigSmsRegionConfigArgs]]:
        
        ...
    
    @sms_region_config.setter
    def sms_region_config(self, value: Optional[pulumi.Input[ConfigSmsRegionConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:identityplatform/config:Config")
class Config(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authorized_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., autodelete_anonymous_users: Optional[pulumi.Input[_builtins.bool]] = ..., blocking_functions: Optional[pulumi.Input[Union[ConfigBlockingFunctionsArgs, ConfigBlockingFunctionsArgsDict]]] = ..., client: Optional[pulumi.Input[Union[ConfigClientArgs, ConfigClientArgsDict]]] = ..., mfa: Optional[pulumi.Input[Union[ConfigMfaArgs, ConfigMfaArgsDict]]] = ..., monitoring: Optional[pulumi.Input[Union[ConfigMonitoringArgs, ConfigMonitoringArgsDict]]] = ..., multi_tenant: Optional[pulumi.Input[Union[ConfigMultiTenantArgs, ConfigMultiTenantArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., quota: Optional[pulumi.Input[Union[ConfigQuotaArgs, ConfigQuotaArgsDict]]] = ..., sign_in: Optional[pulumi.Input[Union[ConfigSignInArgs, ConfigSignInArgsDict]]] = ..., sms_region_config: Optional[pulumi.Input[Union[ConfigSmsRegionConfigArgs, ConfigSmsRegionConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ConfigArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., authorized_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., autodelete_anonymous_users: Optional[pulumi.Input[_builtins.bool]] = ..., blocking_functions: Optional[pulumi.Input[Union[ConfigBlockingFunctionsArgs, ConfigBlockingFunctionsArgsDict]]] = ..., client: Optional[pulumi.Input[Union[ConfigClientArgs, ConfigClientArgsDict]]] = ..., mfa: Optional[pulumi.Input[Union[ConfigMfaArgs, ConfigMfaArgsDict]]] = ..., monitoring: Optional[pulumi.Input[Union[ConfigMonitoringArgs, ConfigMonitoringArgsDict]]] = ..., multi_tenant: Optional[pulumi.Input[Union[ConfigMultiTenantArgs, ConfigMultiTenantArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., quota: Optional[pulumi.Input[Union[ConfigQuotaArgs, ConfigQuotaArgsDict]]] = ..., sign_in: Optional[pulumi.Input[Union[ConfigSignInArgs, ConfigSignInArgsDict]]] = ..., sms_region_config: Optional[pulumi.Input[Union[ConfigSmsRegionConfigArgs, ConfigSmsRegionConfigArgsDict]]] = ...) -> Config:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedDomains")
    def authorized_domains(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autodeleteAnonymousUsers")
    def autodelete_anonymous_users(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockingFunctions")
    def blocking_functions(self) -> pulumi.Output[Optional[outputs.ConfigBlockingFunctions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def client(self) -> pulumi.Output[outputs.ConfigClient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mfa(self) -> pulumi.Output[outputs.ConfigMfa]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> pulumi.Output[outputs.ConfigMonitoring]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiTenant")
    def multi_tenant(self) -> pulumi.Output[Optional[outputs.ConfigMultiTenant]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> pulumi.Output[Optional[outputs.ConfigQuota]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signIn")
    def sign_in(self) -> pulumi.Output[outputs.ConfigSignIn]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smsRegionConfig")
    def sms_region_config(self) -> pulumi.Output[outputs.ConfigSmsRegionConfig]:
        
        ...
    


