

import builtins as _builtins
import sys
import pulumi
from typing import Optional
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ControllerConnectionDetailsResponse', 'KubernetesConnectionDetailsResponse', 'SkuResponse']
@pulumi.output_type
class ControllerConnectionDetailsResponse(dict):
    def __init__(__self__, *, orchestrator_specific_connection_details: Optional[outputs.KubernetesConnectionDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orchestratorSpecificConnectionDetails")
    def orchestrator_specific_connection_details(self) -> Optional[outputs.KubernetesConnectionDetailsResponse]:
        
        ...
    


@pulumi.output_type
class KubernetesConnectionDetailsResponse(dict):
    
    def __init__(__self__, *, instance_type: _builtins.str, kube_config: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeConfig")
    def kube_config(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


