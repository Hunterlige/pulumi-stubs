

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBackendBucketResult', 'AwaitableGetBackendBucketResult', 'get_backend_bucket', 'get_backend_bucket_output']
@pulumi.output_type
class GetBackendBucketResult:
    
    def __init__(__self__, bucket_name=..., cdn_policies=..., compression_mode=..., creation_timestamp=..., custom_response_headers=..., description=..., edge_security_policy=..., enable_cdn=..., id=..., load_balancing_scheme=..., name=..., params=..., project=..., self_link=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdnPolicies")
    def cdn_policies(self) -> Sequence[outputs.GetBackendBucketCdnPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionMode")
    def compression_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseHeaders")
    def custom_response_headers(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Sequence[outputs.GetBackendBucketParamResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    


class AwaitableGetBackendBucketResult(GetBackendBucketResult):
    def __await__(self): # -> Generator[Never, Any, GetBackendBucketResult]:
        ...
    


def get_backend_bucket(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBackendBucketResult:
    
    ...

def get_backend_bucket_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBackendBucketResult]:
    
    ...

