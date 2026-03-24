

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ServerSecurityAlertPolicyArgs', 'ServerSecurityAlertPolicy']
@pulumi.input_type
class ServerSecurityAlertPolicyArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], state: pulumi.Input[SecurityAlertsPolicyState], disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., email_account_admins: Optional[pulumi.Input[_builtins.bool]] = ..., email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., retention_days: Optional[pulumi.Input[_builtins.int]] = ..., security_alert_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_access_key: Optional[pulumi.Input[_builtins.str]] = ..., storage_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[SecurityAlertsPolicyState]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[SecurityAlertsPolicyState]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @disabled_alerts.setter
    def disabled_alerts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAccountAdmins")
    def email_account_admins(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @email_account_admins.setter
    def email_account_admins(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @email_addresses.setter
    def email_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityAlertPolicyName")
    def security_alert_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_alert_policy_name.setter
    def security_alert_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_access_key.setter
    def storage_account_access_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_endpoint.setter
    def storage_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:ServerSecurityAlertPolicy")
class ServerSecurityAlertPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., email_account_admins: Optional[pulumi.Input[_builtins.bool]] = ..., email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., retention_days: Optional[pulumi.Input[_builtins.int]] = ..., security_alert_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[SecurityAlertsPolicyState]] = ..., storage_account_access_key: Optional[pulumi.Input[_builtins.str]] = ..., storage_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServerSecurityAlertPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ServerSecurityAlertPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAccountAdmins")
    def email_account_admins(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


