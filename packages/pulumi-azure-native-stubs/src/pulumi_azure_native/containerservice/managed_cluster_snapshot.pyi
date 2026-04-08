import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ManagedClusterSnapshotArgs", "ManagedClusterSnapshot"]

@pulumi.input_type
class ManagedClusterSnapshotArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        creation_data: Optional[pulumi.Input[CreationDataArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_type: Optional[pulumi.Input[Union[_builtins.str, SnapshotType]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional[pulumi.Input[CreationDataArgs]]: ...
    @creation_data.setter
    def creation_data(self, value: Optional[pulumi.Input[CreationDataArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SnapshotType]]]: ...
    @snapshot_type.setter
    def snapshot_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SnapshotType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class ManagedClusterSnapshot(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        creation_data: Optional[
            pulumi.Input[Union[CreationDataArgs, CreationDataArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_type: Optional[pulumi.Input[Union[_builtins.str, SnapshotType]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedClusterSnapshotArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ManagedClusterSnapshot: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(
        self,
    ) -> pulumi.Output[Optional[outputs.CreationDataResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedClusterPropertiesReadOnly")
    def managed_cluster_properties_read_only(
        self,
    ) -> pulumi.Output[outputs.ManagedClusterPropertiesForSnapshotResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
