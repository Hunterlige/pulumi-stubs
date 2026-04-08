import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NodeTypeArgs", "NodeType"]

@pulumi.input_type
class NodeTypeArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        is_primary: pulumi.Input[_builtins.bool],
        resource_group_name: pulumi.Input[_builtins.str],
        vm_instance_count: pulumi.Input[_builtins.int],
        additional_data_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[VmssDataDiskArgs]]]
        ] = ...,
        additional_network_interface_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AdditionalNetworkInterfaceConfigurationArgs]]
            ]
        ] = ...,
        application_ports: Optional[pulumi.Input[EndpointRangeDescriptionArgs]] = ...,
        capacities: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        computer_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_letter: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        data_disk_type: Optional[pulumi.Input[Union[_builtins.str, DiskType]]] = ...,
        dscp_configuration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_accelerated_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_encryption_at_host: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_node_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_node_public_i_pv6: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_over_provisioning: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_ports: Optional[pulumi.Input[EndpointRangeDescriptionArgs]] = ...,
        eviction_policy: Optional[
            pulumi.Input[Union[_builtins.str, EvictionPolicyType]]
        ] = ...,
        frontend_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[FrontendConfigurationArgs]]]
        ] = ...,
        host_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        is_spot_vm: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_stateless: Optional[pulumi.Input[_builtins.bool]] = ...,
        multiple_placement_groups: Optional[pulumi.Input[_builtins.bool]] = ...,
        nat_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodeTypeNatConfigArgs]]]
        ] = ...,
        nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_security_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkSecurityRuleArgs]]]
        ] = ...,
        node_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        secure_boot_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_type: Optional[pulumi.Input[Union[_builtins.str, SecurityType]]] = ...,
        service_artifact_reference_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[NodeTypeSkuArgs]] = ...,
        spot_restore_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        use_default_public_load_balancer: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_ephemeral_os_disk: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_temp_data_disk: Optional[pulumi.Input[_builtins.bool]] = ...,
        vm_extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMSSExtensionArgs]]]
        ] = ...,
        vm_image_offer: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image_plan: Optional[pulumi.Input[VmImagePlanArgs]] = ...,
        vm_image_publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image_sku: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image_version: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_managed_identity: Optional[pulumi.Input[VmManagedIdentityArgs]] = ...,
        vm_secrets: Optional[
            pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]
        ] = ...,
        vm_setup_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VmSetupAction]]]]
        ] = ...,
        vm_shared_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> pulumi.Input[_builtins.bool]: ...
    @is_primary.setter
    def is_primary(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmInstanceCount")
    def vm_instance_count(self) -> pulumi.Input[_builtins.int]: ...
    @vm_instance_count.setter
    def vm_instance_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="additionalDataDisks")
    def additional_data_disks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VmssDataDiskArgs]]]]: ...
    @additional_data_disks.setter
    def additional_data_disks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VmssDataDiskArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalNetworkInterfaceConfigurations")
    def additional_network_interface_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AdditionalNetworkInterfaceConfigurationArgs]]
        ]
    ]: ...
    @additional_network_interface_configurations.setter
    def additional_network_interface_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AdditionalNetworkInterfaceConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="applicationPorts")
    def application_ports(
        self,
    ) -> Optional[pulumi.Input[EndpointRangeDescriptionArgs]]: ...
    @application_ports.setter
    def application_ports(
        self, value: Optional[pulumi.Input[EndpointRangeDescriptionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def capacities(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @capacities.setter
    def capacities(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="computerNamePrefix")
    def computer_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @computer_name_prefix.setter
    def computer_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDiskLetter")
    def data_disk_letter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_disk_letter.setter
    def data_disk_letter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDiskSizeGB")
    def data_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_disk_size_gb.setter
    def data_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskType]]]: ...
    @data_disk_type.setter
    def data_disk_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dscpConfigurationId")
    def dscp_configuration_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dscp_configuration_id.setter
    def dscp_configuration_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_accelerated_networking.setter
    def enable_accelerated_networking(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableEncryptionAtHost")
    def enable_encryption_at_host(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_encryption_at_host.setter
    def enable_encryption_at_host(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIP")
    def enable_node_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_node_public_ip.setter
    def enable_node_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIPv6")
    def enable_node_public_i_pv6(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_node_public_i_pv6.setter
    def enable_node_public_i_pv6(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableOverProvisioning")
    def enable_over_provisioning(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_over_provisioning.setter
    def enable_over_provisioning(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralPorts")
    def ephemeral_ports(
        self,
    ) -> Optional[pulumi.Input[EndpointRangeDescriptionArgs]]: ...
    @ephemeral_ports.setter
    def ephemeral_ports(
        self, value: Optional[pulumi.Input[EndpointRangeDescriptionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EvictionPolicyType]]]: ...
    @eviction_policy.setter
    def eviction_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EvictionPolicyType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="frontendConfigurations")
    def frontend_configurations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FrontendConfigurationArgs]]]]: ...
    @frontend_configurations.setter
    def frontend_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FrontendConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostGroupId")
    def host_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_group_id.setter
    def host_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSpotVM")
    def is_spot_vm(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_spot_vm.setter
    def is_spot_vm(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isStateless")
    def is_stateless(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_stateless.setter
    def is_stateless(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="multiplePlacementGroups")
    def multiple_placement_groups(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multiple_placement_groups.setter
    def multiple_placement_groups(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="natConfigurations")
    def nat_configurations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NodeTypeNatConfigArgs]]]]: ...
    @nat_configurations.setter
    def nat_configurations(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[NodeTypeNatConfigArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nat_gateway_id.setter
    def nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityRules")
    def network_security_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkSecurityRuleArgs]]]]: ...
    @network_security_rules.setter
    def network_security_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkSecurityRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeTypeName")
    def node_type_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_type_name.setter
    def node_type_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="placementProperties")
    def placement_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @placement_properties.setter
    def placement_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secureBootEnabled")
    def secure_boot_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @secure_boot_enabled.setter
    def secure_boot_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="securityType")
    def security_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityType]]]: ...
    @security_type.setter
    def security_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceArtifactReferenceId")
    def service_artifact_reference_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_artifact_reference_id.setter
    def service_artifact_reference_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[NodeTypeSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[NodeTypeSkuArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="spotRestoreTimeout")
    def spot_restore_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spot_restore_timeout.setter
    def spot_restore_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="useDefaultPublicLoadBalancer")
    def use_default_public_load_balancer(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_default_public_load_balancer.setter
    def use_default_public_load_balancer(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useEphemeralOSDisk")
    def use_ephemeral_os_disk(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_ephemeral_os_disk.setter
    def use_ephemeral_os_disk(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useTempDataDisk")
    def use_temp_data_disk(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_temp_data_disk.setter
    def use_temp_data_disk(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="vmExtensions")
    def vm_extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VMSSExtensionArgs]]]]: ...
    @vm_extensions.setter
    def vm_extensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VMSSExtensionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmImageOffer")
    def vm_image_offer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_image_offer.setter
    def vm_image_offer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmImagePlan")
    def vm_image_plan(self) -> Optional[pulumi.Input[VmImagePlanArgs]]: ...
    @vm_image_plan.setter
    def vm_image_plan(self, value: Optional[pulumi.Input[VmImagePlanArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vmImagePublisher")
    def vm_image_publisher(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_image_publisher.setter
    def vm_image_publisher(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmImageResourceId")
    def vm_image_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_image_resource_id.setter
    def vm_image_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmImageSku")
    def vm_image_sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_image_sku.setter
    def vm_image_sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmImageVersion")
    def vm_image_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_image_version.setter
    def vm_image_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmManagedIdentity")
    def vm_managed_identity(self) -> Optional[pulumi.Input[VmManagedIdentityArgs]]: ...
    @vm_managed_identity.setter
    def vm_managed_identity(
        self, value: Optional[pulumi.Input[VmManagedIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmSecrets")
    def vm_secrets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]]: ...
    @vm_secrets.setter
    def vm_secrets(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmSetupActions")
    def vm_setup_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VmSetupAction]]]]
    ]: ...
    @vm_setup_actions.setter
    def vm_setup_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VmSetupAction]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmSharedGalleryImageId")
    def vm_shared_gallery_image_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_shared_gallery_image_id.setter
    def vm_shared_gallery_image_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:servicefabric:NodeType")
class NodeType(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_data_disks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[VmssDataDiskArgs, VmssDataDiskArgsDict]]]
            ]
        ] = ...,
        additional_network_interface_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AdditionalNetworkInterfaceConfigurationArgs,
                            AdditionalNetworkInterfaceConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        application_ports: Optional[
            pulumi.Input[
                Union[EndpointRangeDescriptionArgs, EndpointRangeDescriptionArgsDict]
            ]
        ] = ...,
        capacities: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        computer_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_letter: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        data_disk_type: Optional[pulumi.Input[Union[_builtins.str, DiskType]]] = ...,
        dscp_configuration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_accelerated_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_encryption_at_host: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_node_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_node_public_i_pv6: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_over_provisioning: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_ports: Optional[
            pulumi.Input[
                Union[EndpointRangeDescriptionArgs, EndpointRangeDescriptionArgsDict]
            ]
        ] = ...,
        eviction_policy: Optional[
            pulumi.Input[Union[_builtins.str, EvictionPolicyType]]
        ] = ...,
        frontend_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[FrontendConfigurationArgs, FrontendConfigurationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        host_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        is_primary: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_spot_vm: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_stateless: Optional[pulumi.Input[_builtins.bool]] = ...,
        multiple_placement_groups: Optional[pulumi.Input[_builtins.bool]] = ...,
        nat_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[NodeTypeNatConfigArgs, NodeTypeNatConfigArgsDict]
                    ]
                ]
            ]
        ] = ...,
        nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_security_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[NetworkSecurityRuleArgs, NetworkSecurityRuleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        node_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        secure_boot_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_type: Optional[pulumi.Input[Union[_builtins.str, SecurityType]]] = ...,
        service_artifact_reference_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[NodeTypeSkuArgs, NodeTypeSkuArgsDict]]] = ...,
        spot_restore_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        use_default_public_load_balancer: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_ephemeral_os_disk: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_temp_data_disk: Optional[pulumi.Input[_builtins.bool]] = ...,
        vm_extensions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[VMSSExtensionArgs, VMSSExtensionArgsDict]]]
            ]
        ] = ...,
        vm_image_offer: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image_plan: Optional[
            pulumi.Input[Union[VmImagePlanArgs, VmImagePlanArgsDict]]
        ] = ...,
        vm_image_publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image_sku: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image_version: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        vm_managed_identity: Optional[
            pulumi.Input[Union[VmManagedIdentityArgs, VmManagedIdentityArgsDict]]
        ] = ...,
        vm_secrets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[VaultSecretGroupArgs, VaultSecretGroupArgsDict]]
                ]
            ]
        ] = ...,
        vm_setup_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VmSetupAction]]]]
        ] = ...,
        vm_shared_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NodeTypeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> NodeType: ...
    @_builtins.property
    @pulumi.getter(name="additionalDataDisks")
    def additional_data_disks(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.VmssDataDiskResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="additionalNetworkInterfaceConfigurations")
    def additional_network_interface_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.AdditionalNetworkInterfaceConfigurationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="applicationPorts")
    def application_ports(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointRangeDescriptionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def capacities(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="computerNamePrefix")
    def computer_name_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskLetter")
    def data_disk_letter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskSizeGB")
    def data_disk_size_gb(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dscpConfigurationId")
    def dscp_configuration_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableEncryptionAtHost")
    def enable_encryption_at_host(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIP")
    def enable_node_public_ip(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIPv6")
    def enable_node_public_i_pv6(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableOverProvisioning")
    def enable_over_provisioning(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralPorts")
    def ephemeral_ports(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointRangeDescriptionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="frontendConfigurations")
    def frontend_configurations(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.FrontendConfigurationResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="hostGroupId")
    def host_group_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isSpotVM")
    def is_spot_vm(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isStateless")
    def is_stateless(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="multiplePlacementGroups")
    def multiple_placement_groups(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="natConfigurations")
    def nat_configurations(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.NodeTypeNatConfigResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityRules")
    def network_security_rules(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.NetworkSecurityRuleResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="placementProperties")
    def placement_properties(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secureBootEnabled")
    def secure_boot_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="securityType")
    def security_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceArtifactReferenceId")
    def service_artifact_reference_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.NodeTypeSkuResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="spotRestoreTimeout")
    def spot_restore_timeout(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useDefaultPublicLoadBalancer")
    def use_default_public_load_balancer(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="useEphemeralOSDisk")
    def use_ephemeral_os_disk(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="useTempDataDisk")
    def use_temp_data_disk(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="vmExtensions")
    def vm_extensions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.VMSSExtensionResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="vmImageOffer")
    def vm_image_offer(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmImagePlan")
    def vm_image_plan(self) -> pulumi.Output[Optional[outputs.VmImagePlanResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="vmImagePublisher")
    def vm_image_publisher(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmImageResourceId")
    def vm_image_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmImageSku")
    def vm_image_sku(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmImageVersion")
    def vm_image_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmInstanceCount")
    def vm_instance_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vmManagedIdentity")
    def vm_managed_identity(
        self,
    ) -> pulumi.Output[Optional[outputs.VmManagedIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSecrets")
    def vm_secrets(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.VaultSecretGroupResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSetupActions")
    def vm_setup_actions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSharedGalleryImageId")
    def vm_shared_gallery_image_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
