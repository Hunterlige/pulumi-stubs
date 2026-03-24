

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTenantActionGroupResult', 'AwaitableGetTenantActionGroupResult', 'get_tenant_action_group', 'get_tenant_action_group_output']
@pulumi.output_type
class GetTenantActionGroupResult:
    
    def __init__(__self__, azure_api_version=..., azure_app_push_receivers=..., email_receivers=..., enabled=..., group_short_name=..., id=..., location=..., name=..., sms_receivers=..., tags=..., type=..., voice_receivers=..., webhook_receivers=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureAppPushReceivers")
    def azure_app_push_receivers(self) -> Optional[Sequence[outputs.AzureAppPushReceiverResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailReceivers")
    def email_receivers(self) -> Optional[Sequence[outputs.EmailReceiverResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupShortName")
    def group_short_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smsReceivers")
    def sms_receivers(self) -> Optional[Sequence[outputs.SmsReceiverResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceReceivers")
    def voice_receivers(self) -> Optional[Sequence[outputs.VoiceReceiverResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookReceivers")
    def webhook_receivers(self) -> Optional[Sequence[outputs.WebhookReceiverResponse]]:
        
        ...
    


class AwaitableGetTenantActionGroupResult(GetTenantActionGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetTenantActionGroupResult]:
        ...
    


def get_tenant_action_group(management_group_id: Optional[_builtins.str] = ..., tenant_action_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTenantActionGroupResult:
    
    ...

def get_tenant_action_group_output(management_group_id: Optional[pulumi.Input[_builtins.str]] = ..., tenant_action_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTenantActionGroupResult]:
    
    ...

