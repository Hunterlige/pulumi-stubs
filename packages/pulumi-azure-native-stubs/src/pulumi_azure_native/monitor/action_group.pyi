

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ActionGroupInitArgs', 'ActionGroup']
@pulumi.input_type
class ActionGroupInitArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., group_short_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], action_group_name: Optional[pulumi.Input[_builtins.str]] = ..., arm_role_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[ArmRoleReceiverArgs]]]] = ..., automation_runbook_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[AutomationRunbookReceiverArgs]]]] = ..., azure_app_push_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[AzureAppPushReceiverArgs]]]] = ..., azure_function_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[AzureFunctionReceiverArgs]]]] = ..., email_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[EmailReceiverArgs]]]] = ..., event_hub_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[EventHubReceiverArgs]]]] = ..., identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ..., incident_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[IncidentReceiverArgs]]]] = ..., itsm_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[ItsmReceiverArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logic_app_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[LogicAppReceiverArgs]]]] = ..., sms_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[SmsReceiverArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., voice_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[VoiceReceiverArgs]]]] = ..., webhook_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[WebhookReceiverArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupShortName")
    def group_short_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_short_name.setter
    def group_short_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupName")
    def action_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action_group_name.setter
    def action_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="armRoleReceivers")
    def arm_role_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ArmRoleReceiverArgs]]]]:
        
        ...
    
    @arm_role_receivers.setter
    def arm_role_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ArmRoleReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationRunbookReceivers")
    def automation_runbook_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AutomationRunbookReceiverArgs]]]]:
        
        ...
    
    @automation_runbook_receivers.setter
    def automation_runbook_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AutomationRunbookReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureAppPushReceivers")
    def azure_app_push_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzureAppPushReceiverArgs]]]]:
        
        ...
    
    @azure_app_push_receivers.setter
    def azure_app_push_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzureAppPushReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFunctionReceivers")
    def azure_function_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzureFunctionReceiverArgs]]]]:
        
        ...
    
    @azure_function_receivers.setter
    def azure_function_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzureFunctionReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailReceivers")
    def email_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EmailReceiverArgs]]]]:
        
        ...
    
    @email_receivers.setter
    def email_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EmailReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubReceivers")
    def event_hub_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EventHubReceiverArgs]]]]:
        
        ...
    
    @event_hub_receivers.setter
    def event_hub_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EventHubReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentReceivers")
    def incident_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IncidentReceiverArgs]]]]:
        
        ...
    
    @incident_receivers.setter
    def incident_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IncidentReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="itsmReceivers")
    def itsm_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ItsmReceiverArgs]]]]:
        
        ...
    
    @itsm_receivers.setter
    def itsm_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ItsmReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicAppReceivers")
    def logic_app_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LogicAppReceiverArgs]]]]:
        
        ...
    
    @logic_app_receivers.setter
    def logic_app_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LogicAppReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smsReceivers")
    def sms_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SmsReceiverArgs]]]]:
        
        ...
    
    @sms_receivers.setter
    def sms_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SmsReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceReceivers")
    def voice_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VoiceReceiverArgs]]]]:
        
        ...
    
    @voice_receivers.setter
    def voice_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VoiceReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookReceivers")
    def webhook_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebhookReceiverArgs]]]]:
        
        ...
    
    @webhook_receivers.setter
    def webhook_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebhookReceiverArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:monitor:ActionGroup")
class ActionGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action_group_name: Optional[pulumi.Input[_builtins.str]] = ..., arm_role_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ArmRoleReceiverArgs, ArmRoleReceiverArgsDict]]]]] = ..., automation_runbook_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AutomationRunbookReceiverArgs, AutomationRunbookReceiverArgsDict]]]]] = ..., azure_app_push_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AzureAppPushReceiverArgs, AzureAppPushReceiverArgsDict]]]]] = ..., azure_function_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AzureFunctionReceiverArgs, AzureFunctionReceiverArgsDict]]]]] = ..., email_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EmailReceiverArgs, EmailReceiverArgsDict]]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., event_hub_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EventHubReceiverArgs, EventHubReceiverArgsDict]]]]] = ..., group_short_name: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]]] = ..., incident_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IncidentReceiverArgs, IncidentReceiverArgsDict]]]]] = ..., itsm_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ItsmReceiverArgs, ItsmReceiverArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logic_app_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LogicAppReceiverArgs, LogicAppReceiverArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sms_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SmsReceiverArgs, SmsReceiverArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., voice_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VoiceReceiverArgs, VoiceReceiverArgsDict]]]]] = ..., webhook_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WebhookReceiverArgs, WebhookReceiverArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ActionGroupInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ActionGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="armRoleReceivers")
    def arm_role_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.ArmRoleReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationRunbookReceivers")
    def automation_runbook_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.AutomationRunbookReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureAppPushReceivers")
    def azure_app_push_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.AzureAppPushReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFunctionReceivers")
    def azure_function_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.AzureFunctionReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailReceivers")
    def email_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.EmailReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubReceivers")
    def event_hub_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.EventHubReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupShortName")
    def group_short_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentReceivers")
    def incident_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.IncidentReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itsmReceivers")
    def itsm_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.ItsmReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicAppReceivers")
    def logic_app_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.LogicAppReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smsReceivers")
    def sms_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.SmsReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceReceivers")
    def voice_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.VoiceReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookReceivers")
    def webhook_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.WebhookReceiverResponse]]]:
        
        ...
    


