import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BrokerConfigurationArgs",
    "BrokerConfigurationArgsDict",
    "BrokerEncryptionOptionsArgs",
    "BrokerEncryptionOptionsArgsDict",
    "BrokerInstanceArgs",
    "BrokerInstanceArgsDict",
    "BrokerLdapServerMetadataArgs",
    "BrokerLdapServerMetadataArgsDict",
    "BrokerLogsArgs",
    "BrokerLogsArgsDict",
    "BrokerMaintenanceWindowStartTimeArgs",
    "BrokerMaintenanceWindowStartTimeArgsDict",
    "BrokerUserArgs",
    "BrokerUserArgsDict",
]

class BrokerConfigurationArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    revision: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class BrokerConfigurationArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class BrokerEncryptionOptionsArgsDict(TypedDict):
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    use_aws_owned_key: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class BrokerEncryptionOptionsArgs:
    def __init__(
        __self__,
        *,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        use_aws_owned_key: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useAwsOwnedKey")
    def use_aws_owned_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_aws_owned_key.setter
    def use_aws_owned_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class BrokerInstanceArgsDict(TypedDict):
    console_url: NotRequired[pulumi.Input[_builtins.str]]
    endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class BrokerInstanceArgs:
    def __init__(
        __self__,
        *,
        console_url: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consoleUrl")
    def console_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @console_url.setter
    def console_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @endpoints.setter
    def endpoints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BrokerLdapServerMetadataArgsDict(TypedDict):
    hosts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    role_base: NotRequired[pulumi.Input[_builtins.str]]
    role_name: NotRequired[pulumi.Input[_builtins.str]]
    role_search_matching: NotRequired[pulumi.Input[_builtins.str]]
    role_search_subtree: NotRequired[pulumi.Input[_builtins.bool]]
    service_account_password: NotRequired[pulumi.Input[_builtins.str]]
    service_account_username: NotRequired[pulumi.Input[_builtins.str]]
    user_base: NotRequired[pulumi.Input[_builtins.str]]
    user_role_name: NotRequired[pulumi.Input[_builtins.str]]
    user_search_matching: NotRequired[pulumi.Input[_builtins.str]]
    user_search_subtree: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class BrokerLdapServerMetadataArgs:
    def __init__(
        __self__,
        *,
        hosts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        role_base: Optional[pulumi.Input[_builtins.str]] = ...,
        role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        role_search_matching: Optional[pulumi.Input[_builtins.str]] = ...,
        role_search_subtree: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_account_password: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_username: Optional[pulumi.Input[_builtins.str]] = ...,
        user_base: Optional[pulumi.Input[_builtins.str]] = ...,
        user_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        user_search_matching: Optional[pulumi.Input[_builtins.str]] = ...,
        user_search_subtree: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @hosts.setter
    def hosts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleBase")
    def role_base(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_base.setter
    def role_base(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleSearchMatching")
    def role_search_matching(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_search_matching.setter
    def role_search_matching(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleSearchSubtree")
    def role_search_subtree(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @role_search_subtree.setter
    def role_search_subtree(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountPassword")
    def service_account_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_password.setter
    def service_account_password(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountUsername")
    def service_account_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_username.setter
    def service_account_username(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userBase")
    def user_base(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_base.setter
    def user_base(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userRoleName")
    def user_role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_role_name.setter
    def user_role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userSearchMatching")
    def user_search_matching(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_search_matching.setter
    def user_search_matching(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userSearchSubtree")
    def user_search_subtree(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @user_search_subtree.setter
    def user_search_subtree(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class BrokerLogsArgsDict(TypedDict):
    audit: NotRequired[pulumi.Input[_builtins.bool]]
    general: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class BrokerLogsArgs:
    def __init__(
        __self__,
        *,
        audit: Optional[pulumi.Input[_builtins.bool]] = ...,
        general: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audit(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @audit.setter
    def audit(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def general(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @general.setter
    def general(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class BrokerMaintenanceWindowStartTimeArgsDict(TypedDict):
    day_of_week: pulumi.Input[_builtins.str]
    time_of_day: pulumi.Input[_builtins.str]
    time_zone: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class BrokerMaintenanceWindowStartTimeArgs:
    def __init__(
        __self__,
        *,
        day_of_week: pulumi.Input[_builtins.str],
        time_of_day: pulumi.Input[_builtins.str],
        time_zone: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Input[_builtins.str]: ...
    @day_of_week.setter
    def day_of_week(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeOfDay")
    def time_of_day(self) -> pulumi.Input[_builtins.str]: ...
    @time_of_day.setter
    def time_of_day(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[_builtins.str]: ...
    @time_zone.setter
    def time_zone(self, value: pulumi.Input[_builtins.str]): ...

class BrokerUserArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    console_access: NotRequired[pulumi.Input[_builtins.bool]]
    groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    replication_user: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class BrokerUserArgs:
    def __init__(
        __self__,
        *,
        password: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
        console_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        replication_user: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="consoleAccess")
    def console_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @console_access.setter
    def console_access(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @groups.setter
    def groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationUser")
    def replication_user(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @replication_user.setter
    def replication_user(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
