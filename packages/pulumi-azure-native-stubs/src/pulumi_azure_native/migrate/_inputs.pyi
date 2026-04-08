import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ACRPropertiesArgs",
    "ACRPropertiesArgsDict",
    "AKSAssessmentSettingsArgs",
    "AKSAssessmentSettingsArgsDict",
    "AKSDeploymentPropertiesArgs",
    "AKSDeploymentPropertiesArgsDict",
    "AKSDeploymentSpecificationArgs",
    "AKSDeploymentSpecificationArgsDict",
    ...,
    ...,
    "ApacheTomcatAKSWorkloadDeploymentArgs",
    "ApacheTomcatAKSWorkloadDeploymentArgsDict",
    "ApacheTomcatWebApplicationArgs",
    "ApacheTomcatWebApplicationArgsDict",
    ...,
    ...,
    "AppInsightMonitoringPropertiesArgs",
    "AppInsightMonitoringPropertiesArgsDict",
    "AppSvcContainerSettingsArgs",
    "AppSvcContainerSettingsArgsDict",
    "AppSvcNativeSettingsArgs",
    "AppSvcNativeSettingsArgsDict",
    "ArgArgs",
    "ArgArgsDict",
    "AssessmentPropertiesArgs",
    "AssessmentPropertiesArgsDict",
    "AssessmentScopeParametersArgs",
    "AssessmentScopeParametersArgsDict",
    "AutomationArtifactArgs",
    "AutomationArtifactArgsDict",
    "AvailabilitySetResourceSettingsArgs",
    "AvailabilitySetResourceSettingsArgsDict",
    "AvsAssessmentPropertiesV2Args",
    "AvsAssessmentPropertiesV2ArgsDict",
    "AvsAssessmentSettingsArgs",
    "AvsAssessmentSettingsArgsDict",
    "AzureArcManagementSettingsArgs",
    "AzureArcManagementSettingsArgsDict",
    "AzureArcMonitoringSettingsArgs",
    "AzureArcMonitoringSettingsArgsDict",
    "AzureArcSettingsArgs",
    "AzureArcSettingsArgsDict",
    "AzureFileShareHydrationProfileArgs",
    "AzureFileShareHydrationProfileArgsDict",
    "AzureSettingsArgs",
    "AzureSettingsArgsDict",
    "BillingSettingsArgs",
    "BillingSettingsArgsDict",
    "BindingArgs",
    "BindingArgsDict",
    "CertArgs",
    "CertArgsDict",
    "CollectorAgentPropertiesBaseArgs",
    "CollectorAgentPropertiesBaseArgsDict",
    "CollectorAgentPropertiesArgs",
    "CollectorAgentPropertiesArgsDict",
    "CollectorAgentSpnPropertiesBaseArgs",
    "CollectorAgentSpnPropertiesBaseArgsDict",
    "CollectorBodyAgentSpnPropertiesArgs",
    "CollectorBodyAgentSpnPropertiesArgsDict",
    "CollectorPropertiesArgs",
    "CollectorPropertiesArgsDict",
    "CompoundAssessmentPropertiesArgs",
    "CompoundAssessmentPropertiesArgsDict",
    "ComputeSettingsArgs",
    "ComputeSettingsArgsDict",
    "ConnectionStateRequestBodyPropertiesArgs",
    "ConnectionStateRequestBodyPropertiesArgsDict",
    "ContainerImagePropertiesArgs",
    "ContainerImagePropertiesArgsDict",
    "DirectoryPathArgs",
    "DirectoryPathArgsDict",
    "DiscoveredEntityLightSummaryArgs",
    "DiscoveredEntityLightSummaryArgsDict",
    "DiskEncryptionSetResourceSettingsArgs",
    "DiskEncryptionSetResourceSettingsArgsDict",
    "EntityUptimeArgs",
    "EntityUptimeArgsDict",
    "FacilitySettingsArgs",
    "FacilitySettingsArgsDict",
    "GmsaAuthenticationPropertiesArgs",
    "GmsaAuthenticationPropertiesArgsDict",
    "GroupPropertiesArgs",
    "GroupPropertiesArgsDict",
    "HeterogeneousAssessmentPropertiesArgs",
    "HeterogeneousAssessmentPropertiesArgsDict",
    "HypervLicenseArgs",
    "HypervLicenseArgsDict",
    "HypervVirtualizationManagementSettingsArgs",
    "HypervVirtualizationManagementSettingsArgsDict",
    "IISAKSWorkloadDeploymentModelCustomPropertiesArgs",
    ...,
    "IISAKSWorkloadDeploymentArgs",
    "IISAKSWorkloadDeploymentArgsDict",
    "IISApplicationDetailsArgs",
    "IISApplicationDetailsArgsDict",
    "IISVirtualApplicationDetailsArgs",
    "IISVirtualApplicationDetailsArgsDict",
    "IISWebApplicationArgs",
    "IISWebApplicationArgsDict",
    "IISWebServerArgs",
    "IISWebServerArgsDict",
    "IISWorkloadInstanceModelCustomPropertiesArgs",
    "IISWorkloadInstanceModelCustomPropertiesArgsDict",
    "IdentityModelArgs",
    "IdentityModelArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "ImportCollectorPropertiesArgs",
    "ImportCollectorPropertiesArgsDict",
    "ImportSqlCollectorPropertiesArgs",
    "ImportSqlCollectorPropertiesArgsDict",
    "KeyVaultResourceSettingsArgs",
    "KeyVaultResourceSettingsArgsDict",
    "KeyVaultSecretStorePropertiesArgs",
    "KeyVaultSecretStorePropertiesArgsDict",
    "LBBackendAddressPoolResourceSettingsArgs",
    "LBBackendAddressPoolResourceSettingsArgsDict",
    "LBFrontendIPConfigurationResourceSettingsArgs",
    "LBFrontendIPConfigurationResourceSettingsArgsDict",
    "LaborSettingsArgs",
    "LaborSettingsArgsDict",
    "LinuxServerLicensingSettingsArgs",
    "LinuxServerLicensingSettingsArgsDict",
    "LoadBalancerBackendAddressPoolReferenceArgs",
    "LoadBalancerBackendAddressPoolReferenceArgsDict",
    "LoadBalancerNatRuleReferenceArgs",
    "LoadBalancerNatRuleReferenceArgsDict",
    "LoadBalancerResourceSettingsArgs",
    "LoadBalancerResourceSettingsArgsDict",
    "MachineAssessmentSettingsArgs",
    "MachineAssessmentSettingsArgsDict",
    "MachineAssessmentV2PropertiesArgs",
    "MachineAssessmentV2PropertiesArgsDict",
    "ManagedIdentityPropertiesArgs",
    "ManagedIdentityPropertiesArgsDict",
    "ManagementSettingsArgs",
    "ManagementSettingsArgsDict",
    "MigrateAgentModelPropertiesArgs",
    "MigrateAgentModelPropertiesArgsDict",
    "MigrateProjectPropertiesArgs",
    "MigrateProjectPropertiesArgsDict",
    "MigrateProjectTagsArgs",
    "MigrateProjectTagsArgsDict",
    "MigrationConfigurationArgs",
    "MigrationConfigurationArgsDict",
    "MigrationEntityGroupPropertiesArgs",
    "MigrationEntityGroupPropertiesArgsDict",
    "MigrationEntityPropertiesArgs",
    "MigrationEntityPropertiesArgsDict",
    "ModernizeProjectModelPropertiesArgs",
    "ModernizeProjectModelPropertiesArgsDict",
    "MoveCollectionPropertiesArgs",
    "MoveCollectionPropertiesArgsDict",
    "MoveResourceDependencyOverrideArgs",
    "MoveResourceDependencyOverrideArgsDict",
    "MoveResourcePropertiesArgs",
    "MoveResourcePropertiesArgsDict",
    "NetworkInterfaceResourceSettingsArgs",
    "NetworkInterfaceResourceSettingsArgsDict",
    "NetworkSecurityGroupResourceSettingsArgs",
    "NetworkSecurityGroupResourceSettingsArgsDict",
    "NetworkSettingsArgs",
    "NetworkSettingsArgsDict",
    "NicIpConfigurationResourceSettingsArgs",
    "NicIpConfigurationResourceSettingsArgsDict",
    "NsgReferenceArgs",
    "NsgReferenceArgsDict",
    "NsgSecurityRuleArgs",
    "NsgSecurityRuleArgsDict",
    "OnPremiseSettingsArgs",
    "OnPremiseSettingsArgsDict",
    "OperatingSystemDetailsArgs",
    "OperatingSystemDetailsArgsDict",
    "OtherManagementCostsSettingsArgs",
    "OtherManagementCostsSettingsArgsDict",
    "PerfDataSettingsArgs",
    "PerfDataSettingsArgsDict",
    "PerformanceDataArgs",
    "PerformanceDataArgsDict",
    "PortMappingArgs",
    "PortMappingArgsDict",
    "PrivateEndpointConnectionPropertiesArgs",
    "PrivateEndpointConnectionPropertiesArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "ProjectPropertiesArgs",
    "ProjectPropertiesArgsDict",
    "PublicIPAddressResourceSettingsArgs",
    "PublicIPAddressResourceSettingsArgsDict",
    "PublicIpReferenceArgs",
    "PublicIpReferenceArgsDict",
    "ResourceGroupResourceSettingsArgs",
    "ResourceGroupResourceSettingsArgsDict",
    "ResourceIdentityArgs",
    "ResourceIdentityArgsDict",
    "ResourceRequirementsArgs",
    "ResourceRequirementsArgsDict",
    "SavingsSettingsArgs",
    "SavingsSettingsArgsDict",
    "ScopeArgs",
    "ScopeArgsDict",
    "SecretStoreDetailsArgs",
    "SecretStoreDetailsArgsDict",
    "SecretStorePropertiesArgs",
    "SecretStorePropertiesArgsDict",
    "SecuritySettingsArgs",
    "SecuritySettingsArgsDict",
    "ServerMigrationSpecificPropertiesArgs",
    "ServerMigrationSpecificPropertiesArgsDict",
    "SettingsArgs",
    "SettingsArgsDict",
    "SolutionDetailsArgs",
    "SolutionDetailsArgsDict",
    "SolutionPropertiesArgs",
    "SolutionPropertiesArgsDict",
    "SqlAssessmentSettingsArgs",
    "SqlAssessmentSettingsArgsDict",
    "SqlAssessmentV3PropertiesArgs",
    "SqlAssessmentV3PropertiesArgsDict",
    "SqlDatabaseResourceSettingsArgs",
    "SqlDatabaseResourceSettingsArgsDict",
    "SqlDbSettingsV3Args",
    "SqlDbSettingsV3ArgsDict",
    "SqlDbSettingsArgs",
    "SqlDbSettingsArgsDict",
    "SqlElasticPoolResourceSettingsArgs",
    "SqlElasticPoolResourceSettingsArgsDict",
    "SqlMiSettingsV3Args",
    "SqlMiSettingsV3ArgsDict",
    "SqlMiSettingsArgs",
    "SqlMiSettingsArgsDict",
    "SqlServerLicensingSettingsArgs",
    "SqlServerLicensingSettingsArgsDict",
    "SqlServerResourceSettingsArgs",
    "SqlServerResourceSettingsArgsDict",
    "SqlVmSettingsArgs",
    "SqlVmSettingsArgsDict",
    "StorageSettingsArgs",
    "StorageSettingsArgsDict",
    "SubnetReferenceArgs",
    "SubnetReferenceArgsDict",
    "SubnetResourceSettingsArgs",
    "SubnetResourceSettingsArgsDict",
    "TargetAssessmentArmIdsArgs",
    "TargetAssessmentArmIdsArgsDict",
    "TargetStorageProfileArgs",
    "TargetStorageProfileArgsDict",
    "TaskPropertiesArgs",
    "TaskPropertiesArgsDict",
    "ThirdPartyManagementSettingsArgs",
    "ThirdPartyManagementSettingsArgsDict",
    "UserAssignedIdentityArgs",
    "UserAssignedIdentityArgsDict",
    "VMwareMigrateAgentModelCustomPropertiesArgs",
    "VMwareMigrateAgentModelCustomPropertiesArgsDict",
    "VirtualMachineResourceSettingsArgs",
    "VirtualMachineResourceSettingsArgsDict",
    "VirtualNetworkResourceSettingsArgs",
    "VirtualNetworkResourceSettingsArgsDict",
    "VirtualizationSoftwareSettingsArgs",
    "VirtualizationSoftwareSettingsArgsDict",
    "VmUptimeArgs",
    "VmUptimeArgsDict",
    "WavePropertiesArgs",
    "WavePropertiesArgsDict",
    "WebAppAssessmentSettingsArgs",
    "WebAppAssessmentSettingsArgsDict",
    "WebAppAssessmentV3PropertiesArgs",
    "WebAppAssessmentV3PropertiesArgsDict",
    "WebApplicationConfigurationArgs",
    "WebApplicationConfigurationArgsDict",
    "WebApplicationDirectoryArgs",
    "WebApplicationDirectoryArgsDict",
    "WebApplicationFrameworkArgs",
    "WebApplicationFrameworkArgsDict",
    "WindowsServerLicensingSettingsArgs",
    "WindowsServerLicensingSettingsArgsDict",
    "WorkloadDeploymentModelPropertiesArgs",
    "WorkloadDeploymentModelPropertiesArgsDict",
    "WorkloadInstanceModelPropertiesArgs",
    "WorkloadInstanceModelPropertiesArgsDict",
]

class ACRPropertiesArgsDict(TypedDict):
    registry_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ACRPropertiesArgs:
    def __init__(
        __self__,
        *,
        registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registry_name.setter
    def registry_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AKSAssessmentSettingsArgsDict(TypedDict):
    azure_location: pulumi.Input[_builtins.str]
    category: pulumi.Input[Union[_builtins.str, AzureVmCategory]]
    consolidation: pulumi.Input[Union[_builtins.str, ConsolidationType]]
    currency: pulumi.Input[Union[_builtins.str, AzureCurrency]]
    environment_type: pulumi.Input[Union[_builtins.str, AzureEnvironmentType]]
    licensing_program: pulumi.Input[Union[_builtins.str, LicensingProgram]]
    pricing_tier: pulumi.Input[Union[_builtins.str, PricingTier]]
    savings_options: pulumi.Input[Union[_builtins.str, SavingsOptions]]
    sizing_criteria: pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    performance_data: NotRequired[pulumi.Input[PerfDataSettingsArgsDict]]
    scaling_factor: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class AKSAssessmentSettingsArgs:
    def __init__(
        __self__,
        *,
        azure_location: pulumi.Input[_builtins.str],
        category: pulumi.Input[Union[_builtins.str, AzureVmCategory]],
        consolidation: pulumi.Input[Union[_builtins.str, ConsolidationType]],
        currency: pulumi.Input[Union[_builtins.str, AzureCurrency]],
        environment_type: pulumi.Input[Union[_builtins.str, AzureEnvironmentType]],
        licensing_program: pulumi.Input[Union[_builtins.str, LicensingProgram]],
        pricing_tier: pulumi.Input[Union[_builtins.str, PricingTier]],
        savings_options: pulumi.Input[Union[_builtins.str, SavingsOptions]],
        sizing_criteria: pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]],
        discount_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        performance_data: Optional[pulumi.Input[PerfDataSettingsArgs]] = ...,
        scaling_factor: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> pulumi.Input[_builtins.str]: ...
    @azure_location.setter
    def azure_location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Input[Union[_builtins.str, AzureVmCategory]]: ...
    @category.setter
    def category(self, value: pulumi.Input[Union[_builtins.str, AzureVmCategory]]): ...
    @_builtins.property
    @pulumi.getter
    def consolidation(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ConsolidationType]]: ...
    @consolidation.setter
    def consolidation(
        self, value: pulumi.Input[Union[_builtins.str, ConsolidationType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def currency(self) -> pulumi.Input[Union[_builtins.str, AzureCurrency]]: ...
    @currency.setter
    def currency(self, value: pulumi.Input[Union[_builtins.str, AzureCurrency]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AzureEnvironmentType]]: ...
    @environment_type.setter
    def environment_type(
        self, value: pulumi.Input[Union[_builtins.str, AzureEnvironmentType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="licensingProgram")
    def licensing_program(
        self,
    ) -> pulumi.Input[Union[_builtins.str, LicensingProgram]]: ...
    @licensing_program.setter
    def licensing_program(
        self, value: pulumi.Input[Union[_builtins.str, LicensingProgram]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pricingTier")
    def pricing_tier(self) -> pulumi.Input[Union[_builtins.str, PricingTier]]: ...
    @pricing_tier.setter
    def pricing_tier(self, value: pulumi.Input[Union[_builtins.str, PricingTier]]): ...
    @_builtins.property
    @pulumi.getter(name="savingsOptions")
    def savings_options(self) -> pulumi.Input[Union[_builtins.str, SavingsOptions]]: ...
    @savings_options.setter
    def savings_options(
        self, value: pulumi.Input[Union[_builtins.str, SavingsOptions]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sizingCriteria")
    def sizing_criteria(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]: ...
    @sizing_criteria.setter
    def sizing_criteria(
        self, value: pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> Optional[pulumi.Input[PerfDataSettingsArgs]]: ...
    @performance_data.setter
    def performance_data(self, value: Optional[pulumi.Input[PerfDataSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @scaling_factor.setter
    def scaling_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AKSDeploymentPropertiesArgsDict(TypedDict):
    aks_cluster_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AKSDeploymentPropertiesArgs:
    def __init__(
        __self__,
        *,
        aks_cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aksClusterName")
    def aks_cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aks_cluster_name.setter
    def aks_cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AKSDeploymentSpecificationArgsDict(TypedDict):
    kubernetes_objects_yaml: NotRequired[pulumi.Input[_builtins.str]]
    load_balancer_type: NotRequired[
        pulumi.Input[Union[_builtins.str, LoadBalancerType]]
    ]
    replica_count: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AKSDeploymentSpecificationArgs:
    def __init__(
        __self__,
        *,
        kubernetes_objects_yaml: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancer_type: Optional[
            pulumi.Input[Union[_builtins.str, LoadBalancerType]]
        ] = ...,
        replica_count: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesObjectsYaml")
    def kubernetes_objects_yaml(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kubernetes_objects_yaml.setter
    def kubernetes_objects_yaml(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LoadBalancerType]]]: ...
    @load_balancer_type.setter
    def load_balancer_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LoadBalancerType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApacheTomcatAKSWorkloadDeploymentModelCustomPropertiesArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    apache_tomcat_aks_workload_deployment_properties: NotRequired[
        pulumi.Input[ApacheTomcatAKSWorkloadDeploymentArgsDict]
    ]

@pulumi.input_type
class ApacheTomcatAKSWorkloadDeploymentModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        apache_tomcat_aks_workload_deployment_properties: Optional[
            pulumi.Input[ApacheTomcatAKSWorkloadDeploymentArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apacheTomcatAksWorkloadDeploymentProperties")
    def apache_tomcat_aks_workload_deployment_properties(
        self,
    ) -> Optional[pulumi.Input[ApacheTomcatAKSWorkloadDeploymentArgs]]: ...
    @apache_tomcat_aks_workload_deployment_properties.setter
    def apache_tomcat_aks_workload_deployment_properties(
        self, value: Optional[pulumi.Input[ApacheTomcatAKSWorkloadDeploymentArgs]]
    ): ...

class ApacheTomcatAKSWorkloadDeploymentArgsDict(TypedDict):
    automation_artifact_properties: NotRequired[
        pulumi.Input[AutomationArtifactArgsDict]
    ]
    bindings: NotRequired[pulumi.Input[Sequence[pulumi.Input[BindingArgsDict]]]]
    build_container_images: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ContainerImagePropertiesArgsDict]]]
    ]
    cluster_properties: NotRequired[pulumi.Input[AKSDeploymentPropertiesArgsDict]]
    configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgsDict]]]
    ]
    container_image_properties: NotRequired[
        pulumi.Input[ContainerImagePropertiesArgsDict]
    ]
    deployment_name_prefix: NotRequired[pulumi.Input[_builtins.str]]
    deployment_spec: NotRequired[pulumi.Input[AKSDeploymentSpecificationArgsDict]]
    directories: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgsDict]]]
    ]
    limits: NotRequired[pulumi.Input[ResourceRequirementsArgsDict]]
    monitoring_properties: NotRequired[
        pulumi.Input[AppInsightMonitoringPropertiesArgsDict]
    ]
    requests: NotRequired[pulumi.Input[ResourceRequirementsArgsDict]]
    target_platform_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApacheTomcatAKSWorkloadDeploymentArgs:
    def __init__(
        __self__,
        *,
        automation_artifact_properties: Optional[
            pulumi.Input[AutomationArtifactArgs]
        ] = ...,
        bindings: Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]] = ...,
        build_container_images: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerImagePropertiesArgs]]]
        ] = ...,
        cluster_properties: Optional[pulumi.Input[AKSDeploymentPropertiesArgs]] = ...,
        configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
        ] = ...,
        container_image_properties: Optional[
            pulumi.Input[ContainerImagePropertiesArgs]
        ] = ...,
        deployment_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_spec: Optional[pulumi.Input[AKSDeploymentSpecificationArgs]] = ...,
        directories: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
        ] = ...,
        limits: Optional[pulumi.Input[ResourceRequirementsArgs]] = ...,
        monitoring_properties: Optional[
            pulumi.Input[AppInsightMonitoringPropertiesArgs]
        ] = ...,
        requests: Optional[pulumi.Input[ResourceRequirementsArgs]] = ...,
        target_platform_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automationArtifactProperties")
    def automation_artifact_properties(
        self,
    ) -> Optional[pulumi.Input[AutomationArtifactArgs]]: ...
    @automation_artifact_properties.setter
    def automation_artifact_properties(
        self, value: Optional[pulumi.Input[AutomationArtifactArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def bindings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]]: ...
    @bindings.setter
    def bindings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="buildContainerImages")
    def build_container_images(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ContainerImagePropertiesArgs]]]
    ]: ...
    @build_container_images.setter
    def build_container_images(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerImagePropertiesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterProperties")
    def cluster_properties(
        self,
    ) -> Optional[pulumi.Input[AKSDeploymentPropertiesArgs]]: ...
    @cluster_properties.setter
    def cluster_properties(
        self, value: Optional[pulumi.Input[AKSDeploymentPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
    ]: ...
    @configurations.setter
    def configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerImageProperties")
    def container_image_properties(
        self,
    ) -> Optional[pulumi.Input[ContainerImagePropertiesArgs]]: ...
    @container_image_properties.setter
    def container_image_properties(
        self, value: Optional[pulumi.Input[ContainerImagePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentNamePrefix")
    def deployment_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_name_prefix.setter
    def deployment_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentSpec")
    def deployment_spec(
        self,
    ) -> Optional[pulumi.Input[AKSDeploymentSpecificationArgs]]: ...
    @deployment_spec.setter
    def deployment_spec(
        self, value: Optional[pulumi.Input[AKSDeploymentSpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def directories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
    ]: ...
    @directories.setter
    def directories(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[ResourceRequirementsArgs]]: ...
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[ResourceRequirementsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringProperties")
    def monitoring_properties(
        self,
    ) -> Optional[pulumi.Input[AppInsightMonitoringPropertiesArgs]]: ...
    @monitoring_properties.setter
    def monitoring_properties(
        self, value: Optional[pulumi.Input[AppInsightMonitoringPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[ResourceRequirementsArgs]]: ...
    @requests.setter
    def requests(self, value: Optional[pulumi.Input[ResourceRequirementsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="targetPlatformIdentity")
    def target_platform_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_platform_identity.setter
    def target_platform_identity(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ApacheTomcatWebApplicationArgsDict(TypedDict):
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    application_name: NotRequired[pulumi.Input[_builtins.str]]
    application_scratch_path: NotRequired[pulumi.Input[_builtins.str]]
    bindings: NotRequired[pulumi.Input[Sequence[pulumi.Input[BindingArgsDict]]]]
    configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgsDict]]]
    ]
    directories: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgsDict]]]
    ]
    discovered_frameworks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationFrameworkArgsDict]]]
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    limits: NotRequired[pulumi.Input[ResourceRequirementsArgsDict]]
    path: NotRequired[pulumi.Input[DirectoryPathArgsDict]]
    primary_framework: NotRequired[pulumi.Input[WebApplicationFrameworkArgsDict]]
    requests: NotRequired[pulumi.Input[ResourceRequirementsArgsDict]]
    web_server_id: NotRequired[pulumi.Input[_builtins.str]]
    web_server_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApacheTomcatWebApplicationArgs:
    def __init__(
        __self__,
        *,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        application_name: Optional[pulumi.Input[_builtins.str]] = ...,
        application_scratch_path: Optional[pulumi.Input[_builtins.str]] = ...,
        bindings: Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]] = ...,
        configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
        ] = ...,
        directories: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
        ] = ...,
        discovered_frameworks: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationFrameworkArgs]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        limits: Optional[pulumi.Input[ResourceRequirementsArgs]] = ...,
        path: Optional[pulumi.Input[DirectoryPathArgs]] = ...,
        primary_framework: Optional[pulumi.Input[WebApplicationFrameworkArgs]] = ...,
        requests: Optional[pulumi.Input[ResourceRequirementsArgs]] = ...,
        web_server_id: Optional[pulumi.Input[_builtins.str]] = ...,
        web_server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_name.setter
    def application_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationScratchPath")
    def application_scratch_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_scratch_path.setter
    def application_scratch_path(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def bindings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]]: ...
    @bindings.setter
    def bindings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
    ]: ...
    @configurations.setter
    def configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def directories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
    ]: ...
    @directories.setter
    def directories(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveredFrameworks")
    def discovered_frameworks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationFrameworkArgs]]]
    ]: ...
    @discovered_frameworks.setter
    def discovered_frameworks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationFrameworkArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[ResourceRequirementsArgs]]: ...
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[ResourceRequirementsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[DirectoryPathArgs]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[DirectoryPathArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryFramework")
    def primary_framework(
        self,
    ) -> Optional[pulumi.Input[WebApplicationFrameworkArgs]]: ...
    @primary_framework.setter
    def primary_framework(
        self, value: Optional[pulumi.Input[WebApplicationFrameworkArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[ResourceRequirementsArgs]]: ...
    @requests.setter
    def requests(self, value: Optional[pulumi.Input[ResourceRequirementsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="webServerId")
    def web_server_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_server_id.setter
    def web_server_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webServerName")
    def web_server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_server_name.setter
    def web_server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApacheTomcatWorkloadInstanceModelCustomPropertiesArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    apache_tomcat_web_application: NotRequired[
        pulumi.Input[ApacheTomcatWebApplicationArgsDict]
    ]
    web_app_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    web_app_site_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApacheTomcatWorkloadInstanceModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        apache_tomcat_web_application: Optional[
            pulumi.Input[ApacheTomcatWebApplicationArgs]
        ] = ...,
        web_app_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        web_app_site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apacheTomcatWebApplication")
    def apache_tomcat_web_application(
        self,
    ) -> Optional[pulumi.Input[ApacheTomcatWebApplicationArgs]]: ...
    @apache_tomcat_web_application.setter
    def apache_tomcat_web_application(
        self, value: Optional[pulumi.Input[ApacheTomcatWebApplicationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webAppArmId")
    def web_app_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_app_arm_id.setter
    def web_app_arm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webAppSiteName")
    def web_app_site_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_app_site_name.setter
    def web_app_site_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppInsightMonitoringPropertiesArgsDict(TypedDict):
    app_insights_name: NotRequired[pulumi.Input[_builtins.str]]
    is_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    secret_store_details: NotRequired[pulumi.Input[SecretStoreDetailsArgsDict]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AppInsightMonitoringPropertiesArgs:
    def __init__(
        __self__,
        *,
        app_insights_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_store_details: Optional[pulumi.Input[SecretStoreDetailsArgs]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appInsightsName")
    def app_insights_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_insights_name.setter
    def app_insights_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStoreDetails")
    def secret_store_details(
        self,
    ) -> Optional[pulumi.Input[SecretStoreDetailsArgs]]: ...
    @secret_store_details.setter
    def secret_store_details(
        self, value: Optional[pulumi.Input[SecretStoreDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppSvcContainerSettingsArgsDict(TypedDict):
    isolation_required: pulumi.Input[_builtins.bool]

@pulumi.input_type
class AppSvcContainerSettingsArgs:
    def __init__(
        __self__, *, isolation_required: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isolationRequired")
    def isolation_required(self) -> pulumi.Input[_builtins.bool]: ...
    @isolation_required.setter
    def isolation_required(self, value: pulumi.Input[_builtins.bool]): ...

class AppSvcNativeSettingsArgsDict(TypedDict):
    isolation_required: pulumi.Input[_builtins.bool]

@pulumi.input_type
class AppSvcNativeSettingsArgs:
    def __init__(
        __self__, *, isolation_required: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isolationRequired")
    def isolation_required(self) -> pulumi.Input[_builtins.bool]: ...
    @isolation_required.setter
    def isolation_required(self, value: pulumi.Input[_builtins.bool]): ...

class ArgArgsDict(TypedDict):
    query: pulumi.Input[_builtins.str]

@pulumi.input_type
class ArgArgs:
    def __init__(__self__, *, query: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]: ...
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): ...

class AssessmentPropertiesArgsDict(TypedDict):
    azure_disk_type: pulumi.Input[Union[_builtins.str, AzureDiskType]]
    azure_hybrid_use_benefit: pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]
    azure_location: pulumi.Input[Union[_builtins.str, AzureLocation]]
    azure_offer_code: pulumi.Input[Union[_builtins.str, AzureOfferCode]]
    azure_pricing_tier: pulumi.Input[Union[_builtins.str, AzurePricingTier]]
    azure_storage_redundancy: pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]
    azure_vm_families: pulumi.Input[
        Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]
    ]
    currency: pulumi.Input[Union[_builtins.str, Currency]]
    discount_percentage: pulumi.Input[_builtins.float]
    percentile: pulumi.Input[Union[_builtins.str, Percentile]]
    reserved_instance: pulumi.Input[Union[_builtins.str, ReservedInstance]]
    scaling_factor: pulumi.Input[_builtins.float]
    sizing_criterion: pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
    stage: pulumi.Input[Union[_builtins.str, AssessmentStage]]
    time_range: pulumi.Input[Union[_builtins.str, TimeRange]]
    vm_uptime: pulumi.Input[VmUptimeArgsDict]

@pulumi.input_type
class AssessmentPropertiesArgs:
    def __init__(
        __self__,
        *,
        azure_disk_type: pulumi.Input[Union[_builtins.str, AzureDiskType]],
        azure_hybrid_use_benefit: pulumi.Input[
            Union[_builtins.str, AzureHybridUseBenefit]
        ],
        azure_location: pulumi.Input[Union[_builtins.str, AzureLocation]],
        azure_offer_code: pulumi.Input[Union[_builtins.str, AzureOfferCode]],
        azure_pricing_tier: pulumi.Input[Union[_builtins.str, AzurePricingTier]],
        azure_storage_redundancy: pulumi.Input[
            Union[_builtins.str, AzureStorageRedundancy]
        ],
        azure_vm_families: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]
        ],
        currency: pulumi.Input[Union[_builtins.str, Currency]],
        discount_percentage: pulumi.Input[_builtins.float],
        percentile: pulumi.Input[Union[_builtins.str, Percentile]],
        reserved_instance: pulumi.Input[Union[_builtins.str, ReservedInstance]],
        scaling_factor: pulumi.Input[_builtins.float],
        sizing_criterion: pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]],
        stage: pulumi.Input[Union[_builtins.str, AssessmentStage]],
        time_range: pulumi.Input[Union[_builtins.str, TimeRange]],
        vm_uptime: pulumi.Input[VmUptimeArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureDiskType")
    def azure_disk_type(self) -> pulumi.Input[Union[_builtins.str, AzureDiskType]]: ...
    @azure_disk_type.setter
    def azure_disk_type(
        self, value: pulumi.Input[Union[_builtins.str, AzureDiskType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureHybridUseBenefit")
    def azure_hybrid_use_benefit(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]: ...
    @azure_hybrid_use_benefit.setter
    def azure_hybrid_use_benefit(
        self, value: pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> pulumi.Input[Union[_builtins.str, AzureLocation]]: ...
    @azure_location.setter
    def azure_location(
        self, value: pulumi.Input[Union[_builtins.str, AzureLocation]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AzureOfferCode]]: ...
    @azure_offer_code.setter
    def azure_offer_code(
        self, value: pulumi.Input[Union[_builtins.str, AzureOfferCode]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azurePricingTier")
    def azure_pricing_tier(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AzurePricingTier]]: ...
    @azure_pricing_tier.setter
    def azure_pricing_tier(
        self, value: pulumi.Input[Union[_builtins.str, AzurePricingTier]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureStorageRedundancy")
    def azure_storage_redundancy(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]: ...
    @azure_storage_redundancy.setter
    def azure_storage_redundancy(
        self, value: pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureVmFamilies")
    def azure_vm_families(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]: ...
    @azure_vm_families.setter
    def azure_vm_families(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def currency(self) -> pulumi.Input[Union[_builtins.str, Currency]]: ...
    @currency.setter
    def currency(self, value: pulumi.Input[Union[_builtins.str, Currency]]): ...
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> pulumi.Input[_builtins.float]: ...
    @discount_percentage.setter
    def discount_percentage(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def percentile(self) -> pulumi.Input[Union[_builtins.str, Percentile]]: ...
    @percentile.setter
    def percentile(self, value: pulumi.Input[Union[_builtins.str, Percentile]]): ...
    @_builtins.property
    @pulumi.getter(name="reservedInstance")
    def reserved_instance(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ReservedInstance]]: ...
    @reserved_instance.setter
    def reserved_instance(
        self, value: pulumi.Input[Union[_builtins.str, ReservedInstance]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> pulumi.Input[_builtins.float]: ...
    @scaling_factor.setter
    def scaling_factor(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]: ...
    @sizing_criterion.setter
    def sizing_criterion(
        self, value: pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> pulumi.Input[Union[_builtins.str, AssessmentStage]]: ...
    @stage.setter
    def stage(self, value: pulumi.Input[Union[_builtins.str, AssessmentStage]]): ...
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> pulumi.Input[Union[_builtins.str, TimeRange]]: ...
    @time_range.setter
    def time_range(self, value: pulumi.Input[Union[_builtins.str, TimeRange]]): ...
    @_builtins.property
    @pulumi.getter(name="vmUptime")
    def vm_uptime(self) -> pulumi.Input[VmUptimeArgs]: ...
    @vm_uptime.setter
    def vm_uptime(self, value: pulumi.Input[VmUptimeArgs]): ...

class AssessmentScopeParametersArgsDict(TypedDict):
    server_group_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AssessmentScopeParametersArgs:
    def __init__(
        __self__, *, server_group_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverGroupId")
    def server_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_group_id.setter
    def server_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationArtifactArgsDict(TypedDict):
    artifacts: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    azure_file_share_profile: NotRequired[
        pulumi.Input[AzureFileShareHydrationProfileArgsDict]
    ]
    status: NotRequired[pulumi.Input[Union[_builtins.str, AutomationArtifactStatus]]]

@pulumi.input_type
class AutomationArtifactArgs:
    def __init__(
        __self__,
        *,
        artifacts: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        azure_file_share_profile: Optional[
            pulumi.Input[AzureFileShareHydrationProfileArgs]
        ] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, AutomationArtifactStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def artifacts(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @artifacts.setter
    def artifacts(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareProfile")
    def azure_file_share_profile(
        self,
    ) -> Optional[pulumi.Input[AzureFileShareHydrationProfileArgs]]: ...
    @azure_file_share_profile.setter
    def azure_file_share_profile(
        self, value: Optional[pulumi.Input[AzureFileShareHydrationProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AutomationArtifactStatus]]]: ...
    @status.setter
    def status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AutomationArtifactStatus]]],
    ): ...

class AvailabilitySetResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    fault_domain: NotRequired[pulumi.Input[_builtins.int]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]
    update_domain: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AvailabilitySetResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        fault_domain: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        update_domain: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="faultDomain")
    def fault_domain(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @fault_domain.setter
    def fault_domain(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateDomain")
    def update_domain(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @update_domain.setter
    def update_domain(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AvsAssessmentPropertiesV2ArgsDict(TypedDict):
    fallback_machine_assessment_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[ScopeArgsDict]]
    settings: NotRequired[pulumi.Input[AvsAssessmentSettingsArgsDict]]

@pulumi.input_type
class AvsAssessmentPropertiesV2Args:
    def __init__(
        __self__,
        *,
        fallback_machine_assessment_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[ScopeArgs]] = ...,
        settings: Optional[pulumi.Input[AvsAssessmentSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fallbackMachineAssessmentArmId")
    def fallback_machine_assessment_arm_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fallback_machine_assessment_arm_id.setter
    def fallback_machine_assessment_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[ScopeArgs]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[ScopeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[AvsAssessmentSettingsArgs]]: ...
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[AvsAssessmentSettingsArgs]]): ...

class AvsAssessmentSettingsArgsDict(TypedDict):
    avs_assessment_scenario: NotRequired[
        pulumi.Input[Union[_builtins.str, AvsAssessmentScenario]]
    ]
    azure_location: NotRequired[pulumi.Input[_builtins.str]]
    billing_settings: NotRequired[pulumi.Input[BillingSettingsArgsDict]]
    cpu_headroom: NotRequired[pulumi.Input[_builtins.float]]
    currency: NotRequired[pulumi.Input[Union[_builtins.str, AzureCurrency]]]
    dedupe_compression: NotRequired[pulumi.Input[_builtins.float]]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    environment_type: NotRequired[pulumi.Input[Union[_builtins.str, EnvironmentType]]]
    external_storage_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExternalStorageType]]]]
    ]
    failures_to_tolerate_and_raid_level_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]]]
    ]
    is_stretch_cluster_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_vcf_byol_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    mem_overcommit: NotRequired[pulumi.Input[_builtins.float]]
    node_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]]]
    ]
    performance_data: NotRequired[pulumi.Input[PerformanceDataArgsDict]]
    savings_settings: NotRequired[pulumi.Input[SavingsSettingsArgsDict]]
    scaling_factor: NotRequired[pulumi.Input[_builtins.float]]
    sizing_criterion: NotRequired[
        pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
    ]
    vcpu_oversubscription: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class AvsAssessmentSettingsArgs:
    def __init__(
        __self__,
        *,
        avs_assessment_scenario: Optional[
            pulumi.Input[Union[_builtins.str, AvsAssessmentScenario]]
        ] = ...,
        azure_location: Optional[pulumi.Input[_builtins.str]] = ...,
        billing_settings: Optional[pulumi.Input[BillingSettingsArgs]] = ...,
        cpu_headroom: Optional[pulumi.Input[_builtins.float]] = ...,
        currency: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]] = ...,
        dedupe_compression: Optional[pulumi.Input[_builtins.float]] = ...,
        discount_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        environment_type: Optional[
            pulumi.Input[Union[_builtins.str, EnvironmentType]]
        ] = ...,
        external_storage_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ExternalStorageType]]]
            ]
        ] = ...,
        failures_to_tolerate_and_raid_level_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]]]
        ] = ...,
        is_stretch_cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_vcf_byol_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        mem_overcommit: Optional[pulumi.Input[_builtins.float]] = ...,
        node_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]]]
        ] = ...,
        performance_data: Optional[pulumi.Input[PerformanceDataArgs]] = ...,
        savings_settings: Optional[pulumi.Input[SavingsSettingsArgs]] = ...,
        scaling_factor: Optional[pulumi.Input[_builtins.float]] = ...,
        sizing_criterion: Optional[
            pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
        ] = ...,
        vcpu_oversubscription: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="avsAssessmentScenario")
    def avs_assessment_scenario(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AvsAssessmentScenario]]]: ...
    @avs_assessment_scenario.setter
    def avs_assessment_scenario(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AvsAssessmentScenario]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_location.setter
    def azure_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="billingSettings")
    def billing_settings(self) -> Optional[pulumi.Input[BillingSettingsArgs]]: ...
    @billing_settings.setter
    def billing_settings(self, value: Optional[pulumi.Input[BillingSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuHeadroom")
    def cpu_headroom(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @cpu_headroom.setter
    def cpu_headroom(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def currency(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]: ...
    @currency.setter
    def currency(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dedupeCompression")
    def dedupe_compression(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @dedupe_compression.setter
    def dedupe_compression(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnvironmentType]]]: ...
    @environment_type.setter
    def environment_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnvironmentType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="externalStorageTypes")
    def external_storage_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExternalStorageType]]]]
    ]: ...
    @external_storage_types.setter
    def external_storage_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ExternalStorageType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failuresToTolerateAndRaidLevelList")
    def failures_to_tolerate_and_raid_level_list(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]]]
    ]: ...
    @failures_to_tolerate_and_raid_level_list.setter
    def failures_to_tolerate_and_raid_level_list(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isStretchClusterEnabled")
    def is_stretch_cluster_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_stretch_cluster_enabled.setter
    def is_stretch_cluster_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isVcfByolEnabled")
    def is_vcf_byol_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_vcf_byol_enabled.setter
    def is_vcf_byol_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="memOvercommit")
    def mem_overcommit(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @mem_overcommit.setter
    def mem_overcommit(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeTypes")
    def node_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]]]
    ]: ...
    @node_types.setter
    def node_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> Optional[pulumi.Input[PerformanceDataArgs]]: ...
    @performance_data.setter
    def performance_data(self, value: Optional[pulumi.Input[PerformanceDataArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="savingsSettings")
    def savings_settings(self) -> Optional[pulumi.Input[SavingsSettingsArgs]]: ...
    @savings_settings.setter
    def savings_settings(self, value: Optional[pulumi.Input[SavingsSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @scaling_factor.setter
    def scaling_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]]: ...
    @sizing_criterion.setter
    def sizing_criterion(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vcpuOversubscription")
    def vcpu_oversubscription(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @vcpu_oversubscription.setter
    def vcpu_oversubscription(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AzureArcManagementSettingsArgsDict(TypedDict):
    monitoring_settings: pulumi.Input[AzureArcMonitoringSettingsArgsDict]

@pulumi.input_type
class AzureArcManagementSettingsArgs:
    def __init__(
        __self__, *, monitoring_settings: pulumi.Input[AzureArcMonitoringSettingsArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monitoringSettings")
    def monitoring_settings(self) -> pulumi.Input[AzureArcMonitoringSettingsArgs]: ...
    @monitoring_settings.setter
    def monitoring_settings(
        self, value: pulumi.Input[AzureArcMonitoringSettingsArgs]
    ): ...

class AzureArcMonitoringSettingsArgsDict(TypedDict):
    alert_rules_count: pulumi.Input[_builtins.int]
    logs_volume_in_gb: pulumi.Input[_builtins.float]

@pulumi.input_type
class AzureArcMonitoringSettingsArgs:
    def __init__(
        __self__,
        *,
        alert_rules_count: pulumi.Input[_builtins.int],
        logs_volume_in_gb: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alertRulesCount")
    def alert_rules_count(self) -> pulumi.Input[_builtins.int]: ...
    @alert_rules_count.setter
    def alert_rules_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="logsVolumeInGB")
    def logs_volume_in_gb(self) -> pulumi.Input[_builtins.float]: ...
    @logs_volume_in_gb.setter
    def logs_volume_in_gb(self, value: pulumi.Input[_builtins.float]): ...

class AzureArcSettingsArgsDict(TypedDict):
    azure_arc_state: pulumi.Input[Union[_builtins.str, AzureArcState]]
    labor_cost_percentage: NotRequired[pulumi.Input[_builtins.float]]
    management_settings: NotRequired[pulumi.Input[AzureArcManagementSettingsArgsDict]]

@pulumi.input_type
class AzureArcSettingsArgs:
    def __init__(
        __self__,
        *,
        azure_arc_state: pulumi.Input[Union[_builtins.str, AzureArcState]],
        labor_cost_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        management_settings: Optional[
            pulumi.Input[AzureArcManagementSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureArcState")
    def azure_arc_state(self) -> pulumi.Input[Union[_builtins.str, AzureArcState]]: ...
    @azure_arc_state.setter
    def azure_arc_state(
        self, value: pulumi.Input[Union[_builtins.str, AzureArcState]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="laborCostPercentage")
    def labor_cost_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @labor_cost_percentage.setter
    def labor_cost_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="managementSettings")
    def management_settings(
        self,
    ) -> Optional[pulumi.Input[AzureArcManagementSettingsArgs]]: ...
    @management_settings.setter
    def management_settings(
        self, value: Optional[pulumi.Input[AzureArcManagementSettingsArgs]]
    ): ...

class AzureFileShareHydrationProfileArgsDict(TypedDict):
    azure_file_share_dir_path: NotRequired[pulumi.Input[_builtins.str]]
    azure_file_share_name: NotRequired[pulumi.Input[_builtins.str]]
    azure_file_share_resource_group: NotRequired[pulumi.Input[_builtins.str]]
    azure_file_share_storage_account: NotRequired[pulumi.Input[_builtins.str]]
    azure_file_share_subscription_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureFileShareHydrationProfileArgs:
    def __init__(
        __self__,
        *,
        azure_file_share_dir_path: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_file_share_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_file_share_storage_account: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_file_share_subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareDirPath")
    def azure_file_share_dir_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_file_share_dir_path.setter
    def azure_file_share_dir_path(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareName")
    def azure_file_share_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_file_share_name.setter
    def azure_file_share_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareResourceGroup")
    def azure_file_share_resource_group(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_file_share_resource_group.setter
    def azure_file_share_resource_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareStorageAccount")
    def azure_file_share_storage_account(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_file_share_storage_account.setter
    def azure_file_share_storage_account(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareSubscriptionId")
    def azure_file_share_subscription_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_file_share_subscription_id.setter
    def azure_file_share_subscription_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class AzureSettingsArgsDict(TypedDict):
    currency: pulumi.Input[Union[_builtins.str, BusinessCaseCurrency]]
    target_location: pulumi.Input[_builtins.str]
    avs_labor_cost_percentage: NotRequired[pulumi.Input[_builtins.float]]
    business_case_type: NotRequired[
        pulumi.Input[Union[_builtins.str, MigrationStrategy]]
    ]
    comfort_factor: NotRequired[pulumi.Input[_builtins.float]]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    iaas_labor_cost_percentage: NotRequired[pulumi.Input[_builtins.float]]
    infrastructure_growth_rate: NotRequired[pulumi.Input[_builtins.float]]
    network_cost_percentage: NotRequired[pulumi.Input[_builtins.float]]
    paas_labor_cost_percentage: NotRequired[pulumi.Input[_builtins.float]]
    per_year_migration_completion_percentage: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.float]]]
    ]
    performance_data_end_time: NotRequired[pulumi.Input[_builtins.str]]
    performance_data_start_time: NotRequired[pulumi.Input[_builtins.str]]
    performance_utilization_percentile: NotRequired[pulumi.Input[_builtins.float]]
    savings_option: NotRequired[pulumi.Input[Union[_builtins.str, SavingsOption]]]
    wacc: NotRequired[pulumi.Input[_builtins.float]]
    workload_discovery_source: NotRequired[
        pulumi.Input[Union[_builtins.str, DiscoverySource]]
    ]

@pulumi.input_type
class AzureSettingsArgs:
    def __init__(
        __self__,
        *,
        currency: Optional[
            pulumi.Input[Union[_builtins.str, BusinessCaseCurrency]]
        ] = ...,
        target_location: pulumi.Input[_builtins.str],
        avs_labor_cost_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        business_case_type: Optional[
            pulumi.Input[Union[_builtins.str, MigrationStrategy]]
        ] = ...,
        comfort_factor: Optional[pulumi.Input[_builtins.float]] = ...,
        discount_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        iaas_labor_cost_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        infrastructure_growth_rate: Optional[pulumi.Input[_builtins.float]] = ...,
        network_cost_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        paas_labor_cost_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        per_year_migration_completion_percentage: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.float]]]
        ] = ...,
        performance_data_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_data_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_utilization_percentile: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        savings_option: Optional[
            pulumi.Input[Union[_builtins.str, SavingsOption]]
        ] = ...,
        wacc: Optional[pulumi.Input[_builtins.float]] = ...,
        workload_discovery_source: Optional[
            pulumi.Input[Union[_builtins.str, DiscoverySource]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def currency(self) -> pulumi.Input[Union[_builtins.str, BusinessCaseCurrency]]: ...
    @currency.setter
    def currency(
        self, value: pulumi.Input[Union[_builtins.str, BusinessCaseCurrency]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetLocation")
    def target_location(self) -> pulumi.Input[_builtins.str]: ...
    @target_location.setter
    def target_location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="avsLaborCostPercentage")
    def avs_labor_cost_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @avs_labor_cost_percentage.setter
    def avs_labor_cost_percentage(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="businessCaseType")
    def business_case_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MigrationStrategy]]]: ...
    @business_case_type.setter
    def business_case_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MigrationStrategy]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="comfortFactor")
    def comfort_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @comfort_factor.setter
    def comfort_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="iaasLaborCostPercentage")
    def iaas_labor_cost_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @iaas_labor_cost_percentage.setter
    def iaas_labor_cost_percentage(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureGrowthRate")
    def infrastructure_growth_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @infrastructure_growth_rate.setter
    def infrastructure_growth_rate(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkCostPercentage")
    def network_cost_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @network_cost_percentage.setter
    def network_cost_percentage(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="paasLaborCostPercentage")
    def paas_labor_cost_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @paas_labor_cost_percentage.setter
    def paas_labor_cost_percentage(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="perYearMigrationCompletionPercentage")
    def per_year_migration_completion_percentage(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.float]]]]: ...
    @per_year_migration_completion_percentage.setter
    def per_year_migration_completion_percentage(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.float]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceDataEndTime")
    def performance_data_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performance_data_end_time.setter
    def performance_data_end_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceDataStartTime")
    def performance_data_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performance_data_start_time.setter
    def performance_data_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceUtilizationPercentile")
    def performance_utilization_percentile(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @performance_utilization_percentile.setter
    def performance_utilization_percentile(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="savingsOption")
    def savings_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SavingsOption]]]: ...
    @savings_option.setter
    def savings_option(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SavingsOption]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def wacc(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @wacc.setter
    def wacc(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadDiscoverySource")
    def workload_discovery_source(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiscoverySource]]]: ...
    @workload_discovery_source.setter
    def workload_discovery_source(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiscoverySource]]]
    ): ...

class BillingSettingsArgsDict(TypedDict):
    licensing_program: NotRequired[pulumi.Input[Union[_builtins.str, LicensingProgram]]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BillingSettingsArgs:
    def __init__(
        __self__,
        *,
        licensing_program: Optional[
            pulumi.Input[Union[_builtins.str, LicensingProgram]]
        ] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="licensingProgram")
    def licensing_program(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LicensingProgram]]]: ...
    @licensing_program.setter
    def licensing_program(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LicensingProgram]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BindingArgsDict(TypedDict):
    cert: NotRequired[pulumi.Input[CertArgsDict]]
    host_name: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.str]]
    port_mapping: NotRequired[pulumi.Input[PortMappingArgsDict]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BindingArgs:
    def __init__(
        __self__,
        *,
        cert: Optional[pulumi.Input[CertArgs]] = ...,
        host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.str]] = ...,
        port_mapping: Optional[pulumi.Input[PortMappingArgs]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[CertArgs]]: ...
    @cert.setter
    def cert(self, value: Optional[pulumi.Input[CertArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="portMapping")
    def port_mapping(self) -> Optional[pulumi.Input[PortMappingArgs]]: ...
    @port_mapping.setter
    def port_mapping(self, value: Optional[pulumi.Input[PortMappingArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertArgsDict(TypedDict):
    cert_data: NotRequired[pulumi.Input[_builtins.str]]
    cert_needed: NotRequired[pulumi.Input[_builtins.bool]]
    cert_provided: NotRequired[pulumi.Input[_builtins.bool]]
    secret_store: NotRequired[pulumi.Input[Union[_builtins.str, SecretStoreType]]]

@pulumi.input_type
class CertArgs:
    def __init__(
        __self__,
        *,
        cert_data: Optional[pulumi.Input[_builtins.str]] = ...,
        cert_needed: Optional[pulumi.Input[_builtins.bool]] = ...,
        cert_provided: Optional[pulumi.Input[_builtins.bool]] = ...,
        secret_store: Optional[
            pulumi.Input[Union[_builtins.str, SecretStoreType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certData")
    def cert_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert_data.setter
    def cert_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certNeeded")
    def cert_needed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cert_needed.setter
    def cert_needed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="certProvided")
    def cert_provided(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cert_provided.setter
    def cert_provided(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStore")
    def secret_store(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecretStoreType]]]: ...
    @secret_store.setter
    def secret_store(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecretStoreType]]]
    ): ...

class CollectorAgentPropertiesBaseArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    last_heartbeat_utc: NotRequired[pulumi.Input[_builtins.str]]
    spn_details: NotRequired[pulumi.Input[CollectorAgentSpnPropertiesBaseArgsDict]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CollectorAgentPropertiesBaseArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_heartbeat_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        spn_details: Optional[pulumi.Input[CollectorAgentSpnPropertiesBaseArgs]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_heartbeat_utc.setter
    def last_heartbeat_utc(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="spnDetails")
    def spn_details(
        self,
    ) -> Optional[pulumi.Input[CollectorAgentSpnPropertiesBaseArgs]]: ...
    @spn_details.setter
    def spn_details(
        self, value: Optional[pulumi.Input[CollectorAgentSpnPropertiesBaseArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CollectorAgentPropertiesArgsDict(TypedDict):
    spn_details: NotRequired[pulumi.Input[CollectorBodyAgentSpnPropertiesArgsDict]]

@pulumi.input_type
class CollectorAgentPropertiesArgs:
    def __init__(
        __self__,
        *,
        spn_details: Optional[pulumi.Input[CollectorBodyAgentSpnPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="spnDetails")
    def spn_details(
        self,
    ) -> Optional[pulumi.Input[CollectorBodyAgentSpnPropertiesArgs]]: ...
    @spn_details.setter
    def spn_details(
        self, value: Optional[pulumi.Input[CollectorBodyAgentSpnPropertiesArgs]]
    ): ...

class CollectorAgentSpnPropertiesBaseArgsDict(TypedDict):
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    audience: NotRequired[pulumi.Input[_builtins.str]]
    authority: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CollectorAgentSpnPropertiesBaseArgs:
    def __init__(
        __self__,
        *,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
        authority: Optional[pulumi.Input[_builtins.str]] = ...,
        object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authority.setter
    def authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CollectorBodyAgentSpnPropertiesArgsDict(TypedDict):
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    audience: NotRequired[pulumi.Input[_builtins.str]]
    authority: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CollectorBodyAgentSpnPropertiesArgs:
    def __init__(
        __self__,
        *,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
        authority: Optional[pulumi.Input[_builtins.str]] = ...,
        object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authority.setter
    def authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CollectorPropertiesArgsDict(TypedDict):
    agent_properties: NotRequired[pulumi.Input[CollectorAgentPropertiesArgsDict]]
    discovery_site_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CollectorPropertiesArgs:
    def __init__(
        __self__,
        *,
        agent_properties: Optional[pulumi.Input[CollectorAgentPropertiesArgs]] = ...,
        discovery_site_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentProperties")
    def agent_properties(
        self,
    ) -> Optional[pulumi.Input[CollectorAgentPropertiesArgs]]: ...
    @agent_properties.setter
    def agent_properties(
        self, value: Optional[pulumi.Input[CollectorAgentPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovery_site_id.setter
    def discovery_site_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CompoundAssessmentPropertiesArgsDict(TypedDict):
    target_assessment_arm_ids: pulumi.Input[TargetAssessmentArmIdsArgsDict]
    fallback_machine_assessment_arm_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CompoundAssessmentPropertiesArgs:
    def __init__(
        __self__,
        *,
        target_assessment_arm_ids: pulumi.Input[TargetAssessmentArmIdsArgs],
        fallback_machine_assessment_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetAssessmentArmIds")
    def target_assessment_arm_ids(self) -> pulumi.Input[TargetAssessmentArmIdsArgs]: ...
    @target_assessment_arm_ids.setter
    def target_assessment_arm_ids(
        self, value: pulumi.Input[TargetAssessmentArmIdsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fallbackMachineAssessmentArmId")
    def fallback_machine_assessment_arm_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fallback_machine_assessment_arm_id.setter
    def fallback_machine_assessment_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ComputeSettingsArgsDict(TypedDict):
    hyperthread_core_to_memory_ratio: pulumi.Input[_builtins.float]
    price: pulumi.Input[_builtins.float]
    rhel_linux_server_licensing: pulumi.Input[LinuxServerLicensingSettingsArgsDict]
    sql_server_licensing: pulumi.Input[
        Sequence[pulumi.Input[SqlServerLicensingSettingsArgsDict]]
    ]
    suse_linux_server_licensing: pulumi.Input[LinuxServerLicensingSettingsArgsDict]
    virtualization_software_settings: pulumi.Input[
        VirtualizationSoftwareSettingsArgsDict
    ]
    windows_server_licensing: pulumi.Input[WindowsServerLicensingSettingsArgsDict]

@pulumi.input_type
class ComputeSettingsArgs:
    def __init__(
        __self__,
        *,
        hyperthread_core_to_memory_ratio: pulumi.Input[_builtins.float],
        price: pulumi.Input[_builtins.float],
        rhel_linux_server_licensing: pulumi.Input[LinuxServerLicensingSettingsArgs],
        sql_server_licensing: pulumi.Input[
            Sequence[pulumi.Input[SqlServerLicensingSettingsArgs]]
        ],
        suse_linux_server_licensing: pulumi.Input[LinuxServerLicensingSettingsArgs],
        virtualization_software_settings: pulumi.Input[
            VirtualizationSoftwareSettingsArgs
        ],
        windows_server_licensing: pulumi.Input[WindowsServerLicensingSettingsArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hyperthreadCoreToMemoryRatio")
    def hyperthread_core_to_memory_ratio(self) -> pulumi.Input[_builtins.float]: ...
    @hyperthread_core_to_memory_ratio.setter
    def hyperthread_core_to_memory_ratio(
        self, value: pulumi.Input[_builtins.float]
    ): ...
    @_builtins.property
    @pulumi.getter
    def price(self) -> pulumi.Input[_builtins.float]: ...
    @price.setter
    def price(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="rhelLinuxServerLicensing")
    def rhel_linux_server_licensing(
        self,
    ) -> pulumi.Input[LinuxServerLicensingSettingsArgs]: ...
    @rhel_linux_server_licensing.setter
    def rhel_linux_server_licensing(
        self, value: pulumi.Input[LinuxServerLicensingSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerLicensing")
    def sql_server_licensing(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[SqlServerLicensingSettingsArgs]]]: ...
    @sql_server_licensing.setter
    def sql_server_licensing(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[SqlServerLicensingSettingsArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="suseLinuxServerLicensing")
    def suse_linux_server_licensing(
        self,
    ) -> pulumi.Input[LinuxServerLicensingSettingsArgs]: ...
    @suse_linux_server_licensing.setter
    def suse_linux_server_licensing(
        self, value: pulumi.Input[LinuxServerLicensingSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualizationSoftwareSettings")
    def virtualization_software_settings(
        self,
    ) -> pulumi.Input[VirtualizationSoftwareSettingsArgs]: ...
    @virtualization_software_settings.setter
    def virtualization_software_settings(
        self, value: pulumi.Input[VirtualizationSoftwareSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsServerLicensing")
    def windows_server_licensing(
        self,
    ) -> pulumi.Input[WindowsServerLicensingSettingsArgs]: ...
    @windows_server_licensing.setter
    def windows_server_licensing(
        self, value: pulumi.Input[WindowsServerLicensingSettingsArgs]
    ): ...

class ConnectionStateRequestBodyPropertiesArgsDict(TypedDict):
    private_link_service_connection_state: NotRequired[
        pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]
    ]

@pulumi.input_type
class ConnectionStateRequestBodyPropertiesArgs:
    def __init__(
        __self__,
        *,
        private_link_service_connection_state: Optional[
            pulumi.Input[PrivateLinkServiceConnectionStateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]
    ): ...

class ContainerImagePropertiesArgsDict(TypedDict):
    dockerfile: NotRequired[pulumi.Input[_builtins.str]]
    image_name: NotRequired[pulumi.Input[_builtins.str]]
    image_tag: NotRequired[pulumi.Input[_builtins.str]]
    registry_properties: NotRequired[pulumi.Input[ACRPropertiesArgsDict]]
    run_id: NotRequired[pulumi.Input[_builtins.str]]
    run_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ContainerImagePropertiesArgs:
    def __init__(
        __self__,
        *,
        dockerfile: Optional[pulumi.Input[_builtins.str]] = ...,
        image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_properties: Optional[pulumi.Input[ACRPropertiesArgs]] = ...,
        run_id: Optional[pulumi.Input[_builtins.str]] = ...,
        run_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dockerfile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dockerfile.setter
    def dockerfile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_tag.setter
    def image_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registryProperties")
    def registry_properties(self) -> Optional[pulumi.Input[ACRPropertiesArgs]]: ...
    @registry_properties.setter
    def registry_properties(self, value: Optional[pulumi.Input[ACRPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="runId")
    def run_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_id.setter
    def run_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runStatus")
    def run_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_status.setter
    def run_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DirectoryPathArgsDict(TypedDict):
    physical: NotRequired[pulumi.Input[_builtins.str]]
    virtual: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DirectoryPathArgs:
    def __init__(
        __self__,
        *,
        physical: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def physical(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @physical.setter
    def physical(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def virtual(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual.setter
    def virtual(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DiscoveredEntityLightSummaryArgsDict(TypedDict):
    number_of_machines: pulumi.Input[_builtins.int]
    number_of_servers: pulumi.Input[_builtins.int]
    number_of_web_apps: pulumi.Input[_builtins.int]

@pulumi.input_type
class DiscoveredEntityLightSummaryArgs:
    def __init__(
        __self__,
        *,
        number_of_machines: pulumi.Input[_builtins.int],
        number_of_servers: pulumi.Input[_builtins.int],
        number_of_web_apps: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> pulumi.Input[_builtins.int]: ...
    @number_of_machines.setter
    def number_of_machines(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfServers")
    def number_of_servers(self) -> pulumi.Input[_builtins.int]: ...
    @number_of_servers.setter
    def number_of_servers(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfWebApps")
    def number_of_web_apps(self) -> pulumi.Input[_builtins.int]: ...
    @number_of_web_apps.setter
    def number_of_web_apps(self, value: pulumi.Input[_builtins.int]): ...

class DiskEncryptionSetResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DiskEncryptionSetResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EntityUptimeArgsDict(TypedDict):
    days_per_month: NotRequired[pulumi.Input[_builtins.int]]
    hours_per_day: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class EntityUptimeArgs:
    def __init__(
        __self__,
        *,
        days_per_month: Optional[pulumi.Input[_builtins.int]] = ...,
        hours_per_day: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysPerMonth")
    def days_per_month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @days_per_month.setter
    def days_per_month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="hoursPerDay")
    def hours_per_day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours_per_day.setter
    def hours_per_day(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class FacilitySettingsArgsDict(TypedDict):
    facilities_cost_per_kwh: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class FacilitySettingsArgs:
    def __init__(
        __self__,
        *,
        facilities_cost_per_kwh: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="facilitiesCostPerKwh")
    def facilities_cost_per_kwh(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @facilities_cost_per_kwh.setter
    def facilities_cost_per_kwh(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class GmsaAuthenticationPropertiesArgsDict(TypedDict):
    ad_domain_controller_dns: NotRequired[pulumi.Input[_builtins.str]]
    ad_domain_fqdn: NotRequired[pulumi.Input[_builtins.str]]
    akv_properties: NotRequired[pulumi.Input[KeyVaultSecretStorePropertiesArgsDict]]
    domain_admin_password: NotRequired[pulumi.Input[_builtins.str]]
    domain_admin_username: NotRequired[pulumi.Input[_builtins.str]]
    domain_controller_address: NotRequired[pulumi.Input[_builtins.str]]
    gmsa_account_name: NotRequired[pulumi.Input[_builtins.str]]
    gmsa_user_password: NotRequired[pulumi.Input[_builtins.str]]
    gmsa_username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GmsaAuthenticationPropertiesArgs:
    def __init__(
        __self__,
        *,
        ad_domain_controller_dns: Optional[pulumi.Input[_builtins.str]] = ...,
        ad_domain_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        akv_properties: Optional[pulumi.Input[KeyVaultSecretStorePropertiesArgs]] = ...,
        domain_admin_password: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_admin_username: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_controller_address: Optional[pulumi.Input[_builtins.str]] = ...,
        gmsa_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gmsa_user_password: Optional[pulumi.Input[_builtins.str]] = ...,
        gmsa_username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adDomainControllerDns")
    def ad_domain_controller_dns(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ad_domain_controller_dns.setter
    def ad_domain_controller_dns(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="adDomainFqdn")
    def ad_domain_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ad_domain_fqdn.setter
    def ad_domain_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="akvProperties")
    def akv_properties(
        self,
    ) -> Optional[pulumi.Input[KeyVaultSecretStorePropertiesArgs]]: ...
    @akv_properties.setter
    def akv_properties(
        self, value: Optional[pulumi.Input[KeyVaultSecretStorePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainAdminPassword")
    def domain_admin_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_admin_password.setter
    def domain_admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainAdminUsername")
    def domain_admin_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_admin_username.setter
    def domain_admin_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainControllerAddress")
    def domain_controller_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_controller_address.setter
    def domain_controller_address(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gmsaAccountName")
    def gmsa_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gmsa_account_name.setter
    def gmsa_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gmsaUserPassword")
    def gmsa_user_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gmsa_user_password.setter
    def gmsa_user_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gmsaUsername")
    def gmsa_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gmsa_username.setter
    def gmsa_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupPropertiesArgsDict(TypedDict):
    group_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupPropertiesArgs:
    def __init__(
        __self__, *, group_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_type.setter
    def group_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HeterogeneousAssessmentPropertiesArgsDict(TypedDict):
    assessment_arm_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class HeterogeneousAssessmentPropertiesArgs:
    def __init__(
        __self__,
        *,
        assessment_arm_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentArmIds")
    def assessment_arm_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @assessment_arm_ids.setter
    def assessment_arm_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class HypervLicenseArgsDict(TypedDict):
    license_cost: pulumi.Input[_builtins.float]
    license_type: pulumi.Input[Union[_builtins.str, HyperVLicenseType]]

@pulumi.input_type
class HypervLicenseArgs:
    def __init__(
        __self__,
        *,
        license_cost: pulumi.Input[_builtins.float],
        license_type: pulumi.Input[Union[_builtins.str, HyperVLicenseType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="licenseCost")
    def license_cost(self) -> pulumi.Input[_builtins.float]: ...
    @license_cost.setter
    def license_cost(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Input[Union[_builtins.str, HyperVLicenseType]]: ...
    @license_type.setter
    def license_type(
        self, value: pulumi.Input[Union[_builtins.str, HyperVLicenseType]]
    ): ...

class HypervVirtualizationManagementSettingsArgsDict(TypedDict):
    license_and_support_list: pulumi.Input[
        Sequence[pulumi.Input[HypervLicenseArgsDict]]
    ]
    number_of_physical_cores_per_license: pulumi.Input[_builtins.int]
    software_assurance_cost: pulumi.Input[_builtins.float]

@pulumi.input_type
class HypervVirtualizationManagementSettingsArgs:
    def __init__(
        __self__,
        *,
        license_and_support_list: pulumi.Input[
            Sequence[pulumi.Input[HypervLicenseArgs]]
        ],
        number_of_physical_cores_per_license: pulumi.Input[_builtins.int],
        software_assurance_cost: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="licenseAndSupportList")
    def license_and_support_list(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[HypervLicenseArgs]]]: ...
    @license_and_support_list.setter
    def license_and_support_list(
        self, value: pulumi.Input[Sequence[pulumi.Input[HypervLicenseArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numberOfPhysicalCoresPerLicense")
    def number_of_physical_cores_per_license(self) -> pulumi.Input[_builtins.int]: ...
    @number_of_physical_cores_per_license.setter
    def number_of_physical_cores_per_license(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceCost")
    def software_assurance_cost(self) -> pulumi.Input[_builtins.float]: ...
    @software_assurance_cost.setter
    def software_assurance_cost(self, value: pulumi.Input[_builtins.float]): ...

class IISAKSWorkloadDeploymentModelCustomPropertiesArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    iis_aks_workload_deployment_properties: NotRequired[
        pulumi.Input[IISAKSWorkloadDeploymentArgsDict]
    ]

@pulumi.input_type
class IISAKSWorkloadDeploymentModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        iis_aks_workload_deployment_properties: Optional[
            pulumi.Input[IISAKSWorkloadDeploymentArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="iisAksWorkloadDeploymentProperties")
    def iis_aks_workload_deployment_properties(
        self,
    ) -> Optional[pulumi.Input[IISAKSWorkloadDeploymentArgs]]: ...
    @iis_aks_workload_deployment_properties.setter
    def iis_aks_workload_deployment_properties(
        self, value: Optional[pulumi.Input[IISAKSWorkloadDeploymentArgs]]
    ): ...

class IISAKSWorkloadDeploymentArgsDict(TypedDict):
    authentication_properties: NotRequired[
        pulumi.Input[GmsaAuthenticationPropertiesArgsDict]
    ]
    automation_artifact_properties: NotRequired[
        pulumi.Input[AutomationArtifactArgsDict]
    ]
    bindings: NotRequired[pulumi.Input[Sequence[pulumi.Input[BindingArgsDict]]]]
    build_container_images: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ContainerImagePropertiesArgsDict]]]
    ]
    cluster_properties: NotRequired[pulumi.Input[AKSDeploymentPropertiesArgsDict]]
    configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgsDict]]]
    ]
    container_image_properties: NotRequired[
        pulumi.Input[ContainerImagePropertiesArgsDict]
    ]
    deployment_name_prefix: NotRequired[pulumi.Input[_builtins.str]]
    deployment_spec: NotRequired[pulumi.Input[AKSDeploymentSpecificationArgsDict]]
    directories: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgsDict]]]
    ]
    limits: NotRequired[pulumi.Input[ResourceRequirementsArgsDict]]
    monitoring_properties: NotRequired[
        pulumi.Input[AppInsightMonitoringPropertiesArgsDict]
    ]
    requests: NotRequired[pulumi.Input[ResourceRequirementsArgsDict]]
    target_platform_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IISAKSWorkloadDeploymentArgs:
    def __init__(
        __self__,
        *,
        authentication_properties: Optional[
            pulumi.Input[GmsaAuthenticationPropertiesArgs]
        ] = ...,
        automation_artifact_properties: Optional[
            pulumi.Input[AutomationArtifactArgs]
        ] = ...,
        bindings: Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]] = ...,
        build_container_images: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerImagePropertiesArgs]]]
        ] = ...,
        cluster_properties: Optional[pulumi.Input[AKSDeploymentPropertiesArgs]] = ...,
        configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
        ] = ...,
        container_image_properties: Optional[
            pulumi.Input[ContainerImagePropertiesArgs]
        ] = ...,
        deployment_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_spec: Optional[pulumi.Input[AKSDeploymentSpecificationArgs]] = ...,
        directories: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
        ] = ...,
        limits: Optional[pulumi.Input[ResourceRequirementsArgs]] = ...,
        monitoring_properties: Optional[
            pulumi.Input[AppInsightMonitoringPropertiesArgs]
        ] = ...,
        requests: Optional[pulumi.Input[ResourceRequirementsArgs]] = ...,
        target_platform_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationProperties")
    def authentication_properties(
        self,
    ) -> Optional[pulumi.Input[GmsaAuthenticationPropertiesArgs]]: ...
    @authentication_properties.setter
    def authentication_properties(
        self, value: Optional[pulumi.Input[GmsaAuthenticationPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="automationArtifactProperties")
    def automation_artifact_properties(
        self,
    ) -> Optional[pulumi.Input[AutomationArtifactArgs]]: ...
    @automation_artifact_properties.setter
    def automation_artifact_properties(
        self, value: Optional[pulumi.Input[AutomationArtifactArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def bindings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]]: ...
    @bindings.setter
    def bindings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="buildContainerImages")
    def build_container_images(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ContainerImagePropertiesArgs]]]
    ]: ...
    @build_container_images.setter
    def build_container_images(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerImagePropertiesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterProperties")
    def cluster_properties(
        self,
    ) -> Optional[pulumi.Input[AKSDeploymentPropertiesArgs]]: ...
    @cluster_properties.setter
    def cluster_properties(
        self, value: Optional[pulumi.Input[AKSDeploymentPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
    ]: ...
    @configurations.setter
    def configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerImageProperties")
    def container_image_properties(
        self,
    ) -> Optional[pulumi.Input[ContainerImagePropertiesArgs]]: ...
    @container_image_properties.setter
    def container_image_properties(
        self, value: Optional[pulumi.Input[ContainerImagePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentNamePrefix")
    def deployment_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_name_prefix.setter
    def deployment_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentSpec")
    def deployment_spec(
        self,
    ) -> Optional[pulumi.Input[AKSDeploymentSpecificationArgs]]: ...
    @deployment_spec.setter
    def deployment_spec(
        self, value: Optional[pulumi.Input[AKSDeploymentSpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def directories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
    ]: ...
    @directories.setter
    def directories(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[ResourceRequirementsArgs]]: ...
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[ResourceRequirementsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringProperties")
    def monitoring_properties(
        self,
    ) -> Optional[pulumi.Input[AppInsightMonitoringPropertiesArgs]]: ...
    @monitoring_properties.setter
    def monitoring_properties(
        self, value: Optional[pulumi.Input[AppInsightMonitoringPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[ResourceRequirementsArgs]]: ...
    @requests.setter
    def requests(self, value: Optional[pulumi.Input[ResourceRequirementsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="targetPlatformIdentity")
    def target_platform_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_platform_identity.setter
    def target_platform_identity(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class IISApplicationDetailsArgsDict(TypedDict):
    application_pool_name: NotRequired[pulumi.Input[_builtins.str]]
    directories: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DirectoryPathArgsDict]]]
    ]
    enable32_bit_api_on_win64: NotRequired[pulumi.Input[_builtins.bool]]
    managed_pipeline_mode: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[DirectoryPathArgsDict]]
    runtime_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IISApplicationDetailsArgs:
    def __init__(
        __self__,
        *,
        application_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        directories: Optional[
            pulumi.Input[Sequence[pulumi.Input[DirectoryPathArgs]]]
        ] = ...,
        enable32_bit_api_on_win64: Optional[pulumi.Input[_builtins.bool]] = ...,
        managed_pipeline_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[DirectoryPathArgs]] = ...,
        runtime_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationPoolName")
    def application_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_pool_name.setter
    def application_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def directories(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DirectoryPathArgs]]]]: ...
    @directories.setter
    def directories(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DirectoryPathArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enable32BitApiOnWin64")
    def enable32_bit_api_on_win64(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable32_bit_api_on_win64.setter
    def enable32_bit_api_on_win64(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedPipelineMode")
    def managed_pipeline_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_pipeline_mode.setter
    def managed_pipeline_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[DirectoryPathArgs]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[DirectoryPathArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IISVirtualApplicationDetailsArgsDict(TypedDict):
    directories: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DirectoryPathArgsDict]]]
    ]
    path: NotRequired[pulumi.Input[DirectoryPathArgsDict]]

@pulumi.input_type
class IISVirtualApplicationDetailsArgs:
    def __init__(
        __self__,
        *,
        directories: Optional[
            pulumi.Input[Sequence[pulumi.Input[DirectoryPathArgs]]]
        ] = ...,
        path: Optional[pulumi.Input[DirectoryPathArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def directories(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DirectoryPathArgs]]]]: ...
    @directories.setter
    def directories(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DirectoryPathArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[DirectoryPathArgs]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[DirectoryPathArgs]]): ...

class IISWebApplicationArgsDict(TypedDict):
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    application_name: NotRequired[pulumi.Input[_builtins.str]]
    application_scratch_path: NotRequired[pulumi.Input[_builtins.str]]
    applications: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[IISApplicationDetailsArgsDict]]]
    ]
    bindings: NotRequired[pulumi.Input[Sequence[pulumi.Input[BindingArgsDict]]]]
    configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgsDict]]]
    ]
    directories: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgsDict]]]
    ]
    discovered_frameworks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationFrameworkArgsDict]]]
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    iis_web_server: NotRequired[pulumi.Input[IISWebServerArgsDict]]
    limits: NotRequired[pulumi.Input[ResourceRequirementsArgsDict]]
    path: NotRequired[pulumi.Input[DirectoryPathArgsDict]]
    primary_framework: NotRequired[pulumi.Input[WebApplicationFrameworkArgsDict]]
    requests: NotRequired[pulumi.Input[ResourceRequirementsArgsDict]]
    virtual_applications: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[IISVirtualApplicationDetailsArgsDict]]]
    ]
    web_server_id: NotRequired[pulumi.Input[_builtins.str]]
    web_server_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IISWebApplicationArgs:
    def __init__(
        __self__,
        *,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        application_name: Optional[pulumi.Input[_builtins.str]] = ...,
        application_scratch_path: Optional[pulumi.Input[_builtins.str]] = ...,
        applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[IISApplicationDetailsArgs]]]
        ] = ...,
        bindings: Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]] = ...,
        configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
        ] = ...,
        directories: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
        ] = ...,
        discovered_frameworks: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationFrameworkArgs]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        iis_web_server: Optional[pulumi.Input[IISWebServerArgs]] = ...,
        limits: Optional[pulumi.Input[ResourceRequirementsArgs]] = ...,
        path: Optional[pulumi.Input[DirectoryPathArgs]] = ...,
        primary_framework: Optional[pulumi.Input[WebApplicationFrameworkArgs]] = ...,
        requests: Optional[pulumi.Input[ResourceRequirementsArgs]] = ...,
        virtual_applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[IISVirtualApplicationDetailsArgs]]]
        ] = ...,
        web_server_id: Optional[pulumi.Input[_builtins.str]] = ...,
        web_server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_name.setter
    def application_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationScratchPath")
    def application_scratch_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_scratch_path.setter
    def application_scratch_path(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def applications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IISApplicationDetailsArgs]]]]: ...
    @applications.setter
    def applications(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[IISApplicationDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def bindings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]]: ...
    @bindings.setter
    def bindings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BindingArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
    ]: ...
    @configurations.setter
    def configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def directories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
    ]: ...
    @directories.setter
    def directories(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationDirectoryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveredFrameworks")
    def discovered_frameworks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationFrameworkArgs]]]
    ]: ...
    @discovered_frameworks.setter
    def discovered_frameworks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebApplicationFrameworkArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iisWebServer")
    def iis_web_server(self) -> Optional[pulumi.Input[IISWebServerArgs]]: ...
    @iis_web_server.setter
    def iis_web_server(self, value: Optional[pulumi.Input[IISWebServerArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[ResourceRequirementsArgs]]: ...
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[ResourceRequirementsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[DirectoryPathArgs]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[DirectoryPathArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryFramework")
    def primary_framework(
        self,
    ) -> Optional[pulumi.Input[WebApplicationFrameworkArgs]]: ...
    @primary_framework.setter
    def primary_framework(
        self, value: Optional[pulumi.Input[WebApplicationFrameworkArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[ResourceRequirementsArgs]]: ...
    @requests.setter
    def requests(self, value: Optional[pulumi.Input[ResourceRequirementsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualApplications")
    def virtual_applications(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[IISVirtualApplicationDetailsArgs]]]
    ]: ...
    @virtual_applications.setter
    def virtual_applications(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[IISVirtualApplicationDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webServerId")
    def web_server_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_server_id.setter
    def web_server_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webServerName")
    def web_server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_server_name.setter
    def web_server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IISWebServerArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    machines: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    operating_system_details: NotRequired[pulumi.Input[OperatingSystemDetailsArgsDict]]
    root_configuration_location: NotRequired[pulumi.Input[_builtins.str]]
    run_as_account_id: NotRequired[pulumi.Input[_builtins.str]]
    server_fqdn: NotRequired[pulumi.Input[_builtins.str]]
    server_id: NotRequired[pulumi.Input[_builtins.str]]
    server_name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]
    web_applications: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class IISWebServerArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        machines: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        operating_system_details: Optional[
            pulumi.Input[OperatingSystemDetailsArgs]
        ] = ...,
        root_configuration_location: Optional[pulumi.Input[_builtins.str]] = ...,
        run_as_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        server_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        server_id: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        web_applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_addresses.setter
    def ip_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def machines(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @machines.setter
    def machines(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystemDetails")
    def operating_system_details(
        self,
    ) -> Optional[pulumi.Input[OperatingSystemDetailsArgs]]: ...
    @operating_system_details.setter
    def operating_system_details(
        self, value: Optional[pulumi.Input[OperatingSystemDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rootConfigurationLocation")
    def root_configuration_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_configuration_location.setter
    def root_configuration_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_as_account_id.setter
    def run_as_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverFqdn")
    def server_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_fqdn.setter
    def server_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webApplications")
    def web_applications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @web_applications.setter
    def web_applications(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class IISWorkloadInstanceModelCustomPropertiesArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    fileshare_name: NotRequired[pulumi.Input[_builtins.str]]
    iis_web_application: NotRequired[pulumi.Input[IISWebApplicationArgsDict]]
    web_app_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    web_app_site_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IISWorkloadInstanceModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        fileshare_name: Optional[pulumi.Input[_builtins.str]] = ...,
        iis_web_application: Optional[pulumi.Input[IISWebApplicationArgs]] = ...,
        web_app_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        web_app_site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileshareName")
    def fileshare_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fileshare_name.setter
    def fileshare_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iisWebApplication")
    def iis_web_application(self) -> Optional[pulumi.Input[IISWebApplicationArgs]]: ...
    @iis_web_application.setter
    def iis_web_application(
        self, value: Optional[pulumi.Input[IISWebApplicationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webAppArmId")
    def web_app_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_app_arm_id.setter
    def web_app_arm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webAppSiteName")
    def web_app_site_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_app_site_name.setter
    def web_app_site_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IdentityModelArgsDict(TypedDict):
    aad_authority: NotRequired[pulumi.Input[_builtins.str]]
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    audience: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IdentityModelArgs:
    def __init__(
        __self__,
        *,
        aad_authority: Optional[pulumi.Input[_builtins.str]] = ...,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
        object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadAuthority")
    def aad_authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aad_authority.setter
    def aad_authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IdentityArgsDict(TypedDict):
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]]

@pulumi.input_type
class IdentityArgs:
    def __init__(
        __self__,
        *,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]]
    ): ...

class ImportCollectorPropertiesArgsDict(TypedDict):
    discovery_site_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImportCollectorPropertiesArgs:
    def __init__(
        __self__, *, discovery_site_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovery_site_id.setter
    def discovery_site_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImportSqlCollectorPropertiesArgsDict(TypedDict):
    discovery_site_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImportSqlCollectorPropertiesArgs:
    def __init__(
        __self__, *, discovery_site_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovery_site_id.setter
    def discovery_site_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyVaultResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyVaultSecretStorePropertiesArgsDict(TypedDict):
    keyvault_name: NotRequired[pulumi.Input[_builtins.str]]
    managed_identity_properties: NotRequired[
        pulumi.Input[ManagedIdentityPropertiesArgsDict]
    ]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    secret_store_id: NotRequired[pulumi.Input[_builtins.str]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultSecretStorePropertiesArgs:
    def __init__(
        __self__,
        *,
        keyvault_name: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_identity_properties: Optional[
            pulumi.Input[ManagedIdentityPropertiesArgs]
        ] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyvaultName")
    def keyvault_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keyvault_name.setter
    def keyvault_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedIdentityProperties")
    def managed_identity_properties(
        self,
    ) -> Optional[pulumi.Input[ManagedIdentityPropertiesArgs]]: ...
    @managed_identity_properties.setter
    def managed_identity_properties(
        self, value: Optional[pulumi.Input[ManagedIdentityPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStoreId")
    def secret_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_store_id.setter
    def secret_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LBBackendAddressPoolResourceSettingsArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LBBackendAddressPoolResourceSettingsArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LBFrontendIPConfigurationResourceSettingsArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_allocation_method: NotRequired[pulumi.Input[_builtins.str]]
    subnet: NotRequired[pulumi.Input[SubnetReferenceArgsDict]]
    zones: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LBFrontendIPConfigurationResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_allocation_method: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet: Optional[pulumi.Input[SubnetReferenceArgs]] = ...,
        zones: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIpAllocationMethod")
    def private_ip_allocation_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_allocation_method.setter
    def private_ip_allocation_method(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[SubnetReferenceArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[SubnetReferenceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LaborSettingsArgsDict(TypedDict):
    hourly_admin_cost: pulumi.Input[_builtins.float]
    physical_servers_per_admin: pulumi.Input[_builtins.int]
    virtual_machines_per_admin: pulumi.Input[_builtins.int]

@pulumi.input_type
class LaborSettingsArgs:
    def __init__(
        __self__,
        *,
        hourly_admin_cost: pulumi.Input[_builtins.float],
        physical_servers_per_admin: pulumi.Input[_builtins.int],
        virtual_machines_per_admin: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hourlyAdminCost")
    def hourly_admin_cost(self) -> pulumi.Input[_builtins.float]: ...
    @hourly_admin_cost.setter
    def hourly_admin_cost(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="physicalServersPerAdmin")
    def physical_servers_per_admin(self) -> pulumi.Input[_builtins.int]: ...
    @physical_servers_per_admin.setter
    def physical_servers_per_admin(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachinesPerAdmin")
    def virtual_machines_per_admin(self) -> pulumi.Input[_builtins.int]: ...
    @virtual_machines_per_admin.setter
    def virtual_machines_per_admin(self, value: pulumi.Input[_builtins.int]): ...

class LinuxServerLicensingSettingsArgsDict(TypedDict):
    license_cost: pulumi.Input[_builtins.float]

@pulumi.input_type
class LinuxServerLicensingSettingsArgs:
    def __init__(__self__, *, license_cost: pulumi.Input[_builtins.float]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="licenseCost")
    def license_cost(self) -> pulumi.Input[_builtins.float]: ...
    @license_cost.setter
    def license_cost(self, value: pulumi.Input[_builtins.float]): ...

class LoadBalancerBackendAddressPoolReferenceArgsDict(TypedDict):
    source_arm_resource_id: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LoadBalancerBackendAddressPoolReferenceArgs:
    def __init__(
        __self__,
        *,
        source_arm_resource_id: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceArmResourceId")
    def source_arm_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_arm_resource_id.setter
    def source_arm_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LoadBalancerNatRuleReferenceArgsDict(TypedDict):
    source_arm_resource_id: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LoadBalancerNatRuleReferenceArgs:
    def __init__(
        __self__,
        *,
        source_arm_resource_id: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceArmResourceId")
    def source_arm_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_arm_resource_id.setter
    def source_arm_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LoadBalancerResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    backend_address_pools: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LBBackendAddressPoolResourceSettingsArgsDict]]
        ]
    ]
    frontend_ip_configurations: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LBFrontendIPConfigurationResourceSettingsArgsDict]]
        ]
    ]
    sku: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]
    zones: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LoadBalancerResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        backend_address_pools: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LBBackendAddressPoolResourceSettingsArgs]]
            ]
        ] = ...,
        frontend_ip_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LBFrontendIPConfigurationResourceSettingsArgs]]
            ]
        ] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        zones: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LBBackendAddressPoolResourceSettingsArgs]]]
    ]: ...
    @backend_address_pools.setter
    def backend_address_pools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LBBackendAddressPoolResourceSettingsArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LBFrontendIPConfigurationResourceSettingsArgs]]
        ]
    ]: ...
    @frontend_ip_configurations.setter
    def frontend_ip_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LBFrontendIPConfigurationResourceSettingsArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MachineAssessmentSettingsArgsDict(TypedDict):
    azure_disk_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureDiskType]]]]
    ]
    azure_hybrid_use_benefit: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]
    ]
    azure_location: NotRequired[pulumi.Input[_builtins.str]]
    azure_pricing_tier: NotRequired[
        pulumi.Input[Union[_builtins.str, AzurePricingTier]]
    ]
    azure_security_offering_type: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSecurityOfferingType]]
    ]
    azure_storage_redundancy: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]
    ]
    azure_vm_families: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]
    ]
    azure_vm_security_options: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmSecurityType]]]]
    ]
    billing_settings: NotRequired[pulumi.Input[BillingSettingsArgsDict]]
    currency: NotRequired[pulumi.Input[Union[_builtins.str, AzureCurrency]]]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    environment_type: NotRequired[pulumi.Input[Union[_builtins.str, EnvironmentType]]]
    linux_azure_hybrid_use_benefit: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]
    ]
    performance_data: NotRequired[pulumi.Input[PerformanceDataArgsDict]]
    savings_settings: NotRequired[pulumi.Input[SavingsSettingsArgsDict]]
    scaling_factor: NotRequired[pulumi.Input[_builtins.float]]
    sizing_criterion: NotRequired[
        pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
    ]
    vm_uptime: NotRequired[pulumi.Input[VmUptimeArgsDict]]

@pulumi.input_type
class MachineAssessmentSettingsArgs:
    def __init__(
        __self__,
        *,
        azure_disk_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureDiskType]]]]
        ] = ...,
        azure_hybrid_use_benefit: Optional[
            pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]
        ] = ...,
        azure_location: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_pricing_tier: Optional[
            pulumi.Input[Union[_builtins.str, AzurePricingTier]]
        ] = ...,
        azure_security_offering_type: Optional[
            pulumi.Input[Union[_builtins.str, AzureSecurityOfferingType]]
        ] = ...,
        azure_storage_redundancy: Optional[
            pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]
        ] = ...,
        azure_vm_families: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]
        ] = ...,
        azure_vm_security_options: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AzureVmSecurityType]]]
            ]
        ] = ...,
        billing_settings: Optional[pulumi.Input[BillingSettingsArgs]] = ...,
        currency: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]] = ...,
        discount_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        environment_type: Optional[
            pulumi.Input[Union[_builtins.str, EnvironmentType]]
        ] = ...,
        linux_azure_hybrid_use_benefit: Optional[
            pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]
        ] = ...,
        performance_data: Optional[pulumi.Input[PerformanceDataArgs]] = ...,
        savings_settings: Optional[pulumi.Input[SavingsSettingsArgs]] = ...,
        scaling_factor: Optional[pulumi.Input[_builtins.float]] = ...,
        sizing_criterion: Optional[
            pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
        ] = ...,
        vm_uptime: Optional[pulumi.Input[VmUptimeArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureDiskTypes")
    def azure_disk_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureDiskType]]]]
    ]: ...
    @azure_disk_types.setter
    def azure_disk_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureDiskType]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureHybridUseBenefit")
    def azure_hybrid_use_benefit(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]]: ...
    @azure_hybrid_use_benefit.setter
    def azure_hybrid_use_benefit(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_location.setter
    def azure_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="azurePricingTier")
    def azure_pricing_tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzurePricingTier]]]: ...
    @azure_pricing_tier.setter
    def azure_pricing_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzurePricingTier]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSecurityOfferingType")
    def azure_security_offering_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSecurityOfferingType]]]: ...
    @azure_security_offering_type.setter
    def azure_security_offering_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AzureSecurityOfferingType]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureStorageRedundancy")
    def azure_storage_redundancy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]]: ...
    @azure_storage_redundancy.setter
    def azure_storage_redundancy(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureVmFamilies")
    def azure_vm_families(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]
    ]: ...
    @azure_vm_families.setter
    def azure_vm_families(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureVmSecurityOptions")
    def azure_vm_security_options(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmSecurityType]]]]
    ]: ...
    @azure_vm_security_options.setter
    def azure_vm_security_options(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AzureVmSecurityType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="billingSettings")
    def billing_settings(self) -> Optional[pulumi.Input[BillingSettingsArgs]]: ...
    @billing_settings.setter
    def billing_settings(self, value: Optional[pulumi.Input[BillingSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def currency(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]: ...
    @currency.setter
    def currency(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnvironmentType]]]: ...
    @environment_type.setter
    def environment_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnvironmentType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linuxAzureHybridUseBenefit")
    def linux_azure_hybrid_use_benefit(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]]: ...
    @linux_azure_hybrid_use_benefit.setter
    def linux_azure_hybrid_use_benefit(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> Optional[pulumi.Input[PerformanceDataArgs]]: ...
    @performance_data.setter
    def performance_data(self, value: Optional[pulumi.Input[PerformanceDataArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="savingsSettings")
    def savings_settings(self) -> Optional[pulumi.Input[SavingsSettingsArgs]]: ...
    @savings_settings.setter
    def savings_settings(self, value: Optional[pulumi.Input[SavingsSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @scaling_factor.setter
    def scaling_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]]: ...
    @sizing_criterion.setter
    def sizing_criterion(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmUptime")
    def vm_uptime(self) -> Optional[pulumi.Input[VmUptimeArgs]]: ...
    @vm_uptime.setter
    def vm_uptime(self, value: Optional[pulumi.Input[VmUptimeArgs]]): ...

class MachineAssessmentV2PropertiesArgsDict(TypedDict):
    scope: NotRequired[pulumi.Input[ScopeArgsDict]]
    settings: NotRequired[pulumi.Input[MachineAssessmentSettingsArgsDict]]

@pulumi.input_type
class MachineAssessmentV2PropertiesArgs:
    def __init__(
        __self__,
        *,
        scope: Optional[pulumi.Input[ScopeArgs]] = ...,
        settings: Optional[pulumi.Input[MachineAssessmentSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[ScopeArgs]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[ScopeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[MachineAssessmentSettingsArgs]]: ...
    @settings.setter
    def settings(
        self, value: Optional[pulumi.Input[MachineAssessmentSettingsArgs]]
    ): ...

class ManagedIdentityPropertiesArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    managed_identity_name: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedIdentityPropertiesArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_identity_name: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedIdentityName")
    def managed_identity_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_identity_name.setter
    def managed_identity_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagementSettingsArgsDict(TypedDict):
    hyperv_virtualization_management_settings: pulumi.Input[
        HypervVirtualizationManagementSettingsArgsDict
    ]
    other_management_costs_settings: pulumi.Input[OtherManagementCostsSettingsArgsDict]
    third_party_management_settings: pulumi.Input[ThirdPartyManagementSettingsArgsDict]

@pulumi.input_type
class ManagementSettingsArgs:
    def __init__(
        __self__,
        *,
        hyperv_virtualization_management_settings: pulumi.Input[
            HypervVirtualizationManagementSettingsArgs
        ],
        other_management_costs_settings: pulumi.Input[OtherManagementCostsSettingsArgs],
        third_party_management_settings: pulumi.Input[ThirdPartyManagementSettingsArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hypervVirtualizationManagementSettings")
    def hyperv_virtualization_management_settings(
        self,
    ) -> pulumi.Input[HypervVirtualizationManagementSettingsArgs]: ...
    @hyperv_virtualization_management_settings.setter
    def hyperv_virtualization_management_settings(
        self, value: pulumi.Input[HypervVirtualizationManagementSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="otherManagementCostsSettings")
    def other_management_costs_settings(
        self,
    ) -> pulumi.Input[OtherManagementCostsSettingsArgs]: ...
    @other_management_costs_settings.setter
    def other_management_costs_settings(
        self, value: pulumi.Input[OtherManagementCostsSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="thirdPartyManagementSettings")
    def third_party_management_settings(
        self,
    ) -> pulumi.Input[ThirdPartyManagementSettingsArgs]: ...
    @third_party_management_settings.setter
    def third_party_management_settings(
        self, value: pulumi.Input[ThirdPartyManagementSettingsArgs]
    ): ...

class MigrateAgentModelPropertiesArgsDict(TypedDict):
    authentication_identity: NotRequired[pulumi.Input[IdentityModelArgsDict]]
    custom_properties: NotRequired[
        pulumi.Input[VMwareMigrateAgentModelCustomPropertiesArgsDict]
    ]
    machine_id: NotRequired[pulumi.Input[_builtins.str]]
    machine_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MigrateAgentModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        authentication_identity: Optional[pulumi.Input[IdentityModelArgs]] = ...,
        custom_properties: Optional[
            pulumi.Input[VMwareMigrateAgentModelCustomPropertiesArgs]
        ] = ...,
        machine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationIdentity")
    def authentication_identity(self) -> Optional[pulumi.Input[IdentityModelArgs]]: ...
    @authentication_identity.setter
    def authentication_identity(
        self, value: Optional[pulumi.Input[IdentityModelArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(
        self,
    ) -> Optional[pulumi.Input[VMwareMigrateAgentModelCustomPropertiesArgs]]: ...
    @custom_properties.setter
    def custom_properties(
        self, value: Optional[pulumi.Input[VMwareMigrateAgentModelCustomPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_id.setter
    def machine_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_name.setter
    def machine_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MigrateProjectPropertiesArgsDict(TypedDict):
    provisioning_state: NotRequired[
        pulumi.Input[Union[_builtins.str, ProvisioningState]]
    ]
    public_network_access: NotRequired[pulumi.Input[_builtins.str]]
    registered_tools: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    service_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    utility_storage_account_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MigrateProjectPropertiesArgs:
    def __init__(
        __self__,
        *,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, ProvisioningState]]
        ] = ...,
        public_network_access: Optional[pulumi.Input[_builtins.str]] = ...,
        registered_tools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        utility_storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]: ...
    @provisioning_state.setter
    def provisioning_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registeredTools")
    def registered_tools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @registered_tools.setter
    def registered_tools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_endpoint.setter
    def service_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="utilityStorageAccountId")
    def utility_storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @utility_storage_account_id.setter
    def utility_storage_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class MigrateProjectTagsArgsDict(TypedDict):
    additional_properties: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MigrateProjectTagsArgs:
    def __init__(
        __self__, *, additional_properties: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MigrationConfigurationArgsDict(TypedDict):
    key_vault_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    migration_solution_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MigrationConfigurationArgs:
    def __init__(
        __self__,
        *,
        key_vault_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_solution_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceId")
    def key_vault_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_resource_id.setter
    def key_vault_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="migrationSolutionResourceId")
    def migration_solution_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migration_solution_resource_id.setter
    def migration_solution_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_resource_id.setter
    def storage_account_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class MigrationEntityGroupPropertiesArgsDict(TypedDict):
    application_display_name: pulumi.Input[_builtins.str]
    application_id: pulumi.Input[_builtins.str]
    associated_assessment_id: NotRequired[pulumi.Input[_builtins.str]]
    associated_wave_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    migration_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MigrationEntityGroupPropertiesArgs:
    def __init__(
        __self__,
        *,
        application_display_name: pulumi.Input[_builtins.str],
        application_id: pulumi.Input[_builtins.str],
        associated_assessment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        associated_wave_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        migration_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationDisplayName")
    def application_display_name(self) -> pulumi.Input[_builtins.str]: ...
    @application_display_name.setter
    def application_display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[_builtins.str]: ...
    @application_id.setter
    def application_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="associatedAssessmentId")
    def associated_assessment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @associated_assessment_id.setter
    def associated_assessment_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="associatedWaveIds")
    def associated_wave_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @associated_wave_ids.setter
    def associated_wave_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="migrationPath")
    def migration_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migration_path.setter
    def migration_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MigrationEntityPropertiesArgsDict(TypedDict):
    associated_inventory_resource_id: pulumi.Input[_builtins.str]
    inventory_display_name: pulumi.Input[_builtins.str]
    assessed_entity_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    associated_assessment_id: NotRequired[pulumi.Input[_builtins.str]]
    associated_migration_entity_group_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    associated_wave_id: NotRequired[pulumi.Input[_builtins.str]]
    migration_path: NotRequired[pulumi.Input[_builtins.str]]
    migration_specific_properties: NotRequired[
        pulumi.Input[ServerMigrationSpecificPropertiesArgsDict]
    ]
    migration_tool: NotRequired[pulumi.Input[_builtins.str]]
    partner_resource_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_resource_arm_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MigrationEntityPropertiesArgs:
    def __init__(
        __self__,
        *,
        associated_inventory_resource_id: pulumi.Input[_builtins.str],
        inventory_display_name: pulumi.Input[_builtins.str],
        assessed_entity_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        associated_assessment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        associated_migration_entity_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        associated_wave_id: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_path: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_specific_properties: Optional[
            pulumi.Input[ServerMigrationSpecificPropertiesArgs]
        ] = ...,
        migration_tool: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_resource_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_resource_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associatedInventoryResourceId")
    def associated_inventory_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @associated_inventory_resource_id.setter
    def associated_inventory_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inventoryDisplayName")
    def inventory_display_name(self) -> pulumi.Input[_builtins.str]: ...
    @inventory_display_name.setter
    def inventory_display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assessedEntityArmId")
    def assessed_entity_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @assessed_entity_arm_id.setter
    def assessed_entity_arm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="associatedAssessmentId")
    def associated_assessment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @associated_assessment_id.setter
    def associated_assessment_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="associatedMigrationEntityGroupIds")
    def associated_migration_entity_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @associated_migration_entity_group_ids.setter
    def associated_migration_entity_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="associatedWaveId")
    def associated_wave_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @associated_wave_id.setter
    def associated_wave_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="migrationPath")
    def migration_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migration_path.setter
    def migration_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="migrationSpecificProperties")
    def migration_specific_properties(
        self,
    ) -> Optional[pulumi.Input[ServerMigrationSpecificPropertiesArgs]]: ...
    @migration_specific_properties.setter
    def migration_specific_properties(
        self, value: Optional[pulumi.Input[ServerMigrationSpecificPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="migrationTool")
    def migration_tool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migration_tool.setter
    def migration_tool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partnerResourceArmId")
    def partner_resource_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_resource_arm_id.setter
    def partner_resource_arm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureResourceArmId")
    def target_azure_resource_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_resource_arm_id.setter
    def target_azure_resource_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ModernizeProjectModelPropertiesArgsDict(TypedDict):
    migration_configuration: NotRequired[pulumi.Input[MigrationConfigurationArgsDict]]

@pulumi.input_type
class ModernizeProjectModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        migration_configuration: Optional[
            pulumi.Input[MigrationConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="migrationConfiguration")
    def migration_configuration(
        self,
    ) -> Optional[pulumi.Input[MigrationConfigurationArgs]]: ...
    @migration_configuration.setter
    def migration_configuration(
        self, value: Optional[pulumi.Input[MigrationConfigurationArgs]]
    ): ...

class MoveCollectionPropertiesArgsDict(TypedDict):
    move_region: NotRequired[pulumi.Input[_builtins.str]]
    move_type: NotRequired[pulumi.Input[Union[_builtins.str, MoveType]]]
    source_region: NotRequired[pulumi.Input[_builtins.str]]
    target_region: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MoveCollectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        move_region: Optional[pulumi.Input[_builtins.str]] = ...,
        move_type: Optional[pulumi.Input[Union[_builtins.str, MoveType]]] = ...,
        source_region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_region: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="moveRegion")
    def move_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @move_region.setter
    def move_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="moveType")
    def move_type(self) -> Optional[pulumi.Input[Union[_builtins.str, MoveType]]]: ...
    @move_type.setter
    def move_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MoveType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceRegion")
    def source_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_region.setter
    def source_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetRegion")
    def target_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_region.setter
    def target_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MoveResourceDependencyOverrideArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    target_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MoveResourceDependencyOverrideArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MoveResourcePropertiesArgsDict(TypedDict):
    source_id: pulumi.Input[_builtins.str]
    depends_on_overrides: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[MoveResourceDependencyOverrideArgsDict]]]
    ]
    existing_target_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_settings: NotRequired[
        pulumi.Input[
            Union[
                AvailabilitySetResourceSettingsArgsDict,
                DiskEncryptionSetResourceSettingsArgsDict,
                KeyVaultResourceSettingsArgsDict,
                LoadBalancerResourceSettingsArgsDict,
                NetworkInterfaceResourceSettingsArgsDict,
                NetworkSecurityGroupResourceSettingsArgsDict,
                PublicIPAddressResourceSettingsArgsDict,
                ResourceGroupResourceSettingsArgsDict,
                SqlDatabaseResourceSettingsArgsDict,
                SqlElasticPoolResourceSettingsArgsDict,
                SqlServerResourceSettingsArgsDict,
                VirtualMachineResourceSettingsArgsDict,
                VirtualNetworkResourceSettingsArgsDict,
            ]
        ]
    ]

@pulumi.input_type
class MoveResourcePropertiesArgs:
    def __init__(
        __self__,
        *,
        source_id: pulumi.Input[_builtins.str],
        depends_on_overrides: Optional[
            pulumi.Input[Sequence[pulumi.Input[MoveResourceDependencyOverrideArgs]]]
        ] = ...,
        existing_target_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_settings: Optional[
            pulumi.Input[
                Union[
                    AvailabilitySetResourceSettingsArgs,
                    DiskEncryptionSetResourceSettingsArgs,
                    KeyVaultResourceSettingsArgs,
                    LoadBalancerResourceSettingsArgs,
                    NetworkInterfaceResourceSettingsArgs,
                    NetworkSecurityGroupResourceSettingsArgs,
                    PublicIPAddressResourceSettingsArgs,
                    ResourceGroupResourceSettingsArgs,
                    SqlDatabaseResourceSettingsArgs,
                    SqlElasticPoolResourceSettingsArgs,
                    SqlServerResourceSettingsArgs,
                    VirtualMachineResourceSettingsArgs,
                    VirtualNetworkResourceSettingsArgs,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_id.setter
    def source_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dependsOnOverrides")
    def depends_on_overrides(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MoveResourceDependencyOverrideArgs]]]
    ]: ...
    @depends_on_overrides.setter
    def depends_on_overrides(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MoveResourceDependencyOverrideArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="existingTargetId")
    def existing_target_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @existing_target_id.setter
    def existing_target_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceSettings")
    def resource_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AvailabilitySetResourceSettingsArgs,
                DiskEncryptionSetResourceSettingsArgs,
                KeyVaultResourceSettingsArgs,
                LoadBalancerResourceSettingsArgs,
                NetworkInterfaceResourceSettingsArgs,
                NetworkSecurityGroupResourceSettingsArgs,
                PublicIPAddressResourceSettingsArgs,
                ResourceGroupResourceSettingsArgs,
                SqlDatabaseResourceSettingsArgs,
                SqlElasticPoolResourceSettingsArgs,
                SqlServerResourceSettingsArgs,
                VirtualMachineResourceSettingsArgs,
                VirtualNetworkResourceSettingsArgs,
            ]
        ]
    ]: ...
    @resource_settings.setter
    def resource_settings(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AvailabilitySetResourceSettingsArgs,
                    DiskEncryptionSetResourceSettingsArgs,
                    KeyVaultResourceSettingsArgs,
                    LoadBalancerResourceSettingsArgs,
                    NetworkInterfaceResourceSettingsArgs,
                    NetworkSecurityGroupResourceSettingsArgs,
                    PublicIPAddressResourceSettingsArgs,
                    ResourceGroupResourceSettingsArgs,
                    SqlDatabaseResourceSettingsArgs,
                    SqlElasticPoolResourceSettingsArgs,
                    SqlServerResourceSettingsArgs,
                    VirtualMachineResourceSettingsArgs,
                    VirtualNetworkResourceSettingsArgs,
                ]
            ]
        ],
    ): ...

class NetworkInterfaceResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    enable_accelerated_networking: NotRequired[pulumi.Input[_builtins.bool]]
    ip_configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NicIpConfigurationResourceSettingsArgsDict]]]
    ]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkInterfaceResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        enable_accelerated_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[NicIpConfigurationResourceSettingsArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NicIpConfigurationResourceSettingsArgs]]]
    ]: ...
    @ip_configurations.setter
    def ip_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NicIpConfigurationResourceSettingsArgs]]]
        ],
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
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkSecurityGroupResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    security_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NsgSecurityRuleArgsDict]]]
    ]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkSecurityGroupResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        security_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[NsgSecurityRuleArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="securityRules")
    def security_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NsgSecurityRuleArgs]]]]: ...
    @security_rules.setter
    def security_rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NsgSecurityRuleArgs]]]]
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
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkSettingsArgsDict(TypedDict):
    hardware_software_cost_percentage: pulumi.Input[_builtins.float]
    maintenance_cost_percentage: pulumi.Input[_builtins.float]

@pulumi.input_type
class NetworkSettingsArgs:
    def __init__(
        __self__,
        *,
        hardware_software_cost_percentage: pulumi.Input[_builtins.float],
        maintenance_cost_percentage: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hardwareSoftwareCostPercentage")
    def hardware_software_cost_percentage(self) -> pulumi.Input[_builtins.float]: ...
    @hardware_software_cost_percentage.setter
    def hardware_software_cost_percentage(
        self, value: pulumi.Input[_builtins.float]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceCostPercentage")
    def maintenance_cost_percentage(self) -> pulumi.Input[_builtins.float]: ...
    @maintenance_cost_percentage.setter
    def maintenance_cost_percentage(self, value: pulumi.Input[_builtins.float]): ...

class NicIpConfigurationResourceSettingsArgsDict(TypedDict):
    load_balancer_backend_address_pools: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LoadBalancerBackendAddressPoolReferenceArgsDict]]
        ]
    ]
    load_balancer_nat_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LoadBalancerNatRuleReferenceArgsDict]]]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    primary: NotRequired[pulumi.Input[_builtins.bool]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_allocation_method: NotRequired[pulumi.Input[_builtins.str]]
    public_ip: NotRequired[pulumi.Input[PublicIpReferenceArgsDict]]
    subnet: NotRequired[pulumi.Input[SubnetReferenceArgsDict]]

@pulumi.input_type
class NicIpConfigurationResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        load_balancer_backend_address_pools: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LoadBalancerBackendAddressPoolReferenceArgs]]
            ]
        ] = ...,
        load_balancer_nat_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoadBalancerNatRuleReferenceArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary: Optional[pulumi.Input[_builtins.bool]] = ...,
        private_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_allocation_method: Optional[pulumi.Input[_builtins.str]] = ...,
        public_ip: Optional[pulumi.Input[PublicIpReferenceArgs]] = ...,
        subnet: Optional[pulumi.Input[SubnetReferenceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPools")
    def load_balancer_backend_address_pools(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LoadBalancerBackendAddressPoolReferenceArgs]]
        ]
    ]: ...
    @load_balancer_backend_address_pools.setter
    def load_balancer_backend_address_pools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LoadBalancerBackendAddressPoolReferenceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerNatRules")
    def load_balancer_nat_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LoadBalancerNatRuleReferenceArgs]]]
    ]: ...
    @load_balancer_nat_rules.setter
    def load_balancer_nat_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoadBalancerNatRuleReferenceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIpAllocationMethod")
    def private_ip_allocation_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_allocation_method.setter
    def private_ip_allocation_method(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[pulumi.Input[PublicIpReferenceArgs]]: ...
    @public_ip.setter
    def public_ip(self, value: Optional[pulumi.Input[PublicIpReferenceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[SubnetReferenceArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[SubnetReferenceArgs]]): ...

class NsgReferenceArgsDict(TypedDict):
    source_arm_resource_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class NsgReferenceArgs:
    def __init__(
        __self__, *, source_arm_resource_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceArmResourceId")
    def source_arm_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_arm_resource_id.setter
    def source_arm_resource_id(self, value: pulumi.Input[_builtins.str]): ...

class NsgSecurityRuleArgsDict(TypedDict):
    access: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    destination_address_prefix: NotRequired[pulumi.Input[_builtins.str]]
    destination_port_range: NotRequired[pulumi.Input[_builtins.str]]
    direction: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    source_address_prefix: NotRequired[pulumi.Input[_builtins.str]]
    source_port_range: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NsgSecurityRuleArgs:
    def __init__(
        __self__,
        *,
        access: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_address_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_port_range: Optional[pulumi.Input[_builtins.str]] = ...,
        direction: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        source_address_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        source_port_range: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access.setter
    def access(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationAddressPrefix")
    def destination_address_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_address_prefix.setter
    def destination_address_prefix(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_port_range.setter
    def destination_port_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefix")
    def source_address_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_address_prefix.setter
    def source_address_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_port_range.setter
    def source_port_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OnPremiseSettingsArgsDict(TypedDict):
    compute_settings: pulumi.Input[ComputeSettingsArgsDict]
    facility_settings: pulumi.Input[FacilitySettingsArgsDict]
    labor_settings: pulumi.Input[LaborSettingsArgsDict]
    network_settings: pulumi.Input[NetworkSettingsArgsDict]
    security_settings: pulumi.Input[SecuritySettingsArgsDict]
    storage_settings: pulumi.Input[StorageSettingsArgsDict]
    management_settings: NotRequired[pulumi.Input[ManagementSettingsArgsDict]]

@pulumi.input_type
class OnPremiseSettingsArgs:
    def __init__(
        __self__,
        *,
        compute_settings: pulumi.Input[ComputeSettingsArgs],
        facility_settings: pulumi.Input[FacilitySettingsArgs],
        labor_settings: pulumi.Input[LaborSettingsArgs],
        network_settings: pulumi.Input[NetworkSettingsArgs],
        security_settings: pulumi.Input[SecuritySettingsArgs],
        storage_settings: pulumi.Input[StorageSettingsArgs],
        management_settings: Optional[pulumi.Input[ManagementSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeSettings")
    def compute_settings(self) -> pulumi.Input[ComputeSettingsArgs]: ...
    @compute_settings.setter
    def compute_settings(self, value: pulumi.Input[ComputeSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="facilitySettings")
    def facility_settings(self) -> pulumi.Input[FacilitySettingsArgs]: ...
    @facility_settings.setter
    def facility_settings(self, value: pulumi.Input[FacilitySettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="laborSettings")
    def labor_settings(self) -> pulumi.Input[LaborSettingsArgs]: ...
    @labor_settings.setter
    def labor_settings(self, value: pulumi.Input[LaborSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> pulumi.Input[NetworkSettingsArgs]: ...
    @network_settings.setter
    def network_settings(self, value: pulumi.Input[NetworkSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> pulumi.Input[SecuritySettingsArgs]: ...
    @security_settings.setter
    def security_settings(self, value: pulumi.Input[SecuritySettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="storageSettings")
    def storage_settings(self) -> pulumi.Input[StorageSettingsArgs]: ...
    @storage_settings.setter
    def storage_settings(self, value: pulumi.Input[StorageSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="managementSettings")
    def management_settings(self) -> Optional[pulumi.Input[ManagementSettingsArgs]]: ...
    @management_settings.setter
    def management_settings(
        self, value: Optional[pulumi.Input[ManagementSettingsArgs]]
    ): ...

class OperatingSystemDetailsArgsDict(TypedDict):
    os: NotRequired[pulumi.Input[Union[_builtins.str, OperatingSystemType]]]
    os_architecture: NotRequired[pulumi.Input[_builtins.str]]
    os_name: NotRequired[pulumi.Input[_builtins.str]]
    os_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OperatingSystemDetailsArgs:
    def __init__(
        __self__,
        *,
        os: Optional[pulumi.Input[Union[_builtins.str, OperatingSystemType]]] = ...,
        os_architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        os_name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def os(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OperatingSystemType]]]: ...
    @os.setter
    def os(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OperatingSystemType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osArchitecture")
    def os_architecture(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_architecture.setter
    def os_architecture(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_name.setter
    def os_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OtherManagementCostsSettingsArgsDict(TypedDict):
    data_protection_cost_per_server_per_year: pulumi.Input[_builtins.float]
    monitoring_cost_per_server_per_year: pulumi.Input[_builtins.float]
    patching_cost_per_server_per_year: pulumi.Input[_builtins.float]

@pulumi.input_type
class OtherManagementCostsSettingsArgs:
    def __init__(
        __self__,
        *,
        data_protection_cost_per_server_per_year: pulumi.Input[_builtins.float],
        monitoring_cost_per_server_per_year: pulumi.Input[_builtins.float],
        patching_cost_per_server_per_year: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataProtectionCostPerServerPerYear")
    def data_protection_cost_per_server_per_year(
        self,
    ) -> pulumi.Input[_builtins.float]: ...
    @data_protection_cost_per_server_per_year.setter
    def data_protection_cost_per_server_per_year(
        self, value: pulumi.Input[_builtins.float]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringCostPerServerPerYear")
    def monitoring_cost_per_server_per_year(self) -> pulumi.Input[_builtins.float]: ...
    @monitoring_cost_per_server_per_year.setter
    def monitoring_cost_per_server_per_year(
        self, value: pulumi.Input[_builtins.float]
    ): ...
    @_builtins.property
    @pulumi.getter(name="patchingCostPerServerPerYear")
    def patching_cost_per_server_per_year(self) -> pulumi.Input[_builtins.float]: ...
    @patching_cost_per_server_per_year.setter
    def patching_cost_per_server_per_year(
        self, value: pulumi.Input[_builtins.float]
    ): ...

class PerfDataSettingsArgsDict(TypedDict):
    percentile: pulumi.Input[Union[_builtins.str, Percentile]]
    time_range: pulumi.Input[Union[_builtins.str, TimeRange]]
    perf_data_end_time: NotRequired[pulumi.Input[_builtins.str]]
    perf_data_start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PerfDataSettingsArgs:
    def __init__(
        __self__,
        *,
        percentile: pulumi.Input[Union[_builtins.str, Percentile]],
        time_range: pulumi.Input[Union[_builtins.str, TimeRange]],
        perf_data_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        perf_data_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percentile(self) -> pulumi.Input[Union[_builtins.str, Percentile]]: ...
    @percentile.setter
    def percentile(self, value: pulumi.Input[Union[_builtins.str, Percentile]]): ...
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> pulumi.Input[Union[_builtins.str, TimeRange]]: ...
    @time_range.setter
    def time_range(self, value: pulumi.Input[Union[_builtins.str, TimeRange]]): ...
    @_builtins.property
    @pulumi.getter(name="perfDataEndTime")
    def perf_data_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @perf_data_end_time.setter
    def perf_data_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="perfDataStartTime")
    def perf_data_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @perf_data_start_time.setter
    def perf_data_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PerformanceDataArgsDict(TypedDict):
    percentile: NotRequired[pulumi.Input[Union[_builtins.str, Percentile]]]
    perf_data_end_time: NotRequired[pulumi.Input[_builtins.str]]
    perf_data_start_time: NotRequired[pulumi.Input[_builtins.str]]
    time_range: NotRequired[pulumi.Input[Union[_builtins.str, TimeRange]]]

@pulumi.input_type
class PerformanceDataArgs:
    def __init__(
        __self__,
        *,
        percentile: Optional[pulumi.Input[Union[_builtins.str, Percentile]]] = ...,
        perf_data_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        perf_data_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        time_range: Optional[pulumi.Input[Union[_builtins.str, TimeRange]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percentile(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, Percentile]]]: ...
    @percentile.setter
    def percentile(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Percentile]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="perfDataEndTime")
    def perf_data_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @perf_data_end_time.setter
    def perf_data_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="perfDataStartTime")
    def perf_data_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @perf_data_start_time.setter
    def perf_data_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[pulumi.Input[Union[_builtins.str, TimeRange]]]: ...
    @time_range.setter
    def time_range(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TimeRange]]]
    ): ...

class PortMappingArgsDict(TypedDict):
    external_port: NotRequired[pulumi.Input[_builtins.int]]
    internal_port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class PortMappingArgs:
    def __init__(
        __self__,
        *,
        external_port: Optional[pulumi.Input[_builtins.int]] = ...,
        internal_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalPort")
    def external_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @external_port.setter
    def external_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="internalPort")
    def internal_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @internal_port.setter
    def internal_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PrivateEndpointConnectionPropertiesArgsDict(TypedDict):
    private_link_service_connection_state: NotRequired[
        pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]
    ]

@pulumi.input_type
class PrivateEndpointConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        private_link_service_connection_state: Optional[
            pulumi.Input[PrivateLinkServiceConnectionStateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]
    ): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[
            Union[_builtins.str, PrivateEndpointServiceConnectionStatus, Status]
        ]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[
                Union[_builtins.str, PrivateEndpointServiceConnectionStatus, Status]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[_builtins.str, PrivateEndpointServiceConnectionStatus, Status]
        ]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[
                Union[_builtins.str, PrivateEndpointServiceConnectionStatus, Status]
            ]
        ],
    ): ...

class ProjectPropertiesArgsDict(TypedDict):
    assessment_solution_id: NotRequired[pulumi.Input[_builtins.str]]
    customer_storage_account_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    customer_workspace_id: NotRequired[pulumi.Input[_builtins.str]]
    customer_workspace_location: NotRequired[pulumi.Input[_builtins.str]]
    project_status: NotRequired[pulumi.Input[Union[_builtins.str, ProjectStatus]]]
    public_network_access: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectPropertiesArgs:
    def __init__(
        __self__,
        *,
        assessment_solution_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_storage_account_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_workspace_location: Optional[pulumi.Input[_builtins.str]] = ...,
        project_status: Optional[
            pulumi.Input[Union[_builtins.str, ProjectStatus]]
        ] = ...,
        public_network_access: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentSolutionId")
    def assessment_solution_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @assessment_solution_id.setter
    def assessment_solution_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerStorageAccountArmId")
    def customer_storage_account_arm_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_storage_account_arm_id.setter
    def customer_storage_account_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerWorkspaceId")
    def customer_workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_workspace_id.setter
    def customer_workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerWorkspaceLocation")
    def customer_workspace_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_workspace_location.setter
    def customer_workspace_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="projectStatus")
    def project_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProjectStatus]]]: ...
    @project_status.setter
    def project_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProjectStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PublicIPAddressResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    domain_name_label: NotRequired[pulumi.Input[_builtins.str]]
    fqdn: NotRequired[pulumi.Input[_builtins.str]]
    public_ip_allocation_method: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]
    zones: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PublicIPAddressResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        domain_name_label: Optional[pulumi.Input[_builtins.str]] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        public_ip_allocation_method: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        zones: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainNameLabel")
    def domain_name_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name_label.setter
    def domain_name_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIpAllocationMethod")
    def public_ip_allocation_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ip_allocation_method.setter
    def public_ip_allocation_method(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PublicIpReferenceArgsDict(TypedDict):
    source_arm_resource_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class PublicIpReferenceArgs:
    def __init__(
        __self__, *, source_arm_resource_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceArmResourceId")
    def source_arm_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_arm_resource_id.setter
    def source_arm_resource_id(self, value: pulumi.Input[_builtins.str]): ...

class ResourceGroupResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceGroupResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceIdentityArgsDict(TypedDict):
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ResourceIdentityTypes]]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgsDict]]]
    ]

@pulumi.input_type
class ResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityTypes]]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityTypes]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityTypes]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
    ]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
        ],
    ): ...

class ResourceRequirementsArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.str]]
    memory: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceRequirementsArgs:
    def __init__(
        __self__,
        *,
        cpu: Optional[pulumi.Input[_builtins.str]] = ...,
        memory: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SavingsSettingsArgsDict(TypedDict):
    azure_offer_code: NotRequired[pulumi.Input[Union[_builtins.str, AzureOffer]]]
    savings_options: NotRequired[pulumi.Input[Union[_builtins.str, SavingsOptions]]]

@pulumi.input_type
class SavingsSettingsArgs:
    def __init__(
        __self__,
        *,
        azure_offer_code: Optional[
            pulumi.Input[Union[_builtins.str, AzureOffer]]
        ] = ...,
        savings_options: Optional[
            pulumi.Input[Union[_builtins.str, SavingsOptions]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureOffer]]]: ...
    @azure_offer_code.setter
    def azure_offer_code(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureOffer]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="savingsOptions")
    def savings_options(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SavingsOptions]]]: ...
    @savings_options.setter
    def savings_options(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SavingsOptions]]]
    ): ...

class ScopeArgsDict(TypedDict):
    azure_resource_graph_query: NotRequired[pulumi.Input[_builtins.str]]
    scope_type: NotRequired[pulumi.Input[Union[_builtins.str, ScopeType]]]
    server_group_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScopeArgs:
    def __init__(
        __self__,
        *,
        azure_resource_graph_query: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_type: Optional[pulumi.Input[Union[_builtins.str, ScopeType]]] = ...,
        server_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureResourceGraphQuery")
    def azure_resource_graph_query(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_resource_graph_query.setter
    def azure_resource_graph_query(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scopeType")
    def scope_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ScopeType]]]: ...
    @scope_type.setter
    def scope_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ScopeType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverGroupId")
    def server_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_group_id.setter
    def server_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecretStoreDetailsArgsDict(TypedDict):
    secret_store: NotRequired[pulumi.Input[Union[_builtins.str, SecretStoreType]]]
    secret_store_properties: NotRequired[pulumi.Input[SecretStorePropertiesArgsDict]]

@pulumi.input_type
class SecretStoreDetailsArgs:
    def __init__(
        __self__,
        *,
        secret_store: Optional[
            pulumi.Input[Union[_builtins.str, SecretStoreType]]
        ] = ...,
        secret_store_properties: Optional[
            pulumi.Input[SecretStorePropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretStore")
    def secret_store(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecretStoreType]]]: ...
    @secret_store.setter
    def secret_store(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecretStoreType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretStoreProperties")
    def secret_store_properties(
        self,
    ) -> Optional[pulumi.Input[SecretStorePropertiesArgs]]: ...
    @secret_store_properties.setter
    def secret_store_properties(
        self, value: Optional[pulumi.Input[SecretStorePropertiesArgs]]
    ): ...

class SecretStorePropertiesArgsDict(TypedDict):
    secret_store_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecretStorePropertiesArgs:
    def __init__(
        __self__, *, secret_store_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretStoreId")
    def secret_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_store_id.setter
    def secret_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecuritySettingsArgsDict(TypedDict):
    server_security_cost_per_server_per_year: pulumi.Input[_builtins.float]
    sql_server_security_cost_per_server_per_year: pulumi.Input[_builtins.float]

@pulumi.input_type
class SecuritySettingsArgs:
    def __init__(
        __self__,
        *,
        server_security_cost_per_server_per_year: pulumi.Input[_builtins.float],
        sql_server_security_cost_per_server_per_year: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverSecurityCostPerServerPerYear")
    def server_security_cost_per_server_per_year(
        self,
    ) -> pulumi.Input[_builtins.float]: ...
    @server_security_cost_per_server_per_year.setter
    def server_security_cost_per_server_per_year(
        self, value: pulumi.Input[_builtins.float]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerSecurityCostPerServerPerYear")
    def sql_server_security_cost_per_server_per_year(
        self,
    ) -> pulumi.Input[_builtins.float]: ...
    @sql_server_security_cost_per_server_per_year.setter
    def sql_server_security_cost_per_server_per_year(
        self, value: pulumi.Input[_builtins.float]
    ): ...

class ServerMigrationSpecificPropertiesArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    current_job_id: NotRequired[pulumi.Input[_builtins.str]]
    dr_appliance_inventory_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServerMigrationSpecificPropertiesArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        current_job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dr_appliance_inventory_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="currentJobId")
    def current_job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @current_job_id.setter
    def current_job_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="drApplianceInventoryId")
    def dr_appliance_inventory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dr_appliance_inventory_id.setter
    def dr_appliance_inventory_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class SettingsArgsDict(TypedDict):
    azure_settings: pulumi.Input[AzureSettingsArgsDict]
    azure_arc_settings: NotRequired[pulumi.Input[AzureArcSettingsArgsDict]]
    on_premise_settings: NotRequired[pulumi.Input[OnPremiseSettingsArgsDict]]

@pulumi.input_type
class SettingsArgs:
    def __init__(
        __self__,
        *,
        azure_settings: pulumi.Input[AzureSettingsArgs],
        azure_arc_settings: Optional[pulumi.Input[AzureArcSettingsArgs]] = ...,
        on_premise_settings: Optional[pulumi.Input[OnPremiseSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureSettings")
    def azure_settings(self) -> pulumi.Input[AzureSettingsArgs]: ...
    @azure_settings.setter
    def azure_settings(self, value: pulumi.Input[AzureSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="azureArcSettings")
    def azure_arc_settings(self) -> Optional[pulumi.Input[AzureArcSettingsArgs]]: ...
    @azure_arc_settings.setter
    def azure_arc_settings(
        self, value: Optional[pulumi.Input[AzureArcSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onPremiseSettings")
    def on_premise_settings(self) -> Optional[pulumi.Input[OnPremiseSettingsArgs]]: ...
    @on_premise_settings.setter
    def on_premise_settings(
        self, value: Optional[pulumi.Input[OnPremiseSettingsArgs]]
    ): ...

class SolutionDetailsArgsDict(TypedDict):
    assessment_count: NotRequired[pulumi.Input[_builtins.int]]
    extended_details: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    group_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class SolutionDetailsArgs:
    def __init__(
        __self__,
        *,
        assessment_count: Optional[pulumi.Input[_builtins.int]] = ...,
        extended_details: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        group_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentCount")
    def assessment_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @assessment_count.setter
    def assessment_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedDetails")
    def extended_details(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @extended_details.setter
    def extended_details(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="groupCount")
    def group_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @group_count.setter
    def group_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class SolutionPropertiesArgsDict(TypedDict):
    cleanup_state: NotRequired[pulumi.Input[_builtins.str]]
    details: NotRequired[pulumi.Input[SolutionDetailsArgsDict]]
    goal: NotRequired[pulumi.Input[_builtins.str]]
    purpose: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    tool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SolutionPropertiesArgs:
    def __init__(
        __self__,
        *,
        cleanup_state: Optional[pulumi.Input[_builtins.str]] = ...,
        details: Optional[pulumi.Input[SolutionDetailsArgs]] = ...,
        goal: Optional[pulumi.Input[_builtins.str]] = ...,
        purpose: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cleanupState")
    def cleanup_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cleanup_state.setter
    def cleanup_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[SolutionDetailsArgs]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[SolutionDetailsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def goal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @goal.setter
    def goal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tool.setter
    def tool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SqlAssessmentSettingsArgsDict(TypedDict):
    async_commit_mode_intent: NotRequired[
        pulumi.Input[Union[_builtins.str, AsyncCommitModeIntent]]
    ]
    azure_location: NotRequired[pulumi.Input[_builtins.str]]
    azure_security_offering_type: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSecurityOfferingType]]
    ]
    azure_sql_database_settings: NotRequired[pulumi.Input[SqlDbSettingsV3ArgsDict]]
    azure_sql_managed_instance_settings: NotRequired[
        pulumi.Input[SqlMiSettingsV3ArgsDict]
    ]
    azure_sql_vm_settings: NotRequired[pulumi.Input[SqlVmSettingsArgsDict]]
    billing_settings: NotRequired[pulumi.Input[BillingSettingsArgsDict]]
    currency: NotRequired[pulumi.Input[Union[_builtins.str, AzureCurrency]]]
    disaster_recovery_location: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureLocation]]
    ]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    enable_hadr_assessment: NotRequired[pulumi.Input[_builtins.bool]]
    entity_uptime: NotRequired[pulumi.Input[EntityUptimeArgsDict]]
    environment_type: NotRequired[pulumi.Input[Union[_builtins.str, EnvironmentType]]]
    is_internet_access_available: NotRequired[pulumi.Input[_builtins.bool]]
    multi_subnet_intent: NotRequired[
        pulumi.Input[Union[_builtins.str, MultiSubnetIntent]]
    ]
    os_license: NotRequired[pulumi.Input[Union[_builtins.str, OsLicense]]]
    performance_data: NotRequired[pulumi.Input[PerformanceDataArgsDict]]
    preferred_targets: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureTarget]]]]
    ]
    savings_settings: NotRequired[pulumi.Input[SavingsSettingsArgsDict]]
    scaling_factor: NotRequired[pulumi.Input[_builtins.float]]
    sizing_criterion: NotRequired[
        pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
    ]
    sql_server_license: NotRequired[
        pulumi.Input[Union[_builtins.str, SqlServerLicense]]
    ]

@pulumi.input_type
class SqlAssessmentSettingsArgs:
    def __init__(
        __self__,
        *,
        async_commit_mode_intent: Optional[
            pulumi.Input[Union[_builtins.str, AsyncCommitModeIntent]]
        ] = ...,
        azure_location: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_security_offering_type: Optional[
            pulumi.Input[Union[_builtins.str, AzureSecurityOfferingType]]
        ] = ...,
        azure_sql_database_settings: Optional[pulumi.Input[SqlDbSettingsV3Args]] = ...,
        azure_sql_managed_instance_settings: Optional[
            pulumi.Input[SqlMiSettingsV3Args]
        ] = ...,
        azure_sql_vm_settings: Optional[pulumi.Input[SqlVmSettingsArgs]] = ...,
        billing_settings: Optional[pulumi.Input[BillingSettingsArgs]] = ...,
        currency: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]] = ...,
        disaster_recovery_location: Optional[
            pulumi.Input[Union[_builtins.str, AzureLocation]]
        ] = ...,
        discount_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        enable_hadr_assessment: Optional[pulumi.Input[_builtins.bool]] = ...,
        entity_uptime: Optional[pulumi.Input[EntityUptimeArgs]] = ...,
        environment_type: Optional[
            pulumi.Input[Union[_builtins.str, EnvironmentType]]
        ] = ...,
        is_internet_access_available: Optional[pulumi.Input[_builtins.bool]] = ...,
        multi_subnet_intent: Optional[
            pulumi.Input[Union[_builtins.str, MultiSubnetIntent]]
        ] = ...,
        os_license: Optional[pulumi.Input[Union[_builtins.str, OsLicense]]] = ...,
        performance_data: Optional[pulumi.Input[PerformanceDataArgs]] = ...,
        preferred_targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureTarget]]]]
        ] = ...,
        savings_settings: Optional[pulumi.Input[SavingsSettingsArgs]] = ...,
        scaling_factor: Optional[pulumi.Input[_builtins.float]] = ...,
        sizing_criterion: Optional[
            pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
        ] = ...,
        sql_server_license: Optional[
            pulumi.Input[Union[_builtins.str, SqlServerLicense]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asyncCommitModeIntent")
    def async_commit_mode_intent(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AsyncCommitModeIntent]]]: ...
    @async_commit_mode_intent.setter
    def async_commit_mode_intent(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AsyncCommitModeIntent]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_location.setter
    def azure_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="azureSecurityOfferingType")
    def azure_security_offering_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSecurityOfferingType]]]: ...
    @azure_security_offering_type.setter
    def azure_security_offering_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AzureSecurityOfferingType]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlDatabaseSettings")
    def azure_sql_database_settings(
        self,
    ) -> Optional[pulumi.Input[SqlDbSettingsV3Args]]: ...
    @azure_sql_database_settings.setter
    def azure_sql_database_settings(
        self, value: Optional[pulumi.Input[SqlDbSettingsV3Args]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlManagedInstanceSettings")
    def azure_sql_managed_instance_settings(
        self,
    ) -> Optional[pulumi.Input[SqlMiSettingsV3Args]]: ...
    @azure_sql_managed_instance_settings.setter
    def azure_sql_managed_instance_settings(
        self, value: Optional[pulumi.Input[SqlMiSettingsV3Args]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlVmSettings")
    def azure_sql_vm_settings(self) -> Optional[pulumi.Input[SqlVmSettingsArgs]]: ...
    @azure_sql_vm_settings.setter
    def azure_sql_vm_settings(
        self, value: Optional[pulumi.Input[SqlVmSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="billingSettings")
    def billing_settings(self) -> Optional[pulumi.Input[BillingSettingsArgs]]: ...
    @billing_settings.setter
    def billing_settings(self, value: Optional[pulumi.Input[BillingSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def currency(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]: ...
    @currency.setter
    def currency(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disasterRecoveryLocation")
    def disaster_recovery_location(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureLocation]]]: ...
    @disaster_recovery_location.setter
    def disaster_recovery_location(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureLocation]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="enableHadrAssessment")
    def enable_hadr_assessment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_hadr_assessment.setter
    def enable_hadr_assessment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="entityUptime")
    def entity_uptime(self) -> Optional[pulumi.Input[EntityUptimeArgs]]: ...
    @entity_uptime.setter
    def entity_uptime(self, value: Optional[pulumi.Input[EntityUptimeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnvironmentType]]]: ...
    @environment_type.setter
    def environment_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnvironmentType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isInternetAccessAvailable")
    def is_internet_access_available(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_internet_access_available.setter
    def is_internet_access_available(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiSubnetIntent")
    def multi_subnet_intent(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MultiSubnetIntent]]]: ...
    @multi_subnet_intent.setter
    def multi_subnet_intent(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MultiSubnetIntent]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osLicense")
    def os_license(self) -> Optional[pulumi.Input[Union[_builtins.str, OsLicense]]]: ...
    @os_license.setter
    def os_license(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OsLicense]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> Optional[pulumi.Input[PerformanceDataArgs]]: ...
    @performance_data.setter
    def performance_data(self, value: Optional[pulumi.Input[PerformanceDataArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredTargets")
    def preferred_targets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureTarget]]]]
    ]: ...
    @preferred_targets.setter
    def preferred_targets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureTarget]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="savingsSettings")
    def savings_settings(self) -> Optional[pulumi.Input[SavingsSettingsArgs]]: ...
    @savings_settings.setter
    def savings_settings(self, value: Optional[pulumi.Input[SavingsSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @scaling_factor.setter
    def scaling_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]]: ...
    @sizing_criterion.setter
    def sizing_criterion(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerLicense")
    def sql_server_license(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SqlServerLicense]]]: ...
    @sql_server_license.setter
    def sql_server_license(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SqlServerLicense]]]
    ): ...

class SqlAssessmentV3PropertiesArgsDict(TypedDict):
    fallback_machine_assessment_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[ScopeArgsDict]]
    settings: NotRequired[pulumi.Input[SqlAssessmentSettingsArgsDict]]

@pulumi.input_type
class SqlAssessmentV3PropertiesArgs:
    def __init__(
        __self__,
        *,
        fallback_machine_assessment_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[ScopeArgs]] = ...,
        settings: Optional[pulumi.Input[SqlAssessmentSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fallbackMachineAssessmentArmId")
    def fallback_machine_assessment_arm_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fallback_machine_assessment_arm_id.setter
    def fallback_machine_assessment_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[ScopeArgs]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[ScopeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[SqlAssessmentSettingsArgs]]: ...
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[SqlAssessmentSettingsArgs]]): ...

class SqlDatabaseResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]
    zone_redundant: NotRequired[pulumi.Input[Union[_builtins.str, ZoneRedundant]]]

@pulumi.input_type
class SqlDatabaseResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_redundant: Optional[
            pulumi.Input[Union[_builtins.str, ZoneRedundant]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ZoneRedundant]]]: ...
    @zone_redundant.setter
    def zone_redundant(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ZoneRedundant]]]
    ): ...

class SqlDbSettingsV3ArgsDict(TypedDict):
    azure_sql_compute_tier: NotRequired[pulumi.Input[Union[_builtins.str, ComputeTier]]]
    azure_sql_data_base_type: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSqlDataBaseType]]
    ]
    azure_sql_purchase_model: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSqlPurchaseModel]]
    ]
    azure_sql_service_tier: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSqlServiceTierV3]]
    ]

@pulumi.input_type
class SqlDbSettingsV3Args:
    def __init__(
        __self__,
        *,
        azure_sql_compute_tier: Optional[
            pulumi.Input[Union[_builtins.str, ComputeTier]]
        ] = ...,
        azure_sql_data_base_type: Optional[
            pulumi.Input[Union[_builtins.str, AzureSqlDataBaseType]]
        ] = ...,
        azure_sql_purchase_model: Optional[
            pulumi.Input[Union[_builtins.str, AzureSqlPurchaseModel]]
        ] = ...,
        azure_sql_service_tier: Optional[
            pulumi.Input[Union[_builtins.str, AzureSqlServiceTierV3]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureSqlComputeTier")
    def azure_sql_compute_tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ComputeTier]]]: ...
    @azure_sql_compute_tier.setter
    def azure_sql_compute_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ComputeTier]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlDataBaseType")
    def azure_sql_data_base_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSqlDataBaseType]]]: ...
    @azure_sql_data_base_type.setter
    def azure_sql_data_base_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureSqlDataBaseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlPurchaseModel")
    def azure_sql_purchase_model(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSqlPurchaseModel]]]: ...
    @azure_sql_purchase_model.setter
    def azure_sql_purchase_model(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureSqlPurchaseModel]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlServiceTier")
    def azure_sql_service_tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSqlServiceTierV3]]]: ...
    @azure_sql_service_tier.setter
    def azure_sql_service_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureSqlServiceTierV3]]]
    ): ...

class SqlDbSettingsArgsDict(TypedDict):
    azure_sql_compute_tier: NotRequired[pulumi.Input[Union[_builtins.str, ComputeTier]]]
    azure_sql_data_base_type: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSqlDataBaseType]]
    ]
    azure_sql_purchase_model: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSqlPurchaseModel]]
    ]
    azure_sql_service_tier: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSqlServiceTier]]
    ]

@pulumi.input_type
class SqlDbSettingsArgs:
    def __init__(
        __self__,
        *,
        azure_sql_compute_tier: Optional[
            pulumi.Input[Union[_builtins.str, ComputeTier]]
        ] = ...,
        azure_sql_data_base_type: Optional[
            pulumi.Input[Union[_builtins.str, AzureSqlDataBaseType]]
        ] = ...,
        azure_sql_purchase_model: Optional[
            pulumi.Input[Union[_builtins.str, AzureSqlPurchaseModel]]
        ] = ...,
        azure_sql_service_tier: Optional[
            pulumi.Input[Union[_builtins.str, AzureSqlServiceTier]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureSqlComputeTier")
    def azure_sql_compute_tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ComputeTier]]]: ...
    @azure_sql_compute_tier.setter
    def azure_sql_compute_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ComputeTier]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlDataBaseType")
    def azure_sql_data_base_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSqlDataBaseType]]]: ...
    @azure_sql_data_base_type.setter
    def azure_sql_data_base_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureSqlDataBaseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlPurchaseModel")
    def azure_sql_purchase_model(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSqlPurchaseModel]]]: ...
    @azure_sql_purchase_model.setter
    def azure_sql_purchase_model(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureSqlPurchaseModel]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlServiceTier")
    def azure_sql_service_tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSqlServiceTier]]]: ...
    @azure_sql_service_tier.setter
    def azure_sql_service_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureSqlServiceTier]]]
    ): ...

class SqlElasticPoolResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]
    zone_redundant: NotRequired[pulumi.Input[Union[_builtins.str, ZoneRedundant]]]

@pulumi.input_type
class SqlElasticPoolResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_redundant: Optional[
            pulumi.Input[Union[_builtins.str, ZoneRedundant]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ZoneRedundant]]]: ...
    @zone_redundant.setter
    def zone_redundant(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ZoneRedundant]]]
    ): ...

class SqlMiSettingsV3ArgsDict(TypedDict):
    azure_sql_instance_type: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSqlInstanceType]]
    ]
    azure_sql_service_tier: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSqlServiceTierV3]]
    ]

@pulumi.input_type
class SqlMiSettingsV3Args:
    def __init__(
        __self__,
        *,
        azure_sql_instance_type: Optional[
            pulumi.Input[Union[_builtins.str, AzureSqlInstanceType]]
        ] = ...,
        azure_sql_service_tier: Optional[
            pulumi.Input[Union[_builtins.str, AzureSqlServiceTierV3]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureSqlInstanceType")
    def azure_sql_instance_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSqlInstanceType]]]: ...
    @azure_sql_instance_type.setter
    def azure_sql_instance_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureSqlInstanceType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlServiceTier")
    def azure_sql_service_tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSqlServiceTierV3]]]: ...
    @azure_sql_service_tier.setter
    def azure_sql_service_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureSqlServiceTierV3]]]
    ): ...

class SqlMiSettingsArgsDict(TypedDict):
    azure_sql_instance_type: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSqlInstanceType]]
    ]
    azure_sql_service_tier: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureSqlServiceTier]]
    ]

@pulumi.input_type
class SqlMiSettingsArgs:
    def __init__(
        __self__,
        *,
        azure_sql_instance_type: Optional[
            pulumi.Input[Union[_builtins.str, AzureSqlInstanceType]]
        ] = ...,
        azure_sql_service_tier: Optional[
            pulumi.Input[Union[_builtins.str, AzureSqlServiceTier]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureSqlInstanceType")
    def azure_sql_instance_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSqlInstanceType]]]: ...
    @azure_sql_instance_type.setter
    def azure_sql_instance_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureSqlInstanceType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSqlServiceTier")
    def azure_sql_service_tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureSqlServiceTier]]]: ...
    @azure_sql_service_tier.setter
    def azure_sql_service_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureSqlServiceTier]]]
    ): ...

class SqlServerLicensingSettingsArgsDict(TypedDict):
    license_cost: pulumi.Input[_builtins.float]
    software_assurance_cost: pulumi.Input[_builtins.float]
    version: pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]

@pulumi.input_type
class SqlServerLicensingSettingsArgs:
    def __init__(
        __self__,
        *,
        license_cost: pulumi.Input[_builtins.float],
        software_assurance_cost: pulumi.Input[_builtins.float],
        version: pulumi.Input[Union[_builtins.str, SqlServerLicenseType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="licenseCost")
    def license_cost(self) -> pulumi.Input[_builtins.float]: ...
    @license_cost.setter
    def license_cost(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceCost")
    def software_assurance_cost(self) -> pulumi.Input[_builtins.float]: ...
    @software_assurance_cost.setter
    def software_assurance_cost(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]: ...
    @version.setter
    def version(
        self, value: pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]
    ): ...

class SqlServerResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SqlServerResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SqlVmSettingsArgsDict(TypedDict):
    instance_series: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]
    ]

@pulumi.input_type
class SqlVmSettingsArgs:
    def __init__(
        __self__,
        *,
        instance_series: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceSeries")
    def instance_series(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]
    ]: ...
    @instance_series.setter
    def instance_series(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]
        ],
    ): ...

class StorageSettingsArgsDict(TypedDict):
    cost_per_gb_per_month: pulumi.Input[_builtins.float]
    maintainance_cost_percentage_to_acquisition_cost: pulumi.Input[_builtins.float]

@pulumi.input_type
class StorageSettingsArgs:
    def __init__(
        __self__,
        *,
        cost_per_gb_per_month: pulumi.Input[_builtins.float],
        maintainance_cost_percentage_to_acquisition_cost: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costPerGbPerMonth")
    def cost_per_gb_per_month(self) -> pulumi.Input[_builtins.float]: ...
    @cost_per_gb_per_month.setter
    def cost_per_gb_per_month(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="maintainanceCostPercentageToAcquisitionCost")
    def maintainance_cost_percentage_to_acquisition_cost(
        self,
    ) -> pulumi.Input[_builtins.float]: ...
    @maintainance_cost_percentage_to_acquisition_cost.setter
    def maintainance_cost_percentage_to_acquisition_cost(
        self, value: pulumi.Input[_builtins.float]
    ): ...

class SubnetReferenceArgsDict(TypedDict):
    source_arm_resource_id: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubnetReferenceArgs:
    def __init__(
        __self__,
        *,
        source_arm_resource_id: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceArmResourceId")
    def source_arm_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_arm_resource_id.setter
    def source_arm_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubnetResourceSettingsArgsDict(TypedDict):
    address_prefix: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    network_security_group: NotRequired[pulumi.Input[NsgReferenceArgsDict]]

@pulumi.input_type
class SubnetResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        address_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_security_group: Optional[pulumi.Input[NsgReferenceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_prefix.setter
    def address_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[pulumi.Input[NsgReferenceArgs]]: ...
    @network_security_group.setter
    def network_security_group(
        self, value: Optional[pulumi.Input[NsgReferenceArgs]]
    ): ...

class TargetAssessmentArmIdsArgsDict(TypedDict):
    aks: NotRequired[pulumi.Input[_builtins.str]]
    azure_app_service: NotRequired[pulumi.Input[_builtins.str]]
    azure_app_service_container: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetAssessmentArmIdsArgs:
    def __init__(
        __self__,
        *,
        aks: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_app_service: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_app_service_container: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aks(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aks.setter
    def aks(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="azureAppService")
    def azure_app_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_app_service.setter
    def azure_app_service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="azureAppServiceContainer")
    def azure_app_service_container(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_app_service_container.setter
    def azure_app_service_container(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class TargetStorageProfileArgsDict(TypedDict):
    azure_file_share_profile: NotRequired[
        pulumi.Input[AzureFileShareHydrationProfileArgsDict]
    ]
    hydration_storage_provider_type: NotRequired[
        pulumi.Input[Union[_builtins.str, TargetHydrationStorageProviderType]]
    ]
    persistent_volume_id: NotRequired[pulumi.Input[_builtins.str]]
    storage_access_type: NotRequired[
        pulumi.Input[Union[_builtins.str, TargetStorageAccessType]]
    ]
    storage_projection_type: NotRequired[
        pulumi.Input[Union[_builtins.str, TargetStorageProjectionType]]
    ]
    target_name: NotRequired[pulumi.Input[_builtins.str]]
    target_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetStorageProfileArgs:
    def __init__(
        __self__,
        *,
        azure_file_share_profile: Optional[
            pulumi.Input[AzureFileShareHydrationProfileArgs]
        ] = ...,
        hydration_storage_provider_type: Optional[
            pulumi.Input[Union[_builtins.str, TargetHydrationStorageProviderType]]
        ] = ...,
        persistent_volume_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_access_type: Optional[
            pulumi.Input[Union[_builtins.str, TargetStorageAccessType]]
        ] = ...,
        storage_projection_type: Optional[
            pulumi.Input[Union[_builtins.str, TargetStorageProjectionType]]
        ] = ...,
        target_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareProfile")
    def azure_file_share_profile(
        self,
    ) -> Optional[pulumi.Input[AzureFileShareHydrationProfileArgs]]: ...
    @azure_file_share_profile.setter
    def azure_file_share_profile(
        self, value: Optional[pulumi.Input[AzureFileShareHydrationProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hydrationStorageProviderType")
    def hydration_storage_provider_type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, TargetHydrationStorageProviderType]]
    ]: ...
    @hydration_storage_provider_type.setter
    def hydration_storage_provider_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, TargetHydrationStorageProviderType]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="persistentVolumeId")
    def persistent_volume_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @persistent_volume_id.setter
    def persistent_volume_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccessType")
    def storage_access_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TargetStorageAccessType]]]: ...
    @storage_access_type.setter
    def storage_access_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, TargetStorageAccessType]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageProjectionType")
    def storage_projection_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TargetStorageProjectionType]]]: ...
    @storage_projection_type.setter
    def storage_projection_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, TargetStorageProjectionType]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_name.setter
    def target_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetSize")
    def target_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_size.setter
    def target_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskPropertiesArgsDict(TypedDict):
    display_name: pulumi.Input[_builtins.str]
    scope: pulumi.Input[Union[_builtins.str, TaskScope]]
    scope_id: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    stage: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TaskPropertiesArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        scope: pulumi.Input[Union[_builtins.str, TaskScope]],
        scope_id: pulumi.Input[_builtins.str],
        status: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        stage: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[Union[_builtins.str, TaskScope]]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[Union[_builtins.str, TaskScope]]): ...
    @_builtins.property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> pulumi.Input[_builtins.str]: ...
    @scope_id.setter
    def scope_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stage.setter
    def stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ThirdPartyManagementSettingsArgsDict(TypedDict):
    license_cost: pulumi.Input[_builtins.float]
    support_cost: pulumi.Input[_builtins.float]

@pulumi.input_type
class ThirdPartyManagementSettingsArgs:
    def __init__(
        __self__,
        *,
        license_cost: pulumi.Input[_builtins.float],
        support_cost: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="licenseCost")
    def license_cost(self) -> pulumi.Input[_builtins.float]: ...
    @license_cost.setter
    def license_cost(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="supportCost")
    def support_cost(self) -> pulumi.Input[_builtins.float]: ...
    @support_cost.setter
    def support_cost(self, value: pulumi.Input[_builtins.float]): ...

class UserAssignedIdentityArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserAssignedIdentityArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareMigrateAgentModelCustomPropertiesArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    fabric_friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    vmware_site_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareMigrateAgentModelCustomPropertiesArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        fabric_friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_site_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fabricFriendlyName")
    def fabric_friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fabric_friendly_name.setter
    def fabric_friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareSiteId")
    def vmware_site_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vmware_site_id.setter
    def vmware_site_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualMachineResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_availability_set_id: NotRequired[pulumi.Input[_builtins.str]]
    target_availability_zone: NotRequired[
        pulumi.Input[Union[_builtins.str, TargetAvailabilityZone]]
    ]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_size: NotRequired[pulumi.Input[_builtins.str]]
    user_managed_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class VirtualMachineResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_availability_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_availability_zone: Optional[
            pulumi.Input[Union[_builtins.str, TargetAvailabilityZone]]
        ] = ...,
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
        user_managed_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="targetAvailabilitySetId")
    def target_availability_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_availability_set_id.setter
    def target_availability_set_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAvailabilityZone")
    def target_availability_zone(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TargetAvailabilityZone]]]: ...
    @target_availability_zone.setter
    def target_availability_zone(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, TargetAvailabilityZone]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSize")
    def target_vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vm_size.setter
    def target_vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userManagedIdentities")
    def user_managed_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_managed_identities.setter
    def user_managed_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class VirtualNetworkResourceSettingsArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    address_space: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enable_ddos_protection: NotRequired[pulumi.Input[_builtins.bool]]
    subnets: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubnetResourceSettingsArgsDict]]]
    ]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNetworkResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        address_space: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_ddos_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        subnets: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubnetResourceSettingsArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @address_space.setter
    def address_space(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDdosProtection")
    def enable_ddos_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ddos_protection.setter
    def enable_ddos_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def subnets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubnetResourceSettingsArgs]]]]: ...
    @subnets.setter
    def subnets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubnetResourceSettingsArgs]]]
        ],
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
    @pulumi.getter(name="targetResourceGroupName")
    def target_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_group_name.setter
    def target_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_name.setter
    def target_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualizationSoftwareSettingsArgsDict(TypedDict):
    v_mware_cloud_foundation_license_cost: pulumi.Input[_builtins.float]

@pulumi.input_type
class VirtualizationSoftwareSettingsArgs:
    def __init__(
        __self__,
        *,
        v_mware_cloud_foundation_license_cost: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vMwareCloudFoundationLicenseCost")
    def v_mware_cloud_foundation_license_cost(
        self,
    ) -> pulumi.Input[_builtins.float]: ...
    @v_mware_cloud_foundation_license_cost.setter
    def v_mware_cloud_foundation_license_cost(
        self, value: pulumi.Input[_builtins.float]
    ): ...

class VmUptimeArgsDict(TypedDict):
    days_per_month: NotRequired[pulumi.Input[_builtins.float]]
    hours_per_day: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class VmUptimeArgs:
    def __init__(
        __self__,
        *,
        days_per_month: Optional[pulumi.Input[_builtins.float]] = ...,
        hours_per_day: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysPerMonth")
    def days_per_month(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @days_per_month.setter
    def days_per_month(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="hoursPerDay")
    def hours_per_day(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @hours_per_day.setter
    def hours_per_day(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class WavePropertiesArgsDict(TypedDict):
    arg: pulumi.Input[ArgArgsDict]
    display_name: pulumi.Input[_builtins.str]
    planned_start_date: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    planned_completion_date: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WavePropertiesArgs:
    def __init__(
        __self__,
        *,
        arg: pulumi.Input[ArgArgs],
        display_name: pulumi.Input[_builtins.str],
        planned_start_date: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        planned_completion_date: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arg(self) -> pulumi.Input[ArgArgs]: ...
    @arg.setter
    def arg(self, value: pulumi.Input[ArgArgs]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="plannedStartDate")
    def planned_start_date(self) -> pulumi.Input[_builtins.str]: ...
    @planned_start_date.setter
    def planned_start_date(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="plannedCompletionDate")
    def planned_completion_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @planned_completion_date.setter
    def planned_completion_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WebAppAssessmentSettingsArgsDict(TypedDict):
    app_svc_container_settings: pulumi.Input[AppSvcContainerSettingsArgsDict]
    app_svc_native_settings: pulumi.Input[AppSvcNativeSettingsArgsDict]
    azure_security_offering_type: pulumi.Input[
        Union[_builtins.str, AzureSecurityOfferingType]
    ]
    azure_location: NotRequired[pulumi.Input[_builtins.str]]
    billing_settings: NotRequired[pulumi.Input[BillingSettingsArgsDict]]
    currency: NotRequired[pulumi.Input[Union[_builtins.str, AzureCurrency]]]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    environment_type: NotRequired[pulumi.Input[Union[_builtins.str, EnvironmentType]]]
    performance_data: NotRequired[pulumi.Input[PerformanceDataArgsDict]]
    savings_settings: NotRequired[pulumi.Input[SavingsSettingsArgsDict]]
    scaling_factor: NotRequired[pulumi.Input[_builtins.float]]
    sizing_criterion: NotRequired[
        pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
    ]

@pulumi.input_type
class WebAppAssessmentSettingsArgs:
    def __init__(
        __self__,
        *,
        app_svc_container_settings: pulumi.Input[AppSvcContainerSettingsArgs],
        app_svc_native_settings: pulumi.Input[AppSvcNativeSettingsArgs],
        azure_security_offering_type: pulumi.Input[
            Union[_builtins.str, AzureSecurityOfferingType]
        ],
        azure_location: Optional[pulumi.Input[_builtins.str]] = ...,
        billing_settings: Optional[pulumi.Input[BillingSettingsArgs]] = ...,
        currency: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]] = ...,
        discount_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        environment_type: Optional[
            pulumi.Input[Union[_builtins.str, EnvironmentType]]
        ] = ...,
        performance_data: Optional[pulumi.Input[PerformanceDataArgs]] = ...,
        savings_settings: Optional[pulumi.Input[SavingsSettingsArgs]] = ...,
        scaling_factor: Optional[pulumi.Input[_builtins.float]] = ...,
        sizing_criterion: Optional[
            pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appSvcContainerSettings")
    def app_svc_container_settings(
        self,
    ) -> pulumi.Input[AppSvcContainerSettingsArgs]: ...
    @app_svc_container_settings.setter
    def app_svc_container_settings(
        self, value: pulumi.Input[AppSvcContainerSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="appSvcNativeSettings")
    def app_svc_native_settings(self) -> pulumi.Input[AppSvcNativeSettingsArgs]: ...
    @app_svc_native_settings.setter
    def app_svc_native_settings(
        self, value: pulumi.Input[AppSvcNativeSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureSecurityOfferingType")
    def azure_security_offering_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AzureSecurityOfferingType]]: ...
    @azure_security_offering_type.setter
    def azure_security_offering_type(
        self, value: pulumi.Input[Union[_builtins.str, AzureSecurityOfferingType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_location.setter
    def azure_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="billingSettings")
    def billing_settings(self) -> Optional[pulumi.Input[BillingSettingsArgs]]: ...
    @billing_settings.setter
    def billing_settings(self, value: Optional[pulumi.Input[BillingSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def currency(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]: ...
    @currency.setter
    def currency(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnvironmentType]]]: ...
    @environment_type.setter
    def environment_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnvironmentType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> Optional[pulumi.Input[PerformanceDataArgs]]: ...
    @performance_data.setter
    def performance_data(self, value: Optional[pulumi.Input[PerformanceDataArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="savingsSettings")
    def savings_settings(self) -> Optional[pulumi.Input[SavingsSettingsArgs]]: ...
    @savings_settings.setter
    def savings_settings(self, value: Optional[pulumi.Input[SavingsSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @scaling_factor.setter
    def scaling_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]]: ...
    @sizing_criterion.setter
    def sizing_criterion(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]],
    ): ...

class WebAppAssessmentV3PropertiesArgsDict(TypedDict):
    fallback_machine_assessment_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[ScopeArgsDict]]
    settings: NotRequired[pulumi.Input[WebAppAssessmentSettingsArgsDict]]

@pulumi.input_type
class WebAppAssessmentV3PropertiesArgs:
    def __init__(
        __self__,
        *,
        fallback_machine_assessment_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[ScopeArgs]] = ...,
        settings: Optional[pulumi.Input[WebAppAssessmentSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fallbackMachineAssessmentArmId")
    def fallback_machine_assessment_arm_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fallback_machine_assessment_arm_id.setter
    def fallback_machine_assessment_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[ScopeArgs]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[ScopeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[WebAppAssessmentSettingsArgs]]: ...
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[WebAppAssessmentSettingsArgs]]): ...

class WebApplicationConfigurationArgsDict(TypedDict):
    file_path: NotRequired[pulumi.Input[_builtins.str]]
    identifier: NotRequired[pulumi.Input[_builtins.str]]
    is_deployment_time_editable: NotRequired[pulumi.Input[_builtins.bool]]
    local_file_path: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    secret_store_details: NotRequired[pulumi.Input[SecretStoreDetailsArgsDict]]
    section: NotRequired[pulumi.Input[_builtins.str]]
    target_file_path: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ConfigurationType]]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WebApplicationConfigurationArgs:
    def __init__(
        __self__,
        *,
        file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        is_deployment_time_editable: Optional[pulumi.Input[_builtins.bool]] = ...,
        local_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_store_details: Optional[pulumi.Input[SecretStoreDetailsArgs]] = ...,
        section: Optional[pulumi.Input[_builtins.str]] = ...,
        target_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, ConfigurationType]]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeploymentTimeEditable")
    def is_deployment_time_editable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deployment_time_editable.setter
    def is_deployment_time_editable(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localFilePath")
    def local_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_file_path.setter
    def local_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStoreDetails")
    def secret_store_details(
        self,
    ) -> Optional[pulumi.Input[SecretStoreDetailsArgs]]: ...
    @secret_store_details.setter
    def secret_store_details(
        self, value: Optional[pulumi.Input[SecretStoreDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def section(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @section.setter
    def section(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetFilePath")
    def target_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_file_path.setter
    def target_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConfigurationType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConfigurationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WebApplicationDirectoryArgsDict(TypedDict):
    is_editable: NotRequired[pulumi.Input[_builtins.bool]]
    source_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    source_size: NotRequired[pulumi.Input[_builtins.str]]
    storage_profile: NotRequired[pulumi.Input[TargetStorageProfileArgsDict]]

@pulumi.input_type
class WebApplicationDirectoryArgs:
    def __init__(
        __self__,
        *,
        is_editable: Optional[pulumi.Input[_builtins.bool]] = ...,
        source_paths: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        source_size: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_profile: Optional[pulumi.Input[TargetStorageProfileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEditable")
    def is_editable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_editable.setter
    def is_editable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sourcePaths")
    def source_paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_paths.setter
    def source_paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceSize")
    def source_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_size.setter
    def source_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[TargetStorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(
        self, value: Optional[pulumi.Input[TargetStorageProfileArgs]]
    ): ...

class WebApplicationFrameworkArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WebApplicationFrameworkArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WindowsServerLicensingSettingsArgsDict(TypedDict):
    license_cost: pulumi.Input[_builtins.float]
    licenses_per_core: pulumi.Input[_builtins.int]
    software_assurance_cost: pulumi.Input[_builtins.float]

@pulumi.input_type
class WindowsServerLicensingSettingsArgs:
    def __init__(
        __self__,
        *,
        license_cost: pulumi.Input[_builtins.float],
        licenses_per_core: pulumi.Input[_builtins.int],
        software_assurance_cost: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="licenseCost")
    def license_cost(self) -> pulumi.Input[_builtins.float]: ...
    @license_cost.setter
    def license_cost(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="licensesPerCore")
    def licenses_per_core(self) -> pulumi.Input[_builtins.int]: ...
    @licenses_per_core.setter
    def licenses_per_core(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceCost")
    def software_assurance_cost(self) -> pulumi.Input[_builtins.float]: ...
    @software_assurance_cost.setter
    def software_assurance_cost(self, value: pulumi.Input[_builtins.float]): ...

class WorkloadDeploymentModelPropertiesArgsDict(TypedDict):
    custom_properties: NotRequired[
        pulumi.Input[
            Union[
                ApacheTomcatAKSWorkloadDeploymentModelCustomPropertiesArgsDict,
                IISAKSWorkloadDeploymentModelCustomPropertiesArgsDict,
            ]
        ]
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    target_platform: NotRequired[
        pulumi.Input[Union[_builtins.str, WorkloadDeploymentTarget]]
    ]
    workload_instance_properties: NotRequired[
        pulumi.Input[WorkloadInstanceModelPropertiesArgsDict]
    ]

@pulumi.input_type
class WorkloadDeploymentModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        custom_properties: Optional[
            pulumi.Input[
                Union[
                    ApacheTomcatAKSWorkloadDeploymentModelCustomPropertiesArgs,
                    IISAKSWorkloadDeploymentModelCustomPropertiesArgs,
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_platform: Optional[
            pulumi.Input[Union[_builtins.str, WorkloadDeploymentTarget]]
        ] = ...,
        workload_instance_properties: Optional[
            pulumi.Input[WorkloadInstanceModelPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                ApacheTomcatAKSWorkloadDeploymentModelCustomPropertiesArgs,
                IISAKSWorkloadDeploymentModelCustomPropertiesArgs,
            ]
        ]
    ]: ...
    @custom_properties.setter
    def custom_properties(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    ApacheTomcatAKSWorkloadDeploymentModelCustomPropertiesArgs,
                    IISAKSWorkloadDeploymentModelCustomPropertiesArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetPlatform")
    def target_platform(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WorkloadDeploymentTarget]]]: ...
    @target_platform.setter
    def target_platform(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, WorkloadDeploymentTarget]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadInstanceProperties")
    def workload_instance_properties(
        self,
    ) -> Optional[pulumi.Input[WorkloadInstanceModelPropertiesArgs]]: ...
    @workload_instance_properties.setter
    def workload_instance_properties(
        self, value: Optional[pulumi.Input[WorkloadInstanceModelPropertiesArgs]]
    ): ...

class WorkloadInstanceModelPropertiesArgsDict(TypedDict):
    custom_properties: NotRequired[
        pulumi.Input[
            Union[
                ApacheTomcatWorkloadInstanceModelCustomPropertiesArgsDict,
                IISWorkloadInstanceModelCustomPropertiesArgsDict,
            ]
        ]
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    master_site_name: NotRequired[pulumi.Input[_builtins.str]]
    migrate_agent_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_name: NotRequired[pulumi.Input[_builtins.str]]
    source_platform: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadInstanceModelPropertiesArgs:
    def __init__(
        __self__,
        *,
        custom_properties: Optional[
            pulumi.Input[
                Union[
                    ApacheTomcatWorkloadInstanceModelCustomPropertiesArgs,
                    IISWorkloadInstanceModelCustomPropertiesArgs,
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        master_site_name: Optional[pulumi.Input[_builtins.str]] = ...,
        migrate_agent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_platform: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                ApacheTomcatWorkloadInstanceModelCustomPropertiesArgs,
                IISWorkloadInstanceModelCustomPropertiesArgs,
            ]
        ]
    ]: ...
    @custom_properties.setter
    def custom_properties(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    ApacheTomcatWorkloadInstanceModelCustomPropertiesArgs,
                    IISWorkloadInstanceModelCustomPropertiesArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterSiteName")
    def master_site_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_site_name.setter
    def master_site_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="migrateAgentId")
    def migrate_agent_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migrate_agent_id.setter
    def migrate_agent_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_name.setter
    def source_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourcePlatform")
    def source_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_platform.setter
    def source_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
