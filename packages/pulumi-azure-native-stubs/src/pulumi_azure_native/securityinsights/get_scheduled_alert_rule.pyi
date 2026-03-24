

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetScheduledAlertRuleResult', 'AwaitableGetScheduledAlertRuleResult', 'get_scheduled_alert_rule', 'get_scheduled_alert_rule_output']
@pulumi.output_type
class GetScheduledAlertRuleResult:
    
    def __init__(__self__, alert_details_override=..., alert_rule_template_name=..., azure_api_version=..., custom_details=..., description=..., display_name=..., enabled=..., entity_mappings=..., etag=..., event_grouping_settings=..., id=..., incident_configuration=..., kind=..., last_modified_utc=..., name=..., query=..., query_frequency=..., query_period=..., severity=..., suppression_duration=..., suppression_enabled=..., system_data=..., tactics=..., techniques=..., template_version=..., trigger_operator=..., trigger_threshold=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertDetailsOverride")
    def alert_details_override(self) -> Optional[outputs.AlertDetailsOverrideResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateName")
    def alert_rule_template_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDetails")
    def custom_details(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityMappings")
    def entity_mappings(self) -> Optional[Sequence[outputs.EntityMappingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventGroupingSettings")
    def event_grouping_settings(self) -> Optional[outputs.EventGroupingSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentConfiguration")
    def incident_configuration(self) -> Optional[outputs.IncidentConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFrequency")
    def query_frequency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryPeriod")
    def query_period(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressionDuration")
    def suppression_duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressionEnabled")
    def suppression_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tactics(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def techniques(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateVersion")
    def template_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerOperator")
    def trigger_operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerThreshold")
    def trigger_threshold(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetScheduledAlertRuleResult(GetScheduledAlertRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetScheduledAlertRuleResult]:
        ...
    


def get_scheduled_alert_rule(resource_group_name: Optional[_builtins.str] = ..., rule_id: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetScheduledAlertRuleResult:
    
    ...

def get_scheduled_alert_rule_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_id: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetScheduledAlertRuleResult]:
    
    ...

