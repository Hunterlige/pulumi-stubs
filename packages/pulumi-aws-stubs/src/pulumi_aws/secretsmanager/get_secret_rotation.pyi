

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecretRotationResult', 'AwaitableGetSecretRotationResult', 'get_secret_rotation', 'get_secret_rotation_output']
@pulumi.output_type
class GetSecretRotationResult:
    
    def __init__(__self__, id=..., region=..., rotation_enabled=..., rotation_lambda_arn=..., rotation_rules=..., secret_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationEnabled")
    def rotation_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationLambdaArn")
    def rotation_lambda_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationRules")
    def rotation_rules(self) -> Sequence[outputs.GetSecretRotationRotationRuleResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str:
        ...
    


class AwaitableGetSecretRotationResult(GetSecretRotationResult):
    def __await__(self): # -> Generator[Never, Any, GetSecretRotationResult]:
        ...
    


def get_secret_rotation(region: Optional[_builtins.str] = ..., secret_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecretRotationResult:
    
    ...

def get_secret_rotation_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., secret_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecretRotationResult]:
    
    ...

