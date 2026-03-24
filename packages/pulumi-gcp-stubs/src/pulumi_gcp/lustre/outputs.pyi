

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceAccessRulesOptions', 'InstanceAccessRulesOptionsAccessRule', 'GetInstanceAccessRulesOptionResult', 'GetInstanceAccessRulesOptionAccessRuleResult']
@pulumi.output_type
class InstanceAccessRulesOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_squash_mode: _builtins.str, access_rules: Optional[Sequence[outputs.InstanceAccessRulesOptionsAccessRule]] = ..., default_squash_gid: Optional[_builtins.int] = ..., default_squash_uid: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSquashMode")
    def default_squash_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRules")
    def access_rules(self) -> Optional[Sequence[outputs.InstanceAccessRulesOptionsAccessRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSquashGid")
    def default_squash_gid(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSquashUid")
    def default_squash_uid(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstanceAccessRulesOptionsAccessRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address_ranges: Sequence[_builtins.str], name: _builtins.str, squash_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressRanges")
    def ip_address_ranges(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="squashMode")
    def squash_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceAccessRulesOptionResult(dict):
    def __init__(__self__, *, access_rules: Sequence[outputs.GetInstanceAccessRulesOptionAccessRuleResult], default_squash_gid: _builtins.int, default_squash_mode: _builtins.str, default_squash_uid: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRules")
    def access_rules(self) -> Sequence[outputs.GetInstanceAccessRulesOptionAccessRuleResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSquashGid")
    def default_squash_gid(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSquashMode")
    def default_squash_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSquashUid")
    def default_squash_uid(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetInstanceAccessRulesOptionAccessRuleResult(dict):
    def __init__(__self__, *, ip_address_ranges: Sequence[_builtins.str], name: _builtins.str, squash_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressRanges")
    def ip_address_ranges(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="squashMode")
    def squash_mode(self) -> _builtins.str:
        
        ...
    


