

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetImageResult', 'AwaitableGetImageResult', 'get_image', 'get_image_output']
@pulumi.output_type
class GetImageResult:
    
    def __init__(__self__, archive_size_bytes=..., creation_timestamp=..., description=..., disk_size_gb=..., family=..., filter=..., id=..., image_encryption_key_sha256=..., image_id=..., label_fingerprint=..., labels=..., licenses=..., most_recent=..., name=..., project=..., self_link=..., source_disk=..., source_disk_encryption_key_sha256=..., source_disk_id=..., source_image_id=..., status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveSizeBytes")
    def archive_size_bytes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageEncryptionKeySha256")
    def image_encryption_key_sha256(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskEncryptionKeySha256")
    def source_disk_encryption_key_sha256(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


class AwaitableGetImageResult(GetImageResult):
    def __await__(self): # -> Generator[Never, Any, GetImageResult]:
        ...
    


def get_image(family: Optional[_builtins.str] = ..., filter: Optional[_builtins.str] = ..., most_recent: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetImageResult:
    
    ...

def get_image_output(family: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetImageResult]:
    
    ...

