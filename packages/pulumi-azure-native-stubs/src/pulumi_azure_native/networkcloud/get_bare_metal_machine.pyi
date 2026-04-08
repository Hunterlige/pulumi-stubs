import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBareMetalMachineResult",
    "AwaitableGetBareMetalMachineResult",
    "get_bare_metal_machine",
    "get_bare_metal_machine_output",
]

@pulumi.output_type
class GetBareMetalMachineResult:
    def __init__(
        __self__,
        associated_resource_ids=...,
        azure_api_version=...,
        bmc_connection_string=...,
        bmc_credentials=...,
        bmc_mac_address=...,
        boot_mac_address=...,
        cluster_id=...,
        cordon_status=...,
        detailed_status=...,
        detailed_status_message=...,
        etag=...,
        extended_location=...,
        hardware_inventory=...,
        hardware_validation_status=...,
        hybrid_aks_clusters_associated_ids=...,
        id=...,
        kubernetes_node_name=...,
        kubernetes_version=...,
        location=...,
        machine_cluster_version=...,
        machine_details=...,
        machine_name=...,
        machine_roles=...,
        machine_sku_id=...,
        name=...,
        oam_ipv4_address=...,
        oam_ipv6_address=...,
        os_image=...,
        power_state=...,
        provisioning_state=...,
        rack_id=...,
        rack_slot=...,
        ready_state=...,
        runtime_protection_status=...,
        secret_rotation_status=...,
        serial_number=...,
        service_tag=...,
        system_data=...,
        tags=...,
        type=...,
        virtual_machines_associated_ids=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associatedResourceIds")
    def associated_resource_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bmcConnectionString")
    def bmc_connection_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bmcCredentials")
    def bmc_credentials(self) -> outputs.AdministrativeCredentialsResponse: ...
    @_builtins.property
    @pulumi.getter(name="bmcMacAddress")
    def bmc_mac_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootMacAddress")
    def boot_mac_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cordonStatus")
    def cordon_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse: ...
    @_builtins.property
    @pulumi.getter(name="hardwareInventory")
    def hardware_inventory(self) -> outputs.HardwareInventoryResponse: ...
    @_builtins.property
    @pulumi.getter(name="hardwareValidationStatus")
    def hardware_validation_status(
        self,
    ) -> outputs.HardwareValidationStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="hybridAksClustersAssociatedIds")
    def hybrid_aks_clusters_associated_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesNodeName")
    def kubernetes_node_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineClusterVersion")
    def machine_cluster_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineDetails")
    def machine_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineRoles")
    def machine_roles(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineSkuId")
    def machine_sku_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oamIpv4Address")
    def oam_ipv4_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oamIpv6Address")
    def oam_ipv6_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osImage")
    def os_image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rackId")
    def rack_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="readyState")
    def ready_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runtimeProtectionStatus")
    def runtime_protection_status(self) -> outputs.RuntimeProtectionStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="secretRotationStatus")
    def secret_rotation_status(
        self,
    ) -> Sequence[outputs.SecretRotationStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceTag")
    def service_tag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachinesAssociatedIds")
    def virtual_machines_associated_ids(self) -> Sequence[_builtins.str]: ...

class AwaitableGetBareMetalMachineResult(GetBareMetalMachineResult):
    def __await__(self): ...

def get_bare_metal_machine(
    bare_metal_machine_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBareMetalMachineResult: ...
def get_bare_metal_machine_output(
    bare_metal_machine_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBareMetalMachineResult]: ...
