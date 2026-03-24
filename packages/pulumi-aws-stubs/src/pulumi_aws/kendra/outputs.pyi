import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataSourceConfiguration",
    "DataSourceConfigurationS3Configuration",
    ...,
    ...,
    "DataSourceConfigurationTemplateConfiguration",
    "DataSourceConfigurationWebCrawlerConfiguration",
    ...,
    ...,
    ...,
    "DataSourceConfigurationWebCrawlerConfigurationUrls",
    ...,
    ...,
    "DataSourceCustomDocumentEnrichmentConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ExperienceConfiguration",
    "ExperienceConfigurationContentSourceConfiguration",
    "ExperienceConfigurationUserIdentityConfiguration",
    "ExperienceEndpoint",
    "FaqS3Path",
    "IndexCapacityUnits",
    "IndexDocumentMetadataConfigurationUpdate",
    "IndexDocumentMetadataConfigurationUpdateRelevance",
    "IndexDocumentMetadataConfigurationUpdateSearch",
    "IndexIndexStatistic",
    "IndexIndexStatisticFaqStatistic",
    "IndexIndexStatisticTextDocumentStatistic",
    "IndexServerSideEncryptionConfiguration",
    "IndexUserGroupResolutionConfiguration",
    "IndexUserTokenConfigurations",
    ...,
    ...,
    "QuerySuggestionsBlockListSourceS3Path",
    "ThesaurusSourceS3Path",
    "GetExperienceConfigurationResult",
    ...,
    ...,
    "GetExperienceEndpointResult",
    "GetFaqS3PathResult",
    "GetIndexCapacityUnitResult",
    "GetIndexDocumentMetadataConfigurationUpdateResult",
    ...,
    ...,
    "GetIndexIndexStatisticResult",
    "GetIndexIndexStatisticFaqStatisticResult",
    "GetIndexIndexStatisticTextDocumentStatisticResult",
    "GetIndexServerSideEncryptionConfigurationResult",
    "GetIndexUserGroupResolutionConfigurationResult",
    "GetIndexUserTokenConfigurationResult",
    ...,
    ...,
    "GetQuerySuggestionsBlockListSourceS3PathResult",
    "GetThesaurusSourceS3PathResult",
]

@pulumi.output_type
class DataSourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_configuration: Optional[
            outputs.DataSourceConfigurationS3Configuration
        ] = ...,
        template_configuration: Optional[
            outputs.DataSourceConfigurationTemplateConfiguration
        ] = ...,
        web_crawler_configuration: Optional[
            outputs.DataSourceConfigurationWebCrawlerConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    @_utilities.deprecated(...)
    def s3_configuration(
        self,
    ) -> Optional[outputs.DataSourceConfigurationS3Configuration]: ...
    @_builtins.property
    @pulumi.getter(name="templateConfiguration")
    def template_configuration(
        self,
    ) -> Optional[outputs.DataSourceConfigurationTemplateConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="webCrawlerConfiguration")
    @_utilities.deprecated(...)
    def web_crawler_configuration(
        self,
    ) -> Optional[outputs.DataSourceConfigurationWebCrawlerConfiguration]: ...

@pulumi.output_type
class DataSourceConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        access_control_list_configuration: Optional[
            outputs.DataSourceConfigurationS3ConfigurationAccessControlListConfiguration
        ] = ...,
        documents_metadata_configuration: Optional[
            outputs.DataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration
        ] = ...,
        exclusion_patterns: Optional[Sequence[_builtins.str]] = ...,
        inclusion_patterns: Optional[Sequence[_builtins.str]] = ...,
        inclusion_prefixes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessControlListConfiguration")
    def access_control_list_configuration(
        self,
    ) -> Optional[
        outputs.DataSourceConfigurationS3ConfigurationAccessControlListConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="documentsMetadataConfiguration")
    def documents_metadata_configuration(
        self,
    ) -> Optional[
        outputs.DataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="exclusionPatterns")
    def exclusion_patterns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionPatterns")
    def inclusion_patterns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionPrefixes")
    def inclusion_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DataSourceConfigurationS3ConfigurationAccessControlListConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_path: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyPath")
    def key_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_prefix: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceConfigurationTemplateConfiguration(dict):
    def __init__(__self__, *, template: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceConfigurationWebCrawlerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        urls: outputs.DataSourceConfigurationWebCrawlerConfigurationUrls,
        authentication_configuration: Optional[
            outputs.DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration
        ] = ...,
        crawl_depth: Optional[_builtins.int] = ...,
        max_content_size_per_page_in_mega_bytes: Optional[_builtins.float] = ...,
        max_links_per_page: Optional[_builtins.int] = ...,
        max_urls_per_minute_crawl_rate: Optional[_builtins.int] = ...,
        proxy_configuration: Optional[
            outputs.DataSourceConfigurationWebCrawlerConfigurationProxyConfiguration
        ] = ...,
        url_exclusion_patterns: Optional[Sequence[_builtins.str]] = ...,
        url_inclusion_patterns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def urls(self) -> outputs.DataSourceConfigurationWebCrawlerConfigurationUrls: ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> Optional[
        outputs.DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="crawlDepth")
    def crawl_depth(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxContentSizePerPageInMegaBytes")
    def max_content_size_per_page_in_mega_bytes(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="maxLinksPerPage")
    def max_links_per_page(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxUrlsPerMinuteCrawlRate")
    def max_urls_per_minute_crawl_rate(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="proxyConfiguration")
    def proxy_configuration(
        self,
    ) -> Optional[
        outputs.DataSourceConfigurationWebCrawlerConfigurationProxyConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="urlExclusionPatterns")
    def url_exclusion_patterns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="urlInclusionPatterns")
    def url_inclusion_patterns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        basic_authentications: Optional[
            Sequence[
                outputs.DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basicAuthentications")
    def basic_authentications(
        self,
    ) -> Optional[
        Sequence[
            outputs.DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication
        ]
    ]: ...

@pulumi.output_type
class DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication(
    dict
):
    def __init__(
        __self__,
        *,
        credentials: _builtins.str,
        host: _builtins.str,
        port: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceConfigurationWebCrawlerConfigurationProxyConfiguration(dict):
    def __init__(
        __self__,
        *,
        host: _builtins.str,
        port: _builtins.int,
        credentials: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceConfigurationWebCrawlerConfigurationUrls(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        seed_url_configuration: Optional[
            outputs.DataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration
        ] = ...,
        site_maps_configuration: Optional[
            outputs.DataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="seedUrlConfiguration")
    def seed_url_configuration(
        self,
    ) -> Optional[
        outputs.DataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="siteMapsConfiguration")
    def site_maps_configuration(
        self,
    ) -> Optional[
        outputs.DataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration
    ]: ...

@pulumi.output_type
class DataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        seed_urls: Sequence[_builtins.str],
        web_crawler_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="seedUrls")
    def seed_urls(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webCrawlerMode")
    def web_crawler_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, site_maps: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteMaps")
    def site_maps(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inline_configurations: Optional[
            Sequence[
                outputs.DataSourceCustomDocumentEnrichmentConfigurationInlineConfiguration
            ]
        ] = ...,
        post_extraction_hook_configuration: Optional[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration
        ] = ...,
        pre_extraction_hook_configuration: Optional[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration
        ] = ...,
        role_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlineConfigurations")
    def inline_configurations(
        self,
    ) -> Optional[
        Sequence[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationInlineConfiguration
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="postExtractionHookConfiguration")
    def post_extraction_hook_configuration(
        self,
    ) -> Optional[
        outputs.DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="preExtractionHookConfiguration")
    def pre_extraction_hook_configuration(
        self,
    ) -> Optional[
        outputs.DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationInlineConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        condition: Optional[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationCondition
        ] = ...,
        document_content_deletion: Optional[_builtins.bool] = ...,
        target: Optional[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTarget
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[
        outputs.DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationCondition
    ]: ...
    @_builtins.property
    @pulumi.getter(name="documentContentDeletion")
    def document_content_deletion(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def target(
        self,
    ) -> Optional[
        outputs.DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTarget
    ]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        condition_document_attribute_key: _builtins.str,
        operator: _builtins.str,
        condition_on_value: Optional[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionConditionOnValue
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> Optional[
        outputs.DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionConditionOnValue
    ]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionConditionOnValue(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        date_value: Optional[_builtins.str] = ...,
        long_value: Optional[_builtins.int] = ...,
        string_list_values: Optional[Sequence[_builtins.str]] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="longValue")
    def long_value(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stringListValues")
    def string_list_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_document_attribute_key: Optional[_builtins.str] = ...,
        target_document_attribute_value: Optional[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetTargetDocumentAttributeValue
        ] = ...,
        target_document_attribute_value_deletion: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetDocumentAttributeKey")
    def target_document_attribute_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetDocumentAttributeValue")
    def target_document_attribute_value(
        self,
    ) -> Optional[
        outputs.DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetTargetDocumentAttributeValue
    ]: ...
    @_builtins.property
    @pulumi.getter(name="targetDocumentAttributeValueDeletion")
    def target_document_attribute_value_deletion(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetTargetDocumentAttributeValue(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        date_value: Optional[_builtins.str] = ...,
        long_value: Optional[_builtins.int] = ...,
        string_list_values: Optional[Sequence[_builtins.str]] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="longValue")
    def long_value(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stringListValues")
    def string_list_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lambda_arn: _builtins.str,
        s3_bucket: _builtins.str,
        invocation_condition: Optional[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invocationCondition")
    def invocation_condition(
        self,
    ) -> Optional[
        outputs.DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition
    ]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        condition_document_attribute_key: _builtins.str,
        operator: _builtins.str,
        condition_on_value: Optional[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> Optional[
        outputs.DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue
    ]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        date_value: Optional[_builtins.str] = ...,
        long_value: Optional[_builtins.int] = ...,
        string_list_values: Optional[Sequence[_builtins.str]] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="longValue")
    def long_value(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stringListValues")
    def string_list_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lambda_arn: _builtins.str,
        s3_bucket: _builtins.str,
        invocation_condition: Optional[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invocationCondition")
    def invocation_condition(
        self,
    ) -> Optional[
        outputs.DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition
    ]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        condition_document_attribute_key: _builtins.str,
        operator: _builtins.str,
        condition_on_value: Optional[
            outputs.DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> Optional[
        outputs.DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue
    ]: ...

@pulumi.output_type
class DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        date_value: Optional[_builtins.str] = ...,
        long_value: Optional[_builtins.int] = ...,
        string_list_values: Optional[Sequence[_builtins.str]] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="longValue")
    def long_value(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stringListValues")
    def string_list_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExperienceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content_source_configuration: Optional[
            outputs.ExperienceConfigurationContentSourceConfiguration
        ] = ...,
        user_identity_configuration: Optional[
            outputs.ExperienceConfigurationUserIdentityConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentSourceConfiguration")
    def content_source_configuration(
        self,
    ) -> Optional[outputs.ExperienceConfigurationContentSourceConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="userIdentityConfiguration")
    def user_identity_configuration(
        self,
    ) -> Optional[outputs.ExperienceConfigurationUserIdentityConfiguration]: ...

@pulumi.output_type
class ExperienceConfigurationContentSourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source_ids: Optional[Sequence[_builtins.str]] = ...,
        direct_put_content: Optional[_builtins.bool] = ...,
        faq_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceIds")
    def data_source_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="directPutContent")
    def direct_put_content(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="faqIds")
    def faq_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ExperienceConfigurationUserIdentityConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, identity_attribute_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityAttributeName")
    def identity_attribute_name(self) -> _builtins.str: ...

@pulumi.output_type
class ExperienceEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint: Optional[_builtins.str] = ...,
        endpoint_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FaqS3Path(dict):
    def __init__(__self__, *, bucket: _builtins.str, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class IndexCapacityUnits(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        query_capacity_units: Optional[_builtins.int] = ...,
        storage_capacity_units: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryCapacityUnits")
    def query_capacity_units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="storageCapacityUnits")
    def storage_capacity_units(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class IndexDocumentMetadataConfigurationUpdate(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        relevance: Optional[
            outputs.IndexDocumentMetadataConfigurationUpdateRelevance
        ] = ...,
        search: Optional[outputs.IndexDocumentMetadataConfigurationUpdateSearch] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def relevance(
        self,
    ) -> Optional[outputs.IndexDocumentMetadataConfigurationUpdateRelevance]: ...
    @_builtins.property
    @pulumi.getter
    def search(
        self,
    ) -> Optional[outputs.IndexDocumentMetadataConfigurationUpdateSearch]: ...

@pulumi.output_type
class IndexDocumentMetadataConfigurationUpdateRelevance(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        duration: Optional[_builtins.str] = ...,
        freshness: Optional[_builtins.bool] = ...,
        importance: Optional[_builtins.int] = ...,
        rank_order: Optional[_builtins.str] = ...,
        values_importance_map: Optional[Mapping[str, _builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def freshness(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def importance(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rankOrder")
    def rank_order(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valuesImportanceMap")
    def values_importance_map(self) -> Optional[Mapping[str, _builtins.int]]: ...

@pulumi.output_type
class IndexDocumentMetadataConfigurationUpdateSearch(dict):
    def __init__(
        __self__,
        *,
        displayable: Optional[_builtins.bool] = ...,
        facetable: Optional[_builtins.bool] = ...,
        searchable: Optional[_builtins.bool] = ...,
        sortable: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def displayable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def facetable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def searchable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def sortable(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class IndexIndexStatistic(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        faq_statistics: Optional[
            Sequence[outputs.IndexIndexStatisticFaqStatistic]
        ] = ...,
        text_document_statistics: Optional[
            Sequence[outputs.IndexIndexStatisticTextDocumentStatistic]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="faqStatistics")
    def faq_statistics(
        self,
    ) -> Optional[Sequence[outputs.IndexIndexStatisticFaqStatistic]]: ...
    @_builtins.property
    @pulumi.getter(name="textDocumentStatistics")
    def text_document_statistics(
        self,
    ) -> Optional[Sequence[outputs.IndexIndexStatisticTextDocumentStatistic]]: ...

@pulumi.output_type
class IndexIndexStatisticFaqStatistic(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, indexed_question_answers_count: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexedQuestionAnswersCount")
    def indexed_question_answers_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class IndexIndexStatisticTextDocumentStatistic(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        indexed_text_bytes: Optional[_builtins.int] = ...,
        indexed_text_documents_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexedTextBytes")
    def indexed_text_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="indexedTextDocumentsCount")
    def indexed_text_documents_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class IndexServerSideEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IndexUserGroupResolutionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, user_group_resolution_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userGroupResolutionMode")
    def user_group_resolution_mode(self) -> _builtins.str: ...

@pulumi.output_type
class IndexUserTokenConfigurations(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        json_token_type_configuration: Optional[
            outputs.IndexUserTokenConfigurationsJsonTokenTypeConfiguration
        ] = ...,
        jwt_token_type_configuration: Optional[
            outputs.IndexUserTokenConfigurationsJwtTokenTypeConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jsonTokenTypeConfiguration")
    def json_token_type_configuration(
        self,
    ) -> Optional[outputs.IndexUserTokenConfigurationsJsonTokenTypeConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="jwtTokenTypeConfiguration")
    def jwt_token_type_configuration(
        self,
    ) -> Optional[outputs.IndexUserTokenConfigurationsJwtTokenTypeConfiguration]: ...

@pulumi.output_type
class IndexUserTokenConfigurationsJsonTokenTypeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_attribute_field: _builtins.str,
        user_name_attribute_field: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupAttributeField")
    def group_attribute_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userNameAttributeField")
    def user_name_attribute_field(self) -> _builtins.str: ...

@pulumi.output_type
class IndexUserTokenConfigurationsJwtTokenTypeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_location: _builtins.str,
        claim_regex: Optional[_builtins.str] = ...,
        group_attribute_field: Optional[_builtins.str] = ...,
        issuer: Optional[_builtins.str] = ...,
        secrets_manager_arn: Optional[_builtins.str] = ...,
        url: Optional[_builtins.str] = ...,
        user_name_attribute_field: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyLocation")
    def key_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="claimRegex")
    def claim_regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupAttributeField")
    def group_attribute_field(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerArn")
    def secrets_manager_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userNameAttributeField")
    def user_name_attribute_field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class QuerySuggestionsBlockListSourceS3Path(dict):
    def __init__(__self__, *, bucket: _builtins.str, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class ThesaurusSourceS3Path(dict):
    def __init__(__self__, *, bucket: _builtins.str, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class GetExperienceConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        content_source_configurations: Sequence[
            outputs.GetExperienceConfigurationContentSourceConfigurationResult
        ],
        user_identity_configurations: Sequence[
            outputs.GetExperienceConfigurationUserIdentityConfigurationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentSourceConfigurations")
    def content_source_configurations(
        self,
    ) -> Sequence[
        outputs.GetExperienceConfigurationContentSourceConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="userIdentityConfigurations")
    def user_identity_configurations(
        self,
    ) -> Sequence[
        outputs.GetExperienceConfigurationUserIdentityConfigurationResult
    ]: ...

@pulumi.output_type
class GetExperienceConfigurationContentSourceConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        data_source_ids: Sequence[_builtins.str],
        direct_put_content: _builtins.bool,
        faq_ids: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceIds")
    def data_source_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="directPutContent")
    def direct_put_content(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="faqIds")
    def faq_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetExperienceConfigurationUserIdentityConfigurationResult(dict):
    def __init__(__self__, *, identity_attribute_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityAttributeName")
    def identity_attribute_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetExperienceEndpointResult(dict):
    def __init__(
        __self__, *, endpoint: _builtins.str, endpoint_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetFaqS3PathResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class GetIndexCapacityUnitResult(dict):
    def __init__(
        __self__,
        *,
        query_capacity_units: _builtins.int,
        storage_capacity_units: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryCapacityUnits")
    def query_capacity_units(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageCapacityUnits")
    def storage_capacity_units(self) -> _builtins.int: ...

@pulumi.output_type
class GetIndexDocumentMetadataConfigurationUpdateResult(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        relevances: Sequence[
            outputs.GetIndexDocumentMetadataConfigurationUpdateRelevanceResult
        ],
        searches: Sequence[
            outputs.GetIndexDocumentMetadataConfigurationUpdateSearchResult
        ],
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def relevances(
        self,
    ) -> Sequence[
        outputs.GetIndexDocumentMetadataConfigurationUpdateRelevanceResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def searches(
        self,
    ) -> Sequence[outputs.GetIndexDocumentMetadataConfigurationUpdateSearchResult]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetIndexDocumentMetadataConfigurationUpdateRelevanceResult(dict):
    def __init__(
        __self__,
        *,
        duration: _builtins.str,
        freshness: _builtins.bool,
        importance: _builtins.int,
        rank_order: _builtins.str,
        values_importance_map: Mapping[str, _builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def freshness(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def importance(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="rankOrder")
    def rank_order(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="valuesImportanceMap")
    def values_importance_map(self) -> Mapping[str, _builtins.int]: ...

@pulumi.output_type
class GetIndexDocumentMetadataConfigurationUpdateSearchResult(dict):
    def __init__(
        __self__,
        *,
        displayable: _builtins.bool,
        facetable: _builtins.bool,
        searchable: _builtins.bool,
        sortable: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def displayable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def facetable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def searchable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def sortable(self) -> _builtins.bool: ...

@pulumi.output_type
class GetIndexIndexStatisticResult(dict):
    def __init__(
        __self__,
        *,
        faq_statistics: Sequence[outputs.GetIndexIndexStatisticFaqStatisticResult],
        text_document_statistics: Sequence[
            outputs.GetIndexIndexStatisticTextDocumentStatisticResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="faqStatistics")
    def faq_statistics(
        self,
    ) -> Sequence[outputs.GetIndexIndexStatisticFaqStatisticResult]: ...
    @_builtins.property
    @pulumi.getter(name="textDocumentStatistics")
    def text_document_statistics(
        self,
    ) -> Sequence[outputs.GetIndexIndexStatisticTextDocumentStatisticResult]: ...

@pulumi.output_type
class GetIndexIndexStatisticFaqStatisticResult(dict):
    def __init__(
        __self__, *, indexed_question_answers_count: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexedQuestionAnswersCount")
    def indexed_question_answers_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetIndexIndexStatisticTextDocumentStatisticResult(dict):
    def __init__(
        __self__,
        *,
        indexed_text_bytes: _builtins.int,
        indexed_text_documents_count: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexedTextBytes")
    def indexed_text_bytes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="indexedTextDocumentsCount")
    def indexed_text_documents_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetIndexServerSideEncryptionConfigurationResult(dict):
    def __init__(__self__, *, kms_key_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetIndexUserGroupResolutionConfigurationResult(dict):
    def __init__(__self__, *, user_group_resolution_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userGroupResolutionMode")
    def user_group_resolution_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetIndexUserTokenConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        json_token_type_configurations: Sequence[
            outputs.GetIndexUserTokenConfigurationJsonTokenTypeConfigurationResult
        ],
        jwt_token_type_configurations: Sequence[
            outputs.GetIndexUserTokenConfigurationJwtTokenTypeConfigurationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jsonTokenTypeConfigurations")
    def json_token_type_configurations(
        self,
    ) -> Sequence[
        outputs.GetIndexUserTokenConfigurationJsonTokenTypeConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="jwtTokenTypeConfigurations")
    def jwt_token_type_configurations(
        self,
    ) -> Sequence[
        outputs.GetIndexUserTokenConfigurationJwtTokenTypeConfigurationResult
    ]: ...

@pulumi.output_type
class GetIndexUserTokenConfigurationJsonTokenTypeConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        group_attribute_field: _builtins.str,
        user_name_attribute_field: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupAttributeField")
    def group_attribute_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userNameAttributeField")
    def user_name_attribute_field(self) -> _builtins.str: ...

@pulumi.output_type
class GetIndexUserTokenConfigurationJwtTokenTypeConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        claim_regex: _builtins.str,
        group_attribute_field: _builtins.str,
        issuer: _builtins.str,
        key_location: _builtins.str,
        secrets_manager_arn: _builtins.str,
        url: _builtins.str,
        user_name_attribute_field: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="claimRegex")
    def claim_regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupAttributeField")
    def group_attribute_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyLocation")
    def key_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerArn")
    def secrets_manager_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userNameAttributeField")
    def user_name_attribute_field(self) -> _builtins.str: ...

@pulumi.output_type
class GetQuerySuggestionsBlockListSourceS3PathResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class GetThesaurusSourceS3PathResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
