

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetArcSettingResult', 'AwaitableGetArcSettingResult', 'get_arc_setting', 'get_arc_setting_output']
@pulumi.output_type
class GetArcSettingResult:
    
    def __init__(__self__, aggregate_state=..., arc_application_client_id=..., arc_application_object_id=..., arc_application_tenant_id=..., arc_instance_resource_group=..., arc_service_principal_object_id=..., azure_api_version=..., connectivity_properties=..., default_extensions=..., id=..., name=..., per_node_details=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregateState")
    def aggregate_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcApplicationClientId")
    def arc_application_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcApplicationObjectId")
    def arc_application_object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcApplicationTenantId")
    def arc_application_tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcInstanceResourceGroup")
    def arc_instance_resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcServicePrincipalObjectId")
    def arc_service_principal_object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityProperties")
    def connectivity_properties(self) -> Optional[Sequence[outputs.ArcConnectivityPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultExtensions")
    def default_extensions(self) -> Sequence[outputs.DefaultExtensionDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perNodeDetails")
    def per_node_details(self) -> Sequence[outputs.PerNodeStateResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetArcSettingResult(GetArcSettingResult):
    def __await__(self): # -> Generator[Never, Any, GetArcSettingResult]:
        ...
    


def get_arc_setting(arc_setting_name: Optional[_builtins.str] = ..., cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetArcSettingResult:
    
    ...

def get_arc_setting_output(arc_setting_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetArcSettingResult]:
    
    ...

