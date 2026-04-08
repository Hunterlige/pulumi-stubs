import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SmtpUsernameArgs", "SmtpUsername"]

@pulumi.input_type
class SmtpUsernameArgs:
    def __init__(
        __self__,
        *,
        communication_service_name: pulumi.Input[_builtins.str],
        entra_application_id: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        tenant_id: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
        smtp_username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="communicationServiceName")
    def communication_service_name(self) -> pulumi.Input[_builtins.str]: ...
    @communication_service_name.setter
    def communication_service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="entraApplicationId")
    def entra_application_id(self) -> pulumi.Input[_builtins.str]: ...
    @entra_application_id.setter
    def entra_application_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="smtpUsername")
    def smtp_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @smtp_username.setter
    def smtp_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:communication:SmtpUsername")
class SmtpUsername(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        communication_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        entra_application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        smtp_username: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SmtpUsernameArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SmtpUsername: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entraApplicationId")
    def entra_application_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Output[_builtins.str]: ...
