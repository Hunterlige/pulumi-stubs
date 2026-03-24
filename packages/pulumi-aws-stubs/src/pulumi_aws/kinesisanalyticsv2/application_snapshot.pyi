import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationSnapshotArgs", "ApplicationSnapshot"]

@pulumi.input_type
class ApplicationSnapshotArgs:
    def __init__(
        __self__,
        *,
        application_name: pulumi.Input[_builtins.str],
        snapshot_name: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Input[_builtins.str]: ...
    @application_name.setter
    def application_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Input[_builtins.str]: ...
    @snapshot_name.setter
    def snapshot_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ApplicationSnapshotState:
    def __init__(
        __self__,
        *,
        application_name: Optional[pulumi.Input[_builtins.str]] = ...,
        application_version_id: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_name.setter
    def application_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationVersionId")
    def application_version_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @application_version_id.setter
    def application_version_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotCreationTimestamp")
    def snapshot_creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_creation_timestamp.setter
    def snapshot_creation_timestamp(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ApplicationSnapshot(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationSnapshotArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_name: Optional[pulumi.Input[_builtins.str]] = ...,
        application_version_id: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ApplicationSnapshot: ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="applicationVersionId")
    def application_version_id(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotCreationTimestamp")
    def snapshot_creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Output[_builtins.str]: ...
