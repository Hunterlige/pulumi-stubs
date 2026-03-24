

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeliveryPackageInformationResponse', 'DriveBitLockerKeyResponse', 'DriveStatusResponse', 'EncryptionKeyDetailsResponse', 'ExportResponse', 'IdentityDetailsResponse', 'JobDetailsResponse', 'PackageInformationResponse', 'ReturnAddressResponse', 'ReturnShippingResponse', 'ShippingInformationResponse', 'SystemDataResponse']
@pulumi.output_type
class DeliveryPackageInformationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, carrier_name: _builtins.str, tracking_number: _builtins.str, drive_count: Optional[_builtins.float] = ..., ship_date: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingNumber")
    def tracking_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveCount")
    def drive_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shipDate")
    def ship_date(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DriveBitLockerKeyResponse(dict):
    
    def __init__(__self__, *, bit_locker_key: Optional[_builtins.str] = ..., drive_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitLockerKey")
    def bit_locker_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveId")
    def drive_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DriveStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bit_locker_key: Optional[_builtins.str] = ..., bytes_succeeded: Optional[_builtins.float] = ..., copy_status: Optional[_builtins.str] = ..., drive_header_hash: Optional[_builtins.str] = ..., drive_id: Optional[_builtins.str] = ..., error_log_uri: Optional[_builtins.str] = ..., manifest_file: Optional[_builtins.str] = ..., manifest_hash: Optional[_builtins.str] = ..., manifest_uri: Optional[_builtins.str] = ..., percent_complete: Optional[_builtins.float] = ..., state: Optional[_builtins.str] = ..., verbose_log_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitLockerKey")
    def bit_locker_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bytesSucceeded")
    def bytes_succeeded(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyStatus")
    def copy_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveHeaderHash")
    def drive_header_hash(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveId")
    def drive_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorLogUri")
    def error_log_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestFile")
    def manifest_file(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestHash")
    def manifest_hash(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestUri")
    def manifest_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentComplete")
    def percent_complete(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verboseLogUri")
    def verbose_log_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EncryptionKeyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kek_type: Optional[_builtins.str] = ..., kek_url: Optional[_builtins.str] = ..., kek_vault_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekType")
    def kek_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekUrl")
    def kek_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekVaultResourceID")
    def kek_vault_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExportResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, blob_list_blob_path: Optional[_builtins.str] = ..., blob_path: Optional[Sequence[_builtins.str]] = ..., blob_path_prefix: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobListBlobPath")
    def blob_list_blob_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobPath")
    def blob_path(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobPathPrefix")
    def blob_path_prefix(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class IdentityDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_drive_manifest: Optional[_builtins.bool] = ..., cancel_requested: Optional[_builtins.bool] = ..., delivery_package: Optional[outputs.DeliveryPackageInformationResponse] = ..., diagnostics_path: Optional[_builtins.str] = ..., drive_list: Optional[Sequence[outputs.DriveStatusResponse]] = ..., encryption_key: Optional[outputs.EncryptionKeyDetailsResponse] = ..., export: Optional[outputs.ExportResponse] = ..., incomplete_blob_list_uri: Optional[_builtins.str] = ..., job_type: Optional[_builtins.str] = ..., log_level: Optional[_builtins.str] = ..., percent_complete: Optional[_builtins.float] = ..., provisioning_state: Optional[_builtins.str] = ..., return_address: Optional[outputs.ReturnAddressResponse] = ..., return_package: Optional[outputs.PackageInformationResponse] = ..., return_shipping: Optional[outputs.ReturnShippingResponse] = ..., shipping_information: Optional[outputs.ShippingInformationResponse] = ..., state: Optional[_builtins.str] = ..., storage_account_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupDriveManifest")
    def backup_drive_manifest(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cancelRequested")
    def cancel_requested(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryPackage")
    def delivery_package(self) -> Optional[outputs.DeliveryPackageInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diagnosticsPath")
    def diagnostics_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveList")
    def drive_list(self) -> Optional[Sequence[outputs.DriveStatusResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[outputs.EncryptionKeyDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def export(self) -> Optional[outputs.ExportResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incompleteBlobListUri")
    def incomplete_blob_list_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentComplete")
    def percent_complete(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnAddress")
    def return_address(self) -> Optional[outputs.ReturnAddressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPackage")
    def return_package(self) -> Optional[outputs.PackageInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnShipping")
    def return_shipping(self) -> Optional[outputs.ReturnShippingResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shippingInformation")
    def shipping_information(self) -> Optional[outputs.ShippingInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PackageInformationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, carrier_name: _builtins.str, drive_count: _builtins.float, ship_date: _builtins.str, tracking_number: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveCount")
    def drive_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shipDate")
    def ship_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingNumber")
    def tracking_number(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ReturnAddressResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, city: _builtins.str, country_or_region: _builtins.str, email: _builtins.str, phone: _builtins.str, postal_code: _builtins.str, recipient_name: _builtins.str, street_address1: _builtins.str, state_or_province: Optional[_builtins.str] = ..., street_address2: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryOrRegion")
    def country_or_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recipientName")
    def recipient_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress1")
    def street_address1(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateOrProvince")
    def state_or_province(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress2")
    def street_address2(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReturnShippingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, carrier_account_number: _builtins.str, carrier_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierAccountNumber")
    def carrier_account_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ShippingInformationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_information: _builtins.str, city: Optional[_builtins.str] = ..., country_or_region: Optional[_builtins.str] = ..., phone: Optional[_builtins.str] = ..., postal_code: Optional[_builtins.str] = ..., recipient_name: Optional[_builtins.str] = ..., state_or_province: Optional[_builtins.str] = ..., street_address1: Optional[_builtins.str] = ..., street_address2: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalInformation")
    def additional_information(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryOrRegion")
    def country_or_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recipientName")
    def recipient_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateOrProvince")
    def state_or_province(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress1")
    def street_address1(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress2")
    def street_address2(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


