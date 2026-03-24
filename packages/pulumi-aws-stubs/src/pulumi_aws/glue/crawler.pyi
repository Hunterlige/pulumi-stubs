

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CrawlerArgs', 'Crawler']
@pulumi.input_type
class CrawlerArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], role: pulumi.Input[_builtins.str], catalog_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerCatalogTargetArgs]]]] = ..., classifiers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., configuration: Optional[pulumi.Input[_builtins.str]] = ..., delta_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDeltaTargetArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dynamodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDynamodbTargetArgs]]]] = ..., hudi_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerHudiTargetArgs]]]] = ..., iceberg_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerIcebergTargetArgs]]]] = ..., jdbc_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerJdbcTargetArgs]]]] = ..., lake_formation_configuration: Optional[pulumi.Input[CrawlerLakeFormationConfigurationArgs]] = ..., lineage_configuration: Optional[pulumi.Input[CrawlerLineageConfigurationArgs]] = ..., mongodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerMongodbTargetArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., recrawl_policy: Optional[pulumi.Input[CrawlerRecrawlPolicyArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerS3TargetArgs]]]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schema_change_policy: Optional[pulumi.Input[CrawlerSchemaChangePolicyArgs]] = ..., security_configuration: Optional[pulumi.Input[_builtins.str]] = ..., table_prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogTargets")
    def catalog_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerCatalogTargetArgs]]]]:
        
        ...
    
    @catalog_targets.setter
    def catalog_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerCatalogTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def classifiers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @classifiers.setter
    def classifiers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deltaTargets")
    def delta_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDeltaTargetArgs]]]]:
        
        ...
    
    @delta_targets.setter
    def delta_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDeltaTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamodbTargets")
    def dynamodb_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDynamodbTargetArgs]]]]:
        
        ...
    
    @dynamodb_targets.setter
    def dynamodb_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDynamodbTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hudiTargets")
    def hudi_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerHudiTargetArgs]]]]:
        
        ...
    
    @hudi_targets.setter
    def hudi_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerHudiTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icebergTargets")
    def iceberg_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerIcebergTargetArgs]]]]:
        
        ...
    
    @iceberg_targets.setter
    def iceberg_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerIcebergTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jdbcTargets")
    def jdbc_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerJdbcTargetArgs]]]]:
        
        ...
    
    @jdbc_targets.setter
    def jdbc_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerJdbcTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lakeFormationConfiguration")
    def lake_formation_configuration(self) -> Optional[pulumi.Input[CrawlerLakeFormationConfigurationArgs]]:
        
        ...
    
    @lake_formation_configuration.setter
    def lake_formation_configuration(self, value: Optional[pulumi.Input[CrawlerLakeFormationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lineageConfiguration")
    def lineage_configuration(self) -> Optional[pulumi.Input[CrawlerLineageConfigurationArgs]]:
        
        ...
    
    @lineage_configuration.setter
    def lineage_configuration(self, value: Optional[pulumi.Input[CrawlerLineageConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mongodbTargets")
    def mongodb_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerMongodbTargetArgs]]]]:
        
        ...
    
    @mongodb_targets.setter
    def mongodb_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerMongodbTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recrawlPolicy")
    def recrawl_policy(self) -> Optional[pulumi.Input[CrawlerRecrawlPolicyArgs]]:
        
        ...
    
    @recrawl_policy.setter
    def recrawl_policy(self, value: Optional[pulumi.Input[CrawlerRecrawlPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Targets")
    def s3_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerS3TargetArgs]]]]:
        
        ...
    
    @s3_targets.setter
    def s3_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerS3TargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaChangePolicy")
    def schema_change_policy(self) -> Optional[pulumi.Input[CrawlerSchemaChangePolicyArgs]]:
        
        ...
    
    @schema_change_policy.setter
    def schema_change_policy(self, value: Optional[pulumi.Input[CrawlerSchemaChangePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_configuration.setter
    def security_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_prefix.setter
    def table_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _CrawlerState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., catalog_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerCatalogTargetArgs]]]] = ..., classifiers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., configuration: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., delta_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDeltaTargetArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dynamodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDynamodbTargetArgs]]]] = ..., hudi_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerHudiTargetArgs]]]] = ..., iceberg_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerIcebergTargetArgs]]]] = ..., jdbc_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerJdbcTargetArgs]]]] = ..., lake_formation_configuration: Optional[pulumi.Input[CrawlerLakeFormationConfigurationArgs]] = ..., lineage_configuration: Optional[pulumi.Input[CrawlerLineageConfigurationArgs]] = ..., mongodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerMongodbTargetArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., recrawl_policy: Optional[pulumi.Input[CrawlerRecrawlPolicyArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., s3_targets: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerS3TargetArgs]]]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schema_change_policy: Optional[pulumi.Input[CrawlerSchemaChangePolicyArgs]] = ..., security_configuration: Optional[pulumi.Input[_builtins.str]] = ..., table_prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogTargets")
    def catalog_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerCatalogTargetArgs]]]]:
        
        ...
    
    @catalog_targets.setter
    def catalog_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerCatalogTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def classifiers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @classifiers.setter
    def classifiers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deltaTargets")
    def delta_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDeltaTargetArgs]]]]:
        
        ...
    
    @delta_targets.setter
    def delta_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDeltaTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamodbTargets")
    def dynamodb_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDynamodbTargetArgs]]]]:
        
        ...
    
    @dynamodb_targets.setter
    def dynamodb_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerDynamodbTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hudiTargets")
    def hudi_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerHudiTargetArgs]]]]:
        
        ...
    
    @hudi_targets.setter
    def hudi_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerHudiTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icebergTargets")
    def iceberg_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerIcebergTargetArgs]]]]:
        
        ...
    
    @iceberg_targets.setter
    def iceberg_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerIcebergTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jdbcTargets")
    def jdbc_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerJdbcTargetArgs]]]]:
        
        ...
    
    @jdbc_targets.setter
    def jdbc_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerJdbcTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lakeFormationConfiguration")
    def lake_formation_configuration(self) -> Optional[pulumi.Input[CrawlerLakeFormationConfigurationArgs]]:
        
        ...
    
    @lake_formation_configuration.setter
    def lake_formation_configuration(self, value: Optional[pulumi.Input[CrawlerLakeFormationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lineageConfiguration")
    def lineage_configuration(self) -> Optional[pulumi.Input[CrawlerLineageConfigurationArgs]]:
        
        ...
    
    @lineage_configuration.setter
    def lineage_configuration(self, value: Optional[pulumi.Input[CrawlerLineageConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mongodbTargets")
    def mongodb_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerMongodbTargetArgs]]]]:
        
        ...
    
    @mongodb_targets.setter
    def mongodb_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerMongodbTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recrawlPolicy")
    def recrawl_policy(self) -> Optional[pulumi.Input[CrawlerRecrawlPolicyArgs]]:
        
        ...
    
    @recrawl_policy.setter
    def recrawl_policy(self, value: Optional[pulumi.Input[CrawlerRecrawlPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Targets")
    def s3_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerS3TargetArgs]]]]:
        
        ...
    
    @s3_targets.setter
    def s3_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CrawlerS3TargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaChangePolicy")
    def schema_change_policy(self) -> Optional[pulumi.Input[CrawlerSchemaChangePolicyArgs]]:
        
        ...
    
    @schema_change_policy.setter
    def schema_change_policy(self, value: Optional[pulumi.Input[CrawlerSchemaChangePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_configuration.setter
    def security_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_prefix.setter
    def table_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:glue/crawler:Crawler")
class Crawler(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., catalog_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerCatalogTargetArgs, CrawlerCatalogTargetArgsDict]]]]] = ..., classifiers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., configuration: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., delta_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerDeltaTargetArgs, CrawlerDeltaTargetArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dynamodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerDynamodbTargetArgs, CrawlerDynamodbTargetArgsDict]]]]] = ..., hudi_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerHudiTargetArgs, CrawlerHudiTargetArgsDict]]]]] = ..., iceberg_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerIcebergTargetArgs, CrawlerIcebergTargetArgsDict]]]]] = ..., jdbc_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerJdbcTargetArgs, CrawlerJdbcTargetArgsDict]]]]] = ..., lake_formation_configuration: Optional[pulumi.Input[Union[CrawlerLakeFormationConfigurationArgs, CrawlerLakeFormationConfigurationArgsDict]]] = ..., lineage_configuration: Optional[pulumi.Input[Union[CrawlerLineageConfigurationArgs, CrawlerLineageConfigurationArgsDict]]] = ..., mongodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerMongodbTargetArgs, CrawlerMongodbTargetArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., recrawl_policy: Optional[pulumi.Input[Union[CrawlerRecrawlPolicyArgs, CrawlerRecrawlPolicyArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., s3_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerS3TargetArgs, CrawlerS3TargetArgsDict]]]]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schema_change_policy: Optional[pulumi.Input[Union[CrawlerSchemaChangePolicyArgs, CrawlerSchemaChangePolicyArgsDict]]] = ..., security_configuration: Optional[pulumi.Input[_builtins.str]] = ..., table_prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CrawlerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., catalog_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerCatalogTargetArgs, CrawlerCatalogTargetArgsDict]]]]] = ..., classifiers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., configuration: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., delta_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerDeltaTargetArgs, CrawlerDeltaTargetArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dynamodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerDynamodbTargetArgs, CrawlerDynamodbTargetArgsDict]]]]] = ..., hudi_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerHudiTargetArgs, CrawlerHudiTargetArgsDict]]]]] = ..., iceberg_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerIcebergTargetArgs, CrawlerIcebergTargetArgsDict]]]]] = ..., jdbc_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerJdbcTargetArgs, CrawlerJdbcTargetArgsDict]]]]] = ..., lake_formation_configuration: Optional[pulumi.Input[Union[CrawlerLakeFormationConfigurationArgs, CrawlerLakeFormationConfigurationArgsDict]]] = ..., lineage_configuration: Optional[pulumi.Input[Union[CrawlerLineageConfigurationArgs, CrawlerLineageConfigurationArgsDict]]] = ..., mongodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerMongodbTargetArgs, CrawlerMongodbTargetArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., recrawl_policy: Optional[pulumi.Input[Union[CrawlerRecrawlPolicyArgs, CrawlerRecrawlPolicyArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., s3_targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CrawlerS3TargetArgs, CrawlerS3TargetArgsDict]]]]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schema_change_policy: Optional[pulumi.Input[Union[CrawlerSchemaChangePolicyArgs, CrawlerSchemaChangePolicyArgsDict]]] = ..., security_configuration: Optional[pulumi.Input[_builtins.str]] = ..., table_prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Crawler:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogTargets")
    def catalog_targets(self) -> pulumi.Output[Optional[Sequence[outputs.CrawlerCatalogTarget]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classifiers(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deltaTargets")
    def delta_targets(self) -> pulumi.Output[Optional[Sequence[outputs.CrawlerDeltaTarget]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamodbTargets")
    def dynamodb_targets(self) -> pulumi.Output[Optional[Sequence[outputs.CrawlerDynamodbTarget]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hudiTargets")
    def hudi_targets(self) -> pulumi.Output[Optional[Sequence[outputs.CrawlerHudiTarget]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icebergTargets")
    def iceberg_targets(self) -> pulumi.Output[Optional[Sequence[outputs.CrawlerIcebergTarget]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jdbcTargets")
    def jdbc_targets(self) -> pulumi.Output[Optional[Sequence[outputs.CrawlerJdbcTarget]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lakeFormationConfiguration")
    def lake_formation_configuration(self) -> pulumi.Output[Optional[outputs.CrawlerLakeFormationConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lineageConfiguration")
    def lineage_configuration(self) -> pulumi.Output[Optional[outputs.CrawlerLineageConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mongodbTargets")
    def mongodb_targets(self) -> pulumi.Output[Optional[Sequence[outputs.CrawlerMongodbTarget]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recrawlPolicy")
    def recrawl_policy(self) -> pulumi.Output[Optional[outputs.CrawlerRecrawlPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Targets")
    def s3_targets(self) -> pulumi.Output[Optional[Sequence[outputs.CrawlerS3Target]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaChangePolicy")
    def schema_change_policy(self) -> pulumi.Output[Optional[outputs.CrawlerSchemaChangePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


