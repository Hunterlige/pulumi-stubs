import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualMachineScaleSetVMArgs", "VirtualMachineScaleSetVM"]

@pulumi.input_type
class VirtualMachineScaleSetVMArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        vm_scale_set_name: pulumi.Input[_builtins.str],
        additional_capabilities: Optional[
            pulumi.Input[AdditionalCapabilitiesArgs]
        ] = ...,
        availability_set: Optional[pulumi.Input[SubResourceArgs]] = ...,
        diagnostics_profile: Optional[pulumi.Input[DiagnosticsProfileArgs]] = ...,
        hardware_profile: Optional[pulumi.Input[HardwareProfileArgs]] = ...,
        identity: Optional[pulumi.Input[VirtualMachineIdentityArgs]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        license_type: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile: Optional[pulumi.Input[NetworkProfileArgs]] = ...,
        network_profile_configuration: Optional[
            pulumi.Input[VirtualMachineScaleSetVMNetworkProfileConfigurationArgs]
        ] = ...,
        os_profile: Optional[pulumi.Input[OSProfileArgs]] = ...,
        plan: Optional[pulumi.Input[PlanArgs]] = ...,
        protection_policy: Optional[
            pulumi.Input[VirtualMachineScaleSetVMProtectionPolicyArgs]
        ] = ...,
        resilient_vm_deletion_status: Optional[
            pulumi.Input[Union[_builtins.str, ResilientVMDeletionStatus]]
        ] = ...,
        security_profile: Optional[pulumi.Input[SecurityProfileArgs]] = ...,
        storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmScaleSetName")
    def vm_scale_set_name(self) -> pulumi.Input[_builtins.str]: ...
    @vm_scale_set_name.setter
    def vm_scale_set_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(
        self,
    ) -> Optional[pulumi.Input[AdditionalCapabilitiesArgs]]: ...
    @additional_capabilities.setter
    def additional_capabilities(
        self, value: Optional[pulumi.Input[AdditionalCapabilitiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilitySet")
    def availability_set(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @availability_set.setter
    def availability_set(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> Optional[pulumi.Input[DiagnosticsProfileArgs]]: ...
    @diagnostics_profile.setter
    def diagnostics_profile(
        self, value: Optional[pulumi.Input[DiagnosticsProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input[HardwareProfileArgs]]: ...
    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input[HardwareProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[VirtualMachineIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[VirtualMachineIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @license_type.setter
    def license_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[NetworkProfileArgs]]: ...
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[NetworkProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="networkProfileConfiguration")
    def network_profile_configuration(
        self,
    ) -> Optional[
        pulumi.Input[VirtualMachineScaleSetVMNetworkProfileConfigurationArgs]
    ]: ...
    @network_profile_configuration.setter
    def network_profile_configuration(
        self,
        value: Optional[
            pulumi.Input[VirtualMachineScaleSetVMNetworkProfileConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input[OSProfileArgs]]: ...
    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input[OSProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[PlanArgs]]: ...
    @plan.setter
    def plan(self, value: Optional[pulumi.Input[PlanArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionPolicy")
    def protection_policy(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineScaleSetVMProtectionPolicyArgs]]: ...
    @protection_policy.setter
    def protection_policy(
        self,
        value: Optional[pulumi.Input[VirtualMachineScaleSetVMProtectionPolicyArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resilientVMDeletionStatus")
    def resilient_vm_deletion_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResilientVMDeletionStatus]]]: ...
    @resilient_vm_deletion_status.setter
    def resilient_vm_deletion_status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ResilientVMDeletionStatus]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[SecurityProfileArgs]]: ...
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[SecurityProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): ...
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
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:compute:VirtualMachineScaleSetVM")
class VirtualMachineScaleSetVM(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_capabilities: Optional[
            pulumi.Input[
                Union[AdditionalCapabilitiesArgs, AdditionalCapabilitiesArgsDict]
            ]
        ] = ...,
        availability_set: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        diagnostics_profile: Optional[
            pulumi.Input[Union[DiagnosticsProfileArgs, DiagnosticsProfileArgsDict]]
        ] = ...,
        hardware_profile: Optional[
            pulumi.Input[Union[HardwareProfileArgs, HardwareProfileArgsDict]]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[VirtualMachineIdentityArgs, VirtualMachineIdentityArgsDict]
            ]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        license_type: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile: Optional[
            pulumi.Input[Union[NetworkProfileArgs, NetworkProfileArgsDict]]
        ] = ...,
        network_profile_configuration: Optional[
            pulumi.Input[
                Union[
                    VirtualMachineScaleSetVMNetworkProfileConfigurationArgs,
                    VirtualMachineScaleSetVMNetworkProfileConfigurationArgsDict,
                ]
            ]
        ] = ...,
        os_profile: Optional[
            pulumi.Input[Union[OSProfileArgs, OSProfileArgsDict]]
        ] = ...,
        plan: Optional[pulumi.Input[Union[PlanArgs, PlanArgsDict]]] = ...,
        protection_policy: Optional[
            pulumi.Input[
                Union[
                    VirtualMachineScaleSetVMProtectionPolicyArgs,
                    VirtualMachineScaleSetVMProtectionPolicyArgsDict,
                ]
            ]
        ] = ...,
        resilient_vm_deletion_status: Optional[
            pulumi.Input[Union[_builtins.str, ResilientVMDeletionStatus]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile: Optional[
            pulumi.Input[Union[SecurityProfileArgs, SecurityProfileArgsDict]]
        ] = ...,
        storage_profile: Optional[
            pulumi.Input[Union[StorageProfileArgs, StorageProfileArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_data: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_scale_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualMachineScaleSetVMArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualMachineScaleSetVM: ...
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(
        self,
    ) -> pulumi.Output[Optional[outputs.AdditionalCapabilitiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="availabilitySet")
    def availability_set(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.DiagnosticsProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.HardwareProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.VirtualMachineIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(
        self,
    ) -> pulumi.Output[outputs.VirtualMachineScaleSetVMInstanceViewResponse]: ...
    @_builtins.property
    @pulumi.getter(name="latestModelApplied")
    def latest_model_applied(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelDefinitionApplied")
    def model_definition_applied(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.NetworkProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfileConfiguration")
    def network_profile_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.VirtualMachineScaleSetVMNetworkProfileConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output[Optional[outputs.OSProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional[outputs.PlanResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="protectionPolicy")
    def protection_policy(
        self,
    ) -> pulumi.Output[
        Optional[outputs.VirtualMachineScaleSetVMProtectionPolicyResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resilientVMDeletionStatus")
    def resilient_vm_deletion_status(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> pulumi.Output[Sequence[outputs.VirtualMachineExtensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]: ...
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
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
