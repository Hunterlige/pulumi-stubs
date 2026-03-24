

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSubscriptionDiagnosticSettingResult', 'AwaitableGetSubscriptionDiagnosticSettingResult', 'get_subscription_diagnostic_setting', 'get_subscription_diagnostic_setting_output']
@pulumi.output_type
class GetSubscriptionDiagnosticSettingResult:
    
    def __init__(__self__, azure_api_version=..., event_hub_authorization_rule_id=..., event_hub_name=..., id=..., logs=..., marketplace_partner_id=..., name=..., service_bus_rule_id=..., storage_account_id=..., system_data=..., type=..., workspace_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubAuthorizationRuleId")
    def event_hub_authorization_rule_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logs(self) -> Optional[Sequence[outputs.SubscriptionLogSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplacePartnerId")
    def marketplace_partner_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusRuleId")
    def service_bus_rule_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetSubscriptionDiagnosticSettingResult(GetSubscriptionDiagnosticSettingResult):
    def __await__(self): # -> Generator[Never, Any, GetSubscriptionDiagnosticSettingResult]:
        ...
    


def get_subscription_diagnostic_setting(name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSubscriptionDiagnosticSettingResult:
    
    ...

def get_subscription_diagnostic_setting_output(name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSubscriptionDiagnosticSettingResult]:
    
    ...

