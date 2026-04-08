import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ContentPackageArgs", "ContentPackage"]

@pulumi.input_type
class ContentPackageArgs:
    def __init__(
        __self__,
        *,
        content_id: pulumi.Input[_builtins.str],
        content_kind: pulumi.Input[Union[_builtins.str, PackageKind]],
        content_product_id: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        author: Optional[pulumi.Input[MetadataAuthorArgs]] = ...,
        categories: Optional[pulumi.Input[MetadataCategoriesArgs]] = ...,
        content_schema_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dependencies: Optional[pulumi.Input[MetadataDependenciesArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        first_publish_date: Optional[pulumi.Input[_builtins.str]] = ...,
        icon: Optional[pulumi.Input[_builtins.str]] = ...,
        is_deprecated: Optional[pulumi.Input[Union[_builtins.str, Flag]]] = ...,
        is_featured: Optional[pulumi.Input[Union[_builtins.str, Flag]]] = ...,
        is_new: Optional[pulumi.Input[Union[_builtins.str, Flag]]] = ...,
        is_preview: Optional[pulumi.Input[Union[_builtins.str, Flag]]] = ...,
        last_publish_date: Optional[pulumi.Input[_builtins.str]] = ...,
        package_id: Optional[pulumi.Input[_builtins.str]] = ...,
        providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        publisher_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[MetadataSourceArgs]] = ...,
        support: Optional[pulumi.Input[MetadataSupportArgs]] = ...,
        threat_analysis_tactics: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        threat_analysis_techniques: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentId")
    def content_id(self) -> pulumi.Input[_builtins.str]: ...
    @content_id.setter
    def content_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contentKind")
    def content_kind(self) -> pulumi.Input[Union[_builtins.str, PackageKind]]: ...
    @content_kind.setter
    def content_kind(self, value: pulumi.Input[Union[_builtins.str, PackageKind]]): ...
    @_builtins.property
    @pulumi.getter(name="contentProductId")
    def content_product_id(self) -> pulumi.Input[_builtins.str]: ...
    @content_product_id.setter
    def content_product_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def author(self) -> Optional[pulumi.Input[MetadataAuthorArgs]]: ...
    @author.setter
    def author(self, value: Optional[pulumi.Input[MetadataAuthorArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[MetadataCategoriesArgs]]: ...
    @categories.setter
    def categories(self, value: Optional[pulumi.Input[MetadataCategoriesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_schema_version.setter
    def content_schema_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[pulumi.Input[MetadataDependenciesArgs]]: ...
    @dependencies.setter
    def dependencies(self, value: Optional[pulumi.Input[MetadataDependenciesArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @first_publish_date.setter
    def first_publish_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @icon.setter
    def icon(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeprecated")
    def is_deprecated(self) -> Optional[pulumi.Input[Union[_builtins.str, Flag]]]: ...
    @is_deprecated.setter
    def is_deprecated(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Flag]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isFeatured")
    def is_featured(self) -> Optional[pulumi.Input[Union[_builtins.str, Flag]]]: ...
    @is_featured.setter
    def is_featured(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Flag]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isNew")
    def is_new(self) -> Optional[pulumi.Input[Union[_builtins.str, Flag]]]: ...
    @is_new.setter
    def is_new(self, value: Optional[pulumi.Input[Union[_builtins.str, Flag]]]): ...
    @_builtins.property
    @pulumi.getter(name="isPreview")
    def is_preview(self) -> Optional[pulumi.Input[Union[_builtins.str, Flag]]]: ...
    @is_preview.setter
    def is_preview(self, value: Optional[pulumi.Input[Union[_builtins.str, Flag]]]): ...
    @_builtins.property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_publish_date.setter
    def last_publish_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageId")
    def package_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_id.setter
    def package_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def providers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @providers.setter
    def providers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher_display_name.setter
    def publisher_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[MetadataSourceArgs]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[MetadataSourceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def support(self) -> Optional[pulumi.Input[MetadataSupportArgs]]: ...
    @support.setter
    def support(self, value: Optional[pulumi.Input[MetadataSupportArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @threat_analysis_tactics.setter
    def threat_analysis_tactics(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @threat_analysis_techniques.setter
    def threat_analysis_techniques(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:securityinsights:ContentPackage")
class ContentPackage(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        author: Optional[
            pulumi.Input[Union[MetadataAuthorArgs, MetadataAuthorArgsDict]]
        ] = ...,
        categories: Optional[
            pulumi.Input[Union[MetadataCategoriesArgs, MetadataCategoriesArgsDict]]
        ] = ...,
        content_id: Optional[pulumi.Input[_builtins.str]] = ...,
        content_kind: Optional[pulumi.Input[Union[_builtins.str, PackageKind]]] = ...,
        content_product_id: Optional[pulumi.Input[_builtins.str]] = ...,
        content_schema_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dependencies: Optional[
            pulumi.Input[Union[MetadataDependenciesArgs, MetadataDependenciesArgsDict]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        first_publish_date: Optional[pulumi.Input[_builtins.str]] = ...,
        icon: Optional[pulumi.Input[_builtins.str]] = ...,
        is_deprecated: Optional[pulumi.Input[Union[_builtins.str, Flag]]] = ...,
        is_featured: Optional[pulumi.Input[Union[_builtins.str, Flag]]] = ...,
        is_new: Optional[pulumi.Input[Union[_builtins.str, Flag]]] = ...,
        is_preview: Optional[pulumi.Input[Union[_builtins.str, Flag]]] = ...,
        last_publish_date: Optional[pulumi.Input[_builtins.str]] = ...,
        package_id: Optional[pulumi.Input[_builtins.str]] = ...,
        providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        publisher_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[
            pulumi.Input[Union[MetadataSourceArgs, MetadataSourceArgsDict]]
        ] = ...,
        support: Optional[
            pulumi.Input[Union[MetadataSupportArgs, MetadataSupportArgsDict]]
        ] = ...,
        threat_analysis_tactics: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        threat_analysis_techniques: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ContentPackageArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ContentPackage: ...
    @_builtins.property
    @pulumi.getter
    def author(self) -> pulumi.Output[Optional[outputs.MetadataAuthorResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def categories(
        self,
    ) -> pulumi.Output[Optional[outputs.MetadataCategoriesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="contentId")
    def content_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentKind")
    def content_kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentProductId")
    def content_product_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def dependencies(
        self,
    ) -> pulumi.Output[Optional[outputs.MetadataDependenciesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def icon(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isDeprecated")
    def is_deprecated(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isFeatured")
    def is_featured(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isNew")
    def is_new(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isPreview")
    def is_preview(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def providers(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[outputs.MetadataSourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def support(self) -> pulumi.Output[Optional[outputs.MetadataSupportResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
