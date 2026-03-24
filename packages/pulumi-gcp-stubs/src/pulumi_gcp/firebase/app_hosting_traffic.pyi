

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
__all__ = ['AppHostingTrafficArgs', 'AppHostingTraffic']
@pulumi.input_type
class AppHostingTrafficArgs:
    def __init__(__self__, *, backend: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], project: Optional[pulumi.Input[_builtins.str]] = ..., rollout_policy: Optional[pulumi.Input[AppHostingTrafficRolloutPolicyArgs]] = ..., target: Optional[pulumi.Input[AppHostingTrafficTargetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backend(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backend.setter
    def backend(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloutPolicy")
    def rollout_policy(self) -> Optional[pulumi.Input[AppHostingTrafficRolloutPolicyArgs]]:
        
        ...
    
    @rollout_policy.setter
    def rollout_policy(self, value: Optional[pulumi.Input[AppHostingTrafficRolloutPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[AppHostingTrafficTargetArgs]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[AppHostingTrafficTargetArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AppHostingTrafficState:
    def __init__(__self__, *, backend: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., currents: Optional[pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficCurrentArgs]]]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., rollout_policy: Optional[pulumi.Input[AppHostingTrafficRolloutPolicyArgs]] = ..., target: Optional[pulumi.Input[AppHostingTrafficTargetArgs]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backend(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backend.setter
    def backend(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def currents(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficCurrentArgs]]]]:
        
        ...
    
    @currents.setter
    def currents(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficCurrentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloutPolicy")
    def rollout_policy(self) -> Optional[pulumi.Input[AppHostingTrafficRolloutPolicyArgs]]:
        
        ...
    
    @rollout_policy.setter
    def rollout_policy(self, value: Optional[pulumi.Input[AppHostingTrafficRolloutPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[AppHostingTrafficTargetArgs]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[AppHostingTrafficTargetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:firebase/appHostingTraffic:AppHostingTraffic")
class AppHostingTraffic(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backend: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., rollout_policy: Optional[pulumi.Input[Union[AppHostingTrafficRolloutPolicyArgs, AppHostingTrafficRolloutPolicyArgsDict]]] = ..., target: Optional[pulumi.Input[Union[AppHostingTrafficTargetArgs, AppHostingTrafficTargetArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AppHostingTrafficArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., backend: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., currents: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AppHostingTrafficCurrentArgs, AppHostingTrafficCurrentArgsDict]]]]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., rollout_policy: Optional[pulumi.Input[Union[AppHostingTrafficRolloutPolicyArgs, AppHostingTrafficRolloutPolicyArgsDict]]] = ..., target: Optional[pulumi.Input[Union[AppHostingTrafficTargetArgs, AppHostingTrafficTargetArgsDict]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> AppHostingTraffic:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backend(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currents(self) -> pulumi.Output[Sequence[outputs.AppHostingTrafficCurrent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloutPolicy")
    def rollout_policy(self) -> pulumi.Output[Optional[outputs.AppHostingTrafficRolloutPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[outputs.AppHostingTrafficTarget]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


