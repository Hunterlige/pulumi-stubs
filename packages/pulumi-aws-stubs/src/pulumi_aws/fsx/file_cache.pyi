

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
__all__ = ['FileCacheArgs', 'FileCache']
@pulumi.input_type
class FileCacheArgs:
    def __init__(__self__, *, file_cache_type: pulumi.Input[_builtins.str], file_cache_type_version: pulumi.Input[_builtins.str], storage_capacity: pulumi.Input[_builtins.int], subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], copy_tags_to_data_repository_associations: Optional[pulumi.Input[_builtins.bool]] = ..., data_repository_associations: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheDataRepositoryAssociationArgs]]]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., lustre_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCacheType")
    def file_cache_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_cache_type.setter
    def file_cache_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCacheTypeVersion")
    def file_cache_type_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_cache_type_version.setter
    def file_cache_type_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @storage_capacity.setter
    def storage_capacity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTagsToDataRepositoryAssociations")
    def copy_tags_to_data_repository_associations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @copy_tags_to_data_repository_associations.setter
    def copy_tags_to_data_repository_associations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRepositoryAssociations")
    def data_repository_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheDataRepositoryAssociationArgs]]]]:
        
        ...
    
    @data_repository_associations.setter
    def data_repository_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheDataRepositoryAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lustreConfigurations")
    def lustre_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationArgs]]]]:
        
        ...
    
    @lustre_configurations.setter
    def lustre_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _FileCacheState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., copy_tags_to_data_repository_associations: Optional[pulumi.Input[_builtins.bool]] = ..., data_repository_association_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., data_repository_associations: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheDataRepositoryAssociationArgs]]]] = ..., dns_name: Optional[pulumi.Input[_builtins.str]] = ..., file_cache_id: Optional[pulumi.Input[_builtins.str]] = ..., file_cache_type: Optional[pulumi.Input[_builtins.str]] = ..., file_cache_type_version: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., lustre_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationArgs]]]] = ..., network_interface_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., storage_capacity: Optional[pulumi.Input[_builtins.int]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTagsToDataRepositoryAssociations")
    def copy_tags_to_data_repository_associations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @copy_tags_to_data_repository_associations.setter
    def copy_tags_to_data_repository_associations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRepositoryAssociationIds")
    def data_repository_association_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @data_repository_association_ids.setter
    def data_repository_association_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRepositoryAssociations")
    def data_repository_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheDataRepositoryAssociationArgs]]]]:
        
        ...
    
    @data_repository_associations.setter
    def data_repository_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheDataRepositoryAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCacheId")
    def file_cache_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_cache_id.setter
    def file_cache_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCacheType")
    def file_cache_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_cache_type.setter
    def file_cache_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCacheTypeVersion")
    def file_cache_type_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_cache_type_version.setter
    def file_cache_type_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lustreConfigurations")
    def lustre_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationArgs]]]]:
        
        ...
    
    @lustre_configurations.setter
    def lustre_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @network_interface_ids.setter
    def network_interface_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_capacity.setter
    def storage_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:fsx/fileCache:FileCache")
class FileCache(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., copy_tags_to_data_repository_associations: Optional[pulumi.Input[_builtins.bool]] = ..., data_repository_associations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FileCacheDataRepositoryAssociationArgs, FileCacheDataRepositoryAssociationArgsDict]]]]] = ..., file_cache_type: Optional[pulumi.Input[_builtins.str]] = ..., file_cache_type_version: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., lustre_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FileCacheLustreConfigurationArgs, FileCacheLustreConfigurationArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., storage_capacity: Optional[pulumi.Input[_builtins.int]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FileCacheArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., copy_tags_to_data_repository_associations: Optional[pulumi.Input[_builtins.bool]] = ..., data_repository_association_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., data_repository_associations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FileCacheDataRepositoryAssociationArgs, FileCacheDataRepositoryAssociationArgsDict]]]]] = ..., dns_name: Optional[pulumi.Input[_builtins.str]] = ..., file_cache_id: Optional[pulumi.Input[_builtins.str]] = ..., file_cache_type: Optional[pulumi.Input[_builtins.str]] = ..., file_cache_type_version: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., lustre_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FileCacheLustreConfigurationArgs, FileCacheLustreConfigurationArgsDict]]]]] = ..., network_interface_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., storage_capacity: Optional[pulumi.Input[_builtins.int]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> FileCache:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTagsToDataRepositoryAssociations")
    def copy_tags_to_data_repository_associations(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRepositoryAssociationIds")
    def data_repository_association_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRepositoryAssociations")
    def data_repository_associations(self) -> pulumi.Output[Optional[Sequence[outputs.FileCacheDataRepositoryAssociation]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCacheId")
    def file_cache_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCacheType")
    def file_cache_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCacheTypeVersion")
    def file_cache_type_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lustreConfigurations")
    def lustre_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.FileCacheLustreConfiguration]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


