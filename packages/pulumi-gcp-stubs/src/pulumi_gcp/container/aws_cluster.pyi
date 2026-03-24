

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
__all__ = ['AwsClusterArgs', 'AwsCluster']
@pulumi.input_type
class AwsClusterArgs:
    def __init__(__self__, *, authorization: pulumi.Input[AwsClusterAuthorizationArgs], aws_region: pulumi.Input[_builtins.str], control_plane: pulumi.Input[AwsClusterControlPlaneArgs], fleet: pulumi.Input[AwsClusterFleetArgs], location: pulumi.Input[_builtins.str], networking: pulumi.Input[AwsClusterNetworkingArgs], annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., binary_authorization: Optional[pulumi.Input[AwsClusterBinaryAuthorizationArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[AwsClusterLoggingConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Input[AwsClusterAuthorizationArgs]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: pulumi.Input[AwsClusterAuthorizationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @aws_region.setter
    def aws_region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Input[AwsClusterControlPlaneArgs]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: pulumi.Input[AwsClusterControlPlaneArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> pulumi.Input[AwsClusterFleetArgs]:
        
        ...
    
    @fleet.setter
    def fleet(self, value: pulumi.Input[AwsClusterFleetArgs]): # -> None:
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
    def networking(self) -> pulumi.Input[AwsClusterNetworkingArgs]:
        
        ...
    
    @networking.setter
    def networking(self, value: pulumi.Input[AwsClusterNetworkingArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> Optional[pulumi.Input[AwsClusterBinaryAuthorizationArgs]]:
        
        ...
    
    @binary_authorization.setter
    def binary_authorization(self, value: Optional[pulumi.Input[AwsClusterBinaryAuthorizationArgs]]): # -> None:
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
    def logging_config(self) -> Optional[pulumi.Input[AwsClusterLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[AwsClusterLoggingConfigArgs]]): # -> None:
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
class _AwsClusterState:
    def __init__(__self__, *, annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authorization: Optional[pulumi.Input[AwsClusterAuthorizationArgs]] = ..., aws_region: Optional[pulumi.Input[_builtins.str]] = ..., binary_authorization: Optional[pulumi.Input[AwsClusterBinaryAuthorizationArgs]] = ..., control_plane: Optional[pulumi.Input[AwsClusterControlPlaneArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., fleet: Optional[pulumi.Input[AwsClusterFleetArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[AwsClusterLoggingConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networking: Optional[pulumi.Input[AwsClusterNetworkingArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_configs: Optional[pulumi.Input[Sequence[pulumi.Input[AwsClusterWorkloadIdentityConfigArgs]]]] = ...) -> None:
        
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
    def authorization(self) -> Optional[pulumi.Input[AwsClusterAuthorizationArgs]]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input[AwsClusterAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_region.setter
    def aws_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> Optional[pulumi.Input[AwsClusterBinaryAuthorizationArgs]]:
        
        ...
    
    @binary_authorization.setter
    def binary_authorization(self, value: Optional[pulumi.Input[AwsClusterBinaryAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[pulumi.Input[AwsClusterControlPlaneArgs]]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input[AwsClusterControlPlaneArgs]]): # -> None:
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
    def fleet(self) -> Optional[pulumi.Input[AwsClusterFleetArgs]]:
        
        ...
    
    @fleet.setter
    def fleet(self, value: Optional[pulumi.Input[AwsClusterFleetArgs]]): # -> None:
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
    def logging_config(self) -> Optional[pulumi.Input[AwsClusterLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[AwsClusterLoggingConfigArgs]]): # -> None:
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
    def networking(self) -> Optional[pulumi.Input[AwsClusterNetworkingArgs]]:
        
        ...
    
    @networking.setter
    def networking(self, value: Optional[pulumi.Input[AwsClusterNetworkingArgs]]): # -> None:
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
    def workload_identity_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AwsClusterWorkloadIdentityConfigArgs]]]]:
        
        ...
    
    @workload_identity_configs.setter
    def workload_identity_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AwsClusterWorkloadIdentityConfigArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:container/awsCluster:AwsCluster")
class AwsCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authorization: Optional[pulumi.Input[Union[AwsClusterAuthorizationArgs, AwsClusterAuthorizationArgsDict]]] = ..., aws_region: Optional[pulumi.Input[_builtins.str]] = ..., binary_authorization: Optional[pulumi.Input[Union[AwsClusterBinaryAuthorizationArgs, AwsClusterBinaryAuthorizationArgsDict]]] = ..., control_plane: Optional[pulumi.Input[Union[AwsClusterControlPlaneArgs, AwsClusterControlPlaneArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fleet: Optional[pulumi.Input[Union[AwsClusterFleetArgs, AwsClusterFleetArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[Union[AwsClusterLoggingConfigArgs, AwsClusterLoggingConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networking: Optional[pulumi.Input[Union[AwsClusterNetworkingArgs, AwsClusterNetworkingArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AwsClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authorization: Optional[pulumi.Input[Union[AwsClusterAuthorizationArgs, AwsClusterAuthorizationArgsDict]]] = ..., aws_region: Optional[pulumi.Input[_builtins.str]] = ..., binary_authorization: Optional[pulumi.Input[Union[AwsClusterBinaryAuthorizationArgs, AwsClusterBinaryAuthorizationArgsDict]]] = ..., control_plane: Optional[pulumi.Input[Union[AwsClusterControlPlaneArgs, AwsClusterControlPlaneArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., fleet: Optional[pulumi.Input[Union[AwsClusterFleetArgs, AwsClusterFleetArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[Union[AwsClusterLoggingConfigArgs, AwsClusterLoggingConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networking: Optional[pulumi.Input[Union[AwsClusterNetworkingArgs, AwsClusterNetworkingArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AwsClusterWorkloadIdentityConfigArgs, AwsClusterWorkloadIdentityConfigArgsDict]]]]] = ...) -> AwsCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[outputs.AwsClusterAuthorization]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> pulumi.Output[outputs.AwsClusterBinaryAuthorization]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Output[outputs.AwsClusterControlPlane]:
        
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
    def fleet(self) -> pulumi.Output[outputs.AwsClusterFleet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[outputs.AwsClusterLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def networking(self) -> pulumi.Output[outputs.AwsClusterNetworking]:
        
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
    def workload_identity_configs(self) -> pulumi.Output[Sequence[outputs.AwsClusterWorkloadIdentityConfig]]:
        
        ...
    


