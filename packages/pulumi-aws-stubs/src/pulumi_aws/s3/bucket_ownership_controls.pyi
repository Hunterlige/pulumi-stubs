

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BucketOwnershipControlsArgs', 'BucketOwnershipControls']
@pulumi.input_type
class BucketOwnershipControlsArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], rule: pulumi.Input[BucketOwnershipControlsRuleArgs], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Input[BucketOwnershipControlsRuleArgs]:
        
        ...
    
    @rule.setter
    def rule(self, value: pulumi.Input[BucketOwnershipControlsRuleArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketOwnershipControlsState:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[BucketOwnershipControlsRuleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def rule(self) -> Optional[pulumi.Input[BucketOwnershipControlsRuleArgs]]:
        
        ...
    
    @rule.setter
    def rule(self, value: Optional[pulumi.Input[BucketOwnershipControlsRuleArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class BucketOwnershipControls(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[Union[BucketOwnershipControlsRuleArgs, BucketOwnershipControlsRuleArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BucketOwnershipControlsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[Union[BucketOwnershipControlsRuleArgs, BucketOwnershipControlsRuleArgsDict]]] = ...) -> BucketOwnershipControls:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Output[outputs.BucketOwnershipControlsRule]:
        
        ...
    


