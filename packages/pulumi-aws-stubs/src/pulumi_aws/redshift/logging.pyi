

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LoggingArgs', 'Logging']
@pulumi.input_type
class LoggingArgs:
    def __init__(__self__, *, cluster_identifier: pulumi.Input[_builtins.str], bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., log_destination_type: Optional[pulumi.Input[_builtins.str]] = ..., log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_destination_type.setter
    def log_destination_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @log_exports.setter
    def log_exports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _LoggingState:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., log_destination_type: Optional[pulumi.Input[_builtins.str]] = ..., log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_destination_type.setter
    def log_destination_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @log_exports.setter
    def log_exports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:redshift/logging:Logging")
class Logging(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., log_destination_type: Optional[pulumi.Input[_builtins.str]] = ..., log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LoggingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., log_destination_type: Optional[pulumi.Input[_builtins.str]] = ..., log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> Logging:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


