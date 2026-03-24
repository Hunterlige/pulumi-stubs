

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VectorsVectorBucketArgs', 'VectorsVectorBucket']
@pulumi.input_type
class VectorsVectorBucketArgs:
    def __init__(__self__, *, vector_bucket_name: pulumi.Input[_builtins.str], encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[VectorsVectorBucketEncryptionConfigurationArgs]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorBucketName")
    def vector_bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vector_bucket_name.setter
    def vector_bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VectorsVectorBucketEncryptionConfigurationArgs]]]]:
        
        ...
    
    @encryption_configurations.setter
    def encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VectorsVectorBucketEncryptionConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _VectorsVectorBucketState:
    def __init__(__self__, *, creation_time: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[VectorsVectorBucketEncryptionConfigurationArgs]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vector_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ..., vector_bucket_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VectorsVectorBucketEncryptionConfigurationArgs]]]]:
        
        ...
    
    @encryption_configurations.setter
    def encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VectorsVectorBucketEncryptionConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorBucketArn")
    def vector_bucket_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vector_bucket_arn.setter
    def vector_bucket_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorBucketName")
    def vector_bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vector_bucket_name.setter
    def vector_bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3/vectorsVectorBucket:VectorsVectorBucket")
class VectorsVectorBucket(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VectorsVectorBucketEncryptionConfigurationArgs, VectorsVectorBucketEncryptionConfigurationArgsDict]]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vector_bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VectorsVectorBucketArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VectorsVectorBucketEncryptionConfigurationArgs, VectorsVectorBucketEncryptionConfigurationArgsDict]]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vector_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ..., vector_bucket_name: Optional[pulumi.Input[_builtins.str]] = ...) -> VectorsVectorBucket:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> pulumi.Output[Sequence[outputs.VectorsVectorBucketEncryptionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorBucketArn")
    def vector_bucket_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorBucketName")
    def vector_bucket_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


