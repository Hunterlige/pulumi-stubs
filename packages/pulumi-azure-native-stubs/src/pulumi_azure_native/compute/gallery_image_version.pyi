import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GalleryImageVersionArgs", "GalleryImageVersion"]

@pulumi.input_type
class GalleryImageVersionArgs:
    def __init__(
        __self__,
        *,
        gallery_image_name: pulumi.Input[_builtins.str],
        gallery_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        storage_profile: pulumi.Input[GalleryImageVersionStorageProfileArgs],
        gallery_image_version_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        publishing_profile: Optional[
            pulumi.Input[GalleryImageVersionPublishingProfileArgs]
        ] = ...,
        restore: Optional[pulumi.Input[_builtins.bool]] = ...,
        safety_profile: Optional[
            pulumi.Input[GalleryImageVersionSafetyProfileArgs]
        ] = ...,
        security_profile: Optional[pulumi.Input[ImageVersionSecurityProfileArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="galleryImageName")
    def gallery_image_name(self) -> pulumi.Input[_builtins.str]: ...
    @gallery_image_name.setter
    def gallery_image_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> pulumi.Input[_builtins.str]: ...
    @gallery_name.setter
    def gallery_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(
        self,
    ) -> pulumi.Input[GalleryImageVersionStorageProfileArgs]: ...
    @storage_profile.setter
    def storage_profile(
        self, value: pulumi.Input[GalleryImageVersionStorageProfileArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="galleryImageVersionName")
    def gallery_image_version_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gallery_image_version_name.setter
    def gallery_image_version_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publishingProfile")
    def publishing_profile(
        self,
    ) -> Optional[pulumi.Input[GalleryImageVersionPublishingProfileArgs]]: ...
    @publishing_profile.setter
    def publishing_profile(
        self, value: Optional[pulumi.Input[GalleryImageVersionPublishingProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def restore(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @restore.setter
    def restore(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="safetyProfile")
    def safety_profile(
        self,
    ) -> Optional[pulumi.Input[GalleryImageVersionSafetyProfileArgs]]: ...
    @safety_profile.setter
    def safety_profile(
        self, value: Optional[pulumi.Input[GalleryImageVersionSafetyProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(
        self,
    ) -> Optional[pulumi.Input[ImageVersionSecurityProfileArgs]]: ...
    @security_profile.setter
    def security_profile(
        self, value: Optional[pulumi.Input[ImageVersionSecurityProfileArgs]]
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

@pulumi.type_token("azure-native:compute:GalleryImageVersion")
class GalleryImageVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        gallery_image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gallery_image_version_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gallery_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        publishing_profile: Optional[
            pulumi.Input[
                Union[
                    GalleryImageVersionPublishingProfileArgs,
                    GalleryImageVersionPublishingProfileArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        restore: Optional[pulumi.Input[_builtins.bool]] = ...,
        safety_profile: Optional[
            pulumi.Input[
                Union[
                    GalleryImageVersionSafetyProfileArgs,
                    GalleryImageVersionSafetyProfileArgsDict,
                ]
            ]
        ] = ...,
        security_profile: Optional[
            pulumi.Input[
                Union[
                    ImageVersionSecurityProfileArgs, ImageVersionSecurityProfileArgsDict
                ]
            ]
        ] = ...,
        storage_profile: Optional[
            pulumi.Input[
                Union[
                    GalleryImageVersionStorageProfileArgs,
                    GalleryImageVersionStorageProfileArgsDict,
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
        args: GalleryImageVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> GalleryImageVersion: ...
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
    ) -> pulumi.Output[
        Optional[outputs.GalleryImageVersionPublishingProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="replicationStatus")
    def replication_status(
        self,
    ) -> pulumi.Output[outputs.ReplicationStatusResponse]: ...
    @_builtins.property
    @pulumi.getter
    def restore(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="safetyProfile")
    def safety_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.GalleryImageVersionSafetyProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ImageVersionSecurityProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(
        self,
    ) -> pulumi.Output[outputs.GalleryImageVersionStorageProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validationsProfile")
    def validations_profile(
        self,
    ) -> pulumi.Output[outputs.ValidationsProfileResponse]: ...
