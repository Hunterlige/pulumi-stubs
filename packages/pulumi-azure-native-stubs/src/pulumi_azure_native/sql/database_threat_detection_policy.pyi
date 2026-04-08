import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DatabaseThreatDetectionPolicyArgs", "DatabaseThreatDetectionPolicy"]

@pulumi.input_type
class DatabaseThreatDetectionPolicyArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        server_name: pulumi.Input[_builtins.str],
        state: pulumi.Input[Union[_builtins.str, SecurityAlertPolicyState]],
        disabled_alerts: Optional[pulumi.Input[_builtins.str]] = ...,
        email_account_admins: Optional[
            pulumi.Input[Union[_builtins.str, SecurityAlertPolicyEmailAccountAdmins]]
        ] = ...,
        email_addresses: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        security_alert_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_access_key: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        use_server_default: Optional[
            pulumi.Input[Union[_builtins.str, SecurityAlertPolicyUseServerDefault]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]: ...
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[_builtins.str, SecurityAlertPolicyState]]: ...
    @state.setter
    def state(
        self, value: pulumi.Input[Union[_builtins.str, SecurityAlertPolicyState]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disabled_alerts.setter
    def disabled_alerts(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailAccountAdmins")
    def email_account_admins(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, SecurityAlertPolicyEmailAccountAdmins]]
    ]: ...
    @email_account_admins.setter
    def email_account_admins(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, SecurityAlertPolicyEmailAccountAdmins]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_addresses.setter
    def email_addresses(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="securityAlertPolicyName")
    def security_alert_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_alert_policy_name.setter
    def security_alert_policy_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_access_key.setter
    def storage_account_access_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_endpoint.setter
    def storage_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useServerDefault")
    def use_server_default(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, SecurityAlertPolicyUseServerDefault]]
    ]: ...
    @use_server_default.setter
    def use_server_default(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, SecurityAlertPolicyUseServerDefault]]
        ],
    ): ...

@pulumi.type_token("azure-native:sql:DatabaseThreatDetectionPolicy")
class DatabaseThreatDetectionPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled_alerts: Optional[pulumi.Input[_builtins.str]] = ...,
        email_account_admins: Optional[
            pulumi.Input[Union[_builtins.str, SecurityAlertPolicyEmailAccountAdmins]]
        ] = ...,
        email_addresses: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        security_alert_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[
            pulumi.Input[Union[_builtins.str, SecurityAlertPolicyState]]
        ] = ...,
        storage_account_access_key: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        use_server_default: Optional[
            pulumi.Input[Union[_builtins.str, SecurityAlertPolicyUseServerDefault]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DatabaseThreatDetectionPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DatabaseThreatDetectionPolicy: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="emailAccountAdmins")
    def email_account_admins(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useServerDefault")
    def use_server_default(self) -> pulumi.Output[Optional[_builtins.str]]: ...
