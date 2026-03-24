

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BasicAuthenticationArgs', 'BasicAuthenticationArgsDict', 'ClientCertAuthenticationArgs', 'ClientCertAuthenticationArgsDict', 'HttpRequestArgs', 'HttpRequestArgsDict', 'JobActionArgs', 'JobActionArgsDict', 'JobCollectionPropertiesArgs', 'JobCollectionPropertiesArgsDict', 'JobCollectionQuotaArgs', 'JobCollectionQuotaArgsDict', 'JobErrorActionArgs', 'JobErrorActionArgsDict', 'JobMaxRecurrenceArgs', 'JobMaxRecurrenceArgsDict', 'JobPropertiesArgs', 'JobPropertiesArgsDict', 'JobRecurrenceScheduleMonthlyOccurrenceArgs', 'JobRecurrenceScheduleMonthlyOccurrenceArgsDict', 'JobRecurrenceScheduleArgs', 'JobRecurrenceScheduleArgsDict', 'JobRecurrenceArgs', 'JobRecurrenceArgsDict', 'OAuthAuthenticationArgs', 'OAuthAuthenticationArgsDict', 'RetryPolicyArgs', 'RetryPolicyArgsDict', 'ServiceBusAuthenticationArgs', 'ServiceBusAuthenticationArgsDict', 'ServiceBusBrokeredMessagePropertiesArgs', 'ServiceBusBrokeredMessagePropertiesArgsDict', 'ServiceBusQueueMessageArgs', 'ServiceBusQueueMessageArgsDict', 'ServiceBusTopicMessageArgs', 'ServiceBusTopicMessageArgsDict', 'SkuArgs', 'SkuArgsDict', 'StorageQueueMessageArgs', 'StorageQueueMessageArgsDict']
class BasicAuthenticationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BasicAuthenticationArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], password: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClientCertAuthenticationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    certificate_expiration_date: NotRequired[pulumi.Input[_builtins.str]]
    certificate_subject_name: NotRequired[pulumi.Input[_builtins.str]]
    certificate_thumbprint: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    pfx: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClientCertAuthenticationArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], certificate_expiration_date: Optional[pulumi.Input[_builtins.str]] = ..., certificate_subject_name: Optional[pulumi.Input[_builtins.str]] = ..., certificate_thumbprint: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., pfx: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateExpirationDate")
    def certificate_expiration_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_expiration_date.setter
    def certificate_expiration_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateSubjectName")
    def certificate_subject_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_subject_name.setter
    def certificate_subject_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateThumbprint")
    def certificate_thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_thumbprint.setter
    def certificate_thumbprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def pfx(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pfx.setter
    def pfx(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HttpRequestArgsDict(TypedDict):
    authentication: NotRequired[pulumi.Input[Union[BasicAuthenticationArgsDict, ClientCertAuthenticationArgsDict, OAuthAuthenticationArgsDict]]]
    body: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    method: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HttpRequestArgs:
    def __init__(__self__, *, authentication: Optional[pulumi.Input[Union[BasicAuthenticationArgs, ClientCertAuthenticationArgs, OAuthAuthenticationArgs]]] = ..., body: Optional[pulumi.Input[_builtins.str]] = ..., headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., method: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[Union[BasicAuthenticationArgs, ClientCertAuthenticationArgs, OAuthAuthenticationArgs]]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[Union[BasicAuthenticationArgs, ClientCertAuthenticationArgs, OAuthAuthenticationArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobActionArgsDict(TypedDict):
    error_action: NotRequired[pulumi.Input[JobErrorActionArgsDict]]
    queue_message: NotRequired[pulumi.Input[StorageQueueMessageArgsDict]]
    request: NotRequired[pulumi.Input[HttpRequestArgsDict]]
    retry_policy: NotRequired[pulumi.Input[RetryPolicyArgsDict]]
    service_bus_queue_message: NotRequired[pulumi.Input[ServiceBusQueueMessageArgsDict]]
    service_bus_topic_message: NotRequired[pulumi.Input[ServiceBusTopicMessageArgsDict]]
    type: NotRequired[pulumi.Input[JobActionType]]


@pulumi.input_type
class JobActionArgs:
    def __init__(__self__, *, error_action: Optional[pulumi.Input[JobErrorActionArgs]] = ..., queue_message: Optional[pulumi.Input[StorageQueueMessageArgs]] = ..., request: Optional[pulumi.Input[HttpRequestArgs]] = ..., retry_policy: Optional[pulumi.Input[RetryPolicyArgs]] = ..., service_bus_queue_message: Optional[pulumi.Input[ServiceBusQueueMessageArgs]] = ..., service_bus_topic_message: Optional[pulumi.Input[ServiceBusTopicMessageArgs]] = ..., type: Optional[pulumi.Input[JobActionType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorAction")
    def error_action(self) -> Optional[pulumi.Input[JobErrorActionArgs]]:
        
        ...
    
    @error_action.setter
    def error_action(self, value: Optional[pulumi.Input[JobErrorActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueMessage")
    def queue_message(self) -> Optional[pulumi.Input[StorageQueueMessageArgs]]:
        
        ...
    
    @queue_message.setter
    def queue_message(self, value: Optional[pulumi.Input[StorageQueueMessageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[pulumi.Input[HttpRequestArgs]]:
        
        ...
    
    @request.setter
    def request(self, value: Optional[pulumi.Input[HttpRequestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[RetryPolicyArgs]]:
        
        ...
    
    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input[RetryPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusQueueMessage")
    def service_bus_queue_message(self) -> Optional[pulumi.Input[ServiceBusQueueMessageArgs]]:
        
        ...
    
    @service_bus_queue_message.setter
    def service_bus_queue_message(self, value: Optional[pulumi.Input[ServiceBusQueueMessageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusTopicMessage")
    def service_bus_topic_message(self) -> Optional[pulumi.Input[ServiceBusTopicMessageArgs]]:
        
        ...
    
    @service_bus_topic_message.setter
    def service_bus_topic_message(self, value: Optional[pulumi.Input[ServiceBusTopicMessageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[JobActionType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[JobActionType]]): # -> None:
        ...
    


class JobCollectionPropertiesArgsDict(TypedDict):
    quota: NotRequired[pulumi.Input[JobCollectionQuotaArgsDict]]
    sku: NotRequired[pulumi.Input[SkuArgsDict]]
    state: NotRequired[pulumi.Input[JobCollectionState]]


@pulumi.input_type
class JobCollectionPropertiesArgs:
    def __init__(__self__, *, quota: Optional[pulumi.Input[JobCollectionQuotaArgs]] = ..., sku: Optional[pulumi.Input[SkuArgs]] = ..., state: Optional[pulumi.Input[JobCollectionState]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[JobCollectionQuotaArgs]]:
        
        ...
    
    @quota.setter
    def quota(self, value: Optional[pulumi.Input[JobCollectionQuotaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[JobCollectionState]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[JobCollectionState]]): # -> None:
        ...
    


class JobCollectionQuotaArgsDict(TypedDict):
    max_job_count: NotRequired[pulumi.Input[_builtins.int]]
    max_job_occurrence: NotRequired[pulumi.Input[_builtins.int]]
    max_recurrence: NotRequired[pulumi.Input[JobMaxRecurrenceArgsDict]]


@pulumi.input_type
class JobCollectionQuotaArgs:
    def __init__(__self__, *, max_job_count: Optional[pulumi.Input[_builtins.int]] = ..., max_job_occurrence: Optional[pulumi.Input[_builtins.int]] = ..., max_recurrence: Optional[pulumi.Input[JobMaxRecurrenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxJobCount")
    def max_job_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_job_count.setter
    def max_job_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxJobOccurrence")
    def max_job_occurrence(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_job_occurrence.setter
    def max_job_occurrence(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRecurrence")
    def max_recurrence(self) -> Optional[pulumi.Input[JobMaxRecurrenceArgs]]:
        
        ...
    
    @max_recurrence.setter
    def max_recurrence(self, value: Optional[pulumi.Input[JobMaxRecurrenceArgs]]): # -> None:
        ...
    


class JobErrorActionArgsDict(TypedDict):
    queue_message: NotRequired[pulumi.Input[StorageQueueMessageArgsDict]]
    request: NotRequired[pulumi.Input[HttpRequestArgsDict]]
    retry_policy: NotRequired[pulumi.Input[RetryPolicyArgsDict]]
    service_bus_queue_message: NotRequired[pulumi.Input[ServiceBusQueueMessageArgsDict]]
    service_bus_topic_message: NotRequired[pulumi.Input[ServiceBusTopicMessageArgsDict]]
    type: NotRequired[pulumi.Input[JobActionType]]


@pulumi.input_type
class JobErrorActionArgs:
    def __init__(__self__, *, queue_message: Optional[pulumi.Input[StorageQueueMessageArgs]] = ..., request: Optional[pulumi.Input[HttpRequestArgs]] = ..., retry_policy: Optional[pulumi.Input[RetryPolicyArgs]] = ..., service_bus_queue_message: Optional[pulumi.Input[ServiceBusQueueMessageArgs]] = ..., service_bus_topic_message: Optional[pulumi.Input[ServiceBusTopicMessageArgs]] = ..., type: Optional[pulumi.Input[JobActionType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueMessage")
    def queue_message(self) -> Optional[pulumi.Input[StorageQueueMessageArgs]]:
        
        ...
    
    @queue_message.setter
    def queue_message(self, value: Optional[pulumi.Input[StorageQueueMessageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[pulumi.Input[HttpRequestArgs]]:
        
        ...
    
    @request.setter
    def request(self, value: Optional[pulumi.Input[HttpRequestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[RetryPolicyArgs]]:
        
        ...
    
    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input[RetryPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusQueueMessage")
    def service_bus_queue_message(self) -> Optional[pulumi.Input[ServiceBusQueueMessageArgs]]:
        
        ...
    
    @service_bus_queue_message.setter
    def service_bus_queue_message(self, value: Optional[pulumi.Input[ServiceBusQueueMessageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusTopicMessage")
    def service_bus_topic_message(self) -> Optional[pulumi.Input[ServiceBusTopicMessageArgs]]:
        
        ...
    
    @service_bus_topic_message.setter
    def service_bus_topic_message(self, value: Optional[pulumi.Input[ServiceBusTopicMessageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[JobActionType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[JobActionType]]): # -> None:
        ...
    


class JobMaxRecurrenceArgsDict(TypedDict):
    frequency: NotRequired[pulumi.Input[RecurrenceFrequency]]
    interval: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobMaxRecurrenceArgs:
    def __init__(__self__, *, frequency: Optional[pulumi.Input[RecurrenceFrequency]] = ..., interval: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[RecurrenceFrequency]]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[RecurrenceFrequency]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobPropertiesArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[JobActionArgsDict]]
    recurrence: NotRequired[pulumi.Input[JobRecurrenceArgsDict]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[JobState]]


@pulumi.input_type
class JobPropertiesArgs:
    def __init__(__self__, *, action: Optional[pulumi.Input[JobActionArgs]] = ..., recurrence: Optional[pulumi.Input[JobRecurrenceArgs]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[JobState]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[JobActionArgs]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[JobActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input[JobRecurrenceArgs]]:
        
        ...
    
    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input[JobRecurrenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[JobState]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[JobState]]): # -> None:
        ...
    


class JobRecurrenceScheduleMonthlyOccurrenceArgsDict(TypedDict):
    day: NotRequired[pulumi.Input[JobScheduleDay]]
    occurrence: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobRecurrenceScheduleMonthlyOccurrenceArgs:
    def __init__(__self__, *, day: Optional[pulumi.Input[JobScheduleDay]] = ..., occurrence: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[JobScheduleDay]]:
        
        ...
    
    @day.setter
    def day(self, value: Optional[pulumi.Input[JobScheduleDay]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def occurrence(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @occurrence.setter
    def occurrence(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobRecurrenceScheduleArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    minutes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    month_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    monthly_occurrences: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobRecurrenceScheduleMonthlyOccurrenceArgsDict]]]]
    week_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]


@pulumi.input_type
class JobRecurrenceScheduleArgs:
    def __init__(__self__, *, hours: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., minutes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., month_days: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., monthly_occurrences: Optional[pulumi.Input[Sequence[pulumi.Input[JobRecurrenceScheduleMonthlyOccurrenceArgs]]]] = ..., week_days: Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthDays")
    def month_days(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @month_days.setter
    def month_days(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyOccurrences")
    def monthly_occurrences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobRecurrenceScheduleMonthlyOccurrenceArgs]]]]:
        
        ...
    
    @monthly_occurrences.setter
    def monthly_occurrences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobRecurrenceScheduleMonthlyOccurrenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDays")
    def week_days(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]:
        
        ...
    
    @week_days.setter
    def week_days(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]): # -> None:
        ...
    


class JobRecurrenceArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    frequency: NotRequired[pulumi.Input[RecurrenceFrequency]]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    schedule: NotRequired[pulumi.Input[JobRecurrenceScheduleArgsDict]]


@pulumi.input_type
class JobRecurrenceArgs:
    def __init__(__self__, *, count: Optional[pulumi.Input[_builtins.int]] = ..., end_time: Optional[pulumi.Input[_builtins.str]] = ..., frequency: Optional[pulumi.Input[RecurrenceFrequency]] = ..., interval: Optional[pulumi.Input[_builtins.int]] = ..., schedule: Optional[pulumi.Input[JobRecurrenceScheduleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[RecurrenceFrequency]]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[RecurrenceFrequency]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[JobRecurrenceScheduleArgs]]:
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[JobRecurrenceScheduleArgs]]): # -> None:
        ...
    


class OAuthAuthenticationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    audience: NotRequired[pulumi.Input[_builtins.str]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    secret: NotRequired[pulumi.Input[_builtins.str]]
    tenant: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OAuthAuthenticationArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], audience: Optional[pulumi.Input[_builtins.str]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., secret: Optional[pulumi.Input[_builtins.str]] = ..., tenant: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret.setter
    def secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenant(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant.setter
    def tenant(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RetryPolicyArgsDict(TypedDict):
    retry_count: NotRequired[pulumi.Input[_builtins.int]]
    retry_interval: NotRequired[pulumi.Input[_builtins.str]]
    retry_type: NotRequired[pulumi.Input[RetryType]]


@pulumi.input_type
class RetryPolicyArgs:
    def __init__(__self__, *, retry_count: Optional[pulumi.Input[_builtins.int]] = ..., retry_interval: Optional[pulumi.Input[_builtins.str]] = ..., retry_type: Optional[pulumi.Input[RetryType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_count.setter
    def retry_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryInterval")
    def retry_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @retry_interval.setter
    def retry_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryType")
    def retry_type(self) -> Optional[pulumi.Input[RetryType]]:
        
        ...
    
    @retry_type.setter
    def retry_type(self, value: Optional[pulumi.Input[RetryType]]): # -> None:
        ...
    


class ServiceBusAuthenticationArgsDict(TypedDict):
    sas_key: NotRequired[pulumi.Input[_builtins.str]]
    sas_key_name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[ServiceBusAuthenticationType]]


@pulumi.input_type
class ServiceBusAuthenticationArgs:
    def __init__(__self__, *, sas_key: Optional[pulumi.Input[_builtins.str]] = ..., sas_key_name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[ServiceBusAuthenticationType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasKey")
    def sas_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sas_key.setter
    def sas_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasKeyName")
    def sas_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sas_key_name.setter
    def sas_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ServiceBusAuthenticationType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[ServiceBusAuthenticationType]]): # -> None:
        ...
    


class ServiceBusBrokeredMessagePropertiesArgsDict(TypedDict):
    content_type: NotRequired[pulumi.Input[_builtins.str]]
    correlation_id: NotRequired[pulumi.Input[_builtins.str]]
    force_persistence: NotRequired[pulumi.Input[_builtins.bool]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    message_id: NotRequired[pulumi.Input[_builtins.str]]
    partition_key: NotRequired[pulumi.Input[_builtins.str]]
    reply_to: NotRequired[pulumi.Input[_builtins.str]]
    reply_to_session_id: NotRequired[pulumi.Input[_builtins.str]]
    scheduled_enqueue_time_utc: NotRequired[pulumi.Input[_builtins.str]]
    session_id: NotRequired[pulumi.Input[_builtins.str]]
    time_to_live: NotRequired[pulumi.Input[_builtins.str]]
    to: NotRequired[pulumi.Input[_builtins.str]]
    via_partition_key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceBusBrokeredMessagePropertiesArgs:
    def __init__(__self__, *, content_type: Optional[pulumi.Input[_builtins.str]] = ..., correlation_id: Optional[pulumi.Input[_builtins.str]] = ..., force_persistence: Optional[pulumi.Input[_builtins.bool]] = ..., label: Optional[pulumi.Input[_builtins.str]] = ..., message_id: Optional[pulumi.Input[_builtins.str]] = ..., partition_key: Optional[pulumi.Input[_builtins.str]] = ..., reply_to: Optional[pulumi.Input[_builtins.str]] = ..., reply_to_session_id: Optional[pulumi.Input[_builtins.str]] = ..., scheduled_enqueue_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., session_id: Optional[pulumi.Input[_builtins.str]] = ..., time_to_live: Optional[pulumi.Input[_builtins.str]] = ..., to: Optional[pulumi.Input[_builtins.str]] = ..., via_partition_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @correlation_id.setter
    def correlation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forcePersistence")
    def force_persistence(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_persistence.setter
    def force_persistence(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @partition_key.setter
    def partition_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replyTo")
    def reply_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reply_to.setter
    def reply_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replyToSessionId")
    def reply_to_session_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reply_to_session_id.setter
    def reply_to_session_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEnqueueTimeUtc")
    def scheduled_enqueue_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scheduled_enqueue_time_utc.setter
    def scheduled_enqueue_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionId")
    def session_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_id.setter
    def session_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToLive")
    def time_to_live(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_to_live.setter
    def time_to_live(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viaPartitionKey")
    def via_partition_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @via_partition_key.setter
    def via_partition_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceBusQueueMessageArgsDict(TypedDict):
    authentication: NotRequired[pulumi.Input[ServiceBusAuthenticationArgsDict]]
    brokered_message_properties: NotRequired[pulumi.Input[ServiceBusBrokeredMessagePropertiesArgsDict]]
    custom_message_properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    queue_name: NotRequired[pulumi.Input[_builtins.str]]
    transport_type: NotRequired[pulumi.Input[ServiceBusTransportType]]


@pulumi.input_type
class ServiceBusQueueMessageArgs:
    def __init__(__self__, *, authentication: Optional[pulumi.Input[ServiceBusAuthenticationArgs]] = ..., brokered_message_properties: Optional[pulumi.Input[ServiceBusBrokeredMessagePropertiesArgs]] = ..., custom_message_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., queue_name: Optional[pulumi.Input[_builtins.str]] = ..., transport_type: Optional[pulumi.Input[ServiceBusTransportType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[ServiceBusAuthenticationArgs]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[ServiceBusAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokeredMessageProperties")
    def brokered_message_properties(self) -> Optional[pulumi.Input[ServiceBusBrokeredMessagePropertiesArgs]]:
        
        ...
    
    @brokered_message_properties.setter
    def brokered_message_properties(self, value: Optional[pulumi.Input[ServiceBusBrokeredMessagePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMessageProperties")
    def custom_message_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @custom_message_properties.setter
    def custom_message_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queue_name.setter
    def queue_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transportType")
    def transport_type(self) -> Optional[pulumi.Input[ServiceBusTransportType]]:
        
        ...
    
    @transport_type.setter
    def transport_type(self, value: Optional[pulumi.Input[ServiceBusTransportType]]): # -> None:
        ...
    


class ServiceBusTopicMessageArgsDict(TypedDict):
    authentication: NotRequired[pulumi.Input[ServiceBusAuthenticationArgsDict]]
    brokered_message_properties: NotRequired[pulumi.Input[ServiceBusBrokeredMessagePropertiesArgsDict]]
    custom_message_properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    topic_path: NotRequired[pulumi.Input[_builtins.str]]
    transport_type: NotRequired[pulumi.Input[ServiceBusTransportType]]


@pulumi.input_type
class ServiceBusTopicMessageArgs:
    def __init__(__self__, *, authentication: Optional[pulumi.Input[ServiceBusAuthenticationArgs]] = ..., brokered_message_properties: Optional[pulumi.Input[ServiceBusBrokeredMessagePropertiesArgs]] = ..., custom_message_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., topic_path: Optional[pulumi.Input[_builtins.str]] = ..., transport_type: Optional[pulumi.Input[ServiceBusTransportType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[ServiceBusAuthenticationArgs]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[ServiceBusAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokeredMessageProperties")
    def brokered_message_properties(self) -> Optional[pulumi.Input[ServiceBusBrokeredMessagePropertiesArgs]]:
        
        ...
    
    @brokered_message_properties.setter
    def brokered_message_properties(self, value: Optional[pulumi.Input[ServiceBusBrokeredMessagePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMessageProperties")
    def custom_message_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @custom_message_properties.setter
    def custom_message_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicPath")
    def topic_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic_path.setter
    def topic_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transportType")
    def transport_type(self) -> Optional[pulumi.Input[ServiceBusTransportType]]:
        
        ...
    
    @transport_type.setter
    def transport_type(self, value: Optional[pulumi.Input[ServiceBusTransportType]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[SkuDefinition]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[SkuDefinition]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[SkuDefinition]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[SkuDefinition]]): # -> None:
        ...
    


class StorageQueueMessageArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]
    queue_name: NotRequired[pulumi.Input[_builtins.str]]
    sas_token: NotRequired[pulumi.Input[_builtins.str]]
    storage_account: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StorageQueueMessageArgs:
    def __init__(__self__, *, message: Optional[pulumi.Input[_builtins.str]] = ..., queue_name: Optional[pulumi.Input[_builtins.str]] = ..., sas_token: Optional[pulumi.Input[_builtins.str]] = ..., storage_account: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queue_name.setter
    def queue_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sas_token.setter
    def sas_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account.setter
    def storage_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


