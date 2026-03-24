

import builtins as _builtins
import sys
import pulumi
from typing import Any

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AssessmentTemplateEventSubscription']
@pulumi.output_type
class AssessmentTemplateEventSubscription(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event: _builtins.str, topic_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> _builtins.str:
        
        ...
    


