

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetContentPackageResult', 'AwaitableGetContentPackageResult', 'get_content_package', 'get_content_package_output']
@pulumi.output_type
class GetContentPackageResult:
    
    def __init__(__self__, author=..., azure_api_version=..., categories=..., content_id=..., content_kind=..., content_product_id=..., content_schema_version=..., dependencies=..., description=..., display_name=..., etag=..., first_publish_date=..., icon=..., id=..., is_deprecated=..., is_featured=..., is_new=..., is_preview=..., last_publish_date=..., name=..., providers=..., publisher_display_name=..., source=..., support=..., system_data=..., threat_analysis_tactics=..., threat_analysis_techniques=..., type=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def author(self) -> Optional[outputs.MetadataAuthorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[outputs.MetadataCategoriesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentId")
    def content_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentKind")
    def content_kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentProductId")
    def content_product_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[outputs.MetadataDependenciesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeprecated")
    def is_deprecated(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFeatured")
    def is_featured(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isNew")
    def is_new(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPreview")
    def is_preview(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def providers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[outputs.MetadataSourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def support(self) -> Optional[outputs.MetadataSupportResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetContentPackageResult(GetContentPackageResult):
    def __await__(self): # -> Generator[Never, Any, GetContentPackageResult]:
        ...
    


def get_content_package(package_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetContentPackageResult:
    
    ...

def get_content_package_output(package_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetContentPackageResult]:
    
    ...

