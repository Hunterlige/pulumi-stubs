

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BasicAuthenticationResponse', 'ClientCertAuthenticationResponse', 'HttpRequestResponse', 'JobActionResponse', 'JobCollectionPropertiesResponse', 'JobCollectionQuotaResponse', 'JobErrorActionResponse', 'JobMaxRecurrenceResponse', 'JobPropertiesResponse', 'JobRecurrenceResponse', 'JobRecurrenceScheduleMonthlyOccurrenceResponse', 'JobRecurrenceScheduleResponse', 'JobStatusResponse', 'OAuthAuthenticationResponse', 'RetryPolicyResponse', 'ServiceBusAuthenticationResponse', 'ServiceBusBrokeredMessagePropertiesResponse', 'ServiceBusQueueMessageResponse', 'ServiceBusTopicMessageResponse', 'SkuResponse', 'StorageQueueMessageResponse']
@pulumi.output_type
class BasicAuthenticationResponse(dict):
    def __init__(__self__, *, type: _builtins.str, password: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClientCertAuthenticationResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, certificate_expiration_date: Optional[_builtins.str] = ..., certificate_subject_name: Optional[_builtins.str] = ..., certificate_thumbprint: Optional[_builtins.str] = ..., password: Optional[_builtins.str] = ..., pfx: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateExpirationDate")
    def certificate_expiration_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateSubjectName")
    def certificate_subject_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateThumbprint")
    def certificate_thumbprint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pfx(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HttpRequestResponse(dict):
    def __init__(__self__, *, authentication: Optional[Any] = ..., body: Optional[_builtins.str] = ..., headers: Optional[Mapping[str, _builtins.str]] = ..., method: Optional[_builtins.str] = ..., uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobActionResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_action: Optional[outputs.JobErrorActionResponse] = ..., queue_message: Optional[outputs.StorageQueueMessageResponse] = ..., request: Optional[outputs.HttpRequestResponse] = ..., retry_policy: Optional[outputs.RetryPolicyResponse] = ..., service_bus_queue_message: Optional[outputs.ServiceBusQueueMessageResponse] = ..., service_bus_topic_message: Optional[outputs.ServiceBusTopicMessageResponse] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorAction")
    def error_action(self) -> Optional[outputs.JobErrorActionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueMessage")
    def queue_message(self) -> Optional[outputs.StorageQueueMessageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[outputs.HttpRequestResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.RetryPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusQueueMessage")
    def service_bus_queue_message(self) -> Optional[outputs.ServiceBusQueueMessageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusTopicMessage")
    def service_bus_topic_message(self) -> Optional[outputs.ServiceBusTopicMessageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobCollectionPropertiesResponse(dict):
    def __init__(__self__, *, quota: Optional[outputs.JobCollectionQuotaResponse] = ..., sku: Optional[outputs.SkuResponse] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[outputs.JobCollectionQuotaResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobCollectionQuotaResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_job_count: Optional[_builtins.int] = ..., max_job_occurrence: Optional[_builtins.int] = ..., max_recurrence: Optional[outputs.JobMaxRecurrenceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxJobCount")
    def max_job_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxJobOccurrence")
    def max_job_occurrence(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRecurrence")
    def max_recurrence(self) -> Optional[outputs.JobMaxRecurrenceResponse]:
        
        ...
    


@pulumi.output_type
class JobErrorActionResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, queue_message: Optional[outputs.StorageQueueMessageResponse] = ..., request: Optional[outputs.HttpRequestResponse] = ..., retry_policy: Optional[outputs.RetryPolicyResponse] = ..., service_bus_queue_message: Optional[outputs.ServiceBusQueueMessageResponse] = ..., service_bus_topic_message: Optional[outputs.ServiceBusTopicMessageResponse] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueMessage")
    def queue_message(self) -> Optional[outputs.StorageQueueMessageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[outputs.HttpRequestResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.RetryPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusQueueMessage")
    def service_bus_queue_message(self) -> Optional[outputs.ServiceBusQueueMessageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusTopicMessage")
    def service_bus_topic_message(self) -> Optional[outputs.ServiceBusTopicMessageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobMaxRecurrenceResponse(dict):
    def __init__(__self__, *, frequency: Optional[_builtins.str] = ..., interval: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class JobPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, status: outputs.JobStatusResponse, action: Optional[outputs.JobActionResponse] = ..., recurrence: Optional[outputs.JobRecurrenceResponse] = ..., start_time: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.JobStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[outputs.JobActionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[outputs.JobRecurrenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobRecurrenceResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count: Optional[_builtins.int] = ..., end_time: Optional[_builtins.str] = ..., frequency: Optional[_builtins.str] = ..., interval: Optional[_builtins.int] = ..., schedule: Optional[outputs.JobRecurrenceScheduleResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[outputs.JobRecurrenceScheduleResponse]:
        ...
    


@pulumi.output_type
class JobRecurrenceScheduleMonthlyOccurrenceResponse(dict):
    def __init__(__self__, *, day: Optional[_builtins.str] = ..., occurrence: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def occurrence(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class JobRecurrenceScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hours: Optional[Sequence[_builtins.int]] = ..., minutes: Optional[Sequence[_builtins.int]] = ..., month_days: Optional[Sequence[_builtins.int]] = ..., monthly_occurrences: Optional[Sequence[outputs.JobRecurrenceScheduleMonthlyOccurrenceResponse]] = ..., week_days: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthDays")
    def month_days(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyOccurrences")
    def monthly_occurrences(self) -> Optional[Sequence[outputs.JobRecurrenceScheduleMonthlyOccurrenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDays")
    def week_days(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobStatusResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_count: _builtins.int, failure_count: _builtins.int, faulted_count: _builtins.int, last_execution_time: _builtins.str, next_execution_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionCount")
    def execution_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureCount")
    def failure_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="faultedCount")
    def faulted_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecutionTime")
    def last_execution_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextExecutionTime")
    def next_execution_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class OAuthAuthenticationResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, audience: Optional[_builtins.str] = ..., client_id: Optional[_builtins.str] = ..., secret: Optional[_builtins.str] = ..., tenant: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenant(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RetryPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retry_count: Optional[_builtins.int] = ..., retry_interval: Optional[_builtins.str] = ..., retry_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryInterval")
    def retry_interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryType")
    def retry_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceBusAuthenticationResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, sas_key: Optional[_builtins.str] = ..., sas_key_name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasKey")
    def sas_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasKeyName")
    def sas_key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceBusBrokeredMessagePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content_type: Optional[_builtins.str] = ..., correlation_id: Optional[_builtins.str] = ..., force_persistence: Optional[_builtins.bool] = ..., label: Optional[_builtins.str] = ..., message_id: Optional[_builtins.str] = ..., partition_key: Optional[_builtins.str] = ..., reply_to: Optional[_builtins.str] = ..., reply_to_session_id: Optional[_builtins.str] = ..., scheduled_enqueue_time_utc: Optional[_builtins.str] = ..., session_id: Optional[_builtins.str] = ..., time_to_live: Optional[_builtins.str] = ..., to: Optional[_builtins.str] = ..., via_partition_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forcePersistence")
    def force_persistence(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replyTo")
    def reply_to(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replyToSessionId")
    def reply_to_session_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEnqueueTimeUtc")
    def scheduled_enqueue_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionId")
    def session_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToLive")
    def time_to_live(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viaPartitionKey")
    def via_partition_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceBusQueueMessageResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication: Optional[outputs.ServiceBusAuthenticationResponse] = ..., brokered_message_properties: Optional[outputs.ServiceBusBrokeredMessagePropertiesResponse] = ..., custom_message_properties: Optional[Mapping[str, _builtins.str]] = ..., message: Optional[_builtins.str] = ..., namespace: Optional[_builtins.str] = ..., queue_name: Optional[_builtins.str] = ..., transport_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[outputs.ServiceBusAuthenticationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokeredMessageProperties")
    def brokered_message_properties(self) -> Optional[outputs.ServiceBusBrokeredMessagePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMessageProperties")
    def custom_message_properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transportType")
    def transport_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceBusTopicMessageResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication: Optional[outputs.ServiceBusAuthenticationResponse] = ..., brokered_message_properties: Optional[outputs.ServiceBusBrokeredMessagePropertiesResponse] = ..., custom_message_properties: Optional[Mapping[str, _builtins.str]] = ..., message: Optional[_builtins.str] = ..., namespace: Optional[_builtins.str] = ..., topic_path: Optional[_builtins.str] = ..., transport_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[outputs.ServiceBusAuthenticationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokeredMessageProperties")
    def brokered_message_properties(self) -> Optional[outputs.ServiceBusBrokeredMessagePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMessageProperties")
    def custom_message_properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicPath")
    def topic_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transportType")
    def transport_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StorageQueueMessageResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, message: Optional[_builtins.str] = ..., queue_name: Optional[_builtins.str] = ..., sas_token: Optional[_builtins.str] = ..., storage_account: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[_builtins.str]:
        
        ...
    


