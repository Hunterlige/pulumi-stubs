

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
__all__ = ['ConnectionFunctionArgs', 'ConnectionFunction']
@pulumi.input_type
class ConnectionFunctionArgs:
    def __init__(__self__, *, connection_function_code: pulumi.Input[_builtins.str], connection_function_config: pulumi.Input[ConnectionFunctionConnectionFunctionConfigArgs], name: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionCode")
    def connection_function_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_function_code.setter
    def connection_function_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionConfig")
    def connection_function_config(self) -> pulumi.Input[ConnectionFunctionConnectionFunctionConfigArgs]:
        
        ...
    
    @connection_function_config.setter
    def connection_function_config(self, value: pulumi.Input[ConnectionFunctionConnectionFunctionConfigArgs]): # -> None:
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
    def publish(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publish.setter
    def publish(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ConnectionFunctionState:
    def __init__(__self__, *, connection_function_arn: Optional[pulumi.Input[_builtins.str]] = ..., connection_function_code: Optional[pulumi.Input[_builtins.str]] = ..., connection_function_config: Optional[pulumi.Input[ConnectionFunctionConnectionFunctionConfigArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., live_stage_etag: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionArn")
    def connection_function_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_function_arn.setter
    def connection_function_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionCode")
    def connection_function_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_function_code.setter
    def connection_function_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionConfig")
    def connection_function_config(self) -> Optional[pulumi.Input[ConnectionFunctionConnectionFunctionConfigArgs]]:
        
        ...
    
    @connection_function_config.setter
    def connection_function_config(self, value: Optional[pulumi.Input[ConnectionFunctionConnectionFunctionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveStageEtag")
    def live_stage_etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @live_stage_etag.setter
    def live_stage_etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def publish(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publish.setter
    def publish(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token(...)
class ConnectionFunction(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connection_function_code: Optional[pulumi.Input[_builtins.str]] = ..., connection_function_config: Optional[pulumi.Input[Union[ConnectionFunctionConnectionFunctionConfigArgs, ConnectionFunctionConnectionFunctionConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectionFunctionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., connection_function_arn: Optional[pulumi.Input[_builtins.str]] = ..., connection_function_code: Optional[pulumi.Input[_builtins.str]] = ..., connection_function_config: Optional[pulumi.Input[Union[ConnectionFunctionConnectionFunctionConfigArgs, ConnectionFunctionConnectionFunctionConfigArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., live_stage_etag: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> ConnectionFunction:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionArn")
    def connection_function_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionCode")
    def connection_function_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionConfig")
    def connection_function_config(self) -> pulumi.Output[outputs.ConnectionFunctionConnectionFunctionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveStageEtag")
    def live_stage_etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publish(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


