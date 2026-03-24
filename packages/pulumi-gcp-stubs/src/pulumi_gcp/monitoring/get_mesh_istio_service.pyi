

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMeshIstioServiceResult', 'AwaitableGetMeshIstioServiceResult', 'get_mesh_istio_service', 'get_mesh_istio_service_output']
@pulumi.output_type
class GetMeshIstioServiceResult:
    
    def __init__(__self__, display_name=..., id=..., mesh_uid=..., name=..., project=..., service_id=..., service_name=..., service_namespace=..., telemetries=..., user_labels=...) -> None:
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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def telemetries(self) -> Sequence[outputs.GetMeshIstioServiceTelemetryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetMeshIstioServiceResult(GetMeshIstioServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetMeshIstioServiceResult]:
        ...
    


def get_mesh_istio_service(mesh_uid: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., service_namespace: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMeshIstioServiceResult:
    
    ...

def get_mesh_istio_service_output(mesh_uid: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., service_namespace: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMeshIstioServiceResult]:
    
    ...

