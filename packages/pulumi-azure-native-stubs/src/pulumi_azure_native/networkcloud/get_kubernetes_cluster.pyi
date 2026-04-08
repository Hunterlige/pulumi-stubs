import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKubernetesClusterResult",
    "AwaitableGetKubernetesClusterResult",
    "get_kubernetes_cluster",
    "get_kubernetes_cluster_output",
]

@pulumi.output_type
class GetKubernetesClusterResult:
    def __init__(
        __self__,
        aad_configuration=...,
        administrator_configuration=...,
        attached_network_ids=...,
        available_upgrades=...,
        azure_api_version=...,
        cluster_id=...,
        connected_cluster_id=...,
        control_plane_kubernetes_version=...,
        control_plane_node_configuration=...,
        detailed_status=...,
        detailed_status_message=...,
        etag=...,
        extended_location=...,
        feature_statuses=...,
        id=...,
        initial_agent_pool_configurations=...,
        kubernetes_version=...,
        location=...,
        managed_resource_group_configuration=...,
        name=...,
        network_configuration=...,
        nodes=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadConfiguration")
    def aad_configuration(self) -> Optional[outputs.AadConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="administratorConfiguration")
    def administrator_configuration(
        self,
    ) -> Optional[outputs.AdministratorConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="attachedNetworkIds")
    def attached_network_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availableUpgrades")
    def available_upgrades(self) -> Sequence[outputs.AvailableUpgradeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectedClusterId")
    def connected_cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneKubernetesVersion")
    def control_plane_kubernetes_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodeConfiguration")
    def control_plane_node_configuration(
        self,
    ) -> outputs.ControlPlaneNodeConfigurationResponse: ...
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
    @pulumi.getter(name="featureStatuses")
    def feature_statuses(self) -> Sequence[outputs.FeatureStatusResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="initialAgentPoolConfigurations")
    def initial_agent_pool_configurations(
        self,
    ) -> Sequence[outputs.InitialAgentPoolConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(
        self,
    ) -> Optional[outputs.ManagedResourceGroupConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> outputs.NetworkConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Sequence[outputs.KubernetesClusterNodeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetKubernetesClusterResult(GetKubernetesClusterResult):
    def __await__(self): ...

def get_kubernetes_cluster(
    kubernetes_cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKubernetesClusterResult: ...
def get_kubernetes_cluster_output(
    kubernetes_cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKubernetesClusterResult]: ...
