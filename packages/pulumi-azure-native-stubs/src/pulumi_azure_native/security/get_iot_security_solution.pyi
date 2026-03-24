

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIotSecuritySolutionResult', 'AwaitableGetIotSecuritySolutionResult', 'get_iot_security_solution', 'get_iot_security_solution_output']
@pulumi.output_type
class GetIotSecuritySolutionResult:
    
    def __init__(__self__, additional_workspaces=..., auto_discovered_resources=..., azure_api_version=..., disabled_data_sources=..., display_name=..., export=..., id=..., iot_hubs=..., location=..., name=..., recommendations_configuration=..., status=..., system_data=..., tags=..., type=..., unmasked_ip_logging_status=..., user_defined_resources=..., workspace=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalWorkspaces")
    def additional_workspaces(self) -> Optional[Sequence[outputs.AdditionalWorkspacesPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDiscoveredResources")
    def auto_discovered_resources(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disabledDataSources")
    def disabled_data_sources(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def export(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(self) -> Sequence[_builtins.str]:
        
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
    @pulumi.getter(name="recommendationsConfiguration")
    def recommendations_configuration(self) -> Optional[Sequence[outputs.RecommendationConfigurationPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="unmaskedIpLoggingStatus")
    def unmasked_ip_logging_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedResources")
    def user_defined_resources(self) -> Optional[outputs.UserDefinedResourcesPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def workspace(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetIotSecuritySolutionResult(GetIotSecuritySolutionResult):
    def __await__(self): # -> Generator[Never, Any, GetIotSecuritySolutionResult]:
        ...
    


def get_iot_security_solution(resource_group_name: Optional[_builtins.str] = ..., solution_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIotSecuritySolutionResult:
    
    ...

def get_iot_security_solution_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., solution_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIotSecuritySolutionResult]:
    
    ...

