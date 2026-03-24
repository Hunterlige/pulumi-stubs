

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
__all__ = ['V2modelsBotArgs', 'V2modelsBot']
@pulumi.input_type
class V2modelsBotArgs:
    def __init__(__self__, *, data_privacies: pulumi.Input[Sequence[pulumi.Input[V2modelsBotDataPrivacyArgs]]], idle_session_ttl_in_seconds: pulumi.Input[_builtins.int], role_arn: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsBotMemberArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., test_bot_alias_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[V2modelsBotTimeoutsArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPrivacies")
    def data_privacies(self) -> pulumi.Input[Sequence[pulumi.Input[V2modelsBotDataPrivacyArgs]]]:
        
        ...
    
    @data_privacies.setter
    def data_privacies(self, value: pulumi.Input[Sequence[pulumi.Input[V2modelsBotDataPrivacyArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @idle_session_ttl_in_seconds.setter
    def idle_session_ttl_in_seconds(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsBotMemberArgs]]]]:
        
        ...
    
    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsBotMemberArgs]]]]): # -> None:
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
    @pulumi.getter(name="testBotAliasTags")
    def test_bot_alias_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @test_bot_alias_tags.setter
    def test_bot_alias_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[V2modelsBotTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[V2modelsBotTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _V2modelsBotState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., data_privacies: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsBotDataPrivacyArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsBotMemberArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., test_bot_alias_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[V2modelsBotTimeoutsArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPrivacies")
    def data_privacies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsBotDataPrivacyArgs]]]]:
        
        ...
    
    @data_privacies.setter
    def data_privacies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsBotDataPrivacyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_session_ttl_in_seconds.setter
    def idle_session_ttl_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsBotMemberArgs]]]]:
        
        ...
    
    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsBotMemberArgs]]]]): # -> None:
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
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="testBotAliasTags")
    def test_bot_alias_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @test_bot_alias_tags.setter
    def test_bot_alias_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[V2modelsBotTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[V2modelsBotTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:lex/v2modelsBot:V2modelsBot")
class V2modelsBot(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_privacies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2modelsBotDataPrivacyArgs, V2modelsBotDataPrivacyArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2modelsBotMemberArgs, V2modelsBotMemberArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., test_bot_alias_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[V2modelsBotTimeoutsArgs, V2modelsBotTimeoutsArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: V2modelsBotArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., data_privacies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2modelsBotDataPrivacyArgs, V2modelsBotDataPrivacyArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2modelsBotMemberArgs, V2modelsBotMemberArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., test_bot_alias_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[V2modelsBotTimeoutsArgs, V2modelsBotTimeoutsArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> V2modelsBot:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPrivacies")
    def data_privacies(self) -> pulumi.Output[Sequence[outputs.V2modelsBotDataPrivacy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Output[Optional[Sequence[outputs.V2modelsBotMember]]]:
        
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
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="testBotAliasTags")
    def test_bot_alias_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.V2modelsBotTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


