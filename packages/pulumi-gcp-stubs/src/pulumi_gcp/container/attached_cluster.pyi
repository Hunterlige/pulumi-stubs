import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AttachedClusterArgs", "AttachedCluster"]

@pulumi.input_type
class AttachedClusterArgs:
    def __init__(
        __self__,
        *,
        distribution: pulumi.Input[_builtins.str],
        fleet: pulumi.Input[AttachedClusterFleetArgs],
        location: pulumi.Input[_builtins.str],
        oidc_config: pulumi.Input[AttachedClusterOidcConfigArgs],
        platform_version: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        authorization: Optional[pulumi.Input[AttachedClusterAuthorizationArgs]] = ...,
        binary_authorization: Optional[
            pulumi.Input[AttachedClusterBinaryAuthorizationArgs]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_config: Optional[pulumi.Input[AttachedClusterLoggingConfigArgs]] = ...,
        monitoring_config: Optional[
            pulumi.Input[AttachedClusterMonitoringConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_config: Optional[pulumi.Input[AttachedClusterProxyConfigArgs]] = ...,
        security_posture_config: Optional[
            pulumi.Input[AttachedClusterSecurityPostureConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> pulumi.Input[_builtins.str]: ...
    @distribution.setter
    def distribution(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> pulumi.Input[AttachedClusterFleetArgs]: ...
    @fleet.setter
    def fleet(self, value: pulumi.Input[AttachedClusterFleetArgs]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oidcConfig")
    def oidc_config(self) -> pulumi.Input[AttachedClusterOidcConfigArgs]: ...
    @oidc_config.setter
    def oidc_config(self, value: pulumi.Input[AttachedClusterOidcConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> pulumi.Input[_builtins.str]: ...
    @platform_version.setter
    def platform_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def authorization(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterAuthorizationArgs]]: ...
    @authorization.setter
    def authorization(
        self, value: Optional[pulumi.Input[AttachedClusterAuthorizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterBinaryAuthorizationArgs]]: ...
    @binary_authorization.setter
    def binary_authorization(
        self, value: Optional[pulumi.Input[AttachedClusterBinaryAuthorizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[AttachedClusterLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringConfig")
    def monitoring_config(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterMonitoringConfigArgs]]: ...
    @monitoring_config.setter
    def monitoring_config(
        self, value: Optional[pulumi.Input[AttachedClusterMonitoringConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterProxyConfigArgs]]: ...
    @proxy_config.setter
    def proxy_config(
        self, value: Optional[pulumi.Input[AttachedClusterProxyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityPostureConfig")
    @_utilities.deprecated(...)
    def security_posture_config(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterSecurityPostureConfigArgs]]: ...
    @security_posture_config.setter
    def security_posture_config(
        self, value: Optional[pulumi.Input[AttachedClusterSecurityPostureConfigArgs]]
    ): ...

@pulumi.input_type
class _AttachedClusterState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        authorization: Optional[pulumi.Input[AttachedClusterAuthorizationArgs]] = ...,
        binary_authorization: Optional[
            pulumi.Input[AttachedClusterBinaryAuthorizationArgs]
        ] = ...,
        cluster_region: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[AttachedClusterErrorArgs]]]
        ] = ...,
        fleet: Optional[pulumi.Input[AttachedClusterFleetArgs]] = ...,
        kubernetes_version: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_config: Optional[pulumi.Input[AttachedClusterLoggingConfigArgs]] = ...,
        monitoring_config: Optional[
            pulumi.Input[AttachedClusterMonitoringConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oidc_config: Optional[pulumi.Input[AttachedClusterOidcConfigArgs]] = ...,
        platform_version: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_config: Optional[pulumi.Input[AttachedClusterProxyConfigArgs]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_posture_config: Optional[
            pulumi.Input[AttachedClusterSecurityPostureConfigArgs]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AttachedClusterWorkloadIdentityConfigArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def authorization(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterAuthorizationArgs]]: ...
    @authorization.setter
    def authorization(
        self, value: Optional[pulumi.Input[AttachedClusterAuthorizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterBinaryAuthorizationArgs]]: ...
    @binary_authorization.setter
    def binary_authorization(
        self, value: Optional[pulumi.Input[AttachedClusterBinaryAuthorizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterRegion")
    def cluster_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_region.setter
    def cluster_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distribution.setter
    def distribution(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_annotations.setter
    def effective_annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AttachedClusterErrorArgs]]]]: ...
    @errors.setter
    def errors(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AttachedClusterErrorArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> Optional[pulumi.Input[AttachedClusterFleetArgs]]: ...
    @fleet.setter
    def fleet(self, value: Optional[pulumi.Input[AttachedClusterFleetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kubernetes_version.setter
    def kubernetes_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[AttachedClusterLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringConfig")
    def monitoring_config(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterMonitoringConfigArgs]]: ...
    @monitoring_config.setter
    def monitoring_config(
        self, value: Optional[pulumi.Input[AttachedClusterMonitoringConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oidcConfig")
    def oidc_config(self) -> Optional[pulumi.Input[AttachedClusterOidcConfigArgs]]: ...
    @oidc_config.setter
    def oidc_config(
        self, value: Optional[pulumi.Input[AttachedClusterOidcConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterProxyConfigArgs]]: ...
    @proxy_config.setter
    def proxy_config(
        self, value: Optional[pulumi.Input[AttachedClusterProxyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="securityPostureConfig")
    @_utilities.deprecated(...)
    def security_posture_config(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterSecurityPostureConfigArgs]]: ...
    @security_posture_config.setter
    def security_posture_config(
        self, value: Optional[pulumi.Input[AttachedClusterSecurityPostureConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityConfigs")
    def workload_identity_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AttachedClusterWorkloadIdentityConfigArgs]]]
    ]: ...
    @workload_identity_configs.setter
    def workload_identity_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AttachedClusterWorkloadIdentityConfigArgs]]
            ]
        ],
    ): ...

@pulumi.type_token("gcp:container/attachedCluster:AttachedCluster")
class AttachedCluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        authorization: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterAuthorizationArgs,
                    AttachedClusterAuthorizationArgsDict,
                ]
            ]
        ] = ...,
        binary_authorization: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterBinaryAuthorizationArgs,
                    AttachedClusterBinaryAuthorizationArgsDict,
                ]
            ]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution: Optional[pulumi.Input[_builtins.str]] = ...,
        fleet: Optional[
            pulumi.Input[Union[AttachedClusterFleetArgs, AttachedClusterFleetArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_config: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterLoggingConfigArgs,
                    AttachedClusterLoggingConfigArgsDict,
                ]
            ]
        ] = ...,
        monitoring_config: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterMonitoringConfigArgs,
                    AttachedClusterMonitoringConfigArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oidc_config: Optional[
            pulumi.Input[
                Union[AttachedClusterOidcConfigArgs, AttachedClusterOidcConfigArgsDict]
            ]
        ] = ...,
        platform_version: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_config: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterProxyConfigArgs, AttachedClusterProxyConfigArgsDict
                ]
            ]
        ] = ...,
        security_posture_config: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterSecurityPostureConfigArgs,
                    AttachedClusterSecurityPostureConfigArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AttachedClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        authorization: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterAuthorizationArgs,
                    AttachedClusterAuthorizationArgsDict,
                ]
            ]
        ] = ...,
        binary_authorization: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterBinaryAuthorizationArgs,
                    AttachedClusterBinaryAuthorizationArgsDict,
                ]
            ]
        ] = ...,
        cluster_region: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        errors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AttachedClusterErrorArgs, AttachedClusterErrorArgsDict]
                    ]
                ]
            ]
        ] = ...,
        fleet: Optional[
            pulumi.Input[Union[AttachedClusterFleetArgs, AttachedClusterFleetArgsDict]]
        ] = ...,
        kubernetes_version: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_config: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterLoggingConfigArgs,
                    AttachedClusterLoggingConfigArgsDict,
                ]
            ]
        ] = ...,
        monitoring_config: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterMonitoringConfigArgs,
                    AttachedClusterMonitoringConfigArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oidc_config: Optional[
            pulumi.Input[
                Union[AttachedClusterOidcConfigArgs, AttachedClusterOidcConfigArgsDict]
            ]
        ] = ...,
        platform_version: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_config: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterProxyConfigArgs, AttachedClusterProxyConfigArgsDict
                ]
            ]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_posture_config: Optional[
            pulumi.Input[
                Union[
                    AttachedClusterSecurityPostureConfigArgs,
                    AttachedClusterSecurityPostureConfigArgsDict,
                ]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AttachedClusterWorkloadIdentityConfigArgs,
                            AttachedClusterWorkloadIdentityConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> AttachedCluster: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def authorization(
        self,
    ) -> pulumi.Output[Optional[outputs.AttachedClusterAuthorization]]: ...
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(
        self,
    ) -> pulumi.Output[outputs.AttachedClusterBinaryAuthorization]: ...
    @_builtins.property
    @pulumi.getter(name="clusterRegion")
    def cluster_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence[outputs.AttachedClusterError]]: ...
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> pulumi.Output[outputs.AttachedClusterFleet]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AttachedClusterLoggingConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringConfig")
    def monitoring_config(
        self,
    ) -> pulumi.Output[outputs.AttachedClusterMonitoringConfig]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oidcConfig")
    def oidc_config(self) -> pulumi.Output[outputs.AttachedClusterOidcConfig]: ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AttachedClusterProxyConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="securityPostureConfig")
    @_utilities.deprecated(...)
    def security_posture_config(
        self,
    ) -> pulumi.Output[outputs.AttachedClusterSecurityPostureConfig]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityConfigs")
    def workload_identity_configs(
        self,
    ) -> pulumi.Output[Sequence[outputs.AttachedClusterWorkloadIdentityConfig]]: ...
