

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebhookResult', 'AwaitableGetWebhookResult', 'get_webhook', 'get_webhook_output']
@pulumi.output_type
class GetWebhookResult:
    
    def __init__(__self__, azure_api_version=..., content_type=..., delivery_status=..., enable_ssl_verification=..., events=..., id=..., name=..., payload_url=..., provisioning_state=..., send_all_events=..., status=..., system_data=..., tenant_id=..., type=..., update_webhook_key=..., webhook_id=..., webhook_key=..., webhook_key_enabled=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryStatus")
    def delivery_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSslVerification")
    def enable_ssl_verification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadUrl")
    def payload_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendAllEvents")
    def send_all_events(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateWebhookKey")
    def update_webhook_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookId")
    def webhook_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookKey")
    def webhook_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookKeyEnabled")
    def webhook_key_enabled(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWebhookResult(GetWebhookResult):
    def __await__(self): # -> Generator[Never, Any, GetWebhookResult]:
        ...
    


def get_webhook(report_name: Optional[_builtins.str] = ..., webhook_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebhookResult:
    
    ...

def get_webhook_output(report_name: Optional[pulumi.Input[_builtins.str]] = ..., webhook_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebhookResult]:
    
    ...

