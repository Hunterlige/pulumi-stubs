

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOriginRequestPolicyResult', 'AwaitableGetOriginRequestPolicyResult', 'get_origin_request_policy', 'get_origin_request_policy_output']
@pulumi.output_type
class GetOriginRequestPolicyResult:
    
    def __init__(__self__, arn=..., comment=..., cookies_configs=..., etag=..., headers_configs=..., id=..., name=..., query_strings_configs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookiesConfigs")
    def cookies_configs(self) -> Sequence[outputs.GetOriginRequestPolicyCookiesConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headersConfigs")
    def headers_configs(self) -> Sequence[outputs.GetOriginRequestPolicyHeadersConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringsConfigs")
    def query_strings_configs(self) -> Sequence[outputs.GetOriginRequestPolicyQueryStringsConfigResult]:
        
        ...
    


class AwaitableGetOriginRequestPolicyResult(GetOriginRequestPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetOriginRequestPolicyResult]:
        ...
    


def get_origin_request_policy(id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOriginRequestPolicyResult:
    
    ...

def get_origin_request_policy_output(id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOriginRequestPolicyResult]:
    
    ...

