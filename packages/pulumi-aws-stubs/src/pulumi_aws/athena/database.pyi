

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatabaseArgs', 'Database']
@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *, acl_configuration: Optional[pulumi.Input[DatabaseAclConfigurationArgs]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configuration: Optional[pulumi.Input[DatabaseEncryptionConfigurationArgs]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., workgroup: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclConfiguration")
    def acl_configuration(self) -> Optional[pulumi.Input[DatabaseAclConfigurationArgs]]:
        
        ...
    
    @acl_configuration.setter
    def acl_configuration(self, value: Optional[pulumi.Input[DatabaseAclConfigurationArgs]]): # -> None:
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
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[DatabaseEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[DatabaseEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def workgroup(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workgroup.setter
    def workgroup(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DatabaseState:
    def __init__(__self__, *, acl_configuration: Optional[pulumi.Input[DatabaseAclConfigurationArgs]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configuration: Optional[pulumi.Input[DatabaseEncryptionConfigurationArgs]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., workgroup: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclConfiguration")
    def acl_configuration(self) -> Optional[pulumi.Input[DatabaseAclConfigurationArgs]]:
        
        ...
    
    @acl_configuration.setter
    def acl_configuration(self, value: Optional[pulumi.Input[DatabaseAclConfigurationArgs]]): # -> None:
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
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[DatabaseEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[DatabaseEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def workgroup(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workgroup.setter
    def workgroup(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:athena/database:Database")
class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., acl_configuration: Optional[pulumi.Input[Union[DatabaseAclConfigurationArgs, DatabaseAclConfigurationArgsDict]]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configuration: Optional[pulumi.Input[Union[DatabaseEncryptionConfigurationArgs, DatabaseEncryptionConfigurationArgsDict]]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., workgroup: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[DatabaseArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., acl_configuration: Optional[pulumi.Input[Union[DatabaseAclConfigurationArgs, DatabaseAclConfigurationArgsDict]]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configuration: Optional[pulumi.Input[Union[DatabaseEncryptionConfigurationArgs, DatabaseEncryptionConfigurationArgsDict]]] = ..., expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., workgroup: Optional[pulumi.Input[_builtins.str]] = ...) -> Database:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclConfiguration")
    def acl_configuration(self) -> pulumi.Output[Optional[outputs.DatabaseAclConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Output[Optional[outputs.DatabaseEncryptionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def workgroup(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


