

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
__all__ = ['ScheduledAlertRuleArgs', 'ScheduledAlertRule']
@pulumi.input_type
class ScheduledAlertRuleArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], enabled: pulumi.Input[_builtins.bool], kind: pulumi.Input[_builtins.str], query: pulumi.Input[_builtins.str], query_frequency: pulumi.Input[_builtins.str], query_period: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], severity: pulumi.Input[Union[_builtins.str, AlertSeverity]], suppression_duration: pulumi.Input[_builtins.str], suppression_enabled: pulumi.Input[_builtins.bool], trigger_operator: pulumi.Input[TriggerOperator], trigger_threshold: pulumi.Input[_builtins.int], workspace_name: pulumi.Input[_builtins.str], alert_details_override: Optional[pulumi.Input[AlertDetailsOverrideArgs]] = ..., alert_rule_template_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_details: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., entity_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[EntityMappingArgs]]]] = ..., event_grouping_settings: Optional[pulumi.Input[EventGroupingSettingsArgs]] = ..., incident_configuration: Optional[pulumi.Input[IncidentConfigurationArgs]] = ..., rule_id: Optional[pulumi.Input[_builtins.str]] = ..., tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AttackTactic]]]]] = ..., techniques: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., template_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFrequency")
    def query_frequency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @query_frequency.setter
    def query_frequency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryPeriod")
    def query_period(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @query_period.setter
    def query_period(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[Union[_builtins.str, AlertSeverity]]:
        
        ...
    
    @severity.setter
    def severity(self, value: pulumi.Input[Union[_builtins.str, AlertSeverity]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressionDuration")
    def suppression_duration(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @suppression_duration.setter
    def suppression_duration(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressionEnabled")
    def suppression_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @suppression_enabled.setter
    def suppression_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerOperator")
    def trigger_operator(self) -> pulumi.Input[TriggerOperator]:
        
        ...
    
    @trigger_operator.setter
    def trigger_operator(self, value: pulumi.Input[TriggerOperator]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerThreshold")
    def trigger_threshold(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @trigger_threshold.setter
    def trigger_threshold(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertDetailsOverride")
    def alert_details_override(self) -> Optional[pulumi.Input[AlertDetailsOverrideArgs]]:
        
        ...
    
    @alert_details_override.setter
    def alert_details_override(self, value: Optional[pulumi.Input[AlertDetailsOverrideArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateName")
    def alert_rule_template_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alert_rule_template_name.setter
    def alert_rule_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDetails")
    def custom_details(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @custom_details.setter
    def custom_details(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityMappings")
    def entity_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EntityMappingArgs]]]]:
        
        ...
    
    @entity_mappings.setter
    def entity_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EntityMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventGroupingSettings")
    def event_grouping_settings(self) -> Optional[pulumi.Input[EventGroupingSettingsArgs]]:
        
        ...
    
    @event_grouping_settings.setter
    def event_grouping_settings(self, value: Optional[pulumi.Input[EventGroupingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentConfiguration")
    def incident_configuration(self) -> Optional[pulumi.Input[IncidentConfigurationArgs]]:
        
        ...
    
    @incident_configuration.setter
    def incident_configuration(self, value: Optional[pulumi.Input[IncidentConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tactics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AttackTactic]]]]]:
        
        ...
    
    @tactics.setter
    def tactics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AttackTactic]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def techniques(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @techniques.setter
    def techniques(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateVersion")
    def template_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_version.setter
    def template_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:securityinsights:ScheduledAlertRule")
class ScheduledAlertRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., alert_details_override: Optional[pulumi.Input[Union[AlertDetailsOverrideArgs, AlertDetailsOverrideArgsDict]]] = ..., alert_rule_template_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_details: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., entity_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EntityMappingArgs, EntityMappingArgsDict]]]]] = ..., event_grouping_settings: Optional[pulumi.Input[Union[EventGroupingSettingsArgs, EventGroupingSettingsArgsDict]]] = ..., incident_configuration: Optional[pulumi.Input[Union[IncidentConfigurationArgs, IncidentConfigurationArgsDict]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., query: Optional[pulumi.Input[_builtins.str]] = ..., query_frequency: Optional[pulumi.Input[_builtins.str]] = ..., query_period: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_id: Optional[pulumi.Input[_builtins.str]] = ..., severity: Optional[pulumi.Input[Union[_builtins.str, AlertSeverity]]] = ..., suppression_duration: Optional[pulumi.Input[_builtins.str]] = ..., suppression_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AttackTactic]]]]] = ..., techniques: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., template_version: Optional[pulumi.Input[_builtins.str]] = ..., trigger_operator: Optional[pulumi.Input[TriggerOperator]] = ..., trigger_threshold: Optional[pulumi.Input[_builtins.int]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ScheduledAlertRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ScheduledAlertRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertDetailsOverride")
    def alert_details_override(self) -> pulumi.Output[Optional[outputs.AlertDetailsOverrideResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateName")
    def alert_rule_template_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDetails")
    def custom_details(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityMappings")
    def entity_mappings(self) -> pulumi.Output[Optional[Sequence[outputs.EntityMappingResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventGroupingSettings")
    def event_grouping_settings(self) -> pulumi.Output[Optional[outputs.EventGroupingSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentConfiguration")
    def incident_configuration(self) -> pulumi.Output[Optional[outputs.IncidentConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFrequency")
    def query_frequency(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryPeriod")
    def query_period(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressionDuration")
    def suppression_duration(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressionEnabled")
    def suppression_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tactics(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def techniques(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateVersion")
    def template_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerOperator")
    def trigger_operator(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerThreshold")
    def trigger_threshold(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


