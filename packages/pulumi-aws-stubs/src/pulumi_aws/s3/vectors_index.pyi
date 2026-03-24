

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
__all__ = ['VectorsIndexArgs', 'VectorsIndex']
@pulumi.input_type
class VectorsIndexArgs:
    def __init__(__self__, *, data_type: pulumi.Input[_builtins.str], dimension: pulumi.Input[_builtins.int], distance_metric: pulumi.Input[_builtins.str], index_name: pulumi.Input[_builtins.str], vector_bucket_name: pulumi.Input[_builtins.str], encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[VectorsIndexEncryptionConfigurationArgs]]]] = ..., metadata_configuration: Optional[pulumi.Input[VectorsIndexMetadataConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_type.setter
    def data_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="distanceMetric")
    def distance_metric(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @distance_metric.setter
    def distance_metric(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @index_name.setter
    def index_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VectorsIndexEncryptionConfigurationArgs]]]]:
        
        ...
    
    @encryption_configurations.setter
    def encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VectorsIndexEncryptionConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(self) -> Optional[pulumi.Input[VectorsIndexMetadataConfigurationArgs]]:
        
        ...
    
    @metadata_configuration.setter
    def metadata_configuration(self, value: Optional[pulumi.Input[VectorsIndexMetadataConfigurationArgs]]): # -> None:
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
class _VectorsIndexState:
    def __init__(__self__, *, creation_time: Optional[pulumi.Input[_builtins.str]] = ..., data_type: Optional[pulumi.Input[_builtins.str]] = ..., dimension: Optional[pulumi.Input[_builtins.int]] = ..., distance_metric: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[VectorsIndexEncryptionConfigurationArgs]]]] = ..., index_arn: Optional[pulumi.Input[_builtins.str]] = ..., index_name: Optional[pulumi.Input[_builtins.str]] = ..., metadata_configuration: Optional[pulumi.Input[VectorsIndexMetadataConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vector_bucket_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="distanceMetric")
    def distance_metric(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @distance_metric.setter
    def distance_metric(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VectorsIndexEncryptionConfigurationArgs]]]]:
        
        ...
    
    @encryption_configurations.setter
    def encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VectorsIndexEncryptionConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexArn")
    def index_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index_arn.setter
    def index_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index_name.setter
    def index_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(self) -> Optional[pulumi.Input[VectorsIndexMetadataConfigurationArgs]]:
        
        ...
    
    @metadata_configuration.setter
    def metadata_configuration(self, value: Optional[pulumi.Input[VectorsIndexMetadataConfigurationArgs]]): # -> None:
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
    @pulumi.getter(name="vectorBucketName")
    def vector_bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vector_bucket_name.setter
    def vector_bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3/vectorsIndex:VectorsIndex")
class VectorsIndex(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_type: Optional[pulumi.Input[_builtins.str]] = ..., dimension: Optional[pulumi.Input[_builtins.int]] = ..., distance_metric: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VectorsIndexEncryptionConfigurationArgs, VectorsIndexEncryptionConfigurationArgsDict]]]]] = ..., index_name: Optional[pulumi.Input[_builtins.str]] = ..., metadata_configuration: Optional[pulumi.Input[Union[VectorsIndexMetadataConfigurationArgs, VectorsIndexMetadataConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vector_bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VectorsIndexArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., data_type: Optional[pulumi.Input[_builtins.str]] = ..., dimension: Optional[pulumi.Input[_builtins.int]] = ..., distance_metric: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VectorsIndexEncryptionConfigurationArgs, VectorsIndexEncryptionConfigurationArgsDict]]]]] = ..., index_arn: Optional[pulumi.Input[_builtins.str]] = ..., index_name: Optional[pulumi.Input[_builtins.str]] = ..., metadata_configuration: Optional[pulumi.Input[Union[VectorsIndexMetadataConfigurationArgs, VectorsIndexMetadataConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vector_bucket_name: Optional[pulumi.Input[_builtins.str]] = ...) -> VectorsIndex:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distanceMetric")
    def distance_metric(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> pulumi.Output[Sequence[outputs.VectorsIndexEncryptionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexArn")
    def index_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(self) -> pulumi.Output[Optional[outputs.VectorsIndexMetadataConfiguration]]:
        
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
    @pulumi.getter(name="vectorBucketName")
    def vector_bucket_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


