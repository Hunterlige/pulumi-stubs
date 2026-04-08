import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebhookArgs", "Webhook"]

@pulumi.input_type
class WebhookArgs:
    def __init__(
        __self__,
        *,
        automation_account_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        run_on: Optional[pulumi.Input[_builtins.str]] = ...,
        runbook: Optional[pulumi.Input[RunbookAssociationPropertyArgs]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
        webhook_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runOn")
    def run_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_on.setter
    def run_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def runbook(self) -> Optional[pulumi.Input[RunbookAssociationPropertyArgs]]: ...
    @runbook.setter
    def runbook(
        self, value: Optional[pulumi.Input[RunbookAssociationPropertyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webhookName")
    def webhook_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @webhook_name.setter
    def webhook_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:automation:Webhook")
class Webhook(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        automation_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        run_on: Optional[pulumi.Input[_builtins.str]] = ...,
        runbook: Optional[
            pulumi.Input[
                Union[
                    RunbookAssociationPropertyArgs, RunbookAssociationPropertyArgsDict
                ]
            ]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
        webhook_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebhookArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Webhook: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="lastInvokedTime")
    def last_invoked_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="runOn")
    def run_on(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def runbook(
        self,
    ) -> pulumi.Output[Optional[outputs.RunbookAssociationPropertyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
