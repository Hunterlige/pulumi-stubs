

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BucketAclV2Args', 'BucketAclV2']
@pulumi.input_type
class BucketAclV2Args:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], access_control_policy: Optional[pulumi.Input[BucketAclV2AccessControlPolicyArgs]] = ..., acl: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlPolicy")
    def access_control_policy(self) -> Optional[pulumi.Input[BucketAclV2AccessControlPolicyArgs]]:
        
        ...
    
    @access_control_policy.setter
    def access_control_policy(self, value: Optional[pulumi.Input[BucketAclV2AccessControlPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketAclV2State:
    def __init__(__self__, *, access_control_policy: Optional[pulumi.Input[BucketAclV2AccessControlPolicyArgs]] = ..., acl: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlPolicy")
    def access_control_policy(self) -> Optional[pulumi.Input[BucketAclV2AccessControlPolicyArgs]]:
        
        ...
    
    @access_control_policy.setter
    def access_control_policy(self, value: Optional[pulumi.Input[BucketAclV2AccessControlPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3/bucketAclV2:BucketAclV2")
class BucketAclV2(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_control_policy: Optional[pulumi.Input[Union[BucketAclV2AccessControlPolicyArgs, BucketAclV2AccessControlPolicyArgsDict]]] = ..., acl: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BucketAclV2Args, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_control_policy: Optional[pulumi.Input[Union[BucketAclV2AccessControlPolicyArgs, BucketAclV2AccessControlPolicyArgsDict]]] = ..., acl: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> BucketAclV2:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlPolicy")
    def access_control_policy(self) -> pulumi.Output[outputs.BucketAclV2AccessControlPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def acl(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


