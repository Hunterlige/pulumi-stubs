

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResponsePlanArgs', 'ResponsePlan']
@pulumi.input_type
class ResponsePlanArgs:
    def __init__(__self__, *, incident_template: pulumi.Input[ResponsePlanIncidentTemplateArgs], action: Optional[pulumi.Input[ResponsePlanActionArgs]] = ..., chat_channels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engagements: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., integration: Optional[pulumi.Input[ResponsePlanIntegrationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentTemplate")
    def incident_template(self) -> pulumi.Input[ResponsePlanIncidentTemplateArgs]:
        
        ...
    
    @incident_template.setter
    def incident_template(self, value: pulumi.Input[ResponsePlanIncidentTemplateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[ResponsePlanActionArgs]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[ResponsePlanActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatChannels")
    def chat_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @chat_channels.setter
    def chat_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def engagements(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @engagements.setter
    def engagements(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def integration(self) -> Optional[pulumi.Input[ResponsePlanIntegrationArgs]]:
        
        ...
    
    @integration.setter
    def integration(self, value: Optional[pulumi.Input[ResponsePlanIntegrationArgs]]): # -> None:
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
    


@pulumi.input_type
class _ResponsePlanState:
    def __init__(__self__, *, action: Optional[pulumi.Input[ResponsePlanActionArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., chat_channels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engagements: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., incident_template: Optional[pulumi.Input[ResponsePlanIncidentTemplateArgs]] = ..., integration: Optional[pulumi.Input[ResponsePlanIntegrationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[ResponsePlanActionArgs]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[ResponsePlanActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatChannels")
    def chat_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @chat_channels.setter
    def chat_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def engagements(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @engagements.setter
    def engagements(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentTemplate")
    def incident_template(self) -> Optional[pulumi.Input[ResponsePlanIncidentTemplateArgs]]:
        
        ...
    
    @incident_template.setter
    def incident_template(self, value: Optional[pulumi.Input[ResponsePlanIncidentTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def integration(self) -> Optional[pulumi.Input[ResponsePlanIntegrationArgs]]:
        
        ...
    
    @integration.setter
    def integration(self, value: Optional[pulumi.Input[ResponsePlanIntegrationArgs]]): # -> None:
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
    


@pulumi.type_token("aws:ssmincidents/responsePlan:ResponsePlan")
class ResponsePlan(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[Union[ResponsePlanActionArgs, ResponsePlanActionArgsDict]]] = ..., chat_channels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engagements: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., incident_template: Optional[pulumi.Input[Union[ResponsePlanIncidentTemplateArgs, ResponsePlanIncidentTemplateArgsDict]]] = ..., integration: Optional[pulumi.Input[Union[ResponsePlanIntegrationArgs, ResponsePlanIntegrationArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResponsePlanArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[Union[ResponsePlanActionArgs, ResponsePlanActionArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., chat_channels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engagements: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., incident_template: Optional[pulumi.Input[Union[ResponsePlanIncidentTemplateArgs, ResponsePlanIncidentTemplateArgsDict]]] = ..., integration: Optional[pulumi.Input[Union[ResponsePlanIntegrationArgs, ResponsePlanIntegrationArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> ResponsePlan:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[Optional[outputs.ResponsePlanAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatChannels")
    def chat_channels(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engagements(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentTemplate")
    def incident_template(self) -> pulumi.Output[outputs.ResponsePlanIncidentTemplate]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def integration(self) -> pulumi.Output[Optional[outputs.ResponsePlanIntegration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
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
    


