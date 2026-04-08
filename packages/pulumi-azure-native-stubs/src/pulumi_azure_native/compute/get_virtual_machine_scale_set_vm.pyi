import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualMachineScaleSetVMResult",
    "AwaitableGetVirtualMachineScaleSetVMResult",
    "get_virtual_machine_scale_set_vm",
    "get_virtual_machine_scale_set_vm_output",
]

@pulumi.output_type
class GetVirtualMachineScaleSetVMResult:
    def __init__(
        __self__,
        additional_capabilities=...,
        availability_set=...,
        azure_api_version=...,
        diagnostics_profile=...,
        etag=...,
        hardware_profile=...,
        id=...,
        identity=...,
        instance_id=...,
        instance_view=...,
        latest_model_applied=...,
        license_type=...,
        location=...,
        model_definition_applied=...,
        name=...,
        network_profile=...,
        network_profile_configuration=...,
        os_profile=...,
        plan=...,
        protection_policy=...,
        provisioning_state=...,
        resilient_vm_deletion_status=...,
        resources=...,
        security_profile=...,
        sku=...,
        storage_profile=...,
        system_data=...,
        tags=...,
        time_created=...,
        type=...,
        user_data=...,
        vm_id=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(
        self,
    ) -> Optional[outputs.AdditionalCapabilitiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="availabilitySet")
    def availability_set(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> Optional[outputs.DiagnosticsProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[outputs.HardwareProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.VirtualMachineIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.VirtualMachineScaleSetVMInstanceViewResponse: ...
    @_builtins.property
    @pulumi.getter(name="latestModelApplied")
    def latest_model_applied(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelDefinitionApplied")
    def model_definition_applied(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.NetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfileConfiguration")
    def network_profile_configuration(
        self,
    ) -> Optional[
        outputs.VirtualMachineScaleSetVMNetworkProfileConfigurationResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[outputs.OSProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[outputs.PlanResponse]: ...
    @_builtins.property
    @pulumi.getter(name="protectionPolicy")
    def protection_policy(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetVMProtectionPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resilientVMDeletionStatus")
    def resilient_vm_deletion_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[outputs.VirtualMachineExtensionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.SecurityProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[outputs.StorageProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Sequence[_builtins.str]: ...

class AwaitableGetVirtualMachineScaleSetVMResult(GetVirtualMachineScaleSetVMResult):
    def __await__(self): ...

def get_virtual_machine_scale_set_vm(
    expand: Optional[_builtins.str] = ...,
    instance_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    vm_scale_set_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualMachineScaleSetVMResult: ...
def get_virtual_machine_scale_set_vm_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vm_scale_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualMachineScaleSetVMResult]: ...
