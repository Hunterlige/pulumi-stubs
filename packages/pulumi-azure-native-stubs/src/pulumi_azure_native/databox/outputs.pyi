import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccountCredentialDetailsResponse",
    "AdditionalErrorInfoResponse",
    "ApplianceNetworkConfigurationResponse",
    "AzureFileFilterDetailsResponse",
    "BlobFilterDetailsResponse",
    "CloudErrorResponse",
    "ContactDetailsResponse",
    "ContactInfoResponse",
    "CopyProgressResponse",
    "CustomerDiskJobSecretsResponse",
    "DataBoxAccountCopyLogDetailsResponse",
    "DataBoxCustomerDiskCopyLogDetailsResponse",
    "DataBoxCustomerDiskCopyProgressResponse",
    "DataBoxCustomerDiskJobDetailsResponse",
    "DataBoxDiskCopyLogDetailsResponse",
    "DataBoxDiskCopyProgressResponse",
    "DataBoxDiskGranularCopyLogDetailsResponse",
    "DataBoxDiskGranularCopyProgressResponse",
    "DataBoxDiskJobDetailsResponse",
    "DataBoxDiskJobSecretsResponse",
    "DataBoxHeavyAccountCopyLogDetailsResponse",
    "DataBoxHeavyJobDetailsResponse",
    "DataBoxHeavyJobSecretsResponse",
    "DataBoxHeavySecretResponse",
    "DataBoxJobDetailsResponse",
    "DataBoxSecretResponse",
    "DataExportDetailsResponse",
    "DataImportDetailsResponse",
    "DataboxJobSecretsResponse",
    "DatacenterAddressInstructionResponseResponse",
    "DatacenterAddressLocationResponseResponse",
    "DcAccessSecurityCodeResponse",
    "DeviceErasureDetailsResponse",
    "DiskSecretResponse",
    "EncryptionPreferencesResponse",
    "ExportDiskDetailsResponse",
    "FilterFileDetailsResponse",
    "IdentityPropertiesResponse",
    "ImportDiskDetailsResponse",
    "JobDelayDetailsResponse",
    "JobDeliveryInfoResponse",
    "JobStagesResponse",
    "KeyEncryptionKeyResponse",
    "LastMitigationActionOnJobResponse",
    "ManagedDiskDetailsResponse",
    "NotificationPreferenceResponse",
    "PackageCarrierDetailsResponse",
    "PackageCarrierInfoResponse",
    "PackageShippingDetailsResponse",
    "PreferencesResponse",
    "ResourceIdentityResponse",
    "ReverseShippingDetailsResponse",
    "ShareCredentialDetailsResponse",
    "ShippingAddressResponse",
    "SkuResponse",
    "StorageAccountDetailsResponse",
    "SystemDataResponse",
    "TransferAllDetailsResponse",
    "TransferConfigurationResponse",
    "TransferConfigurationResponseTransferAllDetails",
    "TransferConfigurationResponseTransferFilterDetails",
    "TransferFilterDetailsResponse",
    "TransportPreferencesResponse",
    "UnencryptedCredentialsResponse",
    "UserAssignedIdentityResponse",
    "UserAssignedPropertiesResponse",
]

@pulumi.output_type
class AccountCredentialDetailsResponse(dict):
    def __init__(
        __self__,
        *,
        account_connection_string: _builtins.str,
        account_name: _builtins.str,
        data_account_type: _builtins.str,
        share_credential_details: Sequence[outputs.ShareCredentialDetailsResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountConnectionString")
    def account_connection_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareCredentialDetails")
    def share_credential_details(
        self,
    ) -> Sequence[outputs.ShareCredentialDetailsResponse]: ...

@pulumi.output_type
class AdditionalErrorInfoResponse(dict):
    def __init__(
        __self__, *, info: Optional[Any] = ..., type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplianceNetworkConfigurationResponse(dict):
    def __init__(
        __self__, *, mac_address: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AzureFileFilterDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        file_path_list: Optional[Sequence[_builtins.str]] = ...,
        file_prefix_list: Optional[Sequence[_builtins.str]] = ...,
        file_share_list: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filePathList")
    def file_path_list(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="filePrefixList")
    def file_prefix_list(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fileShareList")
    def file_share_list(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class BlobFilterDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        blob_path_list: Optional[Sequence[_builtins.str]] = ...,
        blob_prefix_list: Optional[Sequence[_builtins.str]] = ...,
        container_list: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blobPathList")
    def blob_path_list(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="blobPrefixList")
    def blob_prefix_list(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerList")
    def container_list(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CloudErrorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_info: Sequence[outputs.AdditionalErrorInfoResponse],
        details: Sequence[outputs.CloudErrorResponse],
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        target: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.AdditionalErrorInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.CloudErrorResponse]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContactDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        contact_name: _builtins.str,
        email_list: Sequence[_builtins.str],
        phone: _builtins.str,
        mobile: Optional[_builtins.str] = ...,
        notification_preference: Optional[
            Sequence[outputs.NotificationPreferenceResponse]
        ] = ...,
        phone_extension: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactName")
    def contact_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="emailList")
    def email_list(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def phone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mobile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationPreference")
    def notification_preference(
        self,
    ) -> Optional[Sequence[outputs.NotificationPreferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="phoneExtension")
    def phone_extension(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContactInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        contact_name: _builtins.str,
        phone: _builtins.str,
        mobile: Optional[_builtins.str] = ...,
        phone_extension: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactName")
    def contact_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def phone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mobile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneExtension")
    def phone_extension(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CopyProgressResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        actions: Sequence[_builtins.str],
        bytes_processed: _builtins.float,
        data_account_type: _builtins.str,
        directories_errored_out: _builtins.float,
        error: outputs.CloudErrorResponse,
        files_errored_out: _builtins.float,
        files_processed: _builtins.float,
        invalid_directories_processed: _builtins.float,
        invalid_file_bytes_uploaded: _builtins.float,
        invalid_files_processed: _builtins.float,
        is_enumeration_in_progress: _builtins.bool,
        renamed_container_count: _builtins.float,
        storage_account_name: _builtins.str,
        total_bytes_to_process: _builtins.float,
        total_files_to_process: _builtins.float,
        transfer_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bytesProcessed")
    def bytes_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="directoriesErroredOut")
    def directories_errored_out(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.CloudErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="filesErroredOut")
    def files_errored_out(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="filesProcessed")
    def files_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="invalidDirectoriesProcessed")
    def invalid_directories_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="invalidFileBytesUploaded")
    def invalid_file_bytes_uploaded(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="invalidFilesProcessed")
    def invalid_files_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="isEnumerationInProgress")
    def is_enumeration_in_progress(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="renamedContainerCount")
    def renamed_container_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="totalBytesToProcess")
    def total_bytes_to_process(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="totalFilesToProcess")
    def total_files_to_process(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="transferType")
    def transfer_type(self) -> _builtins.str: ...

@pulumi.output_type
class CustomerDiskJobSecretsResponse(dict):
    def __init__(
        __self__,
        *,
        carrier_account_number: _builtins.str,
        dc_access_security_code: outputs.DcAccessSecurityCodeResponse,
        disk_secrets: Sequence[outputs.DiskSecretResponse],
        error: outputs.CloudErrorResponse,
        job_secrets_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="carrierAccountNumber")
    def carrier_account_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dcAccessSecurityCode")
    def dc_access_security_code(self) -> outputs.DcAccessSecurityCodeResponse: ...
    @_builtins.property
    @pulumi.getter(name="diskSecrets")
    def disk_secrets(self) -> Sequence[outputs.DiskSecretResponse]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.CloudErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="jobSecretsType")
    def job_secrets_type(self) -> _builtins.str: ...

@pulumi.output_type
class DataBoxAccountCopyLogDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_name: _builtins.str,
        copy_log_details_type: _builtins.str,
        copy_log_link: _builtins.str,
        copy_verbose_log_link: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="copyLogDetailsType")
    def copy_log_details_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="copyLogLink")
    def copy_log_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="copyVerboseLogLink")
    def copy_verbose_log_link(self) -> _builtins.str: ...

@pulumi.output_type
class DataBoxCustomerDiskCopyLogDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        copy_log_details_type: _builtins.str,
        error_log_link: _builtins.str,
        serial_number: _builtins.str,
        verbose_log_link: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copyLogDetailsType")
    def copy_log_details_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorLogLink")
    def error_log_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="verboseLogLink")
    def verbose_log_link(self) -> _builtins.str: ...

@pulumi.output_type
class DataBoxCustomerDiskCopyProgressResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        actions: Sequence[_builtins.str],
        bytes_processed: _builtins.float,
        copy_status: _builtins.str,
        data_account_type: _builtins.str,
        directories_errored_out: _builtins.float,
        error: outputs.CloudErrorResponse,
        files_errored_out: _builtins.float,
        files_processed: _builtins.float,
        invalid_directories_processed: _builtins.float,
        invalid_file_bytes_uploaded: _builtins.float,
        invalid_files_processed: _builtins.float,
        is_enumeration_in_progress: _builtins.bool,
        renamed_container_count: _builtins.float,
        serial_number: _builtins.str,
        storage_account_name: _builtins.str,
        total_bytes_to_process: _builtins.float,
        total_files_to_process: _builtins.float,
        transfer_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bytesProcessed")
    def bytes_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="copyStatus")
    def copy_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="directoriesErroredOut")
    def directories_errored_out(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.CloudErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="filesErroredOut")
    def files_errored_out(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="filesProcessed")
    def files_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="invalidDirectoriesProcessed")
    def invalid_directories_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="invalidFileBytesUploaded")
    def invalid_file_bytes_uploaded(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="invalidFilesProcessed")
    def invalid_files_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="isEnumerationInProgress")
    def is_enumeration_in_progress(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="renamedContainerCount")
    def renamed_container_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="totalBytesToProcess")
    def total_bytes_to_process(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="totalFilesToProcess")
    def total_files_to_process(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="transferType")
    def transfer_type(self) -> _builtins.str: ...

@pulumi.output_type
class DataBoxCustomerDiskJobDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Sequence[_builtins.str],
        chain_of_custody_sas_key: _builtins.str,
        contact_details: outputs.ContactDetailsResponse,
        copy_log_details: Sequence[Any],
        copy_progress: Sequence[outputs.DataBoxCustomerDiskCopyProgressResponse],
        data_center_code: _builtins.str,
        datacenter_address: Any,
        deliver_to_dc_package_details: outputs.PackageCarrierInfoResponse,
        delivery_package: outputs.PackageShippingDetailsResponse,
        device_erasure_details: outputs.DeviceErasureDetailsResponse,
        export_disk_details_collection: Mapping[str, outputs.ExportDiskDetailsResponse],
        job_details_type: _builtins.str,
        job_stages: Sequence[outputs.JobStagesResponse],
        last_mitigation_action_on_job: outputs.LastMitigationActionOnJobResponse,
        return_package: outputs.PackageShippingDetailsResponse,
        return_to_customer_package_details: outputs.PackageCarrierDetailsResponse,
        reverse_shipment_label_sas_key: _builtins.str,
        data_export_details: Optional[
            Sequence[outputs.DataExportDetailsResponse]
        ] = ...,
        data_import_details: Optional[
            Sequence[outputs.DataImportDetailsResponse]
        ] = ...,
        enable_manifest_backup: Optional[_builtins.bool] = ...,
        expected_data_size_in_tera_bytes: Optional[_builtins.int] = ...,
        import_disk_details_collection: Optional[
            Mapping[str, outputs.ImportDiskDetailsResponse]
        ] = ...,
        key_encryption_key: Optional[outputs.KeyEncryptionKeyResponse] = ...,
        preferences: Optional[outputs.PreferencesResponse] = ...,
        reverse_shipping_details: Optional[
            outputs.ReverseShippingDetailsResponse
        ] = ...,
        shipping_address: Optional[outputs.ShippingAddressResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="chainOfCustodySasKey")
    def chain_of_custody_sas_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> outputs.ContactDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="copyLogDetails")
    def copy_log_details(self) -> Sequence[Any]: ...
    @_builtins.property
    @pulumi.getter(name="copyProgress")
    def copy_progress(
        self,
    ) -> Sequence[outputs.DataBoxCustomerDiskCopyProgressResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dataCenterCode")
    def data_center_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datacenterAddress")
    def datacenter_address(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="deliverToDcPackageDetails")
    def deliver_to_dc_package_details(self) -> outputs.PackageCarrierInfoResponse: ...
    @_builtins.property
    @pulumi.getter(name="deliveryPackage")
    def delivery_package(self) -> outputs.PackageShippingDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="deviceErasureDetails")
    def device_erasure_details(self) -> outputs.DeviceErasureDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="exportDiskDetailsCollection")
    def export_disk_details_collection(
        self,
    ) -> Mapping[str, outputs.ExportDiskDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="jobDetailsType")
    def job_details_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobStages")
    def job_stages(self) -> Sequence[outputs.JobStagesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastMitigationActionOnJob")
    def last_mitigation_action_on_job(
        self,
    ) -> outputs.LastMitigationActionOnJobResponse: ...
    @_builtins.property
    @pulumi.getter(name="returnPackage")
    def return_package(self) -> outputs.PackageShippingDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="returnToCustomerPackageDetails")
    def return_to_customer_package_details(
        self,
    ) -> outputs.PackageCarrierDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="reverseShipmentLabelSasKey")
    def reverse_shipment_label_sas_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataExportDetails")
    def data_export_details(
        self,
    ) -> Optional[Sequence[outputs.DataExportDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dataImportDetails")
    def data_import_details(
        self,
    ) -> Optional[Sequence[outputs.DataImportDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="enableManifestBackup")
    def enable_manifest_backup(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="expectedDataSizeInTeraBytes")
    def expected_data_size_in_tera_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="importDiskDetailsCollection")
    def import_disk_details_collection(
        self,
    ) -> Optional[Mapping[str, outputs.ImportDiskDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[outputs.KeyEncryptionKeyResponse]: ...
    @_builtins.property
    @pulumi.getter
    def preferences(self) -> Optional[outputs.PreferencesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="reverseShippingDetails")
    def reverse_shipping_details(
        self,
    ) -> Optional[outputs.ReverseShippingDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[outputs.ShippingAddressResponse]: ...

@pulumi.output_type
class DataBoxDiskCopyLogDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        copy_log_details_type: _builtins.str,
        disk_serial_number: _builtins.str,
        error_log_link: _builtins.str,
        verbose_log_link: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copyLogDetailsType")
    def copy_log_details_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskSerialNumber")
    def disk_serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorLogLink")
    def error_log_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="verboseLogLink")
    def verbose_log_link(self) -> _builtins.str: ...

@pulumi.output_type
class DataBoxDiskCopyProgressResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Sequence[_builtins.str],
        bytes_copied: _builtins.float,
        error: outputs.CloudErrorResponse,
        percent_complete: _builtins.int,
        serial_number: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bytesCopied")
    def bytes_copied(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.CloudErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="percentComplete")
    def percent_complete(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class DataBoxDiskGranularCopyLogDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        copy_log_details_type: _builtins.str,
        error_log_link: _builtins.str,
        serial_number: _builtins.str,
        verbose_log_link: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="copyLogDetailsType")
    def copy_log_details_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorLogLink")
    def error_log_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="verboseLogLink")
    def verbose_log_link(self) -> _builtins.str: ...

@pulumi.output_type
class DataBoxDiskGranularCopyProgressResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        actions: Sequence[_builtins.str],
        bytes_processed: _builtins.float,
        copy_status: _builtins.str,
        data_account_type: _builtins.str,
        directories_errored_out: _builtins.float,
        error: outputs.CloudErrorResponse,
        files_errored_out: _builtins.float,
        files_processed: _builtins.float,
        invalid_directories_processed: _builtins.float,
        invalid_file_bytes_uploaded: _builtins.float,
        invalid_files_processed: _builtins.float,
        is_enumeration_in_progress: _builtins.bool,
        renamed_container_count: _builtins.float,
        serial_number: _builtins.str,
        storage_account_name: _builtins.str,
        total_bytes_to_process: _builtins.float,
        total_files_to_process: _builtins.float,
        transfer_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bytesProcessed")
    def bytes_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="copyStatus")
    def copy_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="directoriesErroredOut")
    def directories_errored_out(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.CloudErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="filesErroredOut")
    def files_errored_out(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="filesProcessed")
    def files_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="invalidDirectoriesProcessed")
    def invalid_directories_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="invalidFileBytesUploaded")
    def invalid_file_bytes_uploaded(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="invalidFilesProcessed")
    def invalid_files_processed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="isEnumerationInProgress")
    def is_enumeration_in_progress(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="renamedContainerCount")
    def renamed_container_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="totalBytesToProcess")
    def total_bytes_to_process(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="totalFilesToProcess")
    def total_files_to_process(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="transferType")
    def transfer_type(self) -> _builtins.str: ...

@pulumi.output_type
class DataBoxDiskJobDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Sequence[_builtins.str],
        chain_of_custody_sas_key: _builtins.str,
        contact_details: outputs.ContactDetailsResponse,
        copy_log_details: Sequence[Any],
        copy_progress: Sequence[outputs.DataBoxDiskCopyProgressResponse],
        data_center_code: _builtins.str,
        datacenter_address: Any,
        delivery_package: outputs.PackageShippingDetailsResponse,
        device_erasure_details: outputs.DeviceErasureDetailsResponse,
        disks_and_size_details: Mapping[str, _builtins.int],
        granular_copy_log_details: Sequence[
            outputs.DataBoxDiskGranularCopyLogDetailsResponse
        ],
        granular_copy_progress: Sequence[
            outputs.DataBoxDiskGranularCopyProgressResponse
        ],
        job_details_type: _builtins.str,
        job_stages: Sequence[outputs.JobStagesResponse],
        last_mitigation_action_on_job: outputs.LastMitigationActionOnJobResponse,
        return_package: outputs.PackageShippingDetailsResponse,
        reverse_shipment_label_sas_key: _builtins.str,
        data_export_details: Optional[
            Sequence[outputs.DataExportDetailsResponse]
        ] = ...,
        data_import_details: Optional[
            Sequence[outputs.DataImportDetailsResponse]
        ] = ...,
        expected_data_size_in_tera_bytes: Optional[_builtins.int] = ...,
        key_encryption_key: Optional[outputs.KeyEncryptionKeyResponse] = ...,
        passkey: Optional[_builtins.str] = ...,
        preferences: Optional[outputs.PreferencesResponse] = ...,
        preferred_disks: Optional[Mapping[str, _builtins.int]] = ...,
        reverse_shipping_details: Optional[
            outputs.ReverseShippingDetailsResponse
        ] = ...,
        shipping_address: Optional[outputs.ShippingAddressResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="chainOfCustodySasKey")
    def chain_of_custody_sas_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> outputs.ContactDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="copyLogDetails")
    def copy_log_details(self) -> Sequence[Any]: ...
    @_builtins.property
    @pulumi.getter(name="copyProgress")
    def copy_progress(self) -> Sequence[outputs.DataBoxDiskCopyProgressResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dataCenterCode")
    def data_center_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datacenterAddress")
    def datacenter_address(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="deliveryPackage")
    def delivery_package(self) -> outputs.PackageShippingDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="deviceErasureDetails")
    def device_erasure_details(self) -> outputs.DeviceErasureDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="disksAndSizeDetails")
    def disks_and_size_details(self) -> Mapping[str, _builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="granularCopyLogDetails")
    def granular_copy_log_details(
        self,
    ) -> Sequence[outputs.DataBoxDiskGranularCopyLogDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="granularCopyProgress")
    def granular_copy_progress(
        self,
    ) -> Sequence[outputs.DataBoxDiskGranularCopyProgressResponse]: ...
    @_builtins.property
    @pulumi.getter(name="jobDetailsType")
    def job_details_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobStages")
    def job_stages(self) -> Sequence[outputs.JobStagesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastMitigationActionOnJob")
    def last_mitigation_action_on_job(
        self,
    ) -> outputs.LastMitigationActionOnJobResponse: ...
    @_builtins.property
    @pulumi.getter(name="returnPackage")
    def return_package(self) -> outputs.PackageShippingDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="reverseShipmentLabelSasKey")
    def reverse_shipment_label_sas_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataExportDetails")
    def data_export_details(
        self,
    ) -> Optional[Sequence[outputs.DataExportDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dataImportDetails")
    def data_import_details(
        self,
    ) -> Optional[Sequence[outputs.DataImportDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="expectedDataSizeInTeraBytes")
    def expected_data_size_in_tera_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[outputs.KeyEncryptionKeyResponse]: ...
    @_builtins.property
    @pulumi.getter
    def passkey(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def preferences(self) -> Optional[outputs.PreferencesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="preferredDisks")
    def preferred_disks(self) -> Optional[Mapping[str, _builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="reverseShippingDetails")
    def reverse_shipping_details(
        self,
    ) -> Optional[outputs.ReverseShippingDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[outputs.ShippingAddressResponse]: ...

@pulumi.output_type
class DataBoxDiskJobSecretsResponse(dict):
    def __init__(
        __self__,
        *,
        dc_access_security_code: outputs.DcAccessSecurityCodeResponse,
        disk_secrets: Sequence[outputs.DiskSecretResponse],
        error: outputs.CloudErrorResponse,
        is_passkey_user_defined: _builtins.bool,
        job_secrets_type: _builtins.str,
        pass_key: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dcAccessSecurityCode")
    def dc_access_security_code(self) -> outputs.DcAccessSecurityCodeResponse: ...
    @_builtins.property
    @pulumi.getter(name="diskSecrets")
    def disk_secrets(self) -> Sequence[outputs.DiskSecretResponse]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.CloudErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="isPasskeyUserDefined")
    def is_passkey_user_defined(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="jobSecretsType")
    def job_secrets_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passKey")
    def pass_key(self) -> _builtins.str: ...

@pulumi.output_type
class DataBoxHeavyAccountCopyLogDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_name: _builtins.str,
        copy_log_details_type: _builtins.str,
        copy_log_link: Sequence[_builtins.str],
        copy_verbose_log_link: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="copyLogDetailsType")
    def copy_log_details_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="copyLogLink")
    def copy_log_link(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="copyVerboseLogLink")
    def copy_verbose_log_link(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DataBoxHeavyJobDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Sequence[_builtins.str],
        chain_of_custody_sas_key: _builtins.str,
        contact_details: outputs.ContactDetailsResponse,
        copy_log_details: Sequence[Any],
        copy_progress: Sequence[outputs.CopyProgressResponse],
        data_center_code: _builtins.str,
        datacenter_address: Any,
        delivery_package: outputs.PackageShippingDetailsResponse,
        device_erasure_details: outputs.DeviceErasureDetailsResponse,
        job_details_type: _builtins.str,
        job_stages: Sequence[outputs.JobStagesResponse],
        last_mitigation_action_on_job: outputs.LastMitigationActionOnJobResponse,
        return_package: outputs.PackageShippingDetailsResponse,
        reverse_shipment_label_sas_key: _builtins.str,
        data_export_details: Optional[
            Sequence[outputs.DataExportDetailsResponse]
        ] = ...,
        data_import_details: Optional[
            Sequence[outputs.DataImportDetailsResponse]
        ] = ...,
        device_password: Optional[_builtins.str] = ...,
        expected_data_size_in_tera_bytes: Optional[_builtins.int] = ...,
        key_encryption_key: Optional[outputs.KeyEncryptionKeyResponse] = ...,
        preferences: Optional[outputs.PreferencesResponse] = ...,
        reverse_shipping_details: Optional[
            outputs.ReverseShippingDetailsResponse
        ] = ...,
        shipping_address: Optional[outputs.ShippingAddressResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="chainOfCustodySasKey")
    def chain_of_custody_sas_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> outputs.ContactDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="copyLogDetails")
    def copy_log_details(self) -> Sequence[Any]: ...
    @_builtins.property
    @pulumi.getter(name="copyProgress")
    def copy_progress(self) -> Sequence[outputs.CopyProgressResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dataCenterCode")
    def data_center_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datacenterAddress")
    def datacenter_address(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="deliveryPackage")
    def delivery_package(self) -> outputs.PackageShippingDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="deviceErasureDetails")
    def device_erasure_details(self) -> outputs.DeviceErasureDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="jobDetailsType")
    def job_details_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobStages")
    def job_stages(self) -> Sequence[outputs.JobStagesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastMitigationActionOnJob")
    def last_mitigation_action_on_job(
        self,
    ) -> outputs.LastMitigationActionOnJobResponse: ...
    @_builtins.property
    @pulumi.getter(name="returnPackage")
    def return_package(self) -> outputs.PackageShippingDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="reverseShipmentLabelSasKey")
    def reverse_shipment_label_sas_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataExportDetails")
    def data_export_details(
        self,
    ) -> Optional[Sequence[outputs.DataExportDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dataImportDetails")
    def data_import_details(
        self,
    ) -> Optional[Sequence[outputs.DataImportDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="devicePassword")
    def device_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expectedDataSizeInTeraBytes")
    def expected_data_size_in_tera_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[outputs.KeyEncryptionKeyResponse]: ...
    @_builtins.property
    @pulumi.getter
    def preferences(self) -> Optional[outputs.PreferencesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="reverseShippingDetails")
    def reverse_shipping_details(
        self,
    ) -> Optional[outputs.ReverseShippingDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[outputs.ShippingAddressResponse]: ...

@pulumi.output_type
class DataBoxHeavyJobSecretsResponse(dict):
    def __init__(
        __self__,
        *,
        cabinet_pod_secrets: Sequence[outputs.DataBoxHeavySecretResponse],
        dc_access_security_code: outputs.DcAccessSecurityCodeResponse,
        error: outputs.CloudErrorResponse,
        job_secrets_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cabinetPodSecrets")
    def cabinet_pod_secrets(self) -> Sequence[outputs.DataBoxHeavySecretResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dcAccessSecurityCode")
    def dc_access_security_code(self) -> outputs.DcAccessSecurityCodeResponse: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.CloudErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="jobSecretsType")
    def job_secrets_type(self) -> _builtins.str: ...

@pulumi.output_type
class DataBoxHeavySecretResponse(dict):
    def __init__(
        __self__,
        *,
        account_credential_details: Sequence[outputs.AccountCredentialDetailsResponse],
        device_password: _builtins.str,
        device_serial_number: _builtins.str,
        encoded_validation_cert_pub_key: _builtins.str,
        network_configurations: Sequence[outputs.ApplianceNetworkConfigurationResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountCredentialDetails")
    def account_credential_details(
        self,
    ) -> Sequence[outputs.AccountCredentialDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="devicePassword")
    def device_password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceSerialNumber")
    def device_serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encodedValidationCertPubKey")
    def encoded_validation_cert_pub_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigurations")
    def network_configurations(
        self,
    ) -> Sequence[outputs.ApplianceNetworkConfigurationResponse]: ...

@pulumi.output_type
class DataBoxJobDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Sequence[_builtins.str],
        chain_of_custody_sas_key: _builtins.str,
        contact_details: outputs.ContactDetailsResponse,
        copy_log_details: Sequence[Any],
        copy_progress: Sequence[outputs.CopyProgressResponse],
        data_center_code: _builtins.str,
        datacenter_address: Any,
        delivery_package: outputs.PackageShippingDetailsResponse,
        device_erasure_details: outputs.DeviceErasureDetailsResponse,
        job_details_type: _builtins.str,
        job_stages: Sequence[outputs.JobStagesResponse],
        last_mitigation_action_on_job: outputs.LastMitigationActionOnJobResponse,
        return_package: outputs.PackageShippingDetailsResponse,
        reverse_shipment_label_sas_key: _builtins.str,
        data_export_details: Optional[
            Sequence[outputs.DataExportDetailsResponse]
        ] = ...,
        data_import_details: Optional[
            Sequence[outputs.DataImportDetailsResponse]
        ] = ...,
        device_password: Optional[_builtins.str] = ...,
        expected_data_size_in_tera_bytes: Optional[_builtins.int] = ...,
        key_encryption_key: Optional[outputs.KeyEncryptionKeyResponse] = ...,
        preferences: Optional[outputs.PreferencesResponse] = ...,
        reverse_shipping_details: Optional[
            outputs.ReverseShippingDetailsResponse
        ] = ...,
        shipping_address: Optional[outputs.ShippingAddressResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="chainOfCustodySasKey")
    def chain_of_custody_sas_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> outputs.ContactDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="copyLogDetails")
    def copy_log_details(self) -> Sequence[Any]: ...
    @_builtins.property
    @pulumi.getter(name="copyProgress")
    def copy_progress(self) -> Sequence[outputs.CopyProgressResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dataCenterCode")
    def data_center_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datacenterAddress")
    def datacenter_address(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="deliveryPackage")
    def delivery_package(self) -> outputs.PackageShippingDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="deviceErasureDetails")
    def device_erasure_details(self) -> outputs.DeviceErasureDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="jobDetailsType")
    def job_details_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobStages")
    def job_stages(self) -> Sequence[outputs.JobStagesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastMitigationActionOnJob")
    def last_mitigation_action_on_job(
        self,
    ) -> outputs.LastMitigationActionOnJobResponse: ...
    @_builtins.property
    @pulumi.getter(name="returnPackage")
    def return_package(self) -> outputs.PackageShippingDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="reverseShipmentLabelSasKey")
    def reverse_shipment_label_sas_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataExportDetails")
    def data_export_details(
        self,
    ) -> Optional[Sequence[outputs.DataExportDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dataImportDetails")
    def data_import_details(
        self,
    ) -> Optional[Sequence[outputs.DataImportDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="devicePassword")
    def device_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expectedDataSizeInTeraBytes")
    def expected_data_size_in_tera_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[outputs.KeyEncryptionKeyResponse]: ...
    @_builtins.property
    @pulumi.getter
    def preferences(self) -> Optional[outputs.PreferencesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="reverseShippingDetails")
    def reverse_shipping_details(
        self,
    ) -> Optional[outputs.ReverseShippingDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[outputs.ShippingAddressResponse]: ...

@pulumi.output_type
class DataBoxSecretResponse(dict):
    def __init__(
        __self__,
        *,
        account_credential_details: Sequence[outputs.AccountCredentialDetailsResponse],
        device_password: _builtins.str,
        device_serial_number: _builtins.str,
        encoded_validation_cert_pub_key: _builtins.str,
        network_configurations: Sequence[outputs.ApplianceNetworkConfigurationResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountCredentialDetails")
    def account_credential_details(
        self,
    ) -> Sequence[outputs.AccountCredentialDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="devicePassword")
    def device_password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceSerialNumber")
    def device_serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encodedValidationCertPubKey")
    def encoded_validation_cert_pub_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigurations")
    def network_configurations(
        self,
    ) -> Sequence[outputs.ApplianceNetworkConfigurationResponse]: ...

@pulumi.output_type
class DataExportDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_details: Any,
        transfer_configuration: outputs.TransferConfigurationResponse,
        log_collection_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountDetails")
    def account_details(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="transferConfiguration")
    def transfer_configuration(self) -> outputs.TransferConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="logCollectionLevel")
    def log_collection_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataImportDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_details: Any,
        log_collection_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountDetails")
    def account_details(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="logCollectionLevel")
    def log_collection_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataboxJobSecretsResponse(dict):
    def __init__(
        __self__,
        *,
        dc_access_security_code: outputs.DcAccessSecurityCodeResponse,
        error: outputs.CloudErrorResponse,
        job_secrets_type: _builtins.str,
        pod_secrets: Optional[Sequence[outputs.DataBoxSecretResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dcAccessSecurityCode")
    def dc_access_security_code(self) -> outputs.DcAccessSecurityCodeResponse: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.CloudErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="jobSecretsType")
    def job_secrets_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="podSecrets")
    def pod_secrets(self) -> Optional[Sequence[outputs.DataBoxSecretResponse]]: ...

@pulumi.output_type
class DatacenterAddressInstructionResponseResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        communication_instruction: _builtins.str,
        data_center_azure_location: _builtins.str,
        datacenter_address_type: _builtins.str,
        supported_carriers_for_return_shipment: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="communicationInstruction")
    def communication_instruction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataCenterAzureLocation")
    def data_center_azure_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datacenterAddressType")
    def datacenter_address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedCarriersForReturnShipment")
    def supported_carriers_for_return_shipment(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DatacenterAddressLocationResponseResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_shipping_information: _builtins.str,
        address_type: _builtins.str,
        city: _builtins.str,
        company: _builtins.str,
        contact_person_name: _builtins.str,
        country: _builtins.str,
        data_center_azure_location: _builtins.str,
        datacenter_address_type: _builtins.str,
        phone: _builtins.str,
        phone_extension: _builtins.str,
        state: _builtins.str,
        street1: _builtins.str,
        street2: _builtins.str,
        street3: _builtins.str,
        supported_carriers_for_return_shipment: Sequence[_builtins.str],
        zip: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalShippingInformation")
    def additional_shipping_information(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressType")
    def address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def company(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactPersonName")
    def contact_person_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataCenterAzureLocation")
    def data_center_azure_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datacenterAddressType")
    def datacenter_address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def phone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="phoneExtension")
    def phone_extension(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def street1(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def street2(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def street3(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedCarriersForReturnShipment")
    def supported_carriers_for_return_shipment(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zip(self) -> _builtins.str: ...

@pulumi.output_type
class DcAccessSecurityCodeResponse(dict):
    def __init__(
        __self__,
        *,
        forward_dc_access_code: Optional[_builtins.str] = ...,
        reverse_dc_access_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="forwardDCAccessCode")
    def forward_dc_access_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reverseDCAccessCode")
    def reverse_dc_access_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeviceErasureDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        device_erasure_status: _builtins.str,
        erasure_or_destruction_certificate_sas_key: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceErasureStatus")
    def device_erasure_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="erasureOrDestructionCertificateSasKey")
    def erasure_or_destruction_certificate_sas_key(self) -> _builtins.str: ...

@pulumi.output_type
class DiskSecretResponse(dict):
    def __init__(
        __self__, *, bit_locker_key: _builtins.str, disk_serial_number: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bitLockerKey")
    def bit_locker_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskSerialNumber")
    def disk_serial_number(self) -> _builtins.str: ...

@pulumi.output_type
class EncryptionPreferencesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        double_encryption: Optional[_builtins.str] = ...,
        hardware_encryption: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="doubleEncryption")
    def double_encryption(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareEncryption")
    def hardware_encryption(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExportDiskDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backup_manifest_cloud_path: _builtins.str,
        manifest_file: _builtins.str,
        manifest_hash: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupManifestCloudPath")
    def backup_manifest_cloud_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="manifestFile")
    def manifest_file(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="manifestHash")
    def manifest_hash(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFileDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, filter_file_path: _builtins.str, filter_file_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterFilePath")
    def filter_file_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterFileType")
    def filter_file_type(self) -> _builtins.str: ...

@pulumi.output_type
class IdentityPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        user_assigned: Optional[outputs.UserAssignedPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssigned")
    def user_assigned(self) -> Optional[outputs.UserAssignedPropertiesResponse]: ...

@pulumi.output_type
class ImportDiskDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backup_manifest_cloud_path: _builtins.str,
        bit_locker_key: _builtins.str,
        manifest_file: _builtins.str,
        manifest_hash: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupManifestCloudPath")
    def backup_manifest_cloud_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bitLockerKey")
    def bit_locker_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="manifestFile")
    def manifest_file(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="manifestHash")
    def manifest_hash(self) -> _builtins.str: ...

@pulumi.output_type
class JobDelayDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        error_code: _builtins.str,
        resolution_time: _builtins.str,
        start_time: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resolutionTime")
    def resolution_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class JobDeliveryInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, scheduled_date_time: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduledDateTime")
    def scheduled_date_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobStagesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delay_information: Sequence[outputs.JobDelayDetailsResponse],
        display_name: _builtins.str,
        job_stage_details: Any,
        stage_name: _builtins.str,
        stage_status: _builtins.str,
        stage_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="delayInformation")
    def delay_information(self) -> Sequence[outputs.JobDelayDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobStageDetails")
    def job_stage_details(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stageStatus")
    def stage_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stageTime")
    def stage_time(self) -> _builtins.str: ...

@pulumi.output_type
class KeyEncryptionKeyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kek_type: Optional[_builtins.str] = ...,
        identity_properties: Optional[outputs.IdentityPropertiesResponse] = ...,
        kek_url: Optional[_builtins.str] = ...,
        kek_vault_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kekType")
    def kek_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityProperties")
    def identity_properties(self) -> Optional[outputs.IdentityPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="kekUrl")
    def kek_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kekVaultResourceID")
    def kek_vault_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LastMitigationActionOnJobResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_date_time_in_utc: Optional[_builtins.str] = ...,
        customer_resolution: Optional[_builtins.str] = ...,
        is_performed_by_customer: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionDateTimeInUtc")
    def action_date_time_in_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerResolution")
    def customer_resolution(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isPerformedByCustomer")
    def is_performed_by_customer(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ManagedDiskDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_account_type: Optional[_builtins.str] = ...,
        resource_group_id: _builtins.str,
        staging_storage_account_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stagingStorageAccountId")
    def staging_storage_account_id(self) -> _builtins.str: ...

@pulumi.output_type
class NotificationPreferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        send_notification: Optional[_builtins.bool] = ...,
        stage_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sendNotification")
    def send_notification(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> _builtins.str: ...

@pulumi.output_type
class PackageCarrierDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        carrier_account_number: Optional[_builtins.str] = ...,
        carrier_name: Optional[_builtins.str] = ...,
        tracking_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="carrierAccountNumber")
    def carrier_account_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trackingId")
    def tracking_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PackageCarrierInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        carrier_name: Optional[_builtins.str] = ...,
        tracking_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trackingId")
    def tracking_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PackageShippingDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        carrier_name: _builtins.str,
        tracking_id: _builtins.str,
        tracking_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trackingId")
    def tracking_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trackingUrl")
    def tracking_url(self) -> _builtins.str: ...

@pulumi.output_type
class PreferencesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_preferences: Optional[outputs.EncryptionPreferencesResponse] = ...,
        preferred_data_center_region: Optional[Sequence[_builtins.str]] = ...,
        reverse_transport_preferences: Optional[
            outputs.TransportPreferencesResponse
        ] = ...,
        storage_account_access_tier_preferences: Optional[
            Sequence[_builtins.str]
        ] = ...,
        transport_preferences: Optional[outputs.TransportPreferencesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionPreferences")
    def encryption_preferences(
        self,
    ) -> Optional[outputs.EncryptionPreferencesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="preferredDataCenterRegion")
    def preferred_data_center_region(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="reverseTransportPreferences")
    def reverse_transport_preferences(
        self,
    ) -> Optional[outputs.TransportPreferencesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountAccessTierPreferences")
    def storage_account_access_tier_preferences(
        self,
    ) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transportPreferences")
    def transport_preferences(
        self,
    ) -> Optional[outputs.TransportPreferencesResponse]: ...

@pulumi.output_type
class ResourceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class ReverseShippingDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_updated: _builtins.bool,
        contact_details: Optional[outputs.ContactInfoResponse] = ...,
        shipping_address: Optional[outputs.ShippingAddressResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isUpdated")
    def is_updated(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> Optional[outputs.ContactInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[outputs.ShippingAddressResponse]: ...

@pulumi.output_type
class ShareCredentialDetailsResponse(dict):
    def __init__(
        __self__,
        *,
        password: _builtins.str,
        share_name: _builtins.str,
        share_type: _builtins.str,
        supported_access_protocols: Sequence[_builtins.str],
        user_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareType")
    def share_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedAccessProtocols")
    def supported_access_protocols(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str: ...

@pulumi.output_type
class ShippingAddressResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        country: _builtins.str,
        street_address1: _builtins.str,
        address_type: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        company_name: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        skip_address_validation: Optional[_builtins.bool] = ...,
        state_or_province: Optional[_builtins.str] = ...,
        street_address2: Optional[_builtins.str] = ...,
        street_address3: Optional[_builtins.str] = ...,
        tax_identification_number: Optional[_builtins.str] = ...,
        zip_extended_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="streetAddress1")
    def street_address1(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressType")
    def address_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipAddressValidation")
    def skip_address_validation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="stateOrProvince")
    def state_or_province(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streetAddress2")
    def street_address2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streetAddress3")
    def street_address3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="taxIdentificationNumber")
    def tax_identification_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zipExtendedCode")
    def zip_extended_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        model: _builtins.str,
        name: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        family: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageAccountDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_account_type: Optional[_builtins.str] = ...,
        storage_account_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> _builtins.str: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: _builtins.str,
        created_by: _builtins.str,
        created_by_type: _builtins.str,
        last_modified_at: _builtins.str,
        last_modified_by: _builtins.str,
        last_modified_by_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> _builtins.str: ...

@pulumi.output_type
class TransferAllDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_account_type: Optional[_builtins.str] = ...,
        transfer_all_blobs: Optional[_builtins.bool] = ...,
        transfer_all_files: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transferAllBlobs")
    def transfer_all_blobs(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="transferAllFiles")
    def transfer_all_files(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TransferConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        transfer_configuration_type: _builtins.str,
        transfer_all_details: Optional[
            outputs.TransferConfigurationResponseTransferAllDetails
        ] = ...,
        transfer_filter_details: Optional[
            outputs.TransferConfigurationResponseTransferFilterDetails
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transferConfigurationType")
    def transfer_configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transferAllDetails")
    def transfer_all_details(
        self,
    ) -> Optional[outputs.TransferConfigurationResponseTransferAllDetails]: ...
    @_builtins.property
    @pulumi.getter(name="transferFilterDetails")
    def transfer_filter_details(
        self,
    ) -> Optional[outputs.TransferConfigurationResponseTransferFilterDetails]: ...

@pulumi.output_type
class TransferConfigurationResponseTransferAllDetails(dict):
    def __init__(
        __self__, *, include: Optional[outputs.TransferAllDetailsResponse] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def include(self) -> Optional[outputs.TransferAllDetailsResponse]: ...

@pulumi.output_type
class TransferConfigurationResponseTransferFilterDetails(dict):
    def __init__(
        __self__, *, include: Optional[outputs.TransferFilterDetailsResponse] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def include(self) -> Optional[outputs.TransferFilterDetailsResponse]: ...

@pulumi.output_type
class TransferFilterDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_account_type: Optional[_builtins.str] = ...,
        azure_file_filter_details: Optional[
            outputs.AzureFileFilterDetailsResponse
        ] = ...,
        blob_filter_details: Optional[outputs.BlobFilterDetailsResponse] = ...,
        filter_file_details: Optional[
            Sequence[outputs.FilterFileDetailsResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureFileFilterDetails")
    def azure_file_filter_details(
        self,
    ) -> Optional[outputs.AzureFileFilterDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="blobFilterDetails")
    def blob_filter_details(self) -> Optional[outputs.BlobFilterDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="filterFileDetails")
    def filter_file_details(
        self,
    ) -> Optional[Sequence[outputs.FilterFileDetailsResponse]]: ...

@pulumi.output_type
class TransportPreferencesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, is_updated: _builtins.bool, preferred_shipment_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isUpdated")
    def is_updated(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="preferredShipmentType")
    def preferred_shipment_type(self) -> _builtins.str: ...

@pulumi.output_type
class UnencryptedCredentialsResponse(dict):
    def __init__(__self__, *, job_name: _builtins.str, job_secrets: Any) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobSecrets")
    def job_secrets(self) -> Any: ...

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
class UserAssignedPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...
