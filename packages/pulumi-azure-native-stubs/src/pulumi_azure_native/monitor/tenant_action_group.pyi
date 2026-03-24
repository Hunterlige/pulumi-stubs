

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TenantActionGroupArgs', 'TenantActionGroup']
@pulumi.input_type
class TenantActionGroupArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., group_short_name: pulumi.Input[_builtins.str], management_group_id: pulumi.Input[_builtins.str], azure_app_push_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[AzureAppPushReceiverArgs]]]] = ..., email_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[EmailReceiverArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., sms_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[SmsReceiverArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenant_action_group_name: Optional[pulumi.Input[_builtins.str]] = ..., voice_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[VoiceReceiverArgs]]]] = ..., webhook_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[WebhookReceiverArgs]]]] = ...) -> None:
        
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
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureAppPushReceivers")
    def azure_app_push_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzureAppPushReceiverArgs]]]]:
        
        ...
    
    @azure_app_push_receivers.setter
    def azure_app_push_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzureAppPushReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailReceivers")
    def email_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EmailReceiverArgs]]]]:
        
        ...
    
    @email_receivers.setter
    def email_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EmailReceiverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="tenantActionGroupName")
    def tenant_action_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_action_group_name.setter
    def tenant_action_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("azure-native:monitor:TenantActionGroup")
class TenantActionGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., azure_app_push_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AzureAppPushReceiverArgs, AzureAppPushReceiverArgsDict]]]]] = ..., email_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EmailReceiverArgs, EmailReceiverArgsDict]]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., group_short_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., management_group_id: Optional[pulumi.Input[_builtins.str]] = ..., sms_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SmsReceiverArgs, SmsReceiverArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenant_action_group_name: Optional[pulumi.Input[_builtins.str]] = ..., voice_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VoiceReceiverArgs, VoiceReceiverArgsDict]]]]] = ..., webhook_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WebhookReceiverArgs, WebhookReceiverArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TenantActionGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> TenantActionGroup:
        
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
    @pulumi.getter(name="emailReceivers")
    def email_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.EmailReceiverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupShortName")
    def group_short_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
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
    def webhook_receivers(self) -> pulumi.Output[Optional[Sequence[outputs.WebhookReceiverResponseV1]]]:
        
        ...
    


