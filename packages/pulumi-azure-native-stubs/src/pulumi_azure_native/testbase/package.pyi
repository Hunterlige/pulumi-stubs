import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PackageArgs", "Package"]

@pulumi.input_type
class PackageArgs:
    def __init__(
        __self__,
        *,
        application_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        test_base_account_name: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        blob_path: Optional[pulumi.Input[_builtins.str]] = ...,
        draft_package_id: Optional[pulumi.Input[_builtins.str]] = ...,
        first_party_apps: Optional[
            pulumi.Input[Sequence[pulumi.Input[FirstPartyAppDefinitionArgs]]]
        ] = ...,
        flighting_ring: Optional[pulumi.Input[_builtins.str]] = ...,
        inplace_upgrade_os_pair: Optional[pulumi.Input[InplaceUpgradeOSInfoArgs]] = ...,
        intune_enrollment_metadata: Optional[
            pulumi.Input[IntuneEnrollmentMetadataArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        package_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_os_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetOSInfoArgs]]]
        ] = ...,
        tests: Optional[pulumi.Input[Sequence[pulumi.Input[TestArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Input[_builtins.str]: ...
    @application_name.setter
    def application_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="testBaseAccountName")
    def test_base_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @test_base_account_name.setter
    def test_base_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="blobPath")
    def blob_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blob_path.setter
    def blob_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="draftPackageId")
    def draft_package_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @draft_package_id.setter
    def draft_package_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firstPartyApps")
    def first_party_apps(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FirstPartyAppDefinitionArgs]]]
    ]: ...
    @first_party_apps.setter
    def first_party_apps(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FirstPartyAppDefinitionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="flightingRing")
    def flighting_ring(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flighting_ring.setter
    def flighting_ring(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inplaceUpgradeOSPair")
    def inplace_upgrade_os_pair(
        self,
    ) -> Optional[pulumi.Input[InplaceUpgradeOSInfoArgs]]: ...
    @inplace_upgrade_os_pair.setter
    def inplace_upgrade_os_pair(
        self, value: Optional[pulumi.Input[InplaceUpgradeOSInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="intuneEnrollmentMetadata")
    def intune_enrollment_metadata(
        self,
    ) -> Optional[pulumi.Input[IntuneEnrollmentMetadataArgs]]: ...
    @intune_enrollment_metadata.setter
    def intune_enrollment_metadata(
        self, value: Optional[pulumi.Input[IntuneEnrollmentMetadataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_name.setter
    def package_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="targetOSList")
    def target_os_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TargetOSInfoArgs]]]]: ...
    @target_os_list.setter
    def target_os_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TargetOSInfoArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TestArgs]]]]: ...
    @tests.setter
    def tests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TestArgs]]]]
    ): ...

@pulumi.type_token("azure-native:testbase:Package")
class Package(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_name: Optional[pulumi.Input[_builtins.str]] = ...,
        blob_path: Optional[pulumi.Input[_builtins.str]] = ...,
        draft_package_id: Optional[pulumi.Input[_builtins.str]] = ...,
        first_party_apps: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            FirstPartyAppDefinitionArgs, FirstPartyAppDefinitionArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        flighting_ring: Optional[pulumi.Input[_builtins.str]] = ...,
        inplace_upgrade_os_pair: Optional[
            pulumi.Input[Union[InplaceUpgradeOSInfoArgs, InplaceUpgradeOSInfoArgsDict]]
        ] = ...,
        intune_enrollment_metadata: Optional[
            pulumi.Input[
                Union[IntuneEnrollmentMetadataArgs, IntuneEnrollmentMetadataArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        package_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_os_list: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[TargetOSInfoArgs, TargetOSInfoArgsDict]]]
            ]
        ] = ...,
        test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tests: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[TestArgs, TestArgsDict]]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PackageArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Package: ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blobPath")
    def blob_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="draftPackageId")
    def draft_package_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="firstPartyApps")
    def first_party_apps(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.FirstPartyAppDefinitionResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="flightingRing")
    def flighting_ring(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="galleryApps")
    def gallery_apps(
        self,
    ) -> pulumi.Output[Sequence[outputs.GalleryAppDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="inplaceUpgradeOSPair")
    def inplace_upgrade_os_pair(
        self,
    ) -> pulumi.Output[Optional[outputs.InplaceUpgradeOSInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="intuneEnrollmentMetadata")
    def intune_enrollment_metadata(
        self,
    ) -> pulumi.Output[Optional[outputs.IntuneEnrollmentMetadataResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="packageStatus")
    def package_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="targetOSList")
    def target_os_list(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TargetOSInfoResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="testTypes")
    def test_types(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tests(self) -> pulumi.Output[Optional[Sequence[outputs.TestResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validationResults")
    def validation_results(
        self,
    ) -> pulumi.Output[Sequence[outputs.PackageValidationResultResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
