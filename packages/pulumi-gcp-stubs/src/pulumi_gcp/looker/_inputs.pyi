import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstanceAdminSettingsArgs",
    "InstanceAdminSettingsArgsDict",
    "InstanceControlledEgressConfigArgs",
    "InstanceControlledEgressConfigArgsDict",
    "InstanceCustomDomainArgs",
    "InstanceCustomDomainArgsDict",
    "InstanceDenyMaintenancePeriodArgs",
    "InstanceDenyMaintenancePeriodArgsDict",
    "InstanceDenyMaintenancePeriodEndDateArgs",
    "InstanceDenyMaintenancePeriodEndDateArgsDict",
    "InstanceDenyMaintenancePeriodStartDateArgs",
    "InstanceDenyMaintenancePeriodStartDateArgsDict",
    "InstanceDenyMaintenancePeriodTimeArgs",
    "InstanceDenyMaintenancePeriodTimeArgsDict",
    "InstanceEncryptionConfigArgs",
    "InstanceEncryptionConfigArgsDict",
    "InstanceMaintenanceWindowArgs",
    "InstanceMaintenanceWindowArgsDict",
    "InstanceMaintenanceWindowStartTimeArgs",
    "InstanceMaintenanceWindowStartTimeArgsDict",
    "InstanceOauthConfigArgs",
    "InstanceOauthConfigArgsDict",
    "InstancePeriodicExportConfigArgs",
    "InstancePeriodicExportConfigArgsDict",
    "InstancePeriodicExportConfigStartTimeArgs",
    "InstancePeriodicExportConfigStartTimeArgsDict",
    "InstancePscConfigArgs",
    "InstancePscConfigArgsDict",
    "InstancePscConfigServiceAttachmentArgs",
    "InstancePscConfigServiceAttachmentArgsDict",
    "InstanceUserMetadataArgs",
    "InstanceUserMetadataArgsDict",
]

class InstanceAdminSettingsArgsDict(TypedDict):
    allowed_email_domains: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class InstanceAdminSettingsArgs:
    def __init__(
        __self__,
        *,
        allowed_email_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedEmailDomains")
    def allowed_email_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_email_domains.setter
    def allowed_email_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class InstanceControlledEgressConfigArgsDict(TypedDict):
    egress_fqdns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    marketplace_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class InstanceControlledEgressConfigArgs:
    def __init__(
        __self__,
        *,
        egress_fqdns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        marketplace_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFqdns")
    def egress_fqdns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @egress_fqdns.setter
    def egress_fqdns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="marketplaceEnabled")
    def marketplace_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @marketplace_enabled.setter
    def marketplace_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class InstanceCustomDomainArgsDict(TypedDict):
    domain: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceCustomDomainArgs:
    def __init__(
        __self__,
        *,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceDenyMaintenancePeriodArgsDict(TypedDict):
    end_date: pulumi.Input[InstanceDenyMaintenancePeriodEndDateArgsDict]
    start_date: pulumi.Input[InstanceDenyMaintenancePeriodStartDateArgsDict]
    time: pulumi.Input[InstanceDenyMaintenancePeriodTimeArgsDict]
    ...

@pulumi.input_type
class InstanceDenyMaintenancePeriodArgs:
    def __init__(
        __self__,
        *,
        end_date: pulumi.Input[InstanceDenyMaintenancePeriodEndDateArgs],
        start_date: pulumi.Input[InstanceDenyMaintenancePeriodStartDateArgs],
        time: pulumi.Input[InstanceDenyMaintenancePeriodTimeArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Input[InstanceDenyMaintenancePeriodEndDateArgs]: ...
    @end_date.setter
    def end_date(
        self, value: pulumi.Input[InstanceDenyMaintenancePeriodEndDateArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(
        self,
    ) -> pulumi.Input[InstanceDenyMaintenancePeriodStartDateArgs]: ...
    @start_date.setter
    def start_date(
        self, value: pulumi.Input[InstanceDenyMaintenancePeriodStartDateArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> pulumi.Input[InstanceDenyMaintenancePeriodTimeArgs]: ...
    @time.setter
    def time(self, value: pulumi.Input[InstanceDenyMaintenancePeriodTimeArgs]): ...

class InstanceDenyMaintenancePeriodEndDateArgsDict(TypedDict):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceDenyMaintenancePeriodEndDateArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceDenyMaintenancePeriodStartDateArgsDict(TypedDict):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceDenyMaintenancePeriodStartDateArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceDenyMaintenancePeriodTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceDenyMaintenancePeriodTimeArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceEncryptionConfigArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_name_version: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceEncryptionConfigArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_name_version: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyNameVersion")
    def kms_key_name_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name_version.setter
    def kms_key_name_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyState")
    def kms_key_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_state.setter
    def kms_key_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceMaintenanceWindowArgsDict(TypedDict):
    day_of_week: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[InstanceMaintenanceWindowStartTimeArgsDict]
    ...

@pulumi.input_type
class InstanceMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        day_of_week: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[InstanceMaintenanceWindowStartTimeArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Input[_builtins.str]: ...
    @day_of_week.setter
    def day_of_week(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[InstanceMaintenanceWindowStartTimeArgs]: ...
    @start_time.setter
    def start_time(
        self, value: pulumi.Input[InstanceMaintenanceWindowStartTimeArgs]
    ): ...

class InstanceMaintenanceWindowStartTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceMaintenanceWindowStartTimeArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceOauthConfigArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceOauthConfigArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        client_secret: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]: ...
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): ...

class InstancePeriodicExportConfigArgsDict(TypedDict):
    gcs_uri: pulumi.Input[_builtins.str]
    kms_key: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[InstancePeriodicExportConfigStartTimeArgsDict]
    ...

@pulumi.input_type
class InstancePeriodicExportConfigArgs:
    def __init__(
        __self__,
        *,
        gcs_uri: pulumi.Input[_builtins.str],
        kms_key: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[InstancePeriodicExportConfigStartTimeArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcsUri")
    def gcs_uri(self) -> pulumi.Input[_builtins.str]: ...
    @gcs_uri.setter
    def gcs_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key.setter
    def kms_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[InstancePeriodicExportConfigStartTimeArgs]: ...
    @start_time.setter
    def start_time(
        self, value: pulumi.Input[InstancePeriodicExportConfigStartTimeArgs]
    ): ...

class InstancePeriodicExportConfigStartTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstancePeriodicExportConfigStartTimeArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstancePscConfigArgsDict(TypedDict):
    allowed_vpcs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    looker_service_attachment_uri: NotRequired[pulumi.Input[_builtins.str]]
    service_attachments: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InstancePscConfigServiceAttachmentArgsDict]]]
    ]
    ...

@pulumi.input_type
class InstancePscConfigArgs:
    def __init__(
        __self__,
        *,
        allowed_vpcs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        looker_service_attachment_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        service_attachments: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstancePscConfigServiceAttachmentArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedVpcs")
    def allowed_vpcs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_vpcs.setter
    def allowed_vpcs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lookerServiceAttachmentUri")
    def looker_service_attachment_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @looker_service_attachment_uri.setter
    def looker_service_attachment_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachments")
    def service_attachments(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstancePscConfigServiceAttachmentArgs]]]
    ]: ...
    @service_attachments.setter
    def service_attachments(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstancePscConfigServiceAttachmentArgs]]]
        ],
    ): ...

class InstancePscConfigServiceAttachmentArgsDict(TypedDict):
    connection_status: NotRequired[pulumi.Input[_builtins.str]]
    local_fqdn: NotRequired[pulumi.Input[_builtins.str]]
    target_service_attachment_uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstancePscConfigServiceAttachmentArgs:
    def __init__(
        __self__,
        *,
        connection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        local_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        target_service_attachment_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_status.setter
    def connection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localFqdn")
    def local_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_fqdn.setter
    def local_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetServiceAttachmentUri")
    def target_service_attachment_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_service_attachment_uri.setter
    def target_service_attachment_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class InstanceUserMetadataArgsDict(TypedDict):
    additional_developer_user_count: NotRequired[pulumi.Input[_builtins.int]]
    additional_standard_user_count: NotRequired[pulumi.Input[_builtins.int]]
    additional_viewer_user_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceUserMetadataArgs:
    def __init__(
        __self__,
        *,
        additional_developer_user_count: Optional[pulumi.Input[_builtins.int]] = ...,
        additional_standard_user_count: Optional[pulumi.Input[_builtins.int]] = ...,
        additional_viewer_user_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalDeveloperUserCount")
    def additional_developer_user_count(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @additional_developer_user_count.setter
    def additional_developer_user_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalStandardUserCount")
    def additional_standard_user_count(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @additional_standard_user_count.setter
    def additional_standard_user_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalViewerUserCount")
    def additional_viewer_user_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @additional_viewer_user_count.setter
    def additional_viewer_user_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
