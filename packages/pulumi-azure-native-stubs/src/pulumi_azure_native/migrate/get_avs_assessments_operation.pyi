

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAvsAssessmentsOperationResult', 'AwaitableGetAvsAssessmentsOperationResult', 'get_avs_assessments_operation', 'get_avs_assessments_operation_output']
@pulumi.output_type
class GetAvsAssessmentsOperationResult:
    
    def __init__(__self__, assessment_error_summary=..., assessment_type=..., avs_assessment_scenario=..., avs_estimated_external_storages=..., avs_estimated_networks=..., avs_estimated_nodes=..., azure_api_version=..., azure_location=..., azure_offer_code=..., confidence_rating_in_percentage=..., cost_components=..., cpu_headroom=..., cpu_utilization=..., created_timestamp=..., currency=..., dedupe_compression=..., discount_percentage=..., external_storage_types=..., failures_to_tolerate_and_raid_level=..., failures_to_tolerate_and_raid_level_list=..., group_type=..., id=..., is_stretch_cluster_enabled=..., is_vcf_byol_enabled=..., limiting_factor=..., mem_overcommit=..., name=..., node_type=..., node_types=..., number_of_machines=..., number_of_nodes=..., percentile=..., perf_data_end_time=..., perf_data_start_time=..., prices_timestamp=..., provisioning_state=..., ram_utilization=..., reserved_instance=..., scaling_factor=..., schema_version=..., sizing_criterion=..., stage=..., status=..., storage_utilization=..., suitability=..., suitability_explanation=..., suitability_summary=..., system_data=..., time_range=..., total_cpu_cores=..., total_monthly_cost=..., total_ram_in_gb=..., total_storage_in_gb=..., type=..., updated_timestamp=..., vcpu_oversubscription=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentErrorSummary")
    def assessment_error_summary(self) -> Mapping[str, _builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsAssessmentScenario")
    def avs_assessment_scenario(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsEstimatedExternalStorages")
    def avs_estimated_external_storages(self) -> Sequence[outputs.AvsEstimatedExternalStorageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsEstimatedNetworks")
    def avs_estimated_networks(self) -> Sequence[outputs.AvsEstimatedNetworkResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsEstimatedNodes")
    def avs_estimated_nodes(self) -> Sequence[outputs.AvsEstimatedNodeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costComponents")
    def cost_components(self) -> Sequence[outputs.CostComponentResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuHeadroom")
    def cpu_headroom(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuUtilization")
    def cpu_utilization(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        
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
    @pulumi.getter(name="externalStorageTypes")
    def external_storage_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failuresToTolerateAndRaidLevel")
    def failures_to_tolerate_and_raid_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failuresToTolerateAndRaidLevelList")
    def failures_to_tolerate_and_raid_level_list(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="limitingFactor")
    def limiting_factor(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memOvercommit")
    def mem_overcommit(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypes")
    def node_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> _builtins.int:
        
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
    @pulumi.getter(name="pricesTimestamp")
    def prices_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ramUtilization")
    def ram_utilization(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedInstance")
    def reserved_instance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="storageUtilization")
    def storage_utilization(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suitability(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suitabilityExplanation")
    def suitability_explanation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suitabilitySummary")
    def suitability_summary(self) -> Mapping[str, _builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalCpuCores")
    def total_cpu_cores(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalMonthlyCost")
    def total_monthly_cost(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalRamInGB")
    def total_ram_in_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStorageInGB")
    def total_storage_in_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuOversubscription")
    def vcpu_oversubscription(self) -> Optional[_builtins.float]:
        
        ...
    


class AwaitableGetAvsAssessmentsOperationResult(GetAvsAssessmentsOperationResult):
    def __await__(self): # -> Generator[Never, Any, GetAvsAssessmentsOperationResult]:
        ...
    


def get_avs_assessments_operation(assessment_name: Optional[_builtins.str] = ..., group_name: Optional[_builtins.str] = ..., project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAvsAssessmentsOperationResult:
    
    ...

def get_avs_assessments_operation_output(assessment_name: Optional[pulumi.Input[_builtins.str]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAvsAssessmentsOperationResult]:
    
    ...

