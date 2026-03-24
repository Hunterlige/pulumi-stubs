

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HybridIdentityMetadataArgs', 'HybridIdentityMetadata']
@pulumi.input_type
class HybridIdentityMetadataArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], virtual_machine_name: pulumi.Input[_builtins.str], metadata_name: Optional[pulumi.Input[_builtins.str]] = ..., public_key: Optional[pulumi.Input[_builtins.str]] = ..., resource_uid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineName")
    def virtual_machine_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @virtual_machine_name.setter
    def virtual_machine_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataName")
    def metadata_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata_name.setter
    def metadata_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_uid.setter
    def resource_uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:scvmm:HybridIdentityMetadata")
class HybridIdentityMetadata(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., metadata_name: Optional[pulumi.Input[_builtins.str]] = ..., public_key: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_uid: Optional[pulumi.Input[_builtins.str]] = ..., virtual_machine_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HybridIdentityMetadataArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> HybridIdentityMetadata:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[outputs.IdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


