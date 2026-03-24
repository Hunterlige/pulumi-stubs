

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LinkerDryrunArgs', 'LinkerDryrun']
@pulumi.input_type
class LinkerDryrunArgs:
    def __init__(__self__, *, resource_uri: pulumi.Input[_builtins.str], dryrun_name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[CreateOrUpdateDryrunParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dryrunName")
    def dryrun_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dryrun_name.setter
    def dryrun_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[CreateOrUpdateDryrunParametersArgs]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[CreateOrUpdateDryrunParametersArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:servicelinker:LinkerDryrun")
class LinkerDryrun(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., dryrun_name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Union[CreateOrUpdateDryrunParametersArgs, CreateOrUpdateDryrunParametersArgsDict]]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LinkerDryrunArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> LinkerDryrun:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationPreviews")
    def operation_previews(self) -> pulumi.Output[Sequence[outputs.DryrunOperationPreviewResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[outputs.CreateOrUpdateDryrunParametersResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prerequisiteResults")
    def prerequisite_results(self) -> pulumi.Output[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


