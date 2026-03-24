

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PermissionArgs', 'Permission']
@pulumi.input_type
class PermissionArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], function: pulumi.Input[_builtins.str], principal: pulumi.Input[_builtins.str], event_source_token: Optional[pulumi.Input[_builtins.str]] = ..., function_url_auth_type: Optional[pulumi.Input[_builtins.str]] = ..., invoked_via_function_url: Optional[pulumi.Input[_builtins.bool]] = ..., principal_org_id: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_account: Optional[pulumi.Input[_builtins.str]] = ..., source_arn: Optional[pulumi.Input[_builtins.str]] = ..., statement_id: Optional[pulumi.Input[_builtins.str]] = ..., statement_id_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def function(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function.setter
    def function(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSourceToken")
    def event_source_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_source_token.setter
    def event_source_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionUrlAuthType")
    def function_url_auth_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_url_auth_type.setter
    def function_url_auth_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokedViaFunctionUrl")
    def invoked_via_function_url(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @invoked_via_function_url.setter
    def invoked_via_function_url(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalOrgId")
    def principal_org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_org_id.setter
    def principal_org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qualifier.setter
    def qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_account.setter
    def source_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_arn.setter
    def source_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @statement_id.setter
    def statement_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementIdPrefix")
    def statement_id_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @statement_id_prefix.setter
    def statement_id_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _PermissionState:
    def __init__(__self__, *, action: Optional[pulumi.Input[_builtins.str]] = ..., event_source_token: Optional[pulumi.Input[_builtins.str]] = ..., function: Optional[pulumi.Input[_builtins.str]] = ..., function_url_auth_type: Optional[pulumi.Input[_builtins.str]] = ..., invoked_via_function_url: Optional[pulumi.Input[_builtins.bool]] = ..., principal: Optional[pulumi.Input[_builtins.str]] = ..., principal_org_id: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_account: Optional[pulumi.Input[_builtins.str]] = ..., source_arn: Optional[pulumi.Input[_builtins.str]] = ..., statement_id: Optional[pulumi.Input[_builtins.str]] = ..., statement_id_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSourceToken")
    def event_source_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_source_token.setter
    def event_source_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def function(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function.setter
    def function(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionUrlAuthType")
    def function_url_auth_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_url_auth_type.setter
    def function_url_auth_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokedViaFunctionUrl")
    def invoked_via_function_url(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @invoked_via_function_url.setter
    def invoked_via_function_url(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalOrgId")
    def principal_org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_org_id.setter
    def principal_org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qualifier.setter
    def qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_account.setter
    def source_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_arn.setter
    def source_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @statement_id.setter
    def statement_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementIdPrefix")
    def statement_id_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @statement_id_prefix.setter
    def statement_id_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:lambda/permission:Permission")
class Permission(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[_builtins.str]] = ..., event_source_token: Optional[pulumi.Input[_builtins.str]] = ..., function: Optional[pulumi.Input[_builtins.str]] = ..., function_url_auth_type: Optional[pulumi.Input[_builtins.str]] = ..., invoked_via_function_url: Optional[pulumi.Input[_builtins.bool]] = ..., principal: Optional[pulumi.Input[_builtins.str]] = ..., principal_org_id: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_account: Optional[pulumi.Input[_builtins.str]] = ..., source_arn: Optional[pulumi.Input[_builtins.str]] = ..., statement_id: Optional[pulumi.Input[_builtins.str]] = ..., statement_id_prefix: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PermissionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[_builtins.str]] = ..., event_source_token: Optional[pulumi.Input[_builtins.str]] = ..., function: Optional[pulumi.Input[_builtins.str]] = ..., function_url_auth_type: Optional[pulumi.Input[_builtins.str]] = ..., invoked_via_function_url: Optional[pulumi.Input[_builtins.bool]] = ..., principal: Optional[pulumi.Input[_builtins.str]] = ..., principal_org_id: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_account: Optional[pulumi.Input[_builtins.str]] = ..., source_arn: Optional[pulumi.Input[_builtins.str]] = ..., statement_id: Optional[pulumi.Input[_builtins.str]] = ..., statement_id_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> Permission:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSourceToken")
    def event_source_token(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def function(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionUrlAuthType")
    def function_url_auth_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokedViaFunctionUrl")
    def invoked_via_function_url(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalOrgId")
    def principal_org_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementIdPrefix")
    def statement_id_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


