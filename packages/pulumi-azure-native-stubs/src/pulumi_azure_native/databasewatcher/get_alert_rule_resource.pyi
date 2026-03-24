

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAlertRuleResourceResult', 'AwaitableGetAlertRuleResourceResult', 'get_alert_rule_resource', 'get_alert_rule_resource_output']
@pulumi.output_type
class GetAlertRuleResourceResult:
    
    def __init__(__self__, alert_rule_resource_id=..., alert_rule_template_id=..., alert_rule_template_version=..., azure_api_version=..., created_with_properties=..., creation_time=..., id=..., name=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleResourceId")
    def alert_rule_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateId")
    def alert_rule_template_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateVersion")
    def alert_rule_template_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdWithProperties")
    def created_with_properties(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAlertRuleResourceResult(GetAlertRuleResourceResult):
    def __await__(self): # -> Generator[Never, Any, GetAlertRuleResourceResult]:
        ...
    


def get_alert_rule_resource(alert_rule_resource_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., watcher_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAlertRuleResourceResult:
    
    ...

def get_alert_rule_resource_output(alert_rule_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., watcher_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAlertRuleResourceResult]:
    
    ...

