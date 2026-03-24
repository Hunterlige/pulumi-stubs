

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ScopingConfigurationArgs', 'ScopingConfiguration']
@pulumi.input_type
class ScopingConfigurationArgs:
    def __init__(__self__, *, report_name: pulumi.Input[_builtins.str], answers: Optional[pulumi.Input[Sequence[pulumi.Input[ScopingAnswerArgs]]]] = ..., scoping_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportName")
    def report_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @report_name.setter
    def report_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def answers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScopingAnswerArgs]]]]:
        
        ...
    
    @answers.setter
    def answers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScopingAnswerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopingConfigurationName")
    def scoping_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scoping_configuration_name.setter
    def scoping_configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ScopingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., answers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ScopingAnswerArgs, ScopingAnswerArgsDict]]]]] = ..., report_name: Optional[pulumi.Input[_builtins.str]] = ..., scoping_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ScopingConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ScopingConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def answers(self) -> pulumi.Output[Optional[Sequence[outputs.ScopingAnswerResponse]]]:
        
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
    


