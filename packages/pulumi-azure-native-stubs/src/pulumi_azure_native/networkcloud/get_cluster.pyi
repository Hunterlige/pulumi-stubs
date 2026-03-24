

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClusterResult', 'AwaitableGetClusterResult', 'get_cluster', 'get_cluster_output']
@pulumi.output_type
class GetClusterResult:
    def __init__(__self__, aggregator_or_single_rack_definition=..., analytics_output_settings=..., analytics_workspace_id=..., available_upgrade_versions=..., azure_api_version=..., cluster_capacity=..., cluster_connection_status=..., cluster_extended_location=..., cluster_location=..., cluster_manager_connection_status=..., cluster_manager_id=..., cluster_service_principal=..., cluster_type=..., cluster_version=..., command_output_settings=..., compute_deployment_threshold=..., compute_rack_definitions=..., detailed_status=..., detailed_status_message=..., etag=..., extended_location=..., hybrid_aks_extended_location=..., id=..., identity=..., location=..., managed_resource_group_configuration=..., manual_action_count=..., name=..., network_fabric_id=..., provisioning_state=..., runtime_protection_configuration=..., secret_archive=..., secret_archive_settings=..., support_expiry_date=..., system_data=..., tags=..., type=..., update_strategy=..., vulnerability_scanning_settings=..., workload_resource_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregatorOrSingleRackDefinition")
    def aggregator_or_single_rack_definition(self) -> outputs.RackDefinitionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsOutputSettings")
    def analytics_output_settings(self) -> Optional[outputs.AnalyticsOutputSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsWorkspaceId")
    def analytics_workspace_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableUpgradeVersions")
    def available_upgrade_versions(self) -> Sequence[outputs.ClusterAvailableUpgradeVersionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterCapacity")
    def cluster_capacity(self) -> outputs.ClusterCapacityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterConnectionStatus")
    def cluster_connection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterExtendedLocation")
    def cluster_extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterLocation")
    def cluster_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterManagerConnectionStatus")
    def cluster_manager_connection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterManagerId")
    def cluster_manager_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterServicePrincipal")
    def cluster_service_principal(self) -> Optional[outputs.ServicePrincipalInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandOutputSettings")
    def command_output_settings(self) -> Optional[outputs.CommandOutputSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeDeploymentThreshold")
    def compute_deployment_threshold(self) -> Optional[outputs.ValidationThresholdResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeRackDefinitions")
    def compute_rack_definitions(self) -> Optional[Sequence[outputs.RackDefinitionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridAksExtendedLocation")
    def hybrid_aks_extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> Optional[outputs.ManagedResourceGroupConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualActionCount")
    def manual_action_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeProtectionConfiguration")
    def runtime_protection_configuration(self) -> Optional[outputs.RuntimeProtectionConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArchive")
    def secret_archive(self) -> Optional[outputs.ClusterSecretArchiveResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArchiveSettings")
    def secret_archive_settings(self) -> Optional[outputs.SecretArchiveSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportExpiryDate")
    def support_expiry_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> Optional[outputs.ClusterUpdateStrategyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vulnerabilityScanningSettings")
    def vulnerability_scanning_settings(self) -> Optional[outputs.VulnerabilityScanningSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadResourceIds")
    def workload_resource_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetClusterResult]:
        ...
    


def get_cluster(cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClusterResult:
    
    ...

def get_cluster_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClusterResult]:
    
    ...

