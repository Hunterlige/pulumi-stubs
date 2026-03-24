import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReplicationConfigurationArgs", "ReplicationConfiguration"]

@pulumi.input_type
class ReplicationConfigurationArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[ReplicationConfigurationDestinationArgs],
        source_file_system_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[ReplicationConfigurationDestinationArgs]: ...
    @destination.setter
    def destination(
        self, value: pulumi.Input[ReplicationConfigurationDestinationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileSystemId")
    def source_file_system_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_file_system_id.setter
    def source_file_system_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ReplicationConfigurationState:
    def __init__(
        __self__,
        *,
        creation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[
            pulumi.Input[ReplicationConfigurationDestinationArgs]
        ] = ...,
        original_source_file_system_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_system_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_system_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> Optional[pulumi.Input[ReplicationConfigurationDestinationArgs]]: ...
    @destination.setter
    def destination(
        self, value: Optional[pulumi.Input[ReplicationConfigurationDestinationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="originalSourceFileSystemArn")
    def original_source_file_system_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @original_source_file_system_arn.setter
    def original_source_file_system_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileSystemArn")
    def source_file_system_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_system_arn.setter
    def source_file_system_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileSystemId")
    def source_file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_system_id.setter
    def source_file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileSystemRegion")
    def source_file_system_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_system_region.setter
    def source_file_system_region(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class ReplicationConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        destination: Optional[
            pulumi.Input[
                Union[
                    ReplicationConfigurationDestinationArgs,
                    ReplicationConfigurationDestinationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReplicationConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        creation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[
            pulumi.Input[
                Union[
                    ReplicationConfigurationDestinationArgs,
                    ReplicationConfigurationDestinationArgsDict,
                ]
            ]
        ] = ...,
        original_source_file_system_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_system_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_system_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ReplicationConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Output[outputs.ReplicationConfigurationDestination]: ...
    @_builtins.property
    @pulumi.getter(name="originalSourceFileSystemArn")
    def original_source_file_system_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceFileSystemArn")
    def source_file_system_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceFileSystemId")
    def source_file_system_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceFileSystemRegion")
    def source_file_system_region(self) -> pulumi.Output[_builtins.str]: ...
