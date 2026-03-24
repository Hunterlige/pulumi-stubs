

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListFeatureAccountResult', 'AwaitableListFeatureAccountResult', 'list_feature_account', 'list_feature_account_output']
@pulumi.output_type
class ListFeatureAccountResult:
    
    def __init__(__self__, features=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def features(self) -> Mapping[str, _builtins.bool]:
        
        ...
    


class AwaitableListFeatureAccountResult(ListFeatureAccountResult):
    def __await__(self): # -> Generator[Never, Any, ListFeatureAccountResult]:
        ...
    


def list_feature_account(account_name: Optional[_builtins.str] = ..., features: Optional[Sequence[_builtins.str]] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListFeatureAccountResult:
    
    ...

def list_feature_account_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., features: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListFeatureAccountResult]:
    
    ...

