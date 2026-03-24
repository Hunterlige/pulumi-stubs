

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEngineVersionsResult', 'AwaitableGetEngineVersionsResult', 'get_engine_versions', 'get_engine_versions_output']
@pulumi.output_type
class GetEngineVersionsResult:
    
    def __init__(__self__, default_cluster_version=..., id=..., latest_master_version=..., latest_node_version=..., location=..., project=..., release_channel_default_version=..., release_channel_latest_version=..., release_channel_upgrade_target_version=..., valid_master_versions=..., valid_node_versions=..., version_prefix=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultClusterVersion")
    def default_cluster_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestMasterVersion")
    def latest_master_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestNodeVersion")
    def latest_node_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannelDefaultVersion")
    def release_channel_default_version(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannelLatestVersion")
    def release_channel_latest_version(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannelUpgradeTargetVersion")
    def release_channel_upgrade_target_version(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validMasterVersions")
    def valid_master_versions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validNodeVersions")
    def valid_node_versions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionPrefix")
    def version_prefix(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetEngineVersionsResult(GetEngineVersionsResult):
    def __await__(self): # -> Generator[Never, Any, GetEngineVersionsResult]:
        ...
    


def get_engine_versions(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., version_prefix: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEngineVersionsResult:
    
    ...

def get_engine_versions_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., version_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEngineVersionsResult]:
    
    ...

