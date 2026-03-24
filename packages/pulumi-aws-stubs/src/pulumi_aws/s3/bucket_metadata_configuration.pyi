

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
__all__ = ['BucketMetadataConfigurationArgs', 'BucketMetadataConfiguration']
@pulumi.input_type
class BucketMetadataConfigurationArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], metadata_configuration: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationArgs], expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[BucketMetadataConfigurationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(self) -> pulumi.Input[BucketMetadataConfigurationMetadataConfigurationArgs]:
        
        ...
    
    @metadata_configuration.setter
    def metadata_configuration(self, value: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationArgs]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[BucketMetadataConfigurationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[BucketMetadataConfigurationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketMetadataConfigurationState:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., metadata_configuration: Optional[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[BucketMetadataConfigurationTimeoutsArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(self) -> Optional[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationArgs]]:
        
        ...
    
    @metadata_configuration.setter
    def metadata_configuration(self, value: Optional[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationArgs]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[BucketMetadataConfigurationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[BucketMetadataConfigurationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class BucketMetadataConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., metadata_configuration: Optional[pulumi.Input[Union[BucketMetadataConfigurationMetadataConfigurationArgs, BucketMetadataConfigurationMetadataConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[BucketMetadataConfigurationTimeoutsArgs, BucketMetadataConfigurationTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BucketMetadataConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., metadata_configuration: Optional[pulumi.Input[Union[BucketMetadataConfigurationMetadataConfigurationArgs, BucketMetadataConfigurationMetadataConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[BucketMetadataConfigurationTimeoutsArgs, BucketMetadataConfigurationTimeoutsArgsDict]]] = ...) -> BucketMetadataConfiguration:
        
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
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(self) -> pulumi.Output[outputs.BucketMetadataConfigurationMetadataConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.BucketMetadataConfigurationTimeouts]]:
        ...
    


