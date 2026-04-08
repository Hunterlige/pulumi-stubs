import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetActionGroupResult",
    "AwaitableGetActionGroupResult",
    "get_action_group",
    "get_action_group_output",
]

@pulumi.output_type
class GetActionGroupResult:
    def __init__(
        __self__,
        arm_role_receivers=...,
        automation_runbook_receivers=...,
        azure_api_version=...,
        azure_app_push_receivers=...,
        azure_function_receivers=...,
        email_receivers=...,
        enabled=...,
        event_hub_receivers=...,
        group_short_name=...,
        id=...,
        identity=...,
        incident_receivers=...,
        itsm_receivers=...,
        location=...,
        logic_app_receivers=...,
        name=...,
        sms_receivers=...,
        tags=...,
        type=...,
        voice_receivers=...,
        webhook_receivers=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="armRoleReceivers")
    def arm_role_receivers(
        self,
    ) -> Optional[Sequence[outputs.ArmRoleReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="automationRunbookReceivers")
    def automation_runbook_receivers(
        self,
    ) -> Optional[Sequence[outputs.AutomationRunbookReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureAppPushReceivers")
    def azure_app_push_receivers(
        self,
    ) -> Optional[Sequence[outputs.AzureAppPushReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureFunctionReceivers")
    def azure_function_receivers(
        self,
    ) -> Optional[Sequence[outputs.AzureFunctionReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="emailReceivers")
    def email_receivers(self) -> Optional[Sequence[outputs.EmailReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="eventHubReceivers")
    def event_hub_receivers(
        self,
    ) -> Optional[Sequence[outputs.EventHubReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="groupShortName")
    def group_short_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="incidentReceivers")
    def incident_receivers(
        self,
    ) -> Optional[Sequence[outputs.IncidentReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="itsmReceivers")
    def itsm_receivers(self) -> Optional[Sequence[outputs.ItsmReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logicAppReceivers")
    def logic_app_receivers(
        self,
    ) -> Optional[Sequence[outputs.LogicAppReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="smsReceivers")
    def sms_receivers(self) -> Optional[Sequence[outputs.SmsReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="voiceReceivers")
    def voice_receivers(self) -> Optional[Sequence[outputs.VoiceReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="webhookReceivers")
    def webhook_receivers(
        self,
    ) -> Optional[Sequence[outputs.WebhookReceiverResponse]]: ...

class AwaitableGetActionGroupResult(GetActionGroupResult):
    def __await__(self): ...

def get_action_group(
    action_group_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetActionGroupResult: ...
def get_action_group_output(
    action_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetActionGroupResult]: ...
