

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetContentTemplateResult', 'AwaitableGetContentTemplateResult', 'get_content_template', 'get_content_template_output']
@pulumi.output_type
class GetContentTemplateResult:
    
    def __init__(__self__, author=..., azure_api_version=..., categories=..., content_id=..., content_kind=..., content_product_id=..., content_schema_version=..., custom_version=..., dependant_templates=..., dependencies=..., display_name=..., etag=..., first_publish_date=..., icon=..., id=..., is_deprecated=..., last_publish_date=..., main_template=..., name=..., package_id=..., package_kind=..., package_name=..., package_version=..., preview_images=..., preview_images_dark=..., providers=..., source=..., support=..., system_data=..., threat_analysis_tactics=..., threat_analysis_techniques=..., type=..., version=...) -> None:
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
    @pulumi.getter(name="customVersion")
    def custom_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependantTemplates")
    def dependant_templates(self) -> Sequence[outputs.TemplatePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[outputs.MetadataDependenciesResponse]:
        
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
    def is_deprecated(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainTemplate")
    def main_template(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageId")
    def package_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageKind")
    def package_kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageVersion")
    def package_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="previewImages")
    def preview_images(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="previewImagesDark")
    def preview_images_dark(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def providers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> outputs.MetadataSourceResponse:
        
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
    


class AwaitableGetContentTemplateResult(GetContentTemplateResult):
    def __await__(self): # -> Generator[Never, Any, GetContentTemplateResult]:
        ...
    


def get_content_template(resource_group_name: Optional[_builtins.str] = ..., template_id: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetContentTemplateResult:
    
    ...

def get_content_template_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., template_id: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetContentTemplateResult]:
    
    ...

