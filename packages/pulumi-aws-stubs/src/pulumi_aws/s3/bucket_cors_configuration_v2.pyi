

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
__all__ = ['BucketCorsConfigurationV2Args', 'BucketCorsConfigurationV2']
@pulumi.input_type
class BucketCorsConfigurationV2Args:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], cors_rules: pulumi.Input[Sequence[pulumi.Input[BucketCorsConfigurationV2CorsRuleArgs]]], expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsRules")
    def cors_rules(self) -> pulumi.Input[Sequence[pulumi.Input[BucketCorsConfigurationV2CorsRuleArgs]]]:
        
        ...
    
    @cors_rules.setter
    def cors_rules(self, value: pulumi.Input[Sequence[pulumi.Input[BucketCorsConfigurationV2CorsRuleArgs]]]): # -> None:
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
class _BucketCorsConfigurationV2State:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorsConfigurationV2CorsRuleArgs]]]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsRules")
    def cors_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorsConfigurationV2CorsRuleArgs]]]]:
        
        ...
    
    @cors_rules.setter
    def cors_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorsConfigurationV2CorsRuleArgs]]]]): # -> None:
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
    


@pulumi.type_token(...)
class BucketCorsConfigurationV2(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketCorsConfigurationV2CorsRuleArgs, BucketCorsConfigurationV2CorsRuleArgsDict]]]]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BucketCorsConfigurationV2Args, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketCorsConfigurationV2CorsRuleArgs, BucketCorsConfigurationV2CorsRuleArgsDict]]]]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> BucketCorsConfigurationV2:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsRules")
    def cors_rules(self) -> pulumi.Output[Sequence[outputs.BucketCorsConfigurationV2CorsRule]]:
        
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
    


