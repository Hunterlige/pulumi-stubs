

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAlertsSuppressionRuleResult', 'AwaitableGetAlertsSuppressionRuleResult', 'get_alerts_suppression_rule', 'get_alerts_suppression_rule_output']
@pulumi.output_type
class GetAlertsSuppressionRuleResult:
    
    def __init__(__self__, alert_type=..., azure_api_version=..., comment=..., expiration_date_utc=..., id=..., last_modified_utc=..., name=..., reason=..., state=..., suppression_alerts_scope=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertType")
    def alert_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDateUtc")
    def expiration_date_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressionAlertsScope")
    def suppression_alerts_scope(self) -> Optional[outputs.SuppressionAlertsScopeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAlertsSuppressionRuleResult(GetAlertsSuppressionRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetAlertsSuppressionRuleResult]:
        ...
    


def get_alerts_suppression_rule(alerts_suppression_rule_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAlertsSuppressionRuleResult:
    
    ...

def get_alerts_suppression_rule_output(alerts_suppression_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAlertsSuppressionRuleResult]:
    
    ...

