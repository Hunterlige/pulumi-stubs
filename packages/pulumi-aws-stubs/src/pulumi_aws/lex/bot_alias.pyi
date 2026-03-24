

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BotAliasArgs', 'BotAlias']
@pulumi.input_type
class BotAliasArgs:
    def __init__(__self__, *, bot_name: pulumi.Input[_builtins.str], bot_version: pulumi.Input[_builtins.str], conversation_logs: Optional[pulumi.Input[BotAliasConversationLogsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botName")
    def bot_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bot_name.setter
    def bot_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bot_version.setter
    def bot_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationLogs")
    def conversation_logs(self) -> Optional[pulumi.Input[BotAliasConversationLogsArgs]]:
        
        ...
    
    @conversation_logs.setter
    def conversation_logs(self, value: Optional[pulumi.Input[BotAliasConversationLogsArgs]]): # -> None:
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
    


@pulumi.input_type
class _BotAliasState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., bot_name: Optional[pulumi.Input[_builtins.str]] = ..., bot_version: Optional[pulumi.Input[_builtins.str]] = ..., checksum: Optional[pulumi.Input[_builtins.str]] = ..., conversation_logs: Optional[pulumi.Input[BotAliasConversationLogsArgs]] = ..., created_date: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_date: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="botName")
    def bot_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bot_name.setter
    def bot_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bot_version.setter
    def bot_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checksum.setter
    def checksum(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationLogs")
    def conversation_logs(self) -> Optional[pulumi.Input[BotAliasConversationLogsArgs]]:
        
        ...
    
    @conversation_logs.setter
    def conversation_logs(self, value: Optional[pulumi.Input[BotAliasConversationLogsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_updated_date.setter
    def last_updated_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:lex/botAlias:BotAlias")
class BotAlias(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bot_name: Optional[pulumi.Input[_builtins.str]] = ..., bot_version: Optional[pulumi.Input[_builtins.str]] = ..., conversation_logs: Optional[pulumi.Input[Union[BotAliasConversationLogsArgs, BotAliasConversationLogsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BotAliasArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bot_name: Optional[pulumi.Input[_builtins.str]] = ..., bot_version: Optional[pulumi.Input[_builtins.str]] = ..., checksum: Optional[pulumi.Input[_builtins.str]] = ..., conversation_logs: Optional[pulumi.Input[Union[BotAliasConversationLogsArgs, BotAliasConversationLogsArgsDict]]] = ..., created_date: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_date: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> BotAlias:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botName")
    def bot_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationLogs")
    def conversation_logs(self) -> pulumi.Output[Optional[outputs.BotAliasConversationLogs]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


