

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
__all__ = ['TopicRuleArgs', 'TopicRule']
@pulumi.input_type
class TopicRuleArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], sql: pulumi.Input[_builtins.str], sql_version: pulumi.Input[_builtins.str], cloudwatch_alarms: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchAlarmArgs]]]] = ..., cloudwatch_logs: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchLogArgs]]]] = ..., cloudwatch_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchMetricArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dynamodbs: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbArgs]]]] = ..., dynamodbv2s: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbv2Args]]]] = ..., elasticsearch: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleElasticsearchArgs]]]] = ..., error_action: Optional[pulumi.Input[TopicRuleErrorActionArgs]] = ..., firehoses: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleFirehoseArgs]]]] = ..., https: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleHttpArgs]]]] = ..., iot_analytics: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotAnalyticArgs]]]] = ..., iot_events: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotEventArgs]]]] = ..., kafkas: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKafkaArgs]]]] = ..., kineses: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKinesisArgs]]]] = ..., lambdas: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleLambdaArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., republishes: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleRepublishArgs]]]] = ..., s3: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleS3Args]]]] = ..., sns: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSnsArgs]]]] = ..., sqs: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSqsArgs]]]] = ..., step_functions: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleStepFunctionArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timestreams: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleTimestreamArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sql(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql.setter
    def sql(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVersion")
    def sql_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_version.setter
    def sql_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarms")
    def cloudwatch_alarms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchAlarmArgs]]]]:
        ...
    
    @cloudwatch_alarms.setter
    def cloudwatch_alarms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchAlarmArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchLogArgs]]]]:
        ...
    
    @cloudwatch_logs.setter
    def cloudwatch_logs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchLogArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchMetrics")
    def cloudwatch_metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchMetricArgs]]]]:
        ...
    
    @cloudwatch_metrics.setter
    def cloudwatch_metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchMetricArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynamodbs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbArgs]]]]:
        ...
    
    @dynamodbs.setter
    def dynamodbs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynamodbv2s(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbv2Args]]]]:
        ...
    
    @dynamodbv2s.setter
    def dynamodbv2s(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbv2Args]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def elasticsearch(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleElasticsearchArgs]]]]:
        ...
    
    @elasticsearch.setter
    def elasticsearch(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleElasticsearchArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorAction")
    def error_action(self) -> Optional[pulumi.Input[TopicRuleErrorActionArgs]]:
        
        ...
    
    @error_action.setter
    def error_action(self, value: Optional[pulumi.Input[TopicRuleErrorActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def firehoses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleFirehoseArgs]]]]:
        ...
    
    @firehoses.setter
    def firehoses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleFirehoseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def https(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleHttpArgs]]]]:
        ...
    
    @https.setter
    def https(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleHttpArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotAnalytics")
    def iot_analytics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotAnalyticArgs]]]]:
        ...
    
    @iot_analytics.setter
    def iot_analytics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotAnalyticArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotEvents")
    def iot_events(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotEventArgs]]]]:
        ...
    
    @iot_events.setter
    def iot_events(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotEventArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kafkas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKafkaArgs]]]]:
        ...
    
    @kafkas.setter
    def kafkas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKafkaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kineses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKinesisArgs]]]]:
        ...
    
    @kineses.setter
    def kineses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKinesisArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lambdas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleLambdaArgs]]]]:
        ...
    
    @lambdas.setter
    def lambdas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleLambdaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def republishes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleRepublishArgs]]]]:
        ...
    
    @republishes.setter
    def republishes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleRepublishArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleS3Args]]]]:
        ...
    
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleS3Args]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSnsArgs]]]]:
        ...
    
    @sns.setter
    def sns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSnsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sqs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSqsArgs]]]]:
        ...
    
    @sqs.setter
    def sqs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSqsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepFunctions")
    def step_functions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleStepFunctionArgs]]]]:
        ...
    
    @step_functions.setter
    def step_functions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleStepFunctionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestreams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleTimestreamArgs]]]]:
        ...
    
    @timestreams.setter
    def timestreams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleTimestreamArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _TopicRuleState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., cloudwatch_alarms: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchAlarmArgs]]]] = ..., cloudwatch_logs: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchLogArgs]]]] = ..., cloudwatch_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchMetricArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dynamodbs: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbArgs]]]] = ..., dynamodbv2s: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbv2Args]]]] = ..., elasticsearch: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleElasticsearchArgs]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., error_action: Optional[pulumi.Input[TopicRuleErrorActionArgs]] = ..., firehoses: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleFirehoseArgs]]]] = ..., https: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleHttpArgs]]]] = ..., iot_analytics: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotAnalyticArgs]]]] = ..., iot_events: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotEventArgs]]]] = ..., kafkas: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKafkaArgs]]]] = ..., kineses: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKinesisArgs]]]] = ..., lambdas: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleLambdaArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., republishes: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleRepublishArgs]]]] = ..., s3: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleS3Args]]]] = ..., sns: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSnsArgs]]]] = ..., sql: Optional[pulumi.Input[_builtins.str]] = ..., sql_version: Optional[pulumi.Input[_builtins.str]] = ..., sqs: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSqsArgs]]]] = ..., step_functions: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleStepFunctionArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timestreams: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleTimestreamArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarms")
    def cloudwatch_alarms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchAlarmArgs]]]]:
        ...
    
    @cloudwatch_alarms.setter
    def cloudwatch_alarms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchAlarmArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchLogArgs]]]]:
        ...
    
    @cloudwatch_logs.setter
    def cloudwatch_logs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchLogArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchMetrics")
    def cloudwatch_metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchMetricArgs]]]]:
        ...
    
    @cloudwatch_metrics.setter
    def cloudwatch_metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleCloudwatchMetricArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynamodbs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbArgs]]]]:
        ...
    
    @dynamodbs.setter
    def dynamodbs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynamodbv2s(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbv2Args]]]]:
        ...
    
    @dynamodbv2s.setter
    def dynamodbv2s(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleDynamodbv2Args]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def elasticsearch(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleElasticsearchArgs]]]]:
        ...
    
    @elasticsearch.setter
    def elasticsearch(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleElasticsearchArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorAction")
    def error_action(self) -> Optional[pulumi.Input[TopicRuleErrorActionArgs]]:
        
        ...
    
    @error_action.setter
    def error_action(self, value: Optional[pulumi.Input[TopicRuleErrorActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def firehoses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleFirehoseArgs]]]]:
        ...
    
    @firehoses.setter
    def firehoses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleFirehoseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def https(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleHttpArgs]]]]:
        ...
    
    @https.setter
    def https(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleHttpArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotAnalytics")
    def iot_analytics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotAnalyticArgs]]]]:
        ...
    
    @iot_analytics.setter
    def iot_analytics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotAnalyticArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotEvents")
    def iot_events(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotEventArgs]]]]:
        ...
    
    @iot_events.setter
    def iot_events(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleIotEventArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kafkas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKafkaArgs]]]]:
        ...
    
    @kafkas.setter
    def kafkas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKafkaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kineses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKinesisArgs]]]]:
        ...
    
    @kineses.setter
    def kineses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKinesisArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lambdas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleLambdaArgs]]]]:
        ...
    
    @lambdas.setter
    def lambdas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleLambdaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def republishes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleRepublishArgs]]]]:
        ...
    
    @republishes.setter
    def republishes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleRepublishArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleS3Args]]]]:
        ...
    
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleS3Args]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSnsArgs]]]]:
        ...
    
    @sns.setter
    def sns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSnsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sql(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql.setter
    def sql(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVersion")
    def sql_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_version.setter
    def sql_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sqs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSqsArgs]]]]:
        ...
    
    @sqs.setter
    def sqs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleSqsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepFunctions")
    def step_functions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleStepFunctionArgs]]]]:
        ...
    
    @step_functions.setter
    def step_functions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleStepFunctionArgs]]]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def timestreams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleTimestreamArgs]]]]:
        ...
    
    @timestreams.setter
    def timestreams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleTimestreamArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:iot/topicRule:TopicRule")
class TopicRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cloudwatch_alarms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleCloudwatchAlarmArgs, TopicRuleCloudwatchAlarmArgsDict]]]]] = ..., cloudwatch_logs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleCloudwatchLogArgs, TopicRuleCloudwatchLogArgsDict]]]]] = ..., cloudwatch_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleCloudwatchMetricArgs, TopicRuleCloudwatchMetricArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dynamodbs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleDynamodbArgs, TopicRuleDynamodbArgsDict]]]]] = ..., dynamodbv2s: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleDynamodbv2Args, TopicRuleDynamodbv2ArgsDict]]]]] = ..., elasticsearch: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleElasticsearchArgs, TopicRuleElasticsearchArgsDict]]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., error_action: Optional[pulumi.Input[Union[TopicRuleErrorActionArgs, TopicRuleErrorActionArgsDict]]] = ..., firehoses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleFirehoseArgs, TopicRuleFirehoseArgsDict]]]]] = ..., https: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleHttpArgs, TopicRuleHttpArgsDict]]]]] = ..., iot_analytics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleIotAnalyticArgs, TopicRuleIotAnalyticArgsDict]]]]] = ..., iot_events: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleIotEventArgs, TopicRuleIotEventArgsDict]]]]] = ..., kafkas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleKafkaArgs, TopicRuleKafkaArgsDict]]]]] = ..., kineses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleKinesisArgs, TopicRuleKinesisArgsDict]]]]] = ..., lambdas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleLambdaArgs, TopicRuleLambdaArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., republishes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleRepublishArgs, TopicRuleRepublishArgsDict]]]]] = ..., s3: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleS3Args, TopicRuleS3ArgsDict]]]]] = ..., sns: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleSnsArgs, TopicRuleSnsArgsDict]]]]] = ..., sql: Optional[pulumi.Input[_builtins.str]] = ..., sql_version: Optional[pulumi.Input[_builtins.str]] = ..., sqs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleSqsArgs, TopicRuleSqsArgsDict]]]]] = ..., step_functions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleStepFunctionArgs, TopicRuleStepFunctionArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timestreams: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleTimestreamArgs, TopicRuleTimestreamArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TopicRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cloudwatch_alarms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleCloudwatchAlarmArgs, TopicRuleCloudwatchAlarmArgsDict]]]]] = ..., cloudwatch_logs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleCloudwatchLogArgs, TopicRuleCloudwatchLogArgsDict]]]]] = ..., cloudwatch_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleCloudwatchMetricArgs, TopicRuleCloudwatchMetricArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dynamodbs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleDynamodbArgs, TopicRuleDynamodbArgsDict]]]]] = ..., dynamodbv2s: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleDynamodbv2Args, TopicRuleDynamodbv2ArgsDict]]]]] = ..., elasticsearch: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleElasticsearchArgs, TopicRuleElasticsearchArgsDict]]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., error_action: Optional[pulumi.Input[Union[TopicRuleErrorActionArgs, TopicRuleErrorActionArgsDict]]] = ..., firehoses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleFirehoseArgs, TopicRuleFirehoseArgsDict]]]]] = ..., https: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleHttpArgs, TopicRuleHttpArgsDict]]]]] = ..., iot_analytics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleIotAnalyticArgs, TopicRuleIotAnalyticArgsDict]]]]] = ..., iot_events: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleIotEventArgs, TopicRuleIotEventArgsDict]]]]] = ..., kafkas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleKafkaArgs, TopicRuleKafkaArgsDict]]]]] = ..., kineses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleKinesisArgs, TopicRuleKinesisArgsDict]]]]] = ..., lambdas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleLambdaArgs, TopicRuleLambdaArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., republishes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleRepublishArgs, TopicRuleRepublishArgsDict]]]]] = ..., s3: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleS3Args, TopicRuleS3ArgsDict]]]]] = ..., sns: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleSnsArgs, TopicRuleSnsArgsDict]]]]] = ..., sql: Optional[pulumi.Input[_builtins.str]] = ..., sql_version: Optional[pulumi.Input[_builtins.str]] = ..., sqs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleSqsArgs, TopicRuleSqsArgsDict]]]]] = ..., step_functions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleStepFunctionArgs, TopicRuleStepFunctionArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timestreams: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopicRuleTimestreamArgs, TopicRuleTimestreamArgsDict]]]]] = ...) -> TopicRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarms")
    def cloudwatch_alarms(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleCloudwatchAlarm]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleCloudwatchLog]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchMetrics")
    def cloudwatch_metrics(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleCloudwatchMetric]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynamodbs(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleDynamodb]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynamodbv2s(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleDynamodbv2]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def elasticsearch(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleElasticsearch]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorAction")
    def error_action(self) -> pulumi.Output[Optional[outputs.TopicRuleErrorAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def firehoses(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleFirehose]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def https(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleHttp]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotAnalytics")
    def iot_analytics(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleIotAnalytic]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotEvents")
    def iot_events(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleIotEvent]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kafkas(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleKafka]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kineses(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleKinesis]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lambdas(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleLambda]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def republishes(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleRepublish]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleS3]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sns(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleSns]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sql(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVersion")
    def sql_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sqs(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleSqs]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepFunctions")
    def step_functions(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleStepFunction]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestreams(self) -> pulumi.Output[Optional[Sequence[outputs.TopicRuleTimestream]]]:
        ...
    


