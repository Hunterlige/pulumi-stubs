

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RuleExcludeResourceTag', 'RuleLockConfiguration', 'RuleLockConfigurationUnlockDelay', 'RuleResourceTag', 'RuleRetentionPeriod']
@pulumi.output_type
class RuleExcludeResourceTag(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_tag_key: _builtins.str, resource_tag_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagKey")
    def resource_tag_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagValue")
    def resource_tag_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleLockConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, unlock_delay: outputs.RuleLockConfigurationUnlockDelay) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unlockDelay")
    def unlock_delay(self) -> outputs.RuleLockConfigurationUnlockDelay:
        
        ...
    


@pulumi.output_type
class RuleLockConfigurationUnlockDelay(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, unlock_delay_unit: _builtins.str, unlock_delay_value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unlockDelayUnit")
    def unlock_delay_unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unlockDelayValue")
    def unlock_delay_value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class RuleResourceTag(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_tag_key: _builtins.str, resource_tag_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagKey")
    def resource_tag_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagValue")
    def resource_tag_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleRetentionPeriod(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retention_period_unit: _builtins.str, retention_period_value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodUnit")
    def retention_period_unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodValue")
    def retention_period_value(self) -> _builtins.int:
        
        ...
    


