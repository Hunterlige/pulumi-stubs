

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
__all__ = ['StackArgs', 'Stack']
@pulumi.input_type
class StackArgs:
    def __init__(__self__, *, access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[StackAccessEndpointArgs]]]] = ..., application_settings: Optional[pulumi.Input[StackApplicationSettingsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., embed_host_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., feedback_url: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., redirect_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_connectors: Optional[pulumi.Input[Sequence[pulumi.Input[StackStorageConnectorArgs]]]] = ..., streaming_experience_settings: Optional[pulumi.Input[StackStreamingExperienceSettingsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_settings: Optional[pulumi.Input[Sequence[pulumi.Input[StackUserSettingArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StackAccessEndpointArgs]]]]:
        
        ...
    
    @access_endpoints.setter
    def access_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StackAccessEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSettings")
    def application_settings(self) -> Optional[pulumi.Input[StackApplicationSettingsArgs]]:
        
        ...
    
    @application_settings.setter
    def application_settings(self, value: Optional[pulumi.Input[StackApplicationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="embedHostDomains")
    def embed_host_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @embed_host_domains.setter
    def embed_host_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackUrl")
    def feedback_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @feedback_url.setter
    def feedback_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConnectors")
    def storage_connectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StackStorageConnectorArgs]]]]:
        
        ...
    
    @storage_connectors.setter
    def storage_connectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StackStorageConnectorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamingExperienceSettings")
    def streaming_experience_settings(self) -> Optional[pulumi.Input[StackStreamingExperienceSettingsArgs]]:
        
        ...
    
    @streaming_experience_settings.setter
    def streaming_experience_settings(self, value: Optional[pulumi.Input[StackStreamingExperienceSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSettings")
    def user_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StackUserSettingArgs]]]]:
        
        ...
    
    @user_settings.setter
    def user_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StackUserSettingArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _StackState:
    def __init__(__self__, *, access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[StackAccessEndpointArgs]]]] = ..., application_settings: Optional[pulumi.Input[StackApplicationSettingsArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., embed_host_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., feedback_url: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., redirect_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_connectors: Optional[pulumi.Input[Sequence[pulumi.Input[StackStorageConnectorArgs]]]] = ..., streaming_experience_settings: Optional[pulumi.Input[StackStreamingExperienceSettingsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_settings: Optional[pulumi.Input[Sequence[pulumi.Input[StackUserSettingArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StackAccessEndpointArgs]]]]:
        
        ...
    
    @access_endpoints.setter
    def access_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StackAccessEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSettings")
    def application_settings(self) -> Optional[pulumi.Input[StackApplicationSettingsArgs]]:
        
        ...
    
    @application_settings.setter
    def application_settings(self, value: Optional[pulumi.Input[StackApplicationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="embedHostDomains")
    def embed_host_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @embed_host_domains.setter
    def embed_host_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackUrl")
    def feedback_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @feedback_url.setter
    def feedback_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConnectors")
    def storage_connectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StackStorageConnectorArgs]]]]:
        
        ...
    
    @storage_connectors.setter
    def storage_connectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StackStorageConnectorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamingExperienceSettings")
    def streaming_experience_settings(self) -> Optional[pulumi.Input[StackStreamingExperienceSettingsArgs]]:
        
        ...
    
    @streaming_experience_settings.setter
    def streaming_experience_settings(self, value: Optional[pulumi.Input[StackStreamingExperienceSettingsArgs]]): # -> None:
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
    @pulumi.getter(name="userSettings")
    def user_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StackUserSettingArgs]]]]:
        
        ...
    
    @user_settings.setter
    def user_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StackUserSettingArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:appstream/stack:Stack")
class Stack(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StackAccessEndpointArgs, StackAccessEndpointArgsDict]]]]] = ..., application_settings: Optional[pulumi.Input[Union[StackApplicationSettingsArgs, StackApplicationSettingsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., embed_host_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., feedback_url: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., redirect_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_connectors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StackStorageConnectorArgs, StackStorageConnectorArgsDict]]]]] = ..., streaming_experience_settings: Optional[pulumi.Input[Union[StackStreamingExperienceSettingsArgs, StackStreamingExperienceSettingsArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StackUserSettingArgs, StackUserSettingArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[StackArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StackAccessEndpointArgs, StackAccessEndpointArgsDict]]]]] = ..., application_settings: Optional[pulumi.Input[Union[StackApplicationSettingsArgs, StackApplicationSettingsArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., embed_host_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., feedback_url: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., redirect_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_connectors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StackStorageConnectorArgs, StackStorageConnectorArgsDict]]]]] = ..., streaming_experience_settings: Optional[pulumi.Input[Union[StackStreamingExperienceSettingsArgs, StackStreamingExperienceSettingsArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StackUserSettingArgs, StackUserSettingArgsDict]]]]] = ...) -> Stack:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> pulumi.Output[Sequence[outputs.StackAccessEndpoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSettings")
    def application_settings(self) -> pulumi.Output[outputs.StackApplicationSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="embedHostDomains")
    def embed_host_domains(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackUrl")
    def feedback_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConnectors")
    def storage_connectors(self) -> pulumi.Output[Sequence[outputs.StackStorageConnector]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamingExperienceSettings")
    def streaming_experience_settings(self) -> pulumi.Output[outputs.StackStreamingExperienceSettings]:
        
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
    @pulumi.getter(name="userSettings")
    def user_settings(self) -> pulumi.Output[Sequence[outputs.StackUserSetting]]:
        
        ...
    


