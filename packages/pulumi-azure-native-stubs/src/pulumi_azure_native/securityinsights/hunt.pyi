

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
__all__ = ['HuntArgs', 'Hunt']
@pulumi.input_type
class HuntArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], attack_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AttackTactic]]]]] = ..., attack_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., hunt_id: Optional[pulumi.Input[_builtins.str]] = ..., hypothesis_status: Optional[pulumi.Input[Union[_builtins.str, HypothesisStatus]]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., owner: Optional[pulumi.Input[HuntOwnerArgs]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, Status]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="attackTactics")
    def attack_tactics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AttackTactic]]]]]:
        
        ...
    
    @attack_tactics.setter
    def attack_tactics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AttackTactic]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attackTechniques")
    def attack_techniques(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @attack_techniques.setter
    def attack_techniques(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="huntId")
    def hunt_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hunt_id.setter
    def hunt_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hypothesisStatus")
    def hypothesis_status(self) -> Optional[pulumi.Input[Union[_builtins.str, HypothesisStatus]]]:
        
        ...
    
    @hypothesis_status.setter
    def hypothesis_status(self, value: Optional[pulumi.Input[Union[_builtins.str, HypothesisStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[HuntOwnerArgs]]:
        
        ...
    
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[HuntOwnerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, Status]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, Status]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:securityinsights:Hunt")
class Hunt(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attack_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AttackTactic]]]]] = ..., attack_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., hunt_id: Optional[pulumi.Input[_builtins.str]] = ..., hypothesis_status: Optional[pulumi.Input[Union[_builtins.str, HypothesisStatus]]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., owner: Optional[pulumi.Input[Union[HuntOwnerArgs, HuntOwnerArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, Status]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HuntArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Hunt:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attackTactics")
    def attack_tactics(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attackTechniques")
    def attack_techniques(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hypothesisStatus")
    def hypothesis_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Output[Optional[outputs.HuntOwnerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


