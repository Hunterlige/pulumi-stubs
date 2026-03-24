

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResponsePlanResult', 'AwaitableGetResponsePlanResult', 'get_response_plan', 'get_response_plan_output']
@pulumi.output_type
class GetResponsePlanResult:
    
    def __init__(__self__, actions=..., arn=..., chat_channels=..., display_name=..., engagements=..., id=..., incident_templates=..., integrations=..., name=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.GetResponsePlanActionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatChannels")
    def chat_channels(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engagements(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentTemplates")
    def incident_templates(self) -> Sequence[outputs.GetResponsePlanIncidentTemplateResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def integrations(self) -> Sequence[outputs.GetResponsePlanIntegrationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetResponsePlanResult(GetResponsePlanResult):
    def __await__(self): # -> Generator[Never, Any, GetResponsePlanResult]:
        ...
    


def get_response_plan(arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResponsePlanResult:
    
    ...

def get_response_plan_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResponsePlanResult]:
    
    ...

