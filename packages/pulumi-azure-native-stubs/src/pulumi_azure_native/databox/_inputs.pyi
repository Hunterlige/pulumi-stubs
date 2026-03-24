

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AzureFileFilterDetailsArgs', 'AzureFileFilterDetailsArgsDict', 'BlobFilterDetailsArgs', 'BlobFilterDetailsArgsDict', 'ContactDetailsArgs', 'ContactDetailsArgsDict', 'ContactInfoArgs', 'ContactInfoArgsDict', 'DataBoxCustomerDiskJobDetailsArgs', 'DataBoxCustomerDiskJobDetailsArgsDict', 'DataBoxDiskJobDetailsArgs', 'DataBoxDiskJobDetailsArgsDict', 'DataBoxHeavyJobDetailsArgs', 'DataBoxHeavyJobDetailsArgsDict', 'DataBoxJobDetailsArgs', 'DataBoxJobDetailsArgsDict', 'DataExportDetailsArgs', 'DataExportDetailsArgsDict', 'DataImportDetailsArgs', 'DataImportDetailsArgsDict', 'EncryptionPreferencesArgs', 'EncryptionPreferencesArgsDict', 'FilterFileDetailsArgs', 'FilterFileDetailsArgsDict', 'IdentityPropertiesArgs', 'IdentityPropertiesArgsDict', 'ImportDiskDetailsArgs', 'ImportDiskDetailsArgsDict', 'JobDeliveryInfoArgs', 'JobDeliveryInfoArgsDict', 'KeyEncryptionKeyArgs', 'KeyEncryptionKeyArgsDict', 'ManagedDiskDetailsArgs', 'ManagedDiskDetailsArgsDict', 'NotificationPreferenceArgs', 'NotificationPreferenceArgsDict', 'PackageCarrierDetailsArgs', 'PackageCarrierDetailsArgsDict', 'PreferencesArgs', 'PreferencesArgsDict', 'ResourceIdentityArgs', 'ResourceIdentityArgsDict', 'ReverseShippingDetailsArgs', 'ReverseShippingDetailsArgsDict', 'ShippingAddressArgs', 'ShippingAddressArgsDict', 'SkuArgs', 'SkuArgsDict', 'StorageAccountDetailsArgs', 'StorageAccountDetailsArgsDict', 'TransferAllDetailsArgs', 'TransferAllDetailsArgsDict', 'TransferConfigurationTransferAllDetailsArgs', 'TransferConfigurationTransferAllDetailsArgsDict', 'TransferConfigurationTransferFilterDetailsArgs', 'TransferConfigurationTransferFilterDetailsArgsDict', 'TransferConfigurationArgs', 'TransferConfigurationArgsDict', 'TransferFilterDetailsArgs', 'TransferFilterDetailsArgsDict', 'TransportPreferencesArgs', 'TransportPreferencesArgsDict', 'UserAssignedPropertiesArgs', 'UserAssignedPropertiesArgsDict']
class AzureFileFilterDetailsArgsDict(TypedDict):
    
    file_path_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_prefix_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_share_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AzureFileFilterDetailsArgs:
    def __init__(__self__, *, file_path_list: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., file_prefix_list: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., file_share_list: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePathList")
    def file_path_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @file_path_list.setter
    def file_path_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePrefixList")
    def file_prefix_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @file_prefix_list.setter
    def file_prefix_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShareList")
    def file_share_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @file_share_list.setter
    def file_share_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BlobFilterDetailsArgsDict(TypedDict):
    
    blob_path_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    blob_prefix_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    container_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BlobFilterDetailsArgs:
    def __init__(__self__, *, blob_path_list: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., blob_prefix_list: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., container_list: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobPathList")
    def blob_path_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @blob_path_list.setter
    def blob_path_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobPrefixList")
    def blob_prefix_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @blob_prefix_list.setter
    def blob_prefix_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerList")
    def container_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @container_list.setter
    def container_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ContactDetailsArgsDict(TypedDict):
    
    contact_name: pulumi.Input[_builtins.str]
    email_list: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    phone: pulumi.Input[_builtins.str]
    mobile: NotRequired[pulumi.Input[_builtins.str]]
    notification_preference: NotRequired[pulumi.Input[Sequence[pulumi.Input[NotificationPreferenceArgsDict]]]]
    phone_extension: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContactDetailsArgs:
    def __init__(__self__, *, contact_name: pulumi.Input[_builtins.str], email_list: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], phone: pulumi.Input[_builtins.str], mobile: Optional[pulumi.Input[_builtins.str]] = ..., notification_preference: Optional[pulumi.Input[Sequence[pulumi.Input[NotificationPreferenceArgs]]]] = ..., phone_extension: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactName")
    def contact_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @contact_name.setter
    def contact_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailList")
    def email_list(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @email_list.setter
    def email_list(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone.setter
    def phone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mobile(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mobile.setter
    def mobile(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationPreference")
    def notification_preference(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NotificationPreferenceArgs]]]]:
        
        ...
    
    @notification_preference.setter
    def notification_preference(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NotificationPreferenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneExtension")
    def phone_extension(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_extension.setter
    def phone_extension(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContactInfoArgsDict(TypedDict):
    
    contact_name: pulumi.Input[_builtins.str]
    phone: pulumi.Input[_builtins.str]
    mobile: NotRequired[pulumi.Input[_builtins.str]]
    phone_extension: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContactInfoArgs:
    def __init__(__self__, *, contact_name: pulumi.Input[_builtins.str], phone: pulumi.Input[_builtins.str], mobile: Optional[pulumi.Input[_builtins.str]] = ..., phone_extension: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactName")
    def contact_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @contact_name.setter
    def contact_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone.setter
    def phone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mobile(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mobile.setter
    def mobile(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneExtension")
    def phone_extension(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_extension.setter
    def phone_extension(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataBoxCustomerDiskJobDetailsArgsDict(TypedDict):
    
    contact_details: pulumi.Input[ContactDetailsArgsDict]
    job_details_type: pulumi.Input[_builtins.str]
    return_to_customer_package_details: pulumi.Input[PackageCarrierDetailsArgsDict]
    data_export_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgsDict]]]]
    data_import_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgsDict]]]]
    enable_manifest_backup: NotRequired[pulumi.Input[_builtins.bool]]
    expected_data_size_in_tera_bytes: NotRequired[pulumi.Input[_builtins.int]]
    import_disk_details_collection: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[ImportDiskDetailsArgsDict]]]]
    key_encryption_key: NotRequired[pulumi.Input[KeyEncryptionKeyArgsDict]]
    preferences: NotRequired[pulumi.Input[PreferencesArgsDict]]
    reverse_shipping_details: NotRequired[pulumi.Input[ReverseShippingDetailsArgsDict]]
    shipping_address: NotRequired[pulumi.Input[ShippingAddressArgsDict]]


@pulumi.input_type
class DataBoxCustomerDiskJobDetailsArgs:
    def __init__(__self__, *, contact_details: pulumi.Input[ContactDetailsArgs], job_details_type: pulumi.Input[_builtins.str], return_to_customer_package_details: pulumi.Input[PackageCarrierDetailsArgs], data_export_details: Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]] = ..., data_import_details: Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]] = ..., enable_manifest_backup: Optional[pulumi.Input[_builtins.bool]] = ..., expected_data_size_in_tera_bytes: Optional[pulumi.Input[_builtins.int]] = ..., import_disk_details_collection: Optional[pulumi.Input[Mapping[str, pulumi.Input[ImportDiskDetailsArgs]]]] = ..., key_encryption_key: Optional[pulumi.Input[KeyEncryptionKeyArgs]] = ..., preferences: Optional[pulumi.Input[PreferencesArgs]] = ..., reverse_shipping_details: Optional[pulumi.Input[ReverseShippingDetailsArgs]] = ..., shipping_address: Optional[pulumi.Input[ShippingAddressArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> pulumi.Input[ContactDetailsArgs]:
        
        ...
    
    @contact_details.setter
    def contact_details(self, value: pulumi.Input[ContactDetailsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobDetailsType")
    def job_details_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @job_details_type.setter
    def job_details_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnToCustomerPackageDetails")
    def return_to_customer_package_details(self) -> pulumi.Input[PackageCarrierDetailsArgs]:
        
        ...
    
    @return_to_customer_package_details.setter
    def return_to_customer_package_details(self, value: pulumi.Input[PackageCarrierDetailsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExportDetails")
    def data_export_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]]:
        
        ...
    
    @data_export_details.setter
    def data_export_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataImportDetails")
    def data_import_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]]:
        
        ...
    
    @data_import_details.setter
    def data_import_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableManifestBackup")
    def enable_manifest_backup(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_manifest_backup.setter
    def enable_manifest_backup(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedDataSizeInTeraBytes")
    def expected_data_size_in_tera_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @expected_data_size_in_tera_bytes.setter
    def expected_data_size_in_tera_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importDiskDetailsCollection")
    def import_disk_details_collection(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[ImportDiskDetailsArgs]]]]:
        
        ...
    
    @import_disk_details_collection.setter
    def import_disk_details_collection(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[ImportDiskDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[pulumi.Input[KeyEncryptionKeyArgs]]:
        
        ...
    
    @key_encryption_key.setter
    def key_encryption_key(self, value: Optional[pulumi.Input[KeyEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preferences(self) -> Optional[pulumi.Input[PreferencesArgs]]:
        
        ...
    
    @preferences.setter
    def preferences(self, value: Optional[pulumi.Input[PreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseShippingDetails")
    def reverse_shipping_details(self) -> Optional[pulumi.Input[ReverseShippingDetailsArgs]]:
        
        ...
    
    @reverse_shipping_details.setter
    def reverse_shipping_details(self, value: Optional[pulumi.Input[ReverseShippingDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input[ShippingAddressArgs]]:
        
        ...
    
    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input[ShippingAddressArgs]]): # -> None:
        ...
    


class DataBoxDiskJobDetailsArgsDict(TypedDict):
    
    contact_details: pulumi.Input[ContactDetailsArgsDict]
    job_details_type: pulumi.Input[_builtins.str]
    data_export_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgsDict]]]]
    data_import_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgsDict]]]]
    expected_data_size_in_tera_bytes: NotRequired[pulumi.Input[_builtins.int]]
    key_encryption_key: NotRequired[pulumi.Input[KeyEncryptionKeyArgsDict]]
    passkey: NotRequired[pulumi.Input[_builtins.str]]
    preferences: NotRequired[pulumi.Input[PreferencesArgsDict]]
    preferred_disks: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]
    reverse_shipping_details: NotRequired[pulumi.Input[ReverseShippingDetailsArgsDict]]
    shipping_address: NotRequired[pulumi.Input[ShippingAddressArgsDict]]


@pulumi.input_type
class DataBoxDiskJobDetailsArgs:
    def __init__(__self__, *, contact_details: pulumi.Input[ContactDetailsArgs], job_details_type: pulumi.Input[_builtins.str], data_export_details: Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]] = ..., data_import_details: Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]] = ..., expected_data_size_in_tera_bytes: Optional[pulumi.Input[_builtins.int]] = ..., key_encryption_key: Optional[pulumi.Input[KeyEncryptionKeyArgs]] = ..., passkey: Optional[pulumi.Input[_builtins.str]] = ..., preferences: Optional[pulumi.Input[PreferencesArgs]] = ..., preferred_disks: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]] = ..., reverse_shipping_details: Optional[pulumi.Input[ReverseShippingDetailsArgs]] = ..., shipping_address: Optional[pulumi.Input[ShippingAddressArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> pulumi.Input[ContactDetailsArgs]:
        
        ...
    
    @contact_details.setter
    def contact_details(self, value: pulumi.Input[ContactDetailsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobDetailsType")
    def job_details_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @job_details_type.setter
    def job_details_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExportDetails")
    def data_export_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]]:
        
        ...
    
    @data_export_details.setter
    def data_export_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataImportDetails")
    def data_import_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]]:
        
        ...
    
    @data_import_details.setter
    def data_import_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedDataSizeInTeraBytes")
    def expected_data_size_in_tera_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @expected_data_size_in_tera_bytes.setter
    def expected_data_size_in_tera_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[pulumi.Input[KeyEncryptionKeyArgs]]:
        
        ...
    
    @key_encryption_key.setter
    def key_encryption_key(self, value: Optional[pulumi.Input[KeyEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def passkey(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @passkey.setter
    def passkey(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preferences(self) -> Optional[pulumi.Input[PreferencesArgs]]:
        
        ...
    
    @preferences.setter
    def preferences(self, value: Optional[pulumi.Input[PreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredDisks")
    def preferred_disks(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @preferred_disks.setter
    def preferred_disks(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseShippingDetails")
    def reverse_shipping_details(self) -> Optional[pulumi.Input[ReverseShippingDetailsArgs]]:
        
        ...
    
    @reverse_shipping_details.setter
    def reverse_shipping_details(self, value: Optional[pulumi.Input[ReverseShippingDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input[ShippingAddressArgs]]:
        
        ...
    
    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input[ShippingAddressArgs]]): # -> None:
        ...
    


class DataBoxHeavyJobDetailsArgsDict(TypedDict):
    
    contact_details: pulumi.Input[ContactDetailsArgsDict]
    job_details_type: pulumi.Input[_builtins.str]
    data_export_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgsDict]]]]
    data_import_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgsDict]]]]
    device_password: NotRequired[pulumi.Input[_builtins.str]]
    expected_data_size_in_tera_bytes: NotRequired[pulumi.Input[_builtins.int]]
    key_encryption_key: NotRequired[pulumi.Input[KeyEncryptionKeyArgsDict]]
    preferences: NotRequired[pulumi.Input[PreferencesArgsDict]]
    reverse_shipping_details: NotRequired[pulumi.Input[ReverseShippingDetailsArgsDict]]
    shipping_address: NotRequired[pulumi.Input[ShippingAddressArgsDict]]


@pulumi.input_type
class DataBoxHeavyJobDetailsArgs:
    def __init__(__self__, *, contact_details: pulumi.Input[ContactDetailsArgs], job_details_type: pulumi.Input[_builtins.str], data_export_details: Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]] = ..., data_import_details: Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]] = ..., device_password: Optional[pulumi.Input[_builtins.str]] = ..., expected_data_size_in_tera_bytes: Optional[pulumi.Input[_builtins.int]] = ..., key_encryption_key: Optional[pulumi.Input[KeyEncryptionKeyArgs]] = ..., preferences: Optional[pulumi.Input[PreferencesArgs]] = ..., reverse_shipping_details: Optional[pulumi.Input[ReverseShippingDetailsArgs]] = ..., shipping_address: Optional[pulumi.Input[ShippingAddressArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> pulumi.Input[ContactDetailsArgs]:
        
        ...
    
    @contact_details.setter
    def contact_details(self, value: pulumi.Input[ContactDetailsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobDetailsType")
    def job_details_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @job_details_type.setter
    def job_details_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExportDetails")
    def data_export_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]]:
        
        ...
    
    @data_export_details.setter
    def data_export_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataImportDetails")
    def data_import_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]]:
        
        ...
    
    @data_import_details.setter
    def data_import_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="devicePassword")
    def device_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_password.setter
    def device_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedDataSizeInTeraBytes")
    def expected_data_size_in_tera_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @expected_data_size_in_tera_bytes.setter
    def expected_data_size_in_tera_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[pulumi.Input[KeyEncryptionKeyArgs]]:
        
        ...
    
    @key_encryption_key.setter
    def key_encryption_key(self, value: Optional[pulumi.Input[KeyEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preferences(self) -> Optional[pulumi.Input[PreferencesArgs]]:
        
        ...
    
    @preferences.setter
    def preferences(self, value: Optional[pulumi.Input[PreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseShippingDetails")
    def reverse_shipping_details(self) -> Optional[pulumi.Input[ReverseShippingDetailsArgs]]:
        
        ...
    
    @reverse_shipping_details.setter
    def reverse_shipping_details(self, value: Optional[pulumi.Input[ReverseShippingDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input[ShippingAddressArgs]]:
        
        ...
    
    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input[ShippingAddressArgs]]): # -> None:
        ...
    


class DataBoxJobDetailsArgsDict(TypedDict):
    
    contact_details: pulumi.Input[ContactDetailsArgsDict]
    job_details_type: pulumi.Input[_builtins.str]
    data_export_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgsDict]]]]
    data_import_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgsDict]]]]
    device_password: NotRequired[pulumi.Input[_builtins.str]]
    expected_data_size_in_tera_bytes: NotRequired[pulumi.Input[_builtins.int]]
    key_encryption_key: NotRequired[pulumi.Input[KeyEncryptionKeyArgsDict]]
    preferences: NotRequired[pulumi.Input[PreferencesArgsDict]]
    reverse_shipping_details: NotRequired[pulumi.Input[ReverseShippingDetailsArgsDict]]
    shipping_address: NotRequired[pulumi.Input[ShippingAddressArgsDict]]


@pulumi.input_type
class DataBoxJobDetailsArgs:
    def __init__(__self__, *, contact_details: pulumi.Input[ContactDetailsArgs], job_details_type: pulumi.Input[_builtins.str], data_export_details: Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]] = ..., data_import_details: Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]] = ..., device_password: Optional[pulumi.Input[_builtins.str]] = ..., expected_data_size_in_tera_bytes: Optional[pulumi.Input[_builtins.int]] = ..., key_encryption_key: Optional[pulumi.Input[KeyEncryptionKeyArgs]] = ..., preferences: Optional[pulumi.Input[PreferencesArgs]] = ..., reverse_shipping_details: Optional[pulumi.Input[ReverseShippingDetailsArgs]] = ..., shipping_address: Optional[pulumi.Input[ShippingAddressArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> pulumi.Input[ContactDetailsArgs]:
        
        ...
    
    @contact_details.setter
    def contact_details(self, value: pulumi.Input[ContactDetailsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobDetailsType")
    def job_details_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @job_details_type.setter
    def job_details_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExportDetails")
    def data_export_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]]:
        
        ...
    
    @data_export_details.setter
    def data_export_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataExportDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataImportDetails")
    def data_import_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]]:
        
        ...
    
    @data_import_details.setter
    def data_import_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataImportDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="devicePassword")
    def device_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_password.setter
    def device_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedDataSizeInTeraBytes")
    def expected_data_size_in_tera_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @expected_data_size_in_tera_bytes.setter
    def expected_data_size_in_tera_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[pulumi.Input[KeyEncryptionKeyArgs]]:
        
        ...
    
    @key_encryption_key.setter
    def key_encryption_key(self, value: Optional[pulumi.Input[KeyEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preferences(self) -> Optional[pulumi.Input[PreferencesArgs]]:
        
        ...
    
    @preferences.setter
    def preferences(self, value: Optional[pulumi.Input[PreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseShippingDetails")
    def reverse_shipping_details(self) -> Optional[pulumi.Input[ReverseShippingDetailsArgs]]:
        
        ...
    
    @reverse_shipping_details.setter
    def reverse_shipping_details(self, value: Optional[pulumi.Input[ReverseShippingDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input[ShippingAddressArgs]]:
        
        ...
    
    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input[ShippingAddressArgs]]): # -> None:
        ...
    


class DataExportDetailsArgsDict(TypedDict):
    
    account_details: pulumi.Input[Union[ManagedDiskDetailsArgsDict, StorageAccountDetailsArgsDict]]
    transfer_configuration: pulumi.Input[TransferConfigurationArgsDict]
    log_collection_level: NotRequired[pulumi.Input[Union[_builtins.str, LogCollectionLevel]]]


@pulumi.input_type
class DataExportDetailsArgs:
    def __init__(__self__, *, account_details: pulumi.Input[Union[ManagedDiskDetailsArgs, StorageAccountDetailsArgs]], transfer_configuration: pulumi.Input[TransferConfigurationArgs], log_collection_level: Optional[pulumi.Input[Union[_builtins.str, LogCollectionLevel]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountDetails")
    def account_details(self) -> pulumi.Input[Union[ManagedDiskDetailsArgs, StorageAccountDetailsArgs]]:
        
        ...
    
    @account_details.setter
    def account_details(self, value: pulumi.Input[Union[ManagedDiskDetailsArgs, StorageAccountDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferConfiguration")
    def transfer_configuration(self) -> pulumi.Input[TransferConfigurationArgs]:
        
        ...
    
    @transfer_configuration.setter
    def transfer_configuration(self, value: pulumi.Input[TransferConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logCollectionLevel")
    def log_collection_level(self) -> Optional[pulumi.Input[Union[_builtins.str, LogCollectionLevel]]]:
        
        ...
    
    @log_collection_level.setter
    def log_collection_level(self, value: Optional[pulumi.Input[Union[_builtins.str, LogCollectionLevel]]]): # -> None:
        ...
    


class DataImportDetailsArgsDict(TypedDict):
    
    account_details: pulumi.Input[Union[ManagedDiskDetailsArgsDict, StorageAccountDetailsArgsDict]]
    log_collection_level: NotRequired[pulumi.Input[Union[_builtins.str, LogCollectionLevel]]]


@pulumi.input_type
class DataImportDetailsArgs:
    def __init__(__self__, *, account_details: pulumi.Input[Union[ManagedDiskDetailsArgs, StorageAccountDetailsArgs]], log_collection_level: Optional[pulumi.Input[Union[_builtins.str, LogCollectionLevel]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountDetails")
    def account_details(self) -> pulumi.Input[Union[ManagedDiskDetailsArgs, StorageAccountDetailsArgs]]:
        
        ...
    
    @account_details.setter
    def account_details(self, value: pulumi.Input[Union[ManagedDiskDetailsArgs, StorageAccountDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logCollectionLevel")
    def log_collection_level(self) -> Optional[pulumi.Input[Union[_builtins.str, LogCollectionLevel]]]:
        
        ...
    
    @log_collection_level.setter
    def log_collection_level(self, value: Optional[pulumi.Input[Union[_builtins.str, LogCollectionLevel]]]): # -> None:
        ...
    


class EncryptionPreferencesArgsDict(TypedDict):
    
    double_encryption: NotRequired[pulumi.Input[Union[_builtins.str, DoubleEncryption]]]
    hardware_encryption: NotRequired[pulumi.Input[Union[_builtins.str, HardwareEncryption]]]


@pulumi.input_type
class EncryptionPreferencesArgs:
    def __init__(__self__, *, double_encryption: Optional[pulumi.Input[Union[_builtins.str, DoubleEncryption]]] = ..., hardware_encryption: Optional[pulumi.Input[Union[_builtins.str, HardwareEncryption]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="doubleEncryption")
    def double_encryption(self) -> Optional[pulumi.Input[Union[_builtins.str, DoubleEncryption]]]:
        
        ...
    
    @double_encryption.setter
    def double_encryption(self, value: Optional[pulumi.Input[Union[_builtins.str, DoubleEncryption]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareEncryption")
    def hardware_encryption(self) -> Optional[pulumi.Input[Union[_builtins.str, HardwareEncryption]]]:
        
        ...
    
    @hardware_encryption.setter
    def hardware_encryption(self, value: Optional[pulumi.Input[Union[_builtins.str, HardwareEncryption]]]): # -> None:
        ...
    


class FilterFileDetailsArgsDict(TypedDict):
    
    filter_file_path: pulumi.Input[_builtins.str]
    filter_file_type: pulumi.Input[Union[_builtins.str, FilterFileType]]


@pulumi.input_type
class FilterFileDetailsArgs:
    def __init__(__self__, *, filter_file_path: pulumi.Input[_builtins.str], filter_file_type: pulumi.Input[Union[_builtins.str, FilterFileType]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterFilePath")
    def filter_file_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter_file_path.setter
    def filter_file_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterFileType")
    def filter_file_type(self) -> pulumi.Input[Union[_builtins.str, FilterFileType]]:
        
        ...
    
    @filter_file_type.setter
    def filter_file_type(self, value: pulumi.Input[Union[_builtins.str, FilterFileType]]): # -> None:
        ...
    


class IdentityPropertiesArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[_builtins.str]]
    user_assigned: NotRequired[pulumi.Input[UserAssignedPropertiesArgsDict]]


@pulumi.input_type
class IdentityPropertiesArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ..., user_assigned: Optional[pulumi.Input[UserAssignedPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssigned")
    def user_assigned(self) -> Optional[pulumi.Input[UserAssignedPropertiesArgs]]:
        
        ...
    
    @user_assigned.setter
    def user_assigned(self, value: Optional[pulumi.Input[UserAssignedPropertiesArgs]]): # -> None:
        ...
    


class ImportDiskDetailsArgsDict(TypedDict):
    
    bit_locker_key: pulumi.Input[_builtins.str]
    manifest_file: pulumi.Input[_builtins.str]
    manifest_hash: pulumi.Input[_builtins.str]


@pulumi.input_type
class ImportDiskDetailsArgs:
    def __init__(__self__, *, bit_locker_key: pulumi.Input[_builtins.str], manifest_file: pulumi.Input[_builtins.str], manifest_hash: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitLockerKey")
    def bit_locker_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bit_locker_key.setter
    def bit_locker_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestFile")
    def manifest_file(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @manifest_file.setter
    def manifest_file(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestHash")
    def manifest_hash(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @manifest_hash.setter
    def manifest_hash(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobDeliveryInfoArgsDict(TypedDict):
    
    scheduled_date_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobDeliveryInfoArgs:
    def __init__(__self__, *, scheduled_date_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledDateTime")
    def scheduled_date_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scheduled_date_time.setter
    def scheduled_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeyEncryptionKeyArgsDict(TypedDict):
    
    kek_type: pulumi.Input[Union[_builtins.str, KekType]]
    identity_properties: NotRequired[pulumi.Input[IdentityPropertiesArgsDict]]
    kek_url: NotRequired[pulumi.Input[_builtins.str]]
    kek_vault_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyEncryptionKeyArgs:
    def __init__(__self__, *, kek_type: Optional[pulumi.Input[Union[_builtins.str, KekType]]] = ..., identity_properties: Optional[pulumi.Input[IdentityPropertiesArgs]] = ..., kek_url: Optional[pulumi.Input[_builtins.str]] = ..., kek_vault_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekType")
    def kek_type(self) -> pulumi.Input[Union[_builtins.str, KekType]]:
        
        ...
    
    @kek_type.setter
    def kek_type(self, value: pulumi.Input[Union[_builtins.str, KekType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProperties")
    def identity_properties(self) -> Optional[pulumi.Input[IdentityPropertiesArgs]]:
        
        ...
    
    @identity_properties.setter
    def identity_properties(self, value: Optional[pulumi.Input[IdentityPropertiesArgs]]): # -> None:
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
    


class ManagedDiskDetailsArgsDict(TypedDict):
    
    data_account_type: pulumi.Input[_builtins.str]
    resource_group_id: pulumi.Input[_builtins.str]
    staging_storage_account_id: pulumi.Input[_builtins.str]
    share_password: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedDiskDetailsArgs:
    def __init__(__self__, *, data_account_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_id: pulumi.Input[_builtins.str], staging_storage_account_id: pulumi.Input[_builtins.str], share_password: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_account_type.setter
    def data_account_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_id.setter
    def resource_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingStorageAccountId")
    def staging_storage_account_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @staging_storage_account_id.setter
    def staging_storage_account_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharePassword")
    def share_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @share_password.setter
    def share_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NotificationPreferenceArgsDict(TypedDict):
    
    send_notification: pulumi.Input[_builtins.bool]
    stage_name: pulumi.Input[Union[_builtins.str, NotificationStageName]]


@pulumi.input_type
class NotificationPreferenceArgs:
    def __init__(__self__, *, send_notification: Optional[pulumi.Input[_builtins.bool]] = ..., stage_name: pulumi.Input[Union[_builtins.str, NotificationStageName]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendNotification")
    def send_notification(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @send_notification.setter
    def send_notification(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Input[Union[_builtins.str, NotificationStageName]]:
        
        ...
    
    @stage_name.setter
    def stage_name(self, value: pulumi.Input[Union[_builtins.str, NotificationStageName]]): # -> None:
        ...
    


class PackageCarrierDetailsArgsDict(TypedDict):
    
    carrier_account_number: NotRequired[pulumi.Input[_builtins.str]]
    carrier_name: NotRequired[pulumi.Input[_builtins.str]]
    tracking_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PackageCarrierDetailsArgs:
    def __init__(__self__, *, carrier_account_number: Optional[pulumi.Input[_builtins.str]] = ..., carrier_name: Optional[pulumi.Input[_builtins.str]] = ..., tracking_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierAccountNumber")
    def carrier_account_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @carrier_account_number.setter
    def carrier_account_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @carrier_name.setter
    def carrier_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingId")
    def tracking_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tracking_id.setter
    def tracking_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PreferencesArgsDict(TypedDict):
    
    encryption_preferences: NotRequired[pulumi.Input[EncryptionPreferencesArgsDict]]
    preferred_data_center_region: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    reverse_transport_preferences: NotRequired[pulumi.Input[TransportPreferencesArgsDict]]
    storage_account_access_tier_preferences: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, StorageAccountAccessTier]]]]]
    transport_preferences: NotRequired[pulumi.Input[TransportPreferencesArgsDict]]


@pulumi.input_type
class PreferencesArgs:
    def __init__(__self__, *, encryption_preferences: Optional[pulumi.Input[EncryptionPreferencesArgs]] = ..., preferred_data_center_region: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., reverse_transport_preferences: Optional[pulumi.Input[TransportPreferencesArgs]] = ..., storage_account_access_tier_preferences: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, StorageAccountAccessTier]]]]] = ..., transport_preferences: Optional[pulumi.Input[TransportPreferencesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionPreferences")
    def encryption_preferences(self) -> Optional[pulumi.Input[EncryptionPreferencesArgs]]:
        
        ...
    
    @encryption_preferences.setter
    def encryption_preferences(self, value: Optional[pulumi.Input[EncryptionPreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredDataCenterRegion")
    def preferred_data_center_region(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @preferred_data_center_region.setter
    def preferred_data_center_region(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseTransportPreferences")
    def reverse_transport_preferences(self) -> Optional[pulumi.Input[TransportPreferencesArgs]]:
        
        ...
    
    @reverse_transport_preferences.setter
    def reverse_transport_preferences(self, value: Optional[pulumi.Input[TransportPreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountAccessTierPreferences")
    def storage_account_access_tier_preferences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, StorageAccountAccessTier]]]]]:
        
        ...
    
    @storage_account_access_tier_preferences.setter
    def storage_account_access_tier_preferences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, StorageAccountAccessTier]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transportPreferences")
    def transport_preferences(self) -> Optional[pulumi.Input[TransportPreferencesArgs]]:
        
        ...
    
    @transport_preferences.setter
    def transport_preferences(self, value: Optional[pulumi.Input[TransportPreferencesArgs]]): # -> None:
        ...
    


class ResourceIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[_builtins.str]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ResourceIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ReverseShippingDetailsArgsDict(TypedDict):
    
    contact_details: NotRequired[pulumi.Input[ContactInfoArgsDict]]
    shipping_address: NotRequired[pulumi.Input[ShippingAddressArgsDict]]


@pulumi.input_type
class ReverseShippingDetailsArgs:
    def __init__(__self__, *, contact_details: Optional[pulumi.Input[ContactInfoArgs]] = ..., shipping_address: Optional[pulumi.Input[ShippingAddressArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> Optional[pulumi.Input[ContactInfoArgs]]:
        
        ...
    
    @contact_details.setter
    def contact_details(self, value: Optional[pulumi.Input[ContactInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input[ShippingAddressArgs]]:
        
        ...
    
    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input[ShippingAddressArgs]]): # -> None:
        ...
    


class ShippingAddressArgsDict(TypedDict):
    
    country: pulumi.Input[_builtins.str]
    street_address1: pulumi.Input[_builtins.str]
    address_type: NotRequired[pulumi.Input[Union[_builtins.str, AddressType]]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    company_name: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    skip_address_validation: NotRequired[pulumi.Input[_builtins.bool]]
    state_or_province: NotRequired[pulumi.Input[_builtins.str]]
    street_address2: NotRequired[pulumi.Input[_builtins.str]]
    street_address3: NotRequired[pulumi.Input[_builtins.str]]
    tax_identification_number: NotRequired[pulumi.Input[_builtins.str]]
    zip_extended_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ShippingAddressArgs:
    def __init__(__self__, *, country: pulumi.Input[_builtins.str], street_address1: pulumi.Input[_builtins.str], address_type: Optional[pulumi.Input[Union[_builtins.str, AddressType]]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., company_name: Optional[pulumi.Input[_builtins.str]] = ..., postal_code: Optional[pulumi.Input[_builtins.str]] = ..., skip_address_validation: Optional[pulumi.Input[_builtins.bool]] = ..., state_or_province: Optional[pulumi.Input[_builtins.str]] = ..., street_address2: Optional[pulumi.Input[_builtins.str]] = ..., street_address3: Optional[pulumi.Input[_builtins.str]] = ..., tax_identification_number: Optional[pulumi.Input[_builtins.str]] = ..., zip_extended_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def country(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @country.setter
    def country(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress1")
    def street_address1(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @street_address1.setter
    def street_address1(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressType")
    def address_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AddressType]]]:
        
        ...
    
    @address_type.setter
    def address_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AddressType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipAddressValidation")
    def skip_address_validation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_address_validation.setter
    def skip_address_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="streetAddress3")
    def street_address3(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @street_address3.setter
    def street_address3(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taxIdentificationNumber")
    def tax_identification_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tax_identification_number.setter
    def tax_identification_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipExtendedCode")
    def zip_extended_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zip_extended_code.setter
    def zip_extended_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: pulumi.Input[Union[_builtins.str, SkuName]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    family: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[Union[_builtins.str, SkuName]], display_name: Optional[pulumi.Input[_builtins.str]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StorageAccountDetailsArgsDict(TypedDict):
    
    data_account_type: pulumi.Input[_builtins.str]
    storage_account_id: pulumi.Input[_builtins.str]
    share_password: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StorageAccountDetailsArgs:
    def __init__(__self__, *, data_account_type: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_id: pulumi.Input[_builtins.str], share_password: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_account_type.setter
    def data_account_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_account_id.setter
    def storage_account_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharePassword")
    def share_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @share_password.setter
    def share_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferAllDetailsArgsDict(TypedDict):
    
    data_account_type: pulumi.Input[Union[_builtins.str, DataAccountType]]
    transfer_all_blobs: NotRequired[pulumi.Input[_builtins.bool]]
    transfer_all_files: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class TransferAllDetailsArgs:
    def __init__(__self__, *, data_account_type: Optional[pulumi.Input[Union[_builtins.str, DataAccountType]]] = ..., transfer_all_blobs: Optional[pulumi.Input[_builtins.bool]] = ..., transfer_all_files: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> pulumi.Input[Union[_builtins.str, DataAccountType]]:
        
        ...
    
    @data_account_type.setter
    def data_account_type(self, value: pulumi.Input[Union[_builtins.str, DataAccountType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferAllBlobs")
    def transfer_all_blobs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transfer_all_blobs.setter
    def transfer_all_blobs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferAllFiles")
    def transfer_all_files(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transfer_all_files.setter
    def transfer_all_files(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class TransferConfigurationTransferAllDetailsArgsDict(TypedDict):
    
    include: NotRequired[pulumi.Input[TransferAllDetailsArgsDict]]


@pulumi.input_type
class TransferConfigurationTransferAllDetailsArgs:
    def __init__(__self__, *, include: Optional[pulumi.Input[TransferAllDetailsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def include(self) -> Optional[pulumi.Input[TransferAllDetailsArgs]]:
        
        ...
    
    @include.setter
    def include(self, value: Optional[pulumi.Input[TransferAllDetailsArgs]]): # -> None:
        ...
    


class TransferConfigurationTransferFilterDetailsArgsDict(TypedDict):
    
    include: NotRequired[pulumi.Input[TransferFilterDetailsArgsDict]]


@pulumi.input_type
class TransferConfigurationTransferFilterDetailsArgs:
    def __init__(__self__, *, include: Optional[pulumi.Input[TransferFilterDetailsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def include(self) -> Optional[pulumi.Input[TransferFilterDetailsArgs]]:
        
        ...
    
    @include.setter
    def include(self, value: Optional[pulumi.Input[TransferFilterDetailsArgs]]): # -> None:
        ...
    


class TransferConfigurationArgsDict(TypedDict):
    
    transfer_configuration_type: pulumi.Input[Union[_builtins.str, TransferConfigurationType]]
    transfer_all_details: NotRequired[pulumi.Input[TransferConfigurationTransferAllDetailsArgsDict]]
    transfer_filter_details: NotRequired[pulumi.Input[TransferConfigurationTransferFilterDetailsArgsDict]]


@pulumi.input_type
class TransferConfigurationArgs:
    def __init__(__self__, *, transfer_configuration_type: pulumi.Input[Union[_builtins.str, TransferConfigurationType]], transfer_all_details: Optional[pulumi.Input[TransferConfigurationTransferAllDetailsArgs]] = ..., transfer_filter_details: Optional[pulumi.Input[TransferConfigurationTransferFilterDetailsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferConfigurationType")
    def transfer_configuration_type(self) -> pulumi.Input[Union[_builtins.str, TransferConfigurationType]]:
        
        ...
    
    @transfer_configuration_type.setter
    def transfer_configuration_type(self, value: pulumi.Input[Union[_builtins.str, TransferConfigurationType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferAllDetails")
    def transfer_all_details(self) -> Optional[pulumi.Input[TransferConfigurationTransferAllDetailsArgs]]:
        
        ...
    
    @transfer_all_details.setter
    def transfer_all_details(self, value: Optional[pulumi.Input[TransferConfigurationTransferAllDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferFilterDetails")
    def transfer_filter_details(self) -> Optional[pulumi.Input[TransferConfigurationTransferFilterDetailsArgs]]:
        
        ...
    
    @transfer_filter_details.setter
    def transfer_filter_details(self, value: Optional[pulumi.Input[TransferConfigurationTransferFilterDetailsArgs]]): # -> None:
        ...
    


class TransferFilterDetailsArgsDict(TypedDict):
    
    data_account_type: pulumi.Input[Union[_builtins.str, DataAccountType]]
    azure_file_filter_details: NotRequired[pulumi.Input[AzureFileFilterDetailsArgsDict]]
    blob_filter_details: NotRequired[pulumi.Input[BlobFilterDetailsArgsDict]]
    filter_file_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[FilterFileDetailsArgsDict]]]]


@pulumi.input_type
class TransferFilterDetailsArgs:
    def __init__(__self__, *, data_account_type: Optional[pulumi.Input[Union[_builtins.str, DataAccountType]]] = ..., azure_file_filter_details: Optional[pulumi.Input[AzureFileFilterDetailsArgs]] = ..., blob_filter_details: Optional[pulumi.Input[BlobFilterDetailsArgs]] = ..., filter_file_details: Optional[pulumi.Input[Sequence[pulumi.Input[FilterFileDetailsArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccountType")
    def data_account_type(self) -> pulumi.Input[Union[_builtins.str, DataAccountType]]:
        
        ...
    
    @data_account_type.setter
    def data_account_type(self, value: pulumi.Input[Union[_builtins.str, DataAccountType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFileFilterDetails")
    def azure_file_filter_details(self) -> Optional[pulumi.Input[AzureFileFilterDetailsArgs]]:
        
        ...
    
    @azure_file_filter_details.setter
    def azure_file_filter_details(self, value: Optional[pulumi.Input[AzureFileFilterDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobFilterDetails")
    def blob_filter_details(self) -> Optional[pulumi.Input[BlobFilterDetailsArgs]]:
        
        ...
    
    @blob_filter_details.setter
    def blob_filter_details(self, value: Optional[pulumi.Input[BlobFilterDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterFileDetails")
    def filter_file_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FilterFileDetailsArgs]]]]:
        
        ...
    
    @filter_file_details.setter
    def filter_file_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FilterFileDetailsArgs]]]]): # -> None:
        ...
    


class TransportPreferencesArgsDict(TypedDict):
    
    preferred_shipment_type: pulumi.Input[Union[_builtins.str, TransportShipmentTypes]]


@pulumi.input_type
class TransportPreferencesArgs:
    def __init__(__self__, *, preferred_shipment_type: pulumi.Input[Union[_builtins.str, TransportShipmentTypes]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredShipmentType")
    def preferred_shipment_type(self) -> pulumi.Input[Union[_builtins.str, TransportShipmentTypes]]:
        
        ...
    
    @preferred_shipment_type.setter
    def preferred_shipment_type(self, value: pulumi.Input[Union[_builtins.str, TransportShipmentTypes]]): # -> None:
        ...
    


class UserAssignedPropertiesArgsDict(TypedDict):
    
    resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserAssignedPropertiesArgs:
    def __init__(__self__, *, resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


