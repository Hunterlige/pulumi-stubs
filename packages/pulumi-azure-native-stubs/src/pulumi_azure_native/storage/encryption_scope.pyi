

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EncryptionScopeArgs', 'EncryptionScope']
@pulumi.input_type
class EncryptionScopeArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], encryption_scope_name: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_properties: Optional[pulumi.Input[EncryptionScopeKeyVaultPropertiesArgs]] = ..., require_infrastructure_encryption: Optional[pulumi.Input[_builtins.bool]] = ..., source: Optional[pulumi.Input[Union[_builtins.str, EncryptionScopeSource]]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, EncryptionScopeState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionScopeName")
    def encryption_scope_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_scope_name.setter
    def encryption_scope_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[pulumi.Input[EncryptionScopeKeyVaultPropertiesArgs]]:
        
        ...
    
    @key_vault_properties.setter
    def key_vault_properties(self, value: Optional[pulumi.Input[EncryptionScopeKeyVaultPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireInfrastructureEncryption")
    def require_infrastructure_encryption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_infrastructure_encryption.setter
    def require_infrastructure_encryption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[Union[_builtins.str, EncryptionScopeSource]]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[Union[_builtins.str, EncryptionScopeSource]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, EncryptionScopeState]]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, EncryptionScopeState]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:storage:EncryptionScope")
class EncryptionScope(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., encryption_scope_name: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_properties: Optional[pulumi.Input[Union[EncryptionScopeKeyVaultPropertiesArgs, EncryptionScopeKeyVaultPropertiesArgsDict]]] = ..., require_infrastructure_encryption: Optional[pulumi.Input[_builtins.bool]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[_builtins.str, EncryptionScopeSource]]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, EncryptionScopeState]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EncryptionScopeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> EncryptionScope:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> pulumi.Output[Optional[outputs.EncryptionScopeKeyVaultPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireInfrastructureEncryption")
    def require_infrastructure_encryption(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


