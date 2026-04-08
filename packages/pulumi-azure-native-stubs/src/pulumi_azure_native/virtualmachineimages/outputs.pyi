import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DistributeVersionerLatestResponse",
    "DistributeVersionerSourceResponse",
    "ImageTemplateAutoRunResponse",
    "ImageTemplateFileCustomizerResponse",
    "ImageTemplateFileValidatorResponse",
    "ImageTemplateIdentityResponse",
    "ImageTemplateLastRunStatusResponse",
    "ImageTemplateManagedImageDistributorResponse",
    "ImageTemplateManagedImageSourceResponse",
    "ImageTemplatePlatformImageSourceResponse",
    "ImageTemplatePowerShellCustomizerResponse",
    "ImageTemplatePowerShellValidatorResponse",
    "ImageTemplatePropertiesResponseErrorHandling",
    "ImageTemplatePropertiesResponseOptimize",
    "ImageTemplatePropertiesResponseValidate",
    "ImageTemplatePropertiesResponseVmBoot",
    "ImageTemplateRestartCustomizerResponse",
    "ImageTemplateSharedImageDistributorResponse",
    "ImageTemplateSharedImageVersionSourceResponse",
    "ImageTemplateShellCustomizerResponse",
    "ImageTemplateShellValidatorResponse",
    "ImageTemplateVhdDistributorResponse",
    "ImageTemplateVmProfileResponse",
    "ImageTemplateWindowsUpdateCustomizerResponse",
    "PlatformImagePurchasePlanResponse",
    "ProvisioningErrorResponse",
    "SystemDataResponse",
    "TargetRegionResponse",
    "TriggerStatusResponse",
    "UserAssignedIdentityResponse",
    "VirtualNetworkConfigResponse",
]

@pulumi.output_type
class DistributeVersionerLatestResponse(dict):
    def __init__(
        __self__, *, scheme: _builtins.str, major: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def major(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DistributeVersionerSourceResponse(dict):
    def __init__(__self__, *, scheme: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> _builtins.str: ...

@pulumi.output_type
class ImageTemplateAutoRunResponse(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplateFileCustomizerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        destination: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        sha256_checksum: Optional[_builtins.str] = ...,
        source_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplateFileValidatorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        destination: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        sha256_checksum: Optional[_builtins.str] = ...,
        source_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplateIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class ImageTemplateLastRunStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        run_state: Optional[_builtins.str] = ...,
        run_sub_state: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runState")
    def run_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runSubState")
    def run_sub_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplateManagedImageDistributorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_id: _builtins.str,
        location: _builtins.str,
        run_output_name: _builtins.str,
        type: _builtins.str,
        artifact_tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runOutputName")
    def run_output_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="artifactTags")
    def artifact_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ImageTemplateManagedImageSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, image_id: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ImageTemplatePlatformImageSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exact_version: _builtins.str,
        type: _builtins.str,
        offer: Optional[_builtins.str] = ...,
        plan_info: Optional[outputs.PlatformImagePurchasePlanResponse] = ...,
        publisher: Optional[_builtins.str] = ...,
        sku: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exactVersion")
    def exact_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="planInfo")
    def plan_info(self) -> Optional[outputs.PlatformImagePurchasePlanResponse]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplatePowerShellCustomizerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        inline: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        run_as_system: Optional[_builtins.bool] = ...,
        run_elevated: Optional[_builtins.bool] = ...,
        script_uri: Optional[_builtins.str] = ...,
        sha256_checksum: Optional[_builtins.str] = ...,
        valid_exit_codes: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def inline(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runAsSystem")
    def run_as_system(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runElevated")
    def run_elevated(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="scriptUri")
    def script_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validExitCodes")
    def valid_exit_codes(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class ImageTemplatePowerShellValidatorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        inline: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        run_as_system: Optional[_builtins.bool] = ...,
        run_elevated: Optional[_builtins.bool] = ...,
        script_uri: Optional[_builtins.str] = ...,
        sha256_checksum: Optional[_builtins.str] = ...,
        valid_exit_codes: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def inline(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runAsSystem")
    def run_as_system(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runElevated")
    def run_elevated(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="scriptUri")
    def script_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validExitCodes")
    def valid_exit_codes(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class ImageTemplatePropertiesResponseErrorHandling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        on_customizer_error: Optional[_builtins.str] = ...,
        on_validation_error: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onCustomizerError")
    def on_customizer_error(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="onValidationError")
    def on_validation_error(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplatePropertiesResponseOptimize(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        vm_boot: Optional[outputs.ImageTemplatePropertiesResponseVmBoot] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vmBoot")
    def vm_boot(self) -> Optional[outputs.ImageTemplatePropertiesResponseVmBoot]: ...

@pulumi.output_type
class ImageTemplatePropertiesResponseValidate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        continue_distribute_on_failure: Optional[_builtins.bool] = ...,
        in_vm_validations: Optional[Sequence[Any]] = ...,
        source_validation_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="continueDistributeOnFailure")
    def continue_distribute_on_failure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inVMValidations")
    def in_vm_validations(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceValidationOnly")
    def source_validation_only(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ImageTemplatePropertiesResponseVmBoot(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplateRestartCustomizerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        name: Optional[_builtins.str] = ...,
        restart_check_command: Optional[_builtins.str] = ...,
        restart_command: Optional[_builtins.str] = ...,
        restart_timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restartCheckCommand")
    def restart_check_command(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restartCommand")
    def restart_command(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restartTimeout")
    def restart_timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplateSharedImageDistributorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gallery_image_id: _builtins.str,
        run_output_name: _builtins.str,
        type: _builtins.str,
        artifact_tags: Optional[Mapping[str, _builtins.str]] = ...,
        exclude_from_latest: Optional[_builtins.bool] = ...,
        replication_regions: Optional[Sequence[_builtins.str]] = ...,
        storage_account_type: Optional[_builtins.str] = ...,
        target_regions: Optional[Sequence[outputs.TargetRegionResponse]] = ...,
        versioning: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="galleryImageId")
    def gallery_image_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runOutputName")
    def run_output_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="artifactTags")
    def artifact_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="replicationRegions")
    def replication_regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetRegions")
    def target_regions(self) -> Optional[Sequence[outputs.TargetRegionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def versioning(self) -> Optional[Any]: ...

@pulumi.output_type
class ImageTemplateSharedImageVersionSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exact_version: _builtins.str,
        image_version_id: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exactVersion")
    def exact_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionId")
    def image_version_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ImageTemplateShellCustomizerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        inline: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        script_uri: Optional[_builtins.str] = ...,
        sha256_checksum: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def inline(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scriptUri")
    def script_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplateShellValidatorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        inline: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        script_uri: Optional[_builtins.str] = ...,
        sha256_checksum: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def inline(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scriptUri")
    def script_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplateVhdDistributorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        run_output_name: _builtins.str,
        type: _builtins.str,
        artifact_tags: Optional[Mapping[str, _builtins.str]] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="runOutputName")
    def run_output_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="artifactTags")
    def artifact_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageTemplateVmProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_disk_size_gb: Optional[_builtins.int] = ...,
        user_assigned_identities: Optional[Sequence[_builtins.str]] = ...,
        vm_size: Optional[_builtins.str] = ...,
        vnet_config: Optional[outputs.VirtualNetworkConfigResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osDiskSizeGB")
    def os_disk_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vnetConfig")
    def vnet_config(self) -> Optional[outputs.VirtualNetworkConfigResponse]: ...

@pulumi.output_type
class ImageTemplateWindowsUpdateCustomizerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        filters: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        search_criteria: Optional[_builtins.str] = ...,
        update_limit: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="searchCriteria")
    def search_criteria(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateLimit")
    def update_limit(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PlatformImagePurchasePlanResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        plan_name: _builtins.str,
        plan_product: _builtins.str,
        plan_publisher: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="planName")
    def plan_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="planProduct")
    def plan_product(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="planPublisher")
    def plan_publisher(self) -> _builtins.str: ...

@pulumi.output_type
class ProvisioningErrorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message: Optional[_builtins.str] = ...,
        provisioning_error_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningErrorCode")
    def provisioning_error_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetRegionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        replica_count: Optional[_builtins.int] = ...,
        storage_account_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TriggerStatusResponse(dict):
    def __init__(
        __self__, *, code: _builtins.str, message: _builtins.str, time: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> _builtins.str: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNetworkConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_instance_subnet_id: Optional[_builtins.str] = ...,
        proxy_vm_size: Optional[_builtins.str] = ...,
        subnet_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerInstanceSubnetId")
    def container_instance_subnet_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="proxyVmSize")
    def proxy_vm_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]: ...
