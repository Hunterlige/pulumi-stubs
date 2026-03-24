

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VirtualMachineRunCommandByVirtualMachineArgs', 'VirtualMachineRunCommandByVirtualMachine']
@pulumi.input_type
class VirtualMachineRunCommandByVirtualMachineArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], vm_name: pulumi.Input[_builtins.str], async_execution: Optional[pulumi.Input[_builtins.bool]] = ..., error_blob_managed_identity: Optional[pulumi.Input[RunCommandManagedIdentityArgs]] = ..., error_blob_uri: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., output_blob_managed_identity: Optional[pulumi.Input[RunCommandManagedIdentityArgs]] = ..., output_blob_uri: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[RunCommandInputParameterArgs]]]] = ..., protected_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[RunCommandInputParameterArgs]]]] = ..., run_as_password: Optional[pulumi.Input[_builtins.str]] = ..., run_as_user: Optional[pulumi.Input[_builtins.str]] = ..., run_command_name: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[VirtualMachineRunCommandScriptSourceArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., treat_failure_as_deployment_failure: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmName")
    def vm_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vm_name.setter
    def vm_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncExecution")
    def async_execution(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @async_execution.setter
    def async_execution(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorBlobManagedIdentity")
    def error_blob_managed_identity(self) -> Optional[pulumi.Input[RunCommandManagedIdentityArgs]]:
        
        ...
    
    @error_blob_managed_identity.setter
    def error_blob_managed_identity(self, value: Optional[pulumi.Input[RunCommandManagedIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorBlobUri")
    def error_blob_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_blob_uri.setter
    def error_blob_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputBlobManagedIdentity")
    def output_blob_managed_identity(self) -> Optional[pulumi.Input[RunCommandManagedIdentityArgs]]:
        
        ...
    
    @output_blob_managed_identity.setter
    def output_blob_managed_identity(self, value: Optional[pulumi.Input[RunCommandManagedIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputBlobUri")
    def output_blob_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @output_blob_uri.setter
    def output_blob_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RunCommandInputParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RunCommandInputParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedParameters")
    def protected_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RunCommandInputParameterArgs]]]]:
        
        ...
    
    @protected_parameters.setter
    def protected_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RunCommandInputParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsPassword")
    def run_as_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @run_as_password.setter
    def run_as_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @run_as_user.setter
    def run_as_user(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runCommandName")
    def run_command_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @run_command_name.setter
    def run_command_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[VirtualMachineRunCommandScriptSourceArgs]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[VirtualMachineRunCommandScriptSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="treatFailureAsDeploymentFailure")
    def treat_failure_as_deployment_failure(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @treat_failure_as_deployment_failure.setter
    def treat_failure_as_deployment_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VirtualMachineRunCommandByVirtualMachine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., async_execution: Optional[pulumi.Input[_builtins.bool]] = ..., error_blob_managed_identity: Optional[pulumi.Input[Union[RunCommandManagedIdentityArgs, RunCommandManagedIdentityArgsDict]]] = ..., error_blob_uri: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., output_blob_managed_identity: Optional[pulumi.Input[Union[RunCommandManagedIdentityArgs, RunCommandManagedIdentityArgsDict]]] = ..., output_blob_uri: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RunCommandInputParameterArgs, RunCommandInputParameterArgsDict]]]]] = ..., protected_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RunCommandInputParameterArgs, RunCommandInputParameterArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., run_as_password: Optional[pulumi.Input[_builtins.str]] = ..., run_as_user: Optional[pulumi.Input[_builtins.str]] = ..., run_command_name: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[VirtualMachineRunCommandScriptSourceArgs, VirtualMachineRunCommandScriptSourceArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., treat_failure_as_deployment_failure: Optional[pulumi.Input[_builtins.bool]] = ..., vm_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VirtualMachineRunCommandByVirtualMachineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VirtualMachineRunCommandByVirtualMachine:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncExecution")
    def async_execution(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorBlobManagedIdentity")
    def error_blob_managed_identity(self) -> pulumi.Output[Optional[outputs.RunCommandManagedIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorBlobUri")
    def error_blob_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> pulumi.Output[outputs.VirtualMachineRunCommandInstanceViewResponse]:
        
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
    @pulumi.getter(name="outputBlobManagedIdentity")
    def output_blob_managed_identity(self) -> pulumi.Output[Optional[outputs.RunCommandManagedIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputBlobUri")
    def output_blob_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence[outputs.RunCommandInputParameterResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedParameters")
    def protected_parameters(self) -> pulumi.Output[Optional[Sequence[outputs.RunCommandInputParameterResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsPassword")
    def run_as_password(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[outputs.VirtualMachineRunCommandScriptSourceResponse]]:
        
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
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="treatFailureAsDeploymentFailure")
    def treat_failure_as_deployment_failure(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


