

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClusterResult', 'AwaitableGetClusterResult', 'get_cluster', 'get_cluster_output']
@pulumi.output_type
class GetClusterResult:
    
    def __init__(__self__, access_configs=..., arn=..., certificate_authorities=..., cluster_id=..., compute_configs=..., control_plane_scaling_configs=..., created_at=..., deletion_protection=..., enabled_cluster_log_types=..., endpoint=..., id=..., identities=..., kubernetes_network_configs=..., name=..., outpost_configs=..., platform_version=..., region=..., remote_network_configs=..., role_arn=..., status=..., storage_configs=..., tags=..., upgrade_policies=..., version=..., vpc_config=..., zonal_shift_configs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(self) -> Sequence[outputs.GetClusterAccessConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorities")
    def certificate_authorities(self) -> Sequence[outputs.GetClusterCertificateAuthorityResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeConfigs")
    def compute_configs(self) -> Sequence[outputs.GetClusterComputeConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneScalingConfigs")
    def control_plane_scaling_configs(self) -> Sequence[outputs.GetClusterControlPlaneScalingConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledClusterLogTypes")
    def enabled_cluster_log_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Sequence[outputs.GetClusterIdentityResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesNetworkConfigs")
    def kubernetes_network_configs(self) -> Sequence[outputs.GetClusterKubernetesNetworkConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostConfigs")
    def outpost_configs(self) -> Sequence[outputs.GetClusterOutpostConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteNetworkConfigs")
    def remote_network_configs(self) -> Sequence[outputs.GetClusterRemoteNetworkConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfigs")
    def storage_configs(self) -> Sequence[outputs.GetClusterStorageConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradePolicies")
    def upgrade_policies(self) -> Sequence[outputs.GetClusterUpgradePolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> outputs.GetClusterVpcConfigResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zonalShiftConfigs")
    def zonal_shift_configs(self) -> Sequence[outputs.GetClusterZonalShiftConfigResult]:
        
        ...
    


class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetClusterResult]:
        ...
    


def get_cluster(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClusterResult:
    
    ...

def get_cluster_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClusterResult]:
    
    ...

