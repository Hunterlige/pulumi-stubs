

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDeploymentSettingResult', 'AwaitableGetDeploymentSettingResult', 'get_deployment_setting', 'get_deployment_setting_output']
@pulumi.output_type
class GetDeploymentSettingResult:
    
    def __init__(__self__, arc_node_resource_ids=..., azure_api_version=..., deployment_configuration=..., deployment_mode=..., id=..., name=..., operation_type=..., provisioning_state=..., reported_properties=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcNodeResourceIds")
    def arc_node_resource_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(self) -> outputs.DeploymentConfigurationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> _builtins.str:
        
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
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportedProperties")
    def reported_properties(self) -> outputs.EceReportedPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDeploymentSettingResult(GetDeploymentSettingResult):
    def __await__(self): # -> Generator[Never, Any, GetDeploymentSettingResult]:
        ...
    


def get_deployment_setting(cluster_name: Optional[_builtins.str] = ..., deployment_settings_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDeploymentSettingResult:
    
    ...

def get_deployment_setting_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_settings_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDeploymentSettingResult]:
    
    ...

