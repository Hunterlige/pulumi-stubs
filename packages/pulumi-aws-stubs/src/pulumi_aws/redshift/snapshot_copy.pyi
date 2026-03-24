import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SnapshotCopyArgs", "SnapshotCopy"]

@pulumi.input_type
class SnapshotCopyArgs:
    def __init__(
        __self__,
        *,
        cluster_identifier: pulumi.Input[_builtins.str],
        destination_region: pulumi.Input[_builtins.str],
        manual_snapshot_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_copy_grant_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationRegion")
    def destination_region(self) -> pulumi.Input[_builtins.str]: ...
    @destination_region.setter
    def destination_region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @manual_snapshot_retention_period.setter
    def manual_snapshot_retention_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotCopyGrantName")
    def snapshot_copy_grant_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_copy_grant_name.setter
    def snapshot_copy_grant_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _SnapshotCopyState:
    def __init__(
        __self__,
        *,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_region: Optional[pulumi.Input[_builtins.str]] = ...,
        manual_snapshot_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_copy_grant_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationRegion")
    def destination_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_region.setter
    def destination_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @manual_snapshot_retention_period.setter
    def manual_snapshot_retention_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotCopyGrantName")
    def snapshot_copy_grant_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_copy_grant_name.setter
    def snapshot_copy_grant_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:redshift/snapshotCopy:SnapshotCopy")
class SnapshotCopy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_region: Optional[pulumi.Input[_builtins.str]] = ...,
        manual_snapshot_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_copy_grant_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SnapshotCopyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_region: Optional[pulumi.Input[_builtins.str]] = ...,
        manual_snapshot_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_copy_grant_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SnapshotCopy: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationRegion")
    def destination_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotCopyGrantName")
    def snapshot_copy_grant_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
