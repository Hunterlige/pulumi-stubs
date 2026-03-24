

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppAssessmentV2OperationResult', 'AwaitableGetWebAppAssessmentV2OperationResult', 'get_web_app_assessment_v2_operation', 'get_web_app_assessment_v2_operation_output']
@pulumi.output_type
class GetWebAppAssessmentV2OperationResult:
    
    def __init__(__self__, app_svc_container_settings=..., app_svc_native_settings=..., assessment_type=..., azure_api_version=..., azure_location=..., azure_offer_code=..., azure_security_offering_type=..., confidence_rating_in_percentage=..., created_timestamp=..., currency=..., discount_percentage=..., discovered_entity_light_summary=..., ea_subscription_id=..., entity_uptime=..., environment_type=..., group_type=..., id=..., name=..., percentile=..., perf_data_end_time=..., perf_data_start_time=..., prices_timestamp=..., provisioning_state=..., reserved_instance=..., scaling_factor=..., schema_version=..., sizing_criterion=..., stage=..., status=..., system_data=..., time_range=..., type=..., updated_timestamp=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSvcContainerSettings")
    def app_svc_container_settings(self) -> Optional[outputs.AppSvcContainerSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSvcNativeSettings")
    def app_svc_native_settings(self) -> Optional[outputs.AppSvcNativeSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="azureSecurityOfferingType")
    def azure_security_offering_type(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredEntityLightSummary")
    def discovered_entity_light_summary(self) -> Optional[outputs.DiscoveredEntityLightSummaryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eaSubscriptionId")
    def ea_subscription_id(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter
    def name(self) -> _builtins.str:
        
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
    def provisioning_state(self) -> _builtins.str:
        
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
    


class AwaitableGetWebAppAssessmentV2OperationResult(GetWebAppAssessmentV2OperationResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppAssessmentV2OperationResult]:
        ...
    


def get_web_app_assessment_v2_operation(assessment_name: Optional[_builtins.str] = ..., group_name: Optional[_builtins.str] = ..., project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppAssessmentV2OperationResult:
    
    ...

def get_web_app_assessment_v2_operation_output(assessment_name: Optional[pulumi.Input[_builtins.str]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppAssessmentV2OperationResult]:
    
    ...

