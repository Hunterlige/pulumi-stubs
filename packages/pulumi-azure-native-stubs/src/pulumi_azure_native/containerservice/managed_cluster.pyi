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
        resource_group_name: pulumi.Input[_builtins.str],
        aad_profile: Optional[pulumi.Input[ManagedClusterAADProfileArgs]] = ...,
        addon_profiles: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ManagedClusterAddonProfileArgs]]]
        ] = ...,
        agent_pool_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedClusterAgentPoolProfileArgs]]]
        ] = ...,
        ai_toolchain_operator_profile: Optional[
            pulumi.Input[ManagedClusterAIToolchainOperatorProfileArgs]
        ] = ...,
        api_server_access_profile: Optional[
            pulumi.Input[ManagedClusterAPIServerAccessProfileArgs]
        ] = ...,
        auto_scaler_profile: Optional[
            pulumi.Input[ManagedClusterPropertiesAutoScalerProfileArgs]
        ] = ...,
        auto_upgrade_profile: Optional[
            pulumi.Input[ManagedClusterAutoUpgradeProfileArgs]
        ] = ...,
        azure_monitor_profile: Optional[
            pulumi.Input[ManagedClusterAzureMonitorProfileArgs]
        ] = ...,
        bootstrap_profile: Optional[
            pulumi.Input[ManagedClusterBootstrapProfileArgs]
        ] = ...,
        disable_local_accounts: Optional[pulumi.Input[_builtins.bool]] = ...,
        disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_rbac: Optional[pulumi.Input[_builtins.bool]] = ...,
        extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        fqdn_subdomain: Optional[pulumi.Input[_builtins.str]] = ...,
        http_proxy_config: Optional[
            pulumi.Input[ManagedClusterHTTPProxyConfigArgs]
        ] = ...,
        identity: Optional[pulumi.Input[ManagedClusterIdentityArgs]] = ...,
        identity_profile: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
        ] = ...,
        ingress_profile: Optional[pulumi.Input[ManagedClusterIngressProfileArgs]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        kubernetes_version: Optional[pulumi.Input[_builtins.str]] = ...,
        linux_profile: Optional[pulumi.Input[ContainerServiceLinuxProfileArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metrics_profile: Optional[pulumi.Input[ManagedClusterMetricsProfileArgs]] = ...,
        network_profile: Optional[
            pulumi.Input[ContainerServiceNetworkProfileArgs]
        ] = ...,
        node_provisioning_profile: Optional[
            pulumi.Input[ManagedClusterNodeProvisioningProfileArgs]
        ] = ...,
        node_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        node_resource_group_profile: Optional[
            pulumi.Input[ManagedClusterNodeResourceGroupProfileArgs]
        ] = ...,
        oidc_issuer_profile: Optional[
            pulumi.Input[ManagedClusterOIDCIssuerProfileArgs]
        ] = ...,
        pod_identity_profile: Optional[
            pulumi.Input[ManagedClusterPodIdentityProfileArgs]
        ] = ...,
        private_link_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkResourceArgs]]]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile: Optional[
            pulumi.Input[ManagedClusterSecurityProfileArgs]
        ] = ...,
        service_mesh_profile: Optional[pulumi.Input[ServiceMeshProfileArgs]] = ...,
        service_principal_profile: Optional[
            pulumi.Input[ManagedClusterServicePrincipalProfileArgs]
        ] = ...,
        sku: Optional[pulumi.Input[ManagedClusterSKUArgs]] = ...,
        storage_profile: Optional[pulumi.Input[ManagedClusterStorageProfileArgs]] = ...,
        support_plan: Optional[
            pulumi.Input[Union[_builtins.str, KubernetesSupportPlan]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        upgrade_settings: Optional[pulumi.Input[ClusterUpgradeSettingsArgs]] = ...,
        windows_profile: Optional[pulumi.Input[ManagedClusterWindowsProfileArgs]] = ...,
        workload_auto_scaler_profile: Optional[
            pulumi.Input[ManagedClusterWorkloadAutoScalerProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="aadProfile")
    def aad_profile(self) -> Optional[pulumi.Input[ManagedClusterAADProfileArgs]]: ...
    @aad_profile.setter
    def aad_profile(
        self, value: Optional[pulumi.Input[ManagedClusterAADProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="addonProfiles")
    def addon_profiles(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ManagedClusterAddonProfileArgs]]]
    ]: ...
    @addon_profiles.setter
    def addon_profiles(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ManagedClusterAddonProfileArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ManagedClusterAgentPoolProfileArgs]]]
    ]: ...
    @agent_pool_profiles.setter
    def agent_pool_profiles(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedClusterAgentPoolProfileArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="aiToolchainOperatorProfile")
    def ai_toolchain_operator_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterAIToolchainOperatorProfileArgs]]: ...
    @ai_toolchain_operator_profile.setter
    def ai_toolchain_operator_profile(
        self,
        value: Optional[pulumi.Input[ManagedClusterAIToolchainOperatorProfileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="apiServerAccessProfile")
    def api_server_access_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterAPIServerAccessProfileArgs]]: ...
    @api_server_access_profile.setter
    def api_server_access_profile(
        self, value: Optional[pulumi.Input[ManagedClusterAPIServerAccessProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoScalerProfile")
    def auto_scaler_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterPropertiesAutoScalerProfileArgs]]: ...
    @auto_scaler_profile.setter
    def auto_scaler_profile(
        self,
        value: Optional[pulumi.Input[ManagedClusterPropertiesAutoScalerProfileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeProfile")
    def auto_upgrade_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterAutoUpgradeProfileArgs]]: ...
    @auto_upgrade_profile.setter
    def auto_upgrade_profile(
        self, value: Optional[pulumi.Input[ManagedClusterAutoUpgradeProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorProfile")
    def azure_monitor_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterAzureMonitorProfileArgs]]: ...
    @azure_monitor_profile.setter
    def azure_monitor_profile(
        self, value: Optional[pulumi.Input[ManagedClusterAzureMonitorProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootstrapProfile")
    def bootstrap_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterBootstrapProfileArgs]]: ...
    @bootstrap_profile.setter
    def bootstrap_profile(
        self, value: Optional[pulumi.Input[ManagedClusterBootstrapProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAccounts")
    def disable_local_accounts(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_accounts.setter
    def disable_local_accounts(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetID")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_prefix.setter
    def dns_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableRBAC")
    def enable_rbac(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_rbac.setter
    def enable_rbac(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @extended_location.setter
    def extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fqdnSubdomain")
    def fqdn_subdomain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn_subdomain.setter
    def fqdn_subdomain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterHTTPProxyConfigArgs]]: ...
    @http_proxy_config.setter
    def http_proxy_config(
        self, value: Optional[pulumi.Input[ManagedClusterHTTPProxyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedClusterIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedClusterIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="identityProfile")
    def identity_profile(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
    ]: ...
    @identity_profile.setter
    def identity_profile(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressProfile")
    def ingress_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterIngressProfileArgs]]: ...
    @ingress_profile.setter
    def ingress_profile(
        self, value: Optional[pulumi.Input[ManagedClusterIngressProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kubernetes_version.setter
    def kubernetes_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(
        self,
    ) -> Optional[pulumi.Input[ContainerServiceLinuxProfileArgs]]: ...
    @linux_profile.setter
    def linux_profile(
        self, value: Optional[pulumi.Input[ContainerServiceLinuxProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricsProfile")
    def metrics_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterMetricsProfileArgs]]: ...
    @metrics_profile.setter
    def metrics_profile(
        self, value: Optional[pulumi.Input[ManagedClusterMetricsProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> Optional[pulumi.Input[ContainerServiceNetworkProfileArgs]]: ...
    @network_profile.setter
    def network_profile(
        self, value: Optional[pulumi.Input[ContainerServiceNetworkProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeProvisioningProfile")
    def node_provisioning_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterNodeProvisioningProfileArgs]]: ...
    @node_provisioning_profile.setter
    def node_provisioning_profile(
        self, value: Optional[pulumi.Input[ManagedClusterNodeProvisioningProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeResourceGroup")
    def node_resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_resource_group.setter
    def node_resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeResourceGroupProfile")
    def node_resource_group_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterNodeResourceGroupProfileArgs]]: ...
    @node_resource_group_profile.setter
    def node_resource_group_profile(
        self, value: Optional[pulumi.Input[ManagedClusterNodeResourceGroupProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oidcIssuerProfile")
    def oidc_issuer_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterOIDCIssuerProfileArgs]]: ...
    @oidc_issuer_profile.setter
    def oidc_issuer_profile(
        self, value: Optional[pulumi.Input[ManagedClusterOIDCIssuerProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="podIdentityProfile")
    def pod_identity_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterPodIdentityProfileArgs]]: ...
    @pod_identity_profile.setter
    def pod_identity_profile(
        self, value: Optional[pulumi.Input[ManagedClusterPodIdentityProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkResources")
    def private_link_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkResourceArgs]]]]: ...
    @private_link_resources.setter
    def private_link_resources(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkResourceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterSecurityProfileArgs]]: ...
    @security_profile.setter
    def security_profile(
        self, value: Optional[pulumi.Input[ManagedClusterSecurityProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceMeshProfile")
    def service_mesh_profile(
        self,
    ) -> Optional[pulumi.Input[ServiceMeshProfileArgs]]: ...
    @service_mesh_profile.setter
    def service_mesh_profile(
        self, value: Optional[pulumi.Input[ServiceMeshProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalProfile")
    def service_principal_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterServicePrincipalProfileArgs]]: ...
    @service_principal_profile.setter
    def service_principal_profile(
        self, value: Optional[pulumi.Input[ManagedClusterServicePrincipalProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[ManagedClusterSKUArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[ManagedClusterSKUArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterStorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(
        self, value: Optional[pulumi.Input[ManagedClusterStorageProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportPlan")
    def support_plan(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, KubernetesSupportPlan]]]: ...
    @support_plan.setter
    def support_plan(
        self, value: Optional[pulumi.Input[Union[_builtins.str, KubernetesSupportPlan]]]
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
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> Optional[pulumi.Input[ClusterUpgradeSettingsArgs]]: ...
    @upgrade_settings.setter
    def upgrade_settings(
        self, value: Optional[pulumi.Input[ClusterUpgradeSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsProfile")
    def windows_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterWindowsProfileArgs]]: ...
    @windows_profile.setter
    def windows_profile(
        self, value: Optional[pulumi.Input[ManagedClusterWindowsProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadAutoScalerProfile")
    def workload_auto_scaler_profile(
        self,
    ) -> Optional[pulumi.Input[ManagedClusterWorkloadAutoScalerProfileArgs]]: ...
    @workload_auto_scaler_profile.setter
    def workload_auto_scaler_profile(
        self, value: Optional[pulumi.Input[ManagedClusterWorkloadAutoScalerProfileArgs]]
    ): ...

@pulumi.type_token("azure-native:containerservice:ManagedCluster")
class ManagedCluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aad_profile: Optional[
            pulumi.Input[
                Union[ManagedClusterAADProfileArgs, ManagedClusterAADProfileArgsDict]
            ]
        ] = ...,
        addon_profiles: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            ManagedClusterAddonProfileArgs,
                            ManagedClusterAddonProfileArgsDict,
                        ]
                    ],
                ]
            ]
        ] = ...,
        agent_pool_profiles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ManagedClusterAgentPoolProfileArgs,
                            ManagedClusterAgentPoolProfileArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        ai_toolchain_operator_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterAIToolchainOperatorProfileArgs,
                    ManagedClusterAIToolchainOperatorProfileArgsDict,
                ]
            ]
        ] = ...,
        api_server_access_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterAPIServerAccessProfileArgs,
                    ManagedClusterAPIServerAccessProfileArgsDict,
                ]
            ]
        ] = ...,
        auto_scaler_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterPropertiesAutoScalerProfileArgs,
                    ManagedClusterPropertiesAutoScalerProfileArgsDict,
                ]
            ]
        ] = ...,
        auto_upgrade_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterAutoUpgradeProfileArgs,
                    ManagedClusterAutoUpgradeProfileArgsDict,
                ]
            ]
        ] = ...,
        azure_monitor_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterAzureMonitorProfileArgs,
                    ManagedClusterAzureMonitorProfileArgsDict,
                ]
            ]
        ] = ...,
        bootstrap_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterBootstrapProfileArgs,
                    ManagedClusterBootstrapProfileArgsDict,
                ]
            ]
        ] = ...,
        disable_local_accounts: Optional[pulumi.Input[_builtins.bool]] = ...,
        disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_rbac: Optional[pulumi.Input[_builtins.bool]] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        fqdn_subdomain: Optional[pulumi.Input[_builtins.str]] = ...,
        http_proxy_config: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterHTTPProxyConfigArgs,
                    ManagedClusterHTTPProxyConfigArgsDict,
                ]
            ]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedClusterIdentityArgs, ManagedClusterIdentityArgsDict]
            ]
        ] = ...,
        identity_profile: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[UserAssignedIdentityArgs, UserAssignedIdentityArgsDict]
                    ],
                ]
            ]
        ] = ...,
        ingress_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterIngressProfileArgs,
                    ManagedClusterIngressProfileArgsDict,
                ]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        kubernetes_version: Optional[pulumi.Input[_builtins.str]] = ...,
        linux_profile: Optional[
            pulumi.Input[
                Union[
                    ContainerServiceLinuxProfileArgs,
                    ContainerServiceLinuxProfileArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metrics_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterMetricsProfileArgs,
                    ManagedClusterMetricsProfileArgsDict,
                ]
            ]
        ] = ...,
        network_profile: Optional[
            pulumi.Input[
                Union[
                    ContainerServiceNetworkProfileArgs,
                    ContainerServiceNetworkProfileArgsDict,
                ]
            ]
        ] = ...,
        node_provisioning_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterNodeProvisioningProfileArgs,
                    ManagedClusterNodeProvisioningProfileArgsDict,
                ]
            ]
        ] = ...,
        node_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        node_resource_group_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterNodeResourceGroupProfileArgs,
                    ManagedClusterNodeResourceGroupProfileArgsDict,
                ]
            ]
        ] = ...,
        oidc_issuer_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterOIDCIssuerProfileArgs,
                    ManagedClusterOIDCIssuerProfileArgsDict,
                ]
            ]
        ] = ...,
        pod_identity_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterPodIdentityProfileArgs,
                    ManagedClusterPodIdentityProfileArgsDict,
                ]
            ]
        ] = ...,
        private_link_resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PrivateLinkResourceArgs, PrivateLinkResourceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterSecurityProfileArgs,
                    ManagedClusterSecurityProfileArgsDict,
                ]
            ]
        ] = ...,
        service_mesh_profile: Optional[
            pulumi.Input[Union[ServiceMeshProfileArgs, ServiceMeshProfileArgsDict]]
        ] = ...,
        service_principal_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterServicePrincipalProfileArgs,
                    ManagedClusterServicePrincipalProfileArgsDict,
                ]
            ]
        ] = ...,
        sku: Optional[
            pulumi.Input[Union[ManagedClusterSKUArgs, ManagedClusterSKUArgsDict]]
        ] = ...,
        storage_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterStorageProfileArgs,
                    ManagedClusterStorageProfileArgsDict,
                ]
            ]
        ] = ...,
        support_plan: Optional[
            pulumi.Input[Union[_builtins.str, KubernetesSupportPlan]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        upgrade_settings: Optional[
            pulumi.Input[
                Union[ClusterUpgradeSettingsArgs, ClusterUpgradeSettingsArgsDict]
            ]
        ] = ...,
        windows_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterWindowsProfileArgs,
                    ManagedClusterWindowsProfileArgsDict,
                ]
            ]
        ] = ...,
        workload_auto_scaler_profile: Optional[
            pulumi.Input[
                Union[
                    ManagedClusterWorkloadAutoScalerProfileArgs,
                    ManagedClusterWorkloadAutoScalerProfileArgsDict,
                ]
            ]
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
    @pulumi.getter(name="aadProfile")
    def aad_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterAADProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="addonProfiles")
    def addon_profiles(
        self,
    ) -> pulumi.Output[
        Optional[Mapping[str, outputs.ManagedClusterAddonProfileResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ManagedClusterAgentPoolProfileResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="aiToolchainOperatorProfile")
    def ai_toolchain_operator_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ManagedClusterAIToolchainOperatorProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="apiServerAccessProfile")
    def api_server_access_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ManagedClusterAPIServerAccessProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoScalerProfile")
    def auto_scaler_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ManagedClusterPropertiesResponseAutoScalerProfile]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeProfile")
    def auto_upgrade_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterAutoUpgradeProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorProfile")
    def azure_monitor_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterAzureMonitorProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azurePortalFQDN")
    def azure_portal_fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapProfile")
    def bootstrap_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterBootstrapProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="currentKubernetesVersion")
    def current_kubernetes_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAccounts")
    def disable_local_accounts(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetID")
    def disk_encryption_set_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableRBAC")
    def enable_rbac(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fqdnSubdomain")
    def fqdn_subdomain(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterHTTPProxyConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="identityProfile")
    def identity_profile(
        self,
    ) -> pulumi.Output[
        Optional[Mapping[str, outputs.UserAssignedIdentityResponseV1]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ingressProfile")
    def ingress_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterIngressProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ContainerServiceLinuxProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxAgentPools")
    def max_agent_pools(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="metricsProfile")
    def metrics_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterMetricsProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ContainerServiceNetworkProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeProvisioningProfile")
    def node_provisioning_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ManagedClusterNodeProvisioningProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="nodeResourceGroup")
    def node_resource_group(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeResourceGroupProfile")
    def node_resource_group_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ManagedClusterNodeResourceGroupProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="oidcIssuerProfile")
    def oidc_issuer_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterOIDCIssuerProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="podIdentityProfile")
    def pod_identity_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterPodIdentityProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> pulumi.Output[outputs.PowerStateResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateFQDN")
    def private_fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkResources")
    def private_link_resources(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PrivateLinkResourceResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceUID")
    def resource_uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterSecurityProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceMeshProfile")
    def service_mesh_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceMeshProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalProfile")
    def service_principal_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ManagedClusterServicePrincipalProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.ManagedClusterSKUResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterStatusResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterStorageProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="supportPlan")
    def support_plan(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterUpgradeSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="windowsProfile")
    def windows_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedClusterWindowsProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="workloadAutoScalerProfile")
    def workload_auto_scaler_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ManagedClusterWorkloadAutoScalerProfileResponse]
    ]: ...
