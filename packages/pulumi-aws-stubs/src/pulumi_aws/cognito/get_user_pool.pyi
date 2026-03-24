import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetUserPoolResult",
    "AwaitableGetUserPoolResult",
    "get_user_pool",
    "get_user_pool_output",
]

@pulumi.output_type
class GetUserPoolResult:
    def __init__(
        __self__,
        account_recovery_settings=...,
        admin_create_user_configs=...,
        arn=...,
        auto_verified_attributes=...,
        creation_date=...,
        custom_domain=...,
        deletion_protection=...,
        device_configurations=...,
        domain=...,
        email_configurations=...,
        estimated_number_of_users=...,
        id=...,
        lambda_configs=...,
        last_modified_date=...,
        mfa_configuration=...,
        name=...,
        region=...,
        schema_attributes=...,
        sms_authentication_message=...,
        sms_configuration_failure=...,
        sms_verification_message=...,
        tags=...,
        user_pool_add_ons=...,
        user_pool_id=...,
        user_pool_tags=...,
        username_attributes=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountRecoverySettings")
    def account_recovery_settings(
        self,
    ) -> Sequence[outputs.GetUserPoolAccountRecoverySettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="adminCreateUserConfigs")
    def admin_create_user_configs(
        self,
    ) -> Sequence[outputs.GetUserPoolAdminCreateUserConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoVerifiedAttributes")
    def auto_verified_attributes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceConfigurations")
    def device_configurations(
        self,
    ) -> Sequence[outputs.GetUserPoolDeviceConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="emailConfigurations")
    def email_configurations(
        self,
    ) -> Sequence[outputs.GetUserPoolEmailConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="estimatedNumberOfUsers")
    def estimated_number_of_users(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lambdaConfigs")
    def lambda_configs(self) -> Sequence[outputs.GetUserPoolLambdaConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mfaConfiguration")
    def mfa_configuration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="schemaAttributes")
    def schema_attributes(
        self,
    ) -> Sequence[outputs.GetUserPoolSchemaAttributeResult]: ...
    @_builtins.property
    @pulumi.getter(name="smsAuthenticationMessage")
    def sms_authentication_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="smsConfigurationFailure")
    def sms_configuration_failure(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="smsVerificationMessage")
    def sms_verification_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userPoolAddOns")
    def user_pool_add_ons(self) -> Sequence[outputs.GetUserPoolUserPoolAddOnResult]: ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolTags")
    @_utilities.deprecated("""Use the attribute \"tags\" instead""")
    def user_pool_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usernameAttributes")
    def username_attributes(self) -> Sequence[_builtins.str]: ...

class AwaitableGetUserPoolResult(GetUserPoolResult):
    def __await__(self): ...

def get_user_pool(
    region: Optional[_builtins.str] = ...,
    user_pool_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetUserPoolResult: ...
def get_user_pool_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetUserPoolResult]: ...
