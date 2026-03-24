

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutoscalingPolicyArgs', 'AutoscalingPolicy']
@pulumi.input_type
class AutoscalingPolicyArgs:
    def __init__(__self__, *, policy_id: pulumi.Input[_builtins.str], basic_algorithm: Optional[pulumi.Input[AutoscalingPolicyBasicAlgorithmArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., secondary_worker_config: Optional[pulumi.Input[AutoscalingPolicySecondaryWorkerConfigArgs]] = ..., worker_config: Optional[pulumi.Input[AutoscalingPolicyWorkerConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_id.setter
    def policy_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAlgorithm")
    def basic_algorithm(self) -> Optional[pulumi.Input[AutoscalingPolicyBasicAlgorithmArgs]]:
        
        ...
    
    @basic_algorithm.setter
    def basic_algorithm(self, value: Optional[pulumi.Input[AutoscalingPolicyBasicAlgorithmArgs]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryWorkerConfig")
    def secondary_worker_config(self) -> Optional[pulumi.Input[AutoscalingPolicySecondaryWorkerConfigArgs]]:
        
        ...
    
    @secondary_worker_config.setter
    def secondary_worker_config(self, value: Optional[pulumi.Input[AutoscalingPolicySecondaryWorkerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> Optional[pulumi.Input[AutoscalingPolicyWorkerConfigArgs]]:
        
        ...
    
    @worker_config.setter
    def worker_config(self, value: Optional[pulumi.Input[AutoscalingPolicyWorkerConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AutoscalingPolicyState:
    def __init__(__self__, *, basic_algorithm: Optional[pulumi.Input[AutoscalingPolicyBasicAlgorithmArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., secondary_worker_config: Optional[pulumi.Input[AutoscalingPolicySecondaryWorkerConfigArgs]] = ..., worker_config: Optional[pulumi.Input[AutoscalingPolicyWorkerConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAlgorithm")
    def basic_algorithm(self) -> Optional[pulumi.Input[AutoscalingPolicyBasicAlgorithmArgs]]:
        
        ...
    
    @basic_algorithm.setter
    def basic_algorithm(self, value: Optional[pulumi.Input[AutoscalingPolicyBasicAlgorithmArgs]]): # -> None:
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
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryWorkerConfig")
    def secondary_worker_config(self) -> Optional[pulumi.Input[AutoscalingPolicySecondaryWorkerConfigArgs]]:
        
        ...
    
    @secondary_worker_config.setter
    def secondary_worker_config(self, value: Optional[pulumi.Input[AutoscalingPolicySecondaryWorkerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> Optional[pulumi.Input[AutoscalingPolicyWorkerConfigArgs]]:
        
        ...
    
    @worker_config.setter
    def worker_config(self, value: Optional[pulumi.Input[AutoscalingPolicyWorkerConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dataproc/autoscalingPolicy:AutoscalingPolicy")
class AutoscalingPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., basic_algorithm: Optional[pulumi.Input[Union[AutoscalingPolicyBasicAlgorithmArgs, AutoscalingPolicyBasicAlgorithmArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., secondary_worker_config: Optional[pulumi.Input[Union[AutoscalingPolicySecondaryWorkerConfigArgs, AutoscalingPolicySecondaryWorkerConfigArgsDict]]] = ..., worker_config: Optional[pulumi.Input[Union[AutoscalingPolicyWorkerConfigArgs, AutoscalingPolicyWorkerConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AutoscalingPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., basic_algorithm: Optional[pulumi.Input[Union[AutoscalingPolicyBasicAlgorithmArgs, AutoscalingPolicyBasicAlgorithmArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., secondary_worker_config: Optional[pulumi.Input[Union[AutoscalingPolicySecondaryWorkerConfigArgs, AutoscalingPolicySecondaryWorkerConfigArgsDict]]] = ..., worker_config: Optional[pulumi.Input[Union[AutoscalingPolicyWorkerConfigArgs, AutoscalingPolicyWorkerConfigArgsDict]]] = ...) -> AutoscalingPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAlgorithm")
    def basic_algorithm(self) -> pulumi.Output[Optional[outputs.AutoscalingPolicyBasicAlgorithm]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryWorkerConfig")
    def secondary_worker_config(self) -> pulumi.Output[Optional[outputs.AutoscalingPolicySecondaryWorkerConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> pulumi.Output[Optional[outputs.AutoscalingPolicyWorkerConfig]]:
        
        ...
    


