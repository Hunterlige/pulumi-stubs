import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceArgs", "Workspace"]

@pulumi.input_type
class WorkspaceArgs:
    def __init__(
        __self__,
        *,
        bundle_id: pulumi.Input[_builtins.str],
        directory_id: pulumi.Input[_builtins.str],
        user_name: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_volume_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_volume_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        volume_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_properties: Optional[
            pulumi.Input[WorkspaceWorkspacePropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Input[_builtins.str]: ...
    @bundle_id.setter
    def bundle_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Input[_builtins.str]: ...
    @directory_id.setter
    def directory_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[_builtins.str]: ...
    @user_name.setter
    def user_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @root_volume_encryption_enabled.setter
    def root_volume_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
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
    @_builtins.property
    @pulumi.getter(name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @user_volume_encryption_enabled.setter
    def user_volume_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeEncryptionKey")
    def volume_encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_encryption_key.setter
    def volume_encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceProperties")
    def workspace_properties(
        self,
    ) -> Optional[pulumi.Input[WorkspaceWorkspacePropertiesArgs]]: ...
    @workspace_properties.setter
    def workspace_properties(
        self, value: Optional[pulumi.Input[WorkspaceWorkspacePropertiesArgs]]
    ): ...

@pulumi.input_type
class _WorkspaceState:
    def __init__(
        __self__,
        *,
        bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        computer_name: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_volume_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        user_volume_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        volume_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_properties: Optional[
            pulumi.Input[WorkspaceWorkspacePropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bundle_id.setter
    def bundle_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @computer_name.setter
    def computer_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @root_volume_encryption_enabled.setter
    def root_volume_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @user_volume_encryption_enabled.setter
    def user_volume_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeEncryptionKey")
    def volume_encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_encryption_key.setter
    def volume_encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceProperties")
    def workspace_properties(
        self,
    ) -> Optional[pulumi.Input[WorkspaceWorkspacePropertiesArgs]]: ...
    @workspace_properties.setter
    def workspace_properties(
        self, value: Optional[pulumi.Input[WorkspaceWorkspacePropertiesArgs]]
    ): ...

@pulumi.type_token("aws:workspaces/workspace:Workspace")
class Workspace(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_volume_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        user_volume_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        volume_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_properties: Optional[
            pulumi.Input[
                Union[
                    WorkspaceWorkspacePropertiesArgs,
                    WorkspaceWorkspacePropertiesArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkspaceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        computer_name: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_volume_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        user_volume_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        volume_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_properties: Optional[
            pulumi.Input[
                Union[
                    WorkspaceWorkspacePropertiesArgs,
                    WorkspaceWorkspacePropertiesArgsDict,
                ]
            ]
        ] = ...,
    ) -> Workspace: ...
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="volumeEncryptionKey")
    def volume_encryption_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceProperties")
    def workspace_properties(
        self,
    ) -> pulumi.Output[outputs.WorkspaceWorkspaceProperties]: ...
