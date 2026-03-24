

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBucketObjectContentResult', 'AwaitableGetBucketObjectContentResult', 'get_bucket_object_content', 'get_bucket_object_content_output']
@pulumi.output_type
class GetBucketObjectContentResult:
    
    def __init__(__self__, bucket=..., cache_control=..., content=..., content_base64=..., content_base64sha512=..., content_disposition=..., content_encoding=..., content_hexsha512=..., content_language=..., content_type=..., contexts=..., crc32c=..., customer_encryptions=..., deletion_policy=..., detect_md5hash=..., event_based_hold=..., force_empty_content_type=..., generation=..., id=..., kms_key_name=..., md5hash=..., md5hexhash=..., media_link=..., metadata=..., name=..., output_name=..., retentions=..., self_link=..., source=..., source_md5hash=..., storage_class=..., temporary_hold=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBase64sha512")
    def content_base64sha512(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentHexsha512")
    def content_hexsha512(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def contexts(self) -> Sequence[outputs.GetBucketObjectContentContextResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def crc32c(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerEncryptions")
    def customer_encryptions(self) -> Sequence[outputs.GetBucketObjectContentCustomerEncryptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectMd5hash")
    def detect_md5hash(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBasedHold")
    def event_based_hold(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceEmptyContentType")
    def force_empty_content_type(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def md5hash(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def md5hexhash(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaLink")
    def media_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputName")
    def output_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def retentions(self) -> Sequence[outputs.GetBucketObjectContentRetentionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceMd5hash")
    def source_md5hash(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryHold")
    def temporary_hold(self) -> _builtins.bool:
        ...
    


class AwaitableGetBucketObjectContentResult(GetBucketObjectContentResult):
    def __await__(self): # -> Generator[Never, Any, GetBucketObjectContentResult]:
        ...
    


def get_bucket_object_content(bucket: Optional[_builtins.str] = ..., content: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBucketObjectContentResult:
    
    ...

def get_bucket_object_content_output(bucket: Optional[pulumi.Input[_builtins.str]] = ..., content: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBucketObjectContentResult]:
    
    ...

