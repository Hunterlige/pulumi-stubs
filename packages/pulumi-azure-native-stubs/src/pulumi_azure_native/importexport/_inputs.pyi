

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeliveryPackageInformationArgs', 'DeliveryPackageInformationArgsDict', 'DriveStatusArgs', 'DriveStatusArgsDict', 'EncryptionKeyDetailsArgs', 'EncryptionKeyDetailsArgsDict', 'ExportArgs', 'ExportArgsDict', 'JobDetailsArgs', 'JobDetailsArgsDict', 'PackageInformationArgs', 'PackageInformationArgsDict', 'ReturnAddressArgs', 'ReturnAddressArgsDict', 'ReturnShippingArgs', 'ReturnShippingArgsDict', 'ShippingInformationArgs', 'ShippingInformationArgsDict']
class DeliveryPackageInformationArgsDict(TypedDict):
    
    carrier_name: pulumi.Input[_builtins.str]
    tracking_number: pulumi.Input[_builtins.str]
    drive_count: NotRequired[pulumi.Input[_builtins.float]]
    ship_date: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeliveryPackageInformationArgs:
    def __init__(__self__, *, carrier_name: pulumi.Input[_builtins.str], tracking_number: pulumi.Input[_builtins.str], drive_count: Optional[pulumi.Input[_builtins.float]] = ..., ship_date: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @carrier_name.setter
    def carrier_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingNumber")
    def tracking_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tracking_number.setter
    def tracking_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveCount")
    def drive_count(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @drive_count.setter
    def drive_count(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shipDate")
    def ship_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ship_date.setter
    def ship_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DriveStatusArgsDict(TypedDict):
    
    bit_locker_key: NotRequired[pulumi.Input[_builtins.str]]
    bytes_succeeded: NotRequired[pulumi.Input[_builtins.float]]
    copy_status: NotRequired[pulumi.Input[_builtins.str]]
    drive_header_hash: NotRequired[pulumi.Input[_builtins.str]]
    drive_id: NotRequired[pulumi.Input[_builtins.str]]
    error_log_uri: NotRequired[pulumi.Input[_builtins.str]]
    manifest_file: NotRequired[pulumi.Input[_builtins.str]]
    manifest_hash: NotRequired[pulumi.Input[_builtins.str]]
    manifest_uri: NotRequired[pulumi.Input[_builtins.str]]
    percent_complete: NotRequired[pulumi.Input[_builtins.float]]
    state: NotRequired[pulumi.Input[Union[_builtins.str, DriveState]]]
    verbose_log_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DriveStatusArgs:
    def __init__(__self__, *, bit_locker_key: Optional[pulumi.Input[_builtins.str]] = ..., bytes_succeeded: Optional[pulumi.Input[_builtins.float]] = ..., copy_status: Optional[pulumi.Input[_builtins.str]] = ..., drive_header_hash: Optional[pulumi.Input[_builtins.str]] = ..., drive_id: Optional[pulumi.Input[_builtins.str]] = ..., error_log_uri: Optional[pulumi.Input[_builtins.str]] = ..., manifest_file: Optional[pulumi.Input[_builtins.str]] = ..., manifest_hash: Optional[pulumi.Input[_builtins.str]] = ..., manifest_uri: Optional[pulumi.Input[_builtins.str]] = ..., percent_complete: Optional[pulumi.Input[_builtins.float]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, DriveState]]] = ..., verbose_log_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitLockerKey")
    def bit_locker_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bit_locker_key.setter
    def bit_locker_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bytesSucceeded")
    def bytes_succeeded(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @bytes_succeeded.setter
    def bytes_succeeded(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyStatus")
    def copy_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @copy_status.setter
    def copy_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveHeaderHash")
    def drive_header_hash(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @drive_header_hash.setter
    def drive_header_hash(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveId")
    def drive_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @drive_id.setter
    def drive_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorLogUri")
    def error_log_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_log_uri.setter
    def error_log_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestFile")
    def manifest_file(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @manifest_file.setter
    def manifest_file(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestHash")
    def manifest_hash(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @manifest_hash.setter
    def manifest_hash(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestUri")
    def manifest_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @manifest_uri.setter
    def manifest_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentComplete")
    def percent_complete(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @percent_complete.setter
    def percent_complete(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, DriveState]]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, DriveState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verboseLogUri")
    def verbose_log_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @verbose_log_uri.setter
    def verbose_log_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EncryptionKeyDetailsArgsDict(TypedDict):
    
    kek_type: NotRequired[pulumi.Input[Union[_builtins.str, EncryptionKekType]]]
    kek_url: NotRequired[pulumi.Input[_builtins.str]]
    kek_vault_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EncryptionKeyDetailsArgs:
    def __init__(__self__, *, kek_type: Optional[pulumi.Input[Union[_builtins.str, EncryptionKekType]]] = ..., kek_url: Optional[pulumi.Input[_builtins.str]] = ..., kek_vault_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekType")
    def kek_type(self) -> Optional[pulumi.Input[Union[_builtins.str, EncryptionKekType]]]:
        
        ...
    
    @kek_type.setter
    def kek_type(self, value: Optional[pulumi.Input[Union[_builtins.str, EncryptionKekType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekUrl")
    def kek_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kek_url.setter
    def kek_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekVaultResourceID")
    def kek_vault_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kek_vault_resource_id.setter
    def kek_vault_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExportArgsDict(TypedDict):
    
    blob_list_blob_path: NotRequired[pulumi.Input[_builtins.str]]
    blob_path: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    blob_path_prefix: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ExportArgs:
    def __init__(__self__, *, blob_list_blob_path: Optional[pulumi.Input[_builtins.str]] = ..., blob_path: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., blob_path_prefix: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobListBlobPath")
    def blob_list_blob_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blob_list_blob_path.setter
    def blob_list_blob_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobPath")
    def blob_path(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @blob_path.setter
    def blob_path(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobPathPrefix")
    def blob_path_prefix(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @blob_path_prefix.setter
    def blob_path_prefix(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class JobDetailsArgsDict(TypedDict):
    
    backup_drive_manifest: NotRequired[pulumi.Input[_builtins.bool]]
    cancel_requested: NotRequired[pulumi.Input[_builtins.bool]]
    delivery_package: NotRequired[pulumi.Input[DeliveryPackageInformationArgsDict]]
    diagnostics_path: NotRequired[pulumi.Input[_builtins.str]]
    drive_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[DriveStatusArgsDict]]]]
    encryption_key: NotRequired[pulumi.Input[EncryptionKeyDetailsArgsDict]]
    export: NotRequired[pulumi.Input[ExportArgsDict]]
    incomplete_blob_list_uri: NotRequired[pulumi.Input[_builtins.str]]
    job_type: NotRequired[pulumi.Input[_builtins.str]]
    log_level: NotRequired[pulumi.Input[_builtins.str]]
    percent_complete: NotRequired[pulumi.Input[_builtins.float]]
    provisioning_state: NotRequired[pulumi.Input[_builtins.str]]
    return_address: NotRequired[pulumi.Input[ReturnAddressArgsDict]]
    return_package: NotRequired[pulumi.Input[PackageInformationArgsDict]]
    return_shipping: NotRequired[pulumi.Input[ReturnShippingArgsDict]]
    shipping_information: NotRequired[pulumi.Input[ShippingInformationArgsDict]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobDetailsArgs:
    def __init__(__self__, *, backup_drive_manifest: Optional[pulumi.Input[_builtins.bool]] = ..., cancel_requested: Optional[pulumi.Input[_builtins.bool]] = ..., delivery_package: Optional[pulumi.Input[DeliveryPackageInformationArgs]] = ..., diagnostics_path: Optional[pulumi.Input[_builtins.str]] = ..., drive_list: Optional[pulumi.Input[Sequence[pulumi.Input[DriveStatusArgs]]]] = ..., encryption_key: Optional[pulumi.Input[EncryptionKeyDetailsArgs]] = ..., export: Optional[pulumi.Input[ExportArgs]] = ..., incomplete_blob_list_uri: Optional[pulumi.Input[_builtins.str]] = ..., job_type: Optional[pulumi.Input[_builtins.str]] = ..., log_level: Optional[pulumi.Input[_builtins.str]] = ..., percent_complete: Optional[pulumi.Input[_builtins.float]] = ..., provisioning_state: Optional[pulumi.Input[_builtins.str]] = ..., return_address: Optional[pulumi.Input[ReturnAddressArgs]] = ..., return_package: Optional[pulumi.Input[PackageInformationArgs]] = ..., return_shipping: Optional[pulumi.Input[ReturnShippingArgs]] = ..., shipping_information: Optional[pulumi.Input[ShippingInformationArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupDriveManifest")
    def backup_drive_manifest(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @backup_drive_manifest.setter
    def backup_drive_manifest(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cancelRequested")
    def cancel_requested(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cancel_requested.setter
    def cancel_requested(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryPackage")
    def delivery_package(self) -> Optional[pulumi.Input[DeliveryPackageInformationArgs]]:
        
        ...
    
    @delivery_package.setter
    def delivery_package(self, value: Optional[pulumi.Input[DeliveryPackageInformationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diagnosticsPath")
    def diagnostics_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @diagnostics_path.setter
    def diagnostics_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveList")
    def drive_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DriveStatusArgs]]]]:
        
        ...
    
    @drive_list.setter
    def drive_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DriveStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input[EncryptionKeyDetailsArgs]]:
        
        ...
    
    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input[EncryptionKeyDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def export(self) -> Optional[pulumi.Input[ExportArgs]]:
        
        ...
    
    @export.setter
    def export(self, value: Optional[pulumi.Input[ExportArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incompleteBlobListUri")
    def incomplete_blob_list_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @incomplete_blob_list_uri.setter
    def incomplete_blob_list_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_type.setter
    def job_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentComplete")
    def percent_complete(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @percent_complete.setter
    def percent_complete(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnAddress")
    def return_address(self) -> Optional[pulumi.Input[ReturnAddressArgs]]:
        
        ...
    
    @return_address.setter
    def return_address(self, value: Optional[pulumi.Input[ReturnAddressArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPackage")
    def return_package(self) -> Optional[pulumi.Input[PackageInformationArgs]]:
        
        ...
    
    @return_package.setter
    def return_package(self, value: Optional[pulumi.Input[PackageInformationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnShipping")
    def return_shipping(self) -> Optional[pulumi.Input[ReturnShippingArgs]]:
        
        ...
    
    @return_shipping.setter
    def return_shipping(self, value: Optional[pulumi.Input[ReturnShippingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shippingInformation")
    def shipping_information(self) -> Optional[pulumi.Input[ShippingInformationArgs]]:
        
        ...
    
    @shipping_information.setter
    def shipping_information(self, value: Optional[pulumi.Input[ShippingInformationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PackageInformationArgsDict(TypedDict):
    
    carrier_name: pulumi.Input[_builtins.str]
    drive_count: pulumi.Input[_builtins.float]
    ship_date: pulumi.Input[_builtins.str]
    tracking_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class PackageInformationArgs:
    def __init__(__self__, *, carrier_name: pulumi.Input[_builtins.str], drive_count: pulumi.Input[_builtins.float], ship_date: pulumi.Input[_builtins.str], tracking_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @carrier_name.setter
    def carrier_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveCount")
    def drive_count(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @drive_count.setter
    def drive_count(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shipDate")
    def ship_date(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ship_date.setter
    def ship_date(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingNumber")
    def tracking_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tracking_number.setter
    def tracking_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ReturnAddressArgsDict(TypedDict):
    
    city: pulumi.Input[_builtins.str]
    country_or_region: pulumi.Input[_builtins.str]
    email: pulumi.Input[_builtins.str]
    phone: pulumi.Input[_builtins.str]
    postal_code: pulumi.Input[_builtins.str]
    recipient_name: pulumi.Input[_builtins.str]
    street_address1: pulumi.Input[_builtins.str]
    state_or_province: NotRequired[pulumi.Input[_builtins.str]]
    street_address2: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ReturnAddressArgs:
    def __init__(__self__, *, city: pulumi.Input[_builtins.str], country_or_region: pulumi.Input[_builtins.str], email: pulumi.Input[_builtins.str], phone: pulumi.Input[_builtins.str], postal_code: pulumi.Input[_builtins.str], recipient_name: pulumi.Input[_builtins.str], street_address1: pulumi.Input[_builtins.str], state_or_province: Optional[pulumi.Input[_builtins.str]] = ..., street_address2: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @city.setter
    def city(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryOrRegion")
    def country_or_region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @country_or_region.setter
    def country_or_region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone.setter
    def phone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @postal_code.setter
    def postal_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recipientName")
    def recipient_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @recipient_name.setter
    def recipient_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress1")
    def street_address1(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @street_address1.setter
    def street_address1(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateOrProvince")
    def state_or_province(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_or_province.setter
    def state_or_province(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress2")
    def street_address2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @street_address2.setter
    def street_address2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ReturnShippingArgsDict(TypedDict):
    
    carrier_account_number: pulumi.Input[_builtins.str]
    carrier_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class ReturnShippingArgs:
    def __init__(__self__, *, carrier_account_number: pulumi.Input[_builtins.str], carrier_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierAccountNumber")
    def carrier_account_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @carrier_account_number.setter
    def carrier_account_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @carrier_name.setter
    def carrier_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ShippingInformationArgsDict(TypedDict):
    
    city: NotRequired[pulumi.Input[_builtins.str]]
    country_or_region: NotRequired[pulumi.Input[_builtins.str]]
    phone: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    recipient_name: NotRequired[pulumi.Input[_builtins.str]]
    state_or_province: NotRequired[pulumi.Input[_builtins.str]]
    street_address1: NotRequired[pulumi.Input[_builtins.str]]
    street_address2: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ShippingInformationArgs:
    def __init__(__self__, *, city: Optional[pulumi.Input[_builtins.str]] = ..., country_or_region: Optional[pulumi.Input[_builtins.str]] = ..., phone: Optional[pulumi.Input[_builtins.str]] = ..., postal_code: Optional[pulumi.Input[_builtins.str]] = ..., recipient_name: Optional[pulumi.Input[_builtins.str]] = ..., state_or_province: Optional[pulumi.Input[_builtins.str]] = ..., street_address1: Optional[pulumi.Input[_builtins.str]] = ..., street_address2: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryOrRegion")
    def country_or_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country_or_region.setter
    def country_or_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone.setter
    def phone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recipientName")
    def recipient_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recipient_name.setter
    def recipient_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateOrProvince")
    def state_or_province(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_or_province.setter
    def state_or_province(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress1")
    def street_address1(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @street_address1.setter
    def street_address1(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress2")
    def street_address2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @street_address2.setter
    def street_address2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


