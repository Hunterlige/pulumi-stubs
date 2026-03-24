

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRosettaNetProcessConfigurationResult', 'AwaitableGetRosettaNetProcessConfigurationResult', 'get_rosetta_net_process_configuration', 'get_rosetta_net_process_configuration_output']
@pulumi.output_type
class GetRosettaNetProcessConfigurationResult:
    
    def __init__(__self__, activity_settings=..., azure_api_version=..., changed_time=..., created_time=..., description=..., id=..., initiator_role_settings=..., location=..., metadata=..., name=..., process_code=..., process_name=..., process_version=..., responder_role_settings=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activitySettings")
    def activity_settings(self) -> outputs.RosettaNetPipActivitySettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initiatorRoleSettings")
    def initiator_role_settings(self) -> outputs.RosettaNetPipRoleSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processCode")
    def process_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processName")
    def process_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processVersion")
    def process_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responderRoleSettings")
    def responder_role_settings(self) -> outputs.RosettaNetPipRoleSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRosettaNetProcessConfigurationResult(GetRosettaNetProcessConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetRosettaNetProcessConfigurationResult]:
        ...
    


def get_rosetta_net_process_configuration(integration_account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., rosetta_net_process_configuration_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRosettaNetProcessConfigurationResult:
    
    ...

def get_rosetta_net_process_configuration_output(integration_account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rosetta_net_process_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRosettaNetProcessConfigurationResult]:
    
    ...

