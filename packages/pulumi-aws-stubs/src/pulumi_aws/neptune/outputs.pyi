

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterParameterGroupParameter', 'ClusterServerlessV2ScalingConfiguration', 'GlobalClusterGlobalClusterMember', 'ParameterGroupParameter']
@pulumi.output_type
class ClusterParameterGroupParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str, apply_method: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterServerlessV2ScalingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_capacity: Optional[_builtins.float] = ..., min_capacity: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class GlobalClusterGlobalClusterMember(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, db_cluster_arn: Optional[_builtins.str] = ..., is_writer: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterArn")
    def db_cluster_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWriter")
    def is_writer(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ParameterGroupParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str, apply_method: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[_builtins.str]:
        
        ...
    


