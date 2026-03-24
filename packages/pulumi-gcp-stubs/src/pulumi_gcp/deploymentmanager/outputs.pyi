

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeploymentLabel', 'DeploymentTarget', 'DeploymentTargetConfig', 'DeploymentTargetImport']
@pulumi.output_type
class DeploymentLabel(dict):
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentTarget(dict):
    def __init__(__self__, *, config: outputs.DeploymentTargetConfig, imports: Optional[Sequence[outputs.DeploymentTargetImport]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> outputs.DeploymentTargetConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def imports(self) -> Optional[Sequence[outputs.DeploymentTargetImport]]:
        
        ...
    


@pulumi.output_type
class DeploymentTargetConfig(dict):
    def __init__(__self__, *, content: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DeploymentTargetImport(dict):
    def __init__(__self__, *, content: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


