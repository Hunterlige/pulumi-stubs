

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RuleExcludeResourceTagArgs', 'RuleExcludeResourceTagArgsDict', 'RuleLockConfigurationArgs', 'RuleLockConfigurationArgsDict', 'RuleLockConfigurationUnlockDelayArgs', 'RuleLockConfigurationUnlockDelayArgsDict', 'RuleResourceTagArgs', 'RuleResourceTagArgsDict', 'RuleRetentionPeriodArgs', 'RuleRetentionPeriodArgsDict']
class RuleExcludeResourceTagArgsDict(TypedDict):
    resource_tag_key: pulumi.Input[_builtins.str]
    resource_tag_value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuleExcludeResourceTagArgs:
    def __init__(__self__, *, resource_tag_key: pulumi.Input[_builtins.str], resource_tag_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagKey")
    def resource_tag_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_tag_key.setter
    def resource_tag_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagValue")
    def resource_tag_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_tag_value.setter
    def resource_tag_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuleLockConfigurationArgsDict(TypedDict):
    unlock_delay: pulumi.Input[RuleLockConfigurationUnlockDelayArgsDict]


@pulumi.input_type
class RuleLockConfigurationArgs:
    def __init__(__self__, *, unlock_delay: pulumi.Input[RuleLockConfigurationUnlockDelayArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unlockDelay")
    def unlock_delay(self) -> pulumi.Input[RuleLockConfigurationUnlockDelayArgs]:
        
        ...
    
    @unlock_delay.setter
    def unlock_delay(self, value: pulumi.Input[RuleLockConfigurationUnlockDelayArgs]): # -> None:
        ...
    


class RuleLockConfigurationUnlockDelayArgsDict(TypedDict):
    unlock_delay_unit: pulumi.Input[_builtins.str]
    unlock_delay_value: pulumi.Input[_builtins.int]


@pulumi.input_type
class RuleLockConfigurationUnlockDelayArgs:
    def __init__(__self__, *, unlock_delay_unit: pulumi.Input[_builtins.str], unlock_delay_value: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unlockDelayUnit")
    def unlock_delay_unit(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @unlock_delay_unit.setter
    def unlock_delay_unit(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unlockDelayValue")
    def unlock_delay_value(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @unlock_delay_value.setter
    def unlock_delay_value(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class RuleResourceTagArgsDict(TypedDict):
    resource_tag_key: pulumi.Input[_builtins.str]
    resource_tag_value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuleResourceTagArgs:
    def __init__(__self__, *, resource_tag_key: pulumi.Input[_builtins.str], resource_tag_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagKey")
    def resource_tag_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_tag_key.setter
    def resource_tag_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagValue")
    def resource_tag_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_tag_value.setter
    def resource_tag_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuleRetentionPeriodArgsDict(TypedDict):
    retention_period_unit: pulumi.Input[_builtins.str]
    retention_period_value: pulumi.Input[_builtins.int]


@pulumi.input_type
class RuleRetentionPeriodArgs:
    def __init__(__self__, *, retention_period_unit: pulumi.Input[_builtins.str], retention_period_value: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodUnit")
    def retention_period_unit(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @retention_period_unit.setter
    def retention_period_unit(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodValue")
    def retention_period_value(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @retention_period_value.setter
    def retention_period_value(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


