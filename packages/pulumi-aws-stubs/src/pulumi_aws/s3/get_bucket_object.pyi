

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from .. import _utilities

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBucketObjectResult', 'AwaitableGetBucketObjectResult', 'get_bucket_object', 'get_bucket_object_output']
@pulumi.output_type
class GetBucketObjectResult:
    
    def __init__(__self__, arn=..., body=..., bucket=..., bucket_key_enabled=..., cache_control=..., content_disposition=..., content_encoding=..., content_language=..., content_length=..., content_type=..., etag=..., expiration=..., expires=..., id=..., key=..., last_modified=..., metadata=..., object_lock_legal_hold_status=..., object_lock_mode=..., object_lock_retain_until_date=..., range=..., region=..., server_side_encryption=..., sse_kms_key_id=..., storage_class=..., tags=..., version_id=..., website_redirect_location=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def bucket(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> _builtins.str:
        
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
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLength")
    def content_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expires(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockLegalHoldStatus")
    def object_lock_legal_hold_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockMode")
    def object_lock_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockRetainUntilDate")
    def object_lock_retain_until_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def range(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseKmsKeyId")
    def sse_kms_key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteRedirectLocation")
    def website_redirect_location(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBucketObjectResult(GetBucketObjectResult):
    def __await__(self): # -> Generator[Never, Any, GetBucketObjectResult]:
        ...
    


def get_bucket_object(bucket: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., range: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., version_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBucketObjectResult:
    
    ...

def get_bucket_object_output(bucket: Optional[pulumi.Input[_builtins.str]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., range: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., version_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBucketObjectResult]:
    
    ...

