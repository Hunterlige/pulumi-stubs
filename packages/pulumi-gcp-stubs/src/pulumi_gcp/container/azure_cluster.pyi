

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
__all__ = ['AzureClusterArgs', 'AzureCluster']
@pulumi.input_type
class AzureClusterArgs:
    def __init__(__self__, *, authorization: pulumi.Input[AzureClusterAuthorizationArgs], azure_region: pulumi.Input[_builtins.str], control_plane: pulumi.Input[AzureClusterControlPlaneArgs], fleet: pulumi.Input[AzureClusterFleetArgs], location: pulumi.Input[_builtins.str], networking: pulumi.Input[AzureClusterNetworkingArgs], resource_group_id: pulumi.Input[_builtins.str], annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., azure_services_authentication: Optional[pulumi.Input[AzureClusterAzureServicesAuthenticationArgs]] = ..., client: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[AzureClusterLoggingConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Input[AzureClusterAuthorizationArgs]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: pulumi.Input[AzureClusterAuthorizationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureRegion")
    def azure_region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @azure_region.setter
    def azure_region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Input[AzureClusterControlPlaneArgs]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: pulumi.Input[AzureClusterControlPlaneArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> pulumi.Input[AzureClusterFleetArgs]:
        
        ...
    
    @fleet.setter
    def fleet(self, value: pulumi.Input[AzureClusterFleetArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def networking(self) -> pulumi.Input[AzureClusterNetworkingArgs]:
        
        ...
    
    @networking.setter
    def networking(self, value: pulumi.Input[AzureClusterNetworkingArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_id.setter
    def resource_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureServicesAuthentication")
    def azure_services_authentication(self) -> Optional[pulumi.Input[AzureClusterAzureServicesAuthenticationArgs]]:
        
        ...
    
    @azure_services_authentication.setter
    def azure_services_authentication(self, value: Optional[pulumi.Input[AzureClusterAzureServicesAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client.setter
    def client(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[AzureClusterLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[AzureClusterLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AzureClusterState:
    def __init__(__self__, *, annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authorization: Optional[pulumi.Input[AzureClusterAuthorizationArgs]] = ..., azure_region: Optional[pulumi.Input[_builtins.str]] = ..., azure_services_authentication: Optional[pulumi.Input[AzureClusterAzureServicesAuthenticationArgs]] = ..., client: Optional[pulumi.Input[_builtins.str]] = ..., control_plane: Optional[pulumi.Input[AzureClusterControlPlaneArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., fleet: Optional[pulumi.Input[AzureClusterFleetArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[AzureClusterLoggingConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networking: Optional[pulumi.Input[AzureClusterNetworkingArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., resource_group_id: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_configs: Optional[pulumi.Input[Sequence[pulumi.Input[AzureClusterWorkloadIdentityConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input[AzureClusterAuthorizationArgs]]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input[AzureClusterAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureRegion")
    def azure_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @azure_region.setter
    def azure_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureServicesAuthentication")
    def azure_services_authentication(self) -> Optional[pulumi.Input[AzureClusterAzureServicesAuthenticationArgs]]:
        
        ...
    
    @azure_services_authentication.setter
    def azure_services_authentication(self, value: Optional[pulumi.Input[AzureClusterAzureServicesAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client.setter
    def client(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[pulumi.Input[AzureClusterControlPlaneArgs]]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input[AzureClusterControlPlaneArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_annotations.setter
    def effective_annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> Optional[pulumi.Input[AzureClusterFleetArgs]]:
        
        ...
    
    @fleet.setter
    def fleet(self, value: Optional[pulumi.Input[AzureClusterFleetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[AzureClusterLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[AzureClusterLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def networking(self) -> Optional[pulumi.Input[AzureClusterNetworkingArgs]]:
        
        ...
    
    @networking.setter
    def networking(self, value: Optional[pulumi.Input[AzureClusterNetworkingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityConfigs")
    def workload_identity_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzureClusterWorkloadIdentityConfigArgs]]]]:
        
        ...
    
    @workload_identity_configs.setter
    def workload_identity_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzureClusterWorkloadIdentityConfigArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:container/azureCluster:AzureCluster")
class AzureCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authorization: Optional[pulumi.Input[Union[AzureClusterAuthorizationArgs, AzureClusterAuthorizationArgsDict]]] = ..., azure_region: Optional[pulumi.Input[_builtins.str]] = ..., azure_services_authentication: Optional[pulumi.Input[Union[AzureClusterAzureServicesAuthenticationArgs, AzureClusterAzureServicesAuthenticationArgsDict]]] = ..., client: Optional[pulumi.Input[_builtins.str]] = ..., control_plane: Optional[pulumi.Input[Union[AzureClusterControlPlaneArgs, AzureClusterControlPlaneArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fleet: Optional[pulumi.Input[Union[AzureClusterFleetArgs, AzureClusterFleetArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[Union[AzureClusterLoggingConfigArgs, AzureClusterLoggingConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networking: Optional[pulumi.Input[Union[AzureClusterNetworkingArgs, AzureClusterNetworkingArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AzureClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authorization: Optional[pulumi.Input[Union[AzureClusterAuthorizationArgs, AzureClusterAuthorizationArgsDict]]] = ..., azure_region: Optional[pulumi.Input[_builtins.str]] = ..., azure_services_authentication: Optional[pulumi.Input[Union[AzureClusterAzureServicesAuthenticationArgs, AzureClusterAzureServicesAuthenticationArgsDict]]] = ..., client: Optional[pulumi.Input[_builtins.str]] = ..., control_plane: Optional[pulumi.Input[Union[AzureClusterControlPlaneArgs, AzureClusterControlPlaneArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., fleet: Optional[pulumi.Input[Union[AzureClusterFleetArgs, AzureClusterFleetArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[Union[AzureClusterLoggingConfigArgs, AzureClusterLoggingConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networking: Optional[pulumi.Input[Union[AzureClusterNetworkingArgs, AzureClusterNetworkingArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., resource_group_id: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AzureClusterWorkloadIdentityConfigArgs, AzureClusterWorkloadIdentityConfigArgsDict]]]]] = ...) -> AzureCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[outputs.AzureClusterAuthorization]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureRegion")
    def azure_region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureServicesAuthentication")
    def azure_services_authentication(self) -> pulumi.Output[Optional[outputs.AzureClusterAzureServicesAuthentication]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def client(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Output[outputs.AzureClusterControlPlane]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> pulumi.Output[outputs.AzureClusterFleet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[outputs.AzureClusterLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def networking(self) -> pulumi.Output[outputs.AzureClusterNetworking]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityConfigs")
    def workload_identity_configs(self) -> pulumi.Output[Sequence[outputs.AzureClusterWorkloadIdentityConfig]]:
        
        ...
    


