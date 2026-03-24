

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDistributionTenantResult', 'AwaitableGetDistributionTenantResult', 'get_distribution_tenant', 'get_distribution_tenant_output']
@pulumi.output_type
class GetDistributionTenantResult:
    
    def __init__(__self__, arn=..., connection_group_id=..., customizations=..., distribution_id=..., domain=..., domains=..., enabled=..., etag=..., id=..., managed_certificate_requests=..., name=..., parameters=..., status=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionGroupId")
    def connection_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def customizations(self) -> Sequence[outputs.GetDistributionTenantCustomizationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionId")
    def distribution_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domains(self) -> Sequence[outputs.GetDistributionTenantDomainResult]:
        
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
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedCertificateRequests")
    def managed_certificate_requests(self) -> Sequence[outputs.GetDistributionTenantManagedCertificateRequestResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Sequence[outputs.GetDistributionTenantParameterResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetDistributionTenantResult(GetDistributionTenantResult):
    def __await__(self): # -> Generator[Never, Any, GetDistributionTenantResult]:
        ...
    


def get_distribution_tenant(arn: Optional[_builtins.str] = ..., domain: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDistributionTenantResult:
    
    ...

def get_distribution_tenant_output(arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., domain: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDistributionTenantResult]:
    
    ...

