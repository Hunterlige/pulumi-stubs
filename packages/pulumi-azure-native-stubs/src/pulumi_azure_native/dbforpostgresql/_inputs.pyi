import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AdminCredentialsArgs",
    "AdminCredentialsArgsDict",
    "AuthConfigArgs",
    "AuthConfigArgsDict",
    "BackupArgs",
    "BackupArgsDict",
    "ClusterArgs",
    "ClusterArgsDict",
    "DataEncryptionArgs",
    "DataEncryptionArgsDict",
    "HighAvailabilityArgs",
    "HighAvailabilityArgsDict",
    "IdentityPropertiesArgs",
    "IdentityPropertiesArgsDict",
    "MaintenanceWindowArgs",
    "MaintenanceWindowArgsDict",
    "MigrationSecretParametersArgs",
    "MigrationSecretParametersArgsDict",
    "NetworkArgs",
    "NetworkArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "ReplicaArgs",
    "ReplicaArgsDict",
    "ResourceIdentityArgs",
    "ResourceIdentityArgsDict",
    "ServerGroupClusterAuthConfigArgs",
    "ServerGroupClusterAuthConfigArgsDict",
    "ServerGroupClusterDataEncryptionArgs",
    "ServerGroupClusterDataEncryptionArgsDict",
    "ServerGroupClusterMaintenanceWindowArgs",
    "ServerGroupClusterMaintenanceWindowArgsDict",
    "ServerPropertiesForDefaultCreateArgs",
    "ServerPropertiesForDefaultCreateArgsDict",
    "ServerPropertiesForGeoRestoreArgs",
    "ServerPropertiesForGeoRestoreArgsDict",
    "ServerPropertiesForReplicaArgs",
    "ServerPropertiesForReplicaArgsDict",
    "ServerPropertiesForRestoreArgs",
    "ServerPropertiesForRestoreArgsDict",
    "SingleServerSkuArgs",
    "SingleServerSkuArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "StorageProfileArgs",
    "StorageProfileArgsDict",
    "StorageArgs",
    "StorageArgsDict",
    "UserAssignedIdentityArgs",
    "UserAssignedIdentityArgsDict",
    "UserIdentityArgs",
    "UserIdentityArgsDict",
]

class AdminCredentialsArgsDict(TypedDict):
    source_server_password: pulumi.Input[_builtins.str]
    target_server_password: pulumi.Input[_builtins.str]

@pulumi.input_type
class AdminCredentialsArgs:
    def __init__(
        __self__,
        *,
        source_server_password: pulumi.Input[_builtins.str],
        target_server_password: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceServerPassword")
    def source_server_password(self) -> pulumi.Input[_builtins.str]: ...
    @source_server_password.setter
    def source_server_password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetServerPassword")
    def target_server_password(self) -> pulumi.Input[_builtins.str]: ...
    @target_server_password.setter
    def target_server_password(self, value: pulumi.Input[_builtins.str]): ...

class AuthConfigArgsDict(TypedDict):
    active_directory_auth: NotRequired[
        pulumi.Input[Union[_builtins.str, MicrosoftEntraAuth]]
    ]
    password_auth: NotRequired[pulumi.Input[Union[_builtins.str, PasswordBasedAuth]]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AuthConfigArgs:
    def __init__(
        __self__,
        *,
        active_directory_auth: Optional[
            pulumi.Input[Union[_builtins.str, MicrosoftEntraAuth]]
        ] = ...,
        password_auth: Optional[
            pulumi.Input[Union[_builtins.str, PasswordBasedAuth]]
        ] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryAuth")
    def active_directory_auth(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MicrosoftEntraAuth]]]: ...
    @active_directory_auth.setter
    def active_directory_auth(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MicrosoftEntraAuth]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="passwordAuth")
    def password_auth(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PasswordBasedAuth]]]: ...
    @password_auth.setter
    def password_auth(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PasswordBasedAuth]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BackupArgsDict(TypedDict):
    backup_retention_days: NotRequired[pulumi.Input[_builtins.int]]
    geo_redundant_backup: NotRequired[
        pulumi.Input[Union[_builtins.str, GeographicallyRedundantBackup]]
    ]

@pulumi.input_type
class BackupArgs:
    def __init__(
        __self__,
        *,
        backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        geo_redundant_backup: Optional[
            pulumi.Input[Union[_builtins.str, GeographicallyRedundantBackup]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backup_retention_days.setter
    def backup_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, GeographicallyRedundantBackup]]
    ]: ...
    @geo_redundant_backup.setter
    def geo_redundant_backup(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, GeographicallyRedundantBackup]]
        ],
    ): ...

class ClusterArgsDict(TypedDict):
    cluster_size: NotRequired[pulumi.Input[_builtins.int]]
    default_database_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterArgs:
    def __init__(
        __self__,
        *,
        cluster_size: Optional[pulumi.Input[_builtins.int]] = ...,
        default_database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterSize")
    def cluster_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cluster_size.setter
    def cluster_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultDatabaseName")
    def default_database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_database_name.setter
    def default_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataEncryptionArgsDict(TypedDict):
    geo_backup_key_uri: NotRequired[pulumi.Input[_builtins.str]]
    geo_backup_user_assigned_identity_id: NotRequired[pulumi.Input[_builtins.str]]
    primary_key_uri: NotRequired[pulumi.Input[_builtins.str]]
    primary_user_assigned_identity_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, DataEncryptionType]]]

@pulumi.input_type
class DataEncryptionArgs:
    def __init__(
        __self__,
        *,
        geo_backup_key_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        geo_backup_user_assigned_identity_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        primary_key_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_user_assigned_identity_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, DataEncryptionType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="geoBackupKeyURI")
    def geo_backup_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @geo_backup_key_uri.setter
    def geo_backup_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="geoBackupUserAssignedIdentityId")
    def geo_backup_user_assigned_identity_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @geo_backup_user_assigned_identity_id.setter
    def geo_backup_user_assigned_identity_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryKeyURI")
    def primary_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_key_uri.setter
    def primary_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_user_assigned_identity_id.setter
    def primary_user_assigned_identity_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DataEncryptionType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DataEncryptionType]]]
    ): ...

class HighAvailabilityArgsDict(TypedDict):
    mode: NotRequired[
        pulumi.Input[Union[_builtins.str, PostgreSqlFlexibleServerHighAvailabilityMode]]
    ]
    standby_availability_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HighAvailabilityArgs:
    def __init__(
        __self__,
        *,
        mode: Optional[
            pulumi.Input[
                Union[_builtins.str, PostgreSqlFlexibleServerHighAvailabilityMode]
            ]
        ] = ...,
        standby_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PostgreSqlFlexibleServerHighAvailabilityMode]]
    ]: ...
    @mode.setter
    def mode(
        self,
        value: Optional[
            pulumi.Input[
                Union[_builtins.str, PostgreSqlFlexibleServerHighAvailabilityMode]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @standby_availability_zone.setter
    def standby_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class IdentityPropertiesArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, IdentityType]]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class IdentityPropertiesArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class MaintenanceWindowArgsDict(TypedDict):
    custom_window: NotRequired[pulumi.Input[_builtins.str]]
    day_of_week: NotRequired[pulumi.Input[_builtins.int]]
    start_hour: NotRequired[pulumi.Input[_builtins.int]]
    start_minute: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class MaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        custom_window: Optional[pulumi.Input[_builtins.str]] = ...,
        day_of_week: Optional[pulumi.Input[_builtins.int]] = ...,
        start_hour: Optional[pulumi.Input[_builtins.int]] = ...,
        start_minute: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customWindow")
    def custom_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_window.setter
    def custom_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @start_hour.setter
    def start_hour(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @start_minute.setter
    def start_minute(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class MigrationSecretParametersArgsDict(TypedDict):
    admin_credentials: pulumi.Input[AdminCredentialsArgsDict]
    source_server_username: NotRequired[pulumi.Input[_builtins.str]]
    target_server_username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MigrationSecretParametersArgs:
    def __init__(
        __self__,
        *,
        admin_credentials: pulumi.Input[AdminCredentialsArgs],
        source_server_username: Optional[pulumi.Input[_builtins.str]] = ...,
        target_server_username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminCredentials")
    def admin_credentials(self) -> pulumi.Input[AdminCredentialsArgs]: ...
    @admin_credentials.setter
    def admin_credentials(self, value: pulumi.Input[AdminCredentialsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="sourceServerUsername")
    def source_server_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_server_username.setter
    def source_server_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetServerUsername")
    def target_server_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_server_username.setter
    def target_server_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkArgsDict(TypedDict):
    delegated_subnet_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    private_dns_zone_arm_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, ServerPublicNetworkAccessState]]
    ]

@pulumi.input_type
class NetworkArgs:
    def __init__(
        __self__,
        *,
        delegated_subnet_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        private_dns_zone_arm_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, ServerPublicNetworkAccessState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="delegatedSubnetResourceId")
    def delegated_subnet_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delegated_subnet_resource_id.setter
    def delegated_subnet_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateDnsZoneArmResourceId")
    def private_dns_zone_arm_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_dns_zone_arm_resource_id.setter
    def private_dns_zone_arm_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ServerPublicNetworkAccessState]]
    ]: ...
    @public_network_access.setter
    def public_network_access(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ServerPublicNetworkAccessState]]
        ],
    ): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ],
    ): ...

class ReplicaArgsDict(TypedDict):
    promote_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, ReadReplicaPromoteMode]]
    ]
    promote_option: NotRequired[
        pulumi.Input[Union[_builtins.str, ReadReplicaPromoteOption]]
    ]
    role: NotRequired[pulumi.Input[Union[_builtins.str, ReplicationRole]]]

@pulumi.input_type
class ReplicaArgs:
    def __init__(
        __self__,
        *,
        promote_mode: Optional[
            pulumi.Input[Union[_builtins.str, ReadReplicaPromoteMode]]
        ] = ...,
        promote_option: Optional[
            pulumi.Input[Union[_builtins.str, ReadReplicaPromoteOption]]
        ] = ...,
        role: Optional[pulumi.Input[Union[_builtins.str, ReplicationRole]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="promoteMode")
    def promote_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ReadReplicaPromoteMode]]]: ...
    @promote_mode.setter
    def promote_mode(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ReadReplicaPromoteMode]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="promoteOption")
    def promote_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ReadReplicaPromoteOption]]]: ...
    @promote_option.setter
    def promote_option(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ReadReplicaPromoteOption]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[Union[_builtins.str, ReplicationRole]]]: ...
    @role.setter
    def role(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ReplicationRole]]]
    ): ...

class ResourceIdentityArgsDict(TypedDict):
    type: NotRequired[
        pulumi.Input[Union[_builtins.str, SingleServerIdentityProperties]]
    ]

@pulumi.input_type
class ResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[
            pulumi.Input[Union[_builtins.str, SingleServerIdentityProperties]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, SingleServerIdentityProperties]]
    ]: ...
    @type.setter
    def type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, SingleServerIdentityProperties]]
        ],
    ): ...

class ServerGroupClusterAuthConfigArgsDict(TypedDict):
    active_directory_auth: NotRequired[
        pulumi.Input[Union[_builtins.str, ActiveDirectoryAuth]]
    ]
    password_auth: NotRequired[pulumi.Input[Union[_builtins.str, PasswordAuth]]]

@pulumi.input_type
class ServerGroupClusterAuthConfigArgs:
    def __init__(
        __self__,
        *,
        active_directory_auth: Optional[
            pulumi.Input[Union[_builtins.str, ActiveDirectoryAuth]]
        ] = ...,
        password_auth: Optional[pulumi.Input[Union[_builtins.str, PasswordAuth]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryAuth")
    def active_directory_auth(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ActiveDirectoryAuth]]]: ...
    @active_directory_auth.setter
    def active_directory_auth(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ActiveDirectoryAuth]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="passwordAuth")
    def password_auth(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PasswordAuth]]]: ...
    @password_auth.setter
    def password_auth(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PasswordAuth]]]
    ): ...

class ServerGroupClusterDataEncryptionArgsDict(TypedDict):
    primary_key_uri: NotRequired[pulumi.Input[_builtins.str]]
    primary_user_assigned_identity_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, DataEncryptionType]]]

@pulumi.input_type
class ServerGroupClusterDataEncryptionArgs:
    def __init__(
        __self__,
        *,
        primary_key_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_user_assigned_identity_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, DataEncryptionType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryKeyUri")
    def primary_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_key_uri.setter
    def primary_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_user_assigned_identity_id.setter
    def primary_user_assigned_identity_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DataEncryptionType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DataEncryptionType]]]
    ): ...

class ServerGroupClusterMaintenanceWindowArgsDict(TypedDict):
    custom_window: NotRequired[pulumi.Input[_builtins.str]]
    day_of_week: NotRequired[pulumi.Input[_builtins.int]]
    start_hour: NotRequired[pulumi.Input[_builtins.int]]
    start_minute: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServerGroupClusterMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        custom_window: Optional[pulumi.Input[_builtins.str]] = ...,
        day_of_week: Optional[pulumi.Input[_builtins.int]] = ...,
        start_hour: Optional[pulumi.Input[_builtins.int]] = ...,
        start_minute: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customWindow")
    def custom_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_window.setter
    def custom_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @start_hour.setter
    def start_hour(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @start_minute.setter
    def start_minute(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServerPropertiesForDefaultCreateArgsDict(TypedDict):
    administrator_login: pulumi.Input[_builtins.str]
    administrator_login_password: pulumi.Input[_builtins.str]
    create_mode: pulumi.Input[_builtins.str]
    infrastructure_encryption: NotRequired[
        pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]
    ]
    minimal_tls_version: NotRequired[
        pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]
    ]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]
    ]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]

@pulumi.input_type
class ServerPropertiesForDefaultCreateArgs:
    def __init__(
        __self__,
        *,
        administrator_login: pulumi.Input[_builtins.str],
        administrator_login_password: pulumi.Input[_builtins.str],
        create_mode: pulumi.Input[_builtins.str],
        infrastructure_encryption: Optional[
            pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]
        ] = ...,
        minimal_tls_version: Optional[
            pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]
        ] = ...,
        ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ...,
        storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ...,
        version: Optional[
            pulumi.Input[Union[_builtins.str, SingleServerVersion]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Input[_builtins.str]: ...
    @administrator_login.setter
    def administrator_login(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> pulumi.Input[_builtins.str]: ...
    @administrator_login_password.setter
    def administrator_login_password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[_builtins.str]: ...
    @create_mode.setter
    def create_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]: ...
    @infrastructure_encryption.setter
    def infrastructure_encryption(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]: ...
    @minimal_tls_version.setter
    def minimal_tls_version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]: ...
    @public_network_access.setter
    def public_network_access(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input[SslEnforcementEnum]]: ...
    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input[SslEnforcementEnum]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]: ...
    @version.setter
    def version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]
    ): ...

class ServerPropertiesForGeoRestoreArgsDict(TypedDict):
    create_mode: pulumi.Input[_builtins.str]
    source_server_id: pulumi.Input[_builtins.str]
    infrastructure_encryption: NotRequired[
        pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]
    ]
    minimal_tls_version: NotRequired[
        pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]
    ]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]
    ]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]

@pulumi.input_type
class ServerPropertiesForGeoRestoreArgs:
    def __init__(
        __self__,
        *,
        create_mode: pulumi.Input[_builtins.str],
        source_server_id: pulumi.Input[_builtins.str],
        infrastructure_encryption: Optional[
            pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]
        ] = ...,
        minimal_tls_version: Optional[
            pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]
        ] = ...,
        ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ...,
        storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ...,
        version: Optional[
            pulumi.Input[Union[_builtins.str, SingleServerVersion]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[_builtins.str]: ...
    @create_mode.setter
    def create_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceServerId")
    def source_server_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_server_id.setter
    def source_server_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]: ...
    @infrastructure_encryption.setter
    def infrastructure_encryption(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]: ...
    @minimal_tls_version.setter
    def minimal_tls_version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]: ...
    @public_network_access.setter
    def public_network_access(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input[SslEnforcementEnum]]: ...
    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input[SslEnforcementEnum]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]: ...
    @version.setter
    def version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]
    ): ...

class ServerPropertiesForReplicaArgsDict(TypedDict):
    create_mode: pulumi.Input[_builtins.str]
    source_server_id: pulumi.Input[_builtins.str]
    infrastructure_encryption: NotRequired[
        pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]
    ]
    minimal_tls_version: NotRequired[
        pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]
    ]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]
    ]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]

@pulumi.input_type
class ServerPropertiesForReplicaArgs:
    def __init__(
        __self__,
        *,
        create_mode: pulumi.Input[_builtins.str],
        source_server_id: pulumi.Input[_builtins.str],
        infrastructure_encryption: Optional[
            pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]
        ] = ...,
        minimal_tls_version: Optional[
            pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]
        ] = ...,
        ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ...,
        storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ...,
        version: Optional[
            pulumi.Input[Union[_builtins.str, SingleServerVersion]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[_builtins.str]: ...
    @create_mode.setter
    def create_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceServerId")
    def source_server_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_server_id.setter
    def source_server_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]: ...
    @infrastructure_encryption.setter
    def infrastructure_encryption(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]: ...
    @minimal_tls_version.setter
    def minimal_tls_version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]: ...
    @public_network_access.setter
    def public_network_access(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input[SslEnforcementEnum]]: ...
    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input[SslEnforcementEnum]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]: ...
    @version.setter
    def version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]
    ): ...

class ServerPropertiesForRestoreArgsDict(TypedDict):
    create_mode: pulumi.Input[_builtins.str]
    restore_point_in_time: pulumi.Input[_builtins.str]
    source_server_id: pulumi.Input[_builtins.str]
    infrastructure_encryption: NotRequired[
        pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]
    ]
    minimal_tls_version: NotRequired[
        pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]
    ]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]
    ]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]

@pulumi.input_type
class ServerPropertiesForRestoreArgs:
    def __init__(
        __self__,
        *,
        create_mode: pulumi.Input[_builtins.str],
        restore_point_in_time: pulumi.Input[_builtins.str],
        source_server_id: pulumi.Input[_builtins.str],
        infrastructure_encryption: Optional[
            pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]
        ] = ...,
        minimal_tls_version: Optional[
            pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]
        ] = ...,
        ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ...,
        storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ...,
        version: Optional[
            pulumi.Input[Union[_builtins.str, SingleServerVersion]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[_builtins.str]: ...
    @create_mode.setter
    def create_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> pulumi.Input[_builtins.str]: ...
    @restore_point_in_time.setter
    def restore_point_in_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceServerId")
    def source_server_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_server_id.setter
    def source_server_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]: ...
    @infrastructure_encryption.setter
    def infrastructure_encryption(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]: ...
    @minimal_tls_version.setter
    def minimal_tls_version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]: ...
    @public_network_access.setter
    def public_network_access(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input[SslEnforcementEnum]]: ...
    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input[SslEnforcementEnum]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]: ...
    @version.setter
    def version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]
    ): ...

class SingleServerSkuArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, SingleServerSkuTier]]]

@pulumi.input_type
class SingleServerSkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        size: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[Union[_builtins.str, SingleServerSkuTier]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SingleServerSkuTier]]]: ...
    @tier.setter
    def tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SingleServerSkuTier]]]
    ): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    tier: pulumi.Input[Union[_builtins.str, SkuTier]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        tier: pulumi.Input[Union[_builtins.str, SkuTier]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[_builtins.str, SkuTier]]: ...
    @tier.setter
    def tier(self, value: pulumi.Input[Union[_builtins.str, SkuTier]]): ...

class StorageProfileArgsDict(TypedDict):
    backup_retention_days: NotRequired[pulumi.Input[_builtins.int]]
    geo_redundant_backup: NotRequired[
        pulumi.Input[Union[_builtins.str, GeoRedundantBackup]]
    ]
    storage_autogrow: NotRequired[pulumi.Input[Union[_builtins.str, StorageAutogrow]]]
    storage_mb: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class StorageProfileArgs:
    def __init__(
        __self__,
        *,
        backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        geo_redundant_backup: Optional[
            pulumi.Input[Union[_builtins.str, GeoRedundantBackup]]
        ] = ...,
        storage_autogrow: Optional[
            pulumi.Input[Union[_builtins.str, StorageAutogrow]]
        ] = ...,
        storage_mb: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backup_retention_days.setter
    def backup_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, GeoRedundantBackup]]]: ...
    @geo_redundant_backup.setter
    def geo_redundant_backup(
        self, value: Optional[pulumi.Input[Union[_builtins.str, GeoRedundantBackup]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAutogrow")
    def storage_autogrow(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StorageAutogrow]]]: ...
    @storage_autogrow.setter
    def storage_autogrow(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAutogrow]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageMB")
    def storage_mb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_mb.setter
    def storage_mb(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StorageArgsDict(TypedDict):
    auto_grow: NotRequired[pulumi.Input[Union[_builtins.str, StorageAutoGrow]]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    tier: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureManagedDiskPerformanceTier]]
    ]
    type: NotRequired[pulumi.Input[Union[_builtins.str, StorageType]]]

@pulumi.input_type
class StorageArgs:
    def __init__(
        __self__,
        *,
        auto_grow: Optional[pulumi.Input[Union[_builtins.str, StorageAutoGrow]]] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        tier: Optional[
            pulumi.Input[Union[_builtins.str, AzureManagedDiskPerformanceTier]]
        ] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, StorageType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoGrow")
    def auto_grow(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StorageAutoGrow]]]: ...
    @auto_grow.setter
    def auto_grow(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAutoGrow]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageSizeGB")
    def storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_size_gb.setter
    def storage_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, AzureManagedDiskPerformanceTier]]
    ]: ...
    @tier.setter
    def tier(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, AzureManagedDiskPerformanceTier]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StorageType]]]
    ): ...

class UserAssignedIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, IdentityType]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[UserIdentityArgsDict]]]
    ]

@pulumi.input_type
class UserAssignedIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, IdentityType]],
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserIdentityArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, IdentityType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, IdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[UserIdentityArgs]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self,
        value: Optional[pulumi.Input[Mapping[str, pulumi.Input[UserIdentityArgs]]]],
    ): ...

class UserIdentityArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserIdentityArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
