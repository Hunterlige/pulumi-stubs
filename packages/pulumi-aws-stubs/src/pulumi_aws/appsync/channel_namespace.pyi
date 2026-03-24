

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
__all__ = ['ChannelNamespaceArgs', 'ChannelNamespace']
@pulumi.input_type
class ChannelNamespaceArgs:
    def __init__(__self__, *, api_id: pulumi.Input[_builtins.str], code_handlers: Optional[pulumi.Input[_builtins.str]] = ..., handler_configs: Optional[pulumi.Input[ChannelNamespaceHandlerConfigsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., publish_auth_modes: Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespacePublishAuthModeArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subscribe_auth_modes: Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespaceSubscribeAuthModeArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeHandlers")
    def code_handlers(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code_handlers.setter
    def code_handlers(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="handlerConfigs")
    def handler_configs(self) -> Optional[pulumi.Input[ChannelNamespaceHandlerConfigsArgs]]:
        
        ...
    
    @handler_configs.setter
    def handler_configs(self, value: Optional[pulumi.Input[ChannelNamespaceHandlerConfigsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishAuthModes")
    def publish_auth_modes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespacePublishAuthModeArgs]]]]:
        
        ...
    
    @publish_auth_modes.setter
    def publish_auth_modes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespacePublishAuthModeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscribeAuthModes")
    def subscribe_auth_modes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespaceSubscribeAuthModeArgs]]]]:
        
        ...
    
    @subscribe_auth_modes.setter
    def subscribe_auth_modes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespaceSubscribeAuthModeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ChannelNamespaceState:
    def __init__(__self__, *, api_id: Optional[pulumi.Input[_builtins.str]] = ..., channel_namespace_arn: Optional[pulumi.Input[_builtins.str]] = ..., code_handlers: Optional[pulumi.Input[_builtins.str]] = ..., handler_configs: Optional[pulumi.Input[ChannelNamespaceHandlerConfigsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., publish_auth_modes: Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespacePublishAuthModeArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subscribe_auth_modes: Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespaceSubscribeAuthModeArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelNamespaceArn")
    def channel_namespace_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel_namespace_arn.setter
    def channel_namespace_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeHandlers")
    def code_handlers(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code_handlers.setter
    def code_handlers(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="handlerConfigs")
    def handler_configs(self) -> Optional[pulumi.Input[ChannelNamespaceHandlerConfigsArgs]]:
        
        ...
    
    @handler_configs.setter
    def handler_configs(self, value: Optional[pulumi.Input[ChannelNamespaceHandlerConfigsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishAuthModes")
    def publish_auth_modes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespacePublishAuthModeArgs]]]]:
        
        ...
    
    @publish_auth_modes.setter
    def publish_auth_modes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespacePublishAuthModeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscribeAuthModes")
    def subscribe_auth_modes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespaceSubscribeAuthModeArgs]]]]:
        
        ...
    
    @subscribe_auth_modes.setter
    def subscribe_auth_modes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ChannelNamespaceSubscribeAuthModeArgs]]]]): # -> None:
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
    


@pulumi.type_token("aws:appsync/channelNamespace:ChannelNamespace")
class ChannelNamespace(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., code_handlers: Optional[pulumi.Input[_builtins.str]] = ..., handler_configs: Optional[pulumi.Input[Union[ChannelNamespaceHandlerConfigsArgs, ChannelNamespaceHandlerConfigsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., publish_auth_modes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ChannelNamespacePublishAuthModeArgs, ChannelNamespacePublishAuthModeArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subscribe_auth_modes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ChannelNamespaceSubscribeAuthModeArgs, ChannelNamespaceSubscribeAuthModeArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ChannelNamespaceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., channel_namespace_arn: Optional[pulumi.Input[_builtins.str]] = ..., code_handlers: Optional[pulumi.Input[_builtins.str]] = ..., handler_configs: Optional[pulumi.Input[Union[ChannelNamespaceHandlerConfigsArgs, ChannelNamespaceHandlerConfigsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., publish_auth_modes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ChannelNamespacePublishAuthModeArgs, ChannelNamespacePublishAuthModeArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subscribe_auth_modes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ChannelNamespaceSubscribeAuthModeArgs, ChannelNamespaceSubscribeAuthModeArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> ChannelNamespace:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelNamespaceArn")
    def channel_namespace_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeHandlers")
    def code_handlers(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="handlerConfigs")
    def handler_configs(self) -> pulumi.Output[Optional[outputs.ChannelNamespaceHandlerConfigs]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishAuthModes")
    def publish_auth_modes(self) -> pulumi.Output[Optional[Sequence[outputs.ChannelNamespacePublishAuthMode]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscribeAuthModes")
    def subscribe_auth_modes(self) -> pulumi.Output[Optional[Sequence[outputs.ChannelNamespaceSubscribeAuthMode]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


