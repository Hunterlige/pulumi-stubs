

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkspaceConnectionArgs', 'WorkspaceConnection']
@pulumi.input_type
class WorkspaceConnectionArgs:
    def __init__(__self__, *, properties: pulumi.Input[Union[AADAuthTypeWorkspaceConnectionPropertiesArgs, AccessKeyAuthTypeWorkspaceConnectionPropertiesArgs, AccountKeyAuthTypeWorkspaceConnectionPropertiesArgs, ApiKeyAuthWorkspaceConnectionPropertiesArgs, CustomKeysWorkspaceConnectionPropertiesArgs, ManagedIdentityAuthTypeWorkspaceConnectionPropertiesArgs, NoneAuthTypeWorkspaceConnectionPropertiesArgs, OAuth2AuthTypeWorkspaceConnectionPropertiesArgs, PATAuthTypeWorkspaceConnectionPropertiesArgs, SASAuthTypeWorkspaceConnectionPropertiesArgs, ServicePrincipalAuthTypeWorkspaceConnectionPropertiesArgs, UsernamePasswordAuthTypeWorkspaceConnectionPropertiesArgs]], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], connection_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union[AADAuthTypeWorkspaceConnectionPropertiesArgs, AccessKeyAuthTypeWorkspaceConnectionPropertiesArgs, AccountKeyAuthTypeWorkspaceConnectionPropertiesArgs, ApiKeyAuthWorkspaceConnectionPropertiesArgs, CustomKeysWorkspaceConnectionPropertiesArgs, ManagedIdentityAuthTypeWorkspaceConnectionPropertiesArgs, NoneAuthTypeWorkspaceConnectionPropertiesArgs, OAuth2AuthTypeWorkspaceConnectionPropertiesArgs, PATAuthTypeWorkspaceConnectionPropertiesArgs, SASAuthTypeWorkspaceConnectionPropertiesArgs, ServicePrincipalAuthTypeWorkspaceConnectionPropertiesArgs, UsernamePasswordAuthTypeWorkspaceConnectionPropertiesArgs]]:
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[Union[AADAuthTypeWorkspaceConnectionPropertiesArgs, AccessKeyAuthTypeWorkspaceConnectionPropertiesArgs, AccountKeyAuthTypeWorkspaceConnectionPropertiesArgs, ApiKeyAuthWorkspaceConnectionPropertiesArgs, CustomKeysWorkspaceConnectionPropertiesArgs, ManagedIdentityAuthTypeWorkspaceConnectionPropertiesArgs, NoneAuthTypeWorkspaceConnectionPropertiesArgs, OAuth2AuthTypeWorkspaceConnectionPropertiesArgs, PATAuthTypeWorkspaceConnectionPropertiesArgs, SASAuthTypeWorkspaceConnectionPropertiesArgs, ServicePrincipalAuthTypeWorkspaceConnectionPropertiesArgs, UsernamePasswordAuthTypeWorkspaceConnectionPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class WorkspaceConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[Union[AADAuthTypeWorkspaceConnectionPropertiesArgs, AADAuthTypeWorkspaceConnectionPropertiesArgsDict], Union[AccessKeyAuthTypeWorkspaceConnectionPropertiesArgs, AccessKeyAuthTypeWorkspaceConnectionPropertiesArgsDict], Union[AccountKeyAuthTypeWorkspaceConnectionPropertiesArgs, AccountKeyAuthTypeWorkspaceConnectionPropertiesArgsDict], Union[ApiKeyAuthWorkspaceConnectionPropertiesArgs, ApiKeyAuthWorkspaceConnectionPropertiesArgsDict], Union[CustomKeysWorkspaceConnectionPropertiesArgs, CustomKeysWorkspaceConnectionPropertiesArgsDict], Union[ManagedIdentityAuthTypeWorkspaceConnectionPropertiesArgs, ManagedIdentityAuthTypeWorkspaceConnectionPropertiesArgsDict], Union[NoneAuthTypeWorkspaceConnectionPropertiesArgs, NoneAuthTypeWorkspaceConnectionPropertiesArgsDict], Union[OAuth2AuthTypeWorkspaceConnectionPropertiesArgs, OAuth2AuthTypeWorkspaceConnectionPropertiesArgsDict], Union[PATAuthTypeWorkspaceConnectionPropertiesArgs, PATAuthTypeWorkspaceConnectionPropertiesArgsDict], Union[SASAuthTypeWorkspaceConnectionPropertiesArgs, SASAuthTypeWorkspaceConnectionPropertiesArgsDict], Union[ServicePrincipalAuthTypeWorkspaceConnectionPropertiesArgs, ServicePrincipalAuthTypeWorkspaceConnectionPropertiesArgsDict], Union[UsernamePasswordAuthTypeWorkspaceConnectionPropertiesArgs, UsernamePasswordAuthTypeWorkspaceConnectionPropertiesArgsDict]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkspaceConnectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WorkspaceConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


