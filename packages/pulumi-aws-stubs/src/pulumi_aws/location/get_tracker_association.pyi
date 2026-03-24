

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTrackerAssociationResult', 'AwaitableGetTrackerAssociationResult', 'get_tracker_association', 'get_tracker_association_output']
@pulumi.output_type
class GetTrackerAssociationResult:
    
    def __init__(__self__, consumer_arn=..., id=..., region=..., tracker_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackerName")
    def tracker_name(self) -> _builtins.str:
        ...
    


class AwaitableGetTrackerAssociationResult(GetTrackerAssociationResult):
    def __await__(self): # -> Generator[Never, Any, GetTrackerAssociationResult]:
        ...
    


def get_tracker_association(consumer_arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tracker_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTrackerAssociationResult:
    
    ...

def get_tracker_association_output(consumer_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tracker_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTrackerAssociationResult]:
    
    ...

