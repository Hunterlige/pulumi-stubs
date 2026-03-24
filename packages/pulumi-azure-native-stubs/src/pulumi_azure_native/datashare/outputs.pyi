

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IdentityResponse', 'ScheduledSourceSynchronizationSettingResponse', 'ShareSubscriptionSynchronizationResponse', 'ShareSynchronizationResponse', 'SynchronizationDetailsResponse', 'SystemDataResponse', 'TableLevelSharingPropertiesResponse']
@pulumi.output_type
class IdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScheduledSourceSynchronizationSettingResponse(dict):
    
    def __init__(__self__, *, kind: _builtins.str, recurrence_interval: Optional[_builtins.str] = ..., synchronization_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurrenceInterval")
    def recurrence_interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationTime")
    def synchronization_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ShareSubscriptionSynchronizationResponse(dict):
    
    def __init__(__self__, *, duration_ms: _builtins.int, end_time: _builtins.str, message: _builtins.str, start_time: _builtins.str, status: _builtins.str, synchronization_id: _builtins.str, synchronization_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationMs")
    def duration_ms(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationId")
    def synchronization_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationMode")
    def synchronization_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ShareSynchronizationResponse(dict):
    
    def __init__(__self__, *, synchronization_mode: _builtins.str, consumer_email: Optional[_builtins.str] = ..., consumer_name: Optional[_builtins.str] = ..., consumer_tenant_name: Optional[_builtins.str] = ..., duration_ms: Optional[_builtins.int] = ..., end_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., synchronization_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationMode")
    def synchronization_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerEmail")
    def consumer_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerName")
    def consumer_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerTenantName")
    def consumer_tenant_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationMs")
    def duration_ms(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationId")
    def synchronization_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SynchronizationDetailsResponse(dict):
    
    def __init__(__self__, *, data_set_id: _builtins.str, data_set_type: _builtins.str, duration_ms: _builtins.int, end_time: _builtins.str, files_read: _builtins.float, files_written: _builtins.float, message: _builtins.str, name: _builtins.str, rows_copied: _builtins.float, rows_read: _builtins.float, size_read: _builtins.float, size_written: _builtins.float, start_time: _builtins.str, status: _builtins.str, v_core: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetType")
    def data_set_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationMs")
    def duration_ms(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filesRead")
    def files_read(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filesWritten")
    def files_written(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowsCopied")
    def rows_copied(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowsRead")
    def rows_read(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeRead")
    def size_read(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeWritten")
    def size_written(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCore")
    def v_core(self) -> _builtins.float:
        
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
    


@pulumi.output_type
class TableLevelSharingPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_tables_to_exclude: Optional[Sequence[_builtins.str]] = ..., external_tables_to_include: Optional[Sequence[_builtins.str]] = ..., materialized_views_to_exclude: Optional[Sequence[_builtins.str]] = ..., materialized_views_to_include: Optional[Sequence[_builtins.str]] = ..., tables_to_exclude: Optional[Sequence[_builtins.str]] = ..., tables_to_include: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalTablesToExclude")
    def external_tables_to_exclude(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalTablesToInclude")
    def external_tables_to_include(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="materializedViewsToExclude")
    def materialized_views_to_exclude(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="materializedViewsToInclude")
    def materialized_views_to_include(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablesToExclude")
    def tables_to_exclude(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablesToInclude")
    def tables_to_include(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


