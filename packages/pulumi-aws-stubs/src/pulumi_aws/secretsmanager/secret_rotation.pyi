

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
__all__ = ['SecretRotationArgs', 'SecretRotation']
@pulumi.input_type
class SecretRotationArgs:
    def __init__(__self__, *, rotation_rules: pulumi.Input[SecretRotationRotationRulesArgs], secret_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., rotate_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., rotation_lambda_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationRules")
    def rotation_rules(self) -> pulumi.Input[SecretRotationRotationRulesArgs]:
        
        ...
    
    @rotation_rules.setter
    def rotation_rules(self, value: pulumi.Input[SecretRotationRotationRulesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_id.setter
    def secret_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotateImmediately")
    def rotate_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @rotate_immediately.setter
    def rotate_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationLambdaArn")
    def rotation_lambda_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rotation_lambda_arn.setter
    def rotation_lambda_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SecretRotationState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., rotate_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., rotation_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., rotation_lambda_arn: Optional[pulumi.Input[_builtins.str]] = ..., rotation_rules: Optional[pulumi.Input[SecretRotationRotationRulesArgs]] = ..., secret_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotateImmediately")
    def rotate_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @rotate_immediately.setter
    def rotate_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationEnabled")
    def rotation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @rotation_enabled.setter
    def rotation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationLambdaArn")
    def rotation_lambda_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rotation_lambda_arn.setter
    def rotation_lambda_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationRules")
    def rotation_rules(self) -> Optional[pulumi.Input[SecretRotationRotationRulesArgs]]:
        
        ...
    
    @rotation_rules.setter
    def rotation_rules(self, value: Optional[pulumi.Input[SecretRotationRotationRulesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_id.setter
    def secret_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:secretsmanager/secretRotation:SecretRotation")
class SecretRotation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rotate_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., rotation_lambda_arn: Optional[pulumi.Input[_builtins.str]] = ..., rotation_rules: Optional[pulumi.Input[Union[SecretRotationRotationRulesArgs, SecretRotationRotationRulesArgsDict]]] = ..., secret_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SecretRotationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rotate_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., rotation_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., rotation_lambda_arn: Optional[pulumi.Input[_builtins.str]] = ..., rotation_rules: Optional[pulumi.Input[Union[SecretRotationRotationRulesArgs, SecretRotationRotationRulesArgsDict]]] = ..., secret_id: Optional[pulumi.Input[_builtins.str]] = ...) -> SecretRotation:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotateImmediately")
    def rotate_immediately(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationEnabled")
    def rotation_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationLambdaArn")
    def rotation_lambda_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationRules")
    def rotation_rules(self) -> pulumi.Output[outputs.SecretRotationRotationRules]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


