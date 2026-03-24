

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IdentityPoolCognitoIdentityProvider', 'IdentityPoolRoleAttachmentRoleMapping', 'IdentityPoolRoleAttachmentRoleMappingMappingRule', 'LogDeliveryConfigurationLogConfiguration', ..., ..., ..., 'ManagedLoginBrandingAsset', 'ManagedUserPoolClientAnalyticsConfiguration', 'ManagedUserPoolClientRefreshTokenRotation', 'ManagedUserPoolClientTokenValidityUnits', 'ResourceServerScope', 'RiskConfigurationAccountTakeoverRiskConfiguration', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'RiskConfigurationRiskExceptionConfiguration', 'UserPoolAccountRecoverySetting', 'UserPoolAccountRecoverySettingRecoveryMechanism', 'UserPoolAdminCreateUserConfig', 'UserPoolAdminCreateUserConfigInviteMessageTemplate', 'UserPoolClientAnalyticsConfiguration', 'UserPoolClientRefreshTokenRotation', 'UserPoolClientTokenValidityUnits', 'UserPoolDeviceConfiguration', 'UserPoolEmailConfiguration', 'UserPoolEmailMfaConfiguration', 'UserPoolLambdaConfig', 'UserPoolLambdaConfigCustomEmailSender', 'UserPoolLambdaConfigCustomSmsSender', 'UserPoolLambdaConfigPreTokenGenerationConfig', 'UserPoolPasswordPolicy', 'UserPoolSchema', 'UserPoolSchemaNumberAttributeConstraints', 'UserPoolSchemaStringAttributeConstraints', 'UserPoolSignInPolicy', 'UserPoolSmsConfiguration', 'UserPoolSoftwareTokenMfaConfiguration', 'UserPoolUserAttributeUpdateSettings', 'UserPoolUserPoolAddOns', ..., 'UserPoolUsernameConfiguration', 'UserPoolVerificationMessageTemplate', 'UserPoolWebAuthnConfiguration', 'GetIdentityPoolCognitoIdentityProviderResult', 'GetUserGroupsGroupResult', 'GetUserPoolAccountRecoverySettingResult', ..., 'GetUserPoolAdminCreateUserConfigResult', ..., 'GetUserPoolClientAnalyticsConfigurationResult', 'GetUserPoolClientRefreshTokenRotationResult', 'GetUserPoolClientTokenValidityUnitResult', 'GetUserPoolDeviceConfigurationResult', 'GetUserPoolEmailConfigurationResult', 'GetUserPoolLambdaConfigResult', 'GetUserPoolLambdaConfigCustomEmailSenderResult', 'GetUserPoolLambdaConfigCustomSmsSenderResult', ..., 'GetUserPoolSchemaAttributeResult', ..., ..., 'GetUserPoolUserPoolAddOnResult', ...]
@pulumi.output_type
class IdentityPoolCognitoIdentityProvider(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., provider_name: Optional[_builtins.str] = ..., server_side_token_check: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideTokenCheck")
    def server_side_token_check(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class IdentityPoolRoleAttachmentRoleMapping(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity_provider: _builtins.str, type: _builtins.str, ambiguous_role_resolution: Optional[_builtins.str] = ..., mapping_rules: Optional[Sequence[outputs.IdentityPoolRoleAttachmentRoleMappingMappingRule]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ambiguousRoleResolution")
    def ambiguous_role_resolution(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingRules")
    def mapping_rules(self) -> Optional[Sequence[outputs.IdentityPoolRoleAttachmentRoleMappingMappingRule]]:
        
        ...
    


@pulumi.output_type
class IdentityPoolRoleAttachmentRoleMappingMappingRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, claim: _builtins.str, match_type: _builtins.str, role_arn: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def claim(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchType")
    def match_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class LogDeliveryConfigurationLogConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_source: _builtins.str, log_level: _builtins.str, cloud_watch_logs_configuration: Optional[outputs.LogDeliveryConfigurationLogConfigurationCloudWatchLogsConfiguration] = ..., firehose_configuration: Optional[outputs.LogDeliveryConfigurationLogConfigurationFirehoseConfiguration] = ..., s3_configuration: Optional[outputs.LogDeliveryConfigurationLogConfigurationS3Configuration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogsConfiguration")
    def cloud_watch_logs_configuration(self) -> Optional[outputs.LogDeliveryConfigurationLogConfigurationCloudWatchLogsConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseConfiguration")
    def firehose_configuration(self) -> Optional[outputs.LogDeliveryConfigurationLogConfigurationFirehoseConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> Optional[outputs.LogDeliveryConfigurationLogConfigurationS3Configuration]:
        
        ...
    


@pulumi.output_type
class LogDeliveryConfigurationLogConfigurationCloudWatchLogsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LogDeliveryConfigurationLogConfigurationFirehoseConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, stream_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LogDeliveryConfigurationLogConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedLoginBrandingAsset(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, category: _builtins.str, color_mode: _builtins.str, extension: _builtins.str, bytes: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="colorMode")
    def color_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extension(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bytes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedUserPoolClientAnalyticsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_arn: Optional[_builtins.str] = ..., application_id: Optional[_builtins.str] = ..., external_id: Optional[_builtins.str] = ..., role_arn: Optional[_builtins.str] = ..., user_data_shared: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataShared")
    def user_data_shared(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ManagedUserPoolClientRefreshTokenRotation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, feature: _builtins.str, retry_grace_period_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def feature(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryGracePeriodSeconds")
    def retry_grace_period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ManagedUserPoolClientTokenValidityUnits(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_token: Optional[_builtins.str] = ..., id_token: Optional[_builtins.str] = ..., refresh_token: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idToken")
    def id_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceServerScope(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scope_description: _builtins.str, scope_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeDescription")
    def scope_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeName")
    def scope_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RiskConfigurationAccountTakeoverRiskConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions: outputs.RiskConfigurationAccountTakeoverRiskConfigurationActions, notify_configuration: Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> outputs.RiskConfigurationAccountTakeoverRiskConfigurationActions:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notifyConfiguration")
    def notify_configuration(self) -> Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration]:
        
        ...
    


@pulumi.output_type
class RiskConfigurationAccountTakeoverRiskConfigurationActions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, high_action: Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction] = ..., low_action: Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction] = ..., medium_action: Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="highAction")
    def high_action(self) -> Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowAction")
    def low_action(self) -> Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediumAction")
    def medium_action(self) -> Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction]:
        
        ...
    


@pulumi.output_type
class RiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_action: _builtins.str, notify: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventAction")
    def event_action(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def notify(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class RiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_action: _builtins.str, notify: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventAction")
    def event_action(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def notify(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class RiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_action: _builtins.str, notify: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventAction")
    def event_action(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def notify(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_arn: _builtins.str, block_email: Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail] = ..., from_: Optional[_builtins.str] = ..., mfa_email: Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail] = ..., no_action_email: Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail] = ..., reply_to: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockEmail")
    def block_email(self) -> Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mfaEmail")
    def mfa_email(self) -> Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noActionEmail")
    def no_action_email(self) -> Optional[outputs.RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replyTo")
    def reply_to(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, html_body: _builtins.str, subject: _builtins.str, text_body: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="htmlBody")
    def html_body(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textBody")
    def text_body(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, html_body: _builtins.str, subject: _builtins.str, text_body: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="htmlBody")
    def html_body(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textBody")
    def text_body(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, html_body: _builtins.str, subject: _builtins.str, text_body: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="htmlBody")
    def html_body(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textBody")
    def text_body(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RiskConfigurationCompromisedCredentialsRiskConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions: outputs.RiskConfigurationCompromisedCredentialsRiskConfigurationActions, event_filters: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> outputs.RiskConfigurationCompromisedCredentialsRiskConfigurationActions:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventFilters")
    def event_filters(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RiskConfigurationCompromisedCredentialsRiskConfigurationActions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_action: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventAction")
    def event_action(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RiskConfigurationRiskExceptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, blocked_ip_range_lists: Optional[Sequence[_builtins.str]] = ..., skipped_ip_range_lists: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockedIpRangeLists")
    def blocked_ip_range_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skippedIpRangeLists")
    def skipped_ip_range_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class UserPoolAccountRecoverySetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, recovery_mechanisms: Optional[Sequence[outputs.UserPoolAccountRecoverySettingRecoveryMechanism]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryMechanisms")
    def recovery_mechanisms(self) -> Optional[Sequence[outputs.UserPoolAccountRecoverySettingRecoveryMechanism]]:
        
        ...
    


@pulumi.output_type
class UserPoolAccountRecoverySettingRecoveryMechanism(dict):
    def __init__(__self__, *, name: _builtins.str, priority: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class UserPoolAdminCreateUserConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_admin_create_user_only: Optional[_builtins.bool] = ..., invite_message_template: Optional[outputs.UserPoolAdminCreateUserConfigInviteMessageTemplate] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAdminCreateUserOnly")
    def allow_admin_create_user_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inviteMessageTemplate")
    def invite_message_template(self) -> Optional[outputs.UserPoolAdminCreateUserConfigInviteMessageTemplate]:
        
        ...
    


@pulumi.output_type
class UserPoolAdminCreateUserConfigInviteMessageTemplate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email_message: Optional[_builtins.str] = ..., email_subject: Optional[_builtins.str] = ..., sms_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailMessage")
    def email_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailSubject")
    def email_subject(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smsMessage")
    def sms_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolClientAnalyticsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_arn: Optional[_builtins.str] = ..., application_id: Optional[_builtins.str] = ..., external_id: Optional[_builtins.str] = ..., role_arn: Optional[_builtins.str] = ..., user_data_shared: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataShared")
    def user_data_shared(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class UserPoolClientRefreshTokenRotation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, feature: _builtins.str, retry_grace_period_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def feature(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryGracePeriodSeconds")
    def retry_grace_period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class UserPoolClientTokenValidityUnits(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_token: Optional[_builtins.str] = ..., id_token: Optional[_builtins.str] = ..., refresh_token: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idToken")
    def id_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolDeviceConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, challenge_required_on_new_device: Optional[_builtins.bool] = ..., device_only_remembered_on_user_prompt: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="challengeRequiredOnNewDevice")
    def challenge_required_on_new_device(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceOnlyRememberedOnUserPrompt")
    def device_only_remembered_on_user_prompt(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class UserPoolEmailConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, configuration_set: Optional[_builtins.str] = ..., email_sending_account: Optional[_builtins.str] = ..., from_email_address: Optional[_builtins.str] = ..., reply_to_email_address: Optional[_builtins.str] = ..., source_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSet")
    def configuration_set(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailSendingAccount")
    def email_sending_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromEmailAddress")
    def from_email_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replyToEmailAddress")
    def reply_to_email_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolEmailMfaConfiguration(dict):
    def __init__(__self__, *, message: Optional[_builtins.str] = ..., subject: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolLambdaConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create_auth_challenge: Optional[_builtins.str] = ..., custom_email_sender: Optional[outputs.UserPoolLambdaConfigCustomEmailSender] = ..., custom_message: Optional[_builtins.str] = ..., custom_sms_sender: Optional[outputs.UserPoolLambdaConfigCustomSmsSender] = ..., define_auth_challenge: Optional[_builtins.str] = ..., kms_key_id: Optional[_builtins.str] = ..., post_authentication: Optional[_builtins.str] = ..., post_confirmation: Optional[_builtins.str] = ..., pre_authentication: Optional[_builtins.str] = ..., pre_sign_up: Optional[_builtins.str] = ..., pre_token_generation: Optional[_builtins.str] = ..., pre_token_generation_config: Optional[outputs.UserPoolLambdaConfigPreTokenGenerationConfig] = ..., user_migration: Optional[_builtins.str] = ..., verify_auth_challenge_response: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createAuthChallenge")
    def create_auth_challenge(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customEmailSender")
    def custom_email_sender(self) -> Optional[outputs.UserPoolLambdaConfigCustomEmailSender]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMessage")
    def custom_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSmsSender")
    def custom_sms_sender(self) -> Optional[outputs.UserPoolLambdaConfigCustomSmsSender]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defineAuthChallenge")
    def define_auth_challenge(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postAuthentication")
    def post_authentication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postConfirmation")
    def post_confirmation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preAuthentication")
    def pre_authentication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preSignUp")
    def pre_sign_up(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preTokenGeneration")
    def pre_token_generation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preTokenGenerationConfig")
    def pre_token_generation_config(self) -> Optional[outputs.UserPoolLambdaConfigPreTokenGenerationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userMigration")
    def user_migration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifyAuthChallengeResponse")
    def verify_auth_challenge_response(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolLambdaConfigCustomEmailSender(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lambda_arn: _builtins.str, lambda_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaVersion")
    def lambda_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UserPoolLambdaConfigCustomSmsSender(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lambda_arn: _builtins.str, lambda_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaVersion")
    def lambda_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UserPoolLambdaConfigPreTokenGenerationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lambda_arn: _builtins.str, lambda_version: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaVersion")
    def lambda_version(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class UserPoolPasswordPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, minimum_length: Optional[_builtins.int] = ..., password_history_size: Optional[_builtins.int] = ..., require_lowercase: Optional[_builtins.bool] = ..., require_numbers: Optional[_builtins.bool] = ..., require_symbols: Optional[_builtins.bool] = ..., require_uppercase: Optional[_builtins.bool] = ..., temporary_password_validity_days: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumLength")
    def minimum_length(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordHistorySize")
    def password_history_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireLowercase")
    def require_lowercase(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireNumbers")
    def require_numbers(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireSymbols")
    def require_symbols(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireUppercase")
    def require_uppercase(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryPasswordValidityDays")
    def temporary_password_validity_days(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class UserPoolSchema(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attribute_data_type: _builtins.str, name: _builtins.str, developer_only_attribute: Optional[_builtins.bool] = ..., mutable: Optional[_builtins.bool] = ..., number_attribute_constraints: Optional[outputs.UserPoolSchemaNumberAttributeConstraints] = ..., required: Optional[_builtins.bool] = ..., string_attribute_constraints: Optional[outputs.UserPoolSchemaStringAttributeConstraints] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeDataType")
    def attribute_data_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerOnlyAttribute")
    def developer_only_attribute(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mutable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberAttributeConstraints")
    def number_attribute_constraints(self) -> Optional[outputs.UserPoolSchemaNumberAttributeConstraints]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringAttributeConstraints")
    def string_attribute_constraints(self) -> Optional[outputs.UserPoolSchemaStringAttributeConstraints]:
        
        ...
    


@pulumi.output_type
class UserPoolSchemaNumberAttributeConstraints(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_value: Optional[_builtins.str] = ..., min_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolSchemaStringAttributeConstraints(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_length: Optional[_builtins.str] = ..., min_length: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minLength")
    def min_length(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolSignInPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_first_auth_factors: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedFirstAuthFactors")
    def allowed_first_auth_factors(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class UserPoolSmsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_id: _builtins.str, sns_caller_arn: _builtins.str, sns_region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsCallerArn")
    def sns_caller_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsRegion")
    def sns_region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolSoftwareTokenMfaConfiguration(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class UserPoolUserAttributeUpdateSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attributes_require_verification_before_updates: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributesRequireVerificationBeforeUpdates")
    def attributes_require_verification_before_updates(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolUserPoolAddOns(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, advanced_security_mode: _builtins.str, advanced_security_additional_flows: Optional[outputs.UserPoolUserPoolAddOnsAdvancedSecurityAdditionalFlows] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSecurityMode")
    def advanced_security_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSecurityAdditionalFlows")
    def advanced_security_additional_flows(self) -> Optional[outputs.UserPoolUserPoolAddOnsAdvancedSecurityAdditionalFlows]:
        
        ...
    


@pulumi.output_type
class UserPoolUserPoolAddOnsAdvancedSecurityAdditionalFlows(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_auth_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customAuthMode")
    def custom_auth_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolUsernameConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, case_sensitive: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class UserPoolVerificationMessageTemplate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_email_option: Optional[_builtins.str] = ..., email_message: Optional[_builtins.str] = ..., email_message_by_link: Optional[_builtins.str] = ..., email_subject: Optional[_builtins.str] = ..., email_subject_by_link: Optional[_builtins.str] = ..., sms_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEmailOption")
    def default_email_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailMessage")
    def email_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailMessageByLink")
    def email_message_by_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailSubject")
    def email_subject(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailSubjectByLink")
    def email_subject_by_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smsMessage")
    def sms_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPoolWebAuthnConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, relying_party_id: Optional[_builtins.str] = ..., user_verification: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relyingPartyId")
    def relying_party_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userVerification")
    def user_verification(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetIdentityPoolCognitoIdentityProviderResult(dict):
    def __init__(__self__, *, client_id: _builtins.str, provider_name: _builtins.str, server_side_token_check: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideTokenCheck")
    def server_side_token_check(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class GetUserGroupsGroupResult(dict):
    def __init__(__self__, *, description: _builtins.str, group_name: _builtins.str, precedence: _builtins.int, role_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def precedence(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPoolAccountRecoverySettingResult(dict):
    def __init__(__self__, *, recovery_mechanisms: Sequence[outputs.GetUserPoolAccountRecoverySettingRecoveryMechanismResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryMechanisms")
    def recovery_mechanisms(self) -> Sequence[outputs.GetUserPoolAccountRecoverySettingRecoveryMechanismResult]:
        ...
    


@pulumi.output_type
class GetUserPoolAccountRecoverySettingRecoveryMechanismResult(dict):
    def __init__(__self__, *, name: _builtins.str, priority: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetUserPoolAdminCreateUserConfigResult(dict):
    def __init__(__self__, *, allow_admin_create_user_only: _builtins.bool, invite_message_templates: Sequence[outputs.GetUserPoolAdminCreateUserConfigInviteMessageTemplateResult], unused_account_validity_days: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAdminCreateUserOnly")
    def allow_admin_create_user_only(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inviteMessageTemplates")
    def invite_message_templates(self) -> Sequence[outputs.GetUserPoolAdminCreateUserConfigInviteMessageTemplateResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unusedAccountValidityDays")
    def unused_account_validity_days(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetUserPoolAdminCreateUserConfigInviteMessageTemplateResult(dict):
    def __init__(__self__, *, email_message: _builtins.str, email_subject: _builtins.str, sms_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailMessage")
    def email_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailSubject")
    def email_subject(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smsMessage")
    def sms_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPoolClientAnalyticsConfigurationResult(dict):
    def __init__(__self__, *, application_arn: _builtins.str, application_id: _builtins.str, external_id: _builtins.str, role_arn: _builtins.str, user_data_shared: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataShared")
    def user_data_shared(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetUserPoolClientRefreshTokenRotationResult(dict):
    def __init__(__self__, *, feature: _builtins.str, retry_grace_period_seconds: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def feature(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryGracePeriodSeconds")
    def retry_grace_period_seconds(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetUserPoolClientTokenValidityUnitResult(dict):
    def __init__(__self__, *, access_token: _builtins.str, id_token: _builtins.str, refresh_token: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idToken")
    def id_token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPoolDeviceConfigurationResult(dict):
    def __init__(__self__, *, challenge_required_on_new_device: _builtins.bool, device_only_remembered_on_user_prompt: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="challengeRequiredOnNewDevice")
    def challenge_required_on_new_device(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceOnlyRememberedOnUserPrompt")
    def device_only_remembered_on_user_prompt(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetUserPoolEmailConfigurationResult(dict):
    def __init__(__self__, *, configuration_set: _builtins.str, email_sending_account: _builtins.str, from_: _builtins.str, reply_to_email_address: _builtins.str, source_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSet")
    def configuration_set(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailSendingAccount")
    def email_sending_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replyToEmailAddress")
    def reply_to_email_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPoolLambdaConfigResult(dict):
    def __init__(__self__, *, create_auth_challenge: _builtins.str, custom_email_senders: Sequence[outputs.GetUserPoolLambdaConfigCustomEmailSenderResult], custom_message: _builtins.str, custom_sms_senders: Sequence[outputs.GetUserPoolLambdaConfigCustomSmsSenderResult], define_auth_challenge: _builtins.str, kms_key_id: _builtins.str, post_authentication: _builtins.str, post_confirmation: _builtins.str, pre_authentication: _builtins.str, pre_sign_up: _builtins.str, pre_token_generation: _builtins.str, pre_token_generation_configs: Sequence[outputs.GetUserPoolLambdaConfigPreTokenGenerationConfigResult], user_migration: _builtins.str, verify_auth_challenge_response: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createAuthChallenge")
    def create_auth_challenge(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customEmailSenders")
    def custom_email_senders(self) -> Sequence[outputs.GetUserPoolLambdaConfigCustomEmailSenderResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMessage")
    def custom_message(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSmsSenders")
    def custom_sms_senders(self) -> Sequence[outputs.GetUserPoolLambdaConfigCustomSmsSenderResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defineAuthChallenge")
    def define_auth_challenge(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postAuthentication")
    def post_authentication(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postConfirmation")
    def post_confirmation(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preAuthentication")
    def pre_authentication(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preSignUp")
    def pre_sign_up(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preTokenGeneration")
    def pre_token_generation(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preTokenGenerationConfigs")
    def pre_token_generation_configs(self) -> Sequence[outputs.GetUserPoolLambdaConfigPreTokenGenerationConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userMigration")
    def user_migration(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifyAuthChallengeResponse")
    def verify_auth_challenge_response(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetUserPoolLambdaConfigCustomEmailSenderResult(dict):
    def __init__(__self__, *, lambda_arn: _builtins.str, lambda_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaVersion")
    def lambda_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPoolLambdaConfigCustomSmsSenderResult(dict):
    def __init__(__self__, *, lambda_arn: _builtins.str, lambda_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaVersion")
    def lambda_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPoolLambdaConfigPreTokenGenerationConfigResult(dict):
    def __init__(__self__, *, lambda_arn: _builtins.str, lambda_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaVersion")
    def lambda_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPoolSchemaAttributeResult(dict):
    def __init__(__self__, *, attribute_data_type: _builtins.str, developer_only_attribute: _builtins.bool, mutable: _builtins.bool, name: _builtins.str, number_attribute_constraints: Sequence[outputs.GetUserPoolSchemaAttributeNumberAttributeConstraintResult], required: _builtins.bool, string_attribute_constraints: Sequence[outputs.GetUserPoolSchemaAttributeStringAttributeConstraintResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeDataType")
    def attribute_data_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerOnlyAttribute")
    def developer_only_attribute(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mutable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberAttributeConstraints")
    def number_attribute_constraints(self) -> Sequence[outputs.GetUserPoolSchemaAttributeNumberAttributeConstraintResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringAttributeConstraints")
    def string_attribute_constraints(self) -> Sequence[outputs.GetUserPoolSchemaAttributeStringAttributeConstraintResult]:
        ...
    


@pulumi.output_type
class GetUserPoolSchemaAttributeNumberAttributeConstraintResult(dict):
    def __init__(__self__, *, max_value: _builtins.str, min_value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPoolSchemaAttributeStringAttributeConstraintResult(dict):
    def __init__(__self__, *, max_length: _builtins.str, min_length: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minLength")
    def min_length(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPoolUserPoolAddOnResult(dict):
    def __init__(__self__, *, advanced_security_additional_flows: Sequence[outputs.GetUserPoolUserPoolAddOnAdvancedSecurityAdditionalFlowResult], advanced_security_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSecurityAdditionalFlows")
    def advanced_security_additional_flows(self) -> Sequence[outputs.GetUserPoolUserPoolAddOnAdvancedSecurityAdditionalFlowResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSecurityMode")
    def advanced_security_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPoolUserPoolAddOnAdvancedSecurityAdditionalFlowResult(dict):
    def __init__(__self__, *, custom_auth_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customAuthMode")
    def custom_auth_mode(self) -> _builtins.str:
        
        ...
    


