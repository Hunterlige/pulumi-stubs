import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GalleryApplicationVersionArgs", "GalleryApplicationVersion"]

@pulumi.input_type
class GalleryApplicationVersionArgs:
    def __init__(
        __self__,
        *,
        gallery_application_name: pulumi.Input[_builtins.str],
        gallery_name: pulumi.Input[_builtins.str],
        publishing_profile: pulumi.Input[
            GalleryApplicationVersionPublishingProfileArgs
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        gallery_application_version_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        safety_profile: Optional[
            pulumi.Input[GalleryApplicationVersionSafetyProfileArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="galleryApplicationName")
    def gallery_application_name(self) -> pulumi.Input[_builtins.str]: ...
    @gallery_application_name.setter
    def gallery_application_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> pulumi.Input[_builtins.str]: ...
    @gallery_name.setter
    def gallery_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="publishingProfile")
    def publishing_profile(
        self,
    ) -> pulumi.Input[GalleryApplicationVersionPublishingProfileArgs]: ...
    @publishing_profile.setter
    def publishing_profile(
        self, value: pulumi.Input[GalleryApplicationVersionPublishingProfileArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="galleryApplicationVersionName")
    def gallery_application_version_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gallery_application_version_name.setter
    def gallery_application_version_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="safetyProfile")
    def safety_profile(
        self,
    ) -> Optional[pulumi.Input[GalleryApplicationVersionSafetyProfileArgs]]: ...
    @safety_profile.setter
    def safety_profile(
        self, value: Optional[pulumi.Input[GalleryApplicationVersionSafetyProfileArgs]]
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

@pulumi.type_token("azure-native:compute:GalleryApplicationVersion")
class GalleryApplicationVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        gallery_application_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gallery_application_version_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gallery_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        publishing_profile: Optional[
            pulumi.Input[
                Union[
                    GalleryApplicationVersionPublishingProfileArgs,
                    GalleryApplicationVersionPublishingProfileArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        safety_profile: Optional[
            pulumi.Input[
                Union[
                    GalleryApplicationVersionSafetyProfileArgs,
                    GalleryApplicationVersionSafetyProfileArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GalleryApplicationVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> GalleryApplicationVersion: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publishingProfile")
    def publishing_profile(
        self,
    ) -> pulumi.Output[outputs.GalleryApplicationVersionPublishingProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="replicationStatus")
    def replication_status(
        self,
    ) -> pulumi.Output[outputs.ReplicationStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="safetyProfile")
    def safety_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.GalleryApplicationVersionSafetyProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
