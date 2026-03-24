

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
__all__ = ['FirmwareArgs', 'Firmware']
@pulumi.input_type
class FirmwareArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., file_name: Optional[pulumi.Input[_builtins.str]] = ..., file_size: Optional[pulumi.Input[_builtins.float]] = ..., firmware_id: Optional[pulumi.Input[_builtins.str]] = ..., model: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, Status]]] = ..., status_messages: Optional[pulumi.Input[Sequence[pulumi.Input[StatusMessageArgs]]]] = ..., vendor: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_name.setter
    def file_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @file_size.setter
    def file_size(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firmwareId")
    def firmware_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firmware_id.setter
    def firmware_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, Status]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, Status]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessages")
    def status_messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StatusMessageArgs]]]]:
        
        ...
    
    @status_messages.setter
    def status_messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StatusMessageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vendor(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vendor.setter
    def vendor(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:iotfirmwaredefense:Firmware")
class Firmware(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., file_name: Optional[pulumi.Input[_builtins.str]] = ..., file_size: Optional[pulumi.Input[_builtins.float]] = ..., firmware_id: Optional[pulumi.Input[_builtins.str]] = ..., model: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, Status]]] = ..., status_messages: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StatusMessageArgs, StatusMessageArgsDict]]]]] = ..., vendor: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FirmwareArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Firmware:
        
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
    @pulumi.getter(name="fileName")
    def file_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessages")
    def status_messages(self) -> pulumi.Output[Optional[Sequence[outputs.StatusMessageResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vendor(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


