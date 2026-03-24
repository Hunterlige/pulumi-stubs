

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSSLPolicyResult', 'AwaitableGetSSLPolicyResult', 'get_ssl_policy', 'get_ssl_policy_output']
@pulumi.output_type
class GetSSLPolicyResult:
    
    def __init__(__self__, creation_timestamp=..., custom_features=..., description=..., enabled_features=..., fingerprint=..., id=..., min_tls_version=..., name=..., profile=..., project=..., self_link=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customFeatures")
    def custom_features(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledFeatures")
    def enabled_features(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTlsVersion")
    def min_tls_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def profile(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSSLPolicyResult(GetSSLPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetSSLPolicyResult]:
        ...
    


def get_ssl_policy(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSSLPolicyResult:
    
    ...

def get_ssl_policy_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSSLPolicyResult]:
    
    ...

