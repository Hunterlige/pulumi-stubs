import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CachesIscsiVolumeArgs", "CachesIscsiVolume"]

@pulumi.input_type
class CachesIscsiVolumeArgs:
    def __init__(
        __self__,
        *,
        gateway_arn: pulumi.Input[_builtins.str],
        network_interface_id: pulumi.Input[_builtins.str],
        target_name: pulumi.Input[_builtins.str],
        volume_size_in_bytes: pulumi.Input[_builtins.int],
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_volume_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Input[_builtins.str]: ...
    @gateway_arn.setter
    def gateway_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Input[_builtins.str]: ...
    @network_interface_id.setter
    def network_interface_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> pulumi.Input[_builtins.str]: ...
    @target_name.setter
    def target_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="volumeSizeInBytes")
    def volume_size_in_bytes(self) -> pulumi.Input[_builtins.int]: ...
    @volume_size_in_bytes.setter
    def volume_size_in_bytes(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="kmsEncrypted")
    def kms_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @kms_encrypted.setter
    def kms_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceVolumeArn")
    def source_volume_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_volume_arn.setter
    def source_volume_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _CachesIscsiVolumeState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        chap_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        lun_number: Optional[pulumi.Input[_builtins.int]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_port: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_volume_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        target_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_id: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="chapEnabled")
    def chap_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @chap_enabled.setter
    def chap_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_arn.setter
    def gateway_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsEncrypted")
    def kms_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @kms_encrypted.setter
    def kms_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lunNumber")
    def lun_number(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @lun_number.setter
    def lun_number(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfacePort")
    def network_interface_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @network_interface_port.setter
    def network_interface_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceVolumeArn")
    def source_volume_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_volume_arn.setter
    def source_volume_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_arn.setter
    def target_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_name.setter
    def target_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeArn")
    def volume_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_arn.setter
    def volume_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeSizeInBytes")
    def volume_size_in_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volume_size_in_bytes.setter
    def volume_size_in_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token(...)
class CachesIscsiVolume(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_volume_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CachesIscsiVolumeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        chap_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        lun_number: Optional[pulumi.Input[_builtins.int]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_port: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_volume_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        target_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_id: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> CachesIscsiVolume: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="chapEnabled")
    def chap_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsEncrypted")
    def kms_encrypted(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lunNumber")
    def lun_number(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfacePort")
    def network_interface_port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceVolumeArn")
    def source_volume_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeArn")
    def volume_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeSizeInBytes")
    def volume_size_in_bytes(self) -> pulumi.Output[_builtins.int]: ...
