

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BucketPublicAccessBlockArgs', 'BucketPublicAccessBlock']
@pulumi.input_type
class BucketPublicAccessBlockArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], block_public_acls: Optional[pulumi.Input[_builtins.bool]] = ..., block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_public_acls: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., restrict_public_buckets: Optional[pulumi.Input[_builtins.bool]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @block_public_acls.setter
    def block_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @block_public_policy.setter
    def block_public_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_public_acls.setter
    def ignore_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @restrict_public_buckets.setter
    def restrict_public_buckets(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketPublicAccessBlockState:
    def __init__(__self__, *, block_public_acls: Optional[pulumi.Input[_builtins.bool]] = ..., block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., ignore_public_acls: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., restrict_public_buckets: Optional[pulumi.Input[_builtins.bool]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @block_public_acls.setter
    def block_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @block_public_policy.setter
    def block_public_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_public_acls.setter
    def ignore_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @restrict_public_buckets.setter
    def restrict_public_buckets(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class BucketPublicAccessBlock(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., block_public_acls: Optional[pulumi.Input[_builtins.bool]] = ..., block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., ignore_public_acls: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., restrict_public_buckets: Optional[pulumi.Input[_builtins.bool]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BucketPublicAccessBlockArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., block_public_acls: Optional[pulumi.Input[_builtins.bool]] = ..., block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., ignore_public_acls: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., restrict_public_buckets: Optional[pulumi.Input[_builtins.bool]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...) -> BucketPublicAccessBlock:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


