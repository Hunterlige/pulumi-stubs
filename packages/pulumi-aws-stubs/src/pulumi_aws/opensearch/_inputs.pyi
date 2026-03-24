import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationAppConfigArgs",
    "ApplicationAppConfigArgsDict",
    "ApplicationDataSourceArgs",
    "ApplicationDataSourceArgsDict",
    "ApplicationIamIdentityCenterOptionsArgs",
    "ApplicationIamIdentityCenterOptionsArgsDict",
    "ApplicationTimeoutsArgs",
    "ApplicationTimeoutsArgsDict",
    "AuthorizeVpcEndpointAccessAuthorizedPrincipalArgs",
    ...,
    "DomainAdvancedSecurityOptionsArgs",
    "DomainAdvancedSecurityOptionsArgsDict",
    "DomainAdvancedSecurityOptionsJwtOptionsArgs",
    "DomainAdvancedSecurityOptionsJwtOptionsArgsDict",
    "DomainAdvancedSecurityOptionsMasterUserOptionsArgs",
    ...,
    "DomainAimlOptionsArgs",
    "DomainAimlOptionsArgsDict",
    ...,
    ...,
    "DomainAimlOptionsS3VectorsEngineArgs",
    "DomainAimlOptionsS3VectorsEngineArgsDict",
    "DomainAimlOptionsServerlessVectorAccelerationArgs",
    ...,
    "DomainAutoTuneOptionsArgs",
    "DomainAutoTuneOptionsArgsDict",
    "DomainAutoTuneOptionsMaintenanceScheduleArgs",
    "DomainAutoTuneOptionsMaintenanceScheduleArgsDict",
    ...,
    ...,
    "DomainClusterConfigArgs",
    "DomainClusterConfigArgsDict",
    "DomainClusterConfigColdStorageOptionsArgs",
    "DomainClusterConfigColdStorageOptionsArgsDict",
    "DomainClusterConfigNodeOptionArgs",
    "DomainClusterConfigNodeOptionArgsDict",
    "DomainClusterConfigNodeOptionNodeConfigArgs",
    "DomainClusterConfigNodeOptionNodeConfigArgsDict",
    "DomainClusterConfigZoneAwarenessConfigArgs",
    "DomainClusterConfigZoneAwarenessConfigArgsDict",
    "DomainCognitoOptionsArgs",
    "DomainCognitoOptionsArgsDict",
    "DomainDomainEndpointOptionsArgs",
    "DomainDomainEndpointOptionsArgsDict",
    "DomainEbsOptionsArgs",
    "DomainEbsOptionsArgsDict",
    "DomainEncryptAtRestArgs",
    "DomainEncryptAtRestArgsDict",
    "DomainIdentityCenterOptionsArgs",
    "DomainIdentityCenterOptionsArgsDict",
    "DomainLogPublishingOptionArgs",
    "DomainLogPublishingOptionArgsDict",
    "DomainNodeToNodeEncryptionArgs",
    "DomainNodeToNodeEncryptionArgsDict",
    "DomainOffPeakWindowOptionsArgs",
    "DomainOffPeakWindowOptionsArgsDict",
    "DomainOffPeakWindowOptionsOffPeakWindowArgs",
    "DomainOffPeakWindowOptionsOffPeakWindowArgsDict",
    ...,
    ...,
    "DomainSamlOptionsSamlOptionsArgs",
    "DomainSamlOptionsSamlOptionsArgsDict",
    "DomainSamlOptionsSamlOptionsIdpArgs",
    "DomainSamlOptionsSamlOptionsIdpArgsDict",
    "DomainSnapshotOptionsArgs",
    "DomainSnapshotOptionsArgsDict",
    "DomainSoftwareUpdateOptionsArgs",
    "DomainSoftwareUpdateOptionsArgsDict",
    "DomainVpcOptionsArgs",
    "DomainVpcOptionsArgsDict",
    "OutboundConnectionConnectionPropertiesArgs",
    "OutboundConnectionConnectionPropertiesArgsDict",
    ...,
    ...,
    "OutboundConnectionLocalDomainInfoArgs",
    "OutboundConnectionLocalDomainInfoArgsDict",
    "OutboundConnectionRemoteDomainInfoArgs",
    "OutboundConnectionRemoteDomainInfoArgsDict",
    "PackagePackageSourceArgs",
    "PackagePackageSourceArgsDict",
    "ServerlessCollectionTimeoutsArgs",
    "ServerlessCollectionTimeoutsArgsDict",
    "ServerlessSecurityConfigSamlOptionsArgs",
    "ServerlessSecurityConfigSamlOptionsArgsDict",
    "ServerlessVpcEndpointTimeoutsArgs",
    "ServerlessVpcEndpointTimeoutsArgsDict",
    "VpcEndpointVpcOptionsArgs",
    "VpcEndpointVpcOptionsArgsDict",
    "GetServerlessSecurityConfigSamlOptionArgs",
    "GetServerlessSecurityConfigSamlOptionArgsDict",
]

class ApplicationAppConfigArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApplicationAppConfigArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationDataSourceArgsDict(TypedDict):
    data_source_arn: NotRequired[pulumi.Input[_builtins.str]]
    data_source_description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApplicationDataSourceArgs:
    def __init__(
        __self__,
        *,
        data_source_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        data_source_description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_source_arn.setter
    def data_source_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSourceDescription")
    def data_source_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_source_description.setter
    def data_source_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationIamIdentityCenterOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    iam_identity_center_application_arn: NotRequired[pulumi.Input[_builtins.str]]
    iam_identity_center_instance_arn: NotRequired[pulumi.Input[_builtins.str]]
    iam_role_for_identity_center_application_arn: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    ...

@pulumi.input_type
class ApplicationIamIdentityCenterOptionsArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        iam_identity_center_application_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        iam_identity_center_instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_role_for_identity_center_application_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="iamIdentityCenterApplicationArn")
    def iam_identity_center_application_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_identity_center_application_arn.setter
    def iam_identity_center_application_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamIdentityCenterInstanceArn")
    def iam_identity_center_instance_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_identity_center_instance_arn.setter
    def iam_identity_center_instance_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamRoleForIdentityCenterApplicationArn")
    def iam_role_for_identity_center_application_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_role_for_identity_center_application_arn.setter
    def iam_role_for_identity_center_application_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ApplicationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApplicationTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthorizeVpcEndpointAccessAuthorizedPrincipalArgsDict(TypedDict):
    principal: pulumi.Input[_builtins.str]
    principal_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AuthorizeVpcEndpointAccessAuthorizedPrincipalArgs:
    def __init__(
        __self__,
        *,
        principal: pulumi.Input[_builtins.str],
        principal_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Input[_builtins.str]: ...
    @principal_type.setter
    def principal_type(self, value: pulumi.Input[_builtins.str]): ...

class DomainAdvancedSecurityOptionsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    anonymous_auth_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    internal_user_database_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    jwt_options: NotRequired[
        pulumi.Input[DomainAdvancedSecurityOptionsJwtOptionsArgsDict]
    ]
    master_user_options: NotRequired[
        pulumi.Input[DomainAdvancedSecurityOptionsMasterUserOptionsArgsDict]
    ]
    ...

@pulumi.input_type
class DomainAdvancedSecurityOptionsArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        anonymous_auth_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        internal_user_database_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        jwt_options: Optional[
            pulumi.Input[DomainAdvancedSecurityOptionsJwtOptionsArgs]
        ] = ...,
        master_user_options: Optional[
            pulumi.Input[DomainAdvancedSecurityOptionsMasterUserOptionsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="anonymousAuthEnabled")
    def anonymous_auth_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @anonymous_auth_enabled.setter
    def anonymous_auth_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="internalUserDatabaseEnabled")
    def internal_user_database_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @internal_user_database_enabled.setter
    def internal_user_database_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jwtOptions")
    def jwt_options(
        self,
    ) -> Optional[pulumi.Input[DomainAdvancedSecurityOptionsJwtOptionsArgs]]: ...
    @jwt_options.setter
    def jwt_options(
        self, value: Optional[pulumi.Input[DomainAdvancedSecurityOptionsJwtOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterUserOptions")
    def master_user_options(
        self,
    ) -> Optional[pulumi.Input[DomainAdvancedSecurityOptionsMasterUserOptionsArgs]]: ...
    @master_user_options.setter
    def master_user_options(
        self,
        value: Optional[
            pulumi.Input[DomainAdvancedSecurityOptionsMasterUserOptionsArgs]
        ],
    ): ...

class DomainAdvancedSecurityOptionsJwtOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    public_key: NotRequired[pulumi.Input[_builtins.str]]
    roles_key: NotRequired[pulumi.Input[_builtins.str]]
    subject_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainAdvancedSecurityOptionsJwtOptionsArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        roles_key: Optional[pulumi.Input[_builtins.str]] = ...,
        subject_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rolesKey")
    def roles_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @roles_key.setter
    def roles_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subjectKey")
    def subject_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subject_key.setter
    def subject_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainAdvancedSecurityOptionsMasterUserOptionsArgsDict(TypedDict):
    master_user_arn: NotRequired[pulumi.Input[_builtins.str]]
    master_user_name: NotRequired[pulumi.Input[_builtins.str]]
    master_user_password: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainAdvancedSecurityOptionsMasterUserOptionsArgs:
    def __init__(
        __self__,
        *,
        master_user_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        master_user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        master_user_password: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="masterUserArn")
    def master_user_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_user_arn.setter
    def master_user_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterUserName")
    def master_user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_user_name.setter
    def master_user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterUserPassword")
    def master_user_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_user_password.setter
    def master_user_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainAimlOptionsArgsDict(TypedDict):
    natural_language_query_generation_options: NotRequired[
        pulumi.Input[DomainAimlOptionsNaturalLanguageQueryGenerationOptionsArgsDict]
    ]
    s3_vectors_engine: NotRequired[
        pulumi.Input[DomainAimlOptionsS3VectorsEngineArgsDict]
    ]
    serverless_vector_acceleration: NotRequired[
        pulumi.Input[DomainAimlOptionsServerlessVectorAccelerationArgsDict]
    ]
    ...

@pulumi.input_type
class DomainAimlOptionsArgs:
    def __init__(
        __self__,
        *,
        natural_language_query_generation_options: Optional[
            pulumi.Input[DomainAimlOptionsNaturalLanguageQueryGenerationOptionsArgs]
        ] = ...,
        s3_vectors_engine: Optional[
            pulumi.Input[DomainAimlOptionsS3VectorsEngineArgs]
        ] = ...,
        serverless_vector_acceleration: Optional[
            pulumi.Input[DomainAimlOptionsServerlessVectorAccelerationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="naturalLanguageQueryGenerationOptions")
    def natural_language_query_generation_options(
        self,
    ) -> Optional[
        pulumi.Input[DomainAimlOptionsNaturalLanguageQueryGenerationOptionsArgs]
    ]: ...
    @natural_language_query_generation_options.setter
    def natural_language_query_generation_options(
        self,
        value: Optional[
            pulumi.Input[DomainAimlOptionsNaturalLanguageQueryGenerationOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3VectorsEngine")
    def s3_vectors_engine(
        self,
    ) -> Optional[pulumi.Input[DomainAimlOptionsS3VectorsEngineArgs]]: ...
    @s3_vectors_engine.setter
    def s3_vectors_engine(
        self, value: Optional[pulumi.Input[DomainAimlOptionsS3VectorsEngineArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverlessVectorAcceleration")
    def serverless_vector_acceleration(
        self,
    ) -> Optional[pulumi.Input[DomainAimlOptionsServerlessVectorAccelerationArgs]]: ...
    @serverless_vector_acceleration.setter
    def serverless_vector_acceleration(
        self,
        value: Optional[
            pulumi.Input[DomainAimlOptionsServerlessVectorAccelerationArgs]
        ],
    ): ...

class DomainAimlOptionsNaturalLanguageQueryGenerationOptionsArgsDict(TypedDict):
    desired_state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainAimlOptionsNaturalLanguageQueryGenerationOptionsArgs:
    def __init__(
        __self__, *, desired_state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainAimlOptionsS3VectorsEngineArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DomainAimlOptionsS3VectorsEngineArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DomainAimlOptionsServerlessVectorAccelerationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DomainAimlOptionsServerlessVectorAccelerationArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DomainAutoTuneOptionsArgsDict(TypedDict):
    desired_state: pulumi.Input[_builtins.str]
    maintenance_schedules: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleArgsDict]]
        ]
    ]
    rollback_on_disable: NotRequired[pulumi.Input[_builtins.str]]
    use_off_peak_window: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DomainAutoTuneOptionsArgs:
    def __init__(
        __self__,
        *,
        desired_state: pulumi.Input[_builtins.str],
        maintenance_schedules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleArgs]]
            ]
        ] = ...,
        rollback_on_disable: Optional[pulumi.Input[_builtins.str]] = ...,
        use_off_peak_window: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Input[_builtins.str]: ...
    @desired_state.setter
    def desired_state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleArgs]]
        ]
    ]: ...
    @maintenance_schedules.setter
    def maintenance_schedules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rollbackOnDisable")
    def rollback_on_disable(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollback_on_disable.setter
    def rollback_on_disable(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useOffPeakWindow")
    def use_off_peak_window(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_off_peak_window.setter
    def use_off_peak_window(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DomainAutoTuneOptionsMaintenanceScheduleArgsDict(TypedDict):
    cron_expression_for_recurrence: pulumi.Input[_builtins.str]
    duration: pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleDurationArgsDict]
    start_at: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DomainAutoTuneOptionsMaintenanceScheduleArgs:
    def __init__(
        __self__,
        *,
        cron_expression_for_recurrence: pulumi.Input[_builtins.str],
        duration: pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleDurationArgs],
        start_at: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cronExpressionForRecurrence")
    def cron_expression_for_recurrence(self) -> pulumi.Input[_builtins.str]: ...
    @cron_expression_for_recurrence.setter
    def cron_expression_for_recurrence(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def duration(
        self,
    ) -> pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleDurationArgs]: ...
    @duration.setter
    def duration(
        self, value: pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleDurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> pulumi.Input[_builtins.str]: ...
    @start_at.setter
    def start_at(self, value: pulumi.Input[_builtins.str]): ...

class DomainAutoTuneOptionsMaintenanceScheduleDurationArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DomainAutoTuneOptionsMaintenanceScheduleDurationArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class DomainClusterConfigArgsDict(TypedDict):
    cold_storage_options: NotRequired[
        pulumi.Input[DomainClusterConfigColdStorageOptionsArgsDict]
    ]
    dedicated_master_count: NotRequired[pulumi.Input[_builtins.int]]
    dedicated_master_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    dedicated_master_type: NotRequired[pulumi.Input[_builtins.str]]
    instance_count: NotRequired[pulumi.Input[_builtins.int]]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    multi_az_with_standby_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    node_options: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DomainClusterConfigNodeOptionArgsDict]]]
    ]
    warm_count: NotRequired[pulumi.Input[_builtins.int]]
    warm_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    warm_type: NotRequired[pulumi.Input[_builtins.str]]
    zone_awareness_config: NotRequired[
        pulumi.Input[DomainClusterConfigZoneAwarenessConfigArgsDict]
    ]
    zone_awareness_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DomainClusterConfigArgs:
    def __init__(
        __self__,
        *,
        cold_storage_options: Optional[
            pulumi.Input[DomainClusterConfigColdStorageOptionsArgs]
        ] = ...,
        dedicated_master_count: Optional[pulumi.Input[_builtins.int]] = ...,
        dedicated_master_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        dedicated_master_type: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az_with_standby_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        node_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[DomainClusterConfigNodeOptionArgs]]]
        ] = ...,
        warm_count: Optional[pulumi.Input[_builtins.int]] = ...,
        warm_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        warm_type: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_awareness_config: Optional[
            pulumi.Input[DomainClusterConfigZoneAwarenessConfigArgs]
        ] = ...,
        zone_awareness_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coldStorageOptions")
    def cold_storage_options(
        self,
    ) -> Optional[pulumi.Input[DomainClusterConfigColdStorageOptionsArgs]]: ...
    @cold_storage_options.setter
    def cold_storage_options(
        self, value: Optional[pulumi.Input[DomainClusterConfigColdStorageOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterCount")
    def dedicated_master_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @dedicated_master_count.setter
    def dedicated_master_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterEnabled")
    def dedicated_master_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dedicated_master_enabled.setter
    def dedicated_master_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterType")
    def dedicated_master_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dedicated_master_type.setter
    def dedicated_master_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiAzWithStandbyEnabled")
    def multi_az_with_standby_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_az_with_standby_enabled.setter
    def multi_az_with_standby_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeOptions")
    def node_options(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DomainClusterConfigNodeOptionArgs]]]
    ]: ...
    @node_options.setter
    def node_options(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DomainClusterConfigNodeOptionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="warmCount")
    def warm_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @warm_count.setter
    def warm_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="warmEnabled")
    def warm_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @warm_enabled.setter
    def warm_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="warmType")
    def warm_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @warm_type.setter
    def warm_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="zoneAwarenessConfig")
    def zone_awareness_config(
        self,
    ) -> Optional[pulumi.Input[DomainClusterConfigZoneAwarenessConfigArgs]]: ...
    @zone_awareness_config.setter
    def zone_awareness_config(
        self, value: Optional[pulumi.Input[DomainClusterConfigZoneAwarenessConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="zoneAwarenessEnabled")
    def zone_awareness_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @zone_awareness_enabled.setter
    def zone_awareness_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DomainClusterConfigColdStorageOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DomainClusterConfigColdStorageOptionsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DomainClusterConfigNodeOptionArgsDict(TypedDict):
    node_config: NotRequired[
        pulumi.Input[DomainClusterConfigNodeOptionNodeConfigArgsDict]
    ]
    node_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainClusterConfigNodeOptionArgs:
    def __init__(
        __self__,
        *,
        node_config: Optional[
            pulumi.Input[DomainClusterConfigNodeOptionNodeConfigArgs]
        ] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(
        self,
    ) -> Optional[pulumi.Input[DomainClusterConfigNodeOptionNodeConfigArgs]]: ...
    @node_config.setter
    def node_config(
        self, value: Optional[pulumi.Input[DomainClusterConfigNodeOptionNodeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainClusterConfigNodeOptionNodeConfigArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainClusterConfigNodeOptionNodeConfigArgs:
    def __init__(
        __self__,
        *,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainClusterConfigZoneAwarenessConfigArgsDict(TypedDict):
    availability_zone_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class DomainClusterConfigZoneAwarenessConfigArgs:
    def __init__(
        __self__,
        *,
        availability_zone_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneCount")
    def availability_zone_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @availability_zone_count.setter
    def availability_zone_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DomainCognitoOptionsArgsDict(TypedDict):
    identity_pool_id: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    user_pool_id: pulumi.Input[_builtins.str]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DomainCognitoOptionsArgs:
    def __init__(
        __self__,
        *,
        identity_pool_id: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        user_pool_id: pulumi.Input[_builtins.str],
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @identity_pool_id.setter
    def identity_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DomainDomainEndpointOptionsArgsDict(TypedDict):
    custom_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    custom_endpoint_certificate_arn: NotRequired[pulumi.Input[_builtins.str]]
    custom_endpoint_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    enforce_https: NotRequired[pulumi.Input[_builtins.bool]]
    tls_security_policy: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainDomainEndpointOptionsArgs:
    def __init__(
        __self__,
        *,
        custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_endpoint_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_endpoint_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        enforce_https: Optional[pulumi.Input[_builtins.bool]] = ...,
        tls_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customEndpoint")
    def custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_endpoint.setter
    def custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customEndpointCertificateArn")
    def custom_endpoint_certificate_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_endpoint_certificate_arn.setter
    def custom_endpoint_certificate_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customEndpointEnabled")
    def custom_endpoint_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @custom_endpoint_enabled.setter
    def custom_endpoint_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enforceHttps")
    def enforce_https(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce_https.setter
    def enforce_https(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsSecurityPolicy")
    def tls_security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tls_security_policy.setter
    def tls_security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainEbsOptionsArgsDict(TypedDict):
    ebs_enabled: pulumi.Input[_builtins.bool]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainEbsOptionsArgs:
    def __init__(
        __self__,
        *,
        ebs_enabled: pulumi.Input[_builtins.bool],
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsEnabled")
    def ebs_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @ebs_enabled.setter
    def ebs_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainEncryptAtRestArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainEncryptAtRestArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainIdentityCenterOptionsArgsDict(TypedDict):
    enabled_api_access: NotRequired[pulumi.Input[_builtins.bool]]
    identity_center_instance_arn: NotRequired[pulumi.Input[_builtins.str]]
    roles_key: NotRequired[pulumi.Input[_builtins.str]]
    subject_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainIdentityCenterOptionsArgs:
    def __init__(
        __self__,
        *,
        enabled_api_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        identity_center_instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        roles_key: Optional[pulumi.Input[_builtins.str]] = ...,
        subject_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledApiAccess")
    def enabled_api_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled_api_access.setter
    def enabled_api_access(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="identityCenterInstanceArn")
    def identity_center_instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_center_instance_arn.setter
    def identity_center_instance_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rolesKey")
    def roles_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @roles_key.setter
    def roles_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subjectKey")
    def subject_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subject_key.setter
    def subject_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainLogPublishingOptionArgsDict(TypedDict):
    cloudwatch_log_group_arn: pulumi.Input[_builtins.str]
    log_type: pulumi.Input[_builtins.str]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DomainLogPublishingOptionArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_log_group_arn: pulumi.Input[_builtins.str],
        log_type: pulumi.Input[_builtins.str],
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> pulumi.Input[_builtins.str]: ...
    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> pulumi.Input[_builtins.str]: ...
    @log_type.setter
    def log_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DomainNodeToNodeEncryptionArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class DomainNodeToNodeEncryptionArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class DomainOffPeakWindowOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    off_peak_window: NotRequired[
        pulumi.Input[DomainOffPeakWindowOptionsOffPeakWindowArgsDict]
    ]
    ...

@pulumi.input_type
class DomainOffPeakWindowOptionsArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        off_peak_window: Optional[
            pulumi.Input[DomainOffPeakWindowOptionsOffPeakWindowArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="offPeakWindow")
    def off_peak_window(
        self,
    ) -> Optional[pulumi.Input[DomainOffPeakWindowOptionsOffPeakWindowArgs]]: ...
    @off_peak_window.setter
    def off_peak_window(
        self, value: Optional[pulumi.Input[DomainOffPeakWindowOptionsOffPeakWindowArgs]]
    ): ...

class DomainOffPeakWindowOptionsOffPeakWindowArgsDict(TypedDict):
    window_start_time: NotRequired[
        pulumi.Input[DomainOffPeakWindowOptionsOffPeakWindowWindowStartTimeArgsDict]
    ]
    ...

@pulumi.input_type
class DomainOffPeakWindowOptionsOffPeakWindowArgs:
    def __init__(
        __self__,
        *,
        window_start_time: Optional[
            pulumi.Input[DomainOffPeakWindowOptionsOffPeakWindowWindowStartTimeArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="windowStartTime")
    def window_start_time(
        self,
    ) -> Optional[
        pulumi.Input[DomainOffPeakWindowOptionsOffPeakWindowWindowStartTimeArgs]
    ]: ...
    @window_start_time.setter
    def window_start_time(
        self,
        value: Optional[
            pulumi.Input[DomainOffPeakWindowOptionsOffPeakWindowWindowStartTimeArgs]
        ],
    ): ...

class DomainOffPeakWindowOptionsOffPeakWindowWindowStartTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class DomainOffPeakWindowOptionsOffPeakWindowWindowStartTimeArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
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

class DomainSamlOptionsSamlOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    idp: NotRequired[pulumi.Input[DomainSamlOptionsSamlOptionsIdpArgsDict]]
    master_backend_role: NotRequired[pulumi.Input[_builtins.str]]
    master_user_name: NotRequired[pulumi.Input[_builtins.str]]
    roles_key: NotRequired[pulumi.Input[_builtins.str]]
    session_timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    subject_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainSamlOptionsSamlOptionsArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        idp: Optional[pulumi.Input[DomainSamlOptionsSamlOptionsIdpArgs]] = ...,
        master_backend_role: Optional[pulumi.Input[_builtins.str]] = ...,
        master_user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        roles_key: Optional[pulumi.Input[_builtins.str]] = ...,
        session_timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        subject_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def idp(self) -> Optional[pulumi.Input[DomainSamlOptionsSamlOptionsIdpArgs]]: ...
    @idp.setter
    def idp(
        self, value: Optional[pulumi.Input[DomainSamlOptionsSamlOptionsIdpArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterBackendRole")
    def master_backend_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_backend_role.setter
    def master_backend_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterUserName")
    def master_user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_user_name.setter
    def master_user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rolesKey")
    def roles_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @roles_key.setter
    def roles_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeoutMinutes")
    def session_timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @session_timeout_minutes.setter
    def session_timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="subjectKey")
    def subject_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subject_key.setter
    def subject_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainSamlOptionsSamlOptionsIdpArgsDict(TypedDict):
    entity_id: pulumi.Input[_builtins.str]
    metadata_content: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DomainSamlOptionsSamlOptionsIdpArgs:
    def __init__(
        __self__,
        *,
        entity_id: pulumi.Input[_builtins.str],
        metadata_content: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Input[_builtins.str]: ...
    @entity_id.setter
    def entity_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metadataContent")
    def metadata_content(self) -> pulumi.Input[_builtins.str]: ...
    @metadata_content.setter
    def metadata_content(self, value: pulumi.Input[_builtins.str]): ...

class DomainSnapshotOptionsArgsDict(TypedDict):
    automated_snapshot_start_hour: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DomainSnapshotOptionsArgs:
    def __init__(
        __self__, *, automated_snapshot_start_hour: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automatedSnapshotStartHour")
    def automated_snapshot_start_hour(self) -> pulumi.Input[_builtins.int]: ...
    @automated_snapshot_start_hour.setter
    def automated_snapshot_start_hour(self, value: pulumi.Input[_builtins.int]): ...

class DomainSoftwareUpdateOptionsArgsDict(TypedDict):
    auto_software_update_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DomainSoftwareUpdateOptionsArgs:
    def __init__(
        __self__,
        *,
        auto_software_update_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoSoftwareUpdateEnabled")
    def auto_software_update_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_software_update_enabled.setter
    def auto_software_update_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DomainVpcOptionsArgsDict(TypedDict):
    availability_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainVpcOptionsArgs:
    def __init__(
        __self__,
        *,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OutboundConnectionConnectionPropertiesArgsDict(TypedDict):
    cross_cluster_search: NotRequired[
        pulumi.Input[OutboundConnectionConnectionPropertiesCrossClusterSearchArgsDict]
    ]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OutboundConnectionConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        cross_cluster_search: Optional[
            pulumi.Input[OutboundConnectionConnectionPropertiesCrossClusterSearchArgs]
        ] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossClusterSearch")
    def cross_cluster_search(
        self,
    ) -> Optional[
        pulumi.Input[OutboundConnectionConnectionPropertiesCrossClusterSearchArgs]
    ]: ...
    @cross_cluster_search.setter
    def cross_cluster_search(
        self,
        value: Optional[
            pulumi.Input[OutboundConnectionConnectionPropertiesCrossClusterSearchArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OutboundConnectionConnectionPropertiesCrossClusterSearchArgsDict(TypedDict):
    skip_unavailable: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OutboundConnectionConnectionPropertiesCrossClusterSearchArgs:
    def __init__(
        __self__, *, skip_unavailable: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="skipUnavailable")
    def skip_unavailable(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @skip_unavailable.setter
    def skip_unavailable(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OutboundConnectionLocalDomainInfoArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    owner_id: pulumi.Input[_builtins.str]
    region: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class OutboundConnectionLocalDomainInfoArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        owner_id: pulumi.Input[_builtins.str],
        region: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Input[_builtins.str]: ...
    @owner_id.setter
    def owner_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...

class OutboundConnectionRemoteDomainInfoArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    owner_id: pulumi.Input[_builtins.str]
    region: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class OutboundConnectionRemoteDomainInfoArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        owner_id: pulumi.Input[_builtins.str],
        region: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Input[_builtins.str]: ...
    @owner_id.setter
    def owner_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...

class PackagePackageSourceArgsDict(TypedDict):
    s3_bucket_name: pulumi.Input[_builtins.str]
    s3_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PackagePackageSourceArgs:
    def __init__(
        __self__,
        *,
        s3_bucket_name: pulumi.Input[_builtins.str],
        s3_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> pulumi.Input[_builtins.str]: ...
    @s3_key.setter
    def s3_key(self, value: pulumi.Input[_builtins.str]): ...

class ServerlessCollectionTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServerlessCollectionTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServerlessSecurityConfigSamlOptionsArgsDict(TypedDict):
    metadata: pulumi.Input[_builtins.str]
    group_attribute: NotRequired[pulumi.Input[_builtins.str]]
    session_timeout: NotRequired[pulumi.Input[_builtins.int]]
    user_attribute: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServerlessSecurityConfigSamlOptionsArgs:
    def __init__(
        __self__,
        *,
        metadata: pulumi.Input[_builtins.str],
        group_attribute: Optional[pulumi.Input[_builtins.str]] = ...,
        session_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        user_attribute: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Input[_builtins.str]: ...
    @metadata.setter
    def metadata(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupAttribute")
    def group_attribute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_attribute.setter
    def group_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @session_timeout.setter
    def session_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="userAttribute")
    def user_attribute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_attribute.setter
    def user_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServerlessVpcEndpointTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServerlessVpcEndpointTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VpcEndpointVpcOptionsArgsDict(TypedDict):
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    availability_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class VpcEndpointVpcOptionsArgs:
    def __init__(
        __self__,
        *,
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetServerlessSecurityConfigSamlOptionArgsDict(TypedDict):
    group_attribute: _builtins.str
    metadata: _builtins.str
    session_timeout: _builtins.int
    user_attribute: _builtins.str
    ...

@pulumi.input_type
class GetServerlessSecurityConfigSamlOptionArgs:
    def __init__(
        __self__,
        *,
        group_attribute: _builtins.str,
        metadata: _builtins.str,
        session_timeout: _builtins.int,
        user_attribute: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupAttribute")
    def group_attribute(self) -> _builtins.str: ...
    @group_attribute.setter
    def group_attribute(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> _builtins.str: ...
    @metadata.setter
    def metadata(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> _builtins.int: ...
    @session_timeout.setter
    def session_timeout(self, value: _builtins.int): ...
    @_builtins.property
    @pulumi.getter(name="userAttribute")
    def user_attribute(self) -> _builtins.str: ...
    @user_attribute.setter
    def user_attribute(self, value: _builtins.str): ...
