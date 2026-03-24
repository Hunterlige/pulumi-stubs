

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ChangeDataCaptureArgs', 'ChangeDataCapture']
@pulumi.input_type
class ChangeDataCaptureArgs:
    def __init__(__self__, *, factory_name: pulumi.Input[_builtins.str], policy: pulumi.Input[MapperPolicyArgs], resource_group_name: pulumi.Input[_builtins.str], source_connections_info: pulumi.Input[Sequence[pulumi.Input[MapperSourceConnectionsInfoArgs]]], target_connections_info: pulumi.Input[Sequence[pulumi.Input[MapperTargetConnectionsInfoArgs]]], allow_v_net_override: Optional[pulumi.Input[_builtins.bool]] = ..., change_data_capture_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[ChangeDataCaptureFolderArgs]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @factory_name.setter
    def factory_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[MapperPolicyArgs]:
        
        ...
    
    @policy.setter
    def policy(self, value: pulumi.Input[MapperPolicyArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionsInfo")
    def source_connections_info(self) -> pulumi.Input[Sequence[pulumi.Input[MapperSourceConnectionsInfoArgs]]]:
        
        ...
    
    @source_connections_info.setter
    def source_connections_info(self, value: pulumi.Input[Sequence[pulumi.Input[MapperSourceConnectionsInfoArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionsInfo")
    def target_connections_info(self) -> pulumi.Input[Sequence[pulumi.Input[MapperTargetConnectionsInfoArgs]]]:
        
        ...
    
    @target_connections_info.setter
    def target_connections_info(self, value: pulumi.Input[Sequence[pulumi.Input[MapperTargetConnectionsInfoArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowVNetOverride")
    def allow_v_net_override(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_v_net_override.setter
    def allow_v_net_override(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="changeDataCaptureName")
    def change_data_capture_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @change_data_capture_name.setter
    def change_data_capture_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def folder(self) -> Optional[pulumi.Input[ChangeDataCaptureFolderArgs]]:
        
        ...
    
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[ChangeDataCaptureFolderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:datafactory:ChangeDataCapture")
class ChangeDataCapture(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_v_net_override: Optional[pulumi.Input[_builtins.bool]] = ..., change_data_capture_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., factory_name: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[Union[ChangeDataCaptureFolderArgs, ChangeDataCaptureFolderArgsDict]]] = ..., policy: Optional[pulumi.Input[Union[MapperPolicyArgs, MapperPolicyArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source_connections_info: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MapperSourceConnectionsInfoArgs, MapperSourceConnectionsInfoArgsDict]]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., target_connections_info: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MapperTargetConnectionsInfoArgs, MapperTargetConnectionsInfoArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ChangeDataCaptureArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ChangeDataCapture:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowVNetOverride")
    def allow_v_net_override(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Output[Optional[outputs.ChangeDataCaptureResponseFolder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[outputs.MapperPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionsInfo")
    def source_connections_info(self) -> pulumi.Output[Sequence[outputs.MapperSourceConnectionsInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionsInfo")
    def target_connections_info(self) -> pulumi.Output[Sequence[outputs.MapperTargetConnectionsInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


