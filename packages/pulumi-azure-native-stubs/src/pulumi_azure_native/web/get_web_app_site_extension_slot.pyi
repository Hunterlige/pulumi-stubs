import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAppSiteExtensionSlotResult",
    "AwaitableGetWebAppSiteExtensionSlotResult",
    "get_web_app_site_extension_slot",
    "get_web_app_site_extension_slot_output",
]

@pulumi.output_type
class GetWebAppSiteExtensionSlotResult:
    def __init__(
        __self__,
        authors=...,
        azure_api_version=...,
        comment=...,
        description=...,
        download_count=...,
        extension_id=...,
        extension_type=...,
        extension_url=...,
        feed_url=...,
        icon_url=...,
        id=...,
        installed_date_time=...,
        installer_command_line_params=...,
        kind=...,
        license_url=...,
        local_is_latest_version=...,
        local_path=...,
        name=...,
        project_url=...,
        provisioning_state=...,
        published_date_time=...,
        summary=...,
        title=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authors(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="downloadCount")
    def download_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="extensionId")
    def extension_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extensionType")
    def extension_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extensionUrl")
    def extension_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="feedUrl")
    def feed_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iconUrl")
    def icon_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="installedDateTime")
    def installed_date_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="installerCommandLineParams")
    def installer_command_line_params(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="licenseUrl")
    def license_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localIsLatestVersion")
    def local_is_latest_version(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectUrl")
    def project_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publishedDateTime")
    def published_date_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def summary(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

class AwaitableGetWebAppSiteExtensionSlotResult(GetWebAppSiteExtensionSlotResult):
    def __await__(self): ...

def get_web_app_site_extension_slot(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    site_extension_id: Optional[_builtins.str] = ...,
    slot: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAppSiteExtensionSlotResult: ...
def get_web_app_site_extension_slot_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    site_extension_id: Optional[pulumi.Input[_builtins.str]] = ...,
    slot: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAppSiteExtensionSlotResult]: ...
