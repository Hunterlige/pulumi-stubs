

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterIAMMemberArgs', 'ClusterIAMMember']
@pulumi.input_type
class ClusterIAMMemberArgs:
    def __init__(__self__, *, cluster: pulumi.Input[_builtins.str], member: pulumi.Input[_builtins.str], role: pulumi.Input[_builtins.str], condition: Optional[pulumi.Input[ClusterIAMMemberConditionArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def member(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @member.setter
    def member(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[ClusterIAMMemberConditionArgs]]:
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[ClusterIAMMemberConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterIAMMemberState:
    def __init__(__self__, *, cluster: Optional[pulumi.Input[_builtins.str]] = ..., condition: Optional[pulumi.Input[ClusterIAMMemberConditionArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., member: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[ClusterIAMMemberConditionArgs]]:
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[ClusterIAMMemberConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def member(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @member.setter
    def member(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dataproc/clusterIAMMember:ClusterIAMMember")
class ClusterIAMMember(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., condition: Optional[pulumi.Input[Union[ClusterIAMMemberConditionArgs, ClusterIAMMemberConditionArgsDict]]] = ..., member: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterIAMMemberArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., condition: Optional[pulumi.Input[Union[ClusterIAMMemberConditionArgs, ClusterIAMMemberConditionArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., member: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ...) -> ClusterIAMMember:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional[outputs.ClusterIAMMemberCondition]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def member(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


