import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInsightsDatasetConfigResult",
    "AwaitableGetInsightsDatasetConfigResult",
    "get_insights_dataset_config",
    "get_insights_dataset_config_output",
]

@pulumi.output_type
class GetInsightsDatasetConfigResult:
    def __init__(
        __self__,
        activity_data_retention_period_days=...,
        create_time=...,
        dataset_config_id=...,
        dataset_config_state=...,
        description=...,
        exclude_cloud_storage_buckets=...,
        exclude_cloud_storage_locations=...,
        id=...,
        identities=...,
        include_cloud_storage_buckets=...,
        include_cloud_storage_locations=...,
        include_newly_created_buckets=...,
        link_dataset=...,
        links=...,
        location=...,
        name=...,
        organization_number=...,
        organization_scope=...,
        project=...,
        retention_period_days=...,
        source_folders=...,
        source_projects=...,
        uid=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activityDataRetentionPeriodDays")
    def activity_data_retention_period_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datasetConfigId")
    def dataset_config_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datasetConfigState")
    def dataset_config_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="excludeCloudStorageBuckets")
    def exclude_cloud_storage_buckets(
        self,
    ) -> Sequence[outputs.GetInsightsDatasetConfigExcludeCloudStorageBucketResult]: ...
    @_builtins.property
    @pulumi.getter(name="excludeCloudStorageLocations")
    def exclude_cloud_storage_locations(
        self,
    ) -> Sequence[
        outputs.GetInsightsDatasetConfigExcludeCloudStorageLocationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Sequence[outputs.GetInsightsDatasetConfigIdentityResult]: ...
    @_builtins.property
    @pulumi.getter(name="includeCloudStorageBuckets")
    def include_cloud_storage_buckets(
        self,
    ) -> Sequence[outputs.GetInsightsDatasetConfigIncludeCloudStorageBucketResult]: ...
    @_builtins.property
    @pulumi.getter(name="includeCloudStorageLocations")
    def include_cloud_storage_locations(
        self,
    ) -> Sequence[
        outputs.GetInsightsDatasetConfigIncludeCloudStorageLocationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="includeNewlyCreatedBuckets")
    def include_newly_created_buckets(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="linkDataset")
    def link_dataset(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def links(self) -> Sequence[outputs.GetInsightsDatasetConfigLinkResult]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationNumber")
    def organization_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationScope")
    def organization_scope(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriodDays")
    def retention_period_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sourceFolders")
    def source_folders(
        self,
    ) -> Sequence[outputs.GetInsightsDatasetConfigSourceFolderResult]: ...
    @_builtins.property
    @pulumi.getter(name="sourceProjects")
    def source_projects(
        self,
    ) -> Sequence[outputs.GetInsightsDatasetConfigSourceProjectResult]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetInsightsDatasetConfigResult(GetInsightsDatasetConfigResult):
    def __await__(self): ...

def get_insights_dataset_config(
    dataset_config_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInsightsDatasetConfigResult: ...
def get_insights_dataset_config_output(
    dataset_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInsightsDatasetConfigResult]: ...
