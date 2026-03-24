

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ACRPropertiesResponse', 'AKSAssessmentDetailsResponse', 'AKSAssessmentSettingsResponse', 'AKSDeploymentPropertiesResponse', 'AKSDeploymentSpecificationResponse', ..., 'ApacheTomcatAKSWorkloadDeploymentResponse', 'ApacheTomcatWebApplicationResponse', ..., 'AppInsightMonitoringPropertiesResponse', 'AppSvcContainerSettingsResponse', 'AppSvcNativeSettingsResponse', 'ArgResponse', 'AssessmentDetailsResponse', 'AssessmentPropertiesResponse', 'AssessmentScopeParametersResponse', 'AutomaticResolutionPropertiesResponse', 'AutomationArtifactResponse', 'AvailabilitySetResourceSettingsResponse', 'AvsAssessmentPropertiesV2Response', 'AvsAssessmentSettingsResponse', 'AvsEstimatedExternalStorageResponse', 'AvsEstimatedNetworkResponse', 'AvsEstimatedNodeResponse', 'AzureArcManagementSettingsResponse', 'AzureArcMonitoringSettingsResponse', 'AzureArcSettingsResponse', 'AzureFileShareHydrationProfileResponse', 'AzureSettingsResponse', 'BillingSettingsResponse', 'BindingResponse', 'CertResponse', 'CollectorAgentPropertiesBaseResponse', 'CollectorAgentPropertiesResponse', 'CollectorAgentSpnPropertiesBaseResponse', 'CollectorBodyAgentSpnPropertiesResponse', 'CollectorPropertiesResponse', 'CompoundAssessmentDetailsResponse', 'CompoundAssessmentPropertiesResponse', 'ComputeSettingsResponse', 'ContainerImagePropertiesResponse', 'CostComponentResponse', 'DatabaseProjectSummaryResponse', 'DatabasesSolutionSummaryResponse', 'DeployedResourcesPropertiesResponse', 'DirectoryPathResponse', 'DiscoveredEntityLightSummaryResponse', 'DiskEncryptionSetResourceSettingsResponse', 'EntityUptimeResponse', 'FacilitySettingsResponse', 'GmsaAuthenticationPropertiesResponse', 'GroupPropertiesResponse', 'HealthErrorModelResponse', 'HeterogeneousAssessmentPropertiesResponse', 'HypervLicenseResponse', 'HypervVirtualizationManagementSettingsResponse', ..., 'IISAKSWorkloadDeploymentResponse', 'IISApplicationDetailsResponse', 'IISVirtualApplicationDetailsResponse', 'IISWebApplicationResponse', 'IISWebServerResponse', 'IISWorkloadInstanceModelCustomPropertiesResponse', 'IdentityModelResponse', 'IdentityResponse', 'ImportCollectorPropertiesResponse', 'ImportSqlCollectorPropertiesResponse', 'InnerHealthErrorModelResponse', 'JobStatusResponse', 'KeyVaultResourceSettingsResponse', 'KeyVaultSecretStorePropertiesResponse', 'LBBackendAddressPoolResourceSettingsResponse', 'LBFrontendIPConfigurationResourceSettingsResponse', 'LaborSettingsResponse', 'LinuxServerLicensingSettingsResponse', 'LoadBalancerBackendAddressPoolReferenceResponse', 'LoadBalancerNatRuleReferenceResponse', 'LoadBalancerResourceSettingsResponse', 'MachineAssessmentSettingsResponse', 'MachineAssessmentV2PropertiesResponse', 'ManagedIdentityPropertiesResponse', 'ManagementSettingsResponse', 'ManualResolutionPropertiesResponse', 'MigrateAgentModelPropertiesResponse', 'MigrateAgentModelResponseSystemData', 'MigrateProjectPropertiesResponse', 'MigrateProjectPropertiesResponseV1', 'MigrateProjectResponseTags', 'MigrationConfigurationResponse', 'MigrationEntityGroupPropertiesResponse', 'MigrationEntityPropertiesResponse', 'ModernizeProjectModelPropertiesResponse', 'ModernizeProjectModelResponseSystemData', 'MoveCollectionPropertiesResponse', 'MoveCollectionPropertiesResponseErrors', 'MoveResourceDependencyOverrideResponse', 'MoveResourceDependencyResponse', 'MoveResourceErrorBodyResponse', 'MoveResourceErrorResponse', 'MoveResourcePropertiesResponse', 'MoveResourcePropertiesResponseErrors', 'MoveResourcePropertiesResponseMoveStatus', 'NetworkInterfaceResourceSettingsResponse', 'NetworkSecurityGroupResourceSettingsResponse', 'NetworkSettingsResponse', 'NicIpConfigurationResourceSettingsResponse', 'NsgReferenceResponse', 'NsgSecurityRuleResponse', 'OnPremiseSettingsResponse', 'OperatingSystemDetailsResponse', 'OtherManagementCostsSettingsResponse', 'PerfDataSettingsResponse', 'PerformanceDataResponse', 'PortMappingResponse', 'PrivateEndpointConnectionPropertiesResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointConnectionResponseV1', 'PrivateEndpointConnectionResponseV2', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'ProjectPropertiesResponse', 'ProjectSummaryResponse', 'PublicIPAddressResourceSettingsResponse', 'PublicIpReferenceResponse', 'ReportDetailsResponse', 'ResourceGroupResourceSettingsResponse', 'ResourceIdResponse', 'ResourceIdentityResponse', 'ResourceRequirementsResponse', 'SavingsSettingsResponse', 'ScopeResponse', 'SecretStoreDetailsResponse', 'SecretStorePropertiesResponse', 'SecuritySettingsResponse', 'ServerMigrationSpecificPropertiesResponse', 'ServersProjectSummaryResponse', 'ServersSolutionSummaryResponse', 'SettingsResponse', 'SolutionDetailsResponse', 'SolutionPropertiesResponse', 'SqlAssessmentSettingsResponse', 'SqlAssessmentV3PropertiesResponse', 'SqlDatabaseResourceSettingsResponse', 'SqlDbSettingsResponse', 'SqlDbSettingsV3Response', 'SqlElasticPoolResourceSettingsResponse', 'SqlMiSettingsResponse', 'SqlMiSettingsV3Response', 'SqlServerLicensingSettingsResponse', 'SqlServerResourceSettingsResponse', 'SqlVmSettingsResponse', 'StorageSettingsResponse', 'SubnetReferenceResponse', 'SubnetResourceSettingsResponse', 'SystemDataResponse', 'TargetAssessmentArmIdsResponse', 'TargetStorageProfileResponse', 'TaskPropertiesResponse', 'ThirdPartyManagementSettingsResponse', 'UserAssignedIdentityResponse', 'VMwareMigrateAgentModelCustomPropertiesResponse', 'VirtualMachineResourceSettingsResponse', 'VirtualNetworkResourceSettingsResponse', 'VirtualizationSoftwareSettingsResponse', 'VmUptimeResponse', 'VmUptimeResponseV1', 'VmUptimeResponseV2', 'WavePropertiesResponse', 'WebAppAssessmentSettingsResponse', 'WebAppAssessmentV3PropertiesResponse', 'WebApplicationConfigurationResponse', 'WebApplicationDirectoryResponse', 'WebApplicationFrameworkResponse', 'WindowsServerLicensingSettingsResponse', 'WorkloadDeploymentModelPropertiesResponse', ..., 'WorkloadDeploymentModelResponseSystemData', 'WorkloadInstanceModelPropertiesResponse', 'WorkloadInstanceModelPropertiesResponseCurrentJob', 'WorkloadInstanceModelResponseSystemData']
@pulumi.output_type
class ACRPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, registry_name: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AKSAssessmentDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, confidence_rating_in_percentage: _builtins.float, created_timestamp: _builtins.str, machine_count: _builtins.int, prices_timestamp: _builtins.str, status: _builtins.str, total_monthly_cost: _builtins.float, updated_timestamp: _builtins.str, web_app_count: _builtins.int, web_server_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineCount")
    def machine_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricesTimestamp")
    def prices_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalMonthlyCost")
    def total_monthly_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppCount")
    def web_app_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerCount")
    def web_server_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AKSAssessmentSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_location: _builtins.str, category: _builtins.str, consolidation: _builtins.str, currency: _builtins.str, environment_type: _builtins.str, licensing_program: _builtins.str, pricing_tier: _builtins.str, savings_options: _builtins.str, sizing_criteria: _builtins.str, discount_percentage: Optional[_builtins.float] = ..., performance_data: Optional[outputs.PerfDataSettingsResponse] = ..., scaling_factor: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def consolidation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licensingProgram")
    def licensing_program(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingTier")
    def pricing_tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsOptions")
    def savings_options(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingCriteria")
    def sizing_criteria(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> Optional[outputs.PerfDataSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AKSDeploymentPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aks_cluster_name: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aksClusterName")
    def aks_cluster_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AKSDeploymentSpecificationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kubernetes_objects_yaml: Optional[_builtins.str] = ..., load_balancer_type: Optional[_builtins.str] = ..., replica_count: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesObjectsYaml")
    def kubernetes_objects_yaml(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApacheTomcatAKSWorkloadDeploymentModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, apache_tomcat_aks_workload_deployment_properties: Optional[outputs.ApacheTomcatAKSWorkloadDeploymentResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apacheTomcatAksWorkloadDeploymentProperties")
    def apache_tomcat_aks_workload_deployment_properties(self) -> Optional[outputs.ApacheTomcatAKSWorkloadDeploymentResponse]:
        
        ...
    


@pulumi.output_type
class ApacheTomcatAKSWorkloadDeploymentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_history: Sequence[outputs.DeployedResourcesPropertiesResponse], automation_artifact_properties: Optional[outputs.AutomationArtifactResponse] = ..., bindings: Optional[Sequence[outputs.BindingResponse]] = ..., build_container_images: Optional[Sequence[outputs.ContainerImagePropertiesResponse]] = ..., cluster_properties: Optional[outputs.AKSDeploymentPropertiesResponse] = ..., configurations: Optional[Sequence[outputs.WebApplicationConfigurationResponse]] = ..., container_image_properties: Optional[outputs.ContainerImagePropertiesResponse] = ..., deployment_name_prefix: Optional[_builtins.str] = ..., deployment_spec: Optional[outputs.AKSDeploymentSpecificationResponse] = ..., directories: Optional[Sequence[outputs.WebApplicationDirectoryResponse]] = ..., limits: Optional[outputs.ResourceRequirementsResponse] = ..., monitoring_properties: Optional[outputs.AppInsightMonitoringPropertiesResponse] = ..., requests: Optional[outputs.ResourceRequirementsResponse] = ..., target_platform_identity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentHistory")
    def deployment_history(self) -> Sequence[outputs.DeployedResourcesPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationArtifactProperties")
    def automation_artifact_properties(self) -> Optional[outputs.AutomationArtifactResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bindings(self) -> Optional[Sequence[outputs.BindingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildContainerImages")
    def build_container_images(self) -> Optional[Sequence[outputs.ContainerImagePropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterProperties")
    def cluster_properties(self) -> Optional[outputs.AKSDeploymentPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.WebApplicationConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerImageProperties")
    def container_image_properties(self) -> Optional[outputs.ContainerImagePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentNamePrefix")
    def deployment_name_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentSpec")
    def deployment_spec(self) -> Optional[outputs.AKSDeploymentSpecificationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def directories(self) -> Optional[Sequence[outputs.WebApplicationDirectoryResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[outputs.ResourceRequirementsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringProperties")
    def monitoring_properties(self) -> Optional[outputs.AppInsightMonitoringPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[outputs.ResourceRequirementsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPlatformIdentity")
    def target_platform_identity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApacheTomcatWebApplicationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_id: Optional[_builtins.str] = ..., application_name: Optional[_builtins.str] = ..., application_scratch_path: Optional[_builtins.str] = ..., bindings: Optional[Sequence[outputs.BindingResponse]] = ..., configurations: Optional[Sequence[outputs.WebApplicationConfigurationResponse]] = ..., directories: Optional[Sequence[outputs.WebApplicationDirectoryResponse]] = ..., discovered_frameworks: Optional[Sequence[outputs.WebApplicationFrameworkResponse]] = ..., display_name: Optional[_builtins.str] = ..., limits: Optional[outputs.ResourceRequirementsResponse] = ..., path: Optional[outputs.DirectoryPathResponse] = ..., primary_framework: Optional[outputs.WebApplicationFrameworkResponse] = ..., requests: Optional[outputs.ResourceRequirementsResponse] = ..., web_server_id: Optional[_builtins.str] = ..., web_server_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationScratchPath")
    def application_scratch_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bindings(self) -> Optional[Sequence[outputs.BindingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.WebApplicationConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def directories(self) -> Optional[Sequence[outputs.WebApplicationDirectoryResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredFrameworks")
    def discovered_frameworks(self) -> Optional[Sequence[outputs.WebApplicationFrameworkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[outputs.ResourceRequirementsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[outputs.DirectoryPathResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFramework")
    def primary_framework(self) -> Optional[outputs.WebApplicationFrameworkResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[outputs.ResourceRequirementsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerId")
    def web_server_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerName")
    def web_server_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApacheTomcatWorkloadInstanceModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, apache_tomcat_web_application: Optional[outputs.ApacheTomcatWebApplicationResponse] = ..., web_app_arm_id: Optional[_builtins.str] = ..., web_app_site_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apacheTomcatWebApplication")
    def apache_tomcat_web_application(self) -> Optional[outputs.ApacheTomcatWebApplicationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppArmId")
    def web_app_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppSiteName")
    def web_app_site_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppInsightMonitoringPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_insights_name: Optional[_builtins.str] = ..., is_enabled: Optional[_builtins.bool] = ..., region: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., secret_store_details: Optional[outputs.SecretStoreDetailsResponse] = ..., subscription_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appInsightsName")
    def app_insights_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStoreDetails")
    def secret_store_details(self) -> Optional[outputs.SecretStoreDetailsResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppSvcContainerSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, isolation_required: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isolationRequired")
    def isolation_required(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class AppSvcNativeSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, isolation_required: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isolationRequired")
    def isolation_required(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class ArgResponse(dict):
    
    def __init__(__self__, *, query: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AssessmentDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, confidence_rating_in_percentage: _builtins.float, created_timestamp: _builtins.str, prices_timestamp: _builtins.str, status: _builtins.str, updated_timestamp: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricesTimestamp")
    def prices_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AssessmentPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_disk_type: _builtins.str, azure_hybrid_use_benefit: _builtins.str, azure_location: _builtins.str, azure_offer_code: _builtins.str, azure_pricing_tier: _builtins.str, azure_storage_redundancy: _builtins.str, azure_vm_families: Sequence[_builtins.str], confidence_rating_in_percentage: _builtins.float, created_timestamp: _builtins.str, currency: _builtins.str, discount_percentage: _builtins.float, ea_subscription_id: _builtins.str, monthly_bandwidth_cost: _builtins.float, monthly_compute_cost: _builtins.float, monthly_premium_storage_cost: _builtins.float, monthly_standard_ssd_storage_cost: _builtins.float, monthly_storage_cost: _builtins.float, number_of_machines: _builtins.int, percentile: _builtins.str, perf_data_end_time: _builtins.str, perf_data_start_time: _builtins.str, prices_timestamp: _builtins.str, reserved_instance: _builtins.str, scaling_factor: _builtins.float, sizing_criterion: _builtins.str, stage: _builtins.str, status: _builtins.str, time_range: _builtins.str, updated_timestamp: _builtins.str, vm_uptime: outputs.VmUptimeResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDiskType")
    def azure_disk_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureHybridUseBenefit")
    def azure_hybrid_use_benefit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azurePricingTier")
    def azure_pricing_tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureStorageRedundancy")
    def azure_storage_redundancy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVmFamilies")
    def azure_vm_families(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eaSubscriptionId")
    def ea_subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyBandwidthCost")
    def monthly_bandwidth_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyComputeCost")
    def monthly_compute_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyPremiumStorageCost")
    def monthly_premium_storage_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyStandardSSDStorageCost")
    def monthly_standard_ssd_storage_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyStorageCost")
    def monthly_storage_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percentile(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perfDataEndTime")
    def perf_data_end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perfDataStartTime")
    def perf_data_start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricesTimestamp")
    def prices_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedInstance")
    def reserved_instance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmUptime")
    def vm_uptime(self) -> outputs.VmUptimeResponse:
        
        ...
    


@pulumi.output_type
class AssessmentScopeParametersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, server_group_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverGroupId")
    def server_group_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomaticResolutionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, move_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moveResourceId")
    def move_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomationArtifactResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, artifacts: Optional[Mapping[str, _builtins.str]] = ..., azure_file_share_profile: Optional[outputs.AzureFileShareHydrationProfileResponse] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def artifacts(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFileShareProfile")
    def azure_file_share_profile(self) -> Optional[outputs.AzureFileShareHydrationProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AvailabilitySetResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, fault_domain: Optional[_builtins.int] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ..., update_domain: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="faultDomain")
    def fault_domain(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateDomain")
    def update_domain(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AvsAssessmentPropertiesV2Response(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, details: Optional[outputs.AssessmentDetailsResponse] = ..., fallback_machine_assessment_arm_id: Optional[_builtins.str] = ..., scope: Optional[outputs.ScopeResponse] = ..., settings: Optional[outputs.AvsAssessmentSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[outputs.AssessmentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackMachineAssessmentArmId")
    def fallback_machine_assessment_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.ScopeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.AvsAssessmentSettingsResponse]:
        
        ...
    


@pulumi.output_type
class AvsAssessmentSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, avs_assessment_scenario: Optional[_builtins.str] = ..., azure_location: Optional[_builtins.str] = ..., billing_settings: Optional[outputs.BillingSettingsResponse] = ..., cpu_headroom: Optional[_builtins.float] = ..., currency: Optional[_builtins.str] = ..., dedupe_compression: Optional[_builtins.float] = ..., discount_percentage: Optional[_builtins.float] = ..., environment_type: Optional[_builtins.str] = ..., external_storage_types: Optional[Sequence[_builtins.str]] = ..., failures_to_tolerate_and_raid_level_list: Optional[Sequence[_builtins.str]] = ..., is_stretch_cluster_enabled: Optional[_builtins.bool] = ..., is_vcf_byol_enabled: Optional[_builtins.bool] = ..., mem_overcommit: Optional[_builtins.float] = ..., node_types: Optional[Sequence[_builtins.str]] = ..., performance_data: Optional[outputs.PerformanceDataResponse] = ..., savings_settings: Optional[outputs.SavingsSettingsResponse] = ..., scaling_factor: Optional[_builtins.float] = ..., sizing_criterion: Optional[_builtins.str] = ..., vcpu_oversubscription: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsAssessmentScenario")
    def avs_assessment_scenario(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingSettings")
    def billing_settings(self) -> Optional[outputs.BillingSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuHeadroom")
    def cpu_headroom(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedupeCompression")
    def dedupe_compression(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalStorageTypes")
    def external_storage_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failuresToTolerateAndRaidLevelList")
    def failures_to_tolerate_and_raid_level_list(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isStretchClusterEnabled")
    def is_stretch_cluster_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isVcfByolEnabled")
    def is_vcf_byol_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memOvercommit")
    def mem_overcommit(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypes")
    def node_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> Optional[outputs.PerformanceDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsSettings")
    def savings_settings(self) -> Optional[outputs.SavingsSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuOversubscription")
    def vcpu_oversubscription(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AvsEstimatedExternalStorageResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, monthly_price: Optional[_builtins.float] = ..., storage_type: Optional[_builtins.str] = ..., storage_utilization: Optional[_builtins.float] = ..., total_storage_in_gb: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyPrice")
    def monthly_price(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageUtilization")
    def storage_utilization(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStorageInGB")
    def total_storage_in_gb(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AvsEstimatedNetworkResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, monthly_price: Optional[_builtins.float] = ..., network_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyPrice")
    def monthly_price(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AvsEstimatedNodeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_utilization: Optional[_builtins.float] = ..., ftt_raid_level: Optional[_builtins.str] = ..., monthly_price: Optional[_builtins.float] = ..., node_number: Optional[_builtins.int] = ..., node_type: Optional[_builtins.str] = ..., pricing_model: Optional[_builtins.str] = ..., ram_utilization: Optional[_builtins.float] = ..., storage_utilization: Optional[_builtins.float] = ..., total_cpu: Optional[_builtins.float] = ..., total_ram: Optional[_builtins.float] = ..., total_storage: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuUtilization")
    def cpu_utilization(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fttRaidLevel")
    def ftt_raid_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyPrice")
    def monthly_price(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeNumber")
    def node_number(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingModel")
    def pricing_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ramUtilization")
    def ram_utilization(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageUtilization")
    def storage_utilization(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalCpu")
    def total_cpu(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalRam")
    def total_ram(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStorage")
    def total_storage(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AzureArcManagementSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, monitoring_settings: outputs.AzureArcMonitoringSettingsResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringSettings")
    def monitoring_settings(self) -> outputs.AzureArcMonitoringSettingsResponse:
        
        ...
    


@pulumi.output_type
class AzureArcMonitoringSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alert_rules_count: _builtins.int, logs_volume_in_gb: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRulesCount")
    def alert_rules_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsVolumeInGB")
    def logs_volume_in_gb(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class AzureArcSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_arc_state: _builtins.str, labor_cost_percentage: Optional[_builtins.float] = ..., management_settings: Optional[outputs.AzureArcManagementSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureArcState")
    def azure_arc_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="laborCostPercentage")
    def labor_cost_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementSettings")
    def management_settings(self) -> Optional[outputs.AzureArcManagementSettingsResponse]:
        
        ...
    


@pulumi.output_type
class AzureFileShareHydrationProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_file_share_dir_path: Optional[_builtins.str] = ..., azure_file_share_name: Optional[_builtins.str] = ..., azure_file_share_resource_group: Optional[_builtins.str] = ..., azure_file_share_storage_account: Optional[_builtins.str] = ..., azure_file_share_subscription_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFileShareDirPath")
    def azure_file_share_dir_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFileShareName")
    def azure_file_share_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFileShareResourceGroup")
    def azure_file_share_resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFileShareStorageAccount")
    def azure_file_share_storage_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFileShareSubscriptionId")
    def azure_file_share_subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, currency: Optional[_builtins.str] = ..., target_location: _builtins.str, avs_labor_cost_percentage: Optional[_builtins.float] = ..., business_case_type: Optional[_builtins.str] = ..., comfort_factor: Optional[_builtins.float] = ..., discount_percentage: Optional[_builtins.float] = ..., iaas_labor_cost_percentage: Optional[_builtins.float] = ..., infrastructure_growth_rate: Optional[_builtins.float] = ..., network_cost_percentage: Optional[_builtins.float] = ..., paas_labor_cost_percentage: Optional[_builtins.float] = ..., per_year_migration_completion_percentage: Optional[Mapping[str, _builtins.float]] = ..., performance_data_end_time: Optional[_builtins.str] = ..., performance_data_start_time: Optional[_builtins.str] = ..., performance_utilization_percentile: Optional[_builtins.float] = ..., savings_option: Optional[_builtins.str] = ..., wacc: Optional[_builtins.float] = ..., workload_discovery_source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLocation")
    def target_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsLaborCostPercentage")
    def avs_labor_cost_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="businessCaseType")
    def business_case_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="comfortFactor")
    def comfort_factor(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iaasLaborCostPercentage")
    def iaas_labor_cost_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureGrowthRate")
    def infrastructure_growth_rate(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCostPercentage")
    def network_cost_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="paasLaborCostPercentage")
    def paas_labor_cost_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perYearMigrationCompletionPercentage")
    def per_year_migration_completion_percentage(self) -> Optional[Mapping[str, _builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceDataEndTime")
    def performance_data_end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceDataStartTime")
    def performance_data_start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceUtilizationPercentile")
    def performance_utilization_percentile(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsOption")
    def savings_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wacc(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadDiscoverySource")
    def workload_discovery_source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BillingSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, licensing_program: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licensingProgram")
    def licensing_program(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BindingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, cert: Optional[outputs.CertResponse] = ..., host_name: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., port: Optional[_builtins.str] = ..., port_mapping: Optional[outputs.PortMappingResponse] = ..., protocol: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[outputs.CertResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portMapping")
    def port_mapping(self) -> Optional[outputs.PortMappingResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cert_data: Optional[_builtins.str] = ..., cert_needed: Optional[_builtins.bool] = ..., cert_provided: Optional[_builtins.bool] = ..., secret_store: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certData")
    def cert_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certNeeded")
    def cert_needed(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certProvided")
    def cert_provided(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CollectorAgentPropertiesBaseResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., last_heartbeat_utc: Optional[_builtins.str] = ..., spn_details: Optional[outputs.CollectorAgentSpnPropertiesBaseResponse] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spnDetails")
    def spn_details(self) -> Optional[outputs.CollectorAgentSpnPropertiesBaseResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CollectorAgentPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, last_heartbeat_utc: _builtins.str, version: _builtins.str, spn_details: Optional[outputs.CollectorBodyAgentSpnPropertiesResponse] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spnDetails")
    def spn_details(self) -> Optional[outputs.CollectorBodyAgentSpnPropertiesResponse]:
        ...
    


@pulumi.output_type
class CollectorAgentSpnPropertiesBaseResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_id: Optional[_builtins.str] = ..., audience: Optional[_builtins.str] = ..., authority: Optional[_builtins.str] = ..., object_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CollectorBodyAgentSpnPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_id: Optional[_builtins.str] = ..., audience: Optional[_builtins.str] = ..., authority: Optional[_builtins.str] = ..., object_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CollectorPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_timestamp: _builtins.str, updated_timestamp: _builtins.str, agent_properties: Optional[outputs.CollectorAgentPropertiesResponse] = ..., discovery_site_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentProperties")
    def agent_properties(self) -> Optional[outputs.CollectorAgentPropertiesResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CompoundAssessmentDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, status: _builtins.str, created_timestamp: Optional[_builtins.str] = ..., updated_timestamp: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CompoundAssessmentPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, details: outputs.CompoundAssessmentDetailsResponse, provisioning_state: _builtins.str, target_assessment_arm_ids: outputs.TargetAssessmentArmIdsResponse, fallback_machine_assessment_arm_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> outputs.CompoundAssessmentDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAssessmentArmIds")
    def target_assessment_arm_ids(self) -> outputs.TargetAssessmentArmIdsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackMachineAssessmentArmId")
    def fallback_machine_assessment_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ComputeSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hyperthread_core_to_memory_ratio: _builtins.float, price: _builtins.float, rhel_linux_server_licensing: outputs.LinuxServerLicensingSettingsResponse, sql_server_licensing: Sequence[outputs.SqlServerLicensingSettingsResponse], suse_linux_server_licensing: outputs.LinuxServerLicensingSettingsResponse, virtualization_software_settings: outputs.VirtualizationSoftwareSettingsResponse, windows_server_licensing: outputs.WindowsServerLicensingSettingsResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hyperthreadCoreToMemoryRatio")
    def hyperthread_core_to_memory_ratio(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def price(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rhelLinuxServerLicensing")
    def rhel_linux_server_licensing(self) -> outputs.LinuxServerLicensingSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerLicensing")
    def sql_server_licensing(self) -> Sequence[outputs.SqlServerLicensingSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suseLinuxServerLicensing")
    def suse_linux_server_licensing(self) -> outputs.LinuxServerLicensingSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualizationSoftwareSettings")
    def virtualization_software_settings(self) -> outputs.VirtualizationSoftwareSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsServerLicensing")
    def windows_server_licensing(self) -> outputs.WindowsServerLicensingSettingsResponse:
        
        ...
    


@pulumi.output_type
class ContainerImagePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, dockerfile: Optional[_builtins.str] = ..., image_name: Optional[_builtins.str] = ..., image_tag: Optional[_builtins.str] = ..., registry_properties: Optional[outputs.ACRPropertiesResponse] = ..., run_id: Optional[_builtins.str] = ..., run_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dockerfile(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryProperties")
    def registry_properties(self) -> Optional[outputs.ACRPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runId")
    def run_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runStatus")
    def run_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CostComponentResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, description: Optional[_builtins.str] = ..., value: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class DatabaseProjectSummaryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, extended_summary: Optional[Mapping[str, _builtins.str]] = ..., last_summary_refreshed_time: Optional[_builtins.str] = ..., refresh_summary_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedSummary")
    def extended_summary(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSummaryRefreshedTime")
    def last_summary_refreshed_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshSummaryState")
    def refresh_summary_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabasesSolutionSummaryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, database_instances_assessed_count: Optional[_builtins.int] = ..., databases_assessed_count: Optional[_builtins.int] = ..., migration_ready_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseInstancesAssessedCount")
    def database_instances_assessed_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databasesAssessedCount")
    def databases_assessed_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationReadyCount")
    def migration_ready_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DeployedResourcesPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, context: _builtins.str, deployed_resource_id: _builtins.str, deployment_timestamp: _builtins.str, display_name: _builtins.str, id: _builtins.str, is_clean_up_done: _builtins.bool, is_test_migration: _builtins.bool, status: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedResourceId")
    def deployed_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentTimestamp")
    def deployment_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCleanUpDone")
    def is_clean_up_done(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTestMigration")
    def is_test_migration(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DirectoryPathResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, physical: Optional[_builtins.str] = ..., virtual: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def physical(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def virtual(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiscoveredEntityLightSummaryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, number_of_machines: _builtins.int, number_of_servers: _builtins.int, number_of_web_apps: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfServers")
    def number_of_servers(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfWebApps")
    def number_of_web_apps(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class DiskEncryptionSetResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EntityUptimeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, days_per_month: Optional[_builtins.int] = ..., hours_per_day: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysPerMonth")
    def days_per_month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hoursPerDay")
    def hours_per_day(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FacilitySettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, facilities_cost_per_kwh: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="facilitiesCostPerKwh")
    def facilities_cost_per_kwh(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class GmsaAuthenticationPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, configuration_state: _builtins.str, gmsa_cred_spec_name: _builtins.str, gmsa_secret_name: _builtins.str, ad_domain_controller_dns: Optional[_builtins.str] = ..., ad_domain_fqdn: Optional[_builtins.str] = ..., akv_properties: Optional[outputs.KeyVaultSecretStorePropertiesResponse] = ..., domain_admin_password: Optional[_builtins.str] = ..., domain_admin_username: Optional[_builtins.str] = ..., domain_controller_address: Optional[_builtins.str] = ..., gmsa_account_name: Optional[_builtins.str] = ..., gmsa_user_password: Optional[_builtins.str] = ..., gmsa_username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gmsaCredSpecName")
    def gmsa_cred_spec_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gmsaSecretName")
    def gmsa_secret_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adDomainControllerDns")
    def ad_domain_controller_dns(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adDomainFqdn")
    def ad_domain_fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="akvProperties")
    def akv_properties(self) -> Optional[outputs.KeyVaultSecretStorePropertiesResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainAdminPassword")
    def domain_admin_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainAdminUsername")
    def domain_admin_username(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainControllerAddress")
    def domain_controller_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gmsaAccountName")
    def gmsa_account_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gmsaUserPassword")
    def gmsa_user_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gmsaUsername")
    def gmsa_username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, are_assessments_running: _builtins.bool, assessments: Sequence[_builtins.str], created_timestamp: _builtins.str, group_status: _builtins.str, machine_count: _builtins.int, updated_timestamp: _builtins.str, group_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="areAssessmentsRunning")
    def are_assessments_running(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assessments(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupStatus")
    def group_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineCount")
    def machine_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HealthErrorModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, category: _builtins.str, causes: _builtins.str, code: _builtins.str, creation_time: _builtins.str, health_category: _builtins.str, id: _builtins.str, is_customer_resolvable: _builtins.bool, message: _builtins.str, recommendation: _builtins.str, severity: _builtins.str, source: _builtins.str, summary: _builtins.str, affected_resource_correlation_ids: Optional[Sequence[_builtins.str]] = ..., affected_resource_type: Optional[_builtins.str] = ..., child_errors: Optional[Sequence[outputs.InnerHealthErrorModelResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def causes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCategory")
    def health_category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCustomerResolvable")
    def is_customer_resolvable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="affectedResourceCorrelationIds")
    def affected_resource_correlation_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="affectedResourceType")
    def affected_resource_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="childErrors")
    def child_errors(self) -> Optional[Sequence[outputs.InnerHealthErrorModelResponse]]:
        
        ...
    


@pulumi.output_type
class HeterogeneousAssessmentPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_location: _builtins.str, confidence_rating_in_percentage: _builtins.float, last_calculated_on: _builtins.str, provisioning_state: _builtins.str, schema_version: _builtins.str, sizing_criterion: _builtins.str, status: _builtins.str, assessment_arm_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastCalculatedOn")
    def last_calculated_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentArmIds")
    def assessment_arm_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class HypervLicenseResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, license_cost: _builtins.float, license_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseCost")
    def license_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class HypervVirtualizationManagementSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, license_and_support_list: Sequence[outputs.HypervLicenseResponse], number_of_physical_cores_per_license: _builtins.int, software_assurance_cost: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseAndSupportList")
    def license_and_support_list(self) -> Sequence[outputs.HypervLicenseResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfPhysicalCoresPerLicense")
    def number_of_physical_cores_per_license(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceCost")
    def software_assurance_cost(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class IISAKSWorkloadDeploymentModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, iis_aks_workload_deployment_properties: Optional[outputs.IISAKSWorkloadDeploymentResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iisAksWorkloadDeploymentProperties")
    def iis_aks_workload_deployment_properties(self) -> Optional[outputs.IISAKSWorkloadDeploymentResponse]:
        
        ...
    


@pulumi.output_type
class IISAKSWorkloadDeploymentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_history: Sequence[outputs.DeployedResourcesPropertiesResponse], authentication_properties: Optional[outputs.GmsaAuthenticationPropertiesResponse] = ..., automation_artifact_properties: Optional[outputs.AutomationArtifactResponse] = ..., bindings: Optional[Sequence[outputs.BindingResponse]] = ..., build_container_images: Optional[Sequence[outputs.ContainerImagePropertiesResponse]] = ..., cluster_properties: Optional[outputs.AKSDeploymentPropertiesResponse] = ..., configurations: Optional[Sequence[outputs.WebApplicationConfigurationResponse]] = ..., container_image_properties: Optional[outputs.ContainerImagePropertiesResponse] = ..., deployment_name_prefix: Optional[_builtins.str] = ..., deployment_spec: Optional[outputs.AKSDeploymentSpecificationResponse] = ..., directories: Optional[Sequence[outputs.WebApplicationDirectoryResponse]] = ..., limits: Optional[outputs.ResourceRequirementsResponse] = ..., monitoring_properties: Optional[outputs.AppInsightMonitoringPropertiesResponse] = ..., requests: Optional[outputs.ResourceRequirementsResponse] = ..., target_platform_identity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentHistory")
    def deployment_history(self) -> Sequence[outputs.DeployedResourcesPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProperties")
    def authentication_properties(self) -> Optional[outputs.GmsaAuthenticationPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationArtifactProperties")
    def automation_artifact_properties(self) -> Optional[outputs.AutomationArtifactResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bindings(self) -> Optional[Sequence[outputs.BindingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildContainerImages")
    def build_container_images(self) -> Optional[Sequence[outputs.ContainerImagePropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterProperties")
    def cluster_properties(self) -> Optional[outputs.AKSDeploymentPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.WebApplicationConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerImageProperties")
    def container_image_properties(self) -> Optional[outputs.ContainerImagePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentNamePrefix")
    def deployment_name_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentSpec")
    def deployment_spec(self) -> Optional[outputs.AKSDeploymentSpecificationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def directories(self) -> Optional[Sequence[outputs.WebApplicationDirectoryResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[outputs.ResourceRequirementsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringProperties")
    def monitoring_properties(self) -> Optional[outputs.AppInsightMonitoringPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[outputs.ResourceRequirementsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPlatformIdentity")
    def target_platform_identity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IISApplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, application_pool_name: Optional[_builtins.str] = ..., directories: Optional[Sequence[outputs.DirectoryPathResponse]] = ..., enable32_bit_api_on_win64: Optional[_builtins.bool] = ..., managed_pipeline_mode: Optional[_builtins.str] = ..., path: Optional[outputs.DirectoryPathResponse] = ..., runtime_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationPoolName")
    def application_pool_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def directories(self) -> Optional[Sequence[outputs.DirectoryPathResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enable32BitApiOnWin64")
    def enable32_bit_api_on_win64(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPipelineMode")
    def managed_pipeline_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[outputs.DirectoryPathResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IISVirtualApplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, is_virtual_directory: _builtins.bool, directories: Optional[Sequence[outputs.DirectoryPathResponse]] = ..., path: Optional[outputs.DirectoryPathResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isVirtualDirectory")
    def is_virtual_directory(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def directories(self) -> Optional[Sequence[outputs.DirectoryPathResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[outputs.DirectoryPathResponse]:
        
        ...
    


@pulumi.output_type
class IISWebApplicationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_id: Optional[_builtins.str] = ..., application_name: Optional[_builtins.str] = ..., application_scratch_path: Optional[_builtins.str] = ..., applications: Optional[Sequence[outputs.IISApplicationDetailsResponse]] = ..., bindings: Optional[Sequence[outputs.BindingResponse]] = ..., configurations: Optional[Sequence[outputs.WebApplicationConfigurationResponse]] = ..., directories: Optional[Sequence[outputs.WebApplicationDirectoryResponse]] = ..., discovered_frameworks: Optional[Sequence[outputs.WebApplicationFrameworkResponse]] = ..., display_name: Optional[_builtins.str] = ..., iis_web_server: Optional[outputs.IISWebServerResponse] = ..., limits: Optional[outputs.ResourceRequirementsResponse] = ..., path: Optional[outputs.DirectoryPathResponse] = ..., primary_framework: Optional[outputs.WebApplicationFrameworkResponse] = ..., requests: Optional[outputs.ResourceRequirementsResponse] = ..., virtual_applications: Optional[Sequence[outputs.IISVirtualApplicationDetailsResponse]] = ..., web_server_id: Optional[_builtins.str] = ..., web_server_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationScratchPath")
    def application_scratch_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def applications(self) -> Optional[Sequence[outputs.IISApplicationDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bindings(self) -> Optional[Sequence[outputs.BindingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.WebApplicationConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def directories(self) -> Optional[Sequence[outputs.WebApplicationDirectoryResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredFrameworks")
    def discovered_frameworks(self) -> Optional[Sequence[outputs.WebApplicationFrameworkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iisWebServer")
    def iis_web_server(self) -> Optional[outputs.IISWebServerResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[outputs.ResourceRequirementsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[outputs.DirectoryPathResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFramework")
    def primary_framework(self) -> Optional[outputs.WebApplicationFrameworkResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[outputs.ResourceRequirementsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualApplications")
    def virtual_applications(self) -> Optional[Sequence[outputs.IISVirtualApplicationDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerId")
    def web_server_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerName")
    def web_server_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IISWebServerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., ip_addresses: Optional[Sequence[_builtins.str]] = ..., machines: Optional[Sequence[_builtins.str]] = ..., operating_system_details: Optional[outputs.OperatingSystemDetailsResponse] = ..., root_configuration_location: Optional[_builtins.str] = ..., run_as_account_id: Optional[_builtins.str] = ..., server_fqdn: Optional[_builtins.str] = ..., server_id: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ..., web_applications: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def machines(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystemDetails")
    def operating_system_details(self) -> Optional[outputs.OperatingSystemDetailsResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootConfigurationLocation")
    def root_configuration_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverFqdn")
    def server_fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webApplications")
    def web_applications(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class IISWorkloadInstanceModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, container_name: Optional[_builtins.str] = ..., fileshare_name: Optional[_builtins.str] = ..., iis_web_application: Optional[outputs.IISWebApplicationResponse] = ..., web_app_arm_id: Optional[_builtins.str] = ..., web_app_site_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileshareName")
    def fileshare_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iisWebApplication")
    def iis_web_application(self) -> Optional[outputs.IISWebApplicationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppArmId")
    def web_app_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppSiteName")
    def web_app_site_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentityModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aad_authority: Optional[_builtins.str] = ..., application_id: Optional[_builtins.str] = ..., audience: Optional[_builtins.str] = ..., object_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadAuthority")
    def aad_authority(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ImportCollectorPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_timestamp: _builtins.str, updated_timestamp: _builtins.str, discovery_site_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ImportSqlCollectorPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_timestamp: _builtins.str, provisioning_state: _builtins.str, updated_timestamp: _builtins.str, discovery_site_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InnerHealthErrorModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, category: _builtins.str, causes: _builtins.str, code: _builtins.str, creation_time: _builtins.str, health_category: _builtins.str, id: _builtins.str, is_customer_resolvable: _builtins.bool, message: _builtins.str, recommendation: _builtins.str, severity: _builtins.str, source: _builtins.str, summary: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def causes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCategory")
    def health_category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCustomerResolvable")
    def is_customer_resolvable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class JobStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, job_name: _builtins.str, job_progress: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobProgress")
    def job_progress(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class KeyVaultResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KeyVaultSecretStorePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, input_type: _builtins.str, keyvault_name: Optional[_builtins.str] = ..., managed_identity_properties: Optional[outputs.ManagedIdentityPropertiesResponse] = ..., resource_group: Optional[_builtins.str] = ..., secret_store_id: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputType")
    def input_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyvaultName")
    def keyvault_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityProperties")
    def managed_identity_properties(self) -> Optional[outputs.ManagedIdentityPropertiesResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStoreId")
    def secret_store_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class LBBackendAddressPoolResourceSettingsResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LBFrontendIPConfigurationResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., private_ip_address: Optional[_builtins.str] = ..., private_ip_allocation_method: Optional[_builtins.str] = ..., subnet: Optional[outputs.SubnetReferenceResponse] = ..., zones: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAllocationMethod")
    def private_ip_allocation_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[outputs.SubnetReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaborSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hourly_admin_cost: _builtins.float, physical_servers_per_admin: _builtins.int, virtual_machines_per_admin: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourlyAdminCost")
    def hourly_admin_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalServersPerAdmin")
    def physical_servers_per_admin(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachinesPerAdmin")
    def virtual_machines_per_admin(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class LinuxServerLicensingSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, license_cost: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseCost")
    def license_cost(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class LoadBalancerBackendAddressPoolReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_arm_resource_id: _builtins.str, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArmResourceId")
    def source_arm_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LoadBalancerNatRuleReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_arm_resource_id: _builtins.str, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArmResourceId")
    def source_arm_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LoadBalancerResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, backend_address_pools: Optional[Sequence[outputs.LBBackendAddressPoolResourceSettingsResponse]] = ..., frontend_ip_configurations: Optional[Sequence[outputs.LBFrontendIPConfigurationResourceSettingsResponse]] = ..., sku: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ..., zones: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(self) -> Optional[Sequence[outputs.LBBackendAddressPoolResourceSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(self) -> Optional[Sequence[outputs.LBFrontendIPConfigurationResourceSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MachineAssessmentSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_disk_types: Optional[Sequence[_builtins.str]] = ..., azure_hybrid_use_benefit: Optional[_builtins.str] = ..., azure_location: Optional[_builtins.str] = ..., azure_pricing_tier: Optional[_builtins.str] = ..., azure_security_offering_type: Optional[_builtins.str] = ..., azure_storage_redundancy: Optional[_builtins.str] = ..., azure_vm_families: Optional[Sequence[_builtins.str]] = ..., azure_vm_security_options: Optional[Sequence[_builtins.str]] = ..., billing_settings: Optional[outputs.BillingSettingsResponse] = ..., currency: Optional[_builtins.str] = ..., discount_percentage: Optional[_builtins.float] = ..., environment_type: Optional[_builtins.str] = ..., linux_azure_hybrid_use_benefit: Optional[_builtins.str] = ..., performance_data: Optional[outputs.PerformanceDataResponse] = ..., savings_settings: Optional[outputs.SavingsSettingsResponse] = ..., scaling_factor: Optional[_builtins.float] = ..., sizing_criterion: Optional[_builtins.str] = ..., vm_uptime: Optional[outputs.VmUptimeResponseV2] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDiskTypes")
    def azure_disk_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureHybridUseBenefit")
    def azure_hybrid_use_benefit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azurePricingTier")
    def azure_pricing_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSecurityOfferingType")
    def azure_security_offering_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureStorageRedundancy")
    def azure_storage_redundancy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVmFamilies")
    def azure_vm_families(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVmSecurityOptions")
    def azure_vm_security_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingSettings")
    def billing_settings(self) -> Optional[outputs.BillingSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxAzureHybridUseBenefit")
    def linux_azure_hybrid_use_benefit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> Optional[outputs.PerformanceDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsSettings")
    def savings_settings(self) -> Optional[outputs.SavingsSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmUptime")
    def vm_uptime(self) -> Optional[outputs.VmUptimeResponseV2]:
        
        ...
    


@pulumi.output_type
class MachineAssessmentV2PropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, details: Optional[outputs.AssessmentDetailsResponse] = ..., scope: Optional[outputs.ScopeResponse] = ..., settings: Optional[outputs.MachineAssessmentSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[outputs.AssessmentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.ScopeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.MachineAssessmentSettingsResponse]:
        
        ...
    


@pulumi.output_type
class ManagedIdentityPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., managed_identity_name: Optional[_builtins.str] = ..., principal_id: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityName")
    def managed_identity_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ManagementSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hyperv_virtualization_management_settings: outputs.HypervVirtualizationManagementSettingsResponse, other_management_costs_settings: outputs.OtherManagementCostsSettingsResponse, third_party_management_settings: outputs.ThirdPartyManagementSettingsResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hypervVirtualizationManagementSettings")
    def hyperv_virtualization_management_settings(self) -> outputs.HypervVirtualizationManagementSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="otherManagementCostsSettings")
    def other_management_costs_settings(self) -> outputs.OtherManagementCostsSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thirdPartyManagementSettings")
    def third_party_management_settings(self) -> outputs.ThirdPartyManagementSettingsResponse:
        
        ...
    


@pulumi.output_type
class ManualResolutionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateAgentModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, correlation_id: _builtins.str, health_errors: Sequence[outputs.HealthErrorModelResponse], is_responsive: _builtins.bool, last_heartbeat: _builtins.str, provisioning_state: _builtins.str, version_number: _builtins.str, authentication_identity: Optional[outputs.IdentityModelResponse] = ..., custom_properties: Optional[outputs.VMwareMigrateAgentModelCustomPropertiesResponse] = ..., machine_id: Optional[_builtins.str] = ..., machine_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isResponsive")
    def is_responsive(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeat")
    def last_heartbeat(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionNumber")
    def version_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationIdentity")
    def authentication_identity(self) -> Optional[outputs.IdentityModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[outputs.VMwareMigrateAgentModelCustomPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateAgentModelResponseSystemData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateProjectPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_summary_refreshed_time: _builtins.str, refresh_summary_state: _builtins.str, summary: Mapping[str, Any], provisioning_state: Optional[_builtins.str] = ..., registered_tools: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSummaryRefreshedTime")
    def last_summary_refreshed_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshSummaryState")
    def refresh_summary_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> Mapping[str, Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registeredTools")
    def registered_tools(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class MigrateProjectPropertiesResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_summary_refreshed_time: _builtins.str, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionResponseV1], refresh_summary_state: _builtins.str, registered_tools: Sequence[_builtins.str], summary: Mapping[str, outputs.ProjectSummaryResponse], public_network_access: Optional[_builtins.str] = ..., service_endpoint: Optional[_builtins.str] = ..., utility_storage_account_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSummaryRefreshedTime")
    def last_summary_refreshed_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponseV1]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshSummaryState")
    def refresh_summary_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registeredTools")
    def registered_tools(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> Mapping[str, outputs.ProjectSummaryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="utilityStorageAccountId")
    def utility_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateProjectResponseTags(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_properties: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class MigrationConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_vault_resource_id: Optional[_builtins.str] = ..., migration_solution_resource_id: Optional[_builtins.str] = ..., storage_account_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceId")
    def key_vault_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSolutionResourceId")
    def migration_solution_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrationEntityGroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_display_name: _builtins.str, application_id: _builtins.str, execution_start_date: _builtins.str, execution_status: _builtins.str, provisioning_state: _builtins.str, associated_assessment_id: Optional[_builtins.str] = ..., associated_wave_ids: Optional[Sequence[_builtins.str]] = ..., migration_path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationDisplayName")
    def application_display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionStartDate")
    def execution_start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionStatus")
    def execution_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedAssessmentId")
    def associated_assessment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedWaveIds")
    def associated_wave_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationPath")
    def migration_path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrationEntityPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, associated_inventory_resource_id: _builtins.str, execution_readiness: _builtins.str, execution_stage: _builtins.str, execution_start_date: _builtins.str, execution_status: _builtins.str, inventory_display_name: _builtins.str, migration_strategy: _builtins.str, provisioning_state: _builtins.str, assessed_entity_arm_id: Optional[_builtins.str] = ..., associated_assessment_id: Optional[_builtins.str] = ..., associated_migration_entity_group_ids: Optional[Sequence[_builtins.str]] = ..., associated_wave_id: Optional[_builtins.str] = ..., migration_path: Optional[_builtins.str] = ..., migration_specific_properties: Optional[outputs.ServerMigrationSpecificPropertiesResponse] = ..., migration_tool: Optional[_builtins.str] = ..., partner_resource_arm_id: Optional[_builtins.str] = ..., target: Optional[_builtins.str] = ..., target_azure_resource_arm_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedInventoryResourceId")
    def associated_inventory_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReadiness")
    def execution_readiness(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionStage")
    def execution_stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionStartDate")
    def execution_start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionStatus")
    def execution_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inventoryDisplayName")
    def inventory_display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStrategy")
    def migration_strategy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessedEntityArmId")
    def assessed_entity_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedAssessmentId")
    def associated_assessment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedMigrationEntityGroupIds")
    def associated_migration_entity_group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedWaveId")
    def associated_wave_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationPath")
    def migration_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSpecificProperties")
    def migration_specific_properties(self) -> Optional[outputs.ServerMigrationSpecificPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationTool")
    def migration_tool(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerResourceArmId")
    def partner_resource_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAzureResourceArmId")
    def target_azure_resource_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ModernizeProjectModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, service_endpoint: _builtins.str, service_resource_id: _builtins.str, migration_configuration: Optional[outputs.MigrationConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceResourceId")
    def service_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationConfiguration")
    def migration_configuration(self) -> Optional[outputs.MigrationConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class ModernizeProjectModelResponseSystemData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MoveCollectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, errors: outputs.MoveCollectionPropertiesResponseErrors, provisioning_state: _builtins.str, move_region: Optional[_builtins.str] = ..., move_type: Optional[_builtins.str] = ..., source_region: Optional[_builtins.str] = ..., target_region: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.MoveCollectionPropertiesResponseErrors:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moveRegion")
    def move_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moveType")
    def move_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRegion")
    def source_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRegion")
    def target_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MoveCollectionPropertiesResponseErrors(dict):
    
    def __init__(__self__, *, properties: Optional[outputs.MoveResourceErrorBodyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.MoveResourceErrorBodyResponse]:
        
        ...
    


@pulumi.output_type
class MoveResourceDependencyOverrideResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., target_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MoveResourceDependencyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatic_resolution: Optional[outputs.AutomaticResolutionPropertiesResponse] = ..., dependency_type: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., is_optional: Optional[_builtins.str] = ..., manual_resolution: Optional[outputs.ManualResolutionPropertiesResponse] = ..., resolution_status: Optional[_builtins.str] = ..., resolution_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticResolution")
    def automatic_resolution(self) -> Optional[outputs.AutomaticResolutionPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependencyType")
    def dependency_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOptional")
    def is_optional(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualResolution")
    def manual_resolution(self) -> Optional[outputs.ManualResolutionPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolutionStatus")
    def resolution_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolutionType")
    def resolution_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MoveResourceErrorBodyResponse(dict):
    
    def __init__(__self__, *, code: _builtins.str, details: Sequence[outputs.MoveResourceErrorBodyResponse], message: _builtins.str, target: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.MoveResourceErrorBodyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MoveResourceErrorResponse(dict):
    
    def __init__(__self__, *, properties: Optional[outputs.MoveResourceErrorBodyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.MoveResourceErrorBodyResponse]:
        
        ...
    


@pulumi.output_type
class MoveResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, depends_on: Sequence[outputs.MoveResourceDependencyResponse], errors: outputs.MoveResourcePropertiesResponseErrors, is_resolve_required: _builtins.bool, move_status: outputs.MoveResourcePropertiesResponseMoveStatus, provisioning_state: _builtins.str, source_id: _builtins.str, source_resource_settings: Any, target_id: _builtins.str, depends_on_overrides: Optional[Sequence[outputs.MoveResourceDependencyOverrideResponse]] = ..., existing_target_id: Optional[_builtins.str] = ..., resource_settings: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Sequence[outputs.MoveResourceDependencyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.MoveResourcePropertiesResponseErrors:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isResolveRequired")
    def is_resolve_required(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moveStatus")
    def move_status(self) -> outputs.MoveResourcePropertiesResponseMoveStatus:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceSettings")
    def source_resource_settings(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOnOverrides")
    def depends_on_overrides(self) -> Optional[Sequence[outputs.MoveResourceDependencyOverrideResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingTargetId")
    def existing_target_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSettings")
    def resource_settings(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class MoveResourcePropertiesResponseErrors(dict):
    
    def __init__(__self__, *, properties: Optional[outputs.MoveResourceErrorBodyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.MoveResourceErrorBodyResponse]:
        
        ...
    


@pulumi.output_type
class MoveResourcePropertiesResponseMoveStatus(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, move_state: _builtins.str, errors: Optional[outputs.MoveResourceErrorResponse] = ..., job_status: Optional[outputs.JobStatusResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moveState")
    def move_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[outputs.MoveResourceErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobStatus")
    def job_status(self) -> Optional[outputs.JobStatusResponse]:
        
        ...
    


@pulumi.output_type
class NetworkInterfaceResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, enable_accelerated_networking: Optional[_builtins.bool] = ..., ip_configurations: Optional[Sequence[outputs.NicIpConfigurationResourceSettingsResponse]] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[Sequence[outputs.NicIpConfigurationResourceSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkSecurityGroupResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, security_rules: Optional[Sequence[outputs.NsgSecurityRuleResponse]] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityRules")
    def security_rules(self) -> Optional[Sequence[outputs.NsgSecurityRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hardware_software_cost_percentage: _builtins.float, maintenance_cost_percentage: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareSoftwareCostPercentage")
    def hardware_software_cost_percentage(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceCostPercentage")
    def maintenance_cost_percentage(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class NicIpConfigurationResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, load_balancer_backend_address_pools: Optional[Sequence[outputs.LoadBalancerBackendAddressPoolReferenceResponse]] = ..., load_balancer_nat_rules: Optional[Sequence[outputs.LoadBalancerNatRuleReferenceResponse]] = ..., name: Optional[_builtins.str] = ..., primary: Optional[_builtins.bool] = ..., private_ip_address: Optional[_builtins.str] = ..., private_ip_allocation_method: Optional[_builtins.str] = ..., public_ip: Optional[outputs.PublicIpReferenceResponse] = ..., subnet: Optional[outputs.SubnetReferenceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPools")
    def load_balancer_backend_address_pools(self) -> Optional[Sequence[outputs.LoadBalancerBackendAddressPoolReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerNatRules")
    def load_balancer_nat_rules(self) -> Optional[Sequence[outputs.LoadBalancerNatRuleReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAllocationMethod")
    def private_ip_allocation_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[outputs.PublicIpReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[outputs.SubnetReferenceResponse]:
        
        ...
    


@pulumi.output_type
class NsgReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_arm_resource_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArmResourceId")
    def source_arm_resource_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class NsgSecurityRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., destination_address_prefix: Optional[_builtins.str] = ..., destination_port_range: Optional[_builtins.str] = ..., direction: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., priority: Optional[_builtins.int] = ..., protocol: Optional[_builtins.str] = ..., source_address_prefix: Optional[_builtins.str] = ..., source_port_range: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddressPrefix")
    def destination_address_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefix")
    def source_address_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OnPremiseSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compute_settings: outputs.ComputeSettingsResponse, facility_settings: outputs.FacilitySettingsResponse, labor_settings: outputs.LaborSettingsResponse, network_settings: outputs.NetworkSettingsResponse, security_settings: outputs.SecuritySettingsResponse, storage_settings: outputs.StorageSettingsResponse, management_settings: Optional[outputs.ManagementSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeSettings")
    def compute_settings(self) -> outputs.ComputeSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="facilitySettings")
    def facility_settings(self) -> outputs.FacilitySettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="laborSettings")
    def labor_settings(self) -> outputs.LaborSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> outputs.NetworkSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> outputs.SecuritySettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSettings")
    def storage_settings(self) -> outputs.StorageSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementSettings")
    def management_settings(self) -> Optional[outputs.ManagementSettingsResponse]:
        
        ...
    


@pulumi.output_type
class OperatingSystemDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, os: Optional[_builtins.str] = ..., os_architecture: Optional[_builtins.str] = ..., os_name: Optional[_builtins.str] = ..., os_version: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def os(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osArchitecture")
    def os_architecture(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class OtherManagementCostsSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_protection_cost_per_server_per_year: _builtins.float, monitoring_cost_per_server_per_year: _builtins.float, patching_cost_per_server_per_year: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProtectionCostPerServerPerYear")
    def data_protection_cost_per_server_per_year(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringCostPerServerPerYear")
    def monitoring_cost_per_server_per_year(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchingCostPerServerPerYear")
    def patching_cost_per_server_per_year(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class PerfDataSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, percentile: _builtins.str, time_range: _builtins.str, perf_data_end_time: Optional[_builtins.str] = ..., perf_data_start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percentile(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perfDataEndTime")
    def perf_data_end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perfDataStartTime")
    def perf_data_start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PerformanceDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, percentile: Optional[_builtins.str] = ..., perf_data_end_time: Optional[_builtins.str] = ..., perf_data_start_time: Optional[_builtins.str] = ..., time_range: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percentile(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perfDataEndTime")
    def perf_data_end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perfDataStartTime")
    def perf_data_start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PortMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_port: Optional[_builtins.int] = ..., internal_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalPort")
    def external_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalPort")
    def internal_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, private_endpoint: outputs.ResourceIdResponse, provisioning_state: _builtins.str, private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStateResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> outputs.ResourceIdResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_ids: Sequence[_builtins.str], id: _builtins.str, name: _builtins.str, private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> outputs.PrivateLinkServiceConnectionStateResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, e_tag: _builtins.str, id: _builtins.str, name: _builtins.str, properties: outputs.PrivateEndpointConnectionPropertiesResponse, system_data: outputs.SystemDataResponse, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.PrivateEndpointConnectionPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponseV2(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, properties: outputs.PrivateEndpointConnectionPropertiesResponse, type: _builtins.str, e_tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.PrivateEndpointConnectionPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProjectPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_timestamp: _builtins.str, last_assessment_timestamp: _builtins.str, number_of_assessments: _builtins.int, number_of_groups: _builtins.int, number_of_machines: _builtins.int, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionResponseV2], provisioning_state: _builtins.str, service_endpoint: _builtins.str, updated_timestamp: _builtins.str, assessment_solution_id: Optional[_builtins.str] = ..., customer_storage_account_arm_id: Optional[_builtins.str] = ..., customer_workspace_id: Optional[_builtins.str] = ..., customer_workspace_location: Optional[_builtins.str] = ..., project_status: Optional[_builtins.str] = ..., public_network_access: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAssessmentTimestamp")
    def last_assessment_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfAssessments")
    def number_of_assessments(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfGroups")
    def number_of_groups(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponseV2]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentSolutionId")
    def assessment_solution_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerStorageAccountArmId")
    def customer_storage_account_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerWorkspaceId")
    def customer_workspace_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerWorkspaceLocation")
    def customer_workspace_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectStatus")
    def project_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProjectSummaryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, extended_summary: Optional[Mapping[str, _builtins.str]] = ..., last_summary_refreshed_time: Optional[_builtins.str] = ..., refresh_summary_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedSummary")
    def extended_summary(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSummaryRefreshedTime")
    def last_summary_refreshed_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshSummaryState")
    def refresh_summary_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PublicIPAddressResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, domain_name_label: Optional[_builtins.str] = ..., fqdn: Optional[_builtins.str] = ..., public_ip_allocation_method: Optional[_builtins.str] = ..., sku: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ..., zones: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNameLabel")
    def domain_name_label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAllocationMethod")
    def public_ip_allocation_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PublicIpReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_arm_resource_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArmResourceId")
    def source_arm_resource_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ReportDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, report_status: _builtins.str, report_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportStatus")
    def report_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportType")
    def report_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ResourceGroupResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceIdResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class ResourceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponse]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]:
        ...
    


@pulumi.output_type
class ResourceRequirementsResponse(dict):
    
    def __init__(__self__, *, cpu: Optional[_builtins.str] = ..., memory: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SavingsSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_offer_code: Optional[_builtins.str] = ..., savings_options: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsOptions")
    def savings_options(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScopeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_resource_graph_query: Optional[_builtins.str] = ..., scope_type: Optional[_builtins.str] = ..., server_group_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureResourceGraphQuery")
    def azure_resource_graph_query(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeType")
    def scope_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverGroupId")
    def server_group_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecretStoreDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret_store: Optional[_builtins.str] = ..., secret_store_properties: Optional[outputs.SecretStorePropertiesResponse] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStoreProperties")
    def secret_store_properties(self) -> Optional[outputs.SecretStorePropertiesResponse]:
        ...
    


@pulumi.output_type
class SecretStorePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, input_type: _builtins.str, secret_store_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputType")
    def input_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStoreId")
    def secret_store_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class SecuritySettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, server_security_cost_per_server_per_year: _builtins.float, sql_server_security_cost_per_server_per_year: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSecurityCostPerServerPerYear")
    def server_security_cost_per_server_per_year(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerSecurityCostPerServerPerYear")
    def sql_server_security_cost_per_server_per_year(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class ServerMigrationSpecificPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, current_job_id: Optional[_builtins.str] = ..., dr_appliance_inventory_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentJobId")
    def current_job_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="drApplianceInventoryId")
    def dr_appliance_inventory_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServersProjectSummaryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, assessed_count: Optional[_builtins.int] = ..., discovered_count: Optional[_builtins.int] = ..., extended_summary: Optional[Mapping[str, _builtins.str]] = ..., last_summary_refreshed_time: Optional[_builtins.str] = ..., migrated_count: Optional[_builtins.int] = ..., refresh_summary_state: Optional[_builtins.str] = ..., replicating_count: Optional[_builtins.int] = ..., test_migrated_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessedCount")
    def assessed_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredCount")
    def discovered_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedSummary")
    def extended_summary(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSummaryRefreshedTime")
    def last_summary_refreshed_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migratedCount")
    def migrated_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshSummaryState")
    def refresh_summary_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicatingCount")
    def replicating_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testMigratedCount")
    def test_migrated_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServersSolutionSummaryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, assessed_count: Optional[_builtins.int] = ..., discovered_count: Optional[_builtins.int] = ..., migrated_count: Optional[_builtins.int] = ..., replicating_count: Optional[_builtins.int] = ..., test_migrated_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessedCount")
    def assessed_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredCount")
    def discovered_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migratedCount")
    def migrated_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicatingCount")
    def replicating_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testMigratedCount")
    def test_migrated_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_settings: outputs.AzureSettingsResponse, azure_arc_settings: Optional[outputs.AzureArcSettingsResponse] = ..., on_premise_settings: Optional[outputs.OnPremiseSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSettings")
    def azure_settings(self) -> outputs.AzureSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureArcSettings")
    def azure_arc_settings(self) -> Optional[outputs.AzureArcSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremiseSettings")
    def on_premise_settings(self) -> Optional[outputs.OnPremiseSettingsResponse]:
        
        ...
    


@pulumi.output_type
class SolutionDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assessment_count: Optional[_builtins.int] = ..., extended_details: Optional[Mapping[str, _builtins.str]] = ..., group_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentCount")
    def assessment_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedDetails")
    def extended_details(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupCount")
    def group_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SolutionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cleanup_state: Optional[_builtins.str] = ..., details: Optional[outputs.SolutionDetailsResponse] = ..., goal: Optional[_builtins.str] = ..., purpose: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., summary: Optional[Any] = ..., tool: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanupState")
    def cleanup_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[outputs.SolutionDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def goal(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlAssessmentSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, async_commit_mode_intent: Optional[_builtins.str] = ..., azure_location: Optional[_builtins.str] = ..., azure_security_offering_type: Optional[_builtins.str] = ..., azure_sql_database_settings: Optional[outputs.SqlDbSettingsV3Response] = ..., azure_sql_managed_instance_settings: Optional[outputs.SqlMiSettingsV3Response] = ..., azure_sql_vm_settings: Optional[outputs.SqlVmSettingsResponse] = ..., billing_settings: Optional[outputs.BillingSettingsResponse] = ..., currency: Optional[_builtins.str] = ..., disaster_recovery_location: Optional[_builtins.str] = ..., discount_percentage: Optional[_builtins.float] = ..., enable_hadr_assessment: Optional[_builtins.bool] = ..., entity_uptime: Optional[outputs.EntityUptimeResponse] = ..., environment_type: Optional[_builtins.str] = ..., is_internet_access_available: Optional[_builtins.bool] = ..., multi_subnet_intent: Optional[_builtins.str] = ..., os_license: Optional[_builtins.str] = ..., performance_data: Optional[outputs.PerformanceDataResponse] = ..., preferred_targets: Optional[Sequence[_builtins.str]] = ..., savings_settings: Optional[outputs.SavingsSettingsResponse] = ..., scaling_factor: Optional[_builtins.float] = ..., sizing_criterion: Optional[_builtins.str] = ..., sql_server_license: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncCommitModeIntent")
    def async_commit_mode_intent(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSecurityOfferingType")
    def azure_security_offering_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlDatabaseSettings")
    def azure_sql_database_settings(self) -> Optional[outputs.SqlDbSettingsV3Response]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlManagedInstanceSettings")
    def azure_sql_managed_instance_settings(self) -> Optional[outputs.SqlMiSettingsV3Response]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlVmSettings")
    def azure_sql_vm_settings(self) -> Optional[outputs.SqlVmSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingSettings")
    def billing_settings(self) -> Optional[outputs.BillingSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disasterRecoveryLocation")
    def disaster_recovery_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHadrAssessment")
    def enable_hadr_assessment(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityUptime")
    def entity_uptime(self) -> Optional[outputs.EntityUptimeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isInternetAccessAvailable")
    def is_internet_access_available(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiSubnetIntent")
    def multi_subnet_intent(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osLicense")
    def os_license(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> Optional[outputs.PerformanceDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredTargets")
    def preferred_targets(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsSettings")
    def savings_settings(self) -> Optional[outputs.SavingsSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerLicense")
    def sql_server_license(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlAssessmentV3PropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, details: Optional[outputs.AssessmentDetailsResponse] = ..., fallback_machine_assessment_arm_id: Optional[_builtins.str] = ..., scope: Optional[outputs.ScopeResponse] = ..., settings: Optional[outputs.SqlAssessmentSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[outputs.AssessmentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackMachineAssessmentArmId")
    def fallback_machine_assessment_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.ScopeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.SqlAssessmentSettingsResponse]:
        
        ...
    


@pulumi.output_type
class SqlDatabaseResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, tags: Optional[Mapping[str, _builtins.str]] = ..., target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ..., zone_redundant: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlDbSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_sql_compute_tier: Optional[_builtins.str] = ..., azure_sql_data_base_type: Optional[_builtins.str] = ..., azure_sql_purchase_model: Optional[_builtins.str] = ..., azure_sql_service_tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlComputeTier")
    def azure_sql_compute_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlDataBaseType")
    def azure_sql_data_base_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlPurchaseModel")
    def azure_sql_purchase_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlServiceTier")
    def azure_sql_service_tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlDbSettingsV3Response(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_sql_compute_tier: Optional[_builtins.str] = ..., azure_sql_data_base_type: Optional[_builtins.str] = ..., azure_sql_purchase_model: Optional[_builtins.str] = ..., azure_sql_service_tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlComputeTier")
    def azure_sql_compute_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlDataBaseType")
    def azure_sql_data_base_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlPurchaseModel")
    def azure_sql_purchase_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlServiceTier")
    def azure_sql_service_tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlElasticPoolResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, tags: Optional[Mapping[str, _builtins.str]] = ..., target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ..., zone_redundant: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlMiSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_sql_instance_type: Optional[_builtins.str] = ..., azure_sql_service_tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlInstanceType")
    def azure_sql_instance_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlServiceTier")
    def azure_sql_service_tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlMiSettingsV3Response(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_sql_instance_type: Optional[_builtins.str] = ..., azure_sql_service_tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlInstanceType")
    def azure_sql_instance_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlServiceTier")
    def azure_sql_service_tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlServerLicensingSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, license_cost: _builtins.float, software_assurance_cost: _builtins.float, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseCost")
    def license_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceCost")
    def software_assurance_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SqlServerResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlVmSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_series: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSeries")
    def instance_series(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class StorageSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cost_per_gb_per_month: _builtins.float, maintainance_cost_percentage_to_acquisition_cost: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costPerGbPerMonth")
    def cost_per_gb_per_month(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintainanceCostPercentageToAcquisitionCost")
    def maintainance_cost_percentage_to_acquisition_cost(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class SubnetReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_arm_resource_id: _builtins.str, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArmResourceId")
    def source_arm_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SubnetResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_prefix: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., network_security_group: Optional[outputs.NsgReferenceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[outputs.NsgReferenceResponse]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TargetAssessmentArmIdsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aks: Optional[_builtins.str] = ..., azure_app_service: Optional[_builtins.str] = ..., azure_app_service_container: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aks(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureAppService")
    def azure_app_service(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureAppServiceContainer")
    def azure_app_service_container(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TargetStorageProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_file_share_profile: Optional[outputs.AzureFileShareHydrationProfileResponse] = ..., hydration_storage_provider_type: Optional[_builtins.str] = ..., persistent_volume_id: Optional[_builtins.str] = ..., storage_access_type: Optional[_builtins.str] = ..., storage_projection_type: Optional[_builtins.str] = ..., target_name: Optional[_builtins.str] = ..., target_size: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFileShareProfile")
    def azure_file_share_profile(self) -> Optional[outputs.AzureFileShareHydrationProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hydrationStorageProviderType")
    def hydration_storage_provider_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistentVolumeId")
    def persistent_volume_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccessType")
    def storage_access_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProjectionType")
    def storage_projection_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSize")
    def target_size(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, completion_date: _builtins.str, display_name: _builtins.str, is_editable: _builtins.bool, provisioning_state: _builtins.str, scope: _builtins.str, scope_id: _builtins.str, status: _builtins.str, task_type: _builtins.str, description: Optional[_builtins.str] = ..., stage: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="completionDate")
    def completion_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEditable")
    def is_editable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ThirdPartyManagementSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, license_cost: _builtins.float, support_cost: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseCost")
    def license_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportCost")
    def support_cost(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., principal_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class VMwareMigrateAgentModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, fabric_friendly_name: Optional[_builtins.str] = ..., vmware_site_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricFriendlyName")
    def fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareSiteId")
    def vmware_site_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualMachineResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, tags: Optional[Mapping[str, _builtins.str]] = ..., target_availability_set_id: Optional[_builtins.str] = ..., target_availability_zone: Optional[_builtins.str] = ..., target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ..., target_vm_size: Optional[_builtins.str] = ..., user_managed_identities: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAvailabilitySetId")
    def target_availability_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAvailabilityZone")
    def target_availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmSize")
    def target_vm_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManagedIdentities")
    def user_managed_identities(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VirtualNetworkResourceSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, address_space: Optional[Sequence[_builtins.str]] = ..., dns_servers: Optional[Sequence[_builtins.str]] = ..., enable_ddos_protection: Optional[_builtins.bool] = ..., subnets: Optional[Sequence[outputs.SubnetResourceSettingsResponse]] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., target_resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDdosProtection")
    def enable_ddos_protection(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[outputs.SubnetResourceSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualizationSoftwareSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, v_mware_cloud_foundation_license_cost: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vMwareCloudFoundationLicenseCost")
    def v_mware_cloud_foundation_license_cost(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class VmUptimeResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, days_per_month: Optional[_builtins.float] = ..., hours_per_day: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysPerMonth")
    def days_per_month(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hoursPerDay")
    def hours_per_day(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class VmUptimeResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, days_per_month: Optional[_builtins.int] = ..., hours_per_day: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysPerMonth")
    def days_per_month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hoursPerDay")
    def hours_per_day(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VmUptimeResponseV2(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, days_per_month: Optional[_builtins.int] = ..., hours_per_day: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysPerMonth")
    def days_per_month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hoursPerDay")
    def hours_per_day(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WavePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actual_start_date: _builtins.str, arg: outputs.ArgResponse, display_name: _builtins.str, planned_start_date: _builtins.str, provisioning_state: _builtins.str, stage: _builtins.str, status: _builtins.str, description: Optional[_builtins.str] = ..., planned_completion_date: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actualStartDate")
    def actual_start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arg(self) -> outputs.ArgResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plannedStartDate")
    def planned_start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plannedCompletionDate")
    def planned_completion_date(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAppAssessmentSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_svc_container_settings: outputs.AppSvcContainerSettingsResponse, app_svc_native_settings: outputs.AppSvcNativeSettingsResponse, azure_security_offering_type: _builtins.str, azure_location: Optional[_builtins.str] = ..., billing_settings: Optional[outputs.BillingSettingsResponse] = ..., currency: Optional[_builtins.str] = ..., discount_percentage: Optional[_builtins.float] = ..., environment_type: Optional[_builtins.str] = ..., performance_data: Optional[outputs.PerformanceDataResponse] = ..., savings_settings: Optional[outputs.SavingsSettingsResponse] = ..., scaling_factor: Optional[_builtins.float] = ..., sizing_criterion: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSvcContainerSettings")
    def app_svc_container_settings(self) -> outputs.AppSvcContainerSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSvcNativeSettings")
    def app_svc_native_settings(self) -> outputs.AppSvcNativeSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSecurityOfferingType")
    def azure_security_offering_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingSettings")
    def billing_settings(self) -> Optional[outputs.BillingSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> Optional[outputs.PerformanceDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsSettings")
    def savings_settings(self) -> Optional[outputs.SavingsSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAppAssessmentV3PropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, details: Optional[outputs.AssessmentDetailsResponse] = ..., fallback_machine_assessment_arm_id: Optional[_builtins.str] = ..., scope: Optional[outputs.ScopeResponse] = ..., settings: Optional[outputs.WebAppAssessmentSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[outputs.AssessmentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackMachineAssessmentArmId")
    def fallback_machine_assessment_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.ScopeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.WebAppAssessmentSettingsResponse]:
        
        ...
    


@pulumi.output_type
class WebApplicationConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, file_path: Optional[_builtins.str] = ..., identifier: Optional[_builtins.str] = ..., is_deployment_time_editable: Optional[_builtins.bool] = ..., local_file_path: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., secret_store_details: Optional[outputs.SecretStoreDetailsResponse] = ..., section: Optional[_builtins.str] = ..., target_file_path: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeploymentTimeEditable")
    def is_deployment_time_editable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localFilePath")
    def local_file_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStoreDetails")
    def secret_store_details(self) -> Optional[outputs.SecretStoreDetailsResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def section(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFilePath")
    def target_file_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebApplicationDirectoryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, is_editable: Optional[_builtins.bool] = ..., source_paths: Optional[Sequence[_builtins.str]] = ..., source_size: Optional[_builtins.str] = ..., storage_profile: Optional[outputs.TargetStorageProfileResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEditable")
    def is_editable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePaths")
    def source_paths(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSize")
    def source_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[outputs.TargetStorageProfileResponse]:
        
        ...
    


@pulumi.output_type
class WebApplicationFrameworkResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WindowsServerLicensingSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, license_cost: _builtins.float, licenses_per_core: _builtins.int, software_assurance_cost: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseCost")
    def license_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licensesPerCore")
    def licenses_per_core(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceCost")
    def software_assurance_cost(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class WorkloadDeploymentModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_operations: Sequence[_builtins.str], correlation_id: _builtins.str, current_job: outputs.WorkloadDeploymentModelPropertiesResponseCurrentJob, health_errors: Sequence[outputs.HealthErrorModelResponse], last_successful_migrate_time: _builtins.str, last_successful_test_migrate_time: _builtins.str, migration_status: _builtins.str, migration_status_description: _builtins.str, provisioning_state: _builtins.str, status: _builtins.str, status_description: _builtins.str, test_migration_status: _builtins.str, test_migration_status_description: _builtins.str, custom_properties: Optional[Any] = ..., display_name: Optional[_builtins.str] = ..., target_platform: Optional[_builtins.str] = ..., workload_instance_properties: Optional[outputs.WorkloadInstanceModelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOperations")
    def allowed_operations(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentJob")
    def current_job(self) -> outputs.WorkloadDeploymentModelPropertiesResponseCurrentJob:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulMigrateTime")
    def last_successful_migrate_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulTestMigrateTime")
    def last_successful_test_migrate_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatus")
    def migration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatusDescription")
    def migration_status_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusDescription")
    def status_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testMigrationStatus")
    def test_migration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testMigrationStatusDescription")
    def test_migration_status_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPlatform")
    def target_platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadInstanceProperties")
    def workload_instance_properties(self) -> Optional[outputs.WorkloadInstanceModelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class WorkloadDeploymentModelPropertiesResponseCurrentJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: _builtins.str, end_time: _builtins.str, id: _builtins.str, name: _builtins.str, scenario_name: _builtins.str, start_time: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scenarioName")
    def scenario_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkloadDeploymentModelResponseSystemData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadInstanceModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_operations: Sequence[_builtins.str], current_job: outputs.WorkloadInstanceModelPropertiesResponseCurrentJob, health_errors: Sequence[outputs.HealthErrorModelResponse], last_successful_replication_cycle_time: _builtins.str, provisioning_state: _builtins.str, replication_health: _builtins.str, replication_status: _builtins.str, replication_status_description: _builtins.str, custom_properties: Optional[Any] = ..., display_name: Optional[_builtins.str] = ..., master_site_name: Optional[_builtins.str] = ..., migrate_agent_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., source_name: Optional[_builtins.str] = ..., source_platform: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOperations")
    def allowed_operations(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentJob")
    def current_job(self) -> outputs.WorkloadInstanceModelPropertiesResponseCurrentJob:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulReplicationCycleTime")
    def last_successful_replication_cycle_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationHealth")
    def replication_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationStatus")
    def replication_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationStatusDescription")
    def replication_status_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterSiteName")
    def master_site_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrateAgentId")
    def migrate_agent_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePlatform")
    def source_platform(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadInstanceModelPropertiesResponseCurrentJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: _builtins.str, end_time: _builtins.str, id: _builtins.str, name: _builtins.str, scenario_name: _builtins.str, start_time: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scenarioName")
    def scenario_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkloadInstanceModelResponseSystemData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


