import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNodeTypeResult",
    "AwaitableGetNodeTypeResult",
    "get_node_type",
    "get_node_type_output",
]

@pulumi.output_type
class GetNodeTypeResult:
    def __init__(
        __self__,
        additional_data_disks=...,
        additional_network_interface_configurations=...,
        application_ports=...,
        azure_api_version=...,
        capacities=...,
        computer_name_prefix=...,
        data_disk_letter=...,
        data_disk_size_gb=...,
        data_disk_type=...,
        dscp_configuration_id=...,
        enable_accelerated_networking=...,
        enable_encryption_at_host=...,
        enable_node_public_ip=...,
        enable_node_public_i_pv6=...,
        enable_over_provisioning=...,
        ephemeral_ports=...,
        eviction_policy=...,
        frontend_configurations=...,
        host_group_id=...,
        id=...,
        is_primary=...,
        is_spot_vm=...,
        is_stateless=...,
        multiple_placement_groups=...,
        name=...,
        nat_configurations=...,
        nat_gateway_id=...,
        network_security_rules=...,
        placement_properties=...,
        provisioning_state=...,
        secure_boot_enabled=...,
        security_type=...,
        service_artifact_reference_id=...,
        sku=...,
        spot_restore_timeout=...,
        subnet_id=...,
        system_data=...,
        tags=...,
        type=...,
        use_default_public_load_balancer=...,
        use_ephemeral_os_disk=...,
        use_temp_data_disk=...,
        vm_extensions=...,
        vm_image_offer=...,
        vm_image_plan=...,
        vm_image_publisher=...,
        vm_image_resource_id=...,
        vm_image_sku=...,
        vm_image_version=...,
        vm_instance_count=...,
        vm_managed_identity=...,
        vm_secrets=...,
        vm_setup_actions=...,
        vm_shared_gallery_image_id=...,
        vm_size=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalDataDisks")
    def additional_data_disks(
        self,
    ) -> Optional[Sequence[outputs.VmssDataDiskResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="additionalNetworkInterfaceConfigurations")
    def additional_network_interface_configurations(
        self,
    ) -> Optional[
        Sequence[outputs.AdditionalNetworkInterfaceConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="applicationPorts")
    def application_ports(
        self,
    ) -> Optional[outputs.EndpointRangeDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capacities(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="computerNamePrefix")
    def computer_name_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskLetter")
    def data_disk_letter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskSizeGB")
    def data_disk_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dscpConfigurationId")
    def dscp_configuration_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableEncryptionAtHost")
    def enable_encryption_at_host(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIP")
    def enable_node_public_ip(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIPv6")
    def enable_node_public_i_pv6(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableOverProvisioning")
    def enable_over_provisioning(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralPorts")
    def ephemeral_ports(self) -> Optional[outputs.EndpointRangeDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="frontendConfigurations")
    def frontend_configurations(
        self,
    ) -> Optional[Sequence[outputs.FrontendConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="hostGroupId")
    def host_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isSpotVM")
    def is_spot_vm(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isStateless")
    def is_stateless(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="multiplePlacementGroups")
    def multiple_placement_groups(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="natConfigurations")
    def nat_configurations(
        self,
    ) -> Optional[Sequence[outputs.NodeTypeNatConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityRules")
    def network_security_rules(
        self,
    ) -> Optional[Sequence[outputs.NetworkSecurityRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="placementProperties")
    def placement_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secureBootEnabled")
    def secure_boot_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="securityType")
    def security_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceArtifactReferenceId")
    def service_artifact_reference_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.NodeTypeSkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="spotRestoreTimeout")
    def spot_restore_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]: ...
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
    @pulumi.getter(name="useDefaultPublicLoadBalancer")
    def use_default_public_load_balancer(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="useEphemeralOSDisk")
    def use_ephemeral_os_disk(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="useTempDataDisk")
    def use_temp_data_disk(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="vmExtensions")
    def vm_extensions(self) -> Optional[Sequence[outputs.VMSSExtensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="vmImageOffer")
    def vm_image_offer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmImagePlan")
    def vm_image_plan(self) -> Optional[outputs.VmImagePlanResponse]: ...
    @_builtins.property
    @pulumi.getter(name="vmImagePublisher")
    def vm_image_publisher(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmImageResourceId")
    def vm_image_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmImageSku")
    def vm_image_sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmImageVersion")
    def vm_image_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmInstanceCount")
    def vm_instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="vmManagedIdentity")
    def vm_managed_identity(self) -> Optional[outputs.VmManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="vmSecrets")
    def vm_secrets(self) -> Optional[Sequence[outputs.VaultSecretGroupResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSetupActions")
    def vm_setup_actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSharedGalleryImageId")
    def vm_shared_gallery_image_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetNodeTypeResult(GetNodeTypeResult):
    def __await__(self): ...

def get_node_type(
    cluster_name: Optional[_builtins.str] = ...,
    node_type_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNodeTypeResult: ...
def get_node_type_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    node_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNodeTypeResult]: ...
