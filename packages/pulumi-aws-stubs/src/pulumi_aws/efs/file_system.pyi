import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FileSystemArgs", "FileSystem"]

@pulumi.input_type
class FileSystemArgs:
    def __init__(
        __self__,
        *,
        availability_zone_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_token: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[FileSystemLifecyclePolicyArgs]]]
        ] = ...,
        performance_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        protection: Optional[pulumi.Input[FileSystemProtectionArgs]] = ...,
        provisioned_throughput_in_mibps: Optional[pulumi.Input[_builtins.float]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throughput_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone_name.setter
    def availability_zone_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_token.setter
    def creation_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lifecyclePolicies")
    def lifecycle_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FileSystemLifecyclePolicyArgs]]]
    ]: ...
    @lifecycle_policies.setter
    def lifecycle_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FileSystemLifecyclePolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceMode")
    def performance_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performance_mode.setter
    def performance_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protection(self) -> Optional[pulumi.Input[FileSystemProtectionArgs]]: ...
    @protection.setter
    def protection(self, value: Optional[pulumi.Input[FileSystemProtectionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughputInMibps")
    def provisioned_throughput_in_mibps(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @provisioned_throughput_in_mibps.setter
    def provisioned_throughput_in_mibps(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @throughput_mode.setter
    def throughput_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _FileSystemState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_token: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[FileSystemLifecyclePolicyArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_mount_targets: Optional[pulumi.Input[_builtins.int]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        protection: Optional[pulumi.Input[FileSystemProtectionArgs]] = ...,
        provisioned_throughput_in_mibps: Optional[pulumi.Input[_builtins.float]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_bytes: Optional[
            pulumi.Input[Sequence[pulumi.Input[FileSystemSizeInByteArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        throughput_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone_name.setter
    def availability_zone_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_token.setter
    def creation_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lifecyclePolicies")
    def lifecycle_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FileSystemLifecyclePolicyArgs]]]
    ]: ...
    @lifecycle_policies.setter
    def lifecycle_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FileSystemLifecyclePolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfMountTargets")
    def number_of_mount_targets(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_mount_targets.setter
    def number_of_mount_targets(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="performanceMode")
    def performance_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performance_mode.setter
    def performance_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protection(self) -> Optional[pulumi.Input[FileSystemProtectionArgs]]: ...
    @protection.setter
    def protection(self, value: Optional[pulumi.Input[FileSystemProtectionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughputInMibps")
    def provisioned_throughput_in_mibps(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @provisioned_throughput_in_mibps.setter
    def provisioned_throughput_in_mibps(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FileSystemSizeInByteArgs]]]]: ...
    @size_in_bytes.setter
    def size_in_bytes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[FileSystemSizeInByteArgs]]]],
    ): ...
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
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @throughput_mode.setter
    def throughput_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:efs/fileSystem:FileSystem")
class FileSystem(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        availability_zone_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_token: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            FileSystemLifecyclePolicyArgs,
                            FileSystemLifecyclePolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        performance_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        protection: Optional[
            pulumi.Input[Union[FileSystemProtectionArgs, FileSystemProtectionArgsDict]]
        ] = ...,
        provisioned_throughput_in_mibps: Optional[pulumi.Input[_builtins.float]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throughput_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[FileSystemArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_token: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            FileSystemLifecyclePolicyArgs,
                            FileSystemLifecyclePolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_mount_targets: Optional[pulumi.Input[_builtins.int]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        protection: Optional[
            pulumi.Input[Union[FileSystemProtectionArgs, FileSystemProtectionArgsDict]]
        ] = ...,
        provisioned_throughput_in_mibps: Optional[pulumi.Input[_builtins.float]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_bytes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[FileSystemSizeInByteArgs, FileSystemSizeInByteArgsDict]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        throughput_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> FileSystem: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecyclePolicies")
    def lifecycle_policies(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.FileSystemLifecyclePolicy]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfMountTargets")
    def number_of_mount_targets(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="performanceMode")
    def performance_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protection(self) -> pulumi.Output[outputs.FileSystemProtection]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughputInMibps")
    def provisioned_throughput_in_mibps(
        self,
    ) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(
        self,
    ) -> pulumi.Output[Sequence[outputs.FileSystemSizeInByte]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
