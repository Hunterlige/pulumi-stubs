

import builtins as _builtins
import sys
import pulumi

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StatementParameter']
@pulumi.output_type
class StatementParameter(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


