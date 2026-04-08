import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataSourceConfigurationArgs",
    "DataSourceConfigurationArgsDict",
    "DataSourceConfigurationS3ConfigurationArgs",
    "DataSourceConfigurationS3ConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    "DataSourceConfigurationTemplateConfigurationArgs",
    ...,
    "DataSourceConfigurationWebCrawlerConfigurationArgs",
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
    ...,
    ...,
    ...,
    ...,
    "ExperienceConfigurationArgs",
    "ExperienceConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ExperienceEndpointArgs",
    "ExperienceEndpointArgsDict",
    "FaqS3PathArgs",
    "FaqS3PathArgsDict",
    "IndexCapacityUnitsArgs",
    "IndexCapacityUnitsArgsDict",
    "IndexDocumentMetadataConfigurationUpdateArgs",
    "IndexDocumentMetadataConfigurationUpdateArgsDict",
    ...,
    ...,
    "IndexDocumentMetadataConfigurationUpdateSearchArgs",
    ...,
    "IndexIndexStatisticArgs",
    "IndexIndexStatisticArgsDict",
    "IndexIndexStatisticFaqStatisticArgs",
    "IndexIndexStatisticFaqStatisticArgsDict",
    "IndexIndexStatisticTextDocumentStatisticArgs",
    "IndexIndexStatisticTextDocumentStatisticArgsDict",
    "IndexServerSideEncryptionConfigurationArgs",
    "IndexServerSideEncryptionConfigurationArgsDict",
    "IndexUserGroupResolutionConfigurationArgs",
    "IndexUserGroupResolutionConfigurationArgsDict",
    "IndexUserTokenConfigurationsArgs",
    "IndexUserTokenConfigurationsArgsDict",
    ...,
    ...,
    ...,
    ...,
    "QuerySuggestionsBlockListSourceS3PathArgs",
    "QuerySuggestionsBlockListSourceS3PathArgsDict",
    "ThesaurusSourceS3PathArgs",
    "ThesaurusSourceS3PathArgsDict",
]

class DataSourceConfigurationArgsDict(TypedDict):
    s3_configuration: NotRequired[
        pulumi.Input[DataSourceConfigurationS3ConfigurationArgsDict]
    ]
    template_configuration: NotRequired[
        pulumi.Input[DataSourceConfigurationTemplateConfigurationArgsDict]
    ]
    web_crawler_configuration: NotRequired[
        pulumi.Input[DataSourceConfigurationWebCrawlerConfigurationArgsDict]
    ]

@pulumi.input_type
class DataSourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        s3_configuration: Optional[
            pulumi.Input[DataSourceConfigurationS3ConfigurationArgs]
        ] = ...,
        template_configuration: Optional[
            pulumi.Input[DataSourceConfigurationTemplateConfigurationArgs]
        ] = ...,
        web_crawler_configuration: Optional[
            pulumi.Input[DataSourceConfigurationWebCrawlerConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    @_utilities.deprecated(...)
    def s3_configuration(
        self,
    ) -> Optional[pulumi.Input[DataSourceConfigurationS3ConfigurationArgs]]: ...
    @s3_configuration.setter
    def s3_configuration(
        self, value: Optional[pulumi.Input[DataSourceConfigurationS3ConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateConfiguration")
    def template_configuration(
        self,
    ) -> Optional[pulumi.Input[DataSourceConfigurationTemplateConfigurationArgs]]: ...
    @template_configuration.setter
    def template_configuration(
        self,
        value: Optional[pulumi.Input[DataSourceConfigurationTemplateConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webCrawlerConfiguration")
    @_utilities.deprecated(...)
    def web_crawler_configuration(
        self,
    ) -> Optional[pulumi.Input[DataSourceConfigurationWebCrawlerConfigurationArgs]]: ...
    @web_crawler_configuration.setter
    def web_crawler_configuration(
        self,
        value: Optional[
            pulumi.Input[DataSourceConfigurationWebCrawlerConfigurationArgs]
        ],
    ): ...

class DataSourceConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    access_control_list_configuration: NotRequired[
        pulumi.Input[
            DataSourceConfigurationS3ConfigurationAccessControlListConfigurationArgsDict
        ]
    ]
    documents_metadata_configuration: NotRequired[
        pulumi.Input[
            DataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationArgsDict
        ]
    ]
    exclusion_patterns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    inclusion_patterns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    inclusion_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DataSourceConfigurationS3ConfigurationArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        access_control_list_configuration: Optional[
            pulumi.Input[
                DataSourceConfigurationS3ConfigurationAccessControlListConfigurationArgs
            ]
        ] = ...,
        documents_metadata_configuration: Optional[
            pulumi.Input[
                DataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationArgs
            ]
        ] = ...,
        exclusion_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        inclusion_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        inclusion_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessControlListConfiguration")
    def access_control_list_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceConfigurationS3ConfigurationAccessControlListConfigurationArgs
        ]
    ]: ...
    @access_control_list_configuration.setter
    def access_control_list_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceConfigurationS3ConfigurationAccessControlListConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="documentsMetadataConfiguration")
    def documents_metadata_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationArgs
        ]
    ]: ...
    @documents_metadata_configuration.setter
    def documents_metadata_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="exclusionPatterns")
    def exclusion_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclusion_patterns.setter
    def exclusion_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inclusionPatterns")
    def inclusion_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inclusion_patterns.setter
    def inclusion_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inclusionPrefixes")
    def inclusion_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inclusion_prefixes.setter
    def inclusion_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataSourceConfigurationS3ConfigurationAccessControlListConfigurationArgsDict(
    TypedDict
):
    key_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceConfigurationS3ConfigurationAccessControlListConfigurationArgs:
    def __init__(
        __self__, *, key_path: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyPath")
    def key_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_path.setter
    def key_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationArgsDict(
    TypedDict
):
    s3_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationArgs:
    def __init__(
        __self__, *, s3_prefix: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_prefix.setter
    def s3_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceConfigurationTemplateConfigurationArgsDict(TypedDict):
    template: pulumi.Input[_builtins.str]

@pulumi.input_type
class DataSourceConfigurationTemplateConfigurationArgs:
    def __init__(__self__, *, template: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Input[_builtins.str]: ...
    @template.setter
    def template(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceConfigurationWebCrawlerConfigurationArgsDict(TypedDict):
    urls: pulumi.Input[DataSourceConfigurationWebCrawlerConfigurationUrlsArgsDict]
    authentication_configuration: NotRequired[
        pulumi.Input[
            DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationArgsDict
        ]
    ]
    crawl_depth: NotRequired[pulumi.Input[_builtins.int]]
    max_content_size_per_page_in_mega_bytes: NotRequired[pulumi.Input[_builtins.float]]
    max_links_per_page: NotRequired[pulumi.Input[_builtins.int]]
    max_urls_per_minute_crawl_rate: NotRequired[pulumi.Input[_builtins.int]]
    proxy_configuration: NotRequired[
        pulumi.Input[
            DataSourceConfigurationWebCrawlerConfigurationProxyConfigurationArgsDict
        ]
    ]
    url_exclusion_patterns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    url_inclusion_patterns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DataSourceConfigurationWebCrawlerConfigurationArgs:
    def __init__(
        __self__,
        *,
        urls: pulumi.Input[DataSourceConfigurationWebCrawlerConfigurationUrlsArgs],
        authentication_configuration: Optional[
            pulumi.Input[
                DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationArgs
            ]
        ] = ...,
        crawl_depth: Optional[pulumi.Input[_builtins.int]] = ...,
        max_content_size_per_page_in_mega_bytes: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        max_links_per_page: Optional[pulumi.Input[_builtins.int]] = ...,
        max_urls_per_minute_crawl_rate: Optional[pulumi.Input[_builtins.int]] = ...,
        proxy_configuration: Optional[
            pulumi.Input[
                DataSourceConfigurationWebCrawlerConfigurationProxyConfigurationArgs
            ]
        ] = ...,
        url_exclusion_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        url_inclusion_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def urls(
        self,
    ) -> pulumi.Input[DataSourceConfigurationWebCrawlerConfigurationUrlsArgs]: ...
    @urls.setter
    def urls(
        self,
        value: pulumi.Input[DataSourceConfigurationWebCrawlerConfigurationUrlsArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationArgs
        ]
    ]: ...
    @authentication_configuration.setter
    def authentication_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="crawlDepth")
    def crawl_depth(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @crawl_depth.setter
    def crawl_depth(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxContentSizePerPageInMegaBytes")
    def max_content_size_per_page_in_mega_bytes(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_content_size_per_page_in_mega_bytes.setter
    def max_content_size_per_page_in_mega_bytes(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxLinksPerPage")
    def max_links_per_page(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_links_per_page.setter
    def max_links_per_page(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxUrlsPerMinuteCrawlRate")
    def max_urls_per_minute_crawl_rate(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_urls_per_minute_crawl_rate.setter
    def max_urls_per_minute_crawl_rate(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="proxyConfiguration")
    def proxy_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceConfigurationWebCrawlerConfigurationProxyConfigurationArgs
        ]
    ]: ...
    @proxy_configuration.setter
    def proxy_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceConfigurationWebCrawlerConfigurationProxyConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="urlExclusionPatterns")
    def url_exclusion_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @url_exclusion_patterns.setter
    def url_exclusion_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="urlInclusionPatterns")
    def url_inclusion_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @url_inclusion_patterns.setter
    def url_inclusion_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationArgsDict(
    TypedDict
):
    basic_authentications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationArgs:
    def __init__(
        __self__,
        *,
        basic_authentications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basicAuthentications")
    def basic_authentications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationArgs
                ]
            ]
        ]
    ]: ...
    @basic_authentications.setter
    def basic_authentications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationArgs
                    ]
                ]
            ]
        ],
    ): ...

class DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationArgsDict(
    TypedDict
):
    credentials: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]

@pulumi.input_type
class DataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationArgs:
    def __init__(
        __self__,
        *,
        credentials: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Input[_builtins.str]: ...
    @credentials.setter
    def credentials(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceConfigurationWebCrawlerConfigurationProxyConfigurationArgsDict(
    TypedDict
):
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    credentials: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceConfigurationWebCrawlerConfigurationProxyConfigurationArgs:
    def __init__(
        __self__,
        *,
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
        credentials: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceConfigurationWebCrawlerConfigurationUrlsArgsDict(TypedDict):
    seed_url_configuration: NotRequired[
        pulumi.Input[
            DataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationArgsDict
        ]
    ]
    site_maps_configuration: NotRequired[
        pulumi.Input[
            DataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class DataSourceConfigurationWebCrawlerConfigurationUrlsArgs:
    def __init__(
        __self__,
        *,
        seed_url_configuration: Optional[
            pulumi.Input[
                DataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationArgs
            ]
        ] = ...,
        site_maps_configuration: Optional[
            pulumi.Input[
                DataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="seedUrlConfiguration")
    def seed_url_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationArgs
        ]
    ]: ...
    @seed_url_configuration.setter
    def seed_url_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="siteMapsConfiguration")
    def site_maps_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationArgs
        ]
    ]: ...
    @site_maps_configuration.setter
    def site_maps_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationArgs
            ]
        ],
    ): ...

class DataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationArgsDict(
    TypedDict
):
    seed_urls: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    web_crawler_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationArgs:
    def __init__(
        __self__,
        *,
        seed_urls: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        web_crawler_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="seedUrls")
    def seed_urls(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @seed_urls.setter
    def seed_urls(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="webCrawlerMode")
    def web_crawler_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_crawler_mode.setter
    def web_crawler_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationArgsDict(
    TypedDict
):
    site_maps: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class DataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationArgs:
    def __init__(
        __self__, *, site_maps: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteMaps")
    def site_maps(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @site_maps.setter
    def site_maps(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class DataSourceCustomDocumentEnrichmentConfigurationArgsDict(TypedDict):
    inline_configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationArgsDict
                ]
            ]
        ]
    ]
    post_extraction_hook_configuration: NotRequired[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationArgsDict
        ]
    ]
    pre_extraction_hook_configuration: NotRequired[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationArgsDict
        ]
    ]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationArgs:
    def __init__(
        __self__,
        *,
        inline_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
        post_extraction_hook_configuration: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationArgs
            ]
        ] = ...,
        pre_extraction_hook_configuration: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationArgs
            ]
        ] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlineConfigurations")
    def inline_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @inline_configurations.setter
    def inline_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="postExtractionHookConfiguration")
    def post_extraction_hook_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationArgs
        ]
    ]: ...
    @post_extraction_hook_configuration.setter
    def post_extraction_hook_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="preExtractionHookConfiguration")
    def pre_extraction_hook_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationArgs
        ]
    ]: ...
    @pre_extraction_hook_configuration.setter
    def pre_extraction_hook_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationArgsDict(
    TypedDict
):
    condition: NotRequired[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionArgsDict
        ]
    ]
    document_content_deletion: NotRequired[pulumi.Input[_builtins.bool]]
    target: NotRequired[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetArgsDict
        ]
    ]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationArgs:
    def __init__(
        __self__,
        *,
        condition: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionArgs
            ]
        ] = ...,
        document_content_deletion: Optional[pulumi.Input[_builtins.bool]] = ...,
        target: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionArgs
        ]
    ]: ...
    @condition.setter
    def condition(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="documentContentDeletion")
    def document_content_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @document_content_deletion.setter
    def document_content_deletion(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetArgs
        ]
    ]: ...
    @target.setter
    def target(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetArgs
            ]
        ],
    ): ...

class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionArgsDict(
    TypedDict
):
    condition_document_attribute_key: pulumi.Input[_builtins.str]
    operator: pulumi.Input[_builtins.str]
    condition_on_value: NotRequired[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionConditionOnValueArgsDict
        ]
    ]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionArgs:
    def __init__(
        __self__,
        *,
        condition_document_attribute_key: pulumi.Input[_builtins.str],
        operator: pulumi.Input[_builtins.str],
        condition_on_value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionConditionOnValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> pulumi.Input[_builtins.str]: ...
    @condition_document_attribute_key.setter
    def condition_document_attribute_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[_builtins.str]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionConditionOnValueArgs
        ]
    ]: ...
    @condition_on_value.setter
    def condition_on_value(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionConditionOnValueArgs
            ]
        ],
    ): ...

class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionConditionOnValueArgsDict(
    TypedDict
):
    date_value: NotRequired[pulumi.Input[_builtins.str]]
    long_value: NotRequired[pulumi.Input[_builtins.int]]
    string_list_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationConditionConditionOnValueArgs:
    def __init__(
        __self__,
        *,
        date_value: Optional[pulumi.Input[_builtins.str]] = ...,
        long_value: Optional[pulumi.Input[_builtins.int]] = ...,
        string_list_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_value.setter
    def date_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="longValue")
    def long_value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @long_value.setter
    def long_value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stringListValues")
    def string_list_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @string_list_values.setter
    def string_list_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetArgsDict(
    TypedDict
):
    target_document_attribute_key: NotRequired[pulumi.Input[_builtins.str]]
    target_document_attribute_value: NotRequired[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetTargetDocumentAttributeValueArgsDict
        ]
    ]
    target_document_attribute_value_deletion: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetArgs:
    def __init__(
        __self__,
        *,
        target_document_attribute_key: Optional[pulumi.Input[_builtins.str]] = ...,
        target_document_attribute_value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetTargetDocumentAttributeValueArgs
            ]
        ] = ...,
        target_document_attribute_value_deletion: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetDocumentAttributeKey")
    def target_document_attribute_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_document_attribute_key.setter
    def target_document_attribute_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDocumentAttributeValue")
    def target_document_attribute_value(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetTargetDocumentAttributeValueArgs
        ]
    ]: ...
    @target_document_attribute_value.setter
    def target_document_attribute_value(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetTargetDocumentAttributeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDocumentAttributeValueDeletion")
    def target_document_attribute_value_deletion(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @target_document_attribute_value_deletion.setter
    def target_document_attribute_value_deletion(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetTargetDocumentAttributeValueArgsDict(
    TypedDict
):
    date_value: NotRequired[pulumi.Input[_builtins.str]]
    long_value: NotRequired[pulumi.Input[_builtins.int]]
    string_list_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationTargetTargetDocumentAttributeValueArgs:
    def __init__(
        __self__,
        *,
        date_value: Optional[pulumi.Input[_builtins.str]] = ...,
        long_value: Optional[pulumi.Input[_builtins.int]] = ...,
        string_list_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_value.setter
    def date_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="longValue")
    def long_value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @long_value.setter
    def long_value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stringListValues")
    def string_list_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @string_list_values.setter
    def string_list_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationArgsDict(
    TypedDict
):
    lambda_arn: pulumi.Input[_builtins.str]
    s3_bucket: pulumi.Input[_builtins.str]
    invocation_condition: NotRequired[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionArgsDict
        ]
    ]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationArgs:
    def __init__(
        __self__,
        *,
        lambda_arn: pulumi.Input[_builtins.str],
        s3_bucket: pulumi.Input[_builtins.str],
        invocation_condition: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket.setter
    def s3_bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="invocationCondition")
    def invocation_condition(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionArgs
        ]
    ]: ...
    @invocation_condition.setter
    def invocation_condition(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionArgs
            ]
        ],
    ): ...

class DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionArgsDict(
    TypedDict
):
    condition_document_attribute_key: pulumi.Input[_builtins.str]
    operator: pulumi.Input[_builtins.str]
    condition_on_value: NotRequired[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueArgsDict
        ]
    ]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionArgs:
    def __init__(
        __self__,
        *,
        condition_document_attribute_key: pulumi.Input[_builtins.str],
        operator: pulumi.Input[_builtins.str],
        condition_on_value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> pulumi.Input[_builtins.str]: ...
    @condition_document_attribute_key.setter
    def condition_document_attribute_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[_builtins.str]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueArgs
        ]
    ]: ...
    @condition_on_value.setter
    def condition_on_value(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueArgs
            ]
        ],
    ): ...

class DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueArgsDict(
    TypedDict
):
    date_value: NotRequired[pulumi.Input[_builtins.str]]
    long_value: NotRequired[pulumi.Input[_builtins.int]]
    string_list_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueArgs:
    def __init__(
        __self__,
        *,
        date_value: Optional[pulumi.Input[_builtins.str]] = ...,
        long_value: Optional[pulumi.Input[_builtins.int]] = ...,
        string_list_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_value.setter
    def date_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="longValue")
    def long_value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @long_value.setter
    def long_value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stringListValues")
    def string_list_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @string_list_values.setter
    def string_list_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationArgsDict(
    TypedDict
):
    lambda_arn: pulumi.Input[_builtins.str]
    s3_bucket: pulumi.Input[_builtins.str]
    invocation_condition: NotRequired[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionArgsDict
        ]
    ]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationArgs:
    def __init__(
        __self__,
        *,
        lambda_arn: pulumi.Input[_builtins.str],
        s3_bucket: pulumi.Input[_builtins.str],
        invocation_condition: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket.setter
    def s3_bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="invocationCondition")
    def invocation_condition(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionArgs
        ]
    ]: ...
    @invocation_condition.setter
    def invocation_condition(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionArgs
            ]
        ],
    ): ...

class DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionArgsDict(
    TypedDict
):
    condition_document_attribute_key: pulumi.Input[_builtins.str]
    operator: pulumi.Input[_builtins.str]
    condition_on_value: NotRequired[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueArgsDict
        ]
    ]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionArgs:
    def __init__(
        __self__,
        *,
        condition_document_attribute_key: pulumi.Input[_builtins.str],
        operator: pulumi.Input[_builtins.str],
        condition_on_value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> pulumi.Input[_builtins.str]: ...
    @condition_document_attribute_key.setter
    def condition_document_attribute_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[_builtins.str]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueArgs
        ]
    ]: ...
    @condition_on_value.setter
    def condition_on_value(
        self,
        value: Optional[
            pulumi.Input[
                DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueArgs
            ]
        ],
    ): ...

class DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueArgsDict(
    TypedDict
):
    date_value: NotRequired[pulumi.Input[_builtins.str]]
    long_value: NotRequired[pulumi.Input[_builtins.int]]
    string_list_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueArgs:
    def __init__(
        __self__,
        *,
        date_value: Optional[pulumi.Input[_builtins.str]] = ...,
        long_value: Optional[pulumi.Input[_builtins.int]] = ...,
        string_list_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_value.setter
    def date_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="longValue")
    def long_value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @long_value.setter
    def long_value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stringListValues")
    def string_list_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @string_list_values.setter
    def string_list_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExperienceConfigurationArgsDict(TypedDict):
    content_source_configuration: NotRequired[
        pulumi.Input[ExperienceConfigurationContentSourceConfigurationArgsDict]
    ]
    user_identity_configuration: NotRequired[
        pulumi.Input[ExperienceConfigurationUserIdentityConfigurationArgsDict]
    ]

@pulumi.input_type
class ExperienceConfigurationArgs:
    def __init__(
        __self__,
        *,
        content_source_configuration: Optional[
            pulumi.Input[ExperienceConfigurationContentSourceConfigurationArgs]
        ] = ...,
        user_identity_configuration: Optional[
            pulumi.Input[ExperienceConfigurationUserIdentityConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentSourceConfiguration")
    def content_source_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ExperienceConfigurationContentSourceConfigurationArgs]
    ]: ...
    @content_source_configuration.setter
    def content_source_configuration(
        self,
        value: Optional[
            pulumi.Input[ExperienceConfigurationContentSourceConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userIdentityConfiguration")
    def user_identity_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ExperienceConfigurationUserIdentityConfigurationArgs]
    ]: ...
    @user_identity_configuration.setter
    def user_identity_configuration(
        self,
        value: Optional[
            pulumi.Input[ExperienceConfigurationUserIdentityConfigurationArgs]
        ],
    ): ...

class ExperienceConfigurationContentSourceConfigurationArgsDict(TypedDict):
    data_source_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    direct_put_content: NotRequired[pulumi.Input[_builtins.bool]]
    faq_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ExperienceConfigurationContentSourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        data_source_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        direct_put_content: Optional[pulumi.Input[_builtins.bool]] = ...,
        faq_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceIds")
    def data_source_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @data_source_ids.setter
    def data_source_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="directPutContent")
    def direct_put_content(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @direct_put_content.setter
    def direct_put_content(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="faqIds")
    def faq_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @faq_ids.setter
    def faq_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ExperienceConfigurationUserIdentityConfigurationArgsDict(TypedDict):
    identity_attribute_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExperienceConfigurationUserIdentityConfigurationArgs:
    def __init__(
        __self__, *, identity_attribute_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityAttributeName")
    def identity_attribute_name(self) -> pulumi.Input[_builtins.str]: ...
    @identity_attribute_name.setter
    def identity_attribute_name(self, value: pulumi.Input[_builtins.str]): ...

class ExperienceEndpointArgsDict(TypedDict):
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    endpoint_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExperienceEndpointArgs:
    def __init__(
        __self__,
        *,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FaqS3PathArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]

@pulumi.input_type
class FaqS3PathArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class IndexCapacityUnitsArgsDict(TypedDict):
    query_capacity_units: NotRequired[pulumi.Input[_builtins.int]]
    storage_capacity_units: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class IndexCapacityUnitsArgs:
    def __init__(
        __self__,
        *,
        query_capacity_units: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_capacity_units: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryCapacityUnits")
    def query_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_capacity_units.setter
    def query_capacity_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageCapacityUnits")
    def storage_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_capacity_units.setter
    def storage_capacity_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class IndexDocumentMetadataConfigurationUpdateArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    relevance: NotRequired[
        pulumi.Input[IndexDocumentMetadataConfigurationUpdateRelevanceArgsDict]
    ]
    search: NotRequired[
        pulumi.Input[IndexDocumentMetadataConfigurationUpdateSearchArgsDict]
    ]

@pulumi.input_type
class IndexDocumentMetadataConfigurationUpdateArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        relevance: Optional[
            pulumi.Input[IndexDocumentMetadataConfigurationUpdateRelevanceArgs]
        ] = ...,
        search: Optional[
            pulumi.Input[IndexDocumentMetadataConfigurationUpdateSearchArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def relevance(
        self,
    ) -> Optional[
        pulumi.Input[IndexDocumentMetadataConfigurationUpdateRelevanceArgs]
    ]: ...
    @relevance.setter
    def relevance(
        self,
        value: Optional[
            pulumi.Input[IndexDocumentMetadataConfigurationUpdateRelevanceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def search(
        self,
    ) -> Optional[pulumi.Input[IndexDocumentMetadataConfigurationUpdateSearchArgs]]: ...
    @search.setter
    def search(
        self,
        value: Optional[
            pulumi.Input[IndexDocumentMetadataConfigurationUpdateSearchArgs]
        ],
    ): ...

class IndexDocumentMetadataConfigurationUpdateRelevanceArgsDict(TypedDict):
    duration: NotRequired[pulumi.Input[_builtins.str]]
    freshness: NotRequired[pulumi.Input[_builtins.bool]]
    importance: NotRequired[pulumi.Input[_builtins.int]]
    rank_order: NotRequired[pulumi.Input[_builtins.str]]
    values_importance_map: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]
    ]

@pulumi.input_type
class IndexDocumentMetadataConfigurationUpdateRelevanceArgs:
    def __init__(
        __self__,
        *,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        freshness: Optional[pulumi.Input[_builtins.bool]] = ...,
        importance: Optional[pulumi.Input[_builtins.int]] = ...,
        rank_order: Optional[pulumi.Input[_builtins.str]] = ...,
        values_importance_map: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def freshness(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @freshness.setter
    def freshness(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def importance(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @importance.setter
    def importance(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rankOrder")
    def rank_order(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rank_order.setter
    def rank_order(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valuesImportanceMap")
    def values_importance_map(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]: ...
    @values_importance_map.setter
    def values_importance_map(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]
    ): ...

class IndexDocumentMetadataConfigurationUpdateSearchArgsDict(TypedDict):
    displayable: NotRequired[pulumi.Input[_builtins.bool]]
    facetable: NotRequired[pulumi.Input[_builtins.bool]]
    searchable: NotRequired[pulumi.Input[_builtins.bool]]
    sortable: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class IndexDocumentMetadataConfigurationUpdateSearchArgs:
    def __init__(
        __self__,
        *,
        displayable: Optional[pulumi.Input[_builtins.bool]] = ...,
        facetable: Optional[pulumi.Input[_builtins.bool]] = ...,
        searchable: Optional[pulumi.Input[_builtins.bool]] = ...,
        sortable: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def displayable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @displayable.setter
    def displayable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def facetable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @facetable.setter
    def facetable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def searchable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @searchable.setter
    def searchable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def sortable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @sortable.setter
    def sortable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class IndexIndexStatisticArgsDict(TypedDict):
    faq_statistics: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[IndexIndexStatisticFaqStatisticArgsDict]]]
    ]
    text_document_statistics: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[IndexIndexStatisticTextDocumentStatisticArgsDict]]
        ]
    ]

@pulumi.input_type
class IndexIndexStatisticArgs:
    def __init__(
        __self__,
        *,
        faq_statistics: Optional[
            pulumi.Input[Sequence[pulumi.Input[IndexIndexStatisticFaqStatisticArgs]]]
        ] = ...,
        text_document_statistics: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[IndexIndexStatisticTextDocumentStatisticArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="faqStatistics")
    def faq_statistics(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[IndexIndexStatisticFaqStatisticArgs]]]
    ]: ...
    @faq_statistics.setter
    def faq_statistics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[IndexIndexStatisticFaqStatisticArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="textDocumentStatistics")
    def text_document_statistics(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[IndexIndexStatisticTextDocumentStatisticArgs]]
        ]
    ]: ...
    @text_document_statistics.setter
    def text_document_statistics(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[IndexIndexStatisticTextDocumentStatisticArgs]]
            ]
        ],
    ): ...

class IndexIndexStatisticFaqStatisticArgsDict(TypedDict):
    indexed_question_answers_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class IndexIndexStatisticFaqStatisticArgs:
    def __init__(
        __self__,
        *,
        indexed_question_answers_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexedQuestionAnswersCount")
    def indexed_question_answers_count(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @indexed_question_answers_count.setter
    def indexed_question_answers_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class IndexIndexStatisticTextDocumentStatisticArgsDict(TypedDict):
    indexed_text_bytes: NotRequired[pulumi.Input[_builtins.int]]
    indexed_text_documents_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class IndexIndexStatisticTextDocumentStatisticArgs:
    def __init__(
        __self__,
        *,
        indexed_text_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        indexed_text_documents_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexedTextBytes")
    def indexed_text_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @indexed_text_bytes.setter
    def indexed_text_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="indexedTextDocumentsCount")
    def indexed_text_documents_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @indexed_text_documents_count.setter
    def indexed_text_documents_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class IndexServerSideEncryptionConfigurationArgsDict(TypedDict):
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IndexServerSideEncryptionConfigurationArgs:
    def __init__(
        __self__, *, kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IndexUserGroupResolutionConfigurationArgsDict(TypedDict):
    user_group_resolution_mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class IndexUserGroupResolutionConfigurationArgs:
    def __init__(
        __self__, *, user_group_resolution_mode: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userGroupResolutionMode")
    def user_group_resolution_mode(self) -> pulumi.Input[_builtins.str]: ...
    @user_group_resolution_mode.setter
    def user_group_resolution_mode(self, value: pulumi.Input[_builtins.str]): ...

class IndexUserTokenConfigurationsArgsDict(TypedDict):
    json_token_type_configuration: NotRequired[
        pulumi.Input[IndexUserTokenConfigurationsJsonTokenTypeConfigurationArgsDict]
    ]
    jwt_token_type_configuration: NotRequired[
        pulumi.Input[IndexUserTokenConfigurationsJwtTokenTypeConfigurationArgsDict]
    ]

@pulumi.input_type
class IndexUserTokenConfigurationsArgs:
    def __init__(
        __self__,
        *,
        json_token_type_configuration: Optional[
            pulumi.Input[IndexUserTokenConfigurationsJsonTokenTypeConfigurationArgs]
        ] = ...,
        jwt_token_type_configuration: Optional[
            pulumi.Input[IndexUserTokenConfigurationsJwtTokenTypeConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jsonTokenTypeConfiguration")
    def json_token_type_configuration(
        self,
    ) -> Optional[
        pulumi.Input[IndexUserTokenConfigurationsJsonTokenTypeConfigurationArgs]
    ]: ...
    @json_token_type_configuration.setter
    def json_token_type_configuration(
        self,
        value: Optional[
            pulumi.Input[IndexUserTokenConfigurationsJsonTokenTypeConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="jwtTokenTypeConfiguration")
    def jwt_token_type_configuration(
        self,
    ) -> Optional[
        pulumi.Input[IndexUserTokenConfigurationsJwtTokenTypeConfigurationArgs]
    ]: ...
    @jwt_token_type_configuration.setter
    def jwt_token_type_configuration(
        self,
        value: Optional[
            pulumi.Input[IndexUserTokenConfigurationsJwtTokenTypeConfigurationArgs]
        ],
    ): ...

class IndexUserTokenConfigurationsJsonTokenTypeConfigurationArgsDict(TypedDict):
    group_attribute_field: pulumi.Input[_builtins.str]
    user_name_attribute_field: pulumi.Input[_builtins.str]

@pulumi.input_type
class IndexUserTokenConfigurationsJsonTokenTypeConfigurationArgs:
    def __init__(
        __self__,
        *,
        group_attribute_field: pulumi.Input[_builtins.str],
        user_name_attribute_field: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupAttributeField")
    def group_attribute_field(self) -> pulumi.Input[_builtins.str]: ...
    @group_attribute_field.setter
    def group_attribute_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userNameAttributeField")
    def user_name_attribute_field(self) -> pulumi.Input[_builtins.str]: ...
    @user_name_attribute_field.setter
    def user_name_attribute_field(self, value: pulumi.Input[_builtins.str]): ...

class IndexUserTokenConfigurationsJwtTokenTypeConfigurationArgsDict(TypedDict):
    key_location: pulumi.Input[_builtins.str]
    claim_regex: NotRequired[pulumi.Input[_builtins.str]]
    group_attribute_field: NotRequired[pulumi.Input[_builtins.str]]
    issuer: NotRequired[pulumi.Input[_builtins.str]]
    secrets_manager_arn: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]
    user_name_attribute_field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IndexUserTokenConfigurationsJwtTokenTypeConfigurationArgs:
    def __init__(
        __self__,
        *,
        key_location: pulumi.Input[_builtins.str],
        claim_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        group_attribute_field: Optional[pulumi.Input[_builtins.str]] = ...,
        issuer: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets_manager_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        user_name_attribute_field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyLocation")
    def key_location(self) -> pulumi.Input[_builtins.str]: ...
    @key_location.setter
    def key_location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="claimRegex")
    def claim_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @claim_regex.setter
    def claim_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupAttributeField")
    def group_attribute_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_attribute_field.setter
    def group_attribute_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerArn")
    def secrets_manager_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secrets_manager_arn.setter
    def secrets_manager_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userNameAttributeField")
    def user_name_attribute_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name_attribute_field.setter
    def user_name_attribute_field(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class QuerySuggestionsBlockListSourceS3PathArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]

@pulumi.input_type
class QuerySuggestionsBlockListSourceS3PathArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class ThesaurusSourceS3PathArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]

@pulumi.input_type
class ThesaurusSourceS3PathArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
