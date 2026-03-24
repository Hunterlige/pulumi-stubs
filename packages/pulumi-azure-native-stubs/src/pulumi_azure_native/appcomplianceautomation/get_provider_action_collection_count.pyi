

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProviderActionCollectionCountResult', 'AwaitableGetProviderActionCollectionCountResult', 'get_provider_action_collection_count', 'get_provider_action_collection_count_output']
@pulumi.output_type
class GetProviderActionCollectionCountResult:
    
    def __init__(__self__, count=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    


class AwaitableGetProviderActionCollectionCountResult(GetProviderActionCollectionCountResult):
    def __await__(self): # -> Generator[Never, Any, GetProviderActionCollectionCountResult]:
        ...
    


def get_provider_action_collection_count(type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProviderActionCollectionCountResult:
    
    ...

def get_provider_action_collection_count_output(type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProviderActionCollectionCountResult]:
    
    ...

