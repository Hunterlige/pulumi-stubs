

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkspaceServiceAccountTokenArgs', 'WorkspaceServiceAccountToken']
@pulumi.input_type
class WorkspaceServiceAccountTokenArgs:
    def __init__(__self__, *, seconds_to_live: pulumi.Input[_builtins.int], service_account_id: pulumi.Input[_builtins.str], workspace_id: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @seconds_to_live.setter
    def seconds_to_live(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_account_id.setter
    def service_account_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkspaceServiceAccountTokenState:
    def __init__(__self__, *, created_at: Optional[pulumi.Input[_builtins.str]] = ..., expires_at: Optional[pulumi.Input[_builtins.str]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., seconds_to_live: Optional[pulumi.Input[_builtins.int]] = ..., service_account_id: Optional[pulumi.Input[_builtins.str]] = ..., service_account_token_id: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @seconds_to_live.setter
    def seconds_to_live(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountTokenId")
    def service_account_token_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_token_id.setter
    def service_account_token_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class WorkspaceServiceAccountToken(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., seconds_to_live: Optional[pulumi.Input[_builtins.int]] = ..., service_account_id: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkspaceServiceAccountTokenArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., expires_at: Optional[pulumi.Input[_builtins.str]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., seconds_to_live: Optional[pulumi.Input[_builtins.int]] = ..., service_account_id: Optional[pulumi.Input[_builtins.str]] = ..., service_account_token_id: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ...) -> WorkspaceServiceAccountToken:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountTokenId")
    def service_account_token_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


