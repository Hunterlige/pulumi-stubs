

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSqlAssessmentV2OperationResult', 'AwaitableGetSqlAssessmentV2OperationResult', 'get_sql_assessment_v2_operation', 'get_sql_assessment_v2_operation_output']
@pulumi.output_type
class GetSqlAssessmentV2OperationResult:
    
    def __init__(__self__, assessment_type=..., async_commit_mode_intent=..., azure_api_version=..., azure_location=..., azure_offer_code=..., azure_offer_code_for_vm=..., azure_security_offering_type=..., azure_sql_database_settings=..., azure_sql_managed_instance_settings=..., azure_sql_vm_settings=..., confidence_rating_in_percentage=..., created_timestamp=..., currency=..., disaster_recovery_location=..., discount_percentage=..., ea_subscription_id=..., enable_hadr_assessment=..., entity_uptime=..., environment_type=..., group_type=..., id=..., is_internet_access_available=..., multi_subnet_intent=..., name=..., optimization_logic=..., os_license=..., percentile=..., perf_data_end_time=..., perf_data_start_time=..., prices_timestamp=..., provisioning_state=..., reserved_instance=..., reserved_instance_for_vm=..., scaling_factor=..., schema_version=..., sizing_criterion=..., sql_server_license=..., stage=..., status=..., system_data=..., time_range=..., type=..., updated_timestamp=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncCommitModeIntent")
    def async_commit_mode_intent(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="azureOfferCodeForVm")
    def azure_offer_code_for_vm(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSecurityOfferingType")
    def azure_security_offering_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlDatabaseSettings")
    def azure_sql_database_settings(self) -> Optional[outputs.SqlDbSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlManagedInstanceSettings")
    def azure_sql_managed_instance_settings(self) -> Optional[outputs.SqlMiSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlVmSettings")
    def azure_sql_vm_settings(self) -> Optional[outputs.SqlVmSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> Optional[_builtins.float]:
        
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
    @pulumi.getter(name="disasterRecoveryLocation")
    def disaster_recovery_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eaSubscriptionId")
    def ea_subscription_id(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optimizationLogic")
    def optimization_logic(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osLicense")
    def os_license(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="reservedInstance")
    def reserved_instance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedInstanceForVm")
    def reserved_instance_for_vm(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="sqlServerLicense")
    def sql_server_license(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSqlAssessmentV2OperationResult(GetSqlAssessmentV2OperationResult):
    def __await__(self): # -> Generator[Never, Any, GetSqlAssessmentV2OperationResult]:
        ...
    


def get_sql_assessment_v2_operation(assessment_name: Optional[_builtins.str] = ..., group_name: Optional[_builtins.str] = ..., project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSqlAssessmentV2OperationResult:
    
    ...

def get_sql_assessment_v2_operation_output(assessment_name: Optional[pulumi.Input[_builtins.str]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSqlAssessmentV2OperationResult]:
    
    ...

