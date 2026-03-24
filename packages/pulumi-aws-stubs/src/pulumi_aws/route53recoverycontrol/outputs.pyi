

import builtins as _builtins
import sys
import pulumi
from typing import Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterClusterEndpoint', 'SafetyRuleRuleConfig']
@pulumi.output_type
class ClusterClusterEndpoint(dict):
    def __init__(__self__, *, endpoint: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SafetyRuleRuleConfig(dict):
    def __init__(__self__, *, inverted: _builtins.bool, threshold: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def inverted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


