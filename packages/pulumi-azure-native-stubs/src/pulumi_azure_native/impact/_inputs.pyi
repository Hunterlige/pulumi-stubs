

import builtins as _builtins
import sys
import pulumi
from typing import Any, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClientIncidentDetailsArgs', 'ClientIncidentDetailsArgsDict', 'ConnectivityArgs', 'ConnectivityArgsDict', 'ConnectorPropertiesArgs', 'ConnectorPropertiesArgsDict', 'ContentArgs', 'ContentArgsDict', 'ErrorDetailPropertiesArgs', 'ErrorDetailPropertiesArgsDict', 'ExpectedValueRangeArgs', 'ExpectedValueRangeArgsDict', 'ImpactDetailsArgs', 'ImpactDetailsArgsDict', 'InsightPropertiesArgs', 'InsightPropertiesArgsDict', 'PerformanceArgs', 'PerformanceArgsDict', 'SourceOrTargetArgs', 'SourceOrTargetArgsDict', 'WorkloadImpactPropertiesArgs', 'WorkloadImpactPropertiesArgsDict', 'WorkloadArgs', 'WorkloadArgsDict']
class ClientIncidentDetailsArgsDict(TypedDict):
    
    client_incident_id: NotRequired[pulumi.Input[_builtins.str]]
    client_incident_source: NotRequired[pulumi.Input[Union[_builtins.str, IncidentSource]]]


@pulumi.input_type
class ClientIncidentDetailsArgs:
    def __init__(__self__, *, client_incident_id: Optional[pulumi.Input[_builtins.str]] = ..., client_incident_source: Optional[pulumi.Input[Union[_builtins.str, IncidentSource]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIncidentId")
    def client_incident_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_incident_id.setter
    def client_incident_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIncidentSource")
    def client_incident_source(self) -> Optional[pulumi.Input[Union[_builtins.str, IncidentSource]]]:
        
        ...
    
    @client_incident_source.setter
    def client_incident_source(self, value: Optional[pulumi.Input[Union[_builtins.str, IncidentSource]]]): # -> None:
        ...
    


class ConnectivityArgsDict(TypedDict):
    
    port: NotRequired[pulumi.Input[_builtins.int]]
    protocol: NotRequired[pulumi.Input[Union[_builtins.str, Protocol]]]
    source: NotRequired[pulumi.Input[SourceOrTargetArgsDict]]
    target: NotRequired[pulumi.Input[SourceOrTargetArgsDict]]


@pulumi.input_type
class ConnectivityArgs:
    def __init__(__self__, *, port: Optional[pulumi.Input[_builtins.int]] = ..., protocol: Optional[pulumi.Input[Union[_builtins.str, Protocol]]] = ..., source: Optional[pulumi.Input[SourceOrTargetArgs]] = ..., target: Optional[pulumi.Input[SourceOrTargetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[Union[_builtins.str, Protocol]]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[Union[_builtins.str, Protocol]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[SourceOrTargetArgs]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[SourceOrTargetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[SourceOrTargetArgs]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[SourceOrTargetArgs]]): # -> None:
        ...
    


class ConnectorPropertiesArgsDict(TypedDict):
    
    connector_type: pulumi.Input[Union[_builtins.str, Platform]]


@pulumi.input_type
class ConnectorPropertiesArgs:
    def __init__(__self__, *, connector_type: pulumi.Input[Union[_builtins.str, Platform]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Input[Union[_builtins.str, Platform]]:
        
        ...
    
    @connector_type.setter
    def connector_type(self, value: pulumi.Input[Union[_builtins.str, Platform]]): # -> None:
        ...
    


class ContentArgsDict(TypedDict):
    
    description: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]


@pulumi.input_type
class ContentArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ErrorDetailPropertiesArgsDict(TypedDict):
    
    error_code: NotRequired[pulumi.Input[_builtins.str]]
    error_message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ErrorDetailPropertiesArgs:
    def __init__(__self__, *, error_code: Optional[pulumi.Input[_builtins.str]] = ..., error_message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_code.setter
    def error_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExpectedValueRangeArgsDict(TypedDict):
    
    max: pulumi.Input[_builtins.float]
    min: pulumi.Input[_builtins.float]


@pulumi.input_type
class ExpectedValueRangeArgs:
    def __init__(__self__, *, max: pulumi.Input[_builtins.float], min: pulumi.Input[_builtins.float]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @max.setter
    def max(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @min.setter
    def min(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    


class ImpactDetailsArgsDict(TypedDict):
    
    impact_id: pulumi.Input[_builtins.str]
    impacted_resource_id: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[_builtins.str]
    end_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ImpactDetailsArgs:
    def __init__(__self__, *, impact_id: pulumi.Input[_builtins.str], impacted_resource_id: pulumi.Input[_builtins.str], start_time: pulumi.Input[_builtins.str], end_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="impactId")
    def impact_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @impact_id.setter
    def impact_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="impactedResourceId")
    def impacted_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @impacted_resource_id.setter
    def impacted_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InsightPropertiesArgsDict(TypedDict):
    
    category: pulumi.Input[_builtins.str]
    content: pulumi.Input[ContentArgsDict]
    impact: pulumi.Input[ImpactDetailsArgsDict]
    insight_unique_id: pulumi.Input[_builtins.str]
    additional_details: NotRequired[Any]
    event_id: NotRequired[pulumi.Input[_builtins.str]]
    event_time: NotRequired[pulumi.Input[_builtins.str]]
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InsightPropertiesArgs:
    def __init__(__self__, *, category: pulumi.Input[_builtins.str], content: pulumi.Input[ContentArgs], impact: pulumi.Input[ImpactDetailsArgs], insight_unique_id: pulumi.Input[_builtins.str], additional_details: Optional[Any] = ..., event_id: Optional[pulumi.Input[_builtins.str]] = ..., event_time: Optional[pulumi.Input[_builtins.str]] = ..., group_id: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @category.setter
    def category(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Input[ContentArgs]:
        
        ...
    
    @content.setter
    def content(self, value: pulumi.Input[ContentArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def impact(self) -> pulumi.Input[ImpactDetailsArgs]:
        
        ...
    
    @impact.setter
    def impact(self, value: pulumi.Input[ImpactDetailsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightUniqueId")
    def insight_unique_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @insight_unique_id.setter
    def insight_unique_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Optional[Any]:
        
        ...
    
    @additional_details.setter
    def additional_details(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventId")
    def event_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_id.setter
    def event_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_time.setter
    def event_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PerformanceArgsDict(TypedDict):
    
    actual: NotRequired[pulumi.Input[_builtins.float]]
    expected: NotRequired[pulumi.Input[_builtins.float]]
    expected_value_range: NotRequired[pulumi.Input[ExpectedValueRangeArgsDict]]
    metric_name: NotRequired[pulumi.Input[_builtins.str]]
    unit: NotRequired[pulumi.Input[Union[_builtins.str, MetricUnit]]]


@pulumi.input_type
class PerformanceArgs:
    def __init__(__self__, *, actual: Optional[pulumi.Input[_builtins.float]] = ..., expected: Optional[pulumi.Input[_builtins.float]] = ..., expected_value_range: Optional[pulumi.Input[ExpectedValueRangeArgs]] = ..., metric_name: Optional[pulumi.Input[_builtins.str]] = ..., unit: Optional[pulumi.Input[Union[_builtins.str, MetricUnit]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actual(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @actual.setter
    def actual(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expected(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @expected.setter
    def expected(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedValueRange")
    def expected_value_range(self) -> Optional[pulumi.Input[ExpectedValueRangeArgs]]:
        
        ...
    
    @expected_value_range.setter
    def expected_value_range(self, value: Optional[pulumi.Input[ExpectedValueRangeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[Union[_builtins.str, MetricUnit]]]:
        
        ...
    
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[Union[_builtins.str, MetricUnit]]]): # -> None:
        ...
    


class SourceOrTargetArgsDict(TypedDict):
    
    azure_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SourceOrTargetArgs:
    def __init__(__self__, *, azure_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureResourceId")
    def azure_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @azure_resource_id.setter
    def azure_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkloadImpactPropertiesArgsDict(TypedDict):
    
    impact_category: pulumi.Input[_builtins.str]
    impacted_resource_id: pulumi.Input[_builtins.str]
    start_date_time: pulumi.Input[_builtins.str]
    additional_properties: NotRequired[Any]
    arm_correlation_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    client_incident_details: NotRequired[pulumi.Input[ClientIncidentDetailsArgsDict]]
    confidence_level: NotRequired[pulumi.Input[Union[_builtins.str, ConfidenceLevel]]]
    connectivity: NotRequired[pulumi.Input[ConnectivityArgsDict]]
    end_date_time: NotRequired[pulumi.Input[_builtins.str]]
    error_details: NotRequired[pulumi.Input[ErrorDetailPropertiesArgsDict]]
    impact_description: NotRequired[pulumi.Input[_builtins.str]]
    impact_group_id: NotRequired[pulumi.Input[_builtins.str]]
    performance: NotRequired[pulumi.Input[Sequence[pulumi.Input[PerformanceArgsDict]]]]
    workload: NotRequired[pulumi.Input[WorkloadArgsDict]]


@pulumi.input_type
class WorkloadImpactPropertiesArgs:
    def __init__(__self__, *, impact_category: pulumi.Input[_builtins.str], impacted_resource_id: pulumi.Input[_builtins.str], start_date_time: pulumi.Input[_builtins.str], additional_properties: Optional[Any] = ..., arm_correlation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., client_incident_details: Optional[pulumi.Input[ClientIncidentDetailsArgs]] = ..., confidence_level: Optional[pulumi.Input[Union[_builtins.str, ConfidenceLevel]]] = ..., connectivity: Optional[pulumi.Input[ConnectivityArgs]] = ..., end_date_time: Optional[pulumi.Input[_builtins.str]] = ..., error_details: Optional[pulumi.Input[ErrorDetailPropertiesArgs]] = ..., impact_description: Optional[pulumi.Input[_builtins.str]] = ..., impact_group_id: Optional[pulumi.Input[_builtins.str]] = ..., performance: Optional[pulumi.Input[Sequence[pulumi.Input[PerformanceArgs]]]] = ..., workload: Optional[pulumi.Input[WorkloadArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="impactCategory")
    def impact_category(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @impact_category.setter
    def impact_category(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="impactedResourceId")
    def impacted_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @impacted_resource_id.setter
    def impacted_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @start_date_time.setter
    def start_date_time(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[Any]:
        
        ...
    
    @additional_properties.setter
    def additional_properties(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="armCorrelationIds")
    def arm_correlation_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @arm_correlation_ids.setter
    def arm_correlation_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIncidentDetails")
    def client_incident_details(self) -> Optional[pulumi.Input[ClientIncidentDetailsArgs]]:
        
        ...
    
    @client_incident_details.setter
    def client_incident_details(self, value: Optional[pulumi.Input[ClientIncidentDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[pulumi.Input[Union[_builtins.str, ConfidenceLevel]]]:
        
        ...
    
    @confidence_level.setter
    def confidence_level(self, value: Optional[pulumi.Input[Union[_builtins.str, ConfidenceLevel]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def connectivity(self) -> Optional[pulumi.Input[ConnectivityArgs]]:
        
        ...
    
    @connectivity.setter
    def connectivity(self, value: Optional[pulumi.Input[ConnectivityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDateTime")
    def end_date_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_date_time.setter
    def end_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> Optional[pulumi.Input[ErrorDetailPropertiesArgs]]:
        
        ...
    
    @error_details.setter
    def error_details(self, value: Optional[pulumi.Input[ErrorDetailPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="impactDescription")
    def impact_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @impact_description.setter
    def impact_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="impactGroupId")
    def impact_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @impact_group_id.setter
    def impact_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def performance(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PerformanceArgs]]]]:
        
        ...
    
    @performance.setter
    def performance(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PerformanceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def workload(self) -> Optional[pulumi.Input[WorkloadArgs]]:
        
        ...
    
    @workload.setter
    def workload(self, value: Optional[pulumi.Input[WorkloadArgs]]): # -> None:
        ...
    


class WorkloadArgsDict(TypedDict):
    
    context: NotRequired[pulumi.Input[_builtins.str]]
    toolset: NotRequired[pulumi.Input[Union[_builtins.str, Toolset]]]


@pulumi.input_type
class WorkloadArgs:
    def __init__(__self__, *, context: Optional[pulumi.Input[_builtins.str]] = ..., toolset: Optional[pulumi.Input[Union[_builtins.str, Toolset]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> Optional[pulumi.Input[Union[_builtins.str, Toolset]]]:
        
        ...
    
    @toolset.setter
    def toolset(self, value: Optional[pulumi.Input[Union[_builtins.str, Toolset]]]): # -> None:
        ...
    


