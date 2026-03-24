

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLambdaFunctionAssociationResult', 'AwaitableGetLambdaFunctionAssociationResult', 'get_lambda_function_association', 'get_lambda_function_association_output']
@pulumi.output_type
class GetLambdaFunctionAssociationResult:
    
    def __init__(__self__, function_arn=..., id=..., instance_id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetLambdaFunctionAssociationResult(GetLambdaFunctionAssociationResult):
    def __await__(self): # -> Generator[Never, Any, GetLambdaFunctionAssociationResult]:
        ...
    


def get_lambda_function_association(function_arn: Optional[_builtins.str] = ..., instance_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLambdaFunctionAssociationResult:
    
    ...

def get_lambda_function_association_output(function_arn: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLambdaFunctionAssociationResult]:
    
    ...

