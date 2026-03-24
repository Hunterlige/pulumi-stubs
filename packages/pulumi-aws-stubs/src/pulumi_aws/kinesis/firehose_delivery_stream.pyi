import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FirehoseDeliveryStreamArgs", "FirehoseDeliveryStream"]

@pulumi.input_type
class FirehoseDeliveryStreamArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[_builtins.str],
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_id: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticsearch_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationArgs]
        ] = ...,
        extended_s3_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationArgs]
        ] = ...,
        http_endpoint_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationArgs]
        ] = ...,
        iceberg_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationArgs]
        ] = ...,
        kinesis_source_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamKinesisSourceConfigurationArgs]
        ] = ...,
        msk_source_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamMskSourceConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearch_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationArgs]
        ] = ...,
        opensearchserverless_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationArgs]
        ] = ...,
        redshift_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        server_side_encryption: Optional[
            pulumi.Input[FirehoseDeliveryStreamServerSideEncryptionArgs]
        ] = ...,
        snowflake_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationArgs]
        ] = ...,
        splunk_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationId")
    def destination_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_id.setter
    def destination_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="elasticsearchConfiguration")
    def elasticsearch_configuration(
        self,
    ) -> Optional[
        pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationArgs]
    ]: ...
    @elasticsearch_configuration.setter
    def elasticsearch_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedS3Configuration")
    def extended_s3_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationArgs]]: ...
    @extended_s3_configuration.setter
    def extended_s3_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpEndpointConfiguration")
    def http_endpoint_configuration(
        self,
    ) -> Optional[
        pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationArgs]
    ]: ...
    @http_endpoint_configuration.setter
    def http_endpoint_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="icebergConfiguration")
    def iceberg_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationArgs]]: ...
    @iceberg_configuration.setter
    def iceberg_configuration(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kinesisSourceConfiguration")
    def kinesis_source_configuration(
        self,
    ) -> Optional[
        pulumi.Input[FirehoseDeliveryStreamKinesisSourceConfigurationArgs]
    ]: ...
    @kinesis_source_configuration.setter
    def kinesis_source_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamKinesisSourceConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mskSourceConfiguration")
    def msk_source_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamMskSourceConfigurationArgs]]: ...
    @msk_source_configuration.setter
    def msk_source_configuration(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamMskSourceConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="opensearchConfiguration")
    def opensearch_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationArgs]]: ...
    @opensearch_configuration.setter
    def opensearch_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="opensearchserverlessConfiguration")
    def opensearchserverless_configuration(
        self,
    ) -> Optional[
        pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationArgs]
    ]: ...
    @opensearchserverless_configuration.setter
    def opensearchserverless_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redshiftConfiguration")
    def redshift_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationArgs]]: ...
    @redshift_configuration.setter
    def redshift_configuration(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamServerSideEncryptionArgs]]: ...
    @server_side_encryption.setter
    def server_side_encryption(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamServerSideEncryptionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="snowflakeConfiguration")
    def snowflake_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationArgs]]: ...
    @snowflake_configuration.setter
    def snowflake_configuration(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="splunkConfiguration")
    def splunk_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationArgs]]: ...
    @splunk_configuration.setter
    def splunk_configuration(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _FirehoseDeliveryStreamState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_id: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticsearch_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationArgs]
        ] = ...,
        extended_s3_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationArgs]
        ] = ...,
        http_endpoint_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationArgs]
        ] = ...,
        iceberg_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationArgs]
        ] = ...,
        kinesis_source_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamKinesisSourceConfigurationArgs]
        ] = ...,
        msk_source_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamMskSourceConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearch_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationArgs]
        ] = ...,
        opensearchserverless_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationArgs]
        ] = ...,
        redshift_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        server_side_encryption: Optional[
            pulumi.Input[FirehoseDeliveryStreamServerSideEncryptionArgs]
        ] = ...,
        snowflake_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationArgs]
        ] = ...,
        splunk_configuration: Optional[
            pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationId")
    def destination_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_id.setter
    def destination_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="elasticsearchConfiguration")
    def elasticsearch_configuration(
        self,
    ) -> Optional[
        pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationArgs]
    ]: ...
    @elasticsearch_configuration.setter
    def elasticsearch_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedS3Configuration")
    def extended_s3_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationArgs]]: ...
    @extended_s3_configuration.setter
    def extended_s3_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpEndpointConfiguration")
    def http_endpoint_configuration(
        self,
    ) -> Optional[
        pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationArgs]
    ]: ...
    @http_endpoint_configuration.setter
    def http_endpoint_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="icebergConfiguration")
    def iceberg_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationArgs]]: ...
    @iceberg_configuration.setter
    def iceberg_configuration(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kinesisSourceConfiguration")
    def kinesis_source_configuration(
        self,
    ) -> Optional[
        pulumi.Input[FirehoseDeliveryStreamKinesisSourceConfigurationArgs]
    ]: ...
    @kinesis_source_configuration.setter
    def kinesis_source_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamKinesisSourceConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mskSourceConfiguration")
    def msk_source_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamMskSourceConfigurationArgs]]: ...
    @msk_source_configuration.setter
    def msk_source_configuration(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamMskSourceConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="opensearchConfiguration")
    def opensearch_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationArgs]]: ...
    @opensearch_configuration.setter
    def opensearch_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="opensearchserverlessConfiguration")
    def opensearchserverless_configuration(
        self,
    ) -> Optional[
        pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationArgs]
    ]: ...
    @opensearchserverless_configuration.setter
    def opensearchserverless_configuration(
        self,
        value: Optional[
            pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redshiftConfiguration")
    def redshift_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationArgs]]: ...
    @redshift_configuration.setter
    def redshift_configuration(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamServerSideEncryptionArgs]]: ...
    @server_side_encryption.setter
    def server_side_encryption(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamServerSideEncryptionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="snowflakeConfiguration")
    def snowflake_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationArgs]]: ...
    @snowflake_configuration.setter
    def snowflake_configuration(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="splunkConfiguration")
    def splunk_configuration(
        self,
    ) -> Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationArgs]]: ...
    @splunk_configuration.setter
    def splunk_configuration(
        self,
        value: Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class FirehoseDeliveryStream(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_id: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticsearch_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamElasticsearchConfigurationArgs,
                    FirehoseDeliveryStreamElasticsearchConfigurationArgsDict,
                ]
            ]
        ] = ...,
        extended_s3_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamExtendedS3ConfigurationArgs,
                    FirehoseDeliveryStreamExtendedS3ConfigurationArgsDict,
                ]
            ]
        ] = ...,
        http_endpoint_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamHttpEndpointConfigurationArgs,
                    FirehoseDeliveryStreamHttpEndpointConfigurationArgsDict,
                ]
            ]
        ] = ...,
        iceberg_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamIcebergConfigurationArgs,
                    FirehoseDeliveryStreamIcebergConfigurationArgsDict,
                ]
            ]
        ] = ...,
        kinesis_source_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamKinesisSourceConfigurationArgs,
                    FirehoseDeliveryStreamKinesisSourceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        msk_source_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamMskSourceConfigurationArgs,
                    FirehoseDeliveryStreamMskSourceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearch_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamOpensearchConfigurationArgs,
                    FirehoseDeliveryStreamOpensearchConfigurationArgsDict,
                ]
            ]
        ] = ...,
        opensearchserverless_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamOpensearchserverlessConfigurationArgs,
                    FirehoseDeliveryStreamOpensearchserverlessConfigurationArgsDict,
                ]
            ]
        ] = ...,
        redshift_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamRedshiftConfigurationArgs,
                    FirehoseDeliveryStreamRedshiftConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        server_side_encryption: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamServerSideEncryptionArgs,
                    FirehoseDeliveryStreamServerSideEncryptionArgsDict,
                ]
            ]
        ] = ...,
        snowflake_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamSnowflakeConfigurationArgs,
                    FirehoseDeliveryStreamSnowflakeConfigurationArgsDict,
                ]
            ]
        ] = ...,
        splunk_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamSplunkConfigurationArgs,
                    FirehoseDeliveryStreamSplunkConfigurationArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FirehoseDeliveryStreamArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_id: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticsearch_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamElasticsearchConfigurationArgs,
                    FirehoseDeliveryStreamElasticsearchConfigurationArgsDict,
                ]
            ]
        ] = ...,
        extended_s3_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamExtendedS3ConfigurationArgs,
                    FirehoseDeliveryStreamExtendedS3ConfigurationArgsDict,
                ]
            ]
        ] = ...,
        http_endpoint_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamHttpEndpointConfigurationArgs,
                    FirehoseDeliveryStreamHttpEndpointConfigurationArgsDict,
                ]
            ]
        ] = ...,
        iceberg_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamIcebergConfigurationArgs,
                    FirehoseDeliveryStreamIcebergConfigurationArgsDict,
                ]
            ]
        ] = ...,
        kinesis_source_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamKinesisSourceConfigurationArgs,
                    FirehoseDeliveryStreamKinesisSourceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        msk_source_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamMskSourceConfigurationArgs,
                    FirehoseDeliveryStreamMskSourceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearch_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamOpensearchConfigurationArgs,
                    FirehoseDeliveryStreamOpensearchConfigurationArgsDict,
                ]
            ]
        ] = ...,
        opensearchserverless_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamOpensearchserverlessConfigurationArgs,
                    FirehoseDeliveryStreamOpensearchserverlessConfigurationArgsDict,
                ]
            ]
        ] = ...,
        redshift_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamRedshiftConfigurationArgs,
                    FirehoseDeliveryStreamRedshiftConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        server_side_encryption: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamServerSideEncryptionArgs,
                    FirehoseDeliveryStreamServerSideEncryptionArgsDict,
                ]
            ]
        ] = ...,
        snowflake_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamSnowflakeConfigurationArgs,
                    FirehoseDeliveryStreamSnowflakeConfigurationArgsDict,
                ]
            ]
        ] = ...,
        splunk_configuration: Optional[
            pulumi.Input[
                Union[
                    FirehoseDeliveryStreamSplunkConfigurationArgs,
                    FirehoseDeliveryStreamSplunkConfigurationArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> FirehoseDeliveryStream: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationId")
    def destination_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="elasticsearchConfiguration")
    def elasticsearch_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamElasticsearchConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="extendedS3Configuration")
    def extended_s3_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamExtendedS3Configuration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="httpEndpointConfiguration")
    def http_endpoint_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamHttpEndpointConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="icebergConfiguration")
    def iceberg_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamIcebergConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisSourceConfiguration")
    def kinesis_source_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamKinesisSourceConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mskSourceConfiguration")
    def msk_source_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamMskSourceConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="opensearchConfiguration")
    def opensearch_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamOpensearchConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="opensearchserverlessConfiguration")
    def opensearchserverless_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamOpensearchserverlessConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="redshiftConfiguration")
    def redshift_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamRedshiftConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamServerSideEncryption]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="snowflakeConfiguration")
    def snowflake_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirehoseDeliveryStreamSnowflakeConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="splunkConfiguration")
    def splunk_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.FirehoseDeliveryStreamSplunkConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[_builtins.str]: ...
