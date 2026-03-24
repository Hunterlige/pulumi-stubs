

import builtins as _builtins
import sys
import pulumi
from typing import Any, Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VaultNotification']
@pulumi.output_type
class VaultNotification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, events: Sequence[_builtins.str], sns_topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopic")
    def sns_topic(self) -> _builtins.str:
        
        ...
    


