import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StandardAppVersionArgs", "StandardAppVersion"]

@pulumi.input_type
class StandardAppVersionArgs:
    def __init__(
        __self__,
        *,
        deployment: pulumi.Input[StandardAppVersionDeploymentArgs],
        entrypoint: pulumi.Input[StandardAppVersionEntrypointArgs],
        runtime: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
        app_engine_apis: Optional[pulumi.Input[_builtins.bool]] = ...,
        automatic_scaling: Optional[
            pulumi.Input[StandardAppVersionAutomaticScalingArgs]
        ] = ...,
        basic_scaling: Optional[pulumi.Input[StandardAppVersionBasicScalingArgs]] = ...,
        delete_service_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        env_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        handlers: Optional[
            pulumi.Input[Sequence[pulumi.Input[StandardAppVersionHandlerArgs]]]
        ] = ...,
        inbound_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        instance_class: Optional[pulumi.Input[_builtins.str]] = ...,
        libraries: Optional[
            pulumi.Input[Sequence[pulumi.Input[StandardAppVersionLibraryArgs]]]
        ] = ...,
        manual_scaling: Optional[
            pulumi.Input[StandardAppVersionManualScalingArgs]
        ] = ...,
        noop_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_api_version: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        threadsafe: Optional[pulumi.Input[_builtins.bool]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_access_connector: Optional[
            pulumi.Input[StandardAppVersionVpcAccessConnectorArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> pulumi.Input[StandardAppVersionDeploymentArgs]: ...
    @deployment.setter
    def deployment(self, value: pulumi.Input[StandardAppVersionDeploymentArgs]): ...
    @_builtins.property
    @pulumi.getter
    def entrypoint(self) -> pulumi.Input[StandardAppVersionEntrypointArgs]: ...
    @entrypoint.setter
    def entrypoint(self, value: pulumi.Input[StandardAppVersionEntrypointArgs]): ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Input[_builtins.str]: ...
    @runtime.setter
    def runtime(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appEngineApis")
    def app_engine_apis(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @app_engine_apis.setter
    def app_engine_apis(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="automaticScaling")
    def automatic_scaling(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionAutomaticScalingArgs]]: ...
    @automatic_scaling.setter
    def automatic_scaling(
        self, value: Optional[pulumi.Input[StandardAppVersionAutomaticScalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="basicScaling")
    def basic_scaling(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionBasicScalingArgs]]: ...
    @basic_scaling.setter
    def basic_scaling(
        self, value: Optional[pulumi.Input[StandardAppVersionBasicScalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteServiceOnDestroy")
    def delete_service_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_service_on_destroy.setter
    def delete_service_on_destroy(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="envVariables")
    def env_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @env_variables.setter
    def env_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def handlers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StandardAppVersionHandlerArgs]]]
    ]: ...
    @handlers.setter
    def handlers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StandardAppVersionHandlerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inboundServices")
    def inbound_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inbound_services.setter
    def inbound_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_class.setter
    def instance_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def libraries(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StandardAppVersionLibraryArgs]]]
    ]: ...
    @libraries.setter
    def libraries(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StandardAppVersionLibraryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manualScaling")
    def manual_scaling(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionManualScalingArgs]]: ...
    @manual_scaling.setter
    def manual_scaling(
        self, value: Optional[pulumi.Input[StandardAppVersionManualScalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="noopOnDestroy")
    def noop_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @noop_on_destroy.setter
    def noop_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeApiVersion")
    def runtime_api_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_api_version.setter
    def runtime_api_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def threadsafe(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @threadsafe.setter
    def threadsafe(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessConnector")
    def vpc_access_connector(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionVpcAccessConnectorArgs]]: ...
    @vpc_access_connector.setter
    def vpc_access_connector(
        self, value: Optional[pulumi.Input[StandardAppVersionVpcAccessConnectorArgs]]
    ): ...

@pulumi.input_type
class _StandardAppVersionState:
    def __init__(
        __self__,
        *,
        app_engine_apis: Optional[pulumi.Input[_builtins.bool]] = ...,
        automatic_scaling: Optional[
            pulumi.Input[StandardAppVersionAutomaticScalingArgs]
        ] = ...,
        basic_scaling: Optional[pulumi.Input[StandardAppVersionBasicScalingArgs]] = ...,
        delete_service_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        deployment: Optional[pulumi.Input[StandardAppVersionDeploymentArgs]] = ...,
        entrypoint: Optional[pulumi.Input[StandardAppVersionEntrypointArgs]] = ...,
        env_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        handlers: Optional[
            pulumi.Input[Sequence[pulumi.Input[StandardAppVersionHandlerArgs]]]
        ] = ...,
        inbound_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        instance_class: Optional[pulumi.Input[_builtins.str]] = ...,
        libraries: Optional[
            pulumi.Input[Sequence[pulumi.Input[StandardAppVersionLibraryArgs]]]
        ] = ...,
        manual_scaling: Optional[
            pulumi.Input[StandardAppVersionManualScalingArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        noop_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_api_version: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        threadsafe: Optional[pulumi.Input[_builtins.bool]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_access_connector: Optional[
            pulumi.Input[StandardAppVersionVpcAccessConnectorArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appEngineApis")
    def app_engine_apis(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @app_engine_apis.setter
    def app_engine_apis(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="automaticScaling")
    def automatic_scaling(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionAutomaticScalingArgs]]: ...
    @automatic_scaling.setter
    def automatic_scaling(
        self, value: Optional[pulumi.Input[StandardAppVersionAutomaticScalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="basicScaling")
    def basic_scaling(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionBasicScalingArgs]]: ...
    @basic_scaling.setter
    def basic_scaling(
        self, value: Optional[pulumi.Input[StandardAppVersionBasicScalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteServiceOnDestroy")
    def delete_service_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_service_on_destroy.setter
    def delete_service_on_destroy(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def deployment(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionDeploymentArgs]]: ...
    @deployment.setter
    def deployment(
        self, value: Optional[pulumi.Input[StandardAppVersionDeploymentArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def entrypoint(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionEntrypointArgs]]: ...
    @entrypoint.setter
    def entrypoint(
        self, value: Optional[pulumi.Input[StandardAppVersionEntrypointArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="envVariables")
    def env_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @env_variables.setter
    def env_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def handlers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StandardAppVersionHandlerArgs]]]
    ]: ...
    @handlers.setter
    def handlers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StandardAppVersionHandlerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inboundServices")
    def inbound_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inbound_services.setter
    def inbound_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_class.setter
    def instance_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def libraries(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StandardAppVersionLibraryArgs]]]
    ]: ...
    @libraries.setter
    def libraries(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StandardAppVersionLibraryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manualScaling")
    def manual_scaling(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionManualScalingArgs]]: ...
    @manual_scaling.setter
    def manual_scaling(
        self, value: Optional[pulumi.Input[StandardAppVersionManualScalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="noopOnDestroy")
    def noop_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @noop_on_destroy.setter
    def noop_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeApiVersion")
    def runtime_api_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_api_version.setter
    def runtime_api_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def threadsafe(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @threadsafe.setter
    def threadsafe(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessConnector")
    def vpc_access_connector(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionVpcAccessConnectorArgs]]: ...
    @vpc_access_connector.setter
    def vpc_access_connector(
        self, value: Optional[pulumi.Input[StandardAppVersionVpcAccessConnectorArgs]]
    ): ...

@pulumi.type_token(...)
class StandardAppVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_engine_apis: Optional[pulumi.Input[_builtins.bool]] = ...,
        automatic_scaling: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionAutomaticScalingArgs,
                    StandardAppVersionAutomaticScalingArgsDict,
                ]
            ]
        ] = ...,
        basic_scaling: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionBasicScalingArgs,
                    StandardAppVersionBasicScalingArgsDict,
                ]
            ]
        ] = ...,
        delete_service_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        deployment: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionDeploymentArgs,
                    StandardAppVersionDeploymentArgsDict,
                ]
            ]
        ] = ...,
        entrypoint: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionEntrypointArgs,
                    StandardAppVersionEntrypointArgsDict,
                ]
            ]
        ] = ...,
        env_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        handlers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            StandardAppVersionHandlerArgs,
                            StandardAppVersionHandlerArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        inbound_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        instance_class: Optional[pulumi.Input[_builtins.str]] = ...,
        libraries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            StandardAppVersionLibraryArgs,
                            StandardAppVersionLibraryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        manual_scaling: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionManualScalingArgs,
                    StandardAppVersionManualScalingArgsDict,
                ]
            ]
        ] = ...,
        noop_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_api_version: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        threadsafe: Optional[pulumi.Input[_builtins.bool]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_access_connector: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionVpcAccessConnectorArgs,
                    StandardAppVersionVpcAccessConnectorArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StandardAppVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_engine_apis: Optional[pulumi.Input[_builtins.bool]] = ...,
        automatic_scaling: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionAutomaticScalingArgs,
                    StandardAppVersionAutomaticScalingArgsDict,
                ]
            ]
        ] = ...,
        basic_scaling: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionBasicScalingArgs,
                    StandardAppVersionBasicScalingArgsDict,
                ]
            ]
        ] = ...,
        delete_service_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        deployment: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionDeploymentArgs,
                    StandardAppVersionDeploymentArgsDict,
                ]
            ]
        ] = ...,
        entrypoint: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionEntrypointArgs,
                    StandardAppVersionEntrypointArgsDict,
                ]
            ]
        ] = ...,
        env_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        handlers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            StandardAppVersionHandlerArgs,
                            StandardAppVersionHandlerArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        inbound_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        instance_class: Optional[pulumi.Input[_builtins.str]] = ...,
        libraries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            StandardAppVersionLibraryArgs,
                            StandardAppVersionLibraryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        manual_scaling: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionManualScalingArgs,
                    StandardAppVersionManualScalingArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        noop_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_api_version: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        threadsafe: Optional[pulumi.Input[_builtins.bool]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_access_connector: Optional[
            pulumi.Input[
                Union[
                    StandardAppVersionVpcAccessConnectorArgs,
                    StandardAppVersionVpcAccessConnectorArgsDict,
                ]
            ]
        ] = ...,
    ) -> StandardAppVersion: ...
    @_builtins.property
    @pulumi.getter(name="appEngineApis")
    def app_engine_apis(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="automaticScaling")
    def automatic_scaling(
        self,
    ) -> pulumi.Output[Optional[outputs.StandardAppVersionAutomaticScaling]]: ...
    @_builtins.property
    @pulumi.getter(name="basicScaling")
    def basic_scaling(
        self,
    ) -> pulumi.Output[Optional[outputs.StandardAppVersionBasicScaling]]: ...
    @_builtins.property
    @pulumi.getter(name="deleteServiceOnDestroy")
    def delete_service_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> pulumi.Output[outputs.StandardAppVersionDeployment]: ...
    @_builtins.property
    @pulumi.getter
    def entrypoint(self) -> pulumi.Output[outputs.StandardAppVersionEntrypoint]: ...
    @_builtins.property
    @pulumi.getter(name="envVariables")
    def env_variables(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def handlers(
        self,
    ) -> pulumi.Output[Sequence[outputs.StandardAppVersionHandler]]: ...
    @_builtins.property
    @pulumi.getter(name="inboundServices")
    def inbound_services(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def libraries(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.StandardAppVersionLibrary]]]: ...
    @_builtins.property
    @pulumi.getter(name="manualScaling")
    def manual_scaling(
        self,
    ) -> pulumi.Output[Optional[outputs.StandardAppVersionManualScaling]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="noopOnDestroy")
    def noop_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeApiVersion")
    def runtime_api_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def threadsafe(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessConnector")
    def vpc_access_connector(
        self,
    ) -> pulumi.Output[Optional[outputs.StandardAppVersionVpcAccessConnector]]: ...
