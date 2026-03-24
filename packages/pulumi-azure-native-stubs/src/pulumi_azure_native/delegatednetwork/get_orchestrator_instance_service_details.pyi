

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOrchestratorInstanceServiceDetailsResult', ..., 'get_orchestrator_instance_service_details', 'get_orchestrator_instance_service_details_output']
@pulumi.output_type
class GetOrchestratorInstanceServiceDetailsResult:
    
    def __init__(__self__, api_server_endpoint=..., azure_api_version=..., cluster_root_ca=..., controller_details=..., id=..., identity=..., kind=..., location=..., name=..., orchestrator_app_id=..., orchestrator_tenant_id=..., private_link_resource_id=..., provisioning_state=..., resource_guid=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiServerEndpoint")
    def api_server_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterRootCA")
    def cluster_root_ca(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controllerDetails")
    def controller_details(self) -> outputs.ControllerDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.OrchestratorIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orchestratorAppId")
    def orchestrator_app_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orchestratorTenantId")
    def orchestrator_tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetOrchestratorInstanceServiceDetailsResult(GetOrchestratorInstanceServiceDetailsResult):
    def __await__(self): # -> Generator[Never, Any, GetOrchestratorInstanceServiceDetailsResult]:
        ...
    


def get_orchestrator_instance_service_details(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOrchestratorInstanceServiceDetailsResult:
    
    ...

def get_orchestrator_instance_service_details_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOrchestratorInstanceServiceDetailsResult]:
    
    ...

