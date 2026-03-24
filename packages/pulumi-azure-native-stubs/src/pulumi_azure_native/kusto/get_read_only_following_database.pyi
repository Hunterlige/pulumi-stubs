

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReadOnlyFollowingDatabaseResult', 'AwaitableGetReadOnlyFollowingDatabaseResult', 'get_read_only_following_database', 'get_read_only_following_database_output']
@pulumi.output_type
class GetReadOnlyFollowingDatabaseResult:
    
    def __init__(__self__, attached_database_configuration_name=..., azure_api_version=..., database_share_origin=..., hot_cache_period=..., id=..., kind=..., leader_cluster_resource_id=..., location=..., name=..., original_database_name=..., principals_modification_kind=..., provisioning_state=..., soft_delete_period=..., statistics=..., suspension_details=..., table_level_sharing_properties=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedDatabaseConfigurationName")
    def attached_database_configuration_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseShareOrigin")
    def database_share_origin(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotCachePeriod")
    def hot_cache_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="leaderClusterResourceId")
    def leader_cluster_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originalDatabaseName")
    def original_database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalsModificationKind")
    def principals_modification_kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeletePeriod")
    def soft_delete_period(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statistics(self) -> outputs.DatabaseStatisticsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspensionDetails")
    def suspension_details(self) -> outputs.SuspensionDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableLevelSharingProperties")
    def table_level_sharing_properties(self) -> outputs.TableLevelSharingPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetReadOnlyFollowingDatabaseResult(GetReadOnlyFollowingDatabaseResult):
    def __await__(self): # -> Generator[Never, Any, GetReadOnlyFollowingDatabaseResult]:
        ...
    


def get_read_only_following_database(cluster_name: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReadOnlyFollowingDatabaseResult:
    
    ...

def get_read_only_following_database_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReadOnlyFollowingDatabaseResult]:
    
    ...

