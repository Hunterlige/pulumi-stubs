

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CustomDomainAssociationCertificateValidationRecord', 'DeploymentTimeouts', 'ObservabilityConfigurationTraceConfiguration', 'ServiceEncryptionConfiguration', 'ServiceHealthCheckConfiguration', 'ServiceInstanceConfiguration', 'ServiceNetworkConfiguration', 'ServiceNetworkConfigurationEgressConfiguration', 'ServiceNetworkConfigurationIngressConfiguration', 'ServiceObservabilityConfiguration', 'ServiceSourceConfiguration', ..., 'ServiceSourceConfigurationCodeRepository', ..., ..., ..., 'ServiceSourceConfigurationImageRepository', ..., 'VpcIngressConnectionIngressVpcConfiguration']
@pulumi.output_type
class CustomDomainAssociationCertificateValidationRecord(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ObservabilityConfigurationTraceConfiguration(dict):
    def __init__(__self__, *, vendor: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vendor(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceHealthCheckConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, healthy_threshold: Optional[_builtins.int] = ..., interval: Optional[_builtins.int] = ..., path: Optional[_builtins.str] = ..., protocol: Optional[_builtins.str] = ..., timeout: Optional[_builtins.int] = ..., unhealthy_threshold: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceInstanceConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu: Optional[_builtins.str] = ..., instance_role_arn: Optional[_builtins.str] = ..., memory: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRoleArn")
    def instance_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, egress_configuration: Optional[outputs.ServiceNetworkConfigurationEgressConfiguration] = ..., ingress_configuration: Optional[outputs.ServiceNetworkConfigurationIngressConfiguration] = ..., ip_address_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressConfiguration")
    def egress_configuration(self) -> Optional[outputs.ServiceNetworkConfigurationEgressConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressConfiguration")
    def ingress_configuration(self) -> Optional[outputs.ServiceNetworkConfigurationIngressConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceNetworkConfigurationEgressConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, egress_type: Optional[_builtins.str] = ..., vpc_connector_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressType")
    def egress_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnectorArn")
    def vpc_connector_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceNetworkConfigurationIngressConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_publicly_accessible: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPubliclyAccessible")
    def is_publicly_accessible(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ServiceObservabilityConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, observability_enabled: _builtins.bool, observability_configuration_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="observabilityEnabled")
    def observability_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="observabilityConfigurationArn")
    def observability_configuration_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceSourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication_configuration: Optional[outputs.ServiceSourceConfigurationAuthenticationConfiguration] = ..., auto_deployments_enabled: Optional[_builtins.bool] = ..., code_repository: Optional[outputs.ServiceSourceConfigurationCodeRepository] = ..., image_repository: Optional[outputs.ServiceSourceConfigurationImageRepository] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> Optional[outputs.ServiceSourceConfigurationAuthenticationConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeploymentsEnabled")
    def auto_deployments_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeRepository")
    def code_repository(self) -> Optional[outputs.ServiceSourceConfigurationCodeRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageRepository")
    def image_repository(self) -> Optional[outputs.ServiceSourceConfigurationImageRepository]:
        
        ...
    


@pulumi.output_type
class ServiceSourceConfigurationAuthenticationConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_role_arn: Optional[_builtins.str] = ..., connection_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRoleArn")
    def access_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceSourceConfigurationCodeRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, repository_url: _builtins.str, source_code_version: outputs.ServiceSourceConfigurationCodeRepositorySourceCodeVersion, code_configuration: Optional[outputs.ServiceSourceConfigurationCodeRepositoryCodeConfiguration] = ..., source_directory: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCodeVersion")
    def source_code_version(self) -> outputs.ServiceSourceConfigurationCodeRepositorySourceCodeVersion:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeConfiguration")
    def code_configuration(self) -> Optional[outputs.ServiceSourceConfigurationCodeRepositoryCodeConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDirectory")
    def source_directory(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceSourceConfigurationCodeRepositoryCodeConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, configuration_source: _builtins.str, code_configuration_values: Optional[outputs.ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSource")
    def configuration_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeConfigurationValues")
    def code_configuration_values(self) -> Optional[outputs.ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues]:
        
        ...
    


@pulumi.output_type
class ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValues(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, runtime: _builtins.str, build_command: Optional[_builtins.str] = ..., port: Optional[_builtins.str] = ..., runtime_environment_secrets: Optional[Mapping[str, _builtins.str]] = ..., runtime_environment_variables: Optional[Mapping[str, _builtins.str]] = ..., start_command: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildCommand")
    def build_command(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironmentSecrets")
    def runtime_environment_secrets(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironmentVariables")
    def runtime_environment_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startCommand")
    def start_command(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceSourceConfigurationCodeRepositorySourceCodeVersion(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceSourceConfigurationImageRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image_identifier: _builtins.str, image_repository_type: _builtins.str, image_configuration: Optional[outputs.ServiceSourceConfigurationImageRepositoryImageConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageIdentifier")
    def image_identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageRepositoryType")
    def image_repository_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageConfiguration")
    def image_configuration(self) -> Optional[outputs.ServiceSourceConfigurationImageRepositoryImageConfiguration]:
        
        ...
    


@pulumi.output_type
class ServiceSourceConfigurationImageRepositoryImageConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port: Optional[_builtins.str] = ..., runtime_environment_secrets: Optional[Mapping[str, _builtins.str]] = ..., runtime_environment_variables: Optional[Mapping[str, _builtins.str]] = ..., start_command: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironmentSecrets")
    def runtime_environment_secrets(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironmentVariables")
    def runtime_environment_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startCommand")
    def start_command(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcIngressConnectionIngressVpcConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, vpc_endpoint_id: Optional[_builtins.str] = ..., vpc_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]:
        
        ...
    


