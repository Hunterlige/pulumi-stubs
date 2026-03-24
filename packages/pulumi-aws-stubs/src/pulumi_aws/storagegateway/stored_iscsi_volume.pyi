

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StoredIscsiVolumeArgs', 'StoredIscsiVolume']
@pulumi.input_type
class StoredIscsiVolumeArgs:
    def __init__(__self__, *, disk_id: pulumi.Input[_builtins.str], gateway_arn: pulumi.Input[_builtins.str], network_interface_id: pulumi.Input[_builtins.str], preserve_existing_data: pulumi.Input[_builtins.bool], target_name: pulumi.Input[_builtins.str], kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @disk_id.setter
    def disk_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gateway_arn.setter
    def gateway_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveExistingData")
    def preserve_existing_data(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @preserve_existing_data.setter
    def preserve_existing_data(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_name.setter
    def target_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsEncrypted")
    def kms_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kms_encrypted.setter
    def kms_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _StoredIscsiVolumeState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., chap_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., disk_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., lun_number: Optional[pulumi.Input[_builtins.int]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_port: Optional[pulumi.Input[_builtins.int]] = ..., preserve_existing_data: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_arn: Optional[pulumi.Input[_builtins.str]] = ..., target_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_attachment_status: Optional[pulumi.Input[_builtins.str]] = ..., volume_id: Optional[pulumi.Input[_builtins.str]] = ..., volume_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ..., volume_status: Optional[pulumi.Input[_builtins.str]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="chapEnabled")
    def chap_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @chap_enabled.setter
    def chap_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_arn.setter
    def gateway_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsEncrypted")
    def kms_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kms_encrypted.setter
    def kms_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lunNumber")
    def lun_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @lun_number.setter
    def lun_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfacePort")
    def network_interface_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @network_interface_port.setter
    def network_interface_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveExistingData")
    def preserve_existing_data(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @preserve_existing_data.setter
    def preserve_existing_data(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_arn.setter
    def target_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_name.setter
    def target_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeAttachmentStatus")
    def volume_attachment_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_attachment_status.setter
    def volume_attachment_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSizeInBytes")
    def volume_size_in_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size_in_bytes.setter
    def volume_size_in_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeStatus")
    def volume_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_status.setter
    def volume_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class StoredIscsiVolume(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., disk_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., preserve_existing_data: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StoredIscsiVolumeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., chap_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., disk_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., lun_number: Optional[pulumi.Input[_builtins.int]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_port: Optional[pulumi.Input[_builtins.int]] = ..., preserve_existing_data: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_arn: Optional[pulumi.Input[_builtins.str]] = ..., target_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_attachment_status: Optional[pulumi.Input[_builtins.str]] = ..., volume_id: Optional[pulumi.Input[_builtins.str]] = ..., volume_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ..., volume_status: Optional[pulumi.Input[_builtins.str]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> StoredIscsiVolume:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chapEnabled")
    def chap_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsEncrypted")
    def kms_encrypted(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lunNumber")
    def lun_number(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfacePort")
    def network_interface_port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveExistingData")
    def preserve_existing_data(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeAttachmentStatus")
    def volume_attachment_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSizeInBytes")
    def volume_size_in_bytes(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeStatus")
    def volume_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


