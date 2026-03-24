

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RepositoryCatalogData', 'GetImagesImageResult', 'GetImagesImageIdResult']
@pulumi.output_type
class RepositoryCatalogData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, about_text: Optional[_builtins.str] = ..., architectures: Optional[Sequence[_builtins.str]] = ..., description: Optional[_builtins.str] = ..., logo_image_blob: Optional[_builtins.str] = ..., operating_systems: Optional[Sequence[_builtins.str]] = ..., usage_text: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aboutText")
    def about_text(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def architectures(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logoImageBlob")
    def logo_image_blob(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystems")
    def operating_systems(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageText")
    def usage_text(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetImagesImageResult(dict):
    def __init__(__self__, *, artifact_media_type: _builtins.str, image_digest: _builtins.str, image_manifest_media_type: _builtins.str, image_pushed_at: _builtins.str, image_size_in_bytes: _builtins.int, image_tags: Sequence[_builtins.str], registry_id: _builtins.str, repository_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactMediaType")
    def artifact_media_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageDigest")
    def image_digest(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageManifestMediaType")
    def image_manifest_media_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imagePushedAt")
    def image_pushed_at(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageSizeInBytes")
    def image_size_in_bytes(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageTags")
    def image_tags(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetImagesImageIdResult(dict):
    def __init__(__self__, *, image_digest: Optional[_builtins.str] = ..., image_tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageDigest")
    def image_digest(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> Optional[_builtins.str]:
        
        ...
    


