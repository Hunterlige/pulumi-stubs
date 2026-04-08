import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMetadataResult",
    "AwaitableGetMetadataResult",
    "get_metadata",
    "get_metadata_output",
]

@pulumi.output_type
class GetMetadataResult:
    def __init__(
        __self__,
        author=...,
        azure_api_version=...,
        categories=...,
        content_id=...,
        content_schema_version=...,
        custom_version=...,
        dependencies=...,
        etag=...,
        first_publish_date=...,
        icon=...,
        id=...,
        kind=...,
        last_publish_date=...,
        name=...,
        parent_id=...,
        preview_images=...,
        preview_images_dark=...,
        providers=...,
        source=...,
        support=...,
        system_data=...,
        threat_analysis_tactics=...,
        threat_analysis_techniques=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def author(self) -> Optional[outputs.MetadataAuthorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[outputs.MetadataCategoriesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="contentId")
    def content_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customVersion")
    def custom_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[outputs.MetadataDependenciesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="previewImages")
    def preview_images(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="previewImagesDark")
    def preview_images_dark(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def providers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[outputs.MetadataSourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def support(self) -> Optional[outputs.MetadataSupportResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

class AwaitableGetMetadataResult(GetMetadataResult):
    def __await__(self): ...

def get_metadata(
    metadata_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMetadataResult: ...
def get_metadata_output(
    metadata_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMetadataResult]: ...
