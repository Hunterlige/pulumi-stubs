import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FileSystemAssociationCacheAttributesArgs",
    "FileSystemAssociationCacheAttributesArgsDict",
    "GatewayGatewayNetworkInterfaceArgs",
    "GatewayGatewayNetworkInterfaceArgsDict",
    "GatewayMaintenanceStartTimeArgs",
    "GatewayMaintenanceStartTimeArgsDict",
    "GatewaySmbActiveDirectorySettingsArgs",
    "GatewaySmbActiveDirectorySettingsArgsDict",
    "NfsFileShareCacheAttributesArgs",
    "NfsFileShareCacheAttributesArgsDict",
    "NfsFileShareNfsFileShareDefaultsArgs",
    "NfsFileShareNfsFileShareDefaultsArgsDict",
    "SmbFileShareCacheAttributesArgs",
    "SmbFileShareCacheAttributesArgsDict",
]

class FileSystemAssociationCacheAttributesArgsDict(TypedDict):
    cache_stale_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FileSystemAssociationCacheAttributesArgs:
    def __init__(
        __self__,
        *,
        cache_stale_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cache_stale_timeout_in_seconds.setter
    def cache_stale_timeout_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class GatewayGatewayNetworkInterfaceArgsDict(TypedDict):
    ipv4_address: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayGatewayNetworkInterfaceArgs:
    def __init__(
        __self__, *, ipv4_address: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv4_address.setter
    def ipv4_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GatewayMaintenanceStartTimeArgsDict(TypedDict):
    hour_of_day: pulumi.Input[_builtins.int]
    day_of_month: NotRequired[pulumi.Input[_builtins.str]]
    day_of_week: NotRequired[pulumi.Input[_builtins.str]]
    minute_of_hour: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GatewayMaintenanceStartTimeArgs:
    def __init__(
        __self__,
        *,
        hour_of_day: pulumi.Input[_builtins.int],
        day_of_month: Optional[pulumi.Input[_builtins.str]] = ...,
        day_of_week: Optional[pulumi.Input[_builtins.str]] = ...,
        minute_of_hour: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> pulumi.Input[_builtins.int]: ...
    @hour_of_day.setter
    def hour_of_day(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_month.setter
    def day_of_month(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minute_of_hour.setter
    def minute_of_hour(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GatewaySmbActiveDirectorySettingsArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    active_directory_status: NotRequired[pulumi.Input[_builtins.str]]
    domain_controllers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    organizational_unit: NotRequired[pulumi.Input[_builtins.str]]
    timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GatewaySmbActiveDirectorySettingsArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        password: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
        active_directory_status: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_controllers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        organizational_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]: ...
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryStatus")
    def active_directory_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @active_directory_status.setter
    def active_directory_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainControllers")
    def domain_controllers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @domain_controllers.setter
    def domain_controllers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organizational_unit.setter
    def organizational_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class NfsFileShareCacheAttributesArgsDict(TypedDict):
    cache_stale_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class NfsFileShareCacheAttributesArgs:
    def __init__(
        __self__,
        *,
        cache_stale_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cache_stale_timeout_in_seconds.setter
    def cache_stale_timeout_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class NfsFileShareNfsFileShareDefaultsArgsDict(TypedDict):
    directory_mode: NotRequired[pulumi.Input[_builtins.str]]
    file_mode: NotRequired[pulumi.Input[_builtins.str]]
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    owner_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NfsFileShareNfsFileShareDefaultsArgs:
    def __init__(
        __self__,
        *,
        directory_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        file_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directoryMode")
    def directory_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_mode.setter
    def directory_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileMode")
    def file_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_mode.setter
    def file_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SmbFileShareCacheAttributesArgsDict(TypedDict):
    cache_stale_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class SmbFileShareCacheAttributesArgs:
    def __init__(
        __self__,
        *,
        cache_stale_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cache_stale_timeout_in_seconds.setter
    def cache_stale_timeout_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
