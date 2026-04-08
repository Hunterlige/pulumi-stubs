import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualMachineScaleSetVMRunCommandResult",
    ...,
    "get_virtual_machine_scale_set_vm_run_command",
    ...,
]

@pulumi.output_type
class GetVirtualMachineScaleSetVMRunCommandResult:
    def __init__(
        __self__,
        async_execution=...,
        azure_api_version=...,
        error_blob_managed_identity=...,
        error_blob_uri=...,
        id=...,
        instance_view=...,
        location=...,
        name=...,
        output_blob_managed_identity=...,
        output_blob_uri=...,
        parameters=...,
        protected_parameters=...,
        provisioning_state=...,
        run_as_password=...,
        run_as_user=...,
        source=...,
        system_data=...,
        tags=...,
        timeout_in_seconds=...,
        treat_failure_as_deployment_failure=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asyncExecution")
    def async_execution(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorBlobManagedIdentity")
    def error_blob_managed_identity(
        self,
    ) -> Optional[outputs.RunCommandManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="errorBlobUri")
    def error_blob_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.VirtualMachineRunCommandInstanceViewResponse: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outputBlobManagedIdentity")
    def output_blob_managed_identity(
        self,
    ) -> Optional[outputs.RunCommandManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="outputBlobUri")
    def output_blob_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Sequence[outputs.RunCommandInputParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="protectedParameters")
    def protected_parameters(
        self,
    ) -> Optional[Sequence[outputs.RunCommandInputParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runAsPassword")
    def run_as_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> Optional[outputs.VirtualMachineRunCommandScriptSourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="treatFailureAsDeploymentFailure")
    def treat_failure_as_deployment_failure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetVirtualMachineScaleSetVMRunCommandResult(
    GetVirtualMachineScaleSetVMRunCommandResult
):
    def __await__(self): ...

def get_virtual_machine_scale_set_vm_run_command(
    expand: Optional[_builtins.str] = ...,
    instance_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    run_command_name: Optional[_builtins.str] = ...,
    vm_scale_set_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualMachineScaleSetVMRunCommandResult: ...
def get_virtual_machine_scale_set_vm_run_command_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    run_command_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vm_scale_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualMachineScaleSetVMRunCommandResult]: ...
