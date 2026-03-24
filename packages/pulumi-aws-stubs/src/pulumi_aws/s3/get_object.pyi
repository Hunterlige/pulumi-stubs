

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetObjectResult', 'AwaitableGetObjectResult', 'get_object', 'get_object_output']
@pulumi.output_type
class GetObjectResult:
    
    def __init__(__self__, arn=..., body=..., body_base64=..., bucket=..., bucket_key_enabled=..., cache_control=..., checksum_crc32=..., checksum_crc32c=..., checksum_crc64nvme=..., checksum_mode=..., checksum_sha1=..., checksum_sha256=..., content_disposition=..., content_encoding=..., content_language=..., content_length=..., content_type=..., download_body=..., etag=..., expiration=..., expires=..., id=..., key=..., last_modified=..., metadata=..., object_lock_legal_hold_status=..., object_lock_mode=..., object_lock_retain_until_date=..., range=..., region=..., server_side_encryption=..., sse_kms_key_id=..., storage_class=..., tags=..., version_id=..., website_redirect_location=...) -> None:
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
    @pulumi.getter(name="bodyBase64")
    def body_base64(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
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
    @pulumi.getter(name="checksumCrc32")
    def checksum_crc32(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumCrc32c")
    def checksum_crc32c(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumCrc64nvme")
    def checksum_crc64nvme(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumMode")
    def checksum_mode(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumSha1")
    def checksum_sha1(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumSha256")
    def checksum_sha256(self) -> _builtins.str:
        
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
    @pulumi.getter(name="downloadBody")
    def download_body(self) -> Optional[_builtins.str]:
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
    


class AwaitableGetObjectResult(GetObjectResult):
    def __await__(self): # -> Generator[Never, Any, GetObjectResult]:
        ...
    


def get_object(bucket: Optional[_builtins.str] = ..., checksum_mode: Optional[_builtins.str] = ..., download_body: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., range: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., version_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetObjectResult:
    
    ...

def get_object_output(bucket: Optional[pulumi.Input[_builtins.str]] = ..., checksum_mode: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., download_body: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., range: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., version_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetObjectResult]:
    
    ...

