

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAutomationRuleResult', 'AwaitableGetAutomationRuleResult', 'get_automation_rule', 'get_automation_rule_output']
@pulumi.output_type
class GetAutomationRuleResult:
    def __init__(__self__, actions=..., azure_api_version=..., created_by=..., created_time_utc=..., display_name=..., etag=..., id=..., last_modified_by=..., last_modified_time_utc=..., name=..., order=..., system_data=..., triggering_logic=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> outputs.ClientInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
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
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> outputs.ClientInfoResponse:
        
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
    def order(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggeringLogic")
    def triggering_logic(self) -> outputs.AutomationRuleTriggeringLogicResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAutomationRuleResult(GetAutomationRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetAutomationRuleResult]:
        ...
    


def get_automation_rule(automation_rule_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAutomationRuleResult:
    
    ...

def get_automation_rule_output(automation_rule_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAutomationRuleResult]:
    
    ...

