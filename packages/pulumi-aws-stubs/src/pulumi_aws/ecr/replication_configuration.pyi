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
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_configuration: Optional[
            pulumi.Input[ReplicationConfigurationReplicationConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationConfiguration")
    def replication_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ReplicationConfigurationReplicationConfigurationArgs]
    ]: ...
    @replication_configuration.setter
    def replication_configuration(
        self,
        value: Optional[
            pulumi.Input[ReplicationConfigurationReplicationConfigurationArgs]
        ],
    ): ...

@pulumi.input_type
class _ReplicationConfigurationState:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_configuration: Optional[
            pulumi.Input[ReplicationConfigurationReplicationConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationConfiguration")
    def replication_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ReplicationConfigurationReplicationConfigurationArgs]
    ]: ...
    @replication_configuration.setter
    def replication_configuration(
        self,
        value: Optional[
            pulumi.Input[ReplicationConfigurationReplicationConfigurationArgs]
        ],
    ): ...

@pulumi.type_token(...)
class ReplicationConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_configuration: Optional[
            pulumi.Input[
                Union[
                    ReplicationConfigurationReplicationConfigurationArgs,
                    ReplicationConfigurationReplicationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ReplicationConfigurationArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_configuration: Optional[
            pulumi.Input[
                Union[
                    ReplicationConfigurationReplicationConfigurationArgs,
                    ReplicationConfigurationReplicationConfigurationArgsDict,
                ]
            ]
        ] = ...,
    ) -> ReplicationConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationConfiguration")
    def replication_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ReplicationConfigurationReplicationConfiguration]
    ]: ...
