import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ManagedClusterArgs", "ManagedCluster"]

@pulumi.input_type
class ManagedClusterArgs:
    def __init__(
        __self__,
        *,
        admin_user_name: pulumi.Input[_builtins.str],
        dns_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[SkuArgs],
        addon_features: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ManagedClusterAddOnFeature]]]
            ]
        ] = ...,
        admin_password: Optional[pulumi.Input[_builtins.str]] = ...,
        allow_rdp_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        application_type_versions_cleanup_policy: Optional[
            pulumi.Input[ApplicationTypeVersionsCleanupPolicyArgs]
        ] = ...,
        auxiliary_subnets: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubnetArgs]]]
        ] = ...,
        azure_active_directory: Optional[pulumi.Input[AzureActiveDirectoryArgs]] = ...,
        client_connection_port: Optional[pulumi.Input[_builtins.int]] = ...,
        clients: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClientCertificateArgs]]]
        ] = ...,
        cluster_code_version: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_upgrade_cadence: Optional[
            pulumi.Input[Union[_builtins.str, ClusterUpgradeCadence]]
        ] = ...,
        cluster_upgrade_mode: Optional[
            pulumi.Input[Union[_builtins.str, ClusterUpgradeMode]]
        ] = ...,
        ddos_protection_plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_auto_os_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http_gateway_exclusive_auth_mode: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_ipv6: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_service_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        fabric_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[SettingsSectionDescriptionArgs]]]
        ] = ...,
        http_gateway_connection_port: Optional[pulumi.Input[_builtins.int]] = ...,
        http_gateway_token_auth_connection_port: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        ip_tags: Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]] = ...,
        load_balancing_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoadBalancingRuleArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_security_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkSecurityRuleArgs]]]
        ] = ...,
        public_ip_prefix_id: Optional[pulumi.Input[_builtins.str]] = ...,
        public_i_pv6_prefix_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceEndpointArgs]]]
        ] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        upgrade_description: Optional[pulumi.Input[ClusterUpgradePolicyArgs]] = ...,
        use_custom_vnet: Optional[pulumi.Input[_builtins.bool]] = ...,
        zonal_resiliency: Optional[pulumi.Input[_builtins.bool]] = ...,
        zonal_update_mode: Optional[
            pulumi.Input[Union[_builtins.str, ZonalUpdateMode]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUserName")
    def admin_user_name(self) -> pulumi.Input[_builtins.str]: ...
    @admin_user_name.setter
    def admin_user_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Input[_builtins.str]: ...
    @dns_name.setter
    def dns_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[SkuArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[SkuArgs]): ...
    @_builtins.property
    @pulumi.getter(name="addonFeatures")
    def addon_features(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, ManagedClusterAddOnFeature]]]
        ]
    ]: ...
    @addon_features.setter
    def addon_features(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ManagedClusterAddOnFeature]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_password.setter
    def admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="allowRdpAccess")
    def allow_rdp_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_rdp_access.setter
    def allow_rdp_access(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationTypeVersionsCleanupPolicy")
    def application_type_versions_cleanup_policy(
        self,
    ) -> Optional[pulumi.Input[ApplicationTypeVersionsCleanupPolicyArgs]]: ...
    @application_type_versions_cleanup_policy.setter
    def application_type_versions_cleanup_policy(
        self, value: Optional[pulumi.Input[ApplicationTypeVersionsCleanupPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="auxiliarySubnets")
    def auxiliary_subnets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubnetArgs]]]]: ...
    @auxiliary_subnets.setter
    def auxiliary_subnets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubnetArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureActiveDirectory")
    def azure_active_directory(
        self,
    ) -> Optional[pulumi.Input[AzureActiveDirectoryArgs]]: ...
    @azure_active_directory.setter
    def azure_active_directory(
        self, value: Optional[pulumi.Input[AzureActiveDirectoryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientConnectionPort")
    def client_connection_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @client_connection_port.setter
    def client_connection_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClientCertificateArgs]]]]: ...
    @clients.setter
    def clients(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ClientCertificateArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterCodeVersion")
    def cluster_code_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_code_version.setter
    def cluster_code_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterUpgradeCadence")
    def cluster_upgrade_cadence(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ClusterUpgradeCadence]]]: ...
    @cluster_upgrade_cadence.setter
    def cluster_upgrade_cadence(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ClusterUpgradeCadence]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterUpgradeMode")
    def cluster_upgrade_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ClusterUpgradeMode]]]: ...
    @cluster_upgrade_mode.setter
    def cluster_upgrade_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ClusterUpgradeMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ddosProtectionPlanId")
    def ddos_protection_plan_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ddos_protection_plan_id.setter
    def ddos_protection_plan_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAutoOSUpgrade")
    def enable_auto_os_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_auto_os_upgrade.setter
    def enable_auto_os_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableHttpGatewayExclusiveAuthMode")
    def enable_http_gateway_exclusive_auth_mode(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_http_gateway_exclusive_auth_mode.setter
    def enable_http_gateway_exclusive_auth_mode(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ipv6.setter
    def enable_ipv6(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableServicePublicIP")
    def enable_service_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_service_public_ip.setter
    def enable_service_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fabricSettings")
    def fabric_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SettingsSectionDescriptionArgs]]]
    ]: ...
    @fabric_settings.setter
    def fabric_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SettingsSectionDescriptionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGatewayConnectionPort")
    def http_gateway_connection_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @http_gateway_connection_port.setter
    def http_gateway_connection_port(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGatewayTokenAuthConnectionPort")
    def http_gateway_token_auth_connection_port(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @http_gateway_token_auth_connection_port.setter
    def http_gateway_token_auth_connection_port(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]]: ...
    @ip_tags.setter
    def ip_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingRules")
    def load_balancing_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancingRuleArgs]]]]: ...
    @load_balancing_rules.setter
    def load_balancing_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancingRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="publicIPPrefixId")
    def public_ip_prefix_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ip_prefix_id.setter
    def public_ip_prefix_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIPv6PrefixId")
    def public_i_pv6_prefix_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_i_pv6_prefix_id.setter
    def public_i_pv6_prefix_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointArgs]]]]: ...
    @service_endpoints.setter
    def service_endpoints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointArgs]]]]
    ): ...
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
    @pulumi.getter(name="upgradeDescription")
    def upgrade_description(
        self,
    ) -> Optional[pulumi.Input[ClusterUpgradePolicyArgs]]: ...
    @upgrade_description.setter
    def upgrade_description(
        self, value: Optional[pulumi.Input[ClusterUpgradePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useCustomVnet")
    def use_custom_vnet(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_custom_vnet.setter
    def use_custom_vnet(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="zonalResiliency")
    def zonal_resiliency(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @zonal_resiliency.setter
    def zonal_resiliency(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="zonalUpdateMode")
    def zonal_update_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ZonalUpdateMode]]]: ...
    @zonal_update_mode.setter
    def zonal_update_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ZonalUpdateMode]]]
    ): ...

@pulumi.type_token("azure-native:servicefabric:ManagedCluster")
class ManagedCluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        addon_features: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ManagedClusterAddOnFeature]]]
            ]
        ] = ...,
        admin_password: Optional[pulumi.Input[_builtins.str]] = ...,
        admin_user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        allow_rdp_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        application_type_versions_cleanup_policy: Optional[
            pulumi.Input[
                Union[
                    ApplicationTypeVersionsCleanupPolicyArgs,
                    ApplicationTypeVersionsCleanupPolicyArgsDict,
                ]
            ]
        ] = ...,
        auxiliary_subnets: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[SubnetArgs, SubnetArgsDict]]]]
        ] = ...,
        azure_active_directory: Optional[
            pulumi.Input[Union[AzureActiveDirectoryArgs, AzureActiveDirectoryArgsDict]]
        ] = ...,
        client_connection_port: Optional[pulumi.Input[_builtins.int]] = ...,
        clients: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ClientCertificateArgs, ClientCertificateArgsDict]
                    ]
                ]
            ]
        ] = ...,
        cluster_code_version: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_upgrade_cadence: Optional[
            pulumi.Input[Union[_builtins.str, ClusterUpgradeCadence]]
        ] = ...,
        cluster_upgrade_mode: Optional[
            pulumi.Input[Union[_builtins.str, ClusterUpgradeMode]]
        ] = ...,
        ddos_protection_plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_auto_os_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http_gateway_exclusive_auth_mode: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_ipv6: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_service_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        fabric_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SettingsSectionDescriptionArgs,
                            SettingsSectionDescriptionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        http_gateway_connection_port: Optional[pulumi.Input[_builtins.int]] = ...,
        http_gateway_token_auth_connection_port: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        ip_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[IpTagArgs, IpTagArgsDict]]]]
        ] = ...,
        load_balancing_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[LoadBalancingRuleArgs, LoadBalancingRuleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_security_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[NetworkSecurityRuleArgs, NetworkSecurityRuleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        public_ip_prefix_id: Optional[pulumi.Input[_builtins.str]] = ...,
        public_i_pv6_prefix_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ServiceEndpointArgs, ServiceEndpointArgsDict]]
                ]
            ]
        ] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        upgrade_description: Optional[
            pulumi.Input[Union[ClusterUpgradePolicyArgs, ClusterUpgradePolicyArgsDict]]
        ] = ...,
        use_custom_vnet: Optional[pulumi.Input[_builtins.bool]] = ...,
        zonal_resiliency: Optional[pulumi.Input[_builtins.bool]] = ...,
        zonal_update_mode: Optional[
            pulumi.Input[Union[_builtins.str, ZonalUpdateMode]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ManagedCluster: ...
    @_builtins.property
    @pulumi.getter(name="addonFeatures")
    def addon_features(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="adminUserName")
    def admin_user_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowRdpAccess")
    def allow_rdp_access(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="applicationTypeVersionsCleanupPolicy")
    def application_type_versions_cleanup_policy(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ApplicationTypeVersionsCleanupPolicyResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="auxiliarySubnets")
    def auxiliary_subnets(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.SubnetResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureActiveDirectory")
    def azure_active_directory(
        self,
    ) -> pulumi.Output[Optional[outputs.AzureActiveDirectoryResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientConnectionPort")
    def client_connection_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ClientCertificateResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterCertificateThumbprints")
    def cluster_certificate_thumbprints(
        self,
    ) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterCodeVersion")
    def cluster_code_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterState")
    def cluster_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterUpgradeCadence")
    def cluster_upgrade_cadence(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterUpgradeMode")
    def cluster_upgrade_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ddosProtectionPlanId")
    def ddos_protection_plan_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAutoOSUpgrade")
    def enable_auto_os_upgrade(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableHttpGatewayExclusiveAuthMode")
    def enable_http_gateway_exclusive_auth_mode(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableServicePublicIP")
    def enable_service_public_ip(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fabricSettings")
    def fabric_settings(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.SettingsSectionDescriptionResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpGatewayConnectionPort")
    def http_gateway_connection_port(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="httpGatewayTokenAuthConnectionPort")
    def http_gateway_token_auth_connection_port(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> pulumi.Output[Optional[Sequence[outputs.IpTagResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingRules")
    def load_balancing_rules(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.LoadBalancingRuleResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityRules")
    def network_security_rules(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.NetworkSecurityRuleResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPPrefixId")
    def public_ip_prefix_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPv6PrefixId")
    def public_i_pv6_prefix_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ServiceEndpointResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]: ...
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
    @pulumi.getter(name="upgradeDescription")
    def upgrade_description(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterUpgradePolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="useCustomVnet")
    def use_custom_vnet(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="zonalResiliency")
    def zonal_resiliency(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="zonalUpdateMode")
    def zonal_update_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
