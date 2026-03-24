

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServiceResult', 'AwaitableGetServiceResult', 'get_service', 'get_service_output']
@pulumi.output_type
class GetServiceResult:
    
    def __init__(__self__, arn=..., description=..., dns_configs=..., health_check_configs=..., health_check_custom_configs=..., id=..., name=..., namespace_id=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsConfigs")
    def dns_configs(self) -> Sequence[outputs.GetServiceDnsConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckConfigs")
    def health_check_configs(self) -> Sequence[outputs.GetServiceHealthCheckConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckCustomConfigs")
    def health_check_custom_configs(self) -> Sequence[outputs.GetServiceHealthCheckCustomConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


class AwaitableGetServiceResult(GetServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetServiceResult]:
        ...
    


def get_service(name: Optional[_builtins.str] = ..., namespace_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServiceResult:
    
    ...

def get_service_output(name: Optional[pulumi.Input[_builtins.str]] = ..., namespace_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServiceResult]:
    
    ...

