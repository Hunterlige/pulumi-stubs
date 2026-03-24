

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeviceSecurityGroupArgs', 'DeviceSecurityGroup']
@pulumi.input_type
class DeviceSecurityGroupArgs:
    def __init__(__self__, *, resource_id: pulumi.Input[_builtins.str], allowlist_rules: Optional[pulumi.Input[Sequence[pulumi.Input[AllowlistCustomAlertRuleArgs]]]] = ..., denylist_rules: Optional[pulumi.Input[Sequence[pulumi.Input[DenylistCustomAlertRuleArgs]]]] = ..., device_security_group_name: Optional[pulumi.Input[_builtins.str]] = ..., threshold_rules: Optional[pulumi.Input[Sequence[pulumi.Input[ThresholdCustomAlertRuleArgs]]]] = ..., time_window_rules: Optional[pulumi.Input[Sequence[pulumi.Input[TimeWindowCustomAlertRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowlistRules")
    def allowlist_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AllowlistCustomAlertRuleArgs]]]]:
        
        ...
    
    @allowlist_rules.setter
    def allowlist_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AllowlistCustomAlertRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="denylistRules")
    def denylist_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DenylistCustomAlertRuleArgs]]]]:
        
        ...
    
    @denylist_rules.setter
    def denylist_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DenylistCustomAlertRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceSecurityGroupName")
    def device_security_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_security_group_name.setter
    def device_security_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdRules")
    def threshold_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ThresholdCustomAlertRuleArgs]]]]:
        
        ...
    
    @threshold_rules.setter
    def threshold_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ThresholdCustomAlertRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeWindowRules")
    def time_window_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TimeWindowCustomAlertRuleArgs]]]]:
        
        ...
    
    @time_window_rules.setter
    def time_window_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TimeWindowCustomAlertRuleArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:security:DeviceSecurityGroup")
class DeviceSecurityGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allowlist_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AllowlistCustomAlertRuleArgs, AllowlistCustomAlertRuleArgsDict]]]]] = ..., denylist_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DenylistCustomAlertRuleArgs, DenylistCustomAlertRuleArgsDict]]]]] = ..., device_security_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., threshold_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ThresholdCustomAlertRuleArgs, ThresholdCustomAlertRuleArgsDict]]]]] = ..., time_window_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TimeWindowCustomAlertRuleArgs, TimeWindowCustomAlertRuleArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeviceSecurityGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DeviceSecurityGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowlistRules")
    def allowlist_rules(self) -> pulumi.Output[Optional[Sequence[outputs.AllowlistCustomAlertRuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denylistRules")
    def denylist_rules(self) -> pulumi.Output[Optional[Sequence[outputs.DenylistCustomAlertRuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdRules")
    def threshold_rules(self) -> pulumi.Output[Optional[Sequence[outputs.ThresholdCustomAlertRuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeWindowRules")
    def time_window_rules(self) -> pulumi.Output[Optional[Sequence[outputs.TimeWindowCustomAlertRuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


