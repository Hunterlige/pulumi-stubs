import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStandbyVirtualMachinePoolResult",
    "AwaitableGetStandbyVirtualMachinePoolResult",
    "get_standby_virtual_machine_pool",
    "get_standby_virtual_machine_pool_output",
]

@pulumi.output_type
class GetStandbyVirtualMachinePoolResult:
    def __init__(
        __self__,
        attached_virtual_machine_scale_set_id=...,
        azure_api_version=...,
        elasticity_profile=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        virtual_machine_state=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachedVirtualMachineScaleSetId")
    def attached_virtual_machine_scale_set_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="elasticityProfile")
    def elasticity_profile(
        self,
    ) -> Optional[outputs.StandbyVirtualMachinePoolElasticityProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineState")
    def virtual_machine_state(self) -> _builtins.str: ...

class AwaitableGetStandbyVirtualMachinePoolResult(GetStandbyVirtualMachinePoolResult):
    def __await__(self): ...

def get_standby_virtual_machine_pool(
    resource_group_name: Optional[_builtins.str] = ...,
    standby_virtual_machine_pool_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStandbyVirtualMachinePoolResult: ...
def get_standby_virtual_machine_pool_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    standby_virtual_machine_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStandbyVirtualMachinePoolResult]: ...
