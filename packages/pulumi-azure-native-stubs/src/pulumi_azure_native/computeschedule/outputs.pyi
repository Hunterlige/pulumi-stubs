

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExecutionParametersResponse', 'NotificationPropertiesResponse', 'RetryPolicyResponse', 'ScheduledActionPropertiesResponse', 'ScheduledActionsScheduleResponse', 'SystemDataResponse']
@pulumi.output_type
class ExecutionParametersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, optimization_preference: Optional[_builtins.str] = ..., retry_policy: Optional[outputs.RetryPolicyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optimizationPreference")
    def optimization_preference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.RetryPolicyResponse]:
        
        ...
    


@pulumi.output_type
class NotificationPropertiesResponse(dict):
    
    def __init__(__self__, *, destination: _builtins.str, language: _builtins.str, type: _builtins.str, disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def language(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RetryPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retry_count: Optional[_builtins.int] = ..., retry_window_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryWindowInMinutes")
    def retry_window_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ScheduledActionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_type: _builtins.str, notification_settings: Sequence[outputs.NotificationPropertiesResponse], provisioning_state: _builtins.str, resource_type: _builtins.str, schedule: outputs.ScheduledActionsScheduleResponse, start_time: _builtins.str, disabled: Optional[_builtins.bool] = ..., end_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> Sequence[outputs.NotificationPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> outputs.ScheduledActionsScheduleResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScheduledActionsScheduleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, requested_days_of_the_month: Sequence[_builtins.int], requested_months: Sequence[_builtins.str], requested_week_days: Sequence[_builtins.str], scheduled_time: _builtins.str, time_zone: _builtins.str, deadline_type: Optional[_builtins.str] = ..., execution_parameters: Optional[outputs.ExecutionParametersResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedDaysOfTheMonth")
    def requested_days_of_the_month(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedMonths")
    def requested_months(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedWeekDays")
    def requested_week_days(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledTime")
    def scheduled_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadlineType")
    def deadline_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionParameters")
    def execution_parameters(self) -> Optional[outputs.ExecutionParametersResponse]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


