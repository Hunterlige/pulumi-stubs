import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGalleryApplicationVersionResult",
    "AwaitableGetGalleryApplicationVersionResult",
    "get_gallery_application_version",
    "get_gallery_application_version_output",
]

@pulumi.output_type
class GetGalleryApplicationVersionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        publishing_profile=...,
        replication_status=...,
        safety_profile=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publishingProfile")
    def publishing_profile(
        self,
    ) -> outputs.GalleryApplicationVersionPublishingProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="replicationStatus")
    def replication_status(self) -> outputs.ReplicationStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="safetyProfile")
    def safety_profile(
        self,
    ) -> Optional[outputs.GalleryApplicationVersionSafetyProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetGalleryApplicationVersionResult(GetGalleryApplicationVersionResult):
    def __await__(self): ...

def get_gallery_application_version(
    expand: Optional[_builtins.str] = ...,
    gallery_application_name: Optional[_builtins.str] = ...,
    gallery_application_version_name: Optional[_builtins.str] = ...,
    gallery_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGalleryApplicationVersionResult: ...
def get_gallery_application_version_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    gallery_application_name: Optional[pulumi.Input[_builtins.str]] = ...,
    gallery_application_version_name: Optional[pulumi.Input[_builtins.str]] = ...,
    gallery_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGalleryApplicationVersionResult]: ...
