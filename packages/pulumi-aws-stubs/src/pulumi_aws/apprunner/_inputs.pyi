import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    ...,
    "DeploymentTimeoutsArgs",
    "DeploymentTimeoutsArgsDict",
    "ObservabilityConfigurationTraceConfigurationArgs",
    ...,
    "ServiceEncryptionConfigurationArgs",
    "ServiceEncryptionConfigurationArgsDict",
    "ServiceHealthCheckConfigurationArgs",
    "ServiceHealthCheckConfigurationArgsDict",
    "ServiceInstanceConfigurationArgs",
    "ServiceInstanceConfigurationArgsDict",
    "ServiceNetworkConfigurationArgs",
    "ServiceNetworkConfigurationArgsDict",
    "ServiceNetworkConfigurationEgressConfigurationArgs",
    ...,
    ...,
    ...,
    "ServiceObservabilityConfigurationArgs",
    "ServiceObservabilityConfigurationArgsDict",
    "ServiceSourceConfigurationArgs",
    "ServiceSourceConfigurationArgsDict",
    ...,
    ...,
    "ServiceSourceConfigurationCodeRepositoryArgs",
    "ServiceSourceConfigurationCodeRepositoryArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ServiceSourceConfigurationImageRepositoryArgs",
    "ServiceSourceConfigurationImageRepositoryArgsDict",
    ...,
    ...,
    "VpcIngressConnectionIngressVpcConfigurationArgs",
    ...,
]

class CustomDomainAssociationCertificateValidationRecordArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CustomDomainAssociationCertificateValidationRecordArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DeploymentTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ObservabilityConfigurationTraceConfigurationArgsDict(TypedDict):
    vendor: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ObservabilityConfigurationTraceConfigurationArgs:
    def __init__(
        __self__, *, vendor: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def vendor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vendor.setter
    def vendor(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceEncryptionConfigurationArgsDict(TypedDict):
    kms_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ServiceEncryptionConfigurationArgs:
    def __init__(__self__, *, kms_key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key.setter
    def kms_key(self, value: pulumi.Input[_builtins.str]): ...

class ServiceHealthCheckConfigurationArgsDict(TypedDict):
    healthy_threshold: NotRequired[pulumi.Input[_builtins.int]]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.int]]
    unhealthy_threshold: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ServiceHealthCheckConfigurationArgs:
    def __init__(
        __self__,
        *,
        healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @healthy_threshold.setter
    def healthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceInstanceConfigurationArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.str]]
    instance_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    memory: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceInstanceConfigurationArgs:
    def __init__(
        __self__,
        *,
        cpu: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        memory: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceRoleArn")
    def instance_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_role_arn.setter
    def instance_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceNetworkConfigurationArgsDict(TypedDict):
    egress_configuration: NotRequired[
        pulumi.Input[ServiceNetworkConfigurationEgressConfigurationArgsDict]
    ]
    ingress_configuration: NotRequired[
        pulumi.Input[ServiceNetworkConfigurationIngressConfigurationArgsDict]
    ]
    ip_address_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        egress_configuration: Optional[
            pulumi.Input[ServiceNetworkConfigurationEgressConfigurationArgs]
        ] = ...,
        ingress_configuration: Optional[
            pulumi.Input[ServiceNetworkConfigurationIngressConfigurationArgs]
        ] = ...,
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressConfiguration")
    def egress_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceNetworkConfigurationEgressConfigurationArgs]]: ...
    @egress_configuration.setter
    def egress_configuration(
        self,
        value: Optional[
            pulumi.Input[ServiceNetworkConfigurationEgressConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressConfiguration")
    def ingress_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ServiceNetworkConfigurationIngressConfigurationArgs]
    ]: ...
    @ingress_configuration.setter
    def ingress_configuration(
        self,
        value: Optional[
            pulumi.Input[ServiceNetworkConfigurationIngressConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceNetworkConfigurationEgressConfigurationArgsDict(TypedDict):
    egress_type: NotRequired[pulumi.Input[_builtins.str]]
    vpc_connector_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceNetworkConfigurationEgressConfigurationArgs:
    def __init__(
        __self__,
        *,
        egress_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_connector_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressType")
    def egress_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @egress_type.setter
    def egress_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcConnectorArn")
    def vpc_connector_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_connector_arn.setter
    def vpc_connector_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceNetworkConfigurationIngressConfigurationArgsDict(TypedDict):
    is_publicly_accessible: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class ServiceNetworkConfigurationIngressConfigurationArgs:
    def __init__(
        __self__,
        *,
        is_publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isPubliclyAccessible")
    def is_publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_publicly_accessible.setter
    def is_publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServiceObservabilityConfigurationArgsDict(TypedDict):
    observability_enabled: pulumi.Input[_builtins.bool]
    observability_configuration_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceObservabilityConfigurationArgs:
    def __init__(
        __self__,
        *,
        observability_enabled: pulumi.Input[_builtins.bool],
        observability_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="observabilityEnabled")
    def observability_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @observability_enabled.setter
    def observability_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="observabilityConfigurationArn")
    def observability_configuration_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @observability_configuration_arn.setter
    def observability_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ServiceSourceConfigurationArgsDict(TypedDict):
    authentication_configuration: NotRequired[
        pulumi.Input[ServiceSourceConfigurationAuthenticationConfigurationArgsDict]
    ]
    auto_deployments_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    code_repository: NotRequired[
        pulumi.Input[ServiceSourceConfigurationCodeRepositoryArgsDict]
    ]
    image_repository: NotRequired[
        pulumi.Input[ServiceSourceConfigurationImageRepositoryArgsDict]
    ]
    ...

@pulumi.input_type
class ServiceSourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        authentication_configuration: Optional[
            pulumi.Input[ServiceSourceConfigurationAuthenticationConfigurationArgs]
        ] = ...,
        auto_deployments_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        code_repository: Optional[
            pulumi.Input[ServiceSourceConfigurationCodeRepositoryArgs]
        ] = ...,
        image_repository: Optional[
            pulumi.Input[ServiceSourceConfigurationImageRepositoryArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ServiceSourceConfigurationAuthenticationConfigurationArgs]
    ]: ...
    @authentication_configuration.setter
    def authentication_configuration(
        self,
        value: Optional[
            pulumi.Input[ServiceSourceConfigurationAuthenticationConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoDeploymentsEnabled")
    def auto_deployments_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_deployments_enabled.setter
    def auto_deployments_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="codeRepository")
    def code_repository(
        self,
    ) -> Optional[pulumi.Input[ServiceSourceConfigurationCodeRepositoryArgs]]: ...
    @code_repository.setter
    def code_repository(
        self,
        value: Optional[pulumi.Input[ServiceSourceConfigurationCodeRepositoryArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageRepository")
    def image_repository(
        self,
    ) -> Optional[pulumi.Input[ServiceSourceConfigurationImageRepositoryArgs]]: ...
    @image_repository.setter
    def image_repository(
        self,
        value: Optional[pulumi.Input[ServiceSourceConfigurationImageRepositoryArgs]],
    ): ...

class ServiceSourceConfigurationAuthenticationConfigurationArgsDict(TypedDict):
    access_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    connection_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceSourceConfigurationAuthenticationConfigurationArgs:
    def __init__(
        __self__,
        *,
        access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessRoleArn")
    def access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_role_arn.setter
    def access_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_arn.setter
    def connection_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceSourceConfigurationCodeRepositoryArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]
    source_code_version: pulumi.Input[
        ServiceSourceConfigurationCodeRepositorySourceCodeVersionArgsDict
    ]
    code_configuration: NotRequired[
        pulumi.Input[ServiceSourceConfigurationCodeRepositoryCodeConfigurationArgsDict]
    ]
    source_directory: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceSourceConfigurationCodeRepositoryArgs:
    def __init__(
        __self__,
        *,
        repository_url: pulumi.Input[_builtins.str],
        source_code_version: pulumi.Input[
            ServiceSourceConfigurationCodeRepositorySourceCodeVersionArgs
        ],
        code_configuration: Optional[
            pulumi.Input[ServiceSourceConfigurationCodeRepositoryCodeConfigurationArgs]
        ] = ...,
        source_directory: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]: ...
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceCodeVersion")
    def source_code_version(
        self,
    ) -> pulumi.Input[
        ServiceSourceConfigurationCodeRepositorySourceCodeVersionArgs
    ]: ...
    @source_code_version.setter
    def source_code_version(
        self,
        value: pulumi.Input[
            ServiceSourceConfigurationCodeRepositorySourceCodeVersionArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="codeConfiguration")
    def code_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ServiceSourceConfigurationCodeRepositoryCodeConfigurationArgs]
    ]: ...
    @code_configuration.setter
    def code_configuration(
        self,
        value: Optional[
            pulumi.Input[ServiceSourceConfigurationCodeRepositoryCodeConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceDirectory")
    def source_directory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_directory.setter
    def source_directory(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceSourceConfigurationCodeRepositoryCodeConfigurationArgsDict(TypedDict):
    configuration_source: pulumi.Input[_builtins.str]
    code_configuration_values: NotRequired[
        pulumi.Input[
            ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesArgsDict
        ]
    ]
    ...

@pulumi.input_type
class ServiceSourceConfigurationCodeRepositoryCodeConfigurationArgs:
    def __init__(
        __self__,
        *,
        configuration_source: pulumi.Input[_builtins.str],
        code_configuration_values: Optional[
            pulumi.Input[
                ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationSource")
    def configuration_source(self) -> pulumi.Input[_builtins.str]: ...
    @configuration_source.setter
    def configuration_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="codeConfigurationValues")
    def code_configuration_values(
        self,
    ) -> Optional[
        pulumi.Input[
            ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesArgs
        ]
    ]: ...
    @code_configuration_values.setter
    def code_configuration_values(
        self,
        value: Optional[
            pulumi.Input[
                ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesArgs
            ]
        ],
    ): ...

class ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesArgsDict(
    TypedDict
):
    runtime: pulumi.Input[_builtins.str]
    build_command: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.str]]
    runtime_environment_secrets: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    runtime_environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    start_command: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesArgs:
    def __init__(
        __self__,
        *,
        runtime: pulumi.Input[_builtins.str],
        build_command: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_environment_secrets: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        runtime_environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        start_command: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Input[_builtins.str]: ...
    @runtime.setter
    def runtime(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="buildCommand")
    def build_command(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_command.setter
    def build_command(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironmentSecrets")
    def runtime_environment_secrets(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @runtime_environment_secrets.setter
    def runtime_environment_secrets(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironmentVariables")
    def runtime_environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @runtime_environment_variables.setter
    def runtime_environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startCommand")
    def start_command(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_command.setter
    def start_command(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceSourceConfigurationCodeRepositorySourceCodeVersionArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ServiceSourceConfigurationCodeRepositorySourceCodeVersionArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ServiceSourceConfigurationImageRepositoryArgsDict(TypedDict):
    image_identifier: pulumi.Input[_builtins.str]
    image_repository_type: pulumi.Input[_builtins.str]
    image_configuration: NotRequired[
        pulumi.Input[
            ServiceSourceConfigurationImageRepositoryImageConfigurationArgsDict
        ]
    ]
    ...

@pulumi.input_type
class ServiceSourceConfigurationImageRepositoryArgs:
    def __init__(
        __self__,
        *,
        image_identifier: pulumi.Input[_builtins.str],
        image_repository_type: pulumi.Input[_builtins.str],
        image_configuration: Optional[
            pulumi.Input[
                ServiceSourceConfigurationImageRepositoryImageConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageIdentifier")
    def image_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @image_identifier.setter
    def image_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="imageRepositoryType")
    def image_repository_type(self) -> pulumi.Input[_builtins.str]: ...
    @image_repository_type.setter
    def image_repository_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="imageConfiguration")
    def image_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ServiceSourceConfigurationImageRepositoryImageConfigurationArgs]
    ]: ...
    @image_configuration.setter
    def image_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ServiceSourceConfigurationImageRepositoryImageConfigurationArgs
            ]
        ],
    ): ...

class ServiceSourceConfigurationImageRepositoryImageConfigurationArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.str]]
    runtime_environment_secrets: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    runtime_environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    start_command: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceSourceConfigurationImageRepositoryImageConfigurationArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_environment_secrets: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        runtime_environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        start_command: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironmentSecrets")
    def runtime_environment_secrets(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @runtime_environment_secrets.setter
    def runtime_environment_secrets(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironmentVariables")
    def runtime_environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @runtime_environment_variables.setter
    def runtime_environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startCommand")
    def start_command(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_command.setter
    def start_command(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VpcIngressConnectionIngressVpcConfigurationArgsDict(TypedDict):
    vpc_endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class VpcIngressConnectionIngressVpcConfigurationArgs:
    def __init__(
        __self__,
        *,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
