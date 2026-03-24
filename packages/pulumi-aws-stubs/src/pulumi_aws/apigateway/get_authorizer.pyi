

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAuthorizerResult', 'AwaitableGetAuthorizerResult', 'get_authorizer', 'get_authorizer_output']
@pulumi.output_type
class GetAuthorizerResult:
    
    def __init__(__self__, arn=..., authorizer_credentials=..., authorizer_id=..., authorizer_result_ttl_in_seconds=..., authorizer_uri=..., id=..., identity_source=..., identity_validation_expression=..., name=..., provider_arns=..., region=..., rest_api_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerCredentials")
    def authorizer_credentials(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identitySource")
    def identity_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerArns")
    def provider_arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAuthorizerResult(GetAuthorizerResult):
    def __await__(self): # -> Generator[Never, Any, GetAuthorizerResult]:
        ...
    


def get_authorizer(authorizer_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., rest_api_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAuthorizerResult:
    
    ...

def get_authorizer_output(authorizer_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., rest_api_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAuthorizerResult]:
    
    ...

