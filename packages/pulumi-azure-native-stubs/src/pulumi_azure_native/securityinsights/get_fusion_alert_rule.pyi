

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFusionAlertRuleResult', 'AwaitableGetFusionAlertRuleResult', 'get_fusion_alert_rule', 'get_fusion_alert_rule_output']
@pulumi.output_type
class GetFusionAlertRuleResult:
    
    def __init__(__self__, alert_rule_template_name=..., azure_api_version=..., description=..., display_name=..., enabled=..., etag=..., id=..., kind=..., last_modified_utc=..., name=..., severity=..., system_data=..., tactics=..., techniques=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateName")
    def alert_rule_template_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
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
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tactics(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def techniques(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFusionAlertRuleResult(GetFusionAlertRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetFusionAlertRuleResult]:
        ...
    


def get_fusion_alert_rule(resource_group_name: Optional[_builtins.str] = ..., rule_id: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFusionAlertRuleResult:
    
    ...

def get_fusion_alert_rule_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_id: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFusionAlertRuleResult]:
    
    ...

