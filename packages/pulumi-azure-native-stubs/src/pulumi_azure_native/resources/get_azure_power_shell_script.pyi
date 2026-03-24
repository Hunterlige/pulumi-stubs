

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAzurePowerShellScriptResult', 'AwaitableGetAzurePowerShellScriptResult', 'get_azure_power_shell_script', 'get_azure_power_shell_script_output']
@pulumi.output_type
class GetAzurePowerShellScriptResult:
    
    def __init__(__self__, arguments=..., az_power_shell_version=..., azure_api_version=..., cleanup_preference=..., container_settings=..., environment_variables=..., force_update_tag=..., id=..., identity=..., kind=..., location=..., name=..., outputs=..., primary_script_uri=..., provisioning_state=..., retention_interval=..., script_content=..., status=..., storage_account_settings=..., supporting_script_uris=..., system_data=..., tags=..., timeout=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azPowerShellVersion")
    def az_power_shell_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanupPreference")
    def cleanup_preference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerSettings")
    def container_settings(self) -> Optional[outputs.ContainerConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Sequence[outputs.EnvironmentVariableResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> Mapping[str, Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryScriptUri")
    def primary_script_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptContent")
    def script_content(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.ScriptStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountSettings")
    def storage_account_settings(self) -> Optional[outputs.StorageAccountConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportingScriptUris")
    def supporting_script_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAzurePowerShellScriptResult(GetAzurePowerShellScriptResult):
    def __await__(self): # -> Generator[Never, Any, GetAzurePowerShellScriptResult]:
        ...
    


def get_azure_power_shell_script(resource_group_name: Optional[_builtins.str] = ..., script_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAzurePowerShellScriptResult:
    
    ...

def get_azure_power_shell_script_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., script_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAzurePowerShellScriptResult]:
    
    ...

