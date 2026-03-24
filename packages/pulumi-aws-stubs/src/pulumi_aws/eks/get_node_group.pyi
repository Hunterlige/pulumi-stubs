

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNodeGroupResult', 'AwaitableGetNodeGroupResult', 'get_node_group', 'get_node_group_output']
@pulumi.output_type
class GetNodeGroupResult:
    
    def __init__(__self__, ami_type=..., arn=..., capacity_type=..., cluster_name=..., disk_size=..., id=..., instance_types=..., labels=..., launch_templates=..., node_group_name=..., node_role_arn=..., region=..., release_version=..., remote_accesses=..., resources=..., scaling_configs=..., status=..., subnet_ids=..., tags=..., taints=..., update_configs=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amiType")
    def ami_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityType")
    def capacity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplates")
    def launch_templates(self) -> Sequence[outputs.GetNodeGroupLaunchTemplateResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeGroupName")
    def node_group_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeRoleArn")
    def node_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteAccesses")
    def remote_accesses(self) -> Sequence[outputs.GetNodeGroupRemoteAccessResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[outputs.GetNodeGroupResourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingConfigs")
    def scaling_configs(self) -> Sequence[outputs.GetNodeGroupScalingConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Sequence[outputs.GetNodeGroupTaintResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateConfigs")
    def update_configs(self) -> Sequence[outputs.GetNodeGroupUpdateConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNodeGroupResult(GetNodeGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetNodeGroupResult]:
        ...
    


def get_node_group(cluster_name: Optional[_builtins.str] = ..., node_group_name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNodeGroupResult:
    
    ...

def get_node_group_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., node_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNodeGroupResult]:
    
    ...

