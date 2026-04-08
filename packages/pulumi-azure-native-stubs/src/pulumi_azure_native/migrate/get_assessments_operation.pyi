import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAssessmentsOperationResult",
    "AwaitableGetAssessmentsOperationResult",
    "get_assessments_operation",
    "get_assessments_operation_output",
]

@pulumi.output_type
class GetAssessmentsOperationResult:
    def __init__(
        __self__,
        assessment_error_summary=...,
        assessment_type=...,
        azure_api_version=...,
        azure_disk_types=...,
        azure_hybrid_use_benefit=...,
        azure_location=...,
        azure_offer_code=...,
        azure_pricing_tier=...,
        azure_storage_redundancy=...,
        azure_vm_families=...,
        confidence_rating_in_percentage=...,
        cost_components=...,
        created_timestamp=...,
        currency=...,
        discount_percentage=...,
        distribution_by_os_name=...,
        distribution_by_service_pack_insight=...,
        distribution_by_support_status=...,
        ea_subscription_id=...,
        group_type=...,
        id=...,
        linux_azure_hybrid_use_benefit=...,
        monthly_bandwidth_cost=...,
        monthly_compute_cost=...,
        monthly_premium_storage_cost=...,
        monthly_standard_ssd_storage_cost=...,
        monthly_storage_cost=...,
        monthly_ultra_storage_cost=...,
        name=...,
        number_of_machines=...,
        percentile=...,
        perf_data_end_time=...,
        perf_data_start_time=...,
        prices_timestamp=...,
        provisioning_state=...,
        reserved_instance=...,
        scaling_factor=...,
        schema_version=...,
        sizing_criterion=...,
        stage=...,
        status=...,
        suitability_summary=...,
        system_data=...,
        time_range=...,
        type=...,
        updated_timestamp=...,
        vm_uptime=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentErrorSummary")
    def assessment_error_summary(self) -> Mapping[str, _builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureDiskTypes")
    def azure_disk_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureHybridUseBenefit")
    def azure_hybrid_use_benefit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azurePricingTier")
    def azure_pricing_tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureStorageRedundancy")
    def azure_storage_redundancy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureVmFamilies")
    def azure_vm_families(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="costComponents")
    def cost_components(self) -> Sequence[outputs.CostComponentResponse]: ...
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def currency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="distributionByOsName")
    def distribution_by_os_name(self) -> Mapping[str, _builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="distributionByServicePackInsight")
    def distribution_by_service_pack_insight(self) -> Mapping[str, _builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="distributionBySupportStatus")
    def distribution_by_support_status(self) -> Mapping[str, _builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="eaSubscriptionId")
    def ea_subscription_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linuxAzureHybridUseBenefit")
    def linux_azure_hybrid_use_benefit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="monthlyBandwidthCost")
    def monthly_bandwidth_cost(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="monthlyComputeCost")
    def monthly_compute_cost(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="monthlyPremiumStorageCost")
    def monthly_premium_storage_cost(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="monthlyStandardSsdStorageCost")
    def monthly_standard_ssd_storage_cost(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="monthlyStorageCost")
    def monthly_storage_cost(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="monthlyUltraStorageCost")
    def monthly_ultra_storage_cost(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def percentile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="perfDataEndTime")
    def perf_data_end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="perfDataStartTime")
    def perf_data_start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pricesTimestamp")
    def prices_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reservedInstance")
    def reserved_instance(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="suitabilitySummary")
    def suitability_summary(self) -> Mapping[str, _builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vmUptime")
    def vm_uptime(self) -> Optional[outputs.VmUptimeResponse]: ...

class AwaitableGetAssessmentsOperationResult(GetAssessmentsOperationResult):
    def __await__(self): ...

def get_assessments_operation(
    assessment_name: Optional[_builtins.str] = ...,
    group_name: Optional[_builtins.str] = ...,
    project_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAssessmentsOperationResult: ...
def get_assessments_operation_output(
    assessment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAssessmentsOperationResult]: ...
