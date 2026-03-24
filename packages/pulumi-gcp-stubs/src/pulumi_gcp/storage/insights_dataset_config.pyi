

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
__all__ = ['InsightsDatasetConfigArgs', 'InsightsDatasetConfig']
@pulumi.input_type
class InsightsDatasetConfigArgs:
    def __init__(__self__, *, dataset_config_id: pulumi.Input[_builtins.str], identity: pulumi.Input[InsightsDatasetConfigIdentityArgs], location: pulumi.Input[_builtins.str], retention_period_days: pulumi.Input[_builtins.int], activity_data_retention_period_days: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exclude_cloud_storage_buckets: Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageBucketsArgs]] = ..., exclude_cloud_storage_locations: Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageLocationsArgs]] = ..., include_cloud_storage_buckets: Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageBucketsArgs]] = ..., include_cloud_storage_locations: Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageLocationsArgs]] = ..., include_newly_created_buckets: Optional[pulumi.Input[_builtins.bool]] = ..., link_dataset: Optional[pulumi.Input[_builtins.bool]] = ..., organization_number: Optional[pulumi.Input[_builtins.str]] = ..., organization_scope: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., source_folders: Optional[pulumi.Input[InsightsDatasetConfigSourceFoldersArgs]] = ..., source_projects: Optional[pulumi.Input[InsightsDatasetConfigSourceProjectsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetConfigId")
    def dataset_config_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dataset_config_id.setter
    def dataset_config_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Input[InsightsDatasetConfigIdentityArgs]:
        
        ...
    
    @identity.setter
    def identity(self, value: pulumi.Input[InsightsDatasetConfigIdentityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodDays")
    def retention_period_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @retention_period_days.setter
    def retention_period_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activityDataRetentionPeriodDays")
    def activity_data_retention_period_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @activity_data_retention_period_days.setter
    def activity_data_retention_period_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeCloudStorageBuckets")
    def exclude_cloud_storage_buckets(self) -> Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageBucketsArgs]]:
        
        ...
    
    @exclude_cloud_storage_buckets.setter
    def exclude_cloud_storage_buckets(self, value: Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeCloudStorageLocations")
    def exclude_cloud_storage_locations(self) -> Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageLocationsArgs]]:
        
        ...
    
    @exclude_cloud_storage_locations.setter
    def exclude_cloud_storage_locations(self, value: Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageLocationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeCloudStorageBuckets")
    def include_cloud_storage_buckets(self) -> Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageBucketsArgs]]:
        
        ...
    
    @include_cloud_storage_buckets.setter
    def include_cloud_storage_buckets(self, value: Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeCloudStorageLocations")
    def include_cloud_storage_locations(self) -> Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageLocationsArgs]]:
        
        ...
    
    @include_cloud_storage_locations.setter
    def include_cloud_storage_locations(self, value: Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageLocationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeNewlyCreatedBuckets")
    def include_newly_created_buckets(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_newly_created_buckets.setter
    def include_newly_created_buckets(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkDataset")
    def link_dataset(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @link_dataset.setter
    def link_dataset(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationNumber")
    def organization_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_number.setter
    def organization_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationScope")
    def organization_scope(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @organization_scope.setter
    def organization_scope(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFolders")
    def source_folders(self) -> Optional[pulumi.Input[InsightsDatasetConfigSourceFoldersArgs]]:
        
        ...
    
    @source_folders.setter
    def source_folders(self, value: Optional[pulumi.Input[InsightsDatasetConfigSourceFoldersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceProjects")
    def source_projects(self) -> Optional[pulumi.Input[InsightsDatasetConfigSourceProjectsArgs]]:
        
        ...
    
    @source_projects.setter
    def source_projects(self, value: Optional[pulumi.Input[InsightsDatasetConfigSourceProjectsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _InsightsDatasetConfigState:
    def __init__(__self__, *, activity_data_retention_period_days: Optional[pulumi.Input[_builtins.int]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dataset_config_id: Optional[pulumi.Input[_builtins.str]] = ..., dataset_config_state: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exclude_cloud_storage_buckets: Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageBucketsArgs]] = ..., exclude_cloud_storage_locations: Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageLocationsArgs]] = ..., identity: Optional[pulumi.Input[InsightsDatasetConfigIdentityArgs]] = ..., include_cloud_storage_buckets: Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageBucketsArgs]] = ..., include_cloud_storage_locations: Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageLocationsArgs]] = ..., include_newly_created_buckets: Optional[pulumi.Input[_builtins.bool]] = ..., link_dataset: Optional[pulumi.Input[_builtins.bool]] = ..., links: Optional[pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigLinkArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., organization_number: Optional[pulumi.Input[_builtins.str]] = ..., organization_scope: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., retention_period_days: Optional[pulumi.Input[_builtins.int]] = ..., source_folders: Optional[pulumi.Input[InsightsDatasetConfigSourceFoldersArgs]] = ..., source_projects: Optional[pulumi.Input[InsightsDatasetConfigSourceProjectsArgs]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activityDataRetentionPeriodDays")
    def activity_data_retention_period_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @activity_data_retention_period_days.setter
    def activity_data_retention_period_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetConfigId")
    def dataset_config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataset_config_id.setter
    def dataset_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetConfigState")
    def dataset_config_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataset_config_state.setter
    def dataset_config_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeCloudStorageBuckets")
    def exclude_cloud_storage_buckets(self) -> Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageBucketsArgs]]:
        
        ...
    
    @exclude_cloud_storage_buckets.setter
    def exclude_cloud_storage_buckets(self, value: Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeCloudStorageLocations")
    def exclude_cloud_storage_locations(self) -> Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageLocationsArgs]]:
        
        ...
    
    @exclude_cloud_storage_locations.setter
    def exclude_cloud_storage_locations(self, value: Optional[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageLocationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[InsightsDatasetConfigIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[InsightsDatasetConfigIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeCloudStorageBuckets")
    def include_cloud_storage_buckets(self) -> Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageBucketsArgs]]:
        
        ...
    
    @include_cloud_storage_buckets.setter
    def include_cloud_storage_buckets(self, value: Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeCloudStorageLocations")
    def include_cloud_storage_locations(self) -> Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageLocationsArgs]]:
        
        ...
    
    @include_cloud_storage_locations.setter
    def include_cloud_storage_locations(self, value: Optional[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageLocationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeNewlyCreatedBuckets")
    def include_newly_created_buckets(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_newly_created_buckets.setter
    def include_newly_created_buckets(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkDataset")
    def link_dataset(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @link_dataset.setter
    def link_dataset(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigLinkArgs]]]]:
        
        ...
    
    @links.setter
    def links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigLinkArgs]]]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationNumber")
    def organization_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_number.setter
    def organization_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationScope")
    def organization_scope(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @organization_scope.setter
    def organization_scope(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodDays")
    def retention_period_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_period_days.setter
    def retention_period_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFolders")
    def source_folders(self) -> Optional[pulumi.Input[InsightsDatasetConfigSourceFoldersArgs]]:
        
        ...
    
    @source_folders.setter
    def source_folders(self, value: Optional[pulumi.Input[InsightsDatasetConfigSourceFoldersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceProjects")
    def source_projects(self) -> Optional[pulumi.Input[InsightsDatasetConfigSourceProjectsArgs]]:
        
        ...
    
    @source_projects.setter
    def source_projects(self, value: Optional[pulumi.Input[InsightsDatasetConfigSourceProjectsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class InsightsDatasetConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., activity_data_retention_period_days: Optional[pulumi.Input[_builtins.int]] = ..., dataset_config_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exclude_cloud_storage_buckets: Optional[pulumi.Input[Union[InsightsDatasetConfigExcludeCloudStorageBucketsArgs, InsightsDatasetConfigExcludeCloudStorageBucketsArgsDict]]] = ..., exclude_cloud_storage_locations: Optional[pulumi.Input[Union[InsightsDatasetConfigExcludeCloudStorageLocationsArgs, InsightsDatasetConfigExcludeCloudStorageLocationsArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[InsightsDatasetConfigIdentityArgs, InsightsDatasetConfigIdentityArgsDict]]] = ..., include_cloud_storage_buckets: Optional[pulumi.Input[Union[InsightsDatasetConfigIncludeCloudStorageBucketsArgs, InsightsDatasetConfigIncludeCloudStorageBucketsArgsDict]]] = ..., include_cloud_storage_locations: Optional[pulumi.Input[Union[InsightsDatasetConfigIncludeCloudStorageLocationsArgs, InsightsDatasetConfigIncludeCloudStorageLocationsArgsDict]]] = ..., include_newly_created_buckets: Optional[pulumi.Input[_builtins.bool]] = ..., link_dataset: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., organization_number: Optional[pulumi.Input[_builtins.str]] = ..., organization_scope: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., retention_period_days: Optional[pulumi.Input[_builtins.int]] = ..., source_folders: Optional[pulumi.Input[Union[InsightsDatasetConfigSourceFoldersArgs, InsightsDatasetConfigSourceFoldersArgsDict]]] = ..., source_projects: Optional[pulumi.Input[Union[InsightsDatasetConfigSourceProjectsArgs, InsightsDatasetConfigSourceProjectsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InsightsDatasetConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., activity_data_retention_period_days: Optional[pulumi.Input[_builtins.int]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dataset_config_id: Optional[pulumi.Input[_builtins.str]] = ..., dataset_config_state: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exclude_cloud_storage_buckets: Optional[pulumi.Input[Union[InsightsDatasetConfigExcludeCloudStorageBucketsArgs, InsightsDatasetConfigExcludeCloudStorageBucketsArgsDict]]] = ..., exclude_cloud_storage_locations: Optional[pulumi.Input[Union[InsightsDatasetConfigExcludeCloudStorageLocationsArgs, InsightsDatasetConfigExcludeCloudStorageLocationsArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[InsightsDatasetConfigIdentityArgs, InsightsDatasetConfigIdentityArgsDict]]] = ..., include_cloud_storage_buckets: Optional[pulumi.Input[Union[InsightsDatasetConfigIncludeCloudStorageBucketsArgs, InsightsDatasetConfigIncludeCloudStorageBucketsArgsDict]]] = ..., include_cloud_storage_locations: Optional[pulumi.Input[Union[InsightsDatasetConfigIncludeCloudStorageLocationsArgs, InsightsDatasetConfigIncludeCloudStorageLocationsArgsDict]]] = ..., include_newly_created_buckets: Optional[pulumi.Input[_builtins.bool]] = ..., link_dataset: Optional[pulumi.Input[_builtins.bool]] = ..., links: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InsightsDatasetConfigLinkArgs, InsightsDatasetConfigLinkArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., organization_number: Optional[pulumi.Input[_builtins.str]] = ..., organization_scope: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., retention_period_days: Optional[pulumi.Input[_builtins.int]] = ..., source_folders: Optional[pulumi.Input[Union[InsightsDatasetConfigSourceFoldersArgs, InsightsDatasetConfigSourceFoldersArgsDict]]] = ..., source_projects: Optional[pulumi.Input[Union[InsightsDatasetConfigSourceProjectsArgs, InsightsDatasetConfigSourceProjectsArgsDict]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> InsightsDatasetConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activityDataRetentionPeriodDays")
    def activity_data_retention_period_days(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetConfigId")
    def dataset_config_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetConfigState")
    def dataset_config_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeCloudStorageBuckets")
    def exclude_cloud_storage_buckets(self) -> pulumi.Output[Optional[outputs.InsightsDatasetConfigExcludeCloudStorageBuckets]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeCloudStorageLocations")
    def exclude_cloud_storage_locations(self) -> pulumi.Output[Optional[outputs.InsightsDatasetConfigExcludeCloudStorageLocations]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[outputs.InsightsDatasetConfigIdentity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeCloudStorageBuckets")
    def include_cloud_storage_buckets(self) -> pulumi.Output[Optional[outputs.InsightsDatasetConfigIncludeCloudStorageBuckets]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeCloudStorageLocations")
    def include_cloud_storage_locations(self) -> pulumi.Output[Optional[outputs.InsightsDatasetConfigIncludeCloudStorageLocations]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeNewlyCreatedBuckets")
    def include_newly_created_buckets(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkDataset")
    def link_dataset(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def links(self) -> pulumi.Output[Sequence[outputs.InsightsDatasetConfigLink]]:
        
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
    @pulumi.getter(name="organizationNumber")
    def organization_number(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationScope")
    def organization_scope(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodDays")
    def retention_period_days(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFolders")
    def source_folders(self) -> pulumi.Output[Optional[outputs.InsightsDatasetConfigSourceFolders]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceProjects")
    def source_projects(self) -> pulumi.Output[Optional[outputs.InsightsDatasetConfigSourceProjects]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


