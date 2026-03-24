

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDeviceSecurityGroupResult', 'AwaitableGetDeviceSecurityGroupResult', 'get_device_security_group', 'get_device_security_group_output']
@pulumi.output_type
class GetDeviceSecurityGroupResult:
    
    def __init__(__self__, allowlist_rules=..., azure_api_version=..., denylist_rules=..., id=..., name=..., threshold_rules=..., time_window_rules=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowlistRules")
    def allowlist_rules(self) -> Optional[Sequence[outputs.AllowlistCustomAlertRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denylistRules")
    def denylist_rules(self) -> Optional[Sequence[outputs.DenylistCustomAlertRuleResponse]]:
        
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
    @pulumi.getter(name="thresholdRules")
    def threshold_rules(self) -> Optional[Sequence[outputs.ThresholdCustomAlertRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeWindowRules")
    def time_window_rules(self) -> Optional[Sequence[outputs.TimeWindowCustomAlertRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDeviceSecurityGroupResult(GetDeviceSecurityGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetDeviceSecurityGroupResult]:
        ...
    


def get_device_security_group(device_security_group_name: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDeviceSecurityGroupResult:
    
    ...

def get_device_security_group_output(device_security_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDeviceSecurityGroupResult]:
    
    ...

