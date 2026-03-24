

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MlflowTrackingServerArgs', 'MlflowTrackingServer']
@pulumi.input_type
class MlflowTrackingServerArgs:
    def __init__(__self__, *, artifact_store_uri: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], tracking_server_name: pulumi.Input[_builtins.str], automatic_model_registration: Optional[pulumi.Input[_builtins.bool]] = ..., mlflow_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracking_server_size: Optional[pulumi.Input[_builtins.str]] = ..., weekly_maintenance_window_start: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactStoreUri")
    def artifact_store_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @artifact_store_uri.setter
    def artifact_store_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingServerName")
    def tracking_server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tracking_server_name.setter
    def tracking_server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticModelRegistration")
    def automatic_model_registration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @automatic_model_registration.setter
    def automatic_model_registration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mlflowVersion")
    def mlflow_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mlflow_version.setter
    def mlflow_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingServerSize")
    def tracking_server_size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tracking_server_size.setter
    def tracking_server_size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @weekly_maintenance_window_start.setter
    def weekly_maintenance_window_start(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _MlflowTrackingServerState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., artifact_store_uri: Optional[pulumi.Input[_builtins.str]] = ..., automatic_model_registration: Optional[pulumi.Input[_builtins.bool]] = ..., mlflow_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracking_server_name: Optional[pulumi.Input[_builtins.str]] = ..., tracking_server_size: Optional[pulumi.Input[_builtins.str]] = ..., tracking_server_url: Optional[pulumi.Input[_builtins.str]] = ..., weekly_maintenance_window_start: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactStoreUri")
    def artifact_store_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @artifact_store_uri.setter
    def artifact_store_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticModelRegistration")
    def automatic_model_registration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @automatic_model_registration.setter
    def automatic_model_registration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mlflowVersion")
    def mlflow_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mlflow_version.setter
    def mlflow_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingServerName")
    def tracking_server_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tracking_server_name.setter
    def tracking_server_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingServerSize")
    def tracking_server_size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tracking_server_size.setter
    def tracking_server_size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingServerUrl")
    def tracking_server_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tracking_server_url.setter
    def tracking_server_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @weekly_maintenance_window_start.setter
    def weekly_maintenance_window_start(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class MlflowTrackingServer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., artifact_store_uri: Optional[pulumi.Input[_builtins.str]] = ..., automatic_model_registration: Optional[pulumi.Input[_builtins.bool]] = ..., mlflow_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracking_server_name: Optional[pulumi.Input[_builtins.str]] = ..., tracking_server_size: Optional[pulumi.Input[_builtins.str]] = ..., weekly_maintenance_window_start: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MlflowTrackingServerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., artifact_store_uri: Optional[pulumi.Input[_builtins.str]] = ..., automatic_model_registration: Optional[pulumi.Input[_builtins.bool]] = ..., mlflow_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracking_server_name: Optional[pulumi.Input[_builtins.str]] = ..., tracking_server_size: Optional[pulumi.Input[_builtins.str]] = ..., tracking_server_url: Optional[pulumi.Input[_builtins.str]] = ..., weekly_maintenance_window_start: Optional[pulumi.Input[_builtins.str]] = ...) -> MlflowTrackingServer:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactStoreUri")
    def artifact_store_uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticModelRegistration")
    def automatic_model_registration(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mlflowVersion")
    def mlflow_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingServerName")
    def tracking_server_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingServerSize")
    def tracking_server_size(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingServerUrl")
    def tracking_server_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


