import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "IdentityPoolCognitoIdentityProviderArgs",
    "IdentityPoolCognitoIdentityProviderArgsDict",
    "IdentityPoolRoleAttachmentRoleMappingArgs",
    "IdentityPoolRoleAttachmentRoleMappingArgsDict",
    ...,
    ...,
    "LogDeliveryConfigurationLogConfigurationArgs",
    "LogDeliveryConfigurationLogConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ManagedLoginBrandingAssetArgs",
    "ManagedLoginBrandingAssetArgsDict",
    "ManagedUserPoolClientAnalyticsConfigurationArgs",
    ...,
    "ManagedUserPoolClientRefreshTokenRotationArgs",
    "ManagedUserPoolClientRefreshTokenRotationArgsDict",
    "ManagedUserPoolClientTokenValidityUnitsArgs",
    "ManagedUserPoolClientTokenValidityUnitsArgsDict",
    "ResourceServerScopeArgs",
    "ResourceServerScopeArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RiskConfigurationRiskExceptionConfigurationArgs",
    ...,
    "UserPoolAccountRecoverySettingArgs",
    "UserPoolAccountRecoverySettingArgsDict",
    ...,
    ...,
    "UserPoolAdminCreateUserConfigArgs",
    "UserPoolAdminCreateUserConfigArgsDict",
    ...,
    ...,
    "UserPoolClientAnalyticsConfigurationArgs",
    "UserPoolClientAnalyticsConfigurationArgsDict",
    "UserPoolClientRefreshTokenRotationArgs",
    "UserPoolClientRefreshTokenRotationArgsDict",
    "UserPoolClientTokenValidityUnitsArgs",
    "UserPoolClientTokenValidityUnitsArgsDict",
    "UserPoolDeviceConfigurationArgs",
    "UserPoolDeviceConfigurationArgsDict",
    "UserPoolEmailConfigurationArgs",
    "UserPoolEmailConfigurationArgsDict",
    "UserPoolEmailMfaConfigurationArgs",
    "UserPoolEmailMfaConfigurationArgsDict",
    "UserPoolLambdaConfigArgs",
    "UserPoolLambdaConfigArgsDict",
    "UserPoolLambdaConfigCustomEmailSenderArgs",
    "UserPoolLambdaConfigCustomEmailSenderArgsDict",
    "UserPoolLambdaConfigCustomSmsSenderArgs",
    "UserPoolLambdaConfigCustomSmsSenderArgsDict",
    "UserPoolLambdaConfigPreTokenGenerationConfigArgs",
    ...,
    "UserPoolPasswordPolicyArgs",
    "UserPoolPasswordPolicyArgsDict",
    "UserPoolSchemaArgs",
    "UserPoolSchemaArgsDict",
    "UserPoolSchemaNumberAttributeConstraintsArgs",
    "UserPoolSchemaNumberAttributeConstraintsArgsDict",
    "UserPoolSchemaStringAttributeConstraintsArgs",
    "UserPoolSchemaStringAttributeConstraintsArgsDict",
    "UserPoolSignInPolicyArgs",
    "UserPoolSignInPolicyArgsDict",
    "UserPoolSmsConfigurationArgs",
    "UserPoolSmsConfigurationArgsDict",
    "UserPoolSoftwareTokenMfaConfigurationArgs",
    "UserPoolSoftwareTokenMfaConfigurationArgsDict",
    "UserPoolUserAttributeUpdateSettingsArgs",
    "UserPoolUserAttributeUpdateSettingsArgsDict",
    "UserPoolUserPoolAddOnsArgs",
    "UserPoolUserPoolAddOnsArgsDict",
    ...,
    ...,
    "UserPoolUsernameConfigurationArgs",
    "UserPoolUsernameConfigurationArgsDict",
    "UserPoolVerificationMessageTemplateArgs",
    "UserPoolVerificationMessageTemplateArgsDict",
    "UserPoolWebAuthnConfigurationArgs",
    "UserPoolWebAuthnConfigurationArgsDict",
]

class IdentityPoolCognitoIdentityProviderArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    provider_name: NotRequired[pulumi.Input[_builtins.str]]
    server_side_token_check: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class IdentityPoolCognitoIdentityProviderArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        server_side_token_check: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider_name.setter
    def provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverSideTokenCheck")
    def server_side_token_check(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @server_side_token_check.setter
    def server_side_token_check(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class IdentityPoolRoleAttachmentRoleMappingArgsDict(TypedDict):
    identity_provider: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    ambiguous_role_resolution: NotRequired[pulumi.Input[_builtins.str]]
    mapping_rules: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[IdentityPoolRoleAttachmentRoleMappingMappingRuleArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class IdentityPoolRoleAttachmentRoleMappingArgs:
    def __init__(
        __self__,
        *,
        identity_provider: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        ambiguous_role_resolution: Optional[pulumi.Input[_builtins.str]] = ...,
        mapping_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[IdentityPoolRoleAttachmentRoleMappingMappingRuleArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> pulumi.Input[_builtins.str]: ...
    @identity_provider.setter
    def identity_provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ambiguousRoleResolution")
    def ambiguous_role_resolution(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ambiguous_role_resolution.setter
    def ambiguous_role_resolution(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mappingRules")
    def mapping_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[IdentityPoolRoleAttachmentRoleMappingMappingRuleArgs]]
        ]
    ]: ...
    @mapping_rules.setter
    def mapping_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[IdentityPoolRoleAttachmentRoleMappingMappingRuleArgs]
                ]
            ]
        ],
    ): ...

class IdentityPoolRoleAttachmentRoleMappingMappingRuleArgsDict(TypedDict):
    claim: pulumi.Input[_builtins.str]
    match_type: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class IdentityPoolRoleAttachmentRoleMappingMappingRuleArgs:
    def __init__(
        __self__,
        *,
        claim: pulumi.Input[_builtins.str],
        match_type: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def claim(self) -> pulumi.Input[_builtins.str]: ...
    @claim.setter
    def claim(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="matchType")
    def match_type(self) -> pulumi.Input[_builtins.str]: ...
    @match_type.setter
    def match_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class LogDeliveryConfigurationLogConfigurationArgsDict(TypedDict):
    event_source: pulumi.Input[_builtins.str]
    log_level: pulumi.Input[_builtins.str]
    cloud_watch_logs_configuration: NotRequired[
        pulumi.Input[
            LogDeliveryConfigurationLogConfigurationCloudWatchLogsConfigurationArgsDict
        ]
    ]
    firehose_configuration: NotRequired[
        pulumi.Input[
            LogDeliveryConfigurationLogConfigurationFirehoseConfigurationArgsDict
        ]
    ]
    s3_configuration: NotRequired[
        pulumi.Input[LogDeliveryConfigurationLogConfigurationS3ConfigurationArgsDict]
    ]

@pulumi.input_type
class LogDeliveryConfigurationLogConfigurationArgs:
    def __init__(
        __self__,
        *,
        event_source: pulumi.Input[_builtins.str],
        log_level: pulumi.Input[_builtins.str],
        cloud_watch_logs_configuration: Optional[
            pulumi.Input[
                LogDeliveryConfigurationLogConfigurationCloudWatchLogsConfigurationArgs
            ]
        ] = ...,
        firehose_configuration: Optional[
            pulumi.Input[
                LogDeliveryConfigurationLogConfigurationFirehoseConfigurationArgs
            ]
        ] = ...,
        s3_configuration: Optional[
            pulumi.Input[LogDeliveryConfigurationLogConfigurationS3ConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> pulumi.Input[_builtins.str]: ...
    @event_source.setter
    def event_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> pulumi.Input[_builtins.str]: ...
    @log_level.setter
    def log_level(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogsConfiguration")
    def cloud_watch_logs_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            LogDeliveryConfigurationLogConfigurationCloudWatchLogsConfigurationArgs
        ]
    ]: ...
    @cloud_watch_logs_configuration.setter
    def cloud_watch_logs_configuration(
        self,
        value: Optional[
            pulumi.Input[
                LogDeliveryConfigurationLogConfigurationCloudWatchLogsConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="firehoseConfiguration")
    def firehose_configuration(
        self,
    ) -> Optional[
        pulumi.Input[LogDeliveryConfigurationLogConfigurationFirehoseConfigurationArgs]
    ]: ...
    @firehose_configuration.setter
    def firehose_configuration(
        self,
        value: Optional[
            pulumi.Input[
                LogDeliveryConfigurationLogConfigurationFirehoseConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> Optional[
        pulumi.Input[LogDeliveryConfigurationLogConfigurationS3ConfigurationArgs]
    ]: ...
    @s3_configuration.setter
    def s3_configuration(
        self,
        value: Optional[
            pulumi.Input[LogDeliveryConfigurationLogConfigurationS3ConfigurationArgs]
        ],
    ): ...

class LogDeliveryConfigurationLogConfigurationCloudWatchLogsConfigurationArgsDict(
    TypedDict
):
    log_group_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogDeliveryConfigurationLogConfigurationCloudWatchLogsConfigurationArgs:
    def __init__(
        __self__, *, log_group_arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_group_arn.setter
    def log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogDeliveryConfigurationLogConfigurationFirehoseConfigurationArgsDict(TypedDict):
    stream_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogDeliveryConfigurationLogConfigurationFirehoseConfigurationArgs:
    def __init__(
        __self__, *, stream_arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_arn.setter
    def stream_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogDeliveryConfigurationLogConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogDeliveryConfigurationLogConfigurationS3ConfigurationArgs:
    def __init__(
        __self__, *, bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_arn.setter
    def bucket_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedLoginBrandingAssetArgsDict(TypedDict):
    category: pulumi.Input[_builtins.str]
    color_mode: pulumi.Input[_builtins.str]
    extension: pulumi.Input[_builtins.str]
    bytes: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedLoginBrandingAssetArgs:
    def __init__(
        __self__,
        *,
        category: pulumi.Input[_builtins.str],
        color_mode: pulumi.Input[_builtins.str],
        extension: pulumi.Input[_builtins.str],
        bytes: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Input[_builtins.str]: ...
    @category.setter
    def category(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="colorMode")
    def color_mode(self) -> pulumi.Input[_builtins.str]: ...
    @color_mode.setter
    def color_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def extension(self) -> pulumi.Input[_builtins.str]: ...
    @extension.setter
    def extension(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def bytes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bytes.setter
    def bytes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedUserPoolClientAnalyticsConfigurationArgsDict(TypedDict):
    application_arn: NotRequired[pulumi.Input[_builtins.str]]
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    user_data_shared: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ManagedUserPoolClientAnalyticsConfigurationArgs:
    def __init__(
        __self__,
        *,
        application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        user_data_shared: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_arn.setter
    def application_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userDataShared")
    def user_data_shared(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @user_data_shared.setter
    def user_data_shared(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ManagedUserPoolClientRefreshTokenRotationArgsDict(TypedDict):
    feature: pulumi.Input[_builtins.str]
    retry_grace_period_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ManagedUserPoolClientRefreshTokenRotationArgs:
    def __init__(
        __self__,
        *,
        feature: pulumi.Input[_builtins.str],
        retry_grace_period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def feature(self) -> pulumi.Input[_builtins.str]: ...
    @feature.setter
    def feature(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retryGracePeriodSeconds")
    def retry_grace_period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retry_grace_period_seconds.setter
    def retry_grace_period_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ManagedUserPoolClientTokenValidityUnitsArgsDict(TypedDict):
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    id_token: NotRequired[pulumi.Input[_builtins.str]]
    refresh_token: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedUserPoolClientTokenValidityUnitsArgs:
    def __init__(
        __self__,
        *,
        access_token: Optional[pulumi.Input[_builtins.str]] = ...,
        id_token: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_token: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idToken")
    def id_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id_token.setter
    def id_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceServerScopeArgsDict(TypedDict):
    scope_description: pulumi.Input[_builtins.str]
    scope_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ResourceServerScopeArgs:
    def __init__(
        __self__,
        *,
        scope_description: pulumi.Input[_builtins.str],
        scope_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scopeDescription")
    def scope_description(self) -> pulumi.Input[_builtins.str]: ...
    @scope_description.setter
    def scope_description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scopeName")
    def scope_name(self) -> pulumi.Input[_builtins.str]: ...
    @scope_name.setter
    def scope_name(self, value: pulumi.Input[_builtins.str]): ...

class RiskConfigurationAccountTakeoverRiskConfigurationArgsDict(TypedDict):
    actions: pulumi.Input[
        RiskConfigurationAccountTakeoverRiskConfigurationActionsArgsDict
    ]
    notify_configuration: NotRequired[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class RiskConfigurationAccountTakeoverRiskConfigurationArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationActionsArgs
        ],
        notify_configuration: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> pulumi.Input[RiskConfigurationAccountTakeoverRiskConfigurationActionsArgs]: ...
    @actions.setter
    def actions(
        self,
        value: pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationActionsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notifyConfiguration")
    def notify_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationArgs
        ]
    ]: ...
    @notify_configuration.setter
    def notify_configuration(
        self,
        value: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationArgs
            ]
        ],
    ): ...

class RiskConfigurationAccountTakeoverRiskConfigurationActionsArgsDict(TypedDict):
    high_action: NotRequired[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionArgsDict
        ]
    ]
    low_action: NotRequired[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionArgsDict
        ]
    ]
    medium_action: NotRequired[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionArgsDict
        ]
    ]

@pulumi.input_type
class RiskConfigurationAccountTakeoverRiskConfigurationActionsArgs:
    def __init__(
        __self__,
        *,
        high_action: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionArgs
            ]
        ] = ...,
        low_action: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionArgs
            ]
        ] = ...,
        medium_action: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="highAction")
    def high_action(
        self,
    ) -> Optional[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionArgs
        ]
    ]: ...
    @high_action.setter
    def high_action(
        self,
        value: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lowAction")
    def low_action(
        self,
    ) -> Optional[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionArgs
        ]
    ]: ...
    @low_action.setter
    def low_action(
        self,
        value: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mediumAction")
    def medium_action(
        self,
    ) -> Optional[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionArgs
        ]
    ]: ...
    @medium_action.setter
    def medium_action(
        self,
        value: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionArgs
            ]
        ],
    ): ...

class RiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionArgsDict(
    TypedDict
):
    event_action: pulumi.Input[_builtins.str]
    notify: pulumi.Input[_builtins.bool]

@pulumi.input_type
class RiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionArgs:
    def __init__(
        __self__,
        *,
        event_action: pulumi.Input[_builtins.str],
        notify: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventAction")
    def event_action(self) -> pulumi.Input[_builtins.str]: ...
    @event_action.setter
    def event_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def notify(self) -> pulumi.Input[_builtins.bool]: ...
    @notify.setter
    def notify(self, value: pulumi.Input[_builtins.bool]): ...

class RiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionArgsDict(
    TypedDict
):
    event_action: pulumi.Input[_builtins.str]
    notify: pulumi.Input[_builtins.bool]

@pulumi.input_type
class RiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionArgs:
    def __init__(
        __self__,
        *,
        event_action: pulumi.Input[_builtins.str],
        notify: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventAction")
    def event_action(self) -> pulumi.Input[_builtins.str]: ...
    @event_action.setter
    def event_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def notify(self) -> pulumi.Input[_builtins.bool]: ...
    @notify.setter
    def notify(self, value: pulumi.Input[_builtins.bool]): ...

class RiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionArgsDict(
    TypedDict
):
    event_action: pulumi.Input[_builtins.str]
    notify: pulumi.Input[_builtins.bool]

@pulumi.input_type
class RiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionArgs:
    def __init__(
        __self__,
        *,
        event_action: pulumi.Input[_builtins.str],
        notify: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventAction")
    def event_action(self) -> pulumi.Input[_builtins.str]: ...
    @event_action.setter
    def event_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def notify(self) -> pulumi.Input[_builtins.bool]: ...
    @notify.setter
    def notify(self, value: pulumi.Input[_builtins.bool]): ...

class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationArgsDict(
    TypedDict
):
    source_arn: pulumi.Input[_builtins.str]
    block_email: NotRequired[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailArgsDict
        ]
    ]
    from_: NotRequired[pulumi.Input[_builtins.str]]
    mfa_email: NotRequired[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailArgsDict
        ]
    ]
    no_action_email: NotRequired[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailArgsDict
        ]
    ]
    reply_to: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationArgs:
    def __init__(
        __self__,
        *,
        source_arn: pulumi.Input[_builtins.str],
        block_email: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailArgs
            ]
        ] = ...,
        from_: Optional[pulumi.Input[_builtins.str]] = ...,
        mfa_email: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailArgs
            ]
        ] = ...,
        no_action_email: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailArgs
            ]
        ] = ...,
        reply_to: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Input[_builtins.str]: ...
    @source_arn.setter
    def source_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="blockEmail")
    def block_email(
        self,
    ) -> Optional[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailArgs
        ]
    ]: ...
    @block_email.setter
    def block_email(
        self,
        value: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mfaEmail")
    def mfa_email(
        self,
    ) -> Optional[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailArgs
        ]
    ]: ...
    @mfa_email.setter
    def mfa_email(
        self,
        value: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="noActionEmail")
    def no_action_email(
        self,
    ) -> Optional[
        pulumi.Input[
            RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailArgs
        ]
    ]: ...
    @no_action_email.setter
    def no_action_email(
        self,
        value: Optional[
            pulumi.Input[
                RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replyTo")
    def reply_to(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reply_to.setter
    def reply_to(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailArgsDict(
    TypedDict
):
    html_body: pulumi.Input[_builtins.str]
    subject: pulumi.Input[_builtins.str]
    text_body: pulumi.Input[_builtins.str]

@pulumi.input_type
class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailArgs:
    def __init__(
        __self__,
        *,
        html_body: pulumi.Input[_builtins.str],
        subject: pulumi.Input[_builtins.str],
        text_body: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="htmlBody")
    def html_body(self) -> pulumi.Input[_builtins.str]: ...
    @html_body.setter
    def html_body(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[_builtins.str]: ...
    @subject.setter
    def subject(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="textBody")
    def text_body(self) -> pulumi.Input[_builtins.str]: ...
    @text_body.setter
    def text_body(self, value: pulumi.Input[_builtins.str]): ...

class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailArgsDict(
    TypedDict
):
    html_body: pulumi.Input[_builtins.str]
    subject: pulumi.Input[_builtins.str]
    text_body: pulumi.Input[_builtins.str]

@pulumi.input_type
class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailArgs:
    def __init__(
        __self__,
        *,
        html_body: pulumi.Input[_builtins.str],
        subject: pulumi.Input[_builtins.str],
        text_body: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="htmlBody")
    def html_body(self) -> pulumi.Input[_builtins.str]: ...
    @html_body.setter
    def html_body(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[_builtins.str]: ...
    @subject.setter
    def subject(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="textBody")
    def text_body(self) -> pulumi.Input[_builtins.str]: ...
    @text_body.setter
    def text_body(self, value: pulumi.Input[_builtins.str]): ...

class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailArgsDict(
    TypedDict
):
    html_body: pulumi.Input[_builtins.str]
    subject: pulumi.Input[_builtins.str]
    text_body: pulumi.Input[_builtins.str]

@pulumi.input_type
class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailArgs:
    def __init__(
        __self__,
        *,
        html_body: pulumi.Input[_builtins.str],
        subject: pulumi.Input[_builtins.str],
        text_body: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="htmlBody")
    def html_body(self) -> pulumi.Input[_builtins.str]: ...
    @html_body.setter
    def html_body(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[_builtins.str]: ...
    @subject.setter
    def subject(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="textBody")
    def text_body(self) -> pulumi.Input[_builtins.str]: ...
    @text_body.setter
    def text_body(self, value: pulumi.Input[_builtins.str]): ...

class RiskConfigurationCompromisedCredentialsRiskConfigurationArgsDict(TypedDict):
    actions: pulumi.Input[
        RiskConfigurationCompromisedCredentialsRiskConfigurationActionsArgsDict
    ]
    event_filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RiskConfigurationCompromisedCredentialsRiskConfigurationArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[
            RiskConfigurationCompromisedCredentialsRiskConfigurationActionsArgs
        ],
        event_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> pulumi.Input[
        RiskConfigurationCompromisedCredentialsRiskConfigurationActionsArgs
    ]: ...
    @actions.setter
    def actions(
        self,
        value: pulumi.Input[
            RiskConfigurationCompromisedCredentialsRiskConfigurationActionsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventFilters")
    def event_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @event_filters.setter
    def event_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RiskConfigurationCompromisedCredentialsRiskConfigurationActionsArgsDict(
    TypedDict
):
    event_action: pulumi.Input[_builtins.str]

@pulumi.input_type
class RiskConfigurationCompromisedCredentialsRiskConfigurationActionsArgs:
    def __init__(__self__, *, event_action: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventAction")
    def event_action(self) -> pulumi.Input[_builtins.str]: ...
    @event_action.setter
    def event_action(self, value: pulumi.Input[_builtins.str]): ...

class RiskConfigurationRiskExceptionConfigurationArgsDict(TypedDict):
    blocked_ip_range_lists: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    skipped_ip_range_lists: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class RiskConfigurationRiskExceptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        blocked_ip_range_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        skipped_ip_range_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockedIpRangeLists")
    def blocked_ip_range_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @blocked_ip_range_lists.setter
    def blocked_ip_range_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skippedIpRangeLists")
    def skipped_ip_range_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @skipped_ip_range_lists.setter
    def skipped_ip_range_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class UserPoolAccountRecoverySettingArgsDict(TypedDict):
    recovery_mechanisms: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[UserPoolAccountRecoverySettingRecoveryMechanismArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class UserPoolAccountRecoverySettingArgs:
    def __init__(
        __self__,
        *,
        recovery_mechanisms: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[UserPoolAccountRecoverySettingRecoveryMechanismArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recoveryMechanisms")
    def recovery_mechanisms(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[UserPoolAccountRecoverySettingRecoveryMechanismArgs]]
        ]
    ]: ...
    @recovery_mechanisms.setter
    def recovery_mechanisms(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[UserPoolAccountRecoverySettingRecoveryMechanismArgs]
                ]
            ]
        ],
    ): ...

class UserPoolAccountRecoverySettingRecoveryMechanismArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    priority: pulumi.Input[_builtins.int]

@pulumi.input_type
class UserPoolAccountRecoverySettingRecoveryMechanismArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        priority: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...

class UserPoolAdminCreateUserConfigArgsDict(TypedDict):
    allow_admin_create_user_only: NotRequired[pulumi.Input[_builtins.bool]]
    invite_message_template: NotRequired[
        pulumi.Input[UserPoolAdminCreateUserConfigInviteMessageTemplateArgsDict]
    ]

@pulumi.input_type
class UserPoolAdminCreateUserConfigArgs:
    def __init__(
        __self__,
        *,
        allow_admin_create_user_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        invite_message_template: Optional[
            pulumi.Input[UserPoolAdminCreateUserConfigInviteMessageTemplateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowAdminCreateUserOnly")
    def allow_admin_create_user_only(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_admin_create_user_only.setter
    def allow_admin_create_user_only(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inviteMessageTemplate")
    def invite_message_template(
        self,
    ) -> Optional[
        pulumi.Input[UserPoolAdminCreateUserConfigInviteMessageTemplateArgs]
    ]: ...
    @invite_message_template.setter
    def invite_message_template(
        self,
        value: Optional[
            pulumi.Input[UserPoolAdminCreateUserConfigInviteMessageTemplateArgs]
        ],
    ): ...

class UserPoolAdminCreateUserConfigInviteMessageTemplateArgsDict(TypedDict):
    email_message: NotRequired[pulumi.Input[_builtins.str]]
    email_subject: NotRequired[pulumi.Input[_builtins.str]]
    sms_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolAdminCreateUserConfigInviteMessageTemplateArgs:
    def __init__(
        __self__,
        *,
        email_message: Optional[pulumi.Input[_builtins.str]] = ...,
        email_subject: Optional[pulumi.Input[_builtins.str]] = ...,
        sms_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailMessage")
    def email_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_message.setter
    def email_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailSubject")
    def email_subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_subject.setter
    def email_subject(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="smsMessage")
    def sms_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sms_message.setter
    def sms_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserPoolClientAnalyticsConfigurationArgsDict(TypedDict):
    application_arn: NotRequired[pulumi.Input[_builtins.str]]
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    user_data_shared: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class UserPoolClientAnalyticsConfigurationArgs:
    def __init__(
        __self__,
        *,
        application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        user_data_shared: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_arn.setter
    def application_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userDataShared")
    def user_data_shared(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @user_data_shared.setter
    def user_data_shared(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class UserPoolClientRefreshTokenRotationArgsDict(TypedDict):
    feature: pulumi.Input[_builtins.str]
    retry_grace_period_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class UserPoolClientRefreshTokenRotationArgs:
    def __init__(
        __self__,
        *,
        feature: pulumi.Input[_builtins.str],
        retry_grace_period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def feature(self) -> pulumi.Input[_builtins.str]: ...
    @feature.setter
    def feature(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retryGracePeriodSeconds")
    def retry_grace_period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retry_grace_period_seconds.setter
    def retry_grace_period_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class UserPoolClientTokenValidityUnitsArgsDict(TypedDict):
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    id_token: NotRequired[pulumi.Input[_builtins.str]]
    refresh_token: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolClientTokenValidityUnitsArgs:
    def __init__(
        __self__,
        *,
        access_token: Optional[pulumi.Input[_builtins.str]] = ...,
        id_token: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_token: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idToken")
    def id_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id_token.setter
    def id_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserPoolDeviceConfigurationArgsDict(TypedDict):
    challenge_required_on_new_device: NotRequired[pulumi.Input[_builtins.bool]]
    device_only_remembered_on_user_prompt: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class UserPoolDeviceConfigurationArgs:
    def __init__(
        __self__,
        *,
        challenge_required_on_new_device: Optional[pulumi.Input[_builtins.bool]] = ...,
        device_only_remembered_on_user_prompt: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="challengeRequiredOnNewDevice")
    def challenge_required_on_new_device(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @challenge_required_on_new_device.setter
    def challenge_required_on_new_device(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deviceOnlyRememberedOnUserPrompt")
    def device_only_remembered_on_user_prompt(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @device_only_remembered_on_user_prompt.setter
    def device_only_remembered_on_user_prompt(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class UserPoolEmailConfigurationArgsDict(TypedDict):
    configuration_set: NotRequired[pulumi.Input[_builtins.str]]
    email_sending_account: NotRequired[pulumi.Input[_builtins.str]]
    from_email_address: NotRequired[pulumi.Input[_builtins.str]]
    reply_to_email_address: NotRequired[pulumi.Input[_builtins.str]]
    source_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolEmailConfigurationArgs:
    def __init__(
        __self__,
        *,
        configuration_set: Optional[pulumi.Input[_builtins.str]] = ...,
        email_sending_account: Optional[pulumi.Input[_builtins.str]] = ...,
        from_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        reply_to_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        source_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationSet")
    def configuration_set(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_set.setter
    def configuration_set(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailSendingAccount")
    def email_sending_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_sending_account.setter
    def email_sending_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fromEmailAddress")
    def from_email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @from_email_address.setter
    def from_email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replyToEmailAddress")
    def reply_to_email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reply_to_email_address.setter
    def reply_to_email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_arn.setter
    def source_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserPoolEmailMfaConfigurationArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]
    subject: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolEmailMfaConfigurationArgs:
    def __init__(
        __self__,
        *,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        subject: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subject.setter
    def subject(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserPoolLambdaConfigArgsDict(TypedDict):
    create_auth_challenge: NotRequired[pulumi.Input[_builtins.str]]
    custom_email_sender: NotRequired[
        pulumi.Input[UserPoolLambdaConfigCustomEmailSenderArgsDict]
    ]
    custom_message: NotRequired[pulumi.Input[_builtins.str]]
    custom_sms_sender: NotRequired[
        pulumi.Input[UserPoolLambdaConfigCustomSmsSenderArgsDict]
    ]
    define_auth_challenge: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    post_authentication: NotRequired[pulumi.Input[_builtins.str]]
    post_confirmation: NotRequired[pulumi.Input[_builtins.str]]
    pre_authentication: NotRequired[pulumi.Input[_builtins.str]]
    pre_sign_up: NotRequired[pulumi.Input[_builtins.str]]
    pre_token_generation: NotRequired[pulumi.Input[_builtins.str]]
    pre_token_generation_config: NotRequired[
        pulumi.Input[UserPoolLambdaConfigPreTokenGenerationConfigArgsDict]
    ]
    user_migration: NotRequired[pulumi.Input[_builtins.str]]
    verify_auth_challenge_response: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolLambdaConfigArgs:
    def __init__(
        __self__,
        *,
        create_auth_challenge: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_email_sender: Optional[
            pulumi.Input[UserPoolLambdaConfigCustomEmailSenderArgs]
        ] = ...,
        custom_message: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_sms_sender: Optional[
            pulumi.Input[UserPoolLambdaConfigCustomSmsSenderArgs]
        ] = ...,
        define_auth_challenge: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        post_authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        post_confirmation: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_sign_up: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_token_generation: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_token_generation_config: Optional[
            pulumi.Input[UserPoolLambdaConfigPreTokenGenerationConfigArgs]
        ] = ...,
        user_migration: Optional[pulumi.Input[_builtins.str]] = ...,
        verify_auth_challenge_response: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createAuthChallenge")
    def create_auth_challenge(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_auth_challenge.setter
    def create_auth_challenge(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customEmailSender")
    def custom_email_sender(
        self,
    ) -> Optional[pulumi.Input[UserPoolLambdaConfigCustomEmailSenderArgs]]: ...
    @custom_email_sender.setter
    def custom_email_sender(
        self, value: Optional[pulumi.Input[UserPoolLambdaConfigCustomEmailSenderArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customMessage")
    def custom_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_message.setter
    def custom_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customSmsSender")
    def custom_sms_sender(
        self,
    ) -> Optional[pulumi.Input[UserPoolLambdaConfigCustomSmsSenderArgs]]: ...
    @custom_sms_sender.setter
    def custom_sms_sender(
        self, value: Optional[pulumi.Input[UserPoolLambdaConfigCustomSmsSenderArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defineAuthChallenge")
    def define_auth_challenge(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @define_auth_challenge.setter
    def define_auth_challenge(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postAuthentication")
    def post_authentication(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_authentication.setter
    def post_authentication(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postConfirmation")
    def post_confirmation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_confirmation.setter
    def post_confirmation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preAuthentication")
    def pre_authentication(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pre_authentication.setter
    def pre_authentication(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preSignUp")
    def pre_sign_up(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pre_sign_up.setter
    def pre_sign_up(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preTokenGeneration")
    def pre_token_generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pre_token_generation.setter
    def pre_token_generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preTokenGenerationConfig")
    def pre_token_generation_config(
        self,
    ) -> Optional[pulumi.Input[UserPoolLambdaConfigPreTokenGenerationConfigArgs]]: ...
    @pre_token_generation_config.setter
    def pre_token_generation_config(
        self,
        value: Optional[pulumi.Input[UserPoolLambdaConfigPreTokenGenerationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userMigration")
    def user_migration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_migration.setter
    def user_migration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="verifyAuthChallengeResponse")
    def verify_auth_challenge_response(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @verify_auth_challenge_response.setter
    def verify_auth_challenge_response(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class UserPoolLambdaConfigCustomEmailSenderArgsDict(TypedDict):
    lambda_arn: pulumi.Input[_builtins.str]
    lambda_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class UserPoolLambdaConfigCustomEmailSenderArgs:
    def __init__(
        __self__,
        *,
        lambda_arn: pulumi.Input[_builtins.str],
        lambda_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaVersion")
    def lambda_version(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_version.setter
    def lambda_version(self, value: pulumi.Input[_builtins.str]): ...

class UserPoolLambdaConfigCustomSmsSenderArgsDict(TypedDict):
    lambda_arn: pulumi.Input[_builtins.str]
    lambda_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class UserPoolLambdaConfigCustomSmsSenderArgs:
    def __init__(
        __self__,
        *,
        lambda_arn: pulumi.Input[_builtins.str],
        lambda_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaVersion")
    def lambda_version(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_version.setter
    def lambda_version(self, value: pulumi.Input[_builtins.str]): ...

class UserPoolLambdaConfigPreTokenGenerationConfigArgsDict(TypedDict):
    lambda_arn: pulumi.Input[_builtins.str]
    lambda_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class UserPoolLambdaConfigPreTokenGenerationConfigArgs:
    def __init__(
        __self__,
        *,
        lambda_arn: pulumi.Input[_builtins.str],
        lambda_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaVersion")
    def lambda_version(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_version.setter
    def lambda_version(self, value: pulumi.Input[_builtins.str]): ...

class UserPoolPasswordPolicyArgsDict(TypedDict):
    minimum_length: NotRequired[pulumi.Input[_builtins.int]]
    password_history_size: NotRequired[pulumi.Input[_builtins.int]]
    require_lowercase: NotRequired[pulumi.Input[_builtins.bool]]
    require_numbers: NotRequired[pulumi.Input[_builtins.bool]]
    require_symbols: NotRequired[pulumi.Input[_builtins.bool]]
    require_uppercase: NotRequired[pulumi.Input[_builtins.bool]]
    temporary_password_validity_days: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class UserPoolPasswordPolicyArgs:
    def __init__(
        __self__,
        *,
        minimum_length: Optional[pulumi.Input[_builtins.int]] = ...,
        password_history_size: Optional[pulumi.Input[_builtins.int]] = ...,
        require_lowercase: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_numbers: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_symbols: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_uppercase: Optional[pulumi.Input[_builtins.bool]] = ...,
        temporary_password_validity_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumLength")
    def minimum_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum_length.setter
    def minimum_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordHistorySize")
    def password_history_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @password_history_size.setter
    def password_history_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="requireLowercase")
    def require_lowercase(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_lowercase.setter
    def require_lowercase(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requireNumbers")
    def require_numbers(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_numbers.setter
    def require_numbers(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requireSymbols")
    def require_symbols(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_symbols.setter
    def require_symbols(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requireUppercase")
    def require_uppercase(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_uppercase.setter
    def require_uppercase(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="temporaryPasswordValidityDays")
    def temporary_password_validity_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @temporary_password_validity_days.setter
    def temporary_password_validity_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class UserPoolSchemaArgsDict(TypedDict):
    attribute_data_type: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    developer_only_attribute: NotRequired[pulumi.Input[_builtins.bool]]
    mutable: NotRequired[pulumi.Input[_builtins.bool]]
    number_attribute_constraints: NotRequired[
        pulumi.Input[UserPoolSchemaNumberAttributeConstraintsArgsDict]
    ]
    required: NotRequired[pulumi.Input[_builtins.bool]]
    string_attribute_constraints: NotRequired[
        pulumi.Input[UserPoolSchemaStringAttributeConstraintsArgsDict]
    ]

@pulumi.input_type
class UserPoolSchemaArgs:
    def __init__(
        __self__,
        *,
        attribute_data_type: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        developer_only_attribute: Optional[pulumi.Input[_builtins.bool]] = ...,
        mutable: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_attribute_constraints: Optional[
            pulumi.Input[UserPoolSchemaNumberAttributeConstraintsArgs]
        ] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
        string_attribute_constraints: Optional[
            pulumi.Input[UserPoolSchemaStringAttributeConstraintsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeDataType")
    def attribute_data_type(self) -> pulumi.Input[_builtins.str]: ...
    @attribute_data_type.setter
    def attribute_data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="developerOnlyAttribute")
    def developer_only_attribute(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @developer_only_attribute.setter
    def developer_only_attribute(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mutable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @mutable.setter
    def mutable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberAttributeConstraints")
    def number_attribute_constraints(
        self,
    ) -> Optional[pulumi.Input[UserPoolSchemaNumberAttributeConstraintsArgs]]: ...
    @number_attribute_constraints.setter
    def number_attribute_constraints(
        self,
        value: Optional[pulumi.Input[UserPoolSchemaNumberAttributeConstraintsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="stringAttributeConstraints")
    def string_attribute_constraints(
        self,
    ) -> Optional[pulumi.Input[UserPoolSchemaStringAttributeConstraintsArgs]]: ...
    @string_attribute_constraints.setter
    def string_attribute_constraints(
        self,
        value: Optional[pulumi.Input[UserPoolSchemaStringAttributeConstraintsArgs]],
    ): ...

class UserPoolSchemaNumberAttributeConstraintsArgsDict(TypedDict):
    max_value: NotRequired[pulumi.Input[_builtins.str]]
    min_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolSchemaNumberAttributeConstraintsArgs:
    def __init__(
        __self__,
        *,
        max_value: Optional[pulumi.Input[_builtins.str]] = ...,
        min_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_value.setter
    def max_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_value.setter
    def min_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserPoolSchemaStringAttributeConstraintsArgsDict(TypedDict):
    max_length: NotRequired[pulumi.Input[_builtins.str]]
    min_length: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolSchemaStringAttributeConstraintsArgs:
    def __init__(
        __self__,
        *,
        max_length: Optional[pulumi.Input[_builtins.str]] = ...,
        min_length: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_length.setter
    def max_length(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minLength")
    def min_length(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_length.setter
    def min_length(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserPoolSignInPolicyArgsDict(TypedDict):
    allowed_first_auth_factors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class UserPoolSignInPolicyArgs:
    def __init__(
        __self__,
        *,
        allowed_first_auth_factors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedFirstAuthFactors")
    def allowed_first_auth_factors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_first_auth_factors.setter
    def allowed_first_auth_factors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class UserPoolSmsConfigurationArgsDict(TypedDict):
    external_id: pulumi.Input[_builtins.str]
    sns_caller_arn: pulumi.Input[_builtins.str]
    sns_region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolSmsConfigurationArgs:
    def __init__(
        __self__,
        *,
        external_id: pulumi.Input[_builtins.str],
        sns_caller_arn: pulumi.Input[_builtins.str],
        sns_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Input[_builtins.str]: ...
    @external_id.setter
    def external_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="snsCallerArn")
    def sns_caller_arn(self) -> pulumi.Input[_builtins.str]: ...
    @sns_caller_arn.setter
    def sns_caller_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="snsRegion")
    def sns_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sns_region.setter
    def sns_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserPoolSoftwareTokenMfaConfigurationArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class UserPoolSoftwareTokenMfaConfigurationArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class UserPoolUserAttributeUpdateSettingsArgsDict(TypedDict):
    attributes_require_verification_before_updates: pulumi.Input[
        Sequence[pulumi.Input[_builtins.str]]
    ]

@pulumi.input_type
class UserPoolUserAttributeUpdateSettingsArgs:
    def __init__(
        __self__,
        *,
        attributes_require_verification_before_updates: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributesRequireVerificationBeforeUpdates")
    def attributes_require_verification_before_updates(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @attributes_require_verification_before_updates.setter
    def attributes_require_verification_before_updates(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class UserPoolUserPoolAddOnsArgsDict(TypedDict):
    advanced_security_mode: pulumi.Input[_builtins.str]
    advanced_security_additional_flows: NotRequired[
        pulumi.Input[UserPoolUserPoolAddOnsAdvancedSecurityAdditionalFlowsArgsDict]
    ]

@pulumi.input_type
class UserPoolUserPoolAddOnsArgs:
    def __init__(
        __self__,
        *,
        advanced_security_mode: pulumi.Input[_builtins.str],
        advanced_security_additional_flows: Optional[
            pulumi.Input[UserPoolUserPoolAddOnsAdvancedSecurityAdditionalFlowsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedSecurityMode")
    def advanced_security_mode(self) -> pulumi.Input[_builtins.str]: ...
    @advanced_security_mode.setter
    def advanced_security_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="advancedSecurityAdditionalFlows")
    def advanced_security_additional_flows(
        self,
    ) -> Optional[
        pulumi.Input[UserPoolUserPoolAddOnsAdvancedSecurityAdditionalFlowsArgs]
    ]: ...
    @advanced_security_additional_flows.setter
    def advanced_security_additional_flows(
        self,
        value: Optional[
            pulumi.Input[UserPoolUserPoolAddOnsAdvancedSecurityAdditionalFlowsArgs]
        ],
    ): ...

class UserPoolUserPoolAddOnsAdvancedSecurityAdditionalFlowsArgsDict(TypedDict):
    custom_auth_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolUserPoolAddOnsAdvancedSecurityAdditionalFlowsArgs:
    def __init__(
        __self__, *, custom_auth_mode: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customAuthMode")
    def custom_auth_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_auth_mode.setter
    def custom_auth_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserPoolUsernameConfigurationArgsDict(TypedDict):
    case_sensitive: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class UserPoolUsernameConfigurationArgs:
    def __init__(
        __self__, *, case_sensitive: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @case_sensitive.setter
    def case_sensitive(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class UserPoolVerificationMessageTemplateArgsDict(TypedDict):
    default_email_option: NotRequired[pulumi.Input[_builtins.str]]
    email_message: NotRequired[pulumi.Input[_builtins.str]]
    email_message_by_link: NotRequired[pulumi.Input[_builtins.str]]
    email_subject: NotRequired[pulumi.Input[_builtins.str]]
    email_subject_by_link: NotRequired[pulumi.Input[_builtins.str]]
    sms_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolVerificationMessageTemplateArgs:
    def __init__(
        __self__,
        *,
        default_email_option: Optional[pulumi.Input[_builtins.str]] = ...,
        email_message: Optional[pulumi.Input[_builtins.str]] = ...,
        email_message_by_link: Optional[pulumi.Input[_builtins.str]] = ...,
        email_subject: Optional[pulumi.Input[_builtins.str]] = ...,
        email_subject_by_link: Optional[pulumi.Input[_builtins.str]] = ...,
        sms_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultEmailOption")
    def default_email_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_email_option.setter
    def default_email_option(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailMessage")
    def email_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_message.setter
    def email_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailMessageByLink")
    def email_message_by_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_message_by_link.setter
    def email_message_by_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailSubject")
    def email_subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_subject.setter
    def email_subject(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailSubjectByLink")
    def email_subject_by_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_subject_by_link.setter
    def email_subject_by_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="smsMessage")
    def sms_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sms_message.setter
    def sms_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserPoolWebAuthnConfigurationArgsDict(TypedDict):
    relying_party_id: NotRequired[pulumi.Input[_builtins.str]]
    user_verification: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPoolWebAuthnConfigurationArgs:
    def __init__(
        __self__,
        *,
        relying_party_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_verification: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="relyingPartyId")
    def relying_party_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @relying_party_id.setter
    def relying_party_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userVerification")
    def user_verification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_verification.setter
    def user_verification(self, value: Optional[pulumi.Input[_builtins.str]]): ...
