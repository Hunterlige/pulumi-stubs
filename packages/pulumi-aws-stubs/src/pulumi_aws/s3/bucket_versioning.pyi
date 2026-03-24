

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
__all__ = ['BucketVersioningInitArgs', 'BucketVersioning']
@pulumi.input_type
class BucketVersioningInitArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], versioning_configuration: pulumi.Input[BucketVersioningVersioningConfigurationArgs], expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., mfa: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versioningConfiguration")
    def versioning_configuration(self) -> pulumi.Input[BucketVersioningVersioningConfigurationArgs]:
        
        ...
    
    @versioning_configuration.setter
    def versioning_configuration(self, value: pulumi.Input[BucketVersioningVersioningConfigurationArgs]): # -> None:
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
    def mfa(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mfa.setter
    def mfa(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketVersioningState:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., mfa: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., versioning_configuration: Optional[pulumi.Input[BucketVersioningVersioningConfigurationArgs]] = ...) -> None:
        
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
    def mfa(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mfa.setter
    def mfa(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versioningConfiguration")
    def versioning_configuration(self) -> Optional[pulumi.Input[BucketVersioningVersioningConfigurationArgs]]:
        
        ...
    
    @versioning_configuration.setter
    def versioning_configuration(self, value: Optional[pulumi.Input[BucketVersioningVersioningConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3/bucketVersioning:BucketVersioning")
class BucketVersioning(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., mfa: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., versioning_configuration: Optional[pulumi.Input[Union[BucketVersioningVersioningConfigurationArgs, BucketVersioningVersioningConfigurationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BucketVersioningInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., mfa: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., versioning_configuration: Optional[pulumi.Input[Union[BucketVersioningVersioningConfigurationArgs, BucketVersioningVersioningConfigurationArgsDict]]] = ...) -> BucketVersioning:
        
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
    def mfa(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versioningConfiguration")
    def versioning_configuration(self) -> pulumi.Output[outputs.BucketVersioningVersioningConfiguration]:
        
        ...
    


