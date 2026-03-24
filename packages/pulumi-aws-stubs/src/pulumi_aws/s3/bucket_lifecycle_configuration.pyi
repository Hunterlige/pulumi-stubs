

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
__all__ = ['BucketLifecycleConfigurationArgs', 'BucketLifecycleConfiguration']
@pulumi.input_type
class BucketLifecycleConfigurationArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleArgs]]]] = ..., timeouts: Optional[pulumi.Input[BucketLifecycleConfigurationTimeoutsArgs]] = ..., transition_default_minimum_object_size: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitionDefaultMinimumObjectSize")
    def transition_default_minimum_object_size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transition_default_minimum_object_size.setter
    def transition_default_minimum_object_size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketLifecycleConfigurationState:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleArgs]]]] = ..., timeouts: Optional[pulumi.Input[BucketLifecycleConfigurationTimeoutsArgs]] = ..., transition_default_minimum_object_size: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitionDefaultMinimumObjectSize")
    def transition_default_minimum_object_size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transition_default_minimum_object_size.setter
    def transition_default_minimum_object_size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class BucketLifecycleConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketLifecycleConfigurationRuleArgs, BucketLifecycleConfigurationRuleArgsDict]]]]] = ..., timeouts: Optional[pulumi.Input[Union[BucketLifecycleConfigurationTimeoutsArgs, BucketLifecycleConfigurationTimeoutsArgsDict]]] = ..., transition_default_minimum_object_size: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BucketLifecycleConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketLifecycleConfigurationRuleArgs, BucketLifecycleConfigurationRuleArgsDict]]]]] = ..., timeouts: Optional[pulumi.Input[Union[BucketLifecycleConfigurationTimeoutsArgs, BucketLifecycleConfigurationTimeoutsArgsDict]]] = ..., transition_default_minimum_object_size: Optional[pulumi.Input[_builtins.str]] = ...) -> BucketLifecycleConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[outputs.BucketLifecycleConfigurationRule]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.BucketLifecycleConfigurationTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitionDefaultMinimumObjectSize")
    def transition_default_minimum_object_size(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


