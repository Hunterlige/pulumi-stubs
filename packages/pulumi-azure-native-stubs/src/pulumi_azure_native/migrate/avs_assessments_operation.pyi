

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AvsAssessmentsOperationArgs', 'AvsAssessmentsOperation']
@pulumi.input_type
class AvsAssessmentsOperationArgs:
    def __init__(__self__, *, group_name: pulumi.Input[_builtins.str], project_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], assessment_name: Optional[pulumi.Input[_builtins.str]] = ..., avs_assessment_scenario: Optional[pulumi.Input[Union[_builtins.str, AvsAssessmentScenario]]] = ..., azure_location: Optional[pulumi.Input[Union[_builtins.str, AzureLocation]]] = ..., azure_offer_code: Optional[pulumi.Input[Union[_builtins.str, AzureOfferCode]]] = ..., cpu_headroom: Optional[pulumi.Input[_builtins.float]] = ..., currency: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]] = ..., dedupe_compression: Optional[pulumi.Input[_builtins.float]] = ..., discount_percentage: Optional[pulumi.Input[_builtins.float]] = ..., external_storage_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExternalStorageType]]]]] = ..., failures_to_tolerate_and_raid_level: Optional[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]] = ..., failures_to_tolerate_and_raid_level_list: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]]]] = ..., is_stretch_cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_vcf_byol_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., mem_overcommit: Optional[pulumi.Input[_builtins.float]] = ..., node_type: Optional[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]] = ..., node_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]]]] = ..., percentile: Optional[pulumi.Input[Union[_builtins.str, Percentile]]] = ..., perf_data_end_time: Optional[pulumi.Input[_builtins.str]] = ..., perf_data_start_time: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]] = ..., reserved_instance: Optional[pulumi.Input[Union[_builtins.str, AzureReservedInstance]]] = ..., scaling_factor: Optional[pulumi.Input[_builtins.float]] = ..., sizing_criterion: Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]] = ..., time_range: Optional[pulumi.Input[Union[_builtins.str, TimeRange]]] = ..., vcpu_oversubscription: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_name.setter
    def group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @project_name.setter
    def project_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentName")
    def assessment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assessment_name.setter
    def assessment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsAssessmentScenario")
    def avs_assessment_scenario(self) -> Optional[pulumi.Input[Union[_builtins.str, AvsAssessmentScenario]]]:
        
        ...
    
    @avs_assessment_scenario.setter
    def avs_assessment_scenario(self, value: Optional[pulumi.Input[Union[_builtins.str, AvsAssessmentScenario]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureLocation]]]:
        
        ...
    
    @azure_location.setter
    def azure_location(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureLocation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureOfferCode]]]:
        
        ...
    
    @azure_offer_code.setter
    def azure_offer_code(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureOfferCode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuHeadroom")
    def cpu_headroom(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @cpu_headroom.setter
    def cpu_headroom(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]:
        
        ...
    
    @currency.setter
    def currency(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedupeCompression")
    def dedupe_compression(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @dedupe_compression.setter
    def dedupe_compression(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalStorageTypes")
    def external_storage_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExternalStorageType]]]]]:
        
        ...
    
    @external_storage_types.setter
    def external_storage_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExternalStorageType]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failuresToTolerateAndRaidLevel")
    def failures_to_tolerate_and_raid_level(self) -> Optional[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]]:
        
        ...
    
    @failures_to_tolerate_and_raid_level.setter
    def failures_to_tolerate_and_raid_level(self, value: Optional[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failuresToTolerateAndRaidLevelList")
    def failures_to_tolerate_and_raid_level_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]]]]:
        
        ...
    
    @failures_to_tolerate_and_raid_level_list.setter
    def failures_to_tolerate_and_raid_level_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isStretchClusterEnabled")
    def is_stretch_cluster_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_stretch_cluster_enabled.setter
    def is_stretch_cluster_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isVcfByolEnabled")
    def is_vcf_byol_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_vcf_byol_enabled.setter
    def is_vcf_byol_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memOvercommit")
    def mem_overcommit(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @mem_overcommit.setter
    def mem_overcommit(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypes")
    def node_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]]]]:
        
        ...
    
    @node_types.setter
    def node_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def percentile(self) -> Optional[pulumi.Input[Union[_builtins.str, Percentile]]]:
        
        ...
    
    @percentile.setter
    def percentile(self, value: Optional[pulumi.Input[Union[_builtins.str, Percentile]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="perfDataEndTime")
    def perf_data_end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @perf_data_end_time.setter
    def perf_data_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="perfDataStartTime")
    def perf_data_start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @perf_data_start_time.setter
    def perf_data_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedInstance")
    def reserved_instance(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureReservedInstance]]]:
        
        ...
    
    @reserved_instance.setter
    def reserved_instance(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureReservedInstance]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @scaling_factor.setter
    def scaling_factor(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]]:
        
        ...
    
    @sizing_criterion.setter
    def sizing_criterion(self, value: Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[pulumi.Input[Union[_builtins.str, TimeRange]]]:
        
        ...
    
    @time_range.setter
    def time_range(self, value: Optional[pulumi.Input[Union[_builtins.str, TimeRange]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuOversubscription")
    def vcpu_oversubscription(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @vcpu_oversubscription.setter
    def vcpu_oversubscription(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:migrate:AvsAssessmentsOperation")
class AvsAssessmentsOperation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assessment_name: Optional[pulumi.Input[_builtins.str]] = ..., avs_assessment_scenario: Optional[pulumi.Input[Union[_builtins.str, AvsAssessmentScenario]]] = ..., azure_location: Optional[pulumi.Input[Union[_builtins.str, AzureLocation]]] = ..., azure_offer_code: Optional[pulumi.Input[Union[_builtins.str, AzureOfferCode]]] = ..., cpu_headroom: Optional[pulumi.Input[_builtins.float]] = ..., currency: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]] = ..., dedupe_compression: Optional[pulumi.Input[_builtins.float]] = ..., discount_percentage: Optional[pulumi.Input[_builtins.float]] = ..., external_storage_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExternalStorageType]]]]] = ..., failures_to_tolerate_and_raid_level: Optional[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]] = ..., failures_to_tolerate_and_raid_level_list: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FttAndRaidLevel]]]]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., is_stretch_cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_vcf_byol_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., mem_overcommit: Optional[pulumi.Input[_builtins.float]] = ..., node_type: Optional[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]] = ..., node_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureAvsNodeType]]]]] = ..., percentile: Optional[pulumi.Input[Union[_builtins.str, Percentile]]] = ..., perf_data_end_time: Optional[pulumi.Input[_builtins.str]] = ..., perf_data_start_time: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]] = ..., reserved_instance: Optional[pulumi.Input[Union[_builtins.str, AzureReservedInstance]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scaling_factor: Optional[pulumi.Input[_builtins.float]] = ..., sizing_criterion: Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]] = ..., time_range: Optional[pulumi.Input[Union[_builtins.str, TimeRange]]] = ..., vcpu_oversubscription: Optional[pulumi.Input[_builtins.float]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AvsAssessmentsOperationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AvsAssessmentsOperation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentErrorSummary")
    def assessment_error_summary(self) -> pulumi.Output[Mapping[str, _builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsAssessmentScenario")
    def avs_assessment_scenario(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsEstimatedExternalStorages")
    def avs_estimated_external_storages(self) -> pulumi.Output[Sequence[outputs.AvsEstimatedExternalStorageResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsEstimatedNetworks")
    def avs_estimated_networks(self) -> pulumi.Output[Sequence[outputs.AvsEstimatedNetworkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsEstimatedNodes")
    def avs_estimated_nodes(self) -> pulumi.Output[Sequence[outputs.AvsEstimatedNodeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costComponents")
    def cost_components(self) -> pulumi.Output[Sequence[outputs.CostComponentResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuHeadroom")
    def cpu_headroom(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuUtilization")
    def cpu_utilization(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedupeCompression")
    def dedupe_compression(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalStorageTypes")
    def external_storage_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failuresToTolerateAndRaidLevel")
    def failures_to_tolerate_and_raid_level(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failuresToTolerateAndRaidLevelList")
    def failures_to_tolerate_and_raid_level_list(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isStretchClusterEnabled")
    def is_stretch_cluster_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isVcfByolEnabled")
    def is_vcf_byol_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitingFactor")
    def limiting_factor(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memOvercommit")
    def mem_overcommit(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypes")
    def node_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percentile(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perfDataEndTime")
    def perf_data_end_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perfDataStartTime")
    def perf_data_start_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricesTimestamp")
    def prices_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ramUtilization")
    def ram_utilization(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedInstance")
    def reserved_instance(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageUtilization")
    def storage_utilization(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suitability(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suitabilityExplanation")
    def suitability_explanation(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suitabilitySummary")
    def suitability_summary(self) -> pulumi.Output[Mapping[str, _builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalCpuCores")
    def total_cpu_cores(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalMonthlyCost")
    def total_monthly_cost(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalRamInGB")
    def total_ram_in_gb(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStorageInGB")
    def total_storage_in_gb(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuOversubscription")
    def vcpu_oversubscription(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    


