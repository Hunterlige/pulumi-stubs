

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
__all__ = ['AssessmentsOperationArgs', 'AssessmentsOperation']
@pulumi.input_type
class AssessmentsOperationArgs:
    def __init__(__self__, *, group_name: pulumi.Input[_builtins.str], project_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], assessment_name: Optional[pulumi.Input[_builtins.str]] = ..., azure_disk_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureDiskType]]]]] = ..., azure_hybrid_use_benefit: Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]] = ..., azure_location: Optional[pulumi.Input[_builtins.str]] = ..., azure_offer_code: Optional[pulumi.Input[Union[_builtins.str, AzureOfferCode]]] = ..., azure_pricing_tier: Optional[pulumi.Input[Union[_builtins.str, AzurePricingTier]]] = ..., azure_storage_redundancy: Optional[pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]] = ..., azure_vm_families: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]] = ..., currency: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]] = ..., discount_percentage: Optional[pulumi.Input[_builtins.float]] = ..., ea_subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., linux_azure_hybrid_use_benefit: Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]] = ..., percentile: Optional[pulumi.Input[Union[_builtins.str, Percentile]]] = ..., perf_data_end_time: Optional[pulumi.Input[_builtins.str]] = ..., perf_data_start_time: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]] = ..., reserved_instance: Optional[pulumi.Input[Union[_builtins.str, AzureReservedInstance]]] = ..., scaling_factor: Optional[pulumi.Input[_builtins.float]] = ..., sizing_criterion: Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]] = ..., time_range: Optional[pulumi.Input[Union[_builtins.str, TimeRange]]] = ..., vm_uptime: Optional[pulumi.Input[VmUptimeArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="azureDiskTypes")
    def azure_disk_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureDiskType]]]]]:
        
        ...
    
    @azure_disk_types.setter
    def azure_disk_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureDiskType]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureHybridUseBenefit")
    def azure_hybrid_use_benefit(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]]:
        
        ...
    
    @azure_hybrid_use_benefit.setter
    def azure_hybrid_use_benefit(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @azure_location.setter
    def azure_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureOfferCode]]]:
        
        ...
    
    @azure_offer_code.setter
    def azure_offer_code(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureOfferCode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azurePricingTier")
    def azure_pricing_tier(self) -> Optional[pulumi.Input[Union[_builtins.str, AzurePricingTier]]]:
        
        ...
    
    @azure_pricing_tier.setter
    def azure_pricing_tier(self, value: Optional[pulumi.Input[Union[_builtins.str, AzurePricingTier]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureStorageRedundancy")
    def azure_storage_redundancy(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]]:
        
        ...
    
    @azure_storage_redundancy.setter
    def azure_storage_redundancy(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVmFamilies")
    def azure_vm_families(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]]:
        
        ...
    
    @azure_vm_families.setter
    def azure_vm_families(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]:
        
        ...
    
    @currency.setter
    def currency(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eaSubscriptionId")
    def ea_subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ea_subscription_id.setter
    def ea_subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxAzureHybridUseBenefit")
    def linux_azure_hybrid_use_benefit(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]]:
        
        ...
    
    @linux_azure_hybrid_use_benefit.setter
    def linux_azure_hybrid_use_benefit(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]]): # -> None:
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
    @pulumi.getter(name="vmUptime")
    def vm_uptime(self) -> Optional[pulumi.Input[VmUptimeArgs]]:
        
        ...
    
    @vm_uptime.setter
    def vm_uptime(self, value: Optional[pulumi.Input[VmUptimeArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:migrate:AssessmentsOperation")
class AssessmentsOperation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assessment_name: Optional[pulumi.Input[_builtins.str]] = ..., azure_disk_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureDiskType]]]]] = ..., azure_hybrid_use_benefit: Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]] = ..., azure_location: Optional[pulumi.Input[_builtins.str]] = ..., azure_offer_code: Optional[pulumi.Input[Union[_builtins.str, AzureOfferCode]]] = ..., azure_pricing_tier: Optional[pulumi.Input[Union[_builtins.str, AzurePricingTier]]] = ..., azure_storage_redundancy: Optional[pulumi.Input[Union[_builtins.str, AzureStorageRedundancy]]] = ..., azure_vm_families: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AzureVmFamily]]]]] = ..., currency: Optional[pulumi.Input[Union[_builtins.str, AzureCurrency]]] = ..., discount_percentage: Optional[pulumi.Input[_builtins.float]] = ..., ea_subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., linux_azure_hybrid_use_benefit: Optional[pulumi.Input[Union[_builtins.str, AzureHybridUseBenefit]]] = ..., percentile: Optional[pulumi.Input[Union[_builtins.str, Percentile]]] = ..., perf_data_end_time: Optional[pulumi.Input[_builtins.str]] = ..., perf_data_start_time: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]] = ..., reserved_instance: Optional[pulumi.Input[Union[_builtins.str, AzureReservedInstance]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scaling_factor: Optional[pulumi.Input[_builtins.float]] = ..., sizing_criterion: Optional[pulumi.Input[Union[_builtins.str, AssessmentSizingCriterion]]] = ..., time_range: Optional[pulumi.Input[Union[_builtins.str, TimeRange]]] = ..., vm_uptime: Optional[pulumi.Input[Union[VmUptimeArgs, VmUptimeArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AssessmentsOperationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AssessmentsOperation:
        
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
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDiskTypes")
    def azure_disk_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureHybridUseBenefit")
    def azure_hybrid_use_benefit(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="azurePricingTier")
    def azure_pricing_tier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureStorageRedundancy")
    def azure_storage_redundancy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVmFamilies")
    def azure_vm_families(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
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
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionByOsName")
    def distribution_by_os_name(self) -> pulumi.Output[Mapping[str, _builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionByServicePackInsight")
    def distribution_by_service_pack_insight(self) -> pulumi.Output[Mapping[str, _builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionBySupportStatus")
    def distribution_by_support_status(self) -> pulumi.Output[Mapping[str, _builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eaSubscriptionId")
    def ea_subscription_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxAzureHybridUseBenefit")
    def linux_azure_hybrid_use_benefit(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyBandwidthCost")
    def monthly_bandwidth_cost(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyComputeCost")
    def monthly_compute_cost(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyPremiumStorageCost")
    def monthly_premium_storage_cost(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyStandardSsdStorageCost")
    def monthly_standard_ssd_storage_cost(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyStorageCost")
    def monthly_storage_cost(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyUltraStorageCost")
    def monthly_ultra_storage_cost(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> pulumi.Output[_builtins.int]:
        
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
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmUptime")
    def vm_uptime(self) -> pulumi.Output[Optional[outputs.VmUptimeResponseV1]]:
        
        ...
    


