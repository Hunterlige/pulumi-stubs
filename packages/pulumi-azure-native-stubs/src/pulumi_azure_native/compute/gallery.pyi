import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GalleryArgs", "Gallery"]

@pulumi.input_type
class GalleryArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        gallery_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[GalleryIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        sharing_profile: Optional[pulumi.Input[SharingProfileArgs]] = ...,
        soft_delete_policy: Optional[pulumi.Input[SoftDeletePolicyArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gallery_name.setter
    def gallery_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[GalleryIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[GalleryIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharingProfile")
    def sharing_profile(self) -> Optional[pulumi.Input[SharingProfileArgs]]: ...
    @sharing_profile.setter
    def sharing_profile(self, value: Optional[pulumi.Input[SharingProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="softDeletePolicy")
    def soft_delete_policy(self) -> Optional[pulumi.Input[SoftDeletePolicyArgs]]: ...
    @soft_delete_policy.setter
    def soft_delete_policy(
        self, value: Optional[pulumi.Input[SoftDeletePolicyArgs]]
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

@pulumi.type_token("azure-native:compute:Gallery")
class Gallery(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        gallery_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[Union[GalleryIdentityArgs, GalleryIdentityArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sharing_profile: Optional[
            pulumi.Input[Union[SharingProfileArgs, SharingProfileArgsDict]]
        ] = ...,
        soft_delete_policy: Optional[
            pulumi.Input[Union[SoftDeletePolicyArgs, SoftDeletePolicyArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GalleryArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Gallery: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identifier(
        self,
    ) -> pulumi.Output[Optional[outputs.GalleryIdentifierResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.GalleryIdentityResponse]]: ...
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
    @pulumi.getter(name="sharingProfile")
    def sharing_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.SharingProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sharingStatus")
    def sharing_status(self) -> pulumi.Output[outputs.SharingStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="softDeletePolicy")
    def soft_delete_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.SoftDeletePolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
