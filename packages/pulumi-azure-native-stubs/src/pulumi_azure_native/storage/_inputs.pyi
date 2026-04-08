import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessPolicyArgs",
    "AccessPolicyArgsDict",
    "AccountImmutabilityPolicyPropertiesArgs",
    "AccountImmutabilityPolicyPropertiesArgsDict",
    "ActiveDirectoryPropertiesArgs",
    "ActiveDirectoryPropertiesArgsDict",
    "AzureFilesIdentityBasedAuthenticationArgs",
    "AzureFilesIdentityBasedAuthenticationArgsDict",
    "BlobInventoryCreationTimeArgs",
    "BlobInventoryCreationTimeArgsDict",
    "BlobInventoryPolicyDefinitionArgs",
    "BlobInventoryPolicyDefinitionArgsDict",
    "BlobInventoryPolicyFilterArgs",
    "BlobInventoryPolicyFilterArgsDict",
    "BlobInventoryPolicyRuleArgs",
    "BlobInventoryPolicyRuleArgsDict",
    "BlobInventoryPolicySchemaArgs",
    "BlobInventoryPolicySchemaArgsDict",
    "ChangeFeedArgs",
    "ChangeFeedArgsDict",
    "CorsRulesArgs",
    "CorsRulesArgsDict",
    "CorsRuleArgs",
    "CorsRuleArgsDict",
    "CustomDomainArgs",
    "CustomDomainArgsDict",
    "DateAfterCreationArgs",
    "DateAfterCreationArgsDict",
    "DateAfterModificationArgs",
    "DateAfterModificationArgsDict",
    "DeleteRetentionPolicyArgs",
    "DeleteRetentionPolicyArgsDict",
    "EncryptionIdentityArgs",
    "EncryptionIdentityArgsDict",
    "EncryptionScopeKeyVaultPropertiesArgs",
    "EncryptionScopeKeyVaultPropertiesArgsDict",
    "EncryptionServicesArgs",
    "EncryptionServicesArgsDict",
    "EncryptionServiceArgs",
    "EncryptionServiceArgsDict",
    "EncryptionArgs",
    "EncryptionArgsDict",
    "ExecutionTargetArgs",
    "ExecutionTargetArgsDict",
    "ExecutionTriggerArgs",
    "ExecutionTriggerArgsDict",
    "ExtendedLocationArgs",
    "ExtendedLocationArgsDict",
    "FileSharePropertiesFileSharePaidBurstingArgs",
    "FileSharePropertiesFileSharePaidBurstingArgsDict",
    "IPRuleArgs",
    "IPRuleArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "ImmutableStorageAccountArgs",
    "ImmutableStorageAccountArgsDict",
    "ImmutableStorageWithVersioningArgs",
    "ImmutableStorageWithVersioningArgsDict",
    "KeyPolicyArgs",
    "KeyPolicyArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "LastAccessTimeTrackingPolicyArgs",
    "LastAccessTimeTrackingPolicyArgsDict",
    "ManagementPolicyActionArgs",
    "ManagementPolicyActionArgsDict",
    "ManagementPolicyBaseBlobArgs",
    "ManagementPolicyBaseBlobArgsDict",
    "ManagementPolicyDefinitionArgs",
    "ManagementPolicyDefinitionArgsDict",
    "ManagementPolicyFilterArgs",
    "ManagementPolicyFilterArgsDict",
    "ManagementPolicyRuleArgs",
    "ManagementPolicyRuleArgsDict",
    "ManagementPolicySchemaArgs",
    "ManagementPolicySchemaArgsDict",
    "ManagementPolicySnapShotArgs",
    "ManagementPolicySnapShotArgsDict",
    "ManagementPolicyVersionArgs",
    "ManagementPolicyVersionArgsDict",
    "MultichannelArgs",
    "MultichannelArgsDict",
    "NetworkRuleSetArgs",
    "NetworkRuleSetArgsDict",
    "ObjectReplicationPolicyFilterArgs",
    "ObjectReplicationPolicyFilterArgsDict",
    "ObjectReplicationPolicyPropertiesMetricsArgs",
    "ObjectReplicationPolicyPropertiesMetricsArgsDict",
    "ObjectReplicationPolicyRuleArgs",
    "ObjectReplicationPolicyRuleArgsDict",
    "PermissionScopeArgs",
    "PermissionScopeArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "ProtocolSettingsArgs",
    "ProtocolSettingsArgsDict",
    "ResourceAccessRuleArgs",
    "ResourceAccessRuleArgsDict",
    "RestorePolicyPropertiesArgs",
    "RestorePolicyPropertiesArgsDict",
    "RoutingPreferenceArgs",
    "RoutingPreferenceArgsDict",
    "SasPolicyArgs",
    "SasPolicyArgsDict",
    "SignedIdentifierArgs",
    "SignedIdentifierArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SmbSettingArgs",
    "SmbSettingArgsDict",
    "SshPublicKeyArgs",
    "SshPublicKeyArgsDict",
    "StorageTaskAssignmentExecutionContextArgs",
    "StorageTaskAssignmentExecutionContextArgsDict",
    "StorageTaskAssignmentPropertiesArgs",
    "StorageTaskAssignmentPropertiesArgsDict",
    "StorageTaskAssignmentReportArgs",
    "StorageTaskAssignmentReportArgsDict",
    "TableAccessPolicyArgs",
    "TableAccessPolicyArgsDict",
    "TableSignedIdentifierArgs",
    "TableSignedIdentifierArgsDict",
    "TagFilterArgs",
    "TagFilterArgsDict",
    "TriggerParametersArgs",
    "TriggerParametersArgsDict",
    "VirtualNetworkRuleArgs",
    "VirtualNetworkRuleArgsDict",
]

class AccessPolicyArgsDict(TypedDict):
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessPolicyArgs:
    def __init__(
        __self__,
        *,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccountImmutabilityPolicyPropertiesArgsDict(TypedDict):
    allow_protected_append_writes: NotRequired[pulumi.Input[_builtins.bool]]
    immutability_period_since_creation_in_days: NotRequired[pulumi.Input[_builtins.int]]
    state: NotRequired[
        pulumi.Input[Union[_builtins.str, AccountImmutabilityPolicyState]]
    ]

@pulumi.input_type
class AccountImmutabilityPolicyPropertiesArgs:
    def __init__(
        __self__,
        *,
        allow_protected_append_writes: Optional[pulumi.Input[_builtins.bool]] = ...,
        immutability_period_since_creation_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        state: Optional[
            pulumi.Input[Union[_builtins.str, AccountImmutabilityPolicyState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowProtectedAppendWrites")
    def allow_protected_append_writes(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_protected_append_writes.setter
    def allow_protected_append_writes(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="immutabilityPeriodSinceCreationInDays")
    def immutability_period_since_creation_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @immutability_period_since_creation_in_days.setter
    def immutability_period_since_creation_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, AccountImmutabilityPolicyState]]
    ]: ...
    @state.setter
    def state(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, AccountImmutabilityPolicyState]]
        ],
    ): ...

class ActiveDirectoryPropertiesArgsDict(TypedDict):
    domain_guid: pulumi.Input[_builtins.str]
    domain_name: pulumi.Input[_builtins.str]
    account_type: NotRequired[pulumi.Input[Union[_builtins.str, AccountType]]]
    azure_storage_sid: NotRequired[pulumi.Input[_builtins.str]]
    domain_sid: NotRequired[pulumi.Input[_builtins.str]]
    forest_name: NotRequired[pulumi.Input[_builtins.str]]
    net_bios_domain_name: NotRequired[pulumi.Input[_builtins.str]]
    sam_account_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ActiveDirectoryPropertiesArgs:
    def __init__(
        __self__,
        *,
        domain_guid: pulumi.Input[_builtins.str],
        domain_name: pulumi.Input[_builtins.str],
        account_type: Optional[pulumi.Input[Union[_builtins.str, AccountType]]] = ...,
        azure_storage_sid: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_sid: Optional[pulumi.Input[_builtins.str]] = ...,
        forest_name: Optional[pulumi.Input[_builtins.str]] = ...,
        net_bios_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sam_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainGuid")
    def domain_guid(self) -> pulumi.Input[_builtins.str]: ...
    @domain_guid.setter
    def domain_guid(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountType")
    def account_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AccountType]]]: ...
    @account_type.setter
    def account_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AccountType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureStorageSid")
    def azure_storage_sid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_storage_sid.setter
    def azure_storage_sid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainSid")
    def domain_sid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_sid.setter
    def domain_sid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forestName")
    def forest_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @forest_name.setter
    def forest_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="netBiosDomainName")
    def net_bios_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @net_bios_domain_name.setter
    def net_bios_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samAccountName")
    def sam_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sam_account_name.setter
    def sam_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureFilesIdentityBasedAuthenticationArgsDict(TypedDict):
    directory_service_options: pulumi.Input[
        Union[_builtins.str, DirectoryServiceOptions]
    ]
    active_directory_properties: NotRequired[
        pulumi.Input[ActiveDirectoryPropertiesArgsDict]
    ]
    default_share_permission: NotRequired[
        pulumi.Input[Union[_builtins.str, DefaultSharePermission]]
    ]

@pulumi.input_type
class AzureFilesIdentityBasedAuthenticationArgs:
    def __init__(
        __self__,
        *,
        directory_service_options: pulumi.Input[
            Union[_builtins.str, DirectoryServiceOptions]
        ],
        active_directory_properties: Optional[
            pulumi.Input[ActiveDirectoryPropertiesArgs]
        ] = ...,
        default_share_permission: Optional[
            pulumi.Input[Union[_builtins.str, DefaultSharePermission]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directoryServiceOptions")
    def directory_service_options(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DirectoryServiceOptions]]: ...
    @directory_service_options.setter
    def directory_service_options(
        self, value: pulumi.Input[Union[_builtins.str, DirectoryServiceOptions]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryProperties")
    def active_directory_properties(
        self,
    ) -> Optional[pulumi.Input[ActiveDirectoryPropertiesArgs]]: ...
    @active_directory_properties.setter
    def active_directory_properties(
        self, value: Optional[pulumi.Input[ActiveDirectoryPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultSharePermission")
    def default_share_permission(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DefaultSharePermission]]]: ...
    @default_share_permission.setter
    def default_share_permission(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DefaultSharePermission]]],
    ): ...

class BlobInventoryCreationTimeArgsDict(TypedDict):
    last_n_days: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BlobInventoryCreationTimeArgs:
    def __init__(
        __self__, *, last_n_days: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastNDays")
    def last_n_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @last_n_days.setter
    def last_n_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class BlobInventoryPolicyDefinitionArgsDict(TypedDict):
    format: pulumi.Input[Union[_builtins.str, Format]]
    object_type: pulumi.Input[Union[_builtins.str, ObjectType]]
    schedule: pulumi.Input[Union[_builtins.str, Schedule]]
    schema_fields: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    filters: NotRequired[pulumi.Input[BlobInventoryPolicyFilterArgsDict]]

@pulumi.input_type
class BlobInventoryPolicyDefinitionArgs:
    def __init__(
        __self__,
        *,
        format: pulumi.Input[Union[_builtins.str, Format]],
        object_type: pulumi.Input[Union[_builtins.str, ObjectType]],
        schedule: pulumi.Input[Union[_builtins.str, Schedule]],
        schema_fields: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        filters: Optional[pulumi.Input[BlobInventoryPolicyFilterArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[Union[_builtins.str, Format]]: ...
    @format.setter
    def format(self, value: pulumi.Input[Union[_builtins.str, Format]]): ...
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Input[Union[_builtins.str, ObjectType]]: ...
    @object_type.setter
    def object_type(self, value: pulumi.Input[Union[_builtins.str, ObjectType]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[Union[_builtins.str, Schedule]]: ...
    @schedule.setter
    def schedule(self, value: pulumi.Input[Union[_builtins.str, Schedule]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaFields")
    def schema_fields(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @schema_fields.setter
    def schema_fields(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[BlobInventoryPolicyFilterArgs]]: ...
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[BlobInventoryPolicyFilterArgs]]): ...

class BlobInventoryPolicyFilterArgsDict(TypedDict):
    blob_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    creation_time: NotRequired[pulumi.Input[BlobInventoryCreationTimeArgsDict]]
    exclude_prefix: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_blob_versions: NotRequired[pulumi.Input[_builtins.bool]]
    include_deleted: NotRequired[pulumi.Input[_builtins.bool]]
    include_snapshots: NotRequired[pulumi.Input[_builtins.bool]]
    prefix_match: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BlobInventoryPolicyFilterArgs:
    def __init__(
        __self__,
        *,
        blob_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        creation_time: Optional[pulumi.Input[BlobInventoryCreationTimeArgs]] = ...,
        exclude_prefix: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_blob_versions: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_deleted: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_snapshots: Optional[pulumi.Input[_builtins.bool]] = ...,
        prefix_match: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blobTypes")
    def blob_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @blob_types.setter
    def blob_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(
        self,
    ) -> Optional[pulumi.Input[BlobInventoryCreationTimeArgs]]: ...
    @creation_time.setter
    def creation_time(
        self, value: Optional[pulumi.Input[BlobInventoryCreationTimeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludePrefix")
    def exclude_prefix(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_prefix.setter
    def exclude_prefix(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeBlobVersions")
    def include_blob_versions(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_blob_versions.setter
    def include_blob_versions(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeDeleted")
    def include_deleted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_deleted.setter
    def include_deleted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeSnapshots")
    def include_snapshots(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_snapshots.setter
    def include_snapshots(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prefix_match.setter
    def prefix_match(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BlobInventoryPolicyRuleArgsDict(TypedDict):
    definition: pulumi.Input[BlobInventoryPolicyDefinitionArgsDict]
    destination: pulumi.Input[_builtins.str]
    enabled: pulumi.Input[_builtins.bool]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class BlobInventoryPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        definition: pulumi.Input[BlobInventoryPolicyDefinitionArgs],
        destination: pulumi.Input[_builtins.str],
        enabled: pulumi.Input[_builtins.bool],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Input[BlobInventoryPolicyDefinitionArgs]: ...
    @definition.setter
    def definition(self, value: pulumi.Input[BlobInventoryPolicyDefinitionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class BlobInventoryPolicySchemaArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    rules: pulumi.Input[Sequence[pulumi.Input[BlobInventoryPolicyRuleArgsDict]]]
    type: pulumi.Input[Union[_builtins.str, InventoryRuleType]]

@pulumi.input_type
class BlobInventoryPolicySchemaArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        rules: pulumi.Input[Sequence[pulumi.Input[BlobInventoryPolicyRuleArgs]]],
        type: pulumi.Input[Union[_builtins.str, InventoryRuleType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[BlobInventoryPolicyRuleArgs]]]: ...
    @rules.setter
    def rules(
        self, value: pulumi.Input[Sequence[pulumi.Input[BlobInventoryPolicyRuleArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, InventoryRuleType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, InventoryRuleType]]): ...

class ChangeFeedArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    retention_in_days: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChangeFeedArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        retention_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_in_days.setter
    def retention_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CorsRulesArgsDict(TypedDict):
    cors_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[CorsRuleArgsDict]]]]

@pulumi.input_type
class CorsRulesArgs:
    def __init__(
        __self__,
        *,
        cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[CorsRuleArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="corsRules")
    def cors_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CorsRuleArgs]]]]: ...
    @cors_rules.setter
    def cors_rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CorsRuleArgs]]]]
    ): ...

class CorsRuleArgsDict(TypedDict):
    allowed_headers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_methods: pulumi.Input[
        Sequence[pulumi.Input[Union[_builtins.str, AllowedMethods]]]
    ]
    allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    exposed_headers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    max_age_in_seconds: pulumi.Input[_builtins.int]

@pulumi.input_type
class CorsRuleArgs:
    def __init__(
        __self__,
        *,
        allowed_headers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        allowed_methods: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AllowedMethods]]]
        ],
        allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        exposed_headers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        max_age_in_seconds: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @allowed_headers.setter
    def allowed_headers(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AllowedMethods]]]]: ...
    @allowed_methods.setter
    def allowed_methods(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AllowedMethods]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @allowed_origins.setter
    def allowed_origins(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exposedHeaders")
    def exposed_headers(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @exposed_headers.setter
    def exposed_headers(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> pulumi.Input[_builtins.int]: ...
    @max_age_in_seconds.setter
    def max_age_in_seconds(self, value: pulumi.Input[_builtins.int]): ...

class CustomDomainArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    use_sub_domain_name: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class CustomDomainArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        use_sub_domain_name: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="useSubDomainName")
    def use_sub_domain_name(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_sub_domain_name.setter
    def use_sub_domain_name(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DateAfterCreationArgsDict(TypedDict):
    days_after_creation_greater_than: pulumi.Input[_builtins.float]
    days_after_last_tier_change_greater_than: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class DateAfterCreationArgs:
    def __init__(
        __self__,
        *,
        days_after_creation_greater_than: pulumi.Input[_builtins.float],
        days_after_last_tier_change_greater_than: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysAfterCreationGreaterThan")
    def days_after_creation_greater_than(self) -> pulumi.Input[_builtins.float]: ...
    @days_after_creation_greater_than.setter
    def days_after_creation_greater_than(
        self, value: pulumi.Input[_builtins.float]
    ): ...
    @_builtins.property
    @pulumi.getter(name="daysAfterLastTierChangeGreaterThan")
    def days_after_last_tier_change_greater_than(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @days_after_last_tier_change_greater_than.setter
    def days_after_last_tier_change_greater_than(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class DateAfterModificationArgsDict(TypedDict):
    days_after_creation_greater_than: NotRequired[pulumi.Input[_builtins.float]]
    days_after_last_access_time_greater_than: NotRequired[pulumi.Input[_builtins.float]]
    days_after_last_tier_change_greater_than: NotRequired[pulumi.Input[_builtins.float]]
    days_after_modification_greater_than: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class DateAfterModificationArgs:
    def __init__(
        __self__,
        *,
        days_after_creation_greater_than: Optional[pulumi.Input[_builtins.float]] = ...,
        days_after_last_access_time_greater_than: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        days_after_last_tier_change_greater_than: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        days_after_modification_greater_than: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysAfterCreationGreaterThan")
    def days_after_creation_greater_than(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @days_after_creation_greater_than.setter
    def days_after_creation_greater_than(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="daysAfterLastAccessTimeGreaterThan")
    def days_after_last_access_time_greater_than(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @days_after_last_access_time_greater_than.setter
    def days_after_last_access_time_greater_than(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="daysAfterLastTierChangeGreaterThan")
    def days_after_last_tier_change_greater_than(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @days_after_last_tier_change_greater_than.setter
    def days_after_last_tier_change_greater_than(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="daysAfterModificationGreaterThan")
    def days_after_modification_greater_than(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @days_after_modification_greater_than.setter
    def days_after_modification_greater_than(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class DeleteRetentionPolicyArgsDict(TypedDict):
    allow_permanent_delete: NotRequired[pulumi.Input[_builtins.bool]]
    days: NotRequired[pulumi.Input[_builtins.int]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DeleteRetentionPolicyArgs:
    def __init__(
        __self__,
        *,
        allow_permanent_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        days: Optional[pulumi.Input[_builtins.int]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPermanentDelete")
    def allow_permanent_delete(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_permanent_delete.setter
    def allow_permanent_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EncryptionIdentityArgsDict(TypedDict):
    encryption_federated_identity_client_id: NotRequired[pulumi.Input[_builtins.str]]
    encryption_user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EncryptionIdentityArgs:
    def __init__(
        __self__,
        *,
        encryption_federated_identity_client_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        encryption_user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionFederatedIdentityClientId")
    def encryption_federated_identity_client_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_federated_identity_client_id.setter
    def encryption_federated_identity_client_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionUserAssignedIdentity")
    def encryption_user_assigned_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_user_assigned_identity.setter
    def encryption_user_assigned_identity(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class EncryptionScopeKeyVaultPropertiesArgsDict(TypedDict):
    key_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EncryptionScopeKeyVaultPropertiesArgs:
    def __init__(
        __self__, *, key_uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyUri")
    def key_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_uri.setter
    def key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EncryptionServicesArgsDict(TypedDict):
    blob: NotRequired[pulumi.Input[EncryptionServiceArgsDict]]
    file: NotRequired[pulumi.Input[EncryptionServiceArgsDict]]
    queue: NotRequired[pulumi.Input[EncryptionServiceArgsDict]]
    table: NotRequired[pulumi.Input[EncryptionServiceArgsDict]]

@pulumi.input_type
class EncryptionServicesArgs:
    def __init__(
        __self__,
        *,
        blob: Optional[pulumi.Input[EncryptionServiceArgs]] = ...,
        file: Optional[pulumi.Input[EncryptionServiceArgs]] = ...,
        queue: Optional[pulumi.Input[EncryptionServiceArgs]] = ...,
        table: Optional[pulumi.Input[EncryptionServiceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def blob(self) -> Optional[pulumi.Input[EncryptionServiceArgs]]: ...
    @blob.setter
    def blob(self, value: Optional[pulumi.Input[EncryptionServiceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def file(self) -> Optional[pulumi.Input[EncryptionServiceArgs]]: ...
    @file.setter
    def file(self, value: Optional[pulumi.Input[EncryptionServiceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def queue(self) -> Optional[pulumi.Input[EncryptionServiceArgs]]: ...
    @queue.setter
    def queue(self, value: Optional[pulumi.Input[EncryptionServiceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[EncryptionServiceArgs]]: ...
    @table.setter
    def table(self, value: Optional[pulumi.Input[EncryptionServiceArgs]]): ...

class EncryptionServiceArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    key_type: NotRequired[pulumi.Input[Union[_builtins.str, KeyType]]]

@pulumi.input_type
class EncryptionServiceArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_type: Optional[pulumi.Input[Union[_builtins.str, KeyType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> Optional[pulumi.Input[Union[_builtins.str, KeyType]]]: ...
    @key_type.setter
    def key_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, KeyType]]]
    ): ...

class EncryptionArgsDict(TypedDict):
    encryption_identity: NotRequired[pulumi.Input[EncryptionIdentityArgsDict]]
    key_source: NotRequired[pulumi.Input[Union[_builtins.str, KeySource]]]
    key_vault_properties: NotRequired[pulumi.Input[KeyVaultPropertiesArgsDict]]
    require_infrastructure_encryption: NotRequired[pulumi.Input[_builtins.bool]]
    services: NotRequired[pulumi.Input[EncryptionServicesArgsDict]]

@pulumi.input_type
class EncryptionArgs:
    def __init__(
        __self__,
        *,
        encryption_identity: Optional[pulumi.Input[EncryptionIdentityArgs]] = ...,
        key_source: Optional[pulumi.Input[Union[_builtins.str, KeySource]]] = ...,
        key_vault_properties: Optional[pulumi.Input[KeyVaultPropertiesArgs]] = ...,
        require_infrastructure_encryption: Optional[pulumi.Input[_builtins.bool]] = ...,
        services: Optional[pulumi.Input[EncryptionServicesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionIdentity")
    def encryption_identity(self) -> Optional[pulumi.Input[EncryptionIdentityArgs]]: ...
    @encryption_identity.setter
    def encryption_identity(
        self, value: Optional[pulumi.Input[EncryptionIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[pulumi.Input[Union[_builtins.str, KeySource]]]: ...
    @key_source.setter
    def key_source(
        self, value: Optional[pulumi.Input[Union[_builtins.str, KeySource]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(
        self,
    ) -> Optional[pulumi.Input[KeyVaultPropertiesArgs]]: ...
    @key_vault_properties.setter
    def key_vault_properties(
        self, value: Optional[pulumi.Input[KeyVaultPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireInfrastructureEncryption")
    def require_infrastructure_encryption(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_infrastructure_encryption.setter
    def require_infrastructure_encryption(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[EncryptionServicesArgs]]: ...
    @services.setter
    def services(self, value: Optional[pulumi.Input[EncryptionServicesArgs]]): ...

class ExecutionTargetArgsDict(TypedDict):
    exclude_prefix: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    prefix: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ExecutionTargetArgs:
    def __init__(
        __self__,
        *,
        exclude_prefix: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        prefix: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludePrefix")
    def exclude_prefix(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_prefix.setter
    def exclude_prefix(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def prefix(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prefix.setter
    def prefix(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ExecutionTriggerArgsDict(TypedDict):
    parameters: pulumi.Input[TriggerParametersArgsDict]
    type: pulumi.Input[TriggerType]

@pulumi.input_type
class ExecutionTriggerArgs:
    def __init__(
        __self__,
        *,
        parameters: pulumi.Input[TriggerParametersArgs],
        type: pulumi.Input[TriggerType],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[TriggerParametersArgs]: ...
    @parameters.setter
    def parameters(self, value: pulumi.Input[TriggerParametersArgs]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[TriggerType]: ...
    @type.setter
    def type(self, value: pulumi.Input[TriggerType]): ...

class ExtendedLocationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]

@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]
    ): ...

class FileSharePropertiesFileSharePaidBurstingArgsDict(TypedDict):
    paid_bursting_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    paid_bursting_max_bandwidth_mibps: NotRequired[pulumi.Input[_builtins.int]]
    paid_bursting_max_iops: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FileSharePropertiesFileSharePaidBurstingArgs:
    def __init__(
        __self__,
        *,
        paid_bursting_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        paid_bursting_max_bandwidth_mibps: Optional[pulumi.Input[_builtins.int]] = ...,
        paid_bursting_max_iops: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="paidBurstingEnabled")
    def paid_bursting_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @paid_bursting_enabled.setter
    def paid_bursting_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="paidBurstingMaxBandwidthMibps")
    def paid_bursting_max_bandwidth_mibps(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @paid_bursting_max_bandwidth_mibps.setter
    def paid_bursting_max_bandwidth_mibps(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="paidBurstingMaxIops")
    def paid_bursting_max_iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @paid_bursting_max_iops.setter
    def paid_bursting_max_iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class IPRuleArgsDict(TypedDict):
    i_p_address_or_range: pulumi.Input[_builtins.str]
    action: NotRequired[pulumi.Input[Action]]

@pulumi.input_type
class IPRuleArgs:
    def __init__(
        __self__,
        *,
        i_p_address_or_range: pulumi.Input[_builtins.str],
        action: Optional[pulumi.Input[Action]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iPAddressOrRange")
    def i_p_address_or_range(self) -> pulumi.Input[_builtins.str]: ...
    @i_p_address_or_range.setter
    def i_p_address_or_range(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Action]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[Action]]): ...

class IdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, IdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class IdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, IdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, IdentityType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, IdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ImmutableStorageAccountArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    immutability_policy: NotRequired[
        pulumi.Input[AccountImmutabilityPolicyPropertiesArgsDict]
    ]

@pulumi.input_type
class ImmutableStorageAccountArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        immutability_policy: Optional[
            pulumi.Input[AccountImmutabilityPolicyPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="immutabilityPolicy")
    def immutability_policy(
        self,
    ) -> Optional[pulumi.Input[AccountImmutabilityPolicyPropertiesArgs]]: ...
    @immutability_policy.setter
    def immutability_policy(
        self, value: Optional[pulumi.Input[AccountImmutabilityPolicyPropertiesArgs]]
    ): ...

class ImmutableStorageWithVersioningArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ImmutableStorageWithVersioningArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class KeyPolicyArgsDict(TypedDict):
    key_expiration_period_in_days: pulumi.Input[_builtins.int]

@pulumi.input_type
class KeyPolicyArgs:
    def __init__(
        __self__, *, key_expiration_period_in_days: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyExpirationPeriodInDays")
    def key_expiration_period_in_days(self) -> pulumi.Input[_builtins.int]: ...
    @key_expiration_period_in_days.setter
    def key_expiration_period_in_days(self, value: pulumi.Input[_builtins.int]): ...

class KeyVaultPropertiesArgsDict(TypedDict):
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_uri: NotRequired[pulumi.Input[_builtins.str]]
    key_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        key_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LastAccessTimeTrackingPolicyArgsDict(TypedDict):
    enable: pulumi.Input[_builtins.bool]
    blob_type: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[Union[_builtins.str, Name]]]
    tracking_granularity_in_days: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class LastAccessTimeTrackingPolicyArgs:
    def __init__(
        __self__,
        *,
        enable: pulumi.Input[_builtins.bool],
        blob_type: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[Union[_builtins.str, Name]]] = ...,
        tracking_granularity_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> pulumi.Input[_builtins.bool]: ...
    @enable.setter
    def enable(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="blobType")
    def blob_type(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @blob_type.setter
    def blob_type(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, Name]]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, Name]]]): ...
    @_builtins.property
    @pulumi.getter(name="trackingGranularityInDays")
    def tracking_granularity_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tracking_granularity_in_days.setter
    def tracking_granularity_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ManagementPolicyActionArgsDict(TypedDict):
    base_blob: NotRequired[pulumi.Input[ManagementPolicyBaseBlobArgsDict]]
    snapshot: NotRequired[pulumi.Input[ManagementPolicySnapShotArgsDict]]
    version: NotRequired[pulumi.Input[ManagementPolicyVersionArgsDict]]

@pulumi.input_type
class ManagementPolicyActionArgs:
    def __init__(
        __self__,
        *,
        base_blob: Optional[pulumi.Input[ManagementPolicyBaseBlobArgs]] = ...,
        snapshot: Optional[pulumi.Input[ManagementPolicySnapShotArgs]] = ...,
        version: Optional[pulumi.Input[ManagementPolicyVersionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseBlob")
    def base_blob(self) -> Optional[pulumi.Input[ManagementPolicyBaseBlobArgs]]: ...
    @base_blob.setter
    def base_blob(
        self, value: Optional[pulumi.Input[ManagementPolicyBaseBlobArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> Optional[pulumi.Input[ManagementPolicySnapShotArgs]]: ...
    @snapshot.setter
    def snapshot(self, value: Optional[pulumi.Input[ManagementPolicySnapShotArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[ManagementPolicyVersionArgs]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[ManagementPolicyVersionArgs]]): ...

class ManagementPolicyBaseBlobArgsDict(TypedDict):
    delete: NotRequired[pulumi.Input[DateAfterModificationArgsDict]]
    enable_auto_tier_to_hot_from_cool: NotRequired[pulumi.Input[_builtins.bool]]
    tier_to_archive: NotRequired[pulumi.Input[DateAfterModificationArgsDict]]
    tier_to_cold: NotRequired[pulumi.Input[DateAfterModificationArgsDict]]
    tier_to_cool: NotRequired[pulumi.Input[DateAfterModificationArgsDict]]
    tier_to_hot: NotRequired[pulumi.Input[DateAfterModificationArgsDict]]

@pulumi.input_type
class ManagementPolicyBaseBlobArgs:
    def __init__(
        __self__,
        *,
        delete: Optional[pulumi.Input[DateAfterModificationArgs]] = ...,
        enable_auto_tier_to_hot_from_cool: Optional[pulumi.Input[_builtins.bool]] = ...,
        tier_to_archive: Optional[pulumi.Input[DateAfterModificationArgs]] = ...,
        tier_to_cold: Optional[pulumi.Input[DateAfterModificationArgs]] = ...,
        tier_to_cool: Optional[pulumi.Input[DateAfterModificationArgs]] = ...,
        tier_to_hot: Optional[pulumi.Input[DateAfterModificationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[DateAfterModificationArgs]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[DateAfterModificationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAutoTierToHotFromCool")
    def enable_auto_tier_to_hot_from_cool(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_auto_tier_to_hot_from_cool.setter
    def enable_auto_tier_to_hot_from_cool(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tierToArchive")
    def tier_to_archive(self) -> Optional[pulumi.Input[DateAfterModificationArgs]]: ...
    @tier_to_archive.setter
    def tier_to_archive(
        self, value: Optional[pulumi.Input[DateAfterModificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tierToCold")
    def tier_to_cold(self) -> Optional[pulumi.Input[DateAfterModificationArgs]]: ...
    @tier_to_cold.setter
    def tier_to_cold(
        self, value: Optional[pulumi.Input[DateAfterModificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tierToCool")
    def tier_to_cool(self) -> Optional[pulumi.Input[DateAfterModificationArgs]]: ...
    @tier_to_cool.setter
    def tier_to_cool(
        self, value: Optional[pulumi.Input[DateAfterModificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tierToHot")
    def tier_to_hot(self) -> Optional[pulumi.Input[DateAfterModificationArgs]]: ...
    @tier_to_hot.setter
    def tier_to_hot(self, value: Optional[pulumi.Input[DateAfterModificationArgs]]): ...

class ManagementPolicyDefinitionArgsDict(TypedDict):
    actions: pulumi.Input[ManagementPolicyActionArgsDict]
    filters: NotRequired[pulumi.Input[ManagementPolicyFilterArgsDict]]

@pulumi.input_type
class ManagementPolicyDefinitionArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[ManagementPolicyActionArgs],
        filters: Optional[pulumi.Input[ManagementPolicyFilterArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[ManagementPolicyActionArgs]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[ManagementPolicyActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[ManagementPolicyFilterArgs]]: ...
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[ManagementPolicyFilterArgs]]): ...

class ManagementPolicyFilterArgsDict(TypedDict):
    blob_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    blob_index_match: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TagFilterArgsDict]]]
    ]
    prefix_match: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ManagementPolicyFilterArgs:
    def __init__(
        __self__,
        *,
        blob_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        blob_index_match: Optional[
            pulumi.Input[Sequence[pulumi.Input[TagFilterArgs]]]
        ] = ...,
        prefix_match: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blobTypes")
    def blob_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @blob_types.setter
    def blob_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="blobIndexMatch")
    def blob_index_match(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TagFilterArgs]]]]: ...
    @blob_index_match.setter
    def blob_index_match(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TagFilterArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prefix_match.setter
    def prefix_match(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ManagementPolicyRuleArgsDict(TypedDict):
    definition: pulumi.Input[ManagementPolicyDefinitionArgsDict]
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, RuleType]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ManagementPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        definition: pulumi.Input[ManagementPolicyDefinitionArgs],
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, RuleType]],
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Input[ManagementPolicyDefinitionArgs]: ...
    @definition.setter
    def definition(self, value: pulumi.Input[ManagementPolicyDefinitionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, RuleType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, RuleType]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ManagementPolicySchemaArgsDict(TypedDict):
    rules: pulumi.Input[Sequence[pulumi.Input[ManagementPolicyRuleArgsDict]]]

@pulumi.input_type
class ManagementPolicySchemaArgs:
    def __init__(
        __self__,
        *,
        rules: pulumi.Input[Sequence[pulumi.Input[ManagementPolicyRuleArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ManagementPolicyRuleArgs]]]: ...
    @rules.setter
    def rules(
        self, value: pulumi.Input[Sequence[pulumi.Input[ManagementPolicyRuleArgs]]]
    ): ...

class ManagementPolicySnapShotArgsDict(TypedDict):
    delete: NotRequired[pulumi.Input[DateAfterCreationArgsDict]]
    tier_to_archive: NotRequired[pulumi.Input[DateAfterCreationArgsDict]]
    tier_to_cold: NotRequired[pulumi.Input[DateAfterCreationArgsDict]]
    tier_to_cool: NotRequired[pulumi.Input[DateAfterCreationArgsDict]]
    tier_to_hot: NotRequired[pulumi.Input[DateAfterCreationArgsDict]]

@pulumi.input_type
class ManagementPolicySnapShotArgs:
    def __init__(
        __self__,
        *,
        delete: Optional[pulumi.Input[DateAfterCreationArgs]] = ...,
        tier_to_archive: Optional[pulumi.Input[DateAfterCreationArgs]] = ...,
        tier_to_cold: Optional[pulumi.Input[DateAfterCreationArgs]] = ...,
        tier_to_cool: Optional[pulumi.Input[DateAfterCreationArgs]] = ...,
        tier_to_hot: Optional[pulumi.Input[DateAfterCreationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[DateAfterCreationArgs]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[DateAfterCreationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tierToArchive")
    def tier_to_archive(self) -> Optional[pulumi.Input[DateAfterCreationArgs]]: ...
    @tier_to_archive.setter
    def tier_to_archive(self, value: Optional[pulumi.Input[DateAfterCreationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tierToCold")
    def tier_to_cold(self) -> Optional[pulumi.Input[DateAfterCreationArgs]]: ...
    @tier_to_cold.setter
    def tier_to_cold(self, value: Optional[pulumi.Input[DateAfterCreationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tierToCool")
    def tier_to_cool(self) -> Optional[pulumi.Input[DateAfterCreationArgs]]: ...
    @tier_to_cool.setter
    def tier_to_cool(self, value: Optional[pulumi.Input[DateAfterCreationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tierToHot")
    def tier_to_hot(self) -> Optional[pulumi.Input[DateAfterCreationArgs]]: ...
    @tier_to_hot.setter
    def tier_to_hot(self, value: Optional[pulumi.Input[DateAfterCreationArgs]]): ...

class ManagementPolicyVersionArgsDict(TypedDict):
    delete: NotRequired[pulumi.Input[DateAfterCreationArgsDict]]
    tier_to_archive: NotRequired[pulumi.Input[DateAfterCreationArgsDict]]
    tier_to_cold: NotRequired[pulumi.Input[DateAfterCreationArgsDict]]
    tier_to_cool: NotRequired[pulumi.Input[DateAfterCreationArgsDict]]
    tier_to_hot: NotRequired[pulumi.Input[DateAfterCreationArgsDict]]

@pulumi.input_type
class ManagementPolicyVersionArgs:
    def __init__(
        __self__,
        *,
        delete: Optional[pulumi.Input[DateAfterCreationArgs]] = ...,
        tier_to_archive: Optional[pulumi.Input[DateAfterCreationArgs]] = ...,
        tier_to_cold: Optional[pulumi.Input[DateAfterCreationArgs]] = ...,
        tier_to_cool: Optional[pulumi.Input[DateAfterCreationArgs]] = ...,
        tier_to_hot: Optional[pulumi.Input[DateAfterCreationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[DateAfterCreationArgs]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[DateAfterCreationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tierToArchive")
    def tier_to_archive(self) -> Optional[pulumi.Input[DateAfterCreationArgs]]: ...
    @tier_to_archive.setter
    def tier_to_archive(self, value: Optional[pulumi.Input[DateAfterCreationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tierToCold")
    def tier_to_cold(self) -> Optional[pulumi.Input[DateAfterCreationArgs]]: ...
    @tier_to_cold.setter
    def tier_to_cold(self, value: Optional[pulumi.Input[DateAfterCreationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tierToCool")
    def tier_to_cool(self) -> Optional[pulumi.Input[DateAfterCreationArgs]]: ...
    @tier_to_cool.setter
    def tier_to_cool(self, value: Optional[pulumi.Input[DateAfterCreationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tierToHot")
    def tier_to_hot(self) -> Optional[pulumi.Input[DateAfterCreationArgs]]: ...
    @tier_to_hot.setter
    def tier_to_hot(self, value: Optional[pulumi.Input[DateAfterCreationArgs]]): ...

class MultichannelArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class MultichannelArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class NetworkRuleSetArgsDict(TypedDict):
    default_action: pulumi.Input[DefaultAction]
    bypass: NotRequired[pulumi.Input[Union[_builtins.str, Bypass]]]
    ip_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[IPRuleArgsDict]]]]
    resource_access_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceAccessRuleArgsDict]]]
    ]
    virtual_network_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgsDict]]]
    ]

@pulumi.input_type
class NetworkRuleSetArgs:
    def __init__(
        __self__,
        *,
        default_action: Optional[pulumi.Input[DefaultAction]] = ...,
        bypass: Optional[pulumi.Input[Union[_builtins.str, Bypass]]] = ...,
        ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]] = ...,
        resource_access_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceAccessRuleArgs]]]
        ] = ...,
        virtual_network_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Input[DefaultAction]: ...
    @default_action.setter
    def default_action(self, value: pulumi.Input[DefaultAction]): ...
    @_builtins.property
    @pulumi.getter
    def bypass(self) -> Optional[pulumi.Input[Union[_builtins.str, Bypass]]]: ...
    @bypass.setter
    def bypass(self, value: Optional[pulumi.Input[Union[_builtins.str, Bypass]]]): ...
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]]: ...
    @ip_rules.setter
    def ip_rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRules")
    def resource_access_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceAccessRuleArgs]]]]: ...
    @resource_access_rules.setter
    def resource_access_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceAccessRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgs]]]]: ...
    @virtual_network_rules.setter
    def virtual_network_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgs]]]],
    ): ...

class ObjectReplicationPolicyFilterArgsDict(TypedDict):
    min_creation_time: NotRequired[pulumi.Input[_builtins.str]]
    prefix_match: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ObjectReplicationPolicyFilterArgs:
    def __init__(
        __self__,
        *,
        min_creation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix_match: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minCreationTime")
    def min_creation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_creation_time.setter
    def min_creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prefix_match.setter
    def prefix_match(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ObjectReplicationPolicyPropertiesMetricsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ObjectReplicationPolicyPropertiesMetricsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ObjectReplicationPolicyRuleArgsDict(TypedDict):
    destination_container: pulumi.Input[_builtins.str]
    source_container: pulumi.Input[_builtins.str]
    filters: NotRequired[pulumi.Input[ObjectReplicationPolicyFilterArgsDict]]
    rule_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ObjectReplicationPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        destination_container: pulumi.Input[_builtins.str],
        source_container: pulumi.Input[_builtins.str],
        filters: Optional[pulumi.Input[ObjectReplicationPolicyFilterArgs]] = ...,
        rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationContainer")
    def destination_container(self) -> pulumi.Input[_builtins.str]: ...
    @destination_container.setter
    def destination_container(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceContainer")
    def source_container(self) -> pulumi.Input[_builtins.str]: ...
    @source_container.setter
    def source_container(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[ObjectReplicationPolicyFilterArgs]]: ...
    @filters.setter
    def filters(
        self, value: Optional[pulumi.Input[ObjectReplicationPolicyFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PermissionScopeArgsDict(TypedDict):
    permissions: pulumi.Input[_builtins.str]
    resource_name: pulumi.Input[_builtins.str]
    service: pulumi.Input[_builtins.str]

@pulumi.input_type
class PermissionScopeArgs:
    def __init__(
        __self__,
        *,
        permissions: pulumi.Input[_builtins.str],
        resource_name: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[_builtins.str]: ...
    @permissions.setter
    def permissions(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    action_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        action_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionRequired")
    def action_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_required.setter
    def action_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

class ProtocolSettingsArgsDict(TypedDict):
    smb: NotRequired[pulumi.Input[SmbSettingArgsDict]]

@pulumi.input_type
class ProtocolSettingsArgs:
    def __init__(
        __self__, *, smb: Optional[pulumi.Input[SmbSettingArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def smb(self) -> Optional[pulumi.Input[SmbSettingArgs]]: ...
    @smb.setter
    def smb(self, value: Optional[pulumi.Input[SmbSettingArgs]]): ...

class ResourceAccessRuleArgsDict(TypedDict):
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceAccessRuleArgs:
    def __init__(
        __self__,
        *,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestorePolicyPropertiesArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    days: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RestorePolicyPropertiesArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RoutingPreferenceArgsDict(TypedDict):
    publish_internet_endpoints: NotRequired[pulumi.Input[_builtins.bool]]
    publish_microsoft_endpoints: NotRequired[pulumi.Input[_builtins.bool]]
    routing_choice: NotRequired[pulumi.Input[Union[_builtins.str, RoutingChoice]]]

@pulumi.input_type
class RoutingPreferenceArgs:
    def __init__(
        __self__,
        *,
        publish_internet_endpoints: Optional[pulumi.Input[_builtins.bool]] = ...,
        publish_microsoft_endpoints: Optional[pulumi.Input[_builtins.bool]] = ...,
        routing_choice: Optional[
            pulumi.Input[Union[_builtins.str, RoutingChoice]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publishInternetEndpoints")
    def publish_internet_endpoints(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publish_internet_endpoints.setter
    def publish_internet_endpoints(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishMicrosoftEndpoints")
    def publish_microsoft_endpoints(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publish_microsoft_endpoints.setter
    def publish_microsoft_endpoints(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingChoice")
    def routing_choice(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RoutingChoice]]]: ...
    @routing_choice.setter
    def routing_choice(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RoutingChoice]]]
    ): ...

class SasPolicyArgsDict(TypedDict):
    expiration_action: pulumi.Input[Union[_builtins.str, ExpirationAction]]
    sas_expiration_period: pulumi.Input[_builtins.str]

@pulumi.input_type
class SasPolicyArgs:
    def __init__(
        __self__,
        *,
        expiration_action: Optional[
            pulumi.Input[Union[_builtins.str, ExpirationAction]]
        ] = ...,
        sas_expiration_period: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expirationAction")
    def expiration_action(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ExpirationAction]]: ...
    @expiration_action.setter
    def expiration_action(
        self, value: pulumi.Input[Union[_builtins.str, ExpirationAction]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sasExpirationPeriod")
    def sas_expiration_period(self) -> pulumi.Input[_builtins.str]: ...
    @sas_expiration_period.setter
    def sas_expiration_period(self, value: pulumi.Input[_builtins.str]): ...

class SignedIdentifierArgsDict(TypedDict):
    access_policy: NotRequired[pulumi.Input[AccessPolicyArgsDict]]
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SignedIdentifierArgs:
    def __init__(
        __self__,
        *,
        access_policy: Optional[pulumi.Input[AccessPolicyArgs]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicy")
    def access_policy(self) -> Optional[pulumi.Input[AccessPolicyArgs]]: ...
    @access_policy.setter
    def access_policy(self, value: Optional[pulumi.Input[AccessPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, SkuName]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__, *, name: pulumi.Input[Union[_builtins.str, SkuName]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): ...

class SmbSettingArgsDict(TypedDict):
    authentication_methods: NotRequired[pulumi.Input[_builtins.str]]
    channel_encryption: NotRequired[pulumi.Input[_builtins.str]]
    kerberos_ticket_encryption: NotRequired[pulumi.Input[_builtins.str]]
    multichannel: NotRequired[pulumi.Input[MultichannelArgsDict]]
    versions: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SmbSettingArgs:
    def __init__(
        __self__,
        *,
        authentication_methods: Optional[pulumi.Input[_builtins.str]] = ...,
        channel_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_ticket_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        multichannel: Optional[pulumi.Input[MultichannelArgs]] = ...,
        versions: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMethods")
    def authentication_methods(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_methods.setter
    def authentication_methods(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="channelEncryption")
    def channel_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel_encryption.setter
    def channel_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosTicketEncryption")
    def kerberos_ticket_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_ticket_encryption.setter
    def kerberos_ticket_encryption(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def multichannel(self) -> Optional[pulumi.Input[MultichannelArgs]]: ...
    @multichannel.setter
    def multichannel(self, value: Optional[pulumi.Input[MultichannelArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @versions.setter
    def versions(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SshPublicKeyArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SshPublicKeyArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageTaskAssignmentExecutionContextArgsDict(TypedDict):
    trigger: pulumi.Input[ExecutionTriggerArgsDict]
    target: NotRequired[pulumi.Input[ExecutionTargetArgsDict]]

@pulumi.input_type
class StorageTaskAssignmentExecutionContextArgs:
    def __init__(
        __self__,
        *,
        trigger: pulumi.Input[ExecutionTriggerArgs],
        target: Optional[pulumi.Input[ExecutionTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> pulumi.Input[ExecutionTriggerArgs]: ...
    @trigger.setter
    def trigger(self, value: pulumi.Input[ExecutionTriggerArgs]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[ExecutionTargetArgs]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[ExecutionTargetArgs]]): ...

class StorageTaskAssignmentPropertiesArgsDict(TypedDict):
    description: pulumi.Input[_builtins.str]
    enabled: pulumi.Input[_builtins.bool]
    execution_context: pulumi.Input[StorageTaskAssignmentExecutionContextArgsDict]
    report: pulumi.Input[StorageTaskAssignmentReportArgsDict]
    task_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class StorageTaskAssignmentPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        enabled: pulumi.Input[_builtins.bool],
        execution_context: pulumi.Input[StorageTaskAssignmentExecutionContextArgs],
        report: pulumi.Input[StorageTaskAssignmentReportArgs],
        task_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="executionContext")
    def execution_context(
        self,
    ) -> pulumi.Input[StorageTaskAssignmentExecutionContextArgs]: ...
    @execution_context.setter
    def execution_context(
        self, value: pulumi.Input[StorageTaskAssignmentExecutionContextArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def report(self) -> pulumi.Input[StorageTaskAssignmentReportArgs]: ...
    @report.setter
    def report(self, value: pulumi.Input[StorageTaskAssignmentReportArgs]): ...
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> pulumi.Input[_builtins.str]: ...
    @task_id.setter
    def task_id(self, value: pulumi.Input[_builtins.str]): ...

class StorageTaskAssignmentReportArgsDict(TypedDict):
    prefix: pulumi.Input[_builtins.str]

@pulumi.input_type
class StorageTaskAssignmentReportArgs:
    def __init__(__self__, *, prefix: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]: ...
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): ...

class TableAccessPolicyArgsDict(TypedDict):
    permission: pulumi.Input[_builtins.str]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableAccessPolicyArgs:
    def __init__(
        __self__,
        *,
        permission: pulumi.Input[_builtins.str],
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> pulumi.Input[_builtins.str]: ...
    @permission.setter
    def permission(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableSignedIdentifierArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    access_policy: NotRequired[pulumi.Input[TableAccessPolicyArgsDict]]

@pulumi.input_type
class TableSignedIdentifierArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        access_policy: Optional[pulumi.Input[TableAccessPolicyArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessPolicy")
    def access_policy(self) -> Optional[pulumi.Input[TableAccessPolicyArgs]]: ...
    @access_policy.setter
    def access_policy(self, value: Optional[pulumi.Input[TableAccessPolicyArgs]]): ...

class TagFilterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    op: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TagFilterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        op: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def op(self) -> pulumi.Input[_builtins.str]: ...
    @op.setter
    def op(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class TriggerParametersArgsDict(TypedDict):
    end_by: NotRequired[pulumi.Input[_builtins.str]]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    interval_unit: NotRequired[pulumi.Input[IntervalUnit]]
    start_from: NotRequired[pulumi.Input[_builtins.str]]
    start_on: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TriggerParametersArgs:
    def __init__(
        __self__,
        *,
        end_by: Optional[pulumi.Input[_builtins.str]] = ...,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        interval_unit: Optional[pulumi.Input[IntervalUnit]] = ...,
        start_from: Optional[pulumi.Input[_builtins.str]] = ...,
        start_on: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endBy")
    def end_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_by.setter
    def end_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[pulumi.Input[IntervalUnit]]: ...
    @interval_unit.setter
    def interval_unit(self, value: Optional[pulumi.Input[IntervalUnit]]): ...
    @_builtins.property
    @pulumi.getter(name="startFrom")
    def start_from(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_from.setter
    def start_from(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startOn")
    def start_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_on.setter
    def start_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworkRuleArgsDict(TypedDict):
    virtual_network_resource_id: pulumi.Input[_builtins.str]
    action: NotRequired[pulumi.Input[Action]]
    state: NotRequired[pulumi.Input[Union[_builtins.str, State]]]

@pulumi.input_type
class VirtualNetworkRuleArgs:
    def __init__(
        __self__,
        *,
        virtual_network_resource_id: pulumi.Input[_builtins.str],
        action: Optional[pulumi.Input[Action]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, State]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkResourceId")
    def virtual_network_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_network_resource_id.setter
    def virtual_network_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Action]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[Action]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, State]]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, State]]]): ...
