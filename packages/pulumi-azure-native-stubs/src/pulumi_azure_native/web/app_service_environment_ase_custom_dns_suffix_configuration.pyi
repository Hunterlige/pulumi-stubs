

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ...]
@pulumi.input_type
class AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], certificate_url: Optional[pulumi.Input[_builtins.str]] = ..., dns_suffix: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_reference_identity: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_url.setter
    def certificate_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_suffix.setter
    def dns_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultReferenceIdentity")
    def key_vault_reference_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_reference_identity.setter
    def key_vault_reference_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AppServiceEnvironmentAseCustomDnsSuffixConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., certificate_url: Optional[pulumi.Input[_builtins.str]] = ..., dns_suffix: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_reference_identity: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AppServiceEnvironmentAseCustomDnsSuffixConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultReferenceIdentity")
    def key_vault_reference_identity(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningDetails")
    def provisioning_details(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


