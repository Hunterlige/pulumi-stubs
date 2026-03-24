

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
__all__ = ['ClassificationExportConfigurationArgs', 'ClassificationExportConfiguration']
@pulumi.input_type
class ClassificationExportConfigurationArgs:
    def __init__(__self__, *, s3_destination: pulumi.Input[ClassificationExportConfigurationS3DestinationArgs], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> pulumi.Input[ClassificationExportConfigurationS3DestinationArgs]:
        
        ...
    
    @s3_destination.setter
    def s3_destination(self, value: pulumi.Input[ClassificationExportConfigurationS3DestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ClassificationExportConfigurationState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., s3_destination: Optional[pulumi.Input[ClassificationExportConfigurationS3DestinationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> Optional[pulumi.Input[ClassificationExportConfigurationS3DestinationArgs]]:
        
        ...
    
    @s3_destination.setter
    def s3_destination(self, value: Optional[pulumi.Input[ClassificationExportConfigurationS3DestinationArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ClassificationExportConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_destination: Optional[pulumi.Input[Union[ClassificationExportConfigurationS3DestinationArgs, ClassificationExportConfigurationS3DestinationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClassificationExportConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_destination: Optional[pulumi.Input[Union[ClassificationExportConfigurationS3DestinationArgs, ClassificationExportConfigurationS3DestinationArgsDict]]] = ...) -> ClassificationExportConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> pulumi.Output[outputs.ClassificationExportConfigurationS3Destination]:
        
        ...
    


