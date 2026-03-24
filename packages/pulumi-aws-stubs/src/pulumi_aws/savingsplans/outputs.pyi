

import builtins as _builtins
import sys
import pulumi
from typing import Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SavingsPlanTimeouts']
@pulumi.output_type
class SavingsPlanTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


