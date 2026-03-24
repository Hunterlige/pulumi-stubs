

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
__all__ = ['VolumeArgs', 'Volume']
@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *, elastic_san_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], size_gi_b: pulumi.Input[_builtins.float], volume_group_name: pulumi.Input[_builtins.str], creation_data: Optional[pulumi.Input[SourceCreationDataArgs]] = ..., managed_by: Optional[pulumi.Input[ManagedByInfoArgs]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticSanName")
    def elastic_san_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @elastic_san_name.setter
    def elastic_san_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGiB")
    def size_gi_b(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @size_gi_b.setter
    def size_gi_b(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeGroupName")
    def volume_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @volume_group_name.setter
    def volume_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional[pulumi.Input[SourceCreationDataArgs]]:
        
        ...
    
    @creation_data.setter
    def creation_data(self, value: Optional[pulumi.Input[SourceCreationDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[ManagedByInfoArgs]]:
        
        ...
    
    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[ManagedByInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:elasticsan:Volume")
class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., creation_data: Optional[pulumi.Input[Union[SourceCreationDataArgs, SourceCreationDataArgsDict]]] = ..., elastic_san_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_by: Optional[pulumi.Input[Union[ManagedByInfoArgs, ManagedByInfoArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., size_gi_b: Optional[pulumi.Input[_builtins.float]] = ..., volume_group_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VolumeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Volume:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> pulumi.Output[Optional[outputs.SourceCreationDataResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[Optional[outputs.ManagedByInfoResponse]]:
        
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
    @pulumi.getter(name="sizeGiB")
    def size_gi_b(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageTarget")
    def storage_target(self) -> pulumi.Output[outputs.IscsiTargetInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


