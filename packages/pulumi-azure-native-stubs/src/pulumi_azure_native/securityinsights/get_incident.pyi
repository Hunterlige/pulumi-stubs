

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIncidentResult', 'AwaitableGetIncidentResult', 'get_incident', 'get_incident_output']
@pulumi.output_type
class GetIncidentResult:
    
    def __init__(__self__, additional_data=..., azure_api_version=..., classification=..., classification_comment=..., classification_reason=..., created_time_utc=..., description=..., etag=..., first_activity_time_utc=..., id=..., incident_number=..., incident_url=..., labels=..., last_activity_time_utc=..., last_modified_time_utc=..., name=..., owner=..., provider_incident_id=..., provider_name=..., related_analytic_rule_ids=..., severity=..., status=..., system_data=..., title=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> outputs.IncidentAdditionalDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationComment")
    def classification_comment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationReason")
    def classification_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstActivityTimeUtc")
    def first_activity_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentNumber")
    def incident_number(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentUrl")
    def incident_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[outputs.IncidentLabelResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastActivityTimeUtc")
    def last_activity_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[outputs.IncidentOwnerInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerIncidentId")
    def provider_incident_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedAnalyticRuleIds")
    def related_analytic_rule_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
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
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIncidentResult(GetIncidentResult):
    def __await__(self): # -> Generator[Never, Any, GetIncidentResult]:
        ...
    


def get_incident(incident_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIncidentResult:
    
    ...

def get_incident_output(incident_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIncidentResult]:
    
    ...

