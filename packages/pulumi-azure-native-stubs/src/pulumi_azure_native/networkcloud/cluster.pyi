

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, aggregator_or_single_rack_definition: pulumi.Input[RackDefinitionArgs], cluster_type: pulumi.Input[Union[_builtins.str, ClusterType]], cluster_version: pulumi.Input[_builtins.str], extended_location: pulumi.Input[ExtendedLocationArgs], network_fabric_id: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], analytics_output_settings: Optional[pulumi.Input[AnalyticsOutputSettingsArgs]] = ..., analytics_workspace_id: Optional[pulumi.Input[_builtins.str]] = ..., cluster_location: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_service_principal: Optional[pulumi.Input[ServicePrincipalInformationArgs]] = ..., command_output_settings: Optional[pulumi.Input[CommandOutputSettingsArgs]] = ..., compute_deployment_threshold: Optional[pulumi.Input[ValidationThresholdArgs]] = ..., compute_rack_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[RackDefinitionArgs]]]] = ..., identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_resource_group_configuration: Optional[pulumi.Input[ManagedResourceGroupConfigurationArgs]] = ..., runtime_protection_configuration: Optional[pulumi.Input[RuntimeProtectionConfigurationArgs]] = ..., secret_archive: Optional[pulumi.Input[ClusterSecretArchiveArgs]] = ..., secret_archive_settings: Optional[pulumi.Input[SecretArchiveSettingsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_strategy: Optional[pulumi.Input[ClusterUpdateStrategyArgs]] = ..., vulnerability_scanning_settings: Optional[pulumi.Input[VulnerabilityScanningSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregatorOrSingleRackDefinition")
    def aggregator_or_single_rack_definition(self) -> pulumi.Input[RackDefinitionArgs]:
        
        ...
    
    @aggregator_or_single_rack_definition.setter
    def aggregator_or_single_rack_definition(self, value: pulumi.Input[RackDefinitionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Input[Union[_builtins.str, ClusterType]]:
        
        ...
    
    @cluster_type.setter
    def cluster_type(self, value: pulumi.Input[Union[_builtins.str, ClusterType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_version.setter
    def cluster_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationArgs]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_fabric_id.setter
    def network_fabric_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsOutputSettings")
    def analytics_output_settings(self) -> Optional[pulumi.Input[AnalyticsOutputSettingsArgs]]:
        
        ...
    
    @analytics_output_settings.setter
    def analytics_output_settings(self, value: Optional[pulumi.Input[AnalyticsOutputSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsWorkspaceId")
    def analytics_workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @analytics_workspace_id.setter
    def analytics_workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterLocation")
    def cluster_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_location.setter
    def cluster_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterServicePrincipal")
    def cluster_service_principal(self) -> Optional[pulumi.Input[ServicePrincipalInformationArgs]]:
        
        ...
    
    @cluster_service_principal.setter
    def cluster_service_principal(self, value: Optional[pulumi.Input[ServicePrincipalInformationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandOutputSettings")
    def command_output_settings(self) -> Optional[pulumi.Input[CommandOutputSettingsArgs]]:
        
        ...
    
    @command_output_settings.setter
    def command_output_settings(self, value: Optional[pulumi.Input[CommandOutputSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeDeploymentThreshold")
    def compute_deployment_threshold(self) -> Optional[pulumi.Input[ValidationThresholdArgs]]:
        
        ...
    
    @compute_deployment_threshold.setter
    def compute_deployment_threshold(self, value: Optional[pulumi.Input[ValidationThresholdArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeRackDefinitions")
    def compute_rack_definitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RackDefinitionArgs]]]]:
        
        ...
    
    @compute_rack_definitions.setter
    def compute_rack_definitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RackDefinitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> Optional[pulumi.Input[ManagedResourceGroupConfigurationArgs]]:
        
        ...
    
    @managed_resource_group_configuration.setter
    def managed_resource_group_configuration(self, value: Optional[pulumi.Input[ManagedResourceGroupConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeProtectionConfiguration")
    def runtime_protection_configuration(self) -> Optional[pulumi.Input[RuntimeProtectionConfigurationArgs]]:
        
        ...
    
    @runtime_protection_configuration.setter
    def runtime_protection_configuration(self, value: Optional[pulumi.Input[RuntimeProtectionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArchive")
    def secret_archive(self) -> Optional[pulumi.Input[ClusterSecretArchiveArgs]]:
        
        ...
    
    @secret_archive.setter
    def secret_archive(self, value: Optional[pulumi.Input[ClusterSecretArchiveArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArchiveSettings")
    def secret_archive_settings(self) -> Optional[pulumi.Input[SecretArchiveSettingsArgs]]:
        
        ...
    
    @secret_archive_settings.setter
    def secret_archive_settings(self, value: Optional[pulumi.Input[SecretArchiveSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> Optional[pulumi.Input[ClusterUpdateStrategyArgs]]:
        
        ...
    
    @update_strategy.setter
    def update_strategy(self, value: Optional[pulumi.Input[ClusterUpdateStrategyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vulnerabilityScanningSettings")
    def vulnerability_scanning_settings(self) -> Optional[pulumi.Input[VulnerabilityScanningSettingsArgs]]:
        
        ...
    
    @vulnerability_scanning_settings.setter
    def vulnerability_scanning_settings(self, value: Optional[pulumi.Input[VulnerabilityScanningSettingsArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:networkcloud:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aggregator_or_single_rack_definition: Optional[pulumi.Input[Union[RackDefinitionArgs, RackDefinitionArgsDict]]] = ..., analytics_output_settings: Optional[pulumi.Input[Union[AnalyticsOutputSettingsArgs, AnalyticsOutputSettingsArgsDict]]] = ..., analytics_workspace_id: Optional[pulumi.Input[_builtins.str]] = ..., cluster_location: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_service_principal: Optional[pulumi.Input[Union[ServicePrincipalInformationArgs, ServicePrincipalInformationArgsDict]]] = ..., cluster_type: Optional[pulumi.Input[Union[_builtins.str, ClusterType]]] = ..., cluster_version: Optional[pulumi.Input[_builtins.str]] = ..., command_output_settings: Optional[pulumi.Input[Union[CommandOutputSettingsArgs, CommandOutputSettingsArgsDict]]] = ..., compute_deployment_threshold: Optional[pulumi.Input[Union[ValidationThresholdArgs, ValidationThresholdArgsDict]]] = ..., compute_rack_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RackDefinitionArgs, RackDefinitionArgsDict]]]]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_resource_group_configuration: Optional[pulumi.Input[Union[ManagedResourceGroupConfigurationArgs, ManagedResourceGroupConfigurationArgsDict]]] = ..., network_fabric_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., runtime_protection_configuration: Optional[pulumi.Input[Union[RuntimeProtectionConfigurationArgs, RuntimeProtectionConfigurationArgsDict]]] = ..., secret_archive: Optional[pulumi.Input[Union[ClusterSecretArchiveArgs, ClusterSecretArchiveArgsDict]]] = ..., secret_archive_settings: Optional[pulumi.Input[Union[SecretArchiveSettingsArgs, SecretArchiveSettingsArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_strategy: Optional[pulumi.Input[Union[ClusterUpdateStrategyArgs, ClusterUpdateStrategyArgsDict]]] = ..., vulnerability_scanning_settings: Optional[pulumi.Input[Union[VulnerabilityScanningSettingsArgs, VulnerabilityScanningSettingsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregatorOrSingleRackDefinition")
    def aggregator_or_single_rack_definition(self) -> pulumi.Output[outputs.RackDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsOutputSettings")
    def analytics_output_settings(self) -> pulumi.Output[Optional[outputs.AnalyticsOutputSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsWorkspaceId")
    def analytics_workspace_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableUpgradeVersions")
    def available_upgrade_versions(self) -> pulumi.Output[Sequence[outputs.ClusterAvailableUpgradeVersionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterCapacity")
    def cluster_capacity(self) -> pulumi.Output[outputs.ClusterCapacityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterConnectionStatus")
    def cluster_connection_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterExtendedLocation")
    def cluster_extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterLocation")
    def cluster_location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterManagerConnectionStatus")
    def cluster_manager_connection_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterManagerId")
    def cluster_manager_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterServicePrincipal")
    def cluster_service_principal(self) -> pulumi.Output[Optional[outputs.ServicePrincipalInformationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandOutputSettings")
    def command_output_settings(self) -> pulumi.Output[Optional[outputs.CommandOutputSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeDeploymentThreshold")
    def compute_deployment_threshold(self) -> pulumi.Output[Optional[outputs.ValidationThresholdResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeRackDefinitions")
    def compute_rack_definitions(self) -> pulumi.Output[Optional[Sequence[outputs.RackDefinitionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridAksExtendedLocation")
    def hybrid_aks_extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> pulumi.Output[Optional[outputs.ManagedResourceGroupConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualActionCount")
    def manual_action_count(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeProtectionConfiguration")
    def runtime_protection_configuration(self) -> pulumi.Output[Optional[outputs.RuntimeProtectionConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArchive")
    def secret_archive(self) -> pulumi.Output[Optional[outputs.ClusterSecretArchiveResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArchiveSettings")
    def secret_archive_settings(self) -> pulumi.Output[Optional[outputs.SecretArchiveSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportExpiryDate")
    def support_expiry_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> pulumi.Output[Optional[outputs.ClusterUpdateStrategyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vulnerabilityScanningSettings")
    def vulnerability_scanning_settings(self) -> pulumi.Output[Optional[outputs.VulnerabilityScanningSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadResourceIds")
    def workload_resource_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


