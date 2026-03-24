

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GroupInsightsConfiguration']
@pulumi.output_type
class GroupInsightsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insights_enabled: _builtins.bool, notifications_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsEnabled")
    def insights_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationsEnabled")
    def notifications_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


