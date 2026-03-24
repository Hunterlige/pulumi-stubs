

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBucketResult', 'AwaitableGetBucketResult', 'get_bucket', 'get_bucket_output']
@pulumi.output_type
class GetBucketResult:
    
    def __init__(__self__, arn=..., bucket=..., bucket_domain_name=..., bucket_region=..., bucket_regional_domain_name=..., hosted_zone_id=..., id=..., region=..., website_domain=..., website_endpoint=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketDomainName")
    def bucket_domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketRegionalDomainName")
    def bucket_regional_domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="websiteDomain")
    def website_domain(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteEndpoint")
    def website_endpoint(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBucketResult(GetBucketResult):
    def __await__(self): # -> Generator[Never, Any, GetBucketResult]:
        ...
    


def get_bucket(bucket: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBucketResult:
    
    ...

def get_bucket_output(bucket: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBucketResult]:
    
    ...

