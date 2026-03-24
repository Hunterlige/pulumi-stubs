

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StandbyVirtualMachinePoolArgs', 'StandbyVirtualMachinePool']
@pulumi.input_type
class StandbyVirtualMachinePoolArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], virtual_machine_state: pulumi.Input[Union[_builtins.str, VirtualMachineState]], attached_virtual_machine_scale_set_id: Optional[pulumi.Input[_builtins.str]] = ..., elasticity_profile: Optional[pulumi.Input[StandbyVirtualMachinePoolElasticityProfileArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., standby_virtual_machine_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineState")
    def virtual_machine_state(self) -> pulumi.Input[Union[_builtins.str, VirtualMachineState]]:
        
        ...
    
    @virtual_machine_state.setter
    def virtual_machine_state(self, value: pulumi.Input[Union[_builtins.str, VirtualMachineState]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedVirtualMachineScaleSetId")
    def attached_virtual_machine_scale_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attached_virtual_machine_scale_set_id.setter
    def attached_virtual_machine_scale_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticityProfile")
    def elasticity_profile(self) -> Optional[pulumi.Input[StandbyVirtualMachinePoolElasticityProfileArgs]]:
        
        ...
    
    @elasticity_profile.setter
    def elasticity_profile(self, value: Optional[pulumi.Input[StandbyVirtualMachinePoolElasticityProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="standbyVirtualMachinePoolName")
    def standby_virtual_machine_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @standby_virtual_machine_pool_name.setter
    def standby_virtual_machine_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:standbypool:StandbyVirtualMachinePool")
class StandbyVirtualMachinePool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attached_virtual_machine_scale_set_id: Optional[pulumi.Input[_builtins.str]] = ..., elasticity_profile: Optional[pulumi.Input[Union[StandbyVirtualMachinePoolElasticityProfileArgs, StandbyVirtualMachinePoolElasticityProfileArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., standby_virtual_machine_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_machine_state: Optional[pulumi.Input[Union[_builtins.str, VirtualMachineState]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StandbyVirtualMachinePoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> StandbyVirtualMachinePool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedVirtualMachineScaleSetId")
    def attached_virtual_machine_scale_set_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticityProfile")
    def elasticity_profile(self) -> pulumi.Output[Optional[outputs.StandbyVirtualMachinePoolElasticityProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
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
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineState")
    def virtual_machine_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


