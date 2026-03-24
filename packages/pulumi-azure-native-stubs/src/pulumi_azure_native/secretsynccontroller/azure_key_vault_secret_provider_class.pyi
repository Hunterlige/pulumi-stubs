

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AzureKeyVaultSecretProviderClassArgs', 'AzureKeyVaultSecretProviderClass']
@pulumi.input_type
class AzureKeyVaultSecretProviderClassArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], keyvault_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], tenant_id: pulumi.Input[_builtins.str], azure_key_vault_secret_provider_class_name: Optional[pulumi.Input[_builtins.str]] = ..., extended_location: Optional[pulumi.Input[AzureResourceManagerCommonTypesExtendedLocationArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., objects: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyvaultName")
    def keyvault_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @keyvault_name.setter
    def keyvault_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureKeyVaultSecretProviderClassName")
    def azure_key_vault_secret_provider_class_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @azure_key_vault_secret_provider_class_name.setter
    def azure_key_vault_secret_provider_class_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[AzureResourceManagerCommonTypesExtendedLocationArgs]]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input[AzureResourceManagerCommonTypesExtendedLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def objects(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @objects.setter
    def objects(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AzureKeyVaultSecretProviderClass(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., azure_key_vault_secret_provider_class_name: Optional[pulumi.Input[_builtins.str]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., extended_location: Optional[pulumi.Input[Union[AzureResourceManagerCommonTypesExtendedLocationArgs, AzureResourceManagerCommonTypesExtendedLocationArgsDict]]] = ..., keyvault_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., objects: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AzureKeyVaultSecretProviderClassArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AzureKeyVaultSecretProviderClass:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional[outputs.AzureResourceManagerCommonTypesExtendedLocationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyvaultName")
    def keyvault_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def objects(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


