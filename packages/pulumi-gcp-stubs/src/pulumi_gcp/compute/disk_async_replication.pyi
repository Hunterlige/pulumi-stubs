import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DiskAsyncReplicationArgs", "DiskAsyncReplication"]

@pulumi.input_type
class DiskAsyncReplicationArgs:
    def __init__(
        __self__,
        *,
        primary_disk: pulumi.Input[_builtins.str],
        secondary_disk: pulumi.Input[DiskAsyncReplicationSecondaryDiskArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryDisk")
    def primary_disk(self) -> pulumi.Input[_builtins.str]: ...
    @primary_disk.setter
    def primary_disk(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryDisk")
    def secondary_disk(self) -> pulumi.Input[DiskAsyncReplicationSecondaryDiskArgs]: ...
    @secondary_disk.setter
    def secondary_disk(
        self, value: pulumi.Input[DiskAsyncReplicationSecondaryDiskArgs]
    ): ...

@pulumi.input_type
class _DiskAsyncReplicationState:
    def __init__(
        __self__,
        *,
        primary_disk: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_disk: Optional[
            pulumi.Input[DiskAsyncReplicationSecondaryDiskArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryDisk")
    def primary_disk(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_disk.setter
    def primary_disk(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryDisk")
    def secondary_disk(
        self,
    ) -> Optional[pulumi.Input[DiskAsyncReplicationSecondaryDiskArgs]]: ...
    @secondary_disk.setter
    def secondary_disk(
        self, value: Optional[pulumi.Input[DiskAsyncReplicationSecondaryDiskArgs]]
    ): ...

@pulumi.type_token(...)
class DiskAsyncReplication(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        primary_disk: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_disk: Optional[
            pulumi.Input[
                Union[
                    DiskAsyncReplicationSecondaryDiskArgs,
                    DiskAsyncReplicationSecondaryDiskArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DiskAsyncReplicationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        primary_disk: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_disk: Optional[
            pulumi.Input[
                Union[
                    DiskAsyncReplicationSecondaryDiskArgs,
                    DiskAsyncReplicationSecondaryDiskArgsDict,
                ]
            ]
        ] = ...,
    ) -> DiskAsyncReplication: ...
    @_builtins.property
    @pulumi.getter(name="primaryDisk")
    def primary_disk(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryDisk")
    def secondary_disk(
        self,
    ) -> pulumi.Output[outputs.DiskAsyncReplicationSecondaryDisk]: ...
