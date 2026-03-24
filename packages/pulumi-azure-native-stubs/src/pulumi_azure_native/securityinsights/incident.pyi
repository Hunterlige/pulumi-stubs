

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IncidentArgs', 'Incident']
@pulumi.input_type
class IncidentArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], severity: pulumi.Input[Union[_builtins.str, IncidentSeverity]], status: pulumi.Input[Union[_builtins.str, IncidentStatus]], title: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], classification: Optional[pulumi.Input[Union[_builtins.str, IncidentClassification]]] = ..., classification_comment: Optional[pulumi.Input[_builtins.str]] = ..., classification_reason: Optional[pulumi.Input[Union[_builtins.str, IncidentClassificationReason]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., first_activity_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., incident_id: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[IncidentLabelArgs]]]] = ..., last_activity_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[IncidentOwnerInfoArgs]] = ...) -> None:
        
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
    def severity(self) -> pulumi.Input[Union[_builtins.str, IncidentSeverity]]:
        
        ...
    
    @severity.setter
    def severity(self, value: pulumi.Input[Union[_builtins.str, IncidentSeverity]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[_builtins.str, IncidentStatus]]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[Union[_builtins.str, IncidentStatus]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[pulumi.Input[Union[_builtins.str, IncidentClassification]]]:
        
        ...
    
    @classification.setter
    def classification(self, value: Optional[pulumi.Input[Union[_builtins.str, IncidentClassification]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationComment")
    def classification_comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @classification_comment.setter
    def classification_comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationReason")
    def classification_reason(self) -> Optional[pulumi.Input[Union[_builtins.str, IncidentClassificationReason]]]:
        
        ...
    
    @classification_reason.setter
    def classification_reason(self, value: Optional[pulumi.Input[Union[_builtins.str, IncidentClassificationReason]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstActivityTimeUtc")
    def first_activity_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_activity_time_utc.setter
    def first_activity_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentId")
    def incident_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @incident_id.setter
    def incident_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IncidentLabelArgs]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IncidentLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastActivityTimeUtc")
    def last_activity_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_activity_time_utc.setter
    def last_activity_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[IncidentOwnerInfoArgs]]:
        
        ...
    
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[IncidentOwnerInfoArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:securityinsights:Incident")
class Incident(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., classification: Optional[pulumi.Input[Union[_builtins.str, IncidentClassification]]] = ..., classification_comment: Optional[pulumi.Input[_builtins.str]] = ..., classification_reason: Optional[pulumi.Input[Union[_builtins.str, IncidentClassificationReason]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., first_activity_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., incident_id: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IncidentLabelArgs, IncidentLabelArgsDict]]]]] = ..., last_activity_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[Union[IncidentOwnerInfoArgs, IncidentOwnerInfoArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., severity: Optional[pulumi.Input[Union[_builtins.str, IncidentSeverity]]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, IncidentStatus]]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IncidentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Incident:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> pulumi.Output[outputs.IncidentAdditionalDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classification(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationComment")
    def classification_comment(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationReason")
    def classification_reason(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstActivityTimeUtc")
    def first_activity_time_utc(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentNumber")
    def incident_number(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentUrl")
    def incident_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[outputs.IncidentLabelResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastActivityTimeUtc")
    def last_activity_time_utc(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Output[Optional[outputs.IncidentOwnerInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerIncidentId")
    def provider_incident_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedAnalyticRuleIds")
    def related_analytic_rule_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


