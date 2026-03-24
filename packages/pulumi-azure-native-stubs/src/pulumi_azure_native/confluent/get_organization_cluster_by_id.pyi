

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOrganizationClusterByIdResult', 'AwaitableGetOrganizationClusterByIdResult', 'get_organization_cluster_by_id', 'get_organization_cluster_by_id_output']
@pulumi.output_type
class GetOrganizationClusterByIdResult:
    
    def __init__(__self__, azure_api_version=..., id=..., kind=..., metadata=..., name=..., spec=..., status=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.SCMetadataEntityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[outputs.SCClusterSpecEntityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[outputs.ClusterStatusEntityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetOrganizationClusterByIdResult(GetOrganizationClusterByIdResult):
    def __await__(self): # -> Generator[Never, Any, GetOrganizationClusterByIdResult]:
        ...
    


def get_organization_cluster_by_id(cluster_id: Optional[_builtins.str] = ..., environment_id: Optional[_builtins.str] = ..., organization_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOrganizationClusterByIdResult:
    
    ...

def get_organization_cluster_by_id_output(cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., environment_id: Optional[pulumi.Input[_builtins.str]] = ..., organization_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOrganizationClusterByIdResult]:
    
    ...

