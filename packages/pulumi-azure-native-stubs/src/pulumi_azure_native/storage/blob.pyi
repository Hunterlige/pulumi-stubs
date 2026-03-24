

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BlobArgs', 'Blob']
@pulumi.input_type
class BlobArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], container_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], access_tier: Optional[pulumi.Input[BlobAccessTier]] = ..., blob_name: Optional[pulumi.Input[_builtins.str]] = ..., content_md5: Optional[pulumi.Input[_builtins.str]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = ..., type: Optional[pulumi.Input[BlobType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_name.setter
    def container_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> Optional[pulumi.Input[BlobAccessTier]]:
        
        ...
    
    @access_tier.setter
    def access_tier(self, value: Optional[pulumi.Input[BlobAccessTier]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobName")
    def blob_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blob_name.setter
    def blob_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentMd5")
    def content_md5(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_md5.setter
    def content_md5(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[BlobType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[BlobType]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:storage:Blob")
class Blob(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_tier: Optional[pulumi.Input[BlobAccessTier]] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., blob_name: Optional[pulumi.Input[_builtins.str]] = ..., container_name: Optional[pulumi.Input[_builtins.str]] = ..., content_md5: Optional[pulumi.Input[_builtins.str]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = ..., type: Optional[pulumi.Input[BlobType]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BlobArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Blob:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> pulumi.Output[Optional[BlobAccessTier]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentMd5")
    def content_md5(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[BlobType]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


