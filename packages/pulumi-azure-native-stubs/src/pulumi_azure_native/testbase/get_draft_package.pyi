import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDraftPackageResult",
    "AwaitableGetDraftPackageResult",
    "get_draft_package",
    "get_draft_package_output",
]

@pulumi.output_type
class GetDraftPackageResult:
    def __init__(
        __self__,
        app_file_name=...,
        application_name=...,
        azure_api_version=...,
        comments=...,
        draft_package_path=...,
        edit_package=...,
        executable_launch_command=...,
        first_party_apps=...,
        flighting_ring=...,
        gallery_apps=...,
        highlighted_files=...,
        id=...,
        inplace_upgrade_os_pair=...,
        intune_enrollment_metadata=...,
        intune_metadata=...,
        last_modified_time=...,
        name=...,
        package_id=...,
        package_tags=...,
        process_name=...,
        provisioning_state=...,
        source_type=...,
        system_data=...,
        tab_state=...,
        target_os_list=...,
        test_types=...,
        tests=...,
        type=...,
        use_autofill=...,
        use_sample=...,
        version=...,
        working_path=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appFileName")
    def app_file_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comments(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="draftPackagePath")
    def draft_package_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="editPackage")
    def edit_package(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="executableLaunchCommand")
    def executable_launch_command(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstPartyApps")
    def first_party_apps(
        self,
    ) -> Optional[Sequence[outputs.FirstPartyAppDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="flightingRing")
    def flighting_ring(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="galleryApps")
    def gallery_apps(
        self,
    ) -> Optional[Sequence[outputs.GalleryAppDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="highlightedFiles")
    def highlighted_files(
        self,
    ) -> Optional[Sequence[outputs.HighlightedFileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inplaceUpgradeOSPair")
    def inplace_upgrade_os_pair(
        self,
    ) -> Optional[outputs.InplaceUpgradeOSInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="intuneEnrollmentMetadata")
    def intune_enrollment_metadata(
        self,
    ) -> Optional[outputs.IntuneEnrollmentMetadataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="intuneMetadata")
    def intune_metadata(
        self,
    ) -> Optional[outputs.DraftPackageIntuneAppMetadataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="packageId")
    def package_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="packageTags")
    def package_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="processName")
    def process_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="tabState")
    def tab_state(self) -> Optional[outputs.TabStateResponse]: ...
    @_builtins.property
    @pulumi.getter(name="targetOSList")
    def target_os_list(self) -> Optional[Sequence[outputs.TargetOSInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="testTypes")
    def test_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tests(self) -> Optional[Sequence[outputs.TestResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="useAutofill")
    def use_autofill(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="useSample")
    def use_sample(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workingPath")
    def working_path(self) -> _builtins.str: ...

class AwaitableGetDraftPackageResult(GetDraftPackageResult):
    def __await__(self): ...

def get_draft_package(
    draft_package_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    test_base_account_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDraftPackageResult: ...
def get_draft_package_output(
    draft_package_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDraftPackageResult]: ...
