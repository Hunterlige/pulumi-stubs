

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BillingGroupMetadata', 'BillingGroupProperties', 'CaCertificateRegistrationConfig', 'CaCertificateValidity', 'DomainConfigurationAuthorizerConfig', 'DomainConfigurationTlsConfig', ..., ..., ..., 'IndexingConfigurationThingIndexingConfiguration', ..., ..., ..., 'ProvisioningTemplatePreProvisioningHook', 'ThingGroupMetadata', 'ThingGroupMetadataRootToParentGroup', 'ThingGroupProperties', 'ThingGroupPropertiesAttributePayload', 'ThingTypeProperties', 'TopicRuleCloudwatchAlarm', 'TopicRuleCloudwatchLog', 'TopicRuleCloudwatchMetric', 'TopicRuleDestinationVpcConfiguration', 'TopicRuleDynamodb', 'TopicRuleDynamodbv2', 'TopicRuleDynamodbv2PutItem', 'TopicRuleElasticsearch', 'TopicRuleErrorAction', 'TopicRuleErrorActionCloudwatchAlarm', 'TopicRuleErrorActionCloudwatchLogs', 'TopicRuleErrorActionCloudwatchMetric', 'TopicRuleErrorActionDynamodb', 'TopicRuleErrorActionDynamodbv2', 'TopicRuleErrorActionDynamodbv2PutItem', 'TopicRuleErrorActionElasticsearch', 'TopicRuleErrorActionFirehose', 'TopicRuleErrorActionHttp', 'TopicRuleErrorActionHttpHttpHeader', 'TopicRuleErrorActionIotAnalytics', 'TopicRuleErrorActionIotEvents', 'TopicRuleErrorActionKafka', 'TopicRuleErrorActionKafkaHeader', 'TopicRuleErrorActionKinesis', 'TopicRuleErrorActionLambda', 'TopicRuleErrorActionRepublish', 'TopicRuleErrorActionS3', 'TopicRuleErrorActionSns', 'TopicRuleErrorActionSqs', 'TopicRuleErrorActionStepFunctions', 'TopicRuleErrorActionTimestream', 'TopicRuleErrorActionTimestreamDimension', 'TopicRuleErrorActionTimestreamTimestamp', 'TopicRuleFirehose', 'TopicRuleHttp', 'TopicRuleHttpHttpHeader', 'TopicRuleIotAnalytic', 'TopicRuleIotEvent', 'TopicRuleKafka', 'TopicRuleKafkaHeader', 'TopicRuleKinesis', 'TopicRuleLambda', 'TopicRuleRepublish', 'TopicRuleS3', 'TopicRuleSns', 'TopicRuleSqs', 'TopicRuleStepFunction', 'TopicRuleTimestream', 'TopicRuleTimestreamDimension', 'TopicRuleTimestreamTimestamp']
@pulumi.output_type
class BillingGroupMetadata(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_date: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class BillingGroupProperties(dict):
    def __init__(__self__, *, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CaCertificateRegistrationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: Optional[_builtins.str] = ..., template_body: Optional[_builtins.str] = ..., template_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CaCertificateValidity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, not_after: Optional[_builtins.str] = ..., not_before: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DomainConfigurationAuthorizerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_authorizer_override: Optional[_builtins.bool] = ..., default_authorizer_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAuthorizerOverride")
    def allow_authorizer_override(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAuthorizerName")
    def default_authorizer_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DomainConfigurationTlsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, security_policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IndexingConfigurationThingGroupIndexingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, thing_group_indexing_mode: _builtins.str, custom_fields: Optional[Sequence[outputs.IndexingConfigurationThingGroupIndexingConfigurationCustomField]] = ..., managed_fields: Optional[Sequence[outputs.IndexingConfigurationThingGroupIndexingConfigurationManagedField]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingGroupIndexingMode")
    def thing_group_indexing_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Optional[Sequence[outputs.IndexingConfigurationThingGroupIndexingConfigurationCustomField]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedFields")
    def managed_fields(self) -> Optional[Sequence[outputs.IndexingConfigurationThingGroupIndexingConfigurationManagedField]]:
        
        ...
    


@pulumi.output_type
class IndexingConfigurationThingGroupIndexingConfigurationCustomField(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IndexingConfigurationThingGroupIndexingConfigurationManagedField(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IndexingConfigurationThingIndexingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, thing_indexing_mode: _builtins.str, custom_fields: Optional[Sequence[outputs.IndexingConfigurationThingIndexingConfigurationCustomField]] = ..., device_defender_indexing_mode: Optional[_builtins.str] = ..., filter: Optional[outputs.IndexingConfigurationThingIndexingConfigurationFilter] = ..., managed_fields: Optional[Sequence[outputs.IndexingConfigurationThingIndexingConfigurationManagedField]] = ..., named_shadow_indexing_mode: Optional[_builtins.str] = ..., thing_connectivity_indexing_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingIndexingMode")
    def thing_indexing_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Optional[Sequence[outputs.IndexingConfigurationThingIndexingConfigurationCustomField]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceDefenderIndexingMode")
    def device_defender_indexing_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.IndexingConfigurationThingIndexingConfigurationFilter]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedFields")
    def managed_fields(self) -> Optional[Sequence[outputs.IndexingConfigurationThingIndexingConfigurationManagedField]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namedShadowIndexingMode")
    def named_shadow_indexing_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingConnectivityIndexingMode")
    def thing_connectivity_indexing_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IndexingConfigurationThingIndexingConfigurationCustomField(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IndexingConfigurationThingIndexingConfigurationFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, named_shadow_names: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namedShadowNames")
    def named_shadow_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class IndexingConfigurationThingIndexingConfigurationManagedField(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProvisioningTemplatePreProvisioningHook(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_arn: _builtins.str, payload_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadVersion")
    def payload_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ThingGroupMetadata(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_date: Optional[_builtins.str] = ..., parent_group_name: Optional[_builtins.str] = ..., root_to_parent_groups: Optional[Sequence[outputs.ThingGroupMetadataRootToParentGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentGroupName")
    def parent_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootToParentGroups")
    def root_to_parent_groups(self) -> Optional[Sequence[outputs.ThingGroupMetadataRootToParentGroup]]:
        ...
    


@pulumi.output_type
class ThingGroupMetadataRootToParentGroup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_arn: Optional[_builtins.str] = ..., group_name: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupArn")
    def group_arn(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ThingGroupProperties(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attribute_payload: Optional[outputs.ThingGroupPropertiesAttributePayload] = ..., description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributePayload")
    def attribute_payload(self) -> Optional[outputs.ThingGroupPropertiesAttributePayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ThingGroupPropertiesAttributePayload(dict):
    def __init__(__self__, *, attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class ThingTypeProperties(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., searchable_attributes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchableAttributes")
    def searchable_attributes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class TopicRuleCloudwatchAlarm(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alarm_name: _builtins.str, role_arn: _builtins.str, state_reason: _builtins.str, state_value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateValue")
    def state_value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleCloudwatchLog(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group_name: _builtins.str, role_arn: _builtins.str, batch_mode: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TopicRuleCloudwatchMetric(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_name: _builtins.str, metric_namespace: _builtins.str, metric_unit: _builtins.str, metric_value: _builtins.str, role_arn: _builtins.str, metric_timestamp: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricUnit")
    def metric_unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricValue")
    def metric_value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricTimestamp")
    def metric_timestamp(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleDestinationVpcConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, subnet_ids: Sequence[_builtins.str], vpc_id: _builtins.str, security_groups: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class TopicRuleDynamodb(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hash_key_field: _builtins.str, hash_key_value: _builtins.str, role_arn: _builtins.str, table_name: _builtins.str, hash_key_type: Optional[_builtins.str] = ..., operation: Optional[_builtins.str] = ..., payload_field: Optional[_builtins.str] = ..., range_key_field: Optional[_builtins.str] = ..., range_key_type: Optional[_builtins.str] = ..., range_key_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKeyField")
    def hash_key_field(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKeyValue")
    def hash_key_value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKeyType")
    def hash_key_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadField")
    def payload_field(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKeyField")
    def range_key_field(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKeyType")
    def range_key_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKeyValue")
    def range_key_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleDynamodbv2(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, put_item: Optional[outputs.TopicRuleDynamodbv2PutItem] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="putItem")
    def put_item(self) -> Optional[outputs.TopicRuleDynamodbv2PutItem]:
        
        ...
    


@pulumi.output_type
class TopicRuleDynamodbv2PutItem(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, table_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleElasticsearch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, endpoint: _builtins.str, id: _builtins.str, index: _builtins.str, role_arn: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def index(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_alarm: Optional[outputs.TopicRuleErrorActionCloudwatchAlarm] = ..., cloudwatch_logs: Optional[outputs.TopicRuleErrorActionCloudwatchLogs] = ..., cloudwatch_metric: Optional[outputs.TopicRuleErrorActionCloudwatchMetric] = ..., dynamodb: Optional[outputs.TopicRuleErrorActionDynamodb] = ..., dynamodbv2: Optional[outputs.TopicRuleErrorActionDynamodbv2] = ..., elasticsearch: Optional[outputs.TopicRuleErrorActionElasticsearch] = ..., firehose: Optional[outputs.TopicRuleErrorActionFirehose] = ..., http: Optional[outputs.TopicRuleErrorActionHttp] = ..., iot_analytics: Optional[outputs.TopicRuleErrorActionIotAnalytics] = ..., iot_events: Optional[outputs.TopicRuleErrorActionIotEvents] = ..., kafka: Optional[outputs.TopicRuleErrorActionKafka] = ..., kinesis: Optional[outputs.TopicRuleErrorActionKinesis] = ..., lambda_: Optional[outputs.TopicRuleErrorActionLambda] = ..., republish: Optional[outputs.TopicRuleErrorActionRepublish] = ..., s3: Optional[outputs.TopicRuleErrorActionS3] = ..., sns: Optional[outputs.TopicRuleErrorActionSns] = ..., sqs: Optional[outputs.TopicRuleErrorActionSqs] = ..., step_functions: Optional[outputs.TopicRuleErrorActionStepFunctions] = ..., timestream: Optional[outputs.TopicRuleErrorActionTimestream] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarm")
    def cloudwatch_alarm(self) -> Optional[outputs.TopicRuleErrorActionCloudwatchAlarm]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> Optional[outputs.TopicRuleErrorActionCloudwatchLogs]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchMetric")
    def cloudwatch_metric(self) -> Optional[outputs.TopicRuleErrorActionCloudwatchMetric]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynamodb(self) -> Optional[outputs.TopicRuleErrorActionDynamodb]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynamodbv2(self) -> Optional[outputs.TopicRuleErrorActionDynamodbv2]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def elasticsearch(self) -> Optional[outputs.TopicRuleErrorActionElasticsearch]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def firehose(self) -> Optional[outputs.TopicRuleErrorActionFirehose]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def http(self) -> Optional[outputs.TopicRuleErrorActionHttp]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotAnalytics")
    def iot_analytics(self) -> Optional[outputs.TopicRuleErrorActionIotAnalytics]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotEvents")
    def iot_events(self) -> Optional[outputs.TopicRuleErrorActionIotEvents]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kafka(self) -> Optional[outputs.TopicRuleErrorActionKafka]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kinesis(self) -> Optional[outputs.TopicRuleErrorActionKinesis]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[outputs.TopicRuleErrorActionLambda]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def republish(self) -> Optional[outputs.TopicRuleErrorActionRepublish]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[outputs.TopicRuleErrorActionS3]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sns(self) -> Optional[outputs.TopicRuleErrorActionSns]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sqs(self) -> Optional[outputs.TopicRuleErrorActionSqs]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepFunctions")
    def step_functions(self) -> Optional[outputs.TopicRuleErrorActionStepFunctions]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestream(self) -> Optional[outputs.TopicRuleErrorActionTimestream]:
        ...
    


@pulumi.output_type
class TopicRuleErrorActionCloudwatchAlarm(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alarm_name: _builtins.str, role_arn: _builtins.str, state_reason: _builtins.str, state_value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateValue")
    def state_value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionCloudwatchLogs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group_name: _builtins.str, role_arn: _builtins.str, batch_mode: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionCloudwatchMetric(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_name: _builtins.str, metric_namespace: _builtins.str, metric_unit: _builtins.str, metric_value: _builtins.str, role_arn: _builtins.str, metric_timestamp: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricUnit")
    def metric_unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricValue")
    def metric_value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricTimestamp")
    def metric_timestamp(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionDynamodb(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hash_key_field: _builtins.str, hash_key_value: _builtins.str, role_arn: _builtins.str, table_name: _builtins.str, hash_key_type: Optional[_builtins.str] = ..., operation: Optional[_builtins.str] = ..., payload_field: Optional[_builtins.str] = ..., range_key_field: Optional[_builtins.str] = ..., range_key_type: Optional[_builtins.str] = ..., range_key_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKeyField")
    def hash_key_field(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKeyValue")
    def hash_key_value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKeyType")
    def hash_key_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadField")
    def payload_field(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKeyField")
    def range_key_field(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKeyType")
    def range_key_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKeyValue")
    def range_key_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionDynamodbv2(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, put_item: Optional[outputs.TopicRuleErrorActionDynamodbv2PutItem] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="putItem")
    def put_item(self) -> Optional[outputs.TopicRuleErrorActionDynamodbv2PutItem]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionDynamodbv2PutItem(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, table_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionElasticsearch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, endpoint: _builtins.str, id: _builtins.str, index: _builtins.str, role_arn: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def index(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionFirehose(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delivery_stream_name: _builtins.str, role_arn: _builtins.str, batch_mode: Optional[_builtins.bool] = ..., separator: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryStreamName")
    def delivery_stream_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def separator(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionHttp(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, url: _builtins.str, confirmation_url: Optional[_builtins.str] = ..., http_headers: Optional[Sequence[outputs.TopicRuleErrorActionHttpHttpHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confirmationUrl")
    def confirmation_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[Sequence[outputs.TopicRuleErrorActionHttpHttpHeader]]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionHttpHttpHeader(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionIotAnalytics(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, role_arn: _builtins.str, batch_mode: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionIotEvents(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, input_name: _builtins.str, role_arn: _builtins.str, batch_mode: Optional[_builtins.bool] = ..., message_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputName")
    def input_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionKafka(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_properties: Mapping[str, _builtins.str], destination_arn: _builtins.str, topic: _builtins.str, headers: Optional[Sequence[outputs.TopicRuleErrorActionKafkaHeader]] = ..., key: Optional[_builtins.str] = ..., partition: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientProperties")
    def client_properties(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.TopicRuleErrorActionKafkaHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def partition(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionKafkaHeader(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionKinesis(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, stream_name: _builtins.str, partition_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionLambda(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, function_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionRepublish(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, topic: _builtins.str, qos: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def qos(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionS3(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, key: _builtins.str, role_arn: _builtins.str, canned_acl: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cannedAcl")
    def canned_acl(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionSns(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, target_arn: _builtins.str, message_format: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionSqs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, queue_url: _builtins.str, role_arn: _builtins.str, use_base64: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useBase64")
    def use_base64(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionStepFunctions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, state_machine_name: _builtins.str, execution_name_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMachineName")
    def state_machine_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionNamePrefix")
    def execution_name_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionTimestream(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, dimensions: Sequence[outputs.TopicRuleErrorActionTimestreamDimension], role_arn: _builtins.str, table_name: _builtins.str, timestamp: Optional[outputs.TopicRuleErrorActionTimestreamTimestamp] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Sequence[outputs.TopicRuleErrorActionTimestreamDimension]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[outputs.TopicRuleErrorActionTimestreamTimestamp]:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionTimestreamDimension(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleErrorActionTimestreamTimestamp(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleFirehose(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delivery_stream_name: _builtins.str, role_arn: _builtins.str, batch_mode: Optional[_builtins.bool] = ..., separator: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryStreamName")
    def delivery_stream_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def separator(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleHttp(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, url: _builtins.str, confirmation_url: Optional[_builtins.str] = ..., http_headers: Optional[Sequence[outputs.TopicRuleHttpHttpHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confirmationUrl")
    def confirmation_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[Sequence[outputs.TopicRuleHttpHttpHeader]]:
        
        ...
    


@pulumi.output_type
class TopicRuleHttpHttpHeader(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleIotAnalytic(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, role_arn: _builtins.str, batch_mode: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TopicRuleIotEvent(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, input_name: _builtins.str, role_arn: _builtins.str, batch_mode: Optional[_builtins.bool] = ..., message_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputName")
    def input_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleKafka(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_properties: Mapping[str, _builtins.str], destination_arn: _builtins.str, topic: _builtins.str, headers: Optional[Sequence[outputs.TopicRuleKafkaHeader]] = ..., key: Optional[_builtins.str] = ..., partition: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientProperties")
    def client_properties(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.TopicRuleKafkaHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def partition(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleKafkaHeader(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleKinesis(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, stream_name: _builtins.str, partition_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleLambda(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, function_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleRepublish(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, topic: _builtins.str, qos: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def qos(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TopicRuleS3(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, key: _builtins.str, role_arn: _builtins.str, canned_acl: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cannedAcl")
    def canned_acl(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleSns(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, target_arn: _builtins.str, message_format: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleSqs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, queue_url: _builtins.str, role_arn: _builtins.str, use_base64: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useBase64")
    def use_base64(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class TopicRuleStepFunction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, state_machine_name: _builtins.str, execution_name_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMachineName")
    def state_machine_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionNamePrefix")
    def execution_name_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicRuleTimestream(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, dimensions: Sequence[outputs.TopicRuleTimestreamDimension], role_arn: _builtins.str, table_name: _builtins.str, timestamp: Optional[outputs.TopicRuleTimestreamTimestamp] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Sequence[outputs.TopicRuleTimestreamDimension]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[outputs.TopicRuleTimestreamTimestamp]:
        
        ...
    


@pulumi.output_type
class TopicRuleTimestreamDimension(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicRuleTimestreamTimestamp(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


