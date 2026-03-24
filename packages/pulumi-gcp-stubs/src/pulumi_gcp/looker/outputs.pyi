

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceAdminSettings', 'InstanceControlledEgressConfig', 'InstanceCustomDomain', 'InstanceDenyMaintenancePeriod', 'InstanceDenyMaintenancePeriodEndDate', 'InstanceDenyMaintenancePeriodStartDate', 'InstanceDenyMaintenancePeriodTime', 'InstanceEncryptionConfig', 'InstanceMaintenanceWindow', 'InstanceMaintenanceWindowStartTime', 'InstanceOauthConfig', 'InstancePeriodicExportConfig', 'InstancePeriodicExportConfigStartTime', 'InstancePscConfig', 'InstancePscConfigServiceAttachment', 'InstanceUserMetadata']
@pulumi.output_type
class InstanceAdminSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_email_domains: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedEmailDomains")
    def allowed_email_domains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class InstanceControlledEgressConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, egress_fqdns: Optional[Sequence[_builtins.str]] = ..., marketplace_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressFqdns")
    def egress_fqdns(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceEnabled")
    def marketplace_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InstanceCustomDomain(dict):
    def __init__(__self__, *, domain: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceDenyMaintenancePeriod(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_date: outputs.InstanceDenyMaintenancePeriodEndDate, start_date: outputs.InstanceDenyMaintenancePeriodStartDate, time: outputs.InstanceDenyMaintenancePeriodTime) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> outputs.InstanceDenyMaintenancePeriodEndDate:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> outputs.InstanceDenyMaintenancePeriodStartDate:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> outputs.InstanceDenyMaintenancePeriodTime:
        
        ...
    


@pulumi.output_type
class InstanceDenyMaintenancePeriodEndDate(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstanceDenyMaintenancePeriodStartDate(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstanceDenyMaintenancePeriodTime(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstanceEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ..., kms_key_name_version: Optional[_builtins.str] = ..., kms_key_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyNameVersion")
    def kms_key_name_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyState")
    def kms_key_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, day_of_week: _builtins.str, start_time: outputs.InstanceMaintenanceWindowStartTime) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> outputs.InstanceMaintenanceWindowStartTime:
        
        ...
    


@pulumi.output_type
class InstanceMaintenanceWindowStartTime(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstanceOauthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, client_secret: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstancePeriodicExportConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gcs_uri: _builtins.str, kms_key: _builtins.str, start_time: outputs.InstancePeriodicExportConfigStartTime) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsUri")
    def gcs_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> outputs.InstancePeriodicExportConfigStartTime:
        
        ...
    


@pulumi.output_type
class InstancePeriodicExportConfigStartTime(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstancePscConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_vpcs: Optional[Sequence[_builtins.str]] = ..., looker_service_attachment_uri: Optional[_builtins.str] = ..., service_attachments: Optional[Sequence[outputs.InstancePscConfigServiceAttachment]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedVpcs")
    def allowed_vpcs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookerServiceAttachmentUri")
    def looker_service_attachment_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachments")
    def service_attachments(self) -> Optional[Sequence[outputs.InstancePscConfigServiceAttachment]]:
        
        ...
    


@pulumi.output_type
class InstancePscConfigServiceAttachment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_status: Optional[_builtins.str] = ..., local_fqdn: Optional[_builtins.str] = ..., target_service_attachment_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localFqdn")
    def local_fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAttachmentUri")
    def target_service_attachment_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceUserMetadata(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_developer_user_count: Optional[_builtins.int] = ..., additional_standard_user_count: Optional[_builtins.int] = ..., additional_viewer_user_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDeveloperUserCount")
    def additional_developer_user_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalStandardUserCount")
    def additional_standard_user_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalViewerUserCount")
    def additional_viewer_user_count(self) -> Optional[_builtins.int]:
        
        ...
    


