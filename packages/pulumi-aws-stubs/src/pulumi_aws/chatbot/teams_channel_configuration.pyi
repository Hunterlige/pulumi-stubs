

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
__all__ = ['TeamsChannelConfigurationArgs', 'TeamsChannelConfiguration']
@pulumi.input_type
class TeamsChannelConfigurationArgs:
    def __init__(__self__, *, channel_id: pulumi.Input[_builtins.str], configuration_name: pulumi.Input[_builtins.str], iam_role_arn: pulumi.Input[_builtins.str], team_id: pulumi.Input[_builtins.str], tenant_id: pulumi.Input[_builtins.str], channel_name: Optional[pulumi.Input[_builtins.str]] = ..., guardrail_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., logging_level: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., team_name: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[TeamsChannelConfigurationTimeoutsArgs]] = ..., user_authorization_required: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @channel_id.setter
    def channel_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @configuration_name.setter
    def configuration_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @team_id.setter
    def team_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guardrailPolicyArns")
    def guardrail_policy_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @guardrail_policy_arns.setter
    def guardrail_policy_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logging_level.setter
    def logging_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArns")
    def sns_topic_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @sns_topic_arns.setter
    def sns_topic_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="teamName")
    def team_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @team_name.setter
    def team_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[TeamsChannelConfigurationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[TeamsChannelConfigurationTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAuthorizationRequired")
    def user_authorization_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @user_authorization_required.setter
    def user_authorization_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _TeamsChannelConfigurationState:
    def __init__(__self__, *, channel_id: Optional[pulumi.Input[_builtins.str]] = ..., channel_name: Optional[pulumi.Input[_builtins.str]] = ..., chat_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ..., configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., guardrail_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., logging_level: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., team_id: Optional[pulumi.Input[_builtins.str]] = ..., team_name: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[TeamsChannelConfigurationTimeoutsArgs]] = ..., user_authorization_required: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel_id.setter
    def channel_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatConfigurationArn")
    def chat_configuration_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @chat_configuration_arn.setter
    def chat_configuration_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_name.setter
    def configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guardrailPolicyArns")
    def guardrail_policy_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @guardrail_policy_arns.setter
    def guardrail_policy_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logging_level.setter
    def logging_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArns")
    def sns_topic_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @sns_topic_arns.setter
    def sns_topic_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="teamName")
    def team_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @team_name.setter
    def team_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[TeamsChannelConfigurationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[TeamsChannelConfigurationTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAuthorizationRequired")
    def user_authorization_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @user_authorization_required.setter
    def user_authorization_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class TeamsChannelConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., channel_id: Optional[pulumi.Input[_builtins.str]] = ..., channel_name: Optional[pulumi.Input[_builtins.str]] = ..., configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., guardrail_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., logging_level: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., team_id: Optional[pulumi.Input[_builtins.str]] = ..., team_name: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[TeamsChannelConfigurationTimeoutsArgs, TeamsChannelConfigurationTimeoutsArgsDict]]] = ..., user_authorization_required: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TeamsChannelConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., channel_id: Optional[pulumi.Input[_builtins.str]] = ..., channel_name: Optional[pulumi.Input[_builtins.str]] = ..., chat_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ..., configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., guardrail_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., logging_level: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., team_id: Optional[pulumi.Input[_builtins.str]] = ..., team_name: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[TeamsChannelConfigurationTimeoutsArgs, TeamsChannelConfigurationTimeoutsArgsDict]]] = ..., user_authorization_required: Optional[pulumi.Input[_builtins.bool]] = ...) -> TeamsChannelConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatConfigurationArn")
    def chat_configuration_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guardrailPolicyArns")
    def guardrail_policy_arns(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArns")
    def sns_topic_arns(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="teamName")
    def team_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.TeamsChannelConfigurationTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAuthorizationRequired")
    def user_authorization_required(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    


