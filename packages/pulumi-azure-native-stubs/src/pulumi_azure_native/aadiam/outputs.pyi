

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LogSettingsResponse', 'RetentionPolicyResponse']
@pulumi.output_type
class LogSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, category: Optional[_builtins.str] = ..., retention_policy: Optional[outputs.RetentionPolicyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[outputs.RetentionPolicyResponse]:
        
        ...
    


@pulumi.output_type
class RetentionPolicyResponse(dict):
    
    def __init__(__self__, *, days: _builtins.int, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


