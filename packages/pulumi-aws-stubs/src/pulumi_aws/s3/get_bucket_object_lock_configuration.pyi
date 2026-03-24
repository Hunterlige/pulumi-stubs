

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBucketObjectLockConfigurationResult', 'AwaitableGetBucketObjectLockConfigurationResult', 'get_bucket_object_lock_configuration', 'get_bucket_object_lock_configuration_output']
@pulumi.output_type
class GetBucketObjectLockConfigurationResult:
    
    def __init__(__self__, bucket=..., expected_bucket_owner=..., id=..., object_lock_enabled=..., region=..., rules=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockEnabled")
    def object_lock_enabled(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetBucketObjectLockConfigurationRuleResult]:
        
        ...
    


class AwaitableGetBucketObjectLockConfigurationResult(GetBucketObjectLockConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetBucketObjectLockConfigurationResult]:
        ...
    


def get_bucket_object_lock_configuration(bucket: Optional[_builtins.str] = ..., expected_bucket_owner: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBucketObjectLockConfigurationResult:
    
    ...

def get_bucket_object_lock_configuration_output(bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBucketObjectLockConfigurationResult]:
    
    ...

