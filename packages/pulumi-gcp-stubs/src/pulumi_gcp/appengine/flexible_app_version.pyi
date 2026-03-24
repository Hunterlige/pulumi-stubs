

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
__all__ = ['FlexibleAppVersionArgs', 'FlexibleAppVersion']
@pulumi.input_type
class FlexibleAppVersionArgs:
    def __init__(__self__, *, liveness_check: pulumi.Input[FlexibleAppVersionLivenessCheckArgs], readiness_check: pulumi.Input[FlexibleAppVersionReadinessCheckArgs], runtime: pulumi.Input[_builtins.str], service: pulumi.Input[_builtins.str], api_config: Optional[pulumi.Input[FlexibleAppVersionApiConfigArgs]] = ..., automatic_scaling: Optional[pulumi.Input[FlexibleAppVersionAutomaticScalingArgs]] = ..., beta_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., default_expiration: Optional[pulumi.Input[_builtins.str]] = ..., delete_service_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., deployment: Optional[pulumi.Input[FlexibleAppVersionDeploymentArgs]] = ..., endpoints_api_service: Optional[pulumi.Input[FlexibleAppVersionEndpointsApiServiceArgs]] = ..., entrypoint: Optional[pulumi.Input[FlexibleAppVersionEntrypointArgs]] = ..., env_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., flexible_runtime_settings: Optional[pulumi.Input[FlexibleAppVersionFlexibleRuntimeSettingsArgs]] = ..., handlers: Optional[pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionHandlerArgs]]]] = ..., inbound_services: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instance_class: Optional[pulumi.Input[_builtins.str]] = ..., manual_scaling: Optional[pulumi.Input[FlexibleAppVersionManualScalingArgs]] = ..., network: Optional[pulumi.Input[FlexibleAppVersionNetworkArgs]] = ..., nobuild_files_regex: Optional[pulumi.Input[_builtins.str]] = ..., noop_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[FlexibleAppVersionResourcesArgs]] = ..., runtime_api_version: Optional[pulumi.Input[_builtins.str]] = ..., runtime_channel: Optional[pulumi.Input[_builtins.str]] = ..., runtime_main_executable_path: Optional[pulumi.Input[_builtins.str]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., serving_status: Optional[pulumi.Input[_builtins.str]] = ..., version_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_access_connector: Optional[pulumi.Input[FlexibleAppVersionVpcAccessConnectorArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="livenessCheck")
    def liveness_check(self) -> pulumi.Input[FlexibleAppVersionLivenessCheckArgs]:
        
        ...
    
    @liveness_check.setter
    def liveness_check(self, value: pulumi.Input[FlexibleAppVersionLivenessCheckArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readinessCheck")
    def readiness_check(self) -> pulumi.Input[FlexibleAppVersionReadinessCheckArgs]:
        
        ...
    
    @readiness_check.setter
    def readiness_check(self, value: pulumi.Input[FlexibleAppVersionReadinessCheckArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @runtime.setter
    def runtime(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConfig")
    def api_config(self) -> Optional[pulumi.Input[FlexibleAppVersionApiConfigArgs]]:
        
        ...
    
    @api_config.setter
    def api_config(self, value: Optional[pulumi.Input[FlexibleAppVersionApiConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticScaling")
    def automatic_scaling(self) -> Optional[pulumi.Input[FlexibleAppVersionAutomaticScalingArgs]]:
        
        ...
    
    @automatic_scaling.setter
    def automatic_scaling(self, value: Optional[pulumi.Input[FlexibleAppVersionAutomaticScalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="betaSettings")
    def beta_settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @beta_settings.setter
    def beta_settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultExpiration")
    def default_expiration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_expiration.setter
    def default_expiration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteServiceOnDestroy")
    def delete_service_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_service_on_destroy.setter
    def delete_service_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> Optional[pulumi.Input[FlexibleAppVersionDeploymentArgs]]:
        
        ...
    
    @deployment.setter
    def deployment(self, value: Optional[pulumi.Input[FlexibleAppVersionDeploymentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointsApiService")
    def endpoints_api_service(self) -> Optional[pulumi.Input[FlexibleAppVersionEndpointsApiServiceArgs]]:
        
        ...
    
    @endpoints_api_service.setter
    def endpoints_api_service(self, value: Optional[pulumi.Input[FlexibleAppVersionEndpointsApiServiceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def entrypoint(self) -> Optional[pulumi.Input[FlexibleAppVersionEntrypointArgs]]:
        
        ...
    
    @entrypoint.setter
    def entrypoint(self, value: Optional[pulumi.Input[FlexibleAppVersionEntrypointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="envVariables")
    def env_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @env_variables.setter
    def env_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="flexibleRuntimeSettings")
    def flexible_runtime_settings(self) -> Optional[pulumi.Input[FlexibleAppVersionFlexibleRuntimeSettingsArgs]]:
        
        ...
    
    @flexible_runtime_settings.setter
    def flexible_runtime_settings(self, value: Optional[pulumi.Input[FlexibleAppVersionFlexibleRuntimeSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def handlers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionHandlerArgs]]]]:
        
        ...
    
    @handlers.setter
    def handlers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionHandlerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundServices")
    def inbound_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @inbound_services.setter
    def inbound_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_class.setter
    def instance_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualScaling")
    def manual_scaling(self) -> Optional[pulumi.Input[FlexibleAppVersionManualScalingArgs]]:
        
        ...
    
    @manual_scaling.setter
    def manual_scaling(self, value: Optional[pulumi.Input[FlexibleAppVersionManualScalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[FlexibleAppVersionNetworkArgs]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[FlexibleAppVersionNetworkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nobuildFilesRegex")
    def nobuild_files_regex(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nobuild_files_regex.setter
    def nobuild_files_regex(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noopOnDestroy")
    def noop_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @noop_on_destroy.setter
    def noop_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def resources(self) -> Optional[pulumi.Input[FlexibleAppVersionResourcesArgs]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[FlexibleAppVersionResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeApiVersion")
    def runtime_api_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_api_version.setter
    def runtime_api_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeChannel")
    def runtime_channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_channel.setter
    def runtime_channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeMainExecutablePath")
    def runtime_main_executable_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_main_executable_path.setter
    def runtime_main_executable_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servingStatus")
    def serving_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serving_status.setter
    def serving_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccessConnector")
    def vpc_access_connector(self) -> Optional[pulumi.Input[FlexibleAppVersionVpcAccessConnectorArgs]]:
        
        ...
    
    @vpc_access_connector.setter
    def vpc_access_connector(self, value: Optional[pulumi.Input[FlexibleAppVersionVpcAccessConnectorArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _FlexibleAppVersionState:
    def __init__(__self__, *, api_config: Optional[pulumi.Input[FlexibleAppVersionApiConfigArgs]] = ..., automatic_scaling: Optional[pulumi.Input[FlexibleAppVersionAutomaticScalingArgs]] = ..., beta_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., default_expiration: Optional[pulumi.Input[_builtins.str]] = ..., delete_service_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., deployment: Optional[pulumi.Input[FlexibleAppVersionDeploymentArgs]] = ..., endpoints_api_service: Optional[pulumi.Input[FlexibleAppVersionEndpointsApiServiceArgs]] = ..., entrypoint: Optional[pulumi.Input[FlexibleAppVersionEntrypointArgs]] = ..., env_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., flexible_runtime_settings: Optional[pulumi.Input[FlexibleAppVersionFlexibleRuntimeSettingsArgs]] = ..., handlers: Optional[pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionHandlerArgs]]]] = ..., inbound_services: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instance_class: Optional[pulumi.Input[_builtins.str]] = ..., liveness_check: Optional[pulumi.Input[FlexibleAppVersionLivenessCheckArgs]] = ..., manual_scaling: Optional[pulumi.Input[FlexibleAppVersionManualScalingArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[FlexibleAppVersionNetworkArgs]] = ..., nobuild_files_regex: Optional[pulumi.Input[_builtins.str]] = ..., noop_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., readiness_check: Optional[pulumi.Input[FlexibleAppVersionReadinessCheckArgs]] = ..., resources: Optional[pulumi.Input[FlexibleAppVersionResourcesArgs]] = ..., runtime: Optional[pulumi.Input[_builtins.str]] = ..., runtime_api_version: Optional[pulumi.Input[_builtins.str]] = ..., runtime_channel: Optional[pulumi.Input[_builtins.str]] = ..., runtime_main_executable_path: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., serving_status: Optional[pulumi.Input[_builtins.str]] = ..., version_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_access_connector: Optional[pulumi.Input[FlexibleAppVersionVpcAccessConnectorArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConfig")
    def api_config(self) -> Optional[pulumi.Input[FlexibleAppVersionApiConfigArgs]]:
        
        ...
    
    @api_config.setter
    def api_config(self, value: Optional[pulumi.Input[FlexibleAppVersionApiConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticScaling")
    def automatic_scaling(self) -> Optional[pulumi.Input[FlexibleAppVersionAutomaticScalingArgs]]:
        
        ...
    
    @automatic_scaling.setter
    def automatic_scaling(self, value: Optional[pulumi.Input[FlexibleAppVersionAutomaticScalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="betaSettings")
    def beta_settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @beta_settings.setter
    def beta_settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultExpiration")
    def default_expiration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_expiration.setter
    def default_expiration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteServiceOnDestroy")
    def delete_service_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_service_on_destroy.setter
    def delete_service_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> Optional[pulumi.Input[FlexibleAppVersionDeploymentArgs]]:
        
        ...
    
    @deployment.setter
    def deployment(self, value: Optional[pulumi.Input[FlexibleAppVersionDeploymentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointsApiService")
    def endpoints_api_service(self) -> Optional[pulumi.Input[FlexibleAppVersionEndpointsApiServiceArgs]]:
        
        ...
    
    @endpoints_api_service.setter
    def endpoints_api_service(self, value: Optional[pulumi.Input[FlexibleAppVersionEndpointsApiServiceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def entrypoint(self) -> Optional[pulumi.Input[FlexibleAppVersionEntrypointArgs]]:
        
        ...
    
    @entrypoint.setter
    def entrypoint(self, value: Optional[pulumi.Input[FlexibleAppVersionEntrypointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="envVariables")
    def env_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @env_variables.setter
    def env_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="flexibleRuntimeSettings")
    def flexible_runtime_settings(self) -> Optional[pulumi.Input[FlexibleAppVersionFlexibleRuntimeSettingsArgs]]:
        
        ...
    
    @flexible_runtime_settings.setter
    def flexible_runtime_settings(self, value: Optional[pulumi.Input[FlexibleAppVersionFlexibleRuntimeSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def handlers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionHandlerArgs]]]]:
        
        ...
    
    @handlers.setter
    def handlers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionHandlerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundServices")
    def inbound_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @inbound_services.setter
    def inbound_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_class.setter
    def instance_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="livenessCheck")
    def liveness_check(self) -> Optional[pulumi.Input[FlexibleAppVersionLivenessCheckArgs]]:
        
        ...
    
    @liveness_check.setter
    def liveness_check(self, value: Optional[pulumi.Input[FlexibleAppVersionLivenessCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualScaling")
    def manual_scaling(self) -> Optional[pulumi.Input[FlexibleAppVersionManualScalingArgs]]:
        
        ...
    
    @manual_scaling.setter
    def manual_scaling(self, value: Optional[pulumi.Input[FlexibleAppVersionManualScalingArgs]]): # -> None:
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
    def network(self) -> Optional[pulumi.Input[FlexibleAppVersionNetworkArgs]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[FlexibleAppVersionNetworkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nobuildFilesRegex")
    def nobuild_files_regex(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nobuild_files_regex.setter
    def nobuild_files_regex(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noopOnDestroy")
    def noop_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @noop_on_destroy.setter
    def noop_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readinessCheck")
    def readiness_check(self) -> Optional[pulumi.Input[FlexibleAppVersionReadinessCheckArgs]]:
        
        ...
    
    @readiness_check.setter
    def readiness_check(self, value: Optional[pulumi.Input[FlexibleAppVersionReadinessCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[FlexibleAppVersionResourcesArgs]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[FlexibleAppVersionResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeApiVersion")
    def runtime_api_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_api_version.setter
    def runtime_api_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeChannel")
    def runtime_channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_channel.setter
    def runtime_channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeMainExecutablePath")
    def runtime_main_executable_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_main_executable_path.setter
    def runtime_main_executable_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servingStatus")
    def serving_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serving_status.setter
    def serving_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccessConnector")
    def vpc_access_connector(self) -> Optional[pulumi.Input[FlexibleAppVersionVpcAccessConnectorArgs]]:
        
        ...
    
    @vpc_access_connector.setter
    def vpc_access_connector(self, value: Optional[pulumi.Input[FlexibleAppVersionVpcAccessConnectorArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class FlexibleAppVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_config: Optional[pulumi.Input[Union[FlexibleAppVersionApiConfigArgs, FlexibleAppVersionApiConfigArgsDict]]] = ..., automatic_scaling: Optional[pulumi.Input[Union[FlexibleAppVersionAutomaticScalingArgs, FlexibleAppVersionAutomaticScalingArgsDict]]] = ..., beta_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., default_expiration: Optional[pulumi.Input[_builtins.str]] = ..., delete_service_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., deployment: Optional[pulumi.Input[Union[FlexibleAppVersionDeploymentArgs, FlexibleAppVersionDeploymentArgsDict]]] = ..., endpoints_api_service: Optional[pulumi.Input[Union[FlexibleAppVersionEndpointsApiServiceArgs, FlexibleAppVersionEndpointsApiServiceArgsDict]]] = ..., entrypoint: Optional[pulumi.Input[Union[FlexibleAppVersionEntrypointArgs, FlexibleAppVersionEntrypointArgsDict]]] = ..., env_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., flexible_runtime_settings: Optional[pulumi.Input[Union[FlexibleAppVersionFlexibleRuntimeSettingsArgs, FlexibleAppVersionFlexibleRuntimeSettingsArgsDict]]] = ..., handlers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FlexibleAppVersionHandlerArgs, FlexibleAppVersionHandlerArgsDict]]]]] = ..., inbound_services: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instance_class: Optional[pulumi.Input[_builtins.str]] = ..., liveness_check: Optional[pulumi.Input[Union[FlexibleAppVersionLivenessCheckArgs, FlexibleAppVersionLivenessCheckArgsDict]]] = ..., manual_scaling: Optional[pulumi.Input[Union[FlexibleAppVersionManualScalingArgs, FlexibleAppVersionManualScalingArgsDict]]] = ..., network: Optional[pulumi.Input[Union[FlexibleAppVersionNetworkArgs, FlexibleAppVersionNetworkArgsDict]]] = ..., nobuild_files_regex: Optional[pulumi.Input[_builtins.str]] = ..., noop_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., readiness_check: Optional[pulumi.Input[Union[FlexibleAppVersionReadinessCheckArgs, FlexibleAppVersionReadinessCheckArgsDict]]] = ..., resources: Optional[pulumi.Input[Union[FlexibleAppVersionResourcesArgs, FlexibleAppVersionResourcesArgsDict]]] = ..., runtime: Optional[pulumi.Input[_builtins.str]] = ..., runtime_api_version: Optional[pulumi.Input[_builtins.str]] = ..., runtime_channel: Optional[pulumi.Input[_builtins.str]] = ..., runtime_main_executable_path: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., serving_status: Optional[pulumi.Input[_builtins.str]] = ..., version_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_access_connector: Optional[pulumi.Input[Union[FlexibleAppVersionVpcAccessConnectorArgs, FlexibleAppVersionVpcAccessConnectorArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FlexibleAppVersionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_config: Optional[pulumi.Input[Union[FlexibleAppVersionApiConfigArgs, FlexibleAppVersionApiConfigArgsDict]]] = ..., automatic_scaling: Optional[pulumi.Input[Union[FlexibleAppVersionAutomaticScalingArgs, FlexibleAppVersionAutomaticScalingArgsDict]]] = ..., beta_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., default_expiration: Optional[pulumi.Input[_builtins.str]] = ..., delete_service_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., deployment: Optional[pulumi.Input[Union[FlexibleAppVersionDeploymentArgs, FlexibleAppVersionDeploymentArgsDict]]] = ..., endpoints_api_service: Optional[pulumi.Input[Union[FlexibleAppVersionEndpointsApiServiceArgs, FlexibleAppVersionEndpointsApiServiceArgsDict]]] = ..., entrypoint: Optional[pulumi.Input[Union[FlexibleAppVersionEntrypointArgs, FlexibleAppVersionEntrypointArgsDict]]] = ..., env_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., flexible_runtime_settings: Optional[pulumi.Input[Union[FlexibleAppVersionFlexibleRuntimeSettingsArgs, FlexibleAppVersionFlexibleRuntimeSettingsArgsDict]]] = ..., handlers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FlexibleAppVersionHandlerArgs, FlexibleAppVersionHandlerArgsDict]]]]] = ..., inbound_services: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instance_class: Optional[pulumi.Input[_builtins.str]] = ..., liveness_check: Optional[pulumi.Input[Union[FlexibleAppVersionLivenessCheckArgs, FlexibleAppVersionLivenessCheckArgsDict]]] = ..., manual_scaling: Optional[pulumi.Input[Union[FlexibleAppVersionManualScalingArgs, FlexibleAppVersionManualScalingArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[Union[FlexibleAppVersionNetworkArgs, FlexibleAppVersionNetworkArgsDict]]] = ..., nobuild_files_regex: Optional[pulumi.Input[_builtins.str]] = ..., noop_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., readiness_check: Optional[pulumi.Input[Union[FlexibleAppVersionReadinessCheckArgs, FlexibleAppVersionReadinessCheckArgsDict]]] = ..., resources: Optional[pulumi.Input[Union[FlexibleAppVersionResourcesArgs, FlexibleAppVersionResourcesArgsDict]]] = ..., runtime: Optional[pulumi.Input[_builtins.str]] = ..., runtime_api_version: Optional[pulumi.Input[_builtins.str]] = ..., runtime_channel: Optional[pulumi.Input[_builtins.str]] = ..., runtime_main_executable_path: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., serving_status: Optional[pulumi.Input[_builtins.str]] = ..., version_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_access_connector: Optional[pulumi.Input[Union[FlexibleAppVersionVpcAccessConnectorArgs, FlexibleAppVersionVpcAccessConnectorArgsDict]]] = ...) -> FlexibleAppVersion:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConfig")
    def api_config(self) -> pulumi.Output[Optional[outputs.FlexibleAppVersionApiConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticScaling")
    def automatic_scaling(self) -> pulumi.Output[Optional[outputs.FlexibleAppVersionAutomaticScaling]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="betaSettings")
    def beta_settings(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultExpiration")
    def default_expiration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteServiceOnDestroy")
    def delete_service_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> pulumi.Output[Optional[outputs.FlexibleAppVersionDeployment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointsApiService")
    def endpoints_api_service(self) -> pulumi.Output[Optional[outputs.FlexibleAppVersionEndpointsApiService]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entrypoint(self) -> pulumi.Output[Optional[outputs.FlexibleAppVersionEntrypoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="envVariables")
    def env_variables(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flexibleRuntimeSettings")
    def flexible_runtime_settings(self) -> pulumi.Output[Optional[outputs.FlexibleAppVersionFlexibleRuntimeSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def handlers(self) -> pulumi.Output[Sequence[outputs.FlexibleAppVersionHandler]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundServices")
    def inbound_services(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="livenessCheck")
    def liveness_check(self) -> pulumi.Output[outputs.FlexibleAppVersionLivenessCheck]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualScaling")
    def manual_scaling(self) -> pulumi.Output[Optional[outputs.FlexibleAppVersionManualScaling]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional[outputs.FlexibleAppVersionNetwork]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nobuildFilesRegex")
    def nobuild_files_regex(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noopOnDestroy")
    def noop_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readinessCheck")
    def readiness_check(self) -> pulumi.Output[outputs.FlexibleAppVersionReadinessCheck]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional[outputs.FlexibleAppVersionResources]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeApiVersion")
    def runtime_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeChannel")
    def runtime_channel(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeMainExecutablePath")
    def runtime_main_executable_path(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servingStatus")
    def serving_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccessConnector")
    def vpc_access_connector(self) -> pulumi.Output[Optional[outputs.FlexibleAppVersionVpcAccessConnector]]:
        
        ...
    


