import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMachineRunCommandResult",
    "AwaitableGetMachineRunCommandResult",
    "get_machine_run_command",
    "get_machine_run_command_output",
]

@pulumi.output_type
class GetMachineRunCommandResult:
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
    def instance_view(self) -> outputs.MachineRunCommandInstanceViewResponse: ...
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
    def source(self) -> Optional[outputs.MachineRunCommandScriptSourceResponse]: ...
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
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetMachineRunCommandResult(GetMachineRunCommandResult):
    def __await__(self): ...

def get_machine_run_command(
    machine_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    run_command_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMachineRunCommandResult: ...
def get_machine_run_command_output(
    machine_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    run_command_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMachineRunCommandResult]: ...
