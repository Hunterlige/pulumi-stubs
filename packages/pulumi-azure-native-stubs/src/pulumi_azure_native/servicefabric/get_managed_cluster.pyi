import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagedClusterResult",
    "AwaitableGetManagedClusterResult",
    "get_managed_cluster",
    "get_managed_cluster_output",
]

@pulumi.output_type
class GetManagedClusterResult:
    def __init__(
        __self__,
        addon_features=...,
        admin_password=...,
        admin_user_name=...,
        allow_rdp_access=...,
        application_type_versions_cleanup_policy=...,
        auxiliary_subnets=...,
        azure_active_directory=...,
        azure_api_version=...,
        client_connection_port=...,
        clients=...,
        cluster_certificate_thumbprints=...,
        cluster_code_version=...,
        cluster_id=...,
        cluster_state=...,
        cluster_upgrade_cadence=...,
        cluster_upgrade_mode=...,
        ddos_protection_plan_id=...,
        dns_name=...,
        enable_auto_os_upgrade=...,
        enable_http_gateway_exclusive_auth_mode=...,
        enable_ipv6=...,
        enable_service_public_ip=...,
        etag=...,
        fabric_settings=...,
        fqdn=...,
        http_gateway_connection_port=...,
        http_gateway_token_auth_connection_port=...,
        id=...,
        ip_tags=...,
        ipv4_address=...,
        ipv6_address=...,
        load_balancing_rules=...,
        location=...,
        name=...,
        network_security_rules=...,
        provisioning_state=...,
        public_ip_prefix_id=...,
        public_i_pv6_prefix_id=...,
        service_endpoints=...,
        sku=...,
        subnet_id=...,
        system_data=...,
        tags=...,
        type=...,
        upgrade_description=...,
        use_custom_vnet=...,
        zonal_resiliency=...,
        zonal_update_mode=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addonFeatures")
    def addon_features(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="adminUserName")
    def admin_user_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowRdpAccess")
    def allow_rdp_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="applicationTypeVersionsCleanupPolicy")
    def application_type_versions_cleanup_policy(
        self,
    ) -> Optional[outputs.ApplicationTypeVersionsCleanupPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="auxiliarySubnets")
    def auxiliary_subnets(self) -> Optional[Sequence[outputs.SubnetResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureActiveDirectory")
    def azure_active_directory(
        self,
    ) -> Optional[outputs.AzureActiveDirectoryResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientConnectionPort")
    def client_connection_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def clients(self) -> Optional[Sequence[outputs.ClientCertificateResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterCertificateThumbprints")
    def cluster_certificate_thumbprints(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterCodeVersion")
    def cluster_code_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterState")
    def cluster_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterUpgradeCadence")
    def cluster_upgrade_cadence(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterUpgradeMode")
    def cluster_upgrade_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ddosProtectionPlanId")
    def ddos_protection_plan_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableAutoOSUpgrade")
    def enable_auto_os_upgrade(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableHttpGatewayExclusiveAuthMode")
    def enable_http_gateway_exclusive_auth_mode(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableServicePublicIP")
    def enable_service_public_ip(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fabricSettings")
    def fabric_settings(
        self,
    ) -> Optional[Sequence[outputs.SettingsSectionDescriptionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpGatewayConnectionPort")
    def http_gateway_connection_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="httpGatewayTokenAuthConnectionPort")
    def http_gateway_token_auth_connection_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[Sequence[outputs.IpTagResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingRules")
    def load_balancing_rules(
        self,
    ) -> Optional[Sequence[outputs.LoadBalancingRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityRules")
    def network_security_rules(
        self,
    ) -> Optional[Sequence[outputs.NetworkSecurityRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicIPPrefixId")
    def public_ip_prefix_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPv6PrefixId")
    def public_i_pv6_prefix_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(
        self,
    ) -> Optional[Sequence[outputs.ServiceEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...
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
    @pulumi.getter(name="upgradeDescription")
    def upgrade_description(self) -> Optional[outputs.ClusterUpgradePolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="useCustomVnet")
    def use_custom_vnet(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="zonalResiliency")
    def zonal_resiliency(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="zonalUpdateMode")
    def zonal_update_mode(self) -> Optional[_builtins.str]: ...

class AwaitableGetManagedClusterResult(GetManagedClusterResult):
    def __await__(self): ...

def get_managed_cluster(
    cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagedClusterResult: ...
def get_managed_cluster_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagedClusterResult]: ...
