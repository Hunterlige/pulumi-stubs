

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerSecurityAlertPolicyResult', 'AwaitableGetServerSecurityAlertPolicyResult', 'get_server_security_alert_policy', 'get_server_security_alert_policy_output']
@pulumi.output_type
class GetServerSecurityAlertPolicyResult:
    
    def __init__(__self__, azure_api_version=..., creation_time=..., disabled_alerts=..., email_account_admins=..., email_addresses=..., id=..., name=..., retention_days=..., state=..., storage_account_access_key=..., storage_endpoint=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAccountAdmins")
    def email_account_admins(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
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
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetServerSecurityAlertPolicyResult(GetServerSecurityAlertPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetServerSecurityAlertPolicyResult]:
        ...
    


def get_server_security_alert_policy(resource_group_name: Optional[_builtins.str] = ..., security_alert_policy_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerSecurityAlertPolicyResult:
    
    ...

def get_server_security_alert_policy_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., security_alert_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerSecurityAlertPolicyResult]:
    
    ...

