

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetContainerGroupResult', 'AwaitableGetContainerGroupResult', 'get_container_group', 'get_container_group_output']
@pulumi.output_type
class GetContainerGroupResult:
    
    def __init__(__self__, azure_api_version=..., confidential_compute_properties=..., container_group_profile=..., containers=..., diagnostics=..., dns_config=..., encryption_properties=..., extensions=..., id=..., identity=..., image_registry_credentials=..., init_containers=..., instance_view=..., ip_address=..., is_created_from_standby_pool=..., location=..., name=..., os_type=..., priority=..., provisioning_state=..., restart_policy=..., sku=..., standby_pool_profile=..., subnet_ids=..., tags=..., type=..., volumes=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialComputeProperties")
    def confidential_compute_properties(self) -> Optional[outputs.ConfidentialComputePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerGroupProfile")
    def container_group_profile(self) -> Optional[outputs.ContainerGroupProfileReferenceDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Sequence[outputs.ContainerResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Optional[outputs.ContainerGroupDiagnosticsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> Optional[outputs.DnsConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionProperties")
    def encryption_properties(self) -> Optional[outputs.EncryptionPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[Sequence[outputs.DeploymentExtensionSpecResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ContainerGroupIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageRegistryCredentials")
    def image_registry_credentials(self) -> Optional[Sequence[outputs.ImageRegistryCredentialResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initContainers")
    def init_containers(self) -> Optional[Sequence[outputs.InitContainerDefinitionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.ContainerGroupPropertiesResponseInstanceView:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[outputs.IpAddressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCreatedFromStandbyPool")
    def is_created_from_standby_pool(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restartPolicy")
    def restart_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standbyPoolProfile")
    def standby_pool_profile(self) -> Optional[outputs.StandbyPoolProfileDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[outputs.ContainerGroupSubnetIdResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.VolumeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetContainerGroupResult(GetContainerGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetContainerGroupResult]:
        ...
    


def get_container_group(container_group_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetContainerGroupResult:
    
    ...

def get_container_group_output(container_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetContainerGroupResult]:
    
    ...

