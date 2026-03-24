

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BucketLoggingV2Args', 'BucketLoggingV2']
@pulumi.input_type
class BucketLoggingV2Args:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], target_bucket: pulumi.Input[_builtins.str], target_prefix: pulumi.Input[_builtins.str], expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_grants: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLoggingV2TargetGrantArgs]]]] = ..., target_object_key_format: Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetBucket")
    def target_bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_bucket.setter
    def target_bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPrefix")
    def target_prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_prefix.setter
    def target_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="targetGrants")
    def target_grants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLoggingV2TargetGrantArgs]]]]:
        
        ...
    
    @target_grants.setter
    def target_grants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLoggingV2TargetGrantArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetObjectKeyFormat")
    def target_object_key_format(self) -> Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatArgs]]:
        
        ...
    
    @target_object_key_format.setter
    def target_object_key_format(self, value: Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketLoggingV2State:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_bucket: Optional[pulumi.Input[_builtins.str]] = ..., target_grants: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLoggingV2TargetGrantArgs]]]] = ..., target_object_key_format: Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatArgs]] = ..., target_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    
    @_builtins.property
    @pulumi.getter(name="targetBucket")
    def target_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_bucket.setter
    def target_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGrants")
    def target_grants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLoggingV2TargetGrantArgs]]]]:
        
        ...
    
    @target_grants.setter
    def target_grants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLoggingV2TargetGrantArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetObjectKeyFormat")
    def target_object_key_format(self) -> Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatArgs]]:
        
        ...
    
    @target_object_key_format.setter
    def target_object_key_format(self, value: Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPrefix")
    def target_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_prefix.setter
    def target_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3/bucketLoggingV2:BucketLoggingV2")
class BucketLoggingV2(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_bucket: Optional[pulumi.Input[_builtins.str]] = ..., target_grants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketLoggingV2TargetGrantArgs, BucketLoggingV2TargetGrantArgsDict]]]]] = ..., target_object_key_format: Optional[pulumi.Input[Union[BucketLoggingV2TargetObjectKeyFormatArgs, BucketLoggingV2TargetObjectKeyFormatArgsDict]]] = ..., target_prefix: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BucketLoggingV2Args, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_bucket: Optional[pulumi.Input[_builtins.str]] = ..., target_grants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketLoggingV2TargetGrantArgs, BucketLoggingV2TargetGrantArgsDict]]]]] = ..., target_object_key_format: Optional[pulumi.Input[Union[BucketLoggingV2TargetObjectKeyFormatArgs, BucketLoggingV2TargetObjectKeyFormatArgsDict]]] = ..., target_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> BucketLoggingV2:
        
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
    
    @_builtins.property
    @pulumi.getter(name="targetBucket")
    def target_bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGrants")
    def target_grants(self) -> pulumi.Output[Optional[Sequence[outputs.BucketLoggingV2TargetGrant]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetObjectKeyFormat")
    def target_object_key_format(self) -> pulumi.Output[Optional[outputs.BucketLoggingV2TargetObjectKeyFormat]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPrefix")
    def target_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


