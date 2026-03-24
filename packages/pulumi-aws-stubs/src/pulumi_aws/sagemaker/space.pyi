import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SpaceArgs", "Space"]

@pulumi.input_type
class SpaceArgs:
    def __init__(
        __self__,
        *,
        domain_id: pulumi.Input[_builtins.str],
        space_name: pulumi.Input[_builtins.str],
        ownership_settings: Optional[pulumi.Input[SpaceOwnershipSettingsArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        space_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        space_settings: Optional[pulumi.Input[SpaceSpaceSettingsArgs]] = ...,
        space_sharing_settings: Optional[
            pulumi.Input[SpaceSpaceSharingSettingsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Input[_builtins.str]: ...
    @domain_id.setter
    def domain_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> pulumi.Input[_builtins.str]: ...
    @space_name.setter
    def space_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ownershipSettings")
    def ownership_settings(
        self,
    ) -> Optional[pulumi.Input[SpaceOwnershipSettingsArgs]]: ...
    @ownership_settings.setter
    def ownership_settings(
        self, value: Optional[pulumi.Input[SpaceOwnershipSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="spaceDisplayName")
    def space_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @space_display_name.setter
    def space_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="spaceSettings")
    def space_settings(self) -> Optional[pulumi.Input[SpaceSpaceSettingsArgs]]: ...
    @space_settings.setter
    def space_settings(self, value: Optional[pulumi.Input[SpaceSpaceSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="spaceSharingSettings")
    def space_sharing_settings(
        self,
    ) -> Optional[pulumi.Input[SpaceSpaceSharingSettingsArgs]]: ...
    @space_sharing_settings.setter
    def space_sharing_settings(
        self, value: Optional[pulumi.Input[SpaceSpaceSharingSettingsArgs]]
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

@pulumi.input_type
class _SpaceState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        home_efs_file_system_uid: Optional[pulumi.Input[_builtins.str]] = ...,
        ownership_settings: Optional[pulumi.Input[SpaceOwnershipSettingsArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        space_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        space_name: Optional[pulumi.Input[_builtins.str]] = ...,
        space_settings: Optional[pulumi.Input[SpaceSpaceSettingsArgs]] = ...,
        space_sharing_settings: Optional[
            pulumi.Input[SpaceSpaceSharingSettingsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="homeEfsFileSystemUid")
    def home_efs_file_system_uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @home_efs_file_system_uid.setter
    def home_efs_file_system_uid(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ownershipSettings")
    def ownership_settings(
        self,
    ) -> Optional[pulumi.Input[SpaceOwnershipSettingsArgs]]: ...
    @ownership_settings.setter
    def ownership_settings(
        self, value: Optional[pulumi.Input[SpaceOwnershipSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="spaceDisplayName")
    def space_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @space_display_name.setter
    def space_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @space_name.setter
    def space_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="spaceSettings")
    def space_settings(self) -> Optional[pulumi.Input[SpaceSpaceSettingsArgs]]: ...
    @space_settings.setter
    def space_settings(self, value: Optional[pulumi.Input[SpaceSpaceSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="spaceSharingSettings")
    def space_sharing_settings(
        self,
    ) -> Optional[pulumi.Input[SpaceSpaceSharingSettingsArgs]]: ...
    @space_sharing_settings.setter
    def space_sharing_settings(
        self, value: Optional[pulumi.Input[SpaceSpaceSharingSettingsArgs]]
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:sagemaker/space:Space")
class Space(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ownership_settings: Optional[
            pulumi.Input[
                Union[SpaceOwnershipSettingsArgs, SpaceOwnershipSettingsArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        space_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        space_name: Optional[pulumi.Input[_builtins.str]] = ...,
        space_settings: Optional[
            pulumi.Input[Union[SpaceSpaceSettingsArgs, SpaceSpaceSettingsArgsDict]]
        ] = ...,
        space_sharing_settings: Optional[
            pulumi.Input[
                Union[SpaceSpaceSharingSettingsArgs, SpaceSpaceSharingSettingsArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SpaceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        home_efs_file_system_uid: Optional[pulumi.Input[_builtins.str]] = ...,
        ownership_settings: Optional[
            pulumi.Input[
                Union[SpaceOwnershipSettingsArgs, SpaceOwnershipSettingsArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        space_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        space_name: Optional[pulumi.Input[_builtins.str]] = ...,
        space_settings: Optional[
            pulumi.Input[Union[SpaceSpaceSettingsArgs, SpaceSpaceSettingsArgsDict]]
        ] = ...,
        space_sharing_settings: Optional[
            pulumi.Input[
                Union[SpaceSpaceSharingSettingsArgs, SpaceSpaceSharingSettingsArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Space: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="homeEfsFileSystemUid")
    def home_efs_file_system_uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownershipSettings")
    def ownership_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.SpaceOwnershipSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="spaceDisplayName")
    def space_display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="spaceSettings")
    def space_settings(self) -> pulumi.Output[Optional[outputs.SpaceSpaceSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="spaceSharingSettings")
    def space_sharing_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.SpaceSpaceSharingSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]: ...
