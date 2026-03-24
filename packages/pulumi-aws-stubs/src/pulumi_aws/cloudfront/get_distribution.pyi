

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDistributionResult', 'AwaitableGetDistributionResult', 'get_distribution', 'get_distribution_output']
@pulumi.output_type
class GetDistributionResult:
    
    def __init__(__self__, aliases=..., anycast_ip_list_id=..., arn=..., domain_name=..., enabled=..., etag=..., hosted_zone_id=..., id=..., in_progress_validation_batches=..., last_modified_time=..., status=..., tags=..., web_acl_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anycastIpListId")
    def anycast_ip_list_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
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
    @pulumi.getter(name="inProgressValidationBatches")
    def in_progress_validation_batches(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAclId")
    def web_acl_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDistributionResult(GetDistributionResult):
    def __await__(self): # -> Generator[Never, Any, GetDistributionResult]:
        ...
    


def get_distribution(id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDistributionResult:
    
    ...

def get_distribution_output(id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDistributionResult]:
    
    ...

