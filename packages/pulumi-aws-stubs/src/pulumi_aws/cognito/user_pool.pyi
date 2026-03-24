import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserPoolArgs", "UserPool"]

@pulumi.input_type
class UserPoolArgs:
    def __init__(
        __self__,
        *,
        account_recovery_setting: Optional[
            pulumi.Input[UserPoolAccountRecoverySettingArgs]
        ] = ...,
        admin_create_user_config: Optional[
            pulumi.Input[UserPoolAdminCreateUserConfigArgs]
        ] = ...,
        alias_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        auto_verified_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        device_configuration: Optional[
            pulumi.Input[UserPoolDeviceConfigurationArgs]
        ] = ...,
        email_configuration: Optional[
            pulumi.Input[UserPoolEmailConfigurationArgs]
        ] = ...,
        email_mfa_configuration: Optional[
            pulumi.Input[UserPoolEmailMfaConfigurationArgs]
        ] = ...,
        email_verification_message: Optional[pulumi.Input[_builtins.str]] = ...,
        email_verification_subject: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_config: Optional[pulumi.Input[UserPoolLambdaConfigArgs]] = ...,
        mfa_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password_policy: Optional[pulumi.Input[UserPoolPasswordPolicyArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schemas: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserPoolSchemaArgs]]]
        ] = ...,
        sign_in_policy: Optional[pulumi.Input[UserPoolSignInPolicyArgs]] = ...,
        sms_authentication_message: Optional[pulumi.Input[_builtins.str]] = ...,
        sms_configuration: Optional[pulumi.Input[UserPoolSmsConfigurationArgs]] = ...,
        sms_verification_message: Optional[pulumi.Input[_builtins.str]] = ...,
        software_token_mfa_configuration: Optional[
            pulumi.Input[UserPoolSoftwareTokenMfaConfigurationArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_attribute_update_settings: Optional[
            pulumi.Input[UserPoolUserAttributeUpdateSettingsArgs]
        ] = ...,
        user_pool_add_ons: Optional[pulumi.Input[UserPoolUserPoolAddOnsArgs]] = ...,
        user_pool_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        username_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        username_configuration: Optional[
            pulumi.Input[UserPoolUsernameConfigurationArgs]
        ] = ...,
        verification_message_template: Optional[
            pulumi.Input[UserPoolVerificationMessageTemplateArgs]
        ] = ...,
        web_authn_configuration: Optional[
            pulumi.Input[UserPoolWebAuthnConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountRecoverySetting")
    def account_recovery_setting(
        self,
    ) -> Optional[pulumi.Input[UserPoolAccountRecoverySettingArgs]]: ...
    @account_recovery_setting.setter
    def account_recovery_setting(
        self, value: Optional[pulumi.Input[UserPoolAccountRecoverySettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="adminCreateUserConfig")
    def admin_create_user_config(
        self,
    ) -> Optional[pulumi.Input[UserPoolAdminCreateUserConfigArgs]]: ...
    @admin_create_user_config.setter
    def admin_create_user_config(
        self, value: Optional[pulumi.Input[UserPoolAdminCreateUserConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="aliasAttributes")
    def alias_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @alias_attributes.setter
    def alias_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoVerifiedAttributes")
    def auto_verified_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @auto_verified_attributes.setter
    def auto_verified_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deviceConfiguration")
    def device_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolDeviceConfigurationArgs]]: ...
    @device_configuration.setter
    def device_configuration(
        self, value: Optional[pulumi.Input[UserPoolDeviceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailConfiguration")
    def email_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolEmailConfigurationArgs]]: ...
    @email_configuration.setter
    def email_configuration(
        self, value: Optional[pulumi.Input[UserPoolEmailConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailMfaConfiguration")
    def email_mfa_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolEmailMfaConfigurationArgs]]: ...
    @email_mfa_configuration.setter
    def email_mfa_configuration(
        self, value: Optional[pulumi.Input[UserPoolEmailMfaConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailVerificationMessage")
    def email_verification_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_verification_message.setter
    def email_verification_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailVerificationSubject")
    def email_verification_subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_verification_subject.setter
    def email_verification_subject(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(self) -> Optional[pulumi.Input[UserPoolLambdaConfigArgs]]: ...
    @lambda_config.setter
    def lambda_config(
        self, value: Optional[pulumi.Input[UserPoolLambdaConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mfaConfiguration")
    def mfa_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mfa_configuration.setter
    def mfa_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordPolicy")
    def password_policy(self) -> Optional[pulumi.Input[UserPoolPasswordPolicyArgs]]: ...
    @password_policy.setter
    def password_policy(
        self, value: Optional[pulumi.Input[UserPoolPasswordPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserPoolSchemaArgs]]]]: ...
    @schemas.setter
    def schemas(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserPoolSchemaArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signInPolicy")
    def sign_in_policy(self) -> Optional[pulumi.Input[UserPoolSignInPolicyArgs]]: ...
    @sign_in_policy.setter
    def sign_in_policy(
        self, value: Optional[pulumi.Input[UserPoolSignInPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="smsAuthenticationMessage")
    def sms_authentication_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sms_authentication_message.setter
    def sms_authentication_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="smsConfiguration")
    def sms_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolSmsConfigurationArgs]]: ...
    @sms_configuration.setter
    def sms_configuration(
        self, value: Optional[pulumi.Input[UserPoolSmsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="smsVerificationMessage")
    def sms_verification_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sms_verification_message.setter
    def sms_verification_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softwareTokenMfaConfiguration")
    def software_token_mfa_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolSoftwareTokenMfaConfigurationArgs]]: ...
    @software_token_mfa_configuration.setter
    def software_token_mfa_configuration(
        self, value: Optional[pulumi.Input[UserPoolSoftwareTokenMfaConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAttributeUpdateSettings")
    def user_attribute_update_settings(
        self,
    ) -> Optional[pulumi.Input[UserPoolUserAttributeUpdateSettingsArgs]]: ...
    @user_attribute_update_settings.setter
    def user_attribute_update_settings(
        self, value: Optional[pulumi.Input[UserPoolUserAttributeUpdateSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userPoolAddOns")
    def user_pool_add_ons(
        self,
    ) -> Optional[pulumi.Input[UserPoolUserPoolAddOnsArgs]]: ...
    @user_pool_add_ons.setter
    def user_pool_add_ons(
        self, value: Optional[pulumi.Input[UserPoolUserPoolAddOnsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userPoolTier")
    def user_pool_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_pool_tier.setter
    def user_pool_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="usernameAttributes")
    def username_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @username_attributes.setter
    def username_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usernameConfiguration")
    def username_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolUsernameConfigurationArgs]]: ...
    @username_configuration.setter
    def username_configuration(
        self, value: Optional[pulumi.Input[UserPoolUsernameConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="verificationMessageTemplate")
    def verification_message_template(
        self,
    ) -> Optional[pulumi.Input[UserPoolVerificationMessageTemplateArgs]]: ...
    @verification_message_template.setter
    def verification_message_template(
        self, value: Optional[pulumi.Input[UserPoolVerificationMessageTemplateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webAuthnConfiguration")
    def web_authn_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolWebAuthnConfigurationArgs]]: ...
    @web_authn_configuration.setter
    def web_authn_configuration(
        self, value: Optional[pulumi.Input[UserPoolWebAuthnConfigurationArgs]]
    ): ...

@pulumi.input_type
class _UserPoolState:
    def __init__(
        __self__,
        *,
        account_recovery_setting: Optional[
            pulumi.Input[UserPoolAccountRecoverySettingArgs]
        ] = ...,
        admin_create_user_config: Optional[
            pulumi.Input[UserPoolAdminCreateUserConfigArgs]
        ] = ...,
        alias_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_verified_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        creation_date: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        device_configuration: Optional[
            pulumi.Input[UserPoolDeviceConfigurationArgs]
        ] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        email_configuration: Optional[
            pulumi.Input[UserPoolEmailConfigurationArgs]
        ] = ...,
        email_mfa_configuration: Optional[
            pulumi.Input[UserPoolEmailMfaConfigurationArgs]
        ] = ...,
        email_verification_message: Optional[pulumi.Input[_builtins.str]] = ...,
        email_verification_subject: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        estimated_number_of_users: Optional[pulumi.Input[_builtins.int]] = ...,
        lambda_config: Optional[pulumi.Input[UserPoolLambdaConfigArgs]] = ...,
        last_modified_date: Optional[pulumi.Input[_builtins.str]] = ...,
        mfa_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password_policy: Optional[pulumi.Input[UserPoolPasswordPolicyArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schemas: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserPoolSchemaArgs]]]
        ] = ...,
        sign_in_policy: Optional[pulumi.Input[UserPoolSignInPolicyArgs]] = ...,
        sms_authentication_message: Optional[pulumi.Input[_builtins.str]] = ...,
        sms_configuration: Optional[pulumi.Input[UserPoolSmsConfigurationArgs]] = ...,
        sms_verification_message: Optional[pulumi.Input[_builtins.str]] = ...,
        software_token_mfa_configuration: Optional[
            pulumi.Input[UserPoolSoftwareTokenMfaConfigurationArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_attribute_update_settings: Optional[
            pulumi.Input[UserPoolUserAttributeUpdateSettingsArgs]
        ] = ...,
        user_pool_add_ons: Optional[pulumi.Input[UserPoolUserPoolAddOnsArgs]] = ...,
        user_pool_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        username_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        username_configuration: Optional[
            pulumi.Input[UserPoolUsernameConfigurationArgs]
        ] = ...,
        verification_message_template: Optional[
            pulumi.Input[UserPoolVerificationMessageTemplateArgs]
        ] = ...,
        web_authn_configuration: Optional[
            pulumi.Input[UserPoolWebAuthnConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountRecoverySetting")
    def account_recovery_setting(
        self,
    ) -> Optional[pulumi.Input[UserPoolAccountRecoverySettingArgs]]: ...
    @account_recovery_setting.setter
    def account_recovery_setting(
        self, value: Optional[pulumi.Input[UserPoolAccountRecoverySettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="adminCreateUserConfig")
    def admin_create_user_config(
        self,
    ) -> Optional[pulumi.Input[UserPoolAdminCreateUserConfigArgs]]: ...
    @admin_create_user_config.setter
    def admin_create_user_config(
        self, value: Optional[pulumi.Input[UserPoolAdminCreateUserConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="aliasAttributes")
    def alias_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @alias_attributes.setter
    def alias_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoVerifiedAttributes")
    def auto_verified_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @auto_verified_attributes.setter
    def auto_verified_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_domain.setter
    def custom_domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deviceConfiguration")
    def device_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolDeviceConfigurationArgs]]: ...
    @device_configuration.setter
    def device_configuration(
        self, value: Optional[pulumi.Input[UserPoolDeviceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailConfiguration")
    def email_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolEmailConfigurationArgs]]: ...
    @email_configuration.setter
    def email_configuration(
        self, value: Optional[pulumi.Input[UserPoolEmailConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailMfaConfiguration")
    def email_mfa_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolEmailMfaConfigurationArgs]]: ...
    @email_mfa_configuration.setter
    def email_mfa_configuration(
        self, value: Optional[pulumi.Input[UserPoolEmailMfaConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailVerificationMessage")
    def email_verification_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_verification_message.setter
    def email_verification_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailVerificationSubject")
    def email_verification_subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_verification_subject.setter
    def email_verification_subject(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="estimatedNumberOfUsers")
    def estimated_number_of_users(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @estimated_number_of_users.setter
    def estimated_number_of_users(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(self) -> Optional[pulumi.Input[UserPoolLambdaConfigArgs]]: ...
    @lambda_config.setter
    def lambda_config(
        self, value: Optional[pulumi.Input[UserPoolLambdaConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modified_date.setter
    def last_modified_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mfaConfiguration")
    def mfa_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mfa_configuration.setter
    def mfa_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordPolicy")
    def password_policy(self) -> Optional[pulumi.Input[UserPoolPasswordPolicyArgs]]: ...
    @password_policy.setter
    def password_policy(
        self, value: Optional[pulumi.Input[UserPoolPasswordPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserPoolSchemaArgs]]]]: ...
    @schemas.setter
    def schemas(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserPoolSchemaArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signInPolicy")
    def sign_in_policy(self) -> Optional[pulumi.Input[UserPoolSignInPolicyArgs]]: ...
    @sign_in_policy.setter
    def sign_in_policy(
        self, value: Optional[pulumi.Input[UserPoolSignInPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="smsAuthenticationMessage")
    def sms_authentication_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sms_authentication_message.setter
    def sms_authentication_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="smsConfiguration")
    def sms_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolSmsConfigurationArgs]]: ...
    @sms_configuration.setter
    def sms_configuration(
        self, value: Optional[pulumi.Input[UserPoolSmsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="smsVerificationMessage")
    def sms_verification_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sms_verification_message.setter
    def sms_verification_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softwareTokenMfaConfiguration")
    def software_token_mfa_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolSoftwareTokenMfaConfigurationArgs]]: ...
    @software_token_mfa_configuration.setter
    def software_token_mfa_configuration(
        self, value: Optional[pulumi.Input[UserPoolSoftwareTokenMfaConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAttributeUpdateSettings")
    def user_attribute_update_settings(
        self,
    ) -> Optional[pulumi.Input[UserPoolUserAttributeUpdateSettingsArgs]]: ...
    @user_attribute_update_settings.setter
    def user_attribute_update_settings(
        self, value: Optional[pulumi.Input[UserPoolUserAttributeUpdateSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userPoolAddOns")
    def user_pool_add_ons(
        self,
    ) -> Optional[pulumi.Input[UserPoolUserPoolAddOnsArgs]]: ...
    @user_pool_add_ons.setter
    def user_pool_add_ons(
        self, value: Optional[pulumi.Input[UserPoolUserPoolAddOnsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userPoolTier")
    def user_pool_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_pool_tier.setter
    def user_pool_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="usernameAttributes")
    def username_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @username_attributes.setter
    def username_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usernameConfiguration")
    def username_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolUsernameConfigurationArgs]]: ...
    @username_configuration.setter
    def username_configuration(
        self, value: Optional[pulumi.Input[UserPoolUsernameConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="verificationMessageTemplate")
    def verification_message_template(
        self,
    ) -> Optional[pulumi.Input[UserPoolVerificationMessageTemplateArgs]]: ...
    @verification_message_template.setter
    def verification_message_template(
        self, value: Optional[pulumi.Input[UserPoolVerificationMessageTemplateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webAuthnConfiguration")
    def web_authn_configuration(
        self,
    ) -> Optional[pulumi.Input[UserPoolWebAuthnConfigurationArgs]]: ...
    @web_authn_configuration.setter
    def web_authn_configuration(
        self, value: Optional[pulumi.Input[UserPoolWebAuthnConfigurationArgs]]
    ): ...

@pulumi.type_token("aws:cognito/userPool:UserPool")
class UserPool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_recovery_setting: Optional[
            pulumi.Input[
                Union[
                    UserPoolAccountRecoverySettingArgs,
                    UserPoolAccountRecoverySettingArgsDict,
                ]
            ]
        ] = ...,
        admin_create_user_config: Optional[
            pulumi.Input[
                Union[
                    UserPoolAdminCreateUserConfigArgs,
                    UserPoolAdminCreateUserConfigArgsDict,
                ]
            ]
        ] = ...,
        alias_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        auto_verified_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        device_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolDeviceConfigurationArgs, UserPoolDeviceConfigurationArgsDict
                ]
            ]
        ] = ...,
        email_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolEmailConfigurationArgs, UserPoolEmailConfigurationArgsDict
                ]
            ]
        ] = ...,
        email_mfa_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolEmailMfaConfigurationArgs,
                    UserPoolEmailMfaConfigurationArgsDict,
                ]
            ]
        ] = ...,
        email_verification_message: Optional[pulumi.Input[_builtins.str]] = ...,
        email_verification_subject: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_config: Optional[
            pulumi.Input[Union[UserPoolLambdaConfigArgs, UserPoolLambdaConfigArgsDict]]
        ] = ...,
        mfa_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password_policy: Optional[
            pulumi.Input[
                Union[UserPoolPasswordPolicyArgs, UserPoolPasswordPolicyArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schemas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[UserPoolSchemaArgs, UserPoolSchemaArgsDict]]
                ]
            ]
        ] = ...,
        sign_in_policy: Optional[
            pulumi.Input[Union[UserPoolSignInPolicyArgs, UserPoolSignInPolicyArgsDict]]
        ] = ...,
        sms_authentication_message: Optional[pulumi.Input[_builtins.str]] = ...,
        sms_configuration: Optional[
            pulumi.Input[
                Union[UserPoolSmsConfigurationArgs, UserPoolSmsConfigurationArgsDict]
            ]
        ] = ...,
        sms_verification_message: Optional[pulumi.Input[_builtins.str]] = ...,
        software_token_mfa_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolSoftwareTokenMfaConfigurationArgs,
                    UserPoolSoftwareTokenMfaConfigurationArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_attribute_update_settings: Optional[
            pulumi.Input[
                Union[
                    UserPoolUserAttributeUpdateSettingsArgs,
                    UserPoolUserAttributeUpdateSettingsArgsDict,
                ]
            ]
        ] = ...,
        user_pool_add_ons: Optional[
            pulumi.Input[
                Union[UserPoolUserPoolAddOnsArgs, UserPoolUserPoolAddOnsArgsDict]
            ]
        ] = ...,
        user_pool_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        username_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        username_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolUsernameConfigurationArgs,
                    UserPoolUsernameConfigurationArgsDict,
                ]
            ]
        ] = ...,
        verification_message_template: Optional[
            pulumi.Input[
                Union[
                    UserPoolVerificationMessageTemplateArgs,
                    UserPoolVerificationMessageTemplateArgsDict,
                ]
            ]
        ] = ...,
        web_authn_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolWebAuthnConfigurationArgs,
                    UserPoolWebAuthnConfigurationArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[UserPoolArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_recovery_setting: Optional[
            pulumi.Input[
                Union[
                    UserPoolAccountRecoverySettingArgs,
                    UserPoolAccountRecoverySettingArgsDict,
                ]
            ]
        ] = ...,
        admin_create_user_config: Optional[
            pulumi.Input[
                Union[
                    UserPoolAdminCreateUserConfigArgs,
                    UserPoolAdminCreateUserConfigArgsDict,
                ]
            ]
        ] = ...,
        alias_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_verified_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        creation_date: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        device_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolDeviceConfigurationArgs, UserPoolDeviceConfigurationArgsDict
                ]
            ]
        ] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        email_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolEmailConfigurationArgs, UserPoolEmailConfigurationArgsDict
                ]
            ]
        ] = ...,
        email_mfa_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolEmailMfaConfigurationArgs,
                    UserPoolEmailMfaConfigurationArgsDict,
                ]
            ]
        ] = ...,
        email_verification_message: Optional[pulumi.Input[_builtins.str]] = ...,
        email_verification_subject: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        estimated_number_of_users: Optional[pulumi.Input[_builtins.int]] = ...,
        lambda_config: Optional[
            pulumi.Input[Union[UserPoolLambdaConfigArgs, UserPoolLambdaConfigArgsDict]]
        ] = ...,
        last_modified_date: Optional[pulumi.Input[_builtins.str]] = ...,
        mfa_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password_policy: Optional[
            pulumi.Input[
                Union[UserPoolPasswordPolicyArgs, UserPoolPasswordPolicyArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schemas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[UserPoolSchemaArgs, UserPoolSchemaArgsDict]]
                ]
            ]
        ] = ...,
        sign_in_policy: Optional[
            pulumi.Input[Union[UserPoolSignInPolicyArgs, UserPoolSignInPolicyArgsDict]]
        ] = ...,
        sms_authentication_message: Optional[pulumi.Input[_builtins.str]] = ...,
        sms_configuration: Optional[
            pulumi.Input[
                Union[UserPoolSmsConfigurationArgs, UserPoolSmsConfigurationArgsDict]
            ]
        ] = ...,
        sms_verification_message: Optional[pulumi.Input[_builtins.str]] = ...,
        software_token_mfa_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolSoftwareTokenMfaConfigurationArgs,
                    UserPoolSoftwareTokenMfaConfigurationArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_attribute_update_settings: Optional[
            pulumi.Input[
                Union[
                    UserPoolUserAttributeUpdateSettingsArgs,
                    UserPoolUserAttributeUpdateSettingsArgsDict,
                ]
            ]
        ] = ...,
        user_pool_add_ons: Optional[
            pulumi.Input[
                Union[UserPoolUserPoolAddOnsArgs, UserPoolUserPoolAddOnsArgsDict]
            ]
        ] = ...,
        user_pool_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        username_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        username_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolUsernameConfigurationArgs,
                    UserPoolUsernameConfigurationArgsDict,
                ]
            ]
        ] = ...,
        verification_message_template: Optional[
            pulumi.Input[
                Union[
                    UserPoolVerificationMessageTemplateArgs,
                    UserPoolVerificationMessageTemplateArgsDict,
                ]
            ]
        ] = ...,
        web_authn_configuration: Optional[
            pulumi.Input[
                Union[
                    UserPoolWebAuthnConfigurationArgs,
                    UserPoolWebAuthnConfigurationArgsDict,
                ]
            ]
        ] = ...,
    ) -> UserPool: ...
    @_builtins.property
    @pulumi.getter(name="accountRecoverySetting")
    def account_recovery_setting(
        self,
    ) -> pulumi.Output[Optional[outputs.UserPoolAccountRecoverySetting]]: ...
    @_builtins.property
    @pulumi.getter(name="adminCreateUserConfig")
    def admin_create_user_config(
        self,
    ) -> pulumi.Output[outputs.UserPoolAdminCreateUserConfig]: ...
    @_builtins.property
    @pulumi.getter(name="aliasAttributes")
    def alias_attributes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoVerifiedAttributes")
    def auto_verified_attributes(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deviceConfiguration")
    def device_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.UserPoolDeviceConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailConfiguration")
    def email_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.UserPoolEmailConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="emailMfaConfiguration")
    def email_mfa_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.UserPoolEmailMfaConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="emailVerificationMessage")
    def email_verification_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailVerificationSubject")
    def email_verification_subject(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="estimatedNumberOfUsers")
    def estimated_number_of_users(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(
        self,
    ) -> pulumi.Output[Optional[outputs.UserPoolLambdaConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mfaConfiguration")
    def mfa_configuration(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="passwordPolicy")
    def password_policy(self) -> pulumi.Output[outputs.UserPoolPasswordPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schemas(self) -> pulumi.Output[Optional[Sequence[outputs.UserPoolSchema]]]: ...
    @_builtins.property
    @pulumi.getter(name="signInPolicy")
    def sign_in_policy(self) -> pulumi.Output[outputs.UserPoolSignInPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="smsAuthenticationMessage")
    def sms_authentication_message(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="smsConfiguration")
    def sms_configuration(self) -> pulumi.Output[outputs.UserPoolSmsConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="smsVerificationMessage")
    def sms_verification_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="softwareTokenMfaConfiguration")
    def software_token_mfa_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.UserPoolSoftwareTokenMfaConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userAttributeUpdateSettings")
    def user_attribute_update_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.UserPoolUserAttributeUpdateSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="userPoolAddOns")
    def user_pool_add_ons(
        self,
    ) -> pulumi.Output[Optional[outputs.UserPoolUserPoolAddOns]]: ...
    @_builtins.property
    @pulumi.getter(name="userPoolTier")
    def user_pool_tier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usernameAttributes")
    def username_attributes(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="usernameConfiguration")
    def username_configuration(
        self,
    ) -> pulumi.Output[outputs.UserPoolUsernameConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="verificationMessageTemplate")
    def verification_message_template(
        self,
    ) -> pulumi.Output[outputs.UserPoolVerificationMessageTemplate]: ...
    @_builtins.property
    @pulumi.getter(name="webAuthnConfiguration")
    def web_authn_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.UserPoolWebAuthnConfiguration]]: ...
