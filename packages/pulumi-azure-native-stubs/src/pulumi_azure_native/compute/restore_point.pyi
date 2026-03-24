

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RestorePointArgs', 'RestorePoint']
@pulumi.input_type
class RestorePointArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], restore_point_collection_name: pulumi.Input[_builtins.str], consistency_mode: Optional[pulumi.Input[Union[_builtins.str, ConsistencyModeTypes]]] = ..., exclude_disks: Optional[pulumi.Input[Sequence[pulumi.Input[ApiEntityReferenceArgs]]]] = ..., restore_point_name: Optional[pulumi.Input[_builtins.str]] = ..., source_metadata: Optional[pulumi.Input[RestorePointSourceMetadataArgs]] = ..., source_restore_point: Optional[pulumi.Input[ApiEntityReferenceArgs]] = ..., time_created: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePointCollectionName")
    def restore_point_collection_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @restore_point_collection_name.setter
    def restore_point_collection_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consistencyMode")
    def consistency_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, ConsistencyModeTypes]]]:
        
        ...
    
    @consistency_mode.setter
    def consistency_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, ConsistencyModeTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeDisks")
    def exclude_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiEntityReferenceArgs]]]]:
        
        ...
    
    @exclude_disks.setter
    def exclude_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiEntityReferenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePointName")
    def restore_point_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_point_name.setter
    def restore_point_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceMetadata")
    def source_metadata(self) -> Optional[pulumi.Input[RestorePointSourceMetadataArgs]]:
        
        ...
    
    @source_metadata.setter
    def source_metadata(self, value: Optional[pulumi.Input[RestorePointSourceMetadataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRestorePoint")
    def source_restore_point(self) -> Optional[pulumi.Input[ApiEntityReferenceArgs]]:
        
        ...
    
    @source_restore_point.setter
    def source_restore_point(self, value: Optional[pulumi.Input[ApiEntityReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:compute:RestorePoint")
class RestorePoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., consistency_mode: Optional[pulumi.Input[Union[_builtins.str, ConsistencyModeTypes]]] = ..., exclude_disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ApiEntityReferenceArgs, ApiEntityReferenceArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_point_collection_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_point_name: Optional[pulumi.Input[_builtins.str]] = ..., source_metadata: Optional[pulumi.Input[Union[RestorePointSourceMetadataArgs, RestorePointSourceMetadataArgsDict]]] = ..., source_restore_point: Optional[pulumi.Input[Union[ApiEntityReferenceArgs, ApiEntityReferenceArgsDict]]] = ..., time_created: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RestorePointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> RestorePoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consistencyMode")
    def consistency_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeDisks")
    def exclude_disks(self) -> pulumi.Output[Optional[Sequence[outputs.ApiEntityReferenceResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> pulumi.Output[outputs.RestorePointInstanceViewResponse]:
        
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
    @pulumi.getter(name="sourceMetadata")
    def source_metadata(self) -> pulumi.Output[Optional[outputs.RestorePointSourceMetadataResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRestorePoint")
    def source_restore_point(self) -> pulumi.Output[Optional[outputs.ApiEntityReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


