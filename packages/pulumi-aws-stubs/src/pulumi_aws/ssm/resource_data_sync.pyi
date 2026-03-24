import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ResourceDataSyncArgs", "ResourceDataSync"]

@pulumi.input_type
class ResourceDataSyncArgs:
    def __init__(
        __self__,
        *,
        s3_destination: pulumi.Input[ResourceDataSyncS3DestinationArgs],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> pulumi.Input[ResourceDataSyncS3DestinationArgs]: ...
    @s3_destination.setter
    def s3_destination(
        self, value: pulumi.Input[ResourceDataSyncS3DestinationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ResourceDataSyncState:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_destination: Optional[pulumi.Input[ResourceDataSyncS3DestinationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(
        self,
    ) -> Optional[pulumi.Input[ResourceDataSyncS3DestinationArgs]]: ...
    @s3_destination.setter
    def s3_destination(
        self, value: Optional[pulumi.Input[ResourceDataSyncS3DestinationArgs]]
    ): ...

@pulumi.type_token("aws:ssm/resourceDataSync:ResourceDataSync")
class ResourceDataSync(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_destination: Optional[
            pulumi.Input[
                Union[
                    ResourceDataSyncS3DestinationArgs,
                    ResourceDataSyncS3DestinationArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ResourceDataSyncArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_destination: Optional[
            pulumi.Input[
                Union[
                    ResourceDataSyncS3DestinationArgs,
                    ResourceDataSyncS3DestinationArgsDict,
                ]
            ]
        ] = ...,
    ) -> ResourceDataSync: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(
        self,
    ) -> pulumi.Output[outputs.ResourceDataSyncS3Destination]: ...
