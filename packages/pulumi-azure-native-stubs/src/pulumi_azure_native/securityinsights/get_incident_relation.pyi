

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIncidentRelationResult', 'AwaitableGetIncidentRelationResult', 'get_incident_relation', 'get_incident_relation_output']
@pulumi.output_type
class GetIncidentRelationResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., name=..., related_resource_id=..., related_resource_kind=..., related_resource_name=..., related_resource_type=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="relatedResourceId")
    def related_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedResourceKind")
    def related_resource_kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedResourceName")
    def related_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedResourceType")
    def related_resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIncidentRelationResult(GetIncidentRelationResult):
    def __await__(self): # -> Generator[Never, Any, GetIncidentRelationResult]:
        ...
    


def get_incident_relation(incident_id: Optional[_builtins.str] = ..., relation_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIncidentRelationResult:
    
    ...

def get_incident_relation_output(incident_id: Optional[pulumi.Input[_builtins.str]] = ..., relation_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIncidentRelationResult]:
    
    ...

