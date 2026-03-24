import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BrokerConfiguration",
    "BrokerEncryptionOptions",
    "BrokerInstance",
    "BrokerLdapServerMetadata",
    "BrokerLogs",
    "BrokerMaintenanceWindowStartTime",
    "BrokerUser",
    "GetBrokerConfigurationResult",
    "GetBrokerEncryptionOptionResult",
    "GetBrokerEngineTypesBrokerEngineTypeResult",
    ...,
    "GetBrokerInstanceResult",
    "GetBrokerLdapServerMetadataResult",
    "GetBrokerLogsResult",
    "GetBrokerMaintenanceWindowStartTimeResult",
    "GetBrokerUserResult",
    "GetInstanceTypeOfferingsBrokerInstanceOptionResult",
    ...,
]

@pulumi.output_type
class BrokerConfiguration(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        revision: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BrokerEncryptionOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_id: Optional[_builtins.str] = ...,
        use_aws_owned_key: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useAwsOwnedKey")
    def use_aws_owned_key(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class BrokerInstance(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        console_url: Optional[_builtins.str] = ...,
        endpoints: Optional[Sequence[_builtins.str]] = ...,
        ip_address: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consoleUrl")
    def console_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BrokerLdapServerMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hosts: Optional[Sequence[_builtins.str]] = ...,
        role_base: Optional[_builtins.str] = ...,
        role_name: Optional[_builtins.str] = ...,
        role_search_matching: Optional[_builtins.str] = ...,
        role_search_subtree: Optional[_builtins.bool] = ...,
        service_account_password: Optional[_builtins.str] = ...,
        service_account_username: Optional[_builtins.str] = ...,
        user_base: Optional[_builtins.str] = ...,
        user_role_name: Optional[_builtins.str] = ...,
        user_search_matching: Optional[_builtins.str] = ...,
        user_search_subtree: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="roleBase")
    def role_base(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleSearchMatching")
    def role_search_matching(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleSearchSubtree")
    def role_search_subtree(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountPassword")
    def service_account_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountUsername")
    def service_account_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userBase")
    def user_base(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userRoleName")
    def user_role_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userSearchMatching")
    def user_search_matching(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userSearchSubtree")
    def user_search_subtree(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class BrokerLogs(dict):
    def __init__(
        __self__,
        *,
        audit: Optional[_builtins.bool] = ...,
        general: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audit(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def general(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class BrokerMaintenanceWindowStartTime(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day_of_week: _builtins.str,
        time_of_day: _builtins.str,
        time_zone: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeOfDay")
    def time_of_day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str: ...

@pulumi.output_type
class BrokerUser(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        password: _builtins.str,
        username: _builtins.str,
        console_access: Optional[_builtins.bool] = ...,
        groups: Optional[Sequence[_builtins.str]] = ...,
        replication_user: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="consoleAccess")
    def console_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="replicationUser")
    def replication_user(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GetBrokerConfigurationResult(dict):
    def __init__(__self__, *, id: _builtins.str, revision: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.int: ...

@pulumi.output_type
class GetBrokerEncryptionOptionResult(dict):
    def __init__(
        __self__, *, kms_key_id: _builtins.str, use_aws_owned_key: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="useAwsOwnedKey")
    def use_aws_owned_key(self) -> _builtins.bool: ...

@pulumi.output_type
class GetBrokerEngineTypesBrokerEngineTypeResult(dict):
    def __init__(
        __self__,
        *,
        engine_type: _builtins.str,
        engine_versions: Sequence[
            outputs.GetBrokerEngineTypesBrokerEngineTypeEngineVersionResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="engineVersions")
    def engine_versions(
        self,
    ) -> Sequence[outputs.GetBrokerEngineTypesBrokerEngineTypeEngineVersionResult]: ...

@pulumi.output_type
class GetBrokerEngineTypesBrokerEngineTypeEngineVersionResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetBrokerInstanceResult(dict):
    def __init__(
        __self__,
        *,
        console_url: _builtins.str,
        endpoints: Sequence[_builtins.str],
        ip_address: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consoleUrl")
    def console_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...

@pulumi.output_type
class GetBrokerLdapServerMetadataResult(dict):
    def __init__(
        __self__,
        *,
        hosts: Sequence[_builtins.str],
        role_base: _builtins.str,
        role_name: _builtins.str,
        role_search_matching: _builtins.str,
        role_search_subtree: _builtins.bool,
        service_account_password: _builtins.str,
        service_account_username: _builtins.str,
        user_base: _builtins.str,
        user_role_name: _builtins.str,
        user_search_matching: _builtins.str,
        user_search_subtree: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleBase")
    def role_base(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleSearchMatching")
    def role_search_matching(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleSearchSubtree")
    def role_search_subtree(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountPassword")
    def service_account_password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountUsername")
    def service_account_username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userBase")
    def user_base(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userRoleName")
    def user_role_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userSearchMatching")
    def user_search_matching(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userSearchSubtree")
    def user_search_subtree(self) -> _builtins.bool: ...

@pulumi.output_type
class GetBrokerLogsResult(dict):
    def __init__(
        __self__, *, audit: _builtins.bool, general: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audit(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def general(self) -> _builtins.bool: ...

@pulumi.output_type
class GetBrokerMaintenanceWindowStartTimeResult(dict):
    def __init__(
        __self__,
        *,
        day_of_week: _builtins.str,
        time_of_day: _builtins.str,
        time_zone: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeOfDay")
    def time_of_day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str: ...

@pulumi.output_type
class GetBrokerUserResult(dict):
    def __init__(
        __self__,
        *,
        console_access: _builtins.bool,
        groups: Sequence[_builtins.str],
        replication_user: _builtins.bool,
        username: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consoleAccess")
    def console_access(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationUser")
    def replication_user(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceTypeOfferingsBrokerInstanceOptionResult(dict):
    def __init__(
        __self__,
        *,
        availability_zones: Sequence[
            outputs.GetInstanceTypeOfferingsBrokerInstanceOptionAvailabilityZoneResult
        ],
        engine_type: _builtins.str,
        host_instance_type: _builtins.str,
        storage_type: _builtins.str,
        supported_deployment_modes: Sequence[_builtins.str],
        supported_engine_versions: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Sequence[
        outputs.GetInstanceTypeOfferingsBrokerInstanceOptionAvailabilityZoneResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostInstanceType")
    def host_instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedDeploymentModes")
    def supported_deployment_modes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedEngineVersions")
    def supported_engine_versions(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetInstanceTypeOfferingsBrokerInstanceOptionAvailabilityZoneResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
