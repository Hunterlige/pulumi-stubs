import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AmiArgs", "Ami"]

@pulumi.input_type
class AmiArgs:
    def __init__(
        __self__,
        *,
        architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        boot_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        deprecation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_block_devices: Optional[
            pulumi.Input[Sequence[pulumi.Input[AmiEbsBlockDeviceArgs]]]
        ] = ...,
        ena_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_block_devices: Optional[
            pulumi.Input[Sequence[pulumi.Input[AmiEphemeralBlockDeviceArgs]]]
        ] = ...,
        image_location: Optional[pulumi.Input[_builtins.str]] = ...,
        imds_support: Optional[pulumi.Input[_builtins.str]] = ...,
        kernel_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ramdisk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sriov_net_support: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tpm_support: Optional[pulumi.Input[_builtins.str]] = ...,
        uefi_data: Optional[pulumi.Input[_builtins.str]] = ...,
        virtualization_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @architecture.setter
    def architecture(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bootMode")
    def boot_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_mode.setter
    def boot_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deprecationTime")
    def deprecation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deprecation_time.setter
    def deprecation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AmiEbsBlockDeviceArgs]]]]: ...
    @ebs_block_devices.setter
    def ebs_block_devices(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AmiEbsBlockDeviceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enaSupport")
    def ena_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ena_support.setter
    def ena_support(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AmiEphemeralBlockDeviceArgs]]]
    ]: ...
    @ephemeral_block_devices.setter
    def ephemeral_block_devices(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AmiEphemeralBlockDeviceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageLocation")
    def image_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_location.setter
    def image_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imdsSupport")
    def imds_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imds_support.setter
    def imds_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kernelId")
    def kernel_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kernel_id.setter
    def kernel_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ramdiskId")
    def ramdisk_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ramdisk_id.setter
    def ramdisk_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootDeviceName")
    def root_device_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_device_name.setter
    def root_device_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sriovNetSupport")
    def sriov_net_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sriov_net_support.setter
    def sriov_net_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tpmSupport")
    def tpm_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tpm_support.setter
    def tpm_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uefiData")
    def uefi_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uefi_data.setter
    def uefi_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualizationType")
    def virtualization_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtualization_type.setter
    def virtualization_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AmiState:
    def __init__(
        __self__,
        *,
        architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        boot_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        deprecation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_block_devices: Optional[
            pulumi.Input[Sequence[pulumi.Input[AmiEbsBlockDeviceArgs]]]
        ] = ...,
        ena_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_block_devices: Optional[
            pulumi.Input[Sequence[pulumi.Input[AmiEphemeralBlockDeviceArgs]]]
        ] = ...,
        hypervisor: Optional[pulumi.Input[_builtins.str]] = ...,
        image_location: Optional[pulumi.Input[_builtins.str]] = ...,
        image_owner_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        image_type: Optional[pulumi.Input[_builtins.str]] = ...,
        imds_support: Optional[pulumi.Input[_builtins.str]] = ...,
        kernel_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_launched_time: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_ebs_snapshots: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        platform: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_details: Optional[pulumi.Input[_builtins.str]] = ...,
        public: Optional[pulumi.Input[_builtins.bool]] = ...,
        ramdisk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        root_snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sriov_net_support: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tpm_support: Optional[pulumi.Input[_builtins.str]] = ...,
        uefi_data: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_operation: Optional[pulumi.Input[_builtins.str]] = ...,
        virtualization_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @architecture.setter
    def architecture(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bootMode")
    def boot_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_mode.setter
    def boot_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deprecationTime")
    def deprecation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deprecation_time.setter
    def deprecation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AmiEbsBlockDeviceArgs]]]]: ...
    @ebs_block_devices.setter
    def ebs_block_devices(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AmiEbsBlockDeviceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enaSupport")
    def ena_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ena_support.setter
    def ena_support(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AmiEphemeralBlockDeviceArgs]]]
    ]: ...
    @ephemeral_block_devices.setter
    def ephemeral_block_devices(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AmiEphemeralBlockDeviceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def hypervisor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hypervisor.setter
    def hypervisor(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageLocation")
    def image_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_location.setter
    def image_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageOwnerAlias")
    def image_owner_alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_owner_alias.setter
    def image_owner_alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imdsSupport")
    def imds_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imds_support.setter
    def imds_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kernelId")
    def kernel_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kernel_id.setter
    def kernel_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastLaunchedTime")
    def last_launched_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_launched_time.setter
    def last_launched_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manageEbsSnapshots")
    def manage_ebs_snapshots(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manage_ebs_snapshots.setter
    def manage_ebs_snapshots(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformDetails")
    def platform_details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_details.setter
    def platform_details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def public(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @public.setter
    def public(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ramdiskId")
    def ramdisk_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ramdisk_id.setter
    def ramdisk_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootDeviceName")
    def root_device_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_device_name.setter
    def root_device_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootSnapshotId")
    def root_snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_snapshot_id.setter
    def root_snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sriovNetSupport")
    def sriov_net_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sriov_net_support.setter
    def sriov_net_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tpmSupport")
    def tpm_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tpm_support.setter
    def tpm_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uefiData")
    def uefi_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uefi_data.setter
    def uefi_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="usageOperation")
    def usage_operation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @usage_operation.setter
    def usage_operation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualizationType")
    def virtualization_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtualization_type.setter
    def virtualization_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:ec2/ami:Ami")
class Ami(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        boot_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        deprecation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_block_devices: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AmiEbsBlockDeviceArgs, AmiEbsBlockDeviceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        ena_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_block_devices: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AmiEphemeralBlockDeviceArgs, AmiEphemeralBlockDeviceArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        image_location: Optional[pulumi.Input[_builtins.str]] = ...,
        imds_support: Optional[pulumi.Input[_builtins.str]] = ...,
        kernel_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ramdisk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sriov_net_support: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tpm_support: Optional[pulumi.Input[_builtins.str]] = ...,
        uefi_data: Optional[pulumi.Input[_builtins.str]] = ...,
        virtualization_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AmiArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        boot_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        deprecation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_block_devices: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AmiEbsBlockDeviceArgs, AmiEbsBlockDeviceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        ena_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_block_devices: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AmiEphemeralBlockDeviceArgs, AmiEphemeralBlockDeviceArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        hypervisor: Optional[pulumi.Input[_builtins.str]] = ...,
        image_location: Optional[pulumi.Input[_builtins.str]] = ...,
        image_owner_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        image_type: Optional[pulumi.Input[_builtins.str]] = ...,
        imds_support: Optional[pulumi.Input[_builtins.str]] = ...,
        kernel_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_launched_time: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_ebs_snapshots: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        platform: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_details: Optional[pulumi.Input[_builtins.str]] = ...,
        public: Optional[pulumi.Input[_builtins.bool]] = ...,
        ramdisk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        root_snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sriov_net_support: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tpm_support: Optional[pulumi.Input[_builtins.str]] = ...,
        uefi_data: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_operation: Optional[pulumi.Input[_builtins.str]] = ...,
        virtualization_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Ami: ...
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bootMode")
    def boot_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deprecationTime")
    def deprecation_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(
        self,
    ) -> pulumi.Output[Sequence[outputs.AmiEbsBlockDevice]]: ...
    @_builtins.property
    @pulumi.getter(name="enaSupport")
    def ena_support(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(
        self,
    ) -> pulumi.Output[Sequence[outputs.AmiEphemeralBlockDevice]]: ...
    @_builtins.property
    @pulumi.getter
    def hypervisor(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageLocation")
    def image_location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageOwnerAlias")
    def image_owner_alias(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imdsSupport")
    def imds_support(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kernelId")
    def kernel_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastLaunchedTime")
    def last_launched_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="manageEbsSnapshots")
    def manage_ebs_snapshots(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformDetails")
    def platform_details(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def public(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ramdiskId")
    def ramdisk_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootDeviceName")
    def root_device_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="rootSnapshotId")
    def root_snapshot_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sriovNetSupport")
    def sriov_net_support(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tpmSupport")
    def tpm_support(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="uefiData")
    def uefi_data(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="usageOperation")
    def usage_operation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualizationType")
    def virtualization_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
