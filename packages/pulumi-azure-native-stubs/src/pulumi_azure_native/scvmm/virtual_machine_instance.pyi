import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualMachineInstanceArgs", "VirtualMachineInstance"]

@pulumi.input_type
class VirtualMachineInstanceArgs:
    def __init__(
        __self__,
        *,
        extended_location: pulumi.Input[ExtendedLocationArgs],
        resource_uri: pulumi.Input[_builtins.str],
        availability_sets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[VirtualMachineInstancePropertiesAvailabilitySetsArgs]
                ]
            ]
        ] = ...,
        hardware_profile: Optional[pulumi.Input[HardwareProfileArgs]] = ...,
        infrastructure_profile: Optional[pulumi.Input[InfrastructureProfileArgs]] = ...,
        network_profile: Optional[pulumi.Input[NetworkProfileArgs]] = ...,
        os_profile: Optional[pulumi.Input[OsProfileForVMInstanceArgs]] = ...,
        storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationArgs]: ...
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]: ...
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="availabilitySets")
    def availability_sets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualMachineInstancePropertiesAvailabilitySetsArgs]]
        ]
    ]: ...
    @availability_sets.setter
    def availability_sets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[VirtualMachineInstancePropertiesAvailabilitySetsArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input[HardwareProfileArgs]]: ...
    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input[HardwareProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureProfile")
    def infrastructure_profile(
        self,
    ) -> Optional[pulumi.Input[InfrastructureProfileArgs]]: ...
    @infrastructure_profile.setter
    def infrastructure_profile(
        self, value: Optional[pulumi.Input[InfrastructureProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[NetworkProfileArgs]]: ...
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[NetworkProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input[OsProfileForVMInstanceArgs]]: ...
    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input[OsProfileForVMInstanceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): ...

@pulumi.type_token("azure-native:scvmm:VirtualMachineInstance")
class VirtualMachineInstance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        availability_sets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VirtualMachineInstancePropertiesAvailabilitySetsArgs,
                            VirtualMachineInstancePropertiesAvailabilitySetsArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        hardware_profile: Optional[
            pulumi.Input[Union[HardwareProfileArgs, HardwareProfileArgsDict]]
        ] = ...,
        infrastructure_profile: Optional[
            pulumi.Input[
                Union[InfrastructureProfileArgs, InfrastructureProfileArgsDict]
            ]
        ] = ...,
        network_profile: Optional[
            pulumi.Input[Union[NetworkProfileArgs, NetworkProfileArgsDict]]
        ] = ...,
        os_profile: Optional[
            pulumi.Input[
                Union[OsProfileForVMInstanceArgs, OsProfileForVMInstanceArgsDict]
            ]
        ] = ...,
        resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_profile: Optional[
            pulumi.Input[Union[StorageProfileArgs, StorageProfileArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualMachineInstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualMachineInstance: ...
    @_builtins.property
    @pulumi.getter(name="availabilitySets")
    def availability_sets(
        self,
    ) -> pulumi.Output[
        Optional[
            Sequence[outputs.VirtualMachineInstancePropertiesResponseAvailabilitySets]
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.HardwareProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureProfile")
    def infrastructure_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.InfrastructureProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.NetworkProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.OsProfileForVMInstanceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.StorageProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
