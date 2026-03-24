

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UploadBufferArgs', 'UploadBuffer']
@pulumi.input_type
class UploadBufferArgs:
    def __init__(__self__, *, gateway_arn: pulumi.Input[_builtins.str], disk_id: Optional[pulumi.Input[_builtins.str]] = ..., disk_path: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gateway_arn.setter
    def gateway_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_path.setter
    def disk_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _UploadBufferState:
    def __init__(__self__, *, disk_id: Optional[pulumi.Input[_builtins.str]] = ..., disk_path: Optional[pulumi.Input[_builtins.str]] = ..., gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_path.setter
    def disk_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_arn.setter
    def gateway_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:storagegateway/uploadBuffer:UploadBuffer")
class UploadBuffer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., disk_id: Optional[pulumi.Input[_builtins.str]] = ..., disk_path: Optional[pulumi.Input[_builtins.str]] = ..., gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UploadBufferArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., disk_id: Optional[pulumi.Input[_builtins.str]] = ..., disk_path: Optional[pulumi.Input[_builtins.str]] = ..., gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> UploadBuffer:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


