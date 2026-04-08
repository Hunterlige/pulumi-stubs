import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SnapshotArgs", "Snapshot"]

@pulumi.input_type
class SnapshotArgs:
    def __init__(
        __self__,
        *,
        pool_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Input[_builtins.str]: ...
    @pool_name.setter
    def pool_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:containerstorage:Snapshot")
class Snapshot(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SnapshotArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Snapshot: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.ResourceOperationalStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
