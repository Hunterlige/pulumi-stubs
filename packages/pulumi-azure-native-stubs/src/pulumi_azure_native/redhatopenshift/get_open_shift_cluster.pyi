

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOpenShiftClusterResult', 'AwaitableGetOpenShiftClusterResult', 'get_open_shift_cluster', 'get_open_shift_cluster_output']
@pulumi.output_type
class GetOpenShiftClusterResult:
    
    def __init__(__self__, apiserver_profile=..., azure_api_version=..., cluster_profile=..., console_profile=..., id=..., ingress_profiles=..., location=..., master_profile=..., name=..., network_profile=..., provisioning_state=..., service_principal_profile=..., system_data=..., tags=..., type=..., worker_profiles=..., worker_profiles_status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiserverProfile")
    def apiserver_profile(self) -> Optional[outputs.APIServerProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterProfile")
    def cluster_profile(self) -> Optional[outputs.ClusterProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consoleProfile")
    def console_profile(self) -> Optional[outputs.ConsoleProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressProfiles")
    def ingress_profiles(self) -> Optional[Sequence[outputs.IngressProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterProfile")
    def master_profile(self) -> Optional[outputs.MasterProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.NetworkProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipalProfile")
    def service_principal_profile(self) -> Optional[outputs.ServicePrincipalProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerProfiles")
    def worker_profiles(self) -> Optional[Sequence[outputs.WorkerProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerProfilesStatus")
    def worker_profiles_status(self) -> Sequence[outputs.WorkerProfileResponse]:
        
        ...
    


class AwaitableGetOpenShiftClusterResult(GetOpenShiftClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetOpenShiftClusterResult]:
        ...
    


def get_open_shift_cluster(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOpenShiftClusterResult:
    
    ...

def get_open_shift_cluster_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOpenShiftClusterResult]:
    
    ...

