

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SecurityActionArgs', 'SecurityAction']
@pulumi.input_type
class SecurityActionArgs:
    def __init__(__self__, *, condition_config: pulumi.Input[SecurityActionConditionConfigArgs], env_id: pulumi.Input[_builtins.str], org_id: pulumi.Input[_builtins.str], security_action_id: pulumi.Input[_builtins.str], state: pulumi.Input[_builtins.str], allow: Optional[pulumi.Input[SecurityActionAllowArgs]] = ..., api_proxies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deny: Optional[pulumi.Input[SecurityActionDenyArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., flag: Optional[pulumi.Input[SecurityActionFlagArgs]] = ..., ttl: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionConfig")
    def condition_config(self) -> pulumi.Input[SecurityActionConditionConfigArgs]:
        
        ...
    
    @condition_config.setter
    def condition_config(self, value: pulumi.Input[SecurityActionConditionConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="envId")
    def env_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @env_id.setter
    def env_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityActionId")
    def security_action_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @security_action_id.setter
    def security_action_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[pulumi.Input[SecurityActionAllowArgs]]:
        
        ...
    
    @allow.setter
    def allow(self, value: Optional[pulumi.Input[SecurityActionAllowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProxies")
    def api_proxies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @api_proxies.setter
    def api_proxies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deny(self) -> Optional[pulumi.Input[SecurityActionDenyArgs]]:
        
        ...
    
    @deny.setter
    def deny(self, value: Optional[pulumi.Input[SecurityActionDenyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def flag(self) -> Optional[pulumi.Input[SecurityActionFlagArgs]]:
        
        ...
    
    @flag.setter
    def flag(self, value: Optional[pulumi.Input[SecurityActionFlagArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SecurityActionState:
    def __init__(__self__, *, allow: Optional[pulumi.Input[SecurityActionAllowArgs]] = ..., api_proxies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., condition_config: Optional[pulumi.Input[SecurityActionConditionConfigArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deny: Optional[pulumi.Input[SecurityActionDenyArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., env_id: Optional[pulumi.Input[_builtins.str]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., flag: Optional[pulumi.Input[SecurityActionFlagArgs]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., security_action_id: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., ttl: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[pulumi.Input[SecurityActionAllowArgs]]:
        
        ...
    
    @allow.setter
    def allow(self, value: Optional[pulumi.Input[SecurityActionAllowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProxies")
    def api_proxies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @api_proxies.setter
    def api_proxies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionConfig")
    def condition_config(self) -> Optional[pulumi.Input[SecurityActionConditionConfigArgs]]:
        
        ...
    
    @condition_config.setter
    def condition_config(self, value: Optional[pulumi.Input[SecurityActionConditionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deny(self) -> Optional[pulumi.Input[SecurityActionDenyArgs]]:
        
        ...
    
    @deny.setter
    def deny(self, value: Optional[pulumi.Input[SecurityActionDenyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="envId")
    def env_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @env_id.setter
    def env_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def flag(self) -> Optional[pulumi.Input[SecurityActionFlagArgs]]:
        
        ...
    
    @flag.setter
    def flag(self, value: Optional[pulumi.Input[SecurityActionFlagArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityActionId")
    def security_action_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_action_id.setter
    def security_action_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apigee/securityAction:SecurityAction")
class SecurityAction(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow: Optional[pulumi.Input[Union[SecurityActionAllowArgs, SecurityActionAllowArgsDict]]] = ..., api_proxies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., condition_config: Optional[pulumi.Input[Union[SecurityActionConditionConfigArgs, SecurityActionConditionConfigArgsDict]]] = ..., deny: Optional[pulumi.Input[Union[SecurityActionDenyArgs, SecurityActionDenyArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., env_id: Optional[pulumi.Input[_builtins.str]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., flag: Optional[pulumi.Input[Union[SecurityActionFlagArgs, SecurityActionFlagArgsDict]]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., security_action_id: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., ttl: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SecurityActionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allow: Optional[pulumi.Input[Union[SecurityActionAllowArgs, SecurityActionAllowArgsDict]]] = ..., api_proxies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., condition_config: Optional[pulumi.Input[Union[SecurityActionConditionConfigArgs, SecurityActionConditionConfigArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deny: Optional[pulumi.Input[Union[SecurityActionDenyArgs, SecurityActionDenyArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., env_id: Optional[pulumi.Input[_builtins.str]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., flag: Optional[pulumi.Input[Union[SecurityActionFlagArgs, SecurityActionFlagArgsDict]]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., security_action_id: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., ttl: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> SecurityAction:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> pulumi.Output[Optional[outputs.SecurityActionAllow]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProxies")
    def api_proxies(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionConfig")
    def condition_config(self) -> pulumi.Output[outputs.SecurityActionConditionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deny(self) -> pulumi.Output[Optional[outputs.SecurityActionDeny]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="envId")
    def env_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flag(self) -> pulumi.Output[Optional[outputs.SecurityActionFlag]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityActionId")
    def security_action_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


