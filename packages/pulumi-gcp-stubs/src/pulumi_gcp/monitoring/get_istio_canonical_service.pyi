

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIstioCanonicalServiceResult', 'AwaitableGetIstioCanonicalServiceResult', 'get_istio_canonical_service', 'get_istio_canonical_service_output']
@pulumi.output_type
class GetIstioCanonicalServiceResult:
    
    def __init__(__self__, canonical_service=..., canonical_service_namespace=..., display_name=..., id=..., mesh_uid=..., name=..., project=..., service_id=..., telemetries=..., user_labels=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="canonicalService")
    def canonical_service(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="canonicalServiceNamespace")
    def canonical_service_namespace(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="meshUid")
    def mesh_uid(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def telemetries(self) -> Sequence[outputs.GetIstioCanonicalServiceTelemetryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetIstioCanonicalServiceResult(GetIstioCanonicalServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetIstioCanonicalServiceResult]:
        ...
    


def get_istio_canonical_service(canonical_service: Optional[_builtins.str] = ..., canonical_service_namespace: Optional[_builtins.str] = ..., mesh_uid: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIstioCanonicalServiceResult:
    
    ...

def get_istio_canonical_service_output(canonical_service: Optional[pulumi.Input[_builtins.str]] = ..., canonical_service_namespace: Optional[pulumi.Input[_builtins.str]] = ..., mesh_uid: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIstioCanonicalServiceResult]:
    
    ...

