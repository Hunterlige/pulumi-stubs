

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIntentResult', 'AwaitableGetIntentResult', 'get_intent', 'get_intent_output']
@pulumi.output_type
class GetIntentResult:
    
    def __init__(__self__, arn=..., checksum=..., created_date=..., description=..., id=..., last_updated_date=..., name=..., parent_intent_signature=..., region=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentIntentSignature")
    def parent_intent_signature(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetIntentResult(GetIntentResult):
    def __await__(self): # -> Generator[Never, Any, GetIntentResult]:
        ...
    


def get_intent(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIntentResult:
    
    ...

def get_intent_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., version: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIntentResult]:
    
    ...

