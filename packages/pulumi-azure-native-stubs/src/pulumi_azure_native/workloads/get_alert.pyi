

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAlertResult', 'AwaitableGetAlertResult', 'get_alert', 'get_alert_output']
@pulumi.output_type
class GetAlertResult:
    
    def __init__(__self__, alert_rule_properties=..., alert_rule_resource_id=..., azure_api_version=..., errors=..., id=..., name=..., provider_names=..., provider_type=..., provisioning_state=..., system_data=..., template_name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleProperties")
    def alert_rule_properties(self) -> Optional[outputs.AlertRulePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleResourceId")
    def alert_rule_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.ErrorDetailResponse:
        
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
    @pulumi.getter(name="providerNames")
    def provider_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAlertResult(GetAlertResult):
    def __await__(self): # -> Generator[Never, Any, GetAlertResult]:
        ...
    


def get_alert(alert_name: Optional[_builtins.str] = ..., monitor_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAlertResult:
    
    ...

def get_alert_output(alert_name: Optional[pulumi.Input[_builtins.str]] = ..., monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAlertResult]:
    
    ...

