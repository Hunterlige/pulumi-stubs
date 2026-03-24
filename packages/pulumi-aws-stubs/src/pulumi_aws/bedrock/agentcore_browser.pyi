

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AgentcoreBrowserArgs', 'AgentcoreBrowser']
@pulumi.input_type
class AgentcoreBrowserArgs:
    def __init__(__self__, *, network_configuration: pulumi.Input[AgentcoreBrowserNetworkConfigurationArgs], description: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., recording: Optional[pulumi.Input[AgentcoreBrowserRecordingArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[AgentcoreBrowserTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Input[AgentcoreBrowserNetworkConfigurationArgs]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: pulumi.Input[AgentcoreBrowserNetworkConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recording(self) -> Optional[pulumi.Input[AgentcoreBrowserRecordingArgs]]:
        
        ...
    
    @recording.setter
    def recording(self, value: Optional[pulumi.Input[AgentcoreBrowserRecordingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentcoreBrowserTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentcoreBrowserTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentcoreBrowserState:
    def __init__(__self__, *, browser_arn: Optional[pulumi.Input[_builtins.str]] = ..., browser_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_configuration: Optional[pulumi.Input[AgentcoreBrowserNetworkConfigurationArgs]] = ..., recording: Optional[pulumi.Input[AgentcoreBrowserRecordingArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[AgentcoreBrowserTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="browserArn")
    def browser_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @browser_arn.setter
    def browser_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="browserId")
    def browser_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @browser_id.setter
    def browser_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input[AgentcoreBrowserNetworkConfigurationArgs]]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input[AgentcoreBrowserNetworkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recording(self) -> Optional[pulumi.Input[AgentcoreBrowserRecordingArgs]]:
        
        ...
    
    @recording.setter
    def recording(self, value: Optional[pulumi.Input[AgentcoreBrowserRecordingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentcoreBrowserTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentcoreBrowserTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:bedrock/agentcoreBrowser:AgentcoreBrowser")
class AgentcoreBrowser(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_configuration: Optional[pulumi.Input[Union[AgentcoreBrowserNetworkConfigurationArgs, AgentcoreBrowserNetworkConfigurationArgsDict]]] = ..., recording: Optional[pulumi.Input[Union[AgentcoreBrowserRecordingArgs, AgentcoreBrowserRecordingArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[AgentcoreBrowserTimeoutsArgs, AgentcoreBrowserTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentcoreBrowserArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., browser_arn: Optional[pulumi.Input[_builtins.str]] = ..., browser_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_configuration: Optional[pulumi.Input[Union[AgentcoreBrowserNetworkConfigurationArgs, AgentcoreBrowserNetworkConfigurationArgsDict]]] = ..., recording: Optional[pulumi.Input[Union[AgentcoreBrowserRecordingArgs, AgentcoreBrowserRecordingArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[AgentcoreBrowserTimeoutsArgs, AgentcoreBrowserTimeoutsArgsDict]]] = ...) -> AgentcoreBrowser:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="browserArn")
    def browser_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="browserId")
    def browser_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Output[outputs.AgentcoreBrowserNetworkConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recording(self) -> pulumi.Output[Optional[outputs.AgentcoreBrowserRecording]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.AgentcoreBrowserTimeouts]]:
        ...
    


