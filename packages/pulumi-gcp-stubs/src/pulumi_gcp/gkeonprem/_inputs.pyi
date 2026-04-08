import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BareMetalAdminClusterClusterOperationsArgs",
    "BareMetalAdminClusterClusterOperationsArgsDict",
    "BareMetalAdminClusterControlPlaneArgs",
    "BareMetalAdminClusterControlPlaneArgsDict",
    "BareMetalAdminClusterControlPlaneApiServerArgArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "BareMetalAdminClusterFleetArgs",
    "BareMetalAdminClusterFleetArgsDict",
    "BareMetalAdminClusterLoadBalancerArgs",
    "BareMetalAdminClusterLoadBalancerArgsDict",
    "BareMetalAdminClusterLoadBalancerBgpLbConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "BareMetalAdminClusterLoadBalancerPortConfigArgs",
    ...,
    "BareMetalAdminClusterLoadBalancerVipConfigArgs",
    "BareMetalAdminClusterLoadBalancerVipConfigArgsDict",
    "BareMetalAdminClusterMaintenanceConfigArgs",
    "BareMetalAdminClusterMaintenanceConfigArgsDict",
    "BareMetalAdminClusterNetworkConfigArgs",
    "BareMetalAdminClusterNetworkConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "BareMetalAdminClusterNodeAccessConfigArgs",
    "BareMetalAdminClusterNodeAccessConfigArgsDict",
    "BareMetalAdminClusterNodeConfigArgs",
    "BareMetalAdminClusterNodeConfigArgsDict",
    "BareMetalAdminClusterProxyArgs",
    "BareMetalAdminClusterProxyArgsDict",
    "BareMetalAdminClusterSecurityConfigArgs",
    "BareMetalAdminClusterSecurityConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "BareMetalAdminClusterStatusArgs",
    "BareMetalAdminClusterStatusArgsDict",
    "BareMetalAdminClusterStatusConditionArgs",
    "BareMetalAdminClusterStatusConditionArgsDict",
    "BareMetalAdminClusterStorageArgs",
    "BareMetalAdminClusterStorageArgsDict",
    ...,
    ...,
    "BareMetalAdminClusterStorageLvpShareConfigArgs",
    "BareMetalAdminClusterStorageLvpShareConfigArgsDict",
    ...,
    ...,
    "BareMetalAdminClusterValidationCheckArgs",
    "BareMetalAdminClusterValidationCheckArgsDict",
    "BareMetalAdminClusterValidationCheckStatusArgs",
    "BareMetalAdminClusterValidationCheckStatusArgsDict",
    ...,
    ...,
    "BareMetalClusterBinaryAuthorizationArgs",
    "BareMetalClusterBinaryAuthorizationArgsDict",
    "BareMetalClusterClusterOperationsArgs",
    "BareMetalClusterClusterOperationsArgsDict",
    "BareMetalClusterControlPlaneArgs",
    "BareMetalClusterControlPlaneArgsDict",
    "BareMetalClusterControlPlaneApiServerArgArgs",
    "BareMetalClusterControlPlaneApiServerArgArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "BareMetalClusterFleetArgs",
    "BareMetalClusterFleetArgsDict",
    "BareMetalClusterLoadBalancerArgs",
    "BareMetalClusterLoadBalancerArgsDict",
    "BareMetalClusterLoadBalancerBgpLbConfigArgs",
    "BareMetalClusterLoadBalancerBgpLbConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "BareMetalClusterLoadBalancerManualLbConfigArgs",
    "BareMetalClusterLoadBalancerManualLbConfigArgsDict",
    "BareMetalClusterLoadBalancerMetalLbConfigArgs",
    "BareMetalClusterLoadBalancerMetalLbConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "BareMetalClusterLoadBalancerPortConfigArgs",
    "BareMetalClusterLoadBalancerPortConfigArgsDict",
    "BareMetalClusterLoadBalancerVipConfigArgs",
    "BareMetalClusterLoadBalancerVipConfigArgsDict",
    "BareMetalClusterMaintenanceConfigArgs",
    "BareMetalClusterMaintenanceConfigArgsDict",
    "BareMetalClusterNetworkConfigArgs",
    "BareMetalClusterNetworkConfigArgsDict",
    "BareMetalClusterNetworkConfigIslandModeCidrArgs",
    ...,
    ...,
    ...,
    "BareMetalClusterNetworkConfigSrIovConfigArgs",
    "BareMetalClusterNetworkConfigSrIovConfigArgsDict",
    "BareMetalClusterNodeAccessConfigArgs",
    "BareMetalClusterNodeAccessConfigArgsDict",
    "BareMetalClusterNodeConfigArgs",
    "BareMetalClusterNodeConfigArgsDict",
    "BareMetalClusterOsEnvironmentConfigArgs",
    "BareMetalClusterOsEnvironmentConfigArgsDict",
    "BareMetalClusterProxyArgs",
    "BareMetalClusterProxyArgsDict",
    "BareMetalClusterSecurityConfigArgs",
    "BareMetalClusterSecurityConfigArgsDict",
    "BareMetalClusterSecurityConfigAuthorizationArgs",
    ...,
    ...,
    ...,
    "BareMetalClusterStatusArgs",
    "BareMetalClusterStatusArgsDict",
    "BareMetalClusterStatusConditionArgs",
    "BareMetalClusterStatusConditionArgsDict",
    "BareMetalClusterStorageArgs",
    "BareMetalClusterStorageArgsDict",
    "BareMetalClusterStorageLvpNodeMountsConfigArgs",
    "BareMetalClusterStorageLvpNodeMountsConfigArgsDict",
    "BareMetalClusterStorageLvpShareConfigArgs",
    "BareMetalClusterStorageLvpShareConfigArgsDict",
    "BareMetalClusterStorageLvpShareConfigLvpConfigArgs",
    ...,
    "BareMetalClusterUpgradePolicyArgs",
    "BareMetalClusterUpgradePolicyArgsDict",
    "BareMetalClusterValidationCheckArgs",
    "BareMetalClusterValidationCheckArgsDict",
    "BareMetalClusterValidationCheckStatusArgs",
    "BareMetalClusterValidationCheckStatusArgsDict",
    "BareMetalClusterValidationCheckStatusResultArgs",
    ...,
    "BareMetalNodePoolNodePoolConfigArgs",
    "BareMetalNodePoolNodePoolConfigArgsDict",
    "BareMetalNodePoolNodePoolConfigNodeConfigArgs",
    "BareMetalNodePoolNodePoolConfigNodeConfigArgsDict",
    "BareMetalNodePoolNodePoolConfigTaintArgs",
    "BareMetalNodePoolNodePoolConfigTaintArgsDict",
    "BareMetalNodePoolStatusArgs",
    "BareMetalNodePoolStatusArgsDict",
    "BareMetalNodePoolStatusConditionArgs",
    "BareMetalNodePoolStatusConditionArgsDict",
    "VMwareClusterAntiAffinityGroupsArgs",
    "VMwareClusterAntiAffinityGroupsArgsDict",
    "VMwareClusterAuthorizationArgs",
    "VMwareClusterAuthorizationArgsDict",
    "VMwareClusterAuthorizationAdminUserArgs",
    "VMwareClusterAuthorizationAdminUserArgsDict",
    "VMwareClusterAutoRepairConfigArgs",
    "VMwareClusterAutoRepairConfigArgsDict",
    "VMwareClusterControlPlaneNodeArgs",
    "VMwareClusterControlPlaneNodeArgsDict",
    "VMwareClusterControlPlaneNodeAutoResizeConfigArgs",
    ...,
    "VMwareClusterControlPlaneNodeVsphereConfigArgs",
    "VMwareClusterControlPlaneNodeVsphereConfigArgsDict",
    "VMwareClusterDataplaneV2Args",
    "VMwareClusterDataplaneV2ArgsDict",
    "VMwareClusterFleetArgs",
    "VMwareClusterFleetArgsDict",
    "VMwareClusterLoadBalancerArgs",
    "VMwareClusterLoadBalancerArgsDict",
    "VMwareClusterLoadBalancerF5ConfigArgs",
    "VMwareClusterLoadBalancerF5ConfigArgsDict",
    "VMwareClusterLoadBalancerManualLbConfigArgs",
    "VMwareClusterLoadBalancerManualLbConfigArgsDict",
    "VMwareClusterLoadBalancerMetalLbConfigArgs",
    "VMwareClusterLoadBalancerMetalLbConfigArgsDict",
    ...,
    ...,
    "VMwareClusterLoadBalancerVipConfigArgs",
    "VMwareClusterLoadBalancerVipConfigArgsDict",
    "VMwareClusterNetworkConfigArgs",
    "VMwareClusterNetworkConfigArgsDict",
    "VMwareClusterNetworkConfigControlPlaneV2ConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "VMwareClusterNetworkConfigDhcpIpConfigArgs",
    "VMwareClusterNetworkConfigDhcpIpConfigArgsDict",
    "VMwareClusterNetworkConfigHostConfigArgs",
    "VMwareClusterNetworkConfigHostConfigArgsDict",
    "VMwareClusterNetworkConfigStaticIpConfigArgs",
    "VMwareClusterNetworkConfigStaticIpConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "VMwareClusterStatusArgs",
    "VMwareClusterStatusArgsDict",
    "VMwareClusterStatusConditionArgs",
    "VMwareClusterStatusConditionArgsDict",
    "VMwareClusterStorageArgs",
    "VMwareClusterStorageArgsDict",
    "VMwareClusterUpgradePolicyArgs",
    "VMwareClusterUpgradePolicyArgsDict",
    "VMwareClusterValidationCheckArgs",
    "VMwareClusterValidationCheckArgsDict",
    "VMwareClusterValidationCheckStatusArgs",
    "VMwareClusterValidationCheckStatusArgsDict",
    "VMwareClusterValidationCheckStatusResultArgs",
    "VMwareClusterValidationCheckStatusResultArgsDict",
    "VMwareClusterVcenterArgs",
    "VMwareClusterVcenterArgsDict",
    "VMwareNodePoolConfigArgs",
    "VMwareNodePoolConfigArgsDict",
    "VMwareNodePoolConfigTaintArgs",
    "VMwareNodePoolConfigTaintArgsDict",
    "VMwareNodePoolConfigVsphereConfigArgs",
    "VMwareNodePoolConfigVsphereConfigArgsDict",
    "VMwareNodePoolConfigVsphereConfigTagArgs",
    "VMwareNodePoolConfigVsphereConfigTagArgsDict",
    "VMwareNodePoolNodePoolAutoscalingArgs",
    "VMwareNodePoolNodePoolAutoscalingArgsDict",
    "VMwareNodePoolStatusArgs",
    "VMwareNodePoolStatusArgsDict",
    "VMwareNodePoolStatusConditionArgs",
    "VMwareNodePoolStatusConditionArgsDict",
    "VmwareAdminClusterAddonNodeArgs",
    "VmwareAdminClusterAddonNodeArgsDict",
    "VmwareAdminClusterAddonNodeAutoResizeConfigArgs",
    ...,
    "VmwareAdminClusterAntiAffinityGroupsArgs",
    "VmwareAdminClusterAntiAffinityGroupsArgsDict",
    "VmwareAdminClusterAuthorizationArgs",
    "VmwareAdminClusterAuthorizationArgsDict",
    "VmwareAdminClusterAuthorizationViewerUserArgs",
    "VmwareAdminClusterAuthorizationViewerUserArgsDict",
    "VmwareAdminClusterAutoRepairConfigArgs",
    "VmwareAdminClusterAutoRepairConfigArgsDict",
    "VmwareAdminClusterControlPlaneNodeArgs",
    "VmwareAdminClusterControlPlaneNodeArgsDict",
    "VmwareAdminClusterFleetArgs",
    "VmwareAdminClusterFleetArgsDict",
    "VmwareAdminClusterLoadBalancerArgs",
    "VmwareAdminClusterLoadBalancerArgsDict",
    "VmwareAdminClusterLoadBalancerF5ConfigArgs",
    "VmwareAdminClusterLoadBalancerF5ConfigArgsDict",
    "VmwareAdminClusterLoadBalancerManualLbConfigArgs",
    ...,
    "VmwareAdminClusterLoadBalancerMetalLbConfigArgs",
    ...,
    "VmwareAdminClusterLoadBalancerVipConfigArgs",
    "VmwareAdminClusterLoadBalancerVipConfigArgsDict",
    "VmwareAdminClusterNetworkConfigArgs",
    "VmwareAdminClusterNetworkConfigArgsDict",
    "VmwareAdminClusterNetworkConfigDhcpIpConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "VmwareAdminClusterNetworkConfigHostConfigArgs",
    "VmwareAdminClusterNetworkConfigHostConfigArgsDict",
    "VmwareAdminClusterNetworkConfigStaticIpConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "VmwareAdminClusterPlatformConfigArgs",
    "VmwareAdminClusterPlatformConfigArgsDict",
    "VmwareAdminClusterPlatformConfigBundleArgs",
    "VmwareAdminClusterPlatformConfigBundleArgsDict",
    "VmwareAdminClusterPlatformConfigBundleStatusArgs",
    ...,
    ...,
    ...,
    "VmwareAdminClusterPlatformConfigStatusArgs",
    "VmwareAdminClusterPlatformConfigStatusArgsDict",
    ...,
    ...,
    "VmwareAdminClusterPrivateRegistryConfigArgs",
    "VmwareAdminClusterPrivateRegistryConfigArgsDict",
    "VmwareAdminClusterProxyArgs",
    "VmwareAdminClusterProxyArgsDict",
    "VmwareAdminClusterStatusArgs",
    "VmwareAdminClusterStatusArgsDict",
    "VmwareAdminClusterStatusConditionArgs",
    "VmwareAdminClusterStatusConditionArgsDict",
    "VmwareAdminClusterVcenterArgs",
    "VmwareAdminClusterVcenterArgsDict",
]

class BareMetalAdminClusterClusterOperationsArgsDict(TypedDict):
    enable_application_logs: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BareMetalAdminClusterClusterOperationsArgs:
    def __init__(
        __self__,
        *,
        enable_application_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableApplicationLogs")
    def enable_application_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_application_logs.setter
    def enable_application_logs(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class BareMetalAdminClusterControlPlaneArgsDict(TypedDict):
    control_plane_node_pool_config: pulumi.Input[
        BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigArgsDict
    ]
    api_server_args: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[BareMetalAdminClusterControlPlaneApiServerArgArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class BareMetalAdminClusterControlPlaneArgs:
    def __init__(
        __self__,
        *,
        control_plane_node_pool_config: pulumi.Input[
            BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigArgs
        ],
        api_server_args: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[BareMetalAdminClusterControlPlaneApiServerArgArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodePoolConfig")
    def control_plane_node_pool_config(
        self,
    ) -> pulumi.Input[
        BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigArgs
    ]: ...
    @control_plane_node_pool_config.setter
    def control_plane_node_pool_config(
        self,
        value: pulumi.Input[
            BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="apiServerArgs")
    def api_server_args(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalAdminClusterControlPlaneApiServerArgArgs]]
        ]
    ]: ...
    @api_server_args.setter
    def api_server_args(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[BareMetalAdminClusterControlPlaneApiServerArgArgs]
                ]
            ]
        ],
    ): ...

class BareMetalAdminClusterControlPlaneApiServerArgArgsDict(TypedDict):
    argument: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class BareMetalAdminClusterControlPlaneApiServerArgArgs:
    def __init__(
        __self__,
        *,
        argument: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def argument(self) -> pulumi.Input[_builtins.str]: ...
    @argument.setter
    def argument(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigArgsDict(TypedDict):
    node_pool_config: pulumi.Input[
        BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgsDict
    ]

@pulumi.input_type
class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        node_pool_config: pulumi.Input[
            BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(
        self,
    ) -> pulumi.Input[
        BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgs
    ]: ...
    @node_pool_config.setter
    def node_pool_config(
        self,
        value: pulumi.Input[
            BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgs
        ],
    ): ...

class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgsDict
                ]
            ]
        ]
    ]
    operating_system: NotRequired[pulumi.Input[_builtins.str]]
    taints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgs
                    ]
                ]
            ]
        ] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        taints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgs
                ]
            ]
        ]
    ]: ...
    @node_configs.setter
    def node_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgs
                ]
            ]
        ]
    ]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgs
                    ]
                ]
            ]
        ],
    ): ...

class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_ip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_ip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_ip.setter
    def node_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgsDict(
    TypedDict
):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgs:
    def __init__(
        __self__,
        *,
        effect: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalAdminClusterFleetArgsDict(TypedDict):
    membership: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterFleetArgs:
    def __init__(
        __self__, *, membership: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalAdminClusterLoadBalancerArgsDict(TypedDict):
    port_config: pulumi.Input[BareMetalAdminClusterLoadBalancerPortConfigArgsDict]
    vip_config: pulumi.Input[BareMetalAdminClusterLoadBalancerVipConfigArgsDict]
    bgp_lb_config: NotRequired[
        pulumi.Input[BareMetalAdminClusterLoadBalancerBgpLbConfigArgsDict]
    ]
    manual_lb_config: NotRequired[
        pulumi.Input[BareMetalAdminClusterLoadBalancerManualLbConfigArgsDict]
    ]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerArgs:
    def __init__(
        __self__,
        *,
        port_config: pulumi.Input[BareMetalAdminClusterLoadBalancerPortConfigArgs],
        vip_config: pulumi.Input[BareMetalAdminClusterLoadBalancerVipConfigArgs],
        bgp_lb_config: Optional[
            pulumi.Input[BareMetalAdminClusterLoadBalancerBgpLbConfigArgs]
        ] = ...,
        manual_lb_config: Optional[
            pulumi.Input[BareMetalAdminClusterLoadBalancerManualLbConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portConfig")
    def port_config(
        self,
    ) -> pulumi.Input[BareMetalAdminClusterLoadBalancerPortConfigArgs]: ...
    @port_config.setter
    def port_config(
        self, value: pulumi.Input[BareMetalAdminClusterLoadBalancerPortConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vipConfig")
    def vip_config(
        self,
    ) -> pulumi.Input[BareMetalAdminClusterLoadBalancerVipConfigArgs]: ...
    @vip_config.setter
    def vip_config(
        self, value: pulumi.Input[BareMetalAdminClusterLoadBalancerVipConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bgpLbConfig")
    def bgp_lb_config(
        self,
    ) -> Optional[pulumi.Input[BareMetalAdminClusterLoadBalancerBgpLbConfigArgs]]: ...
    @bgp_lb_config.setter
    def bgp_lb_config(
        self,
        value: Optional[pulumi.Input[BareMetalAdminClusterLoadBalancerBgpLbConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manualLbConfig")
    def manual_lb_config(
        self,
    ) -> Optional[
        pulumi.Input[BareMetalAdminClusterLoadBalancerManualLbConfigArgs]
    ]: ...
    @manual_lb_config.setter
    def manual_lb_config(
        self,
        value: Optional[
            pulumi.Input[BareMetalAdminClusterLoadBalancerManualLbConfigArgs]
        ],
    ): ...

class BareMetalAdminClusterLoadBalancerBgpLbConfigArgsDict(TypedDict):
    address_pools: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterLoadBalancerBgpLbConfigAddressPoolArgsDict
                ]
            ]
        ]
    ]
    asn: NotRequired[pulumi.Input[_builtins.int]]
    bgp_peer_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterLoadBalancerBgpLbConfigBgpPeerConfigArgsDict
                ]
            ]
        ]
    ]
    load_balancer_node_pool_config: NotRequired[
        pulumi.Input[
            BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgsDict
        ]
    ]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigArgs:
    def __init__(
        __self__,
        *,
        address_pools: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterLoadBalancerBgpLbConfigAddressPoolArgs
                    ]
                ]
            ]
        ] = ...,
        asn: Optional[pulumi.Input[_builtins.int]] = ...,
        bgp_peer_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterLoadBalancerBgpLbConfigBgpPeerConfigArgs
                    ]
                ]
            ]
        ] = ...,
        load_balancer_node_pool_config: Optional[
            pulumi.Input[
                BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressPools")
    def address_pools(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterLoadBalancerBgpLbConfigAddressPoolArgs
                ]
            ]
        ]
    ]: ...
    @address_pools.setter
    def address_pools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterLoadBalancerBgpLbConfigAddressPoolArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @asn.setter
    def asn(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpPeerConfigs")
    def bgp_peer_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterLoadBalancerBgpLbConfigBgpPeerConfigArgs
                ]
            ]
        ]
    ]: ...
    @bgp_peer_configs.setter
    def bgp_peer_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterLoadBalancerBgpLbConfigBgpPeerConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerNodePoolConfig")
    def load_balancer_node_pool_config(
        self,
    ) -> Optional[
        pulumi.Input[
            BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgs
        ]
    ]: ...
    @load_balancer_node_pool_config.setter
    def load_balancer_node_pool_config(
        self,
        value: Optional[
            pulumi.Input[
                BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgs
            ]
        ],
    ): ...

class BareMetalAdminClusterLoadBalancerBgpLbConfigAddressPoolArgsDict(TypedDict):
    addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    avoid_buggy_ips: NotRequired[pulumi.Input[_builtins.bool]]
    manual_assign: NotRequired[pulumi.Input[_builtins.bool]]
    pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigAddressPoolArgs:
    def __init__(
        __self__,
        *,
        addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        avoid_buggy_ips: Optional[pulumi.Input[_builtins.bool]] = ...,
        manual_assign: Optional[pulumi.Input[_builtins.bool]] = ...,
        pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @addresses.setter
    def addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="avoidBuggyIps")
    def avoid_buggy_ips(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @avoid_buggy_ips.setter
    def avoid_buggy_ips(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="manualAssign")
    def manual_assign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manual_assign.setter
    def manual_assign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pool.setter
    def pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalAdminClusterLoadBalancerBgpLbConfigBgpPeerConfigArgsDict(TypedDict):
    asn: NotRequired[pulumi.Input[_builtins.int]]
    control_plane_nodes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigBgpPeerConfigArgs:
    def __init__(
        __self__,
        *,
        asn: Optional[pulumi.Input[_builtins.int]] = ...,
        control_plane_nodes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @asn.setter
    def asn(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodes")
    def control_plane_nodes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @control_plane_nodes.setter
    def control_plane_nodes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgsDict(
    TypedDict
):
    node_pool_config: NotRequired[
        pulumi.Input[
            BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgsDict
        ]
    ]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        node_pool_config: Optional[
            pulumi.Input[
                BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(
        self,
    ) -> Optional[
        pulumi.Input[
            BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs
        ]
    ]: ...
    @node_pool_config.setter
    def node_pool_config(
        self,
        value: Optional[
            pulumi.Input[
                BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs
            ]
        ],
    ): ...

class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgsDict(
    TypedDict
):
    kubelet_config: NotRequired[
        pulumi.Input[
            BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgsDict
        ]
    ]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgsDict
                ]
            ]
        ]
    ]
    operating_system: NotRequired[pulumi.Input[_builtins.str]]
    taints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        kubelet_config: Optional[
            pulumi.Input[
                BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgs
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs
                    ]
                ]
            ]
        ] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        taints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(
        self,
    ) -> Optional[
        pulumi.Input[
            BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgs
        ]
    ]: ...
    @kubelet_config.setter
    def kubelet_config(
        self,
        value: Optional[
            pulumi.Input[
                BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs
                ]
            ]
        ]
    ]: ...
    @node_configs.setter
    def node_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs
                ]
            ]
        ]
    ]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs
                    ]
                ]
            ]
        ],
    ): ...

class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgsDict(
    TypedDict
):
    registry_burst: NotRequired[pulumi.Input[_builtins.int]]
    registry_pull_qps: NotRequired[pulumi.Input[_builtins.int]]
    serialize_image_pulls_disabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgs:
    def __init__(
        __self__,
        *,
        registry_burst: Optional[pulumi.Input[_builtins.int]] = ...,
        registry_pull_qps: Optional[pulumi.Input[_builtins.int]] = ...,
        serialize_image_pulls_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registryBurst")
    def registry_burst(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @registry_burst.setter
    def registry_burst(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="registryPullQps")
    def registry_pull_qps(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @registry_pull_qps.setter
    def registry_pull_qps(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serializeImagePullsDisabled")
    def serialize_image_pulls_disabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @serialize_image_pulls_disabled.setter
    def serialize_image_pulls_disabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_ip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_ip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_ip.setter
    def node_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgsDict(
    TypedDict
):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs:
    def __init__(
        __self__,
        *,
        effect: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalAdminClusterLoadBalancerManualLbConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerManualLbConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class BareMetalAdminClusterLoadBalancerPortConfigArgsDict(TypedDict):
    control_plane_load_balancer_port: pulumi.Input[_builtins.int]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerPortConfigArgs:
    def __init__(
        __self__, *, control_plane_load_balancer_port: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneLoadBalancerPort")
    def control_plane_load_balancer_port(self) -> pulumi.Input[_builtins.int]: ...
    @control_plane_load_balancer_port.setter
    def control_plane_load_balancer_port(self, value: pulumi.Input[_builtins.int]): ...

class BareMetalAdminClusterLoadBalancerVipConfigArgsDict(TypedDict):
    control_plane_vip: pulumi.Input[_builtins.str]

@pulumi.input_type
class BareMetalAdminClusterLoadBalancerVipConfigArgs:
    def __init__(
        __self__, *, control_plane_vip: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneVip")
    def control_plane_vip(self) -> pulumi.Input[_builtins.str]: ...
    @control_plane_vip.setter
    def control_plane_vip(self, value: pulumi.Input[_builtins.str]): ...

class BareMetalAdminClusterMaintenanceConfigArgsDict(TypedDict):
    maintenance_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class BareMetalAdminClusterMaintenanceConfigArgs:
    def __init__(
        __self__,
        *,
        maintenance_address_cidr_blocks: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceAddressCidrBlocks")
    def maintenance_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @maintenance_address_cidr_blocks.setter
    def maintenance_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class BareMetalAdminClusterNetworkConfigArgsDict(TypedDict):
    advanced_networking: NotRequired[pulumi.Input[_builtins.bool]]
    island_mode_cidr: NotRequired[
        pulumi.Input[BareMetalAdminClusterNetworkConfigIslandModeCidrArgsDict]
    ]
    multiple_network_interfaces_config: NotRequired[
        pulumi.Input[
            BareMetalAdminClusterNetworkConfigMultipleNetworkInterfacesConfigArgsDict
        ]
    ]

@pulumi.input_type
class BareMetalAdminClusterNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        advanced_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
        island_mode_cidr: Optional[
            pulumi.Input[BareMetalAdminClusterNetworkConfigIslandModeCidrArgs]
        ] = ...,
        multiple_network_interfaces_config: Optional[
            pulumi.Input[
                BareMetalAdminClusterNetworkConfigMultipleNetworkInterfacesConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedNetworking")
    def advanced_networking(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @advanced_networking.setter
    def advanced_networking(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="islandModeCidr")
    def island_mode_cidr(
        self,
    ) -> Optional[
        pulumi.Input[BareMetalAdminClusterNetworkConfigIslandModeCidrArgs]
    ]: ...
    @island_mode_cidr.setter
    def island_mode_cidr(
        self,
        value: Optional[
            pulumi.Input[BareMetalAdminClusterNetworkConfigIslandModeCidrArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multipleNetworkInterfacesConfig")
    def multiple_network_interfaces_config(
        self,
    ) -> Optional[
        pulumi.Input[
            BareMetalAdminClusterNetworkConfigMultipleNetworkInterfacesConfigArgs
        ]
    ]: ...
    @multiple_network_interfaces_config.setter
    def multiple_network_interfaces_config(
        self,
        value: Optional[
            pulumi.Input[
                BareMetalAdminClusterNetworkConfigMultipleNetworkInterfacesConfigArgs
            ]
        ],
    ): ...

class BareMetalAdminClusterNetworkConfigIslandModeCidrArgsDict(TypedDict):
    pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    service_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class BareMetalAdminClusterNetworkConfigIslandModeCidrArgs:
    def __init__(
        __self__,
        *,
        pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        service_address_cidr_blocks: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @pod_address_cidr_blocks.setter
    def pod_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @service_address_cidr_blocks.setter
    def service_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class BareMetalAdminClusterNetworkConfigMultipleNetworkInterfacesConfigArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BareMetalAdminClusterNetworkConfigMultipleNetworkInterfacesConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class BareMetalAdminClusterNodeAccessConfigArgsDict(TypedDict):
    login_user: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterNodeAccessConfigArgs:
    def __init__(
        __self__, *, login_user: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginUser")
    def login_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @login_user.setter
    def login_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalAdminClusterNodeConfigArgsDict(TypedDict):
    max_pods_per_node: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BareMetalAdminClusterNodeConfigArgs:
    def __init__(
        __self__, *, max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods_per_node.setter
    def max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class BareMetalAdminClusterProxyArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    no_proxies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BareMetalAdminClusterProxyArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        no_proxies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="noProxies")
    def no_proxies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @no_proxies.setter
    def no_proxies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BareMetalAdminClusterSecurityConfigArgsDict(TypedDict):
    authorization: NotRequired[
        pulumi.Input[BareMetalAdminClusterSecurityConfigAuthorizationArgsDict]
    ]

@pulumi.input_type
class BareMetalAdminClusterSecurityConfigArgs:
    def __init__(
        __self__,
        *,
        authorization: Optional[
            pulumi.Input[BareMetalAdminClusterSecurityConfigAuthorizationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authorization(
        self,
    ) -> Optional[
        pulumi.Input[BareMetalAdminClusterSecurityConfigAuthorizationArgs]
    ]: ...
    @authorization.setter
    def authorization(
        self,
        value: Optional[
            pulumi.Input[BareMetalAdminClusterSecurityConfigAuthorizationArgs]
        ],
    ): ...

class BareMetalAdminClusterSecurityConfigAuthorizationArgsDict(TypedDict):
    admin_users: pulumi.Input[
        Sequence[
            pulumi.Input[
                BareMetalAdminClusterSecurityConfigAuthorizationAdminUserArgsDict
            ]
        ]
    ]

@pulumi.input_type
class BareMetalAdminClusterSecurityConfigAuthorizationArgs:
    def __init__(
        __self__,
        *,
        admin_users: pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterSecurityConfigAuthorizationAdminUserArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[BareMetalAdminClusterSecurityConfigAuthorizationAdminUserArgs]
        ]
    ]: ...
    @admin_users.setter
    def admin_users(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalAdminClusterSecurityConfigAuthorizationAdminUserArgs
                ]
            ]
        ],
    ): ...

class BareMetalAdminClusterSecurityConfigAuthorizationAdminUserArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]

@pulumi.input_type
class BareMetalAdminClusterSecurityConfigAuthorizationAdminUserArgs:
    def __init__(__self__, *, username: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class BareMetalAdminClusterStatusArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalAdminClusterStatusConditionArgsDict]]
        ]
    ]
    error_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterStatusArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalAdminClusterStatusConditionArgs]]
            ]
        ] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BareMetalAdminClusterStatusConditionArgs]]]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalAdminClusterStatusConditionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalAdminClusterStatusConditionArgsDict(TypedDict):
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterStatusConditionArgs:
    def __init__(
        __self__,
        *,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalAdminClusterStorageArgsDict(TypedDict):
    lvp_node_mounts_config: pulumi.Input[
        BareMetalAdminClusterStorageLvpNodeMountsConfigArgsDict
    ]
    lvp_share_config: pulumi.Input[BareMetalAdminClusterStorageLvpShareConfigArgsDict]

@pulumi.input_type
class BareMetalAdminClusterStorageArgs:
    def __init__(
        __self__,
        *,
        lvp_node_mounts_config: pulumi.Input[
            BareMetalAdminClusterStorageLvpNodeMountsConfigArgs
        ],
        lvp_share_config: pulumi.Input[BareMetalAdminClusterStorageLvpShareConfigArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lvpNodeMountsConfig")
    def lvp_node_mounts_config(
        self,
    ) -> pulumi.Input[BareMetalAdminClusterStorageLvpNodeMountsConfigArgs]: ...
    @lvp_node_mounts_config.setter
    def lvp_node_mounts_config(
        self, value: pulumi.Input[BareMetalAdminClusterStorageLvpNodeMountsConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lvpShareConfig")
    def lvp_share_config(
        self,
    ) -> pulumi.Input[BareMetalAdminClusterStorageLvpShareConfigArgs]: ...
    @lvp_share_config.setter
    def lvp_share_config(
        self, value: pulumi.Input[BareMetalAdminClusterStorageLvpShareConfigArgs]
    ): ...

class BareMetalAdminClusterStorageLvpNodeMountsConfigArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    storage_class: pulumi.Input[_builtins.str]

@pulumi.input_type
class BareMetalAdminClusterStorageLvpNodeMountsConfigArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        storage_class: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]: ...
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): ...

class BareMetalAdminClusterStorageLvpShareConfigArgsDict(TypedDict):
    lvp_config: pulumi.Input[
        BareMetalAdminClusterStorageLvpShareConfigLvpConfigArgsDict
    ]
    shared_path_pv_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BareMetalAdminClusterStorageLvpShareConfigArgs:
    def __init__(
        __self__,
        *,
        lvp_config: pulumi.Input[
            BareMetalAdminClusterStorageLvpShareConfigLvpConfigArgs
        ],
        shared_path_pv_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lvpConfig")
    def lvp_config(
        self,
    ) -> pulumi.Input[BareMetalAdminClusterStorageLvpShareConfigLvpConfigArgs]: ...
    @lvp_config.setter
    def lvp_config(
        self,
        value: pulumi.Input[BareMetalAdminClusterStorageLvpShareConfigLvpConfigArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedPathPvCount")
    def shared_path_pv_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shared_path_pv_count.setter
    def shared_path_pv_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class BareMetalAdminClusterStorageLvpShareConfigLvpConfigArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    storage_class: pulumi.Input[_builtins.str]

@pulumi.input_type
class BareMetalAdminClusterStorageLvpShareConfigLvpConfigArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        storage_class: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]: ...
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): ...

class BareMetalAdminClusterValidationCheckArgsDict(TypedDict):
    options: NotRequired[pulumi.Input[_builtins.str]]
    scenario: NotRequired[pulumi.Input[_builtins.str]]
    statuses: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalAdminClusterValidationCheckStatusArgsDict]]
        ]
    ]

@pulumi.input_type
class BareMetalAdminClusterValidationCheckArgs:
    def __init__(
        __self__,
        *,
        options: Optional[pulumi.Input[_builtins.str]] = ...,
        scenario: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalAdminClusterValidationCheckStatusArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @options.setter
    def options(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scenario(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scenario.setter
    def scenario(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalAdminClusterValidationCheckStatusArgs]]
        ]
    ]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalAdminClusterValidationCheckStatusArgs]]
            ]
        ],
    ): ...

class BareMetalAdminClusterValidationCheckStatusArgsDict(TypedDict):
    results: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[BareMetalAdminClusterValidationCheckStatusResultArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class BareMetalAdminClusterValidationCheckStatusArgs:
    def __init__(
        __self__,
        *,
        results: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[BareMetalAdminClusterValidationCheckStatusResultArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def results(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalAdminClusterValidationCheckStatusResultArgs]]
        ]
    ]: ...
    @results.setter
    def results(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[BareMetalAdminClusterValidationCheckStatusResultArgs]
                ]
            ]
        ],
    ): ...

class BareMetalAdminClusterValidationCheckStatusResultArgsDict(TypedDict):
    category: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    details: NotRequired[pulumi.Input[_builtins.str]]
    options: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalAdminClusterValidationCheckStatusResultArgs:
    def __init__(
        __self__,
        *,
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        details: Optional[pulumi.Input[_builtins.str]] = ...,
        options: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @options.setter
    def options(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterBinaryAuthorizationArgsDict(TypedDict):
    evaluation_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterBinaryAuthorizationArgs:
    def __init__(
        __self__, *, evaluation_mode: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evaluation_mode.setter
    def evaluation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterClusterOperationsArgsDict(TypedDict):
    enable_application_logs: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BareMetalClusterClusterOperationsArgs:
    def __init__(
        __self__,
        *,
        enable_application_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableApplicationLogs")
    def enable_application_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_application_logs.setter
    def enable_application_logs(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class BareMetalClusterControlPlaneArgsDict(TypedDict):
    control_plane_node_pool_config: pulumi.Input[
        BareMetalClusterControlPlaneControlPlaneNodePoolConfigArgsDict
    ]
    api_server_args: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalClusterControlPlaneApiServerArgArgsDict]]
        ]
    ]

@pulumi.input_type
class BareMetalClusterControlPlaneArgs:
    def __init__(
        __self__,
        *,
        control_plane_node_pool_config: pulumi.Input[
            BareMetalClusterControlPlaneControlPlaneNodePoolConfigArgs
        ],
        api_server_args: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalClusterControlPlaneApiServerArgArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodePoolConfig")
    def control_plane_node_pool_config(
        self,
    ) -> pulumi.Input[BareMetalClusterControlPlaneControlPlaneNodePoolConfigArgs]: ...
    @control_plane_node_pool_config.setter
    def control_plane_node_pool_config(
        self,
        value: pulumi.Input[BareMetalClusterControlPlaneControlPlaneNodePoolConfigArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="apiServerArgs")
    def api_server_args(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalClusterControlPlaneApiServerArgArgs]]
        ]
    ]: ...
    @api_server_args.setter
    def api_server_args(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalClusterControlPlaneApiServerArgArgs]]
            ]
        ],
    ): ...

class BareMetalClusterControlPlaneApiServerArgArgsDict(TypedDict):
    argument: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class BareMetalClusterControlPlaneApiServerArgArgs:
    def __init__(
        __self__,
        *,
        argument: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def argument(self) -> pulumi.Input[_builtins.str]: ...
    @argument.setter
    def argument(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class BareMetalClusterControlPlaneControlPlaneNodePoolConfigArgsDict(TypedDict):
    node_pool_config: pulumi.Input[
        BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgsDict
    ]

@pulumi.input_type
class BareMetalClusterControlPlaneControlPlaneNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        node_pool_config: pulumi.Input[
            BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(
        self,
    ) -> pulumi.Input[
        BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgs
    ]: ...
    @node_pool_config.setter
    def node_pool_config(
        self,
        value: pulumi.Input[
            BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgs
        ],
    ): ...

class BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgsDict
                ]
            ]
        ]
    ]
    operating_system: NotRequired[pulumi.Input[_builtins.str]]
    taints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgs
                    ]
                ]
            ]
        ] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        taints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgs
                ]
            ]
        ]
    ]: ...
    @node_configs.setter
    def node_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgs
                ]
            ]
        ]
    ]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgs
                    ]
                ]
            ]
        ],
    ): ...

class BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_ip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfigArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_ip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_ip.setter
    def node_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgsDict(
    TypedDict
):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaintArgs:
    def __init__(
        __self__,
        *,
        effect: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterFleetArgsDict(TypedDict):
    membership: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterFleetArgs:
    def __init__(
        __self__, *, membership: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterLoadBalancerArgsDict(TypedDict):
    port_config: pulumi.Input[BareMetalClusterLoadBalancerPortConfigArgsDict]
    vip_config: pulumi.Input[BareMetalClusterLoadBalancerVipConfigArgsDict]
    bgp_lb_config: NotRequired[
        pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigArgsDict]
    ]
    manual_lb_config: NotRequired[
        pulumi.Input[BareMetalClusterLoadBalancerManualLbConfigArgsDict]
    ]
    metal_lb_config: NotRequired[
        pulumi.Input[BareMetalClusterLoadBalancerMetalLbConfigArgsDict]
    ]

@pulumi.input_type
class BareMetalClusterLoadBalancerArgs:
    def __init__(
        __self__,
        *,
        port_config: pulumi.Input[BareMetalClusterLoadBalancerPortConfigArgs],
        vip_config: pulumi.Input[BareMetalClusterLoadBalancerVipConfigArgs],
        bgp_lb_config: Optional[
            pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigArgs]
        ] = ...,
        manual_lb_config: Optional[
            pulumi.Input[BareMetalClusterLoadBalancerManualLbConfigArgs]
        ] = ...,
        metal_lb_config: Optional[
            pulumi.Input[BareMetalClusterLoadBalancerMetalLbConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portConfig")
    def port_config(
        self,
    ) -> pulumi.Input[BareMetalClusterLoadBalancerPortConfigArgs]: ...
    @port_config.setter
    def port_config(
        self, value: pulumi.Input[BareMetalClusterLoadBalancerPortConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vipConfig")
    def vip_config(self) -> pulumi.Input[BareMetalClusterLoadBalancerVipConfigArgs]: ...
    @vip_config.setter
    def vip_config(
        self, value: pulumi.Input[BareMetalClusterLoadBalancerVipConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bgpLbConfig")
    def bgp_lb_config(
        self,
    ) -> Optional[pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigArgs]]: ...
    @bgp_lb_config.setter
    def bgp_lb_config(
        self, value: Optional[pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="manualLbConfig")
    def manual_lb_config(
        self,
    ) -> Optional[pulumi.Input[BareMetalClusterLoadBalancerManualLbConfigArgs]]: ...
    @manual_lb_config.setter
    def manual_lb_config(
        self,
        value: Optional[pulumi.Input[BareMetalClusterLoadBalancerManualLbConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="metalLbConfig")
    def metal_lb_config(
        self,
    ) -> Optional[pulumi.Input[BareMetalClusterLoadBalancerMetalLbConfigArgs]]: ...
    @metal_lb_config.setter
    def metal_lb_config(
        self,
        value: Optional[pulumi.Input[BareMetalClusterLoadBalancerMetalLbConfigArgs]],
    ): ...

class BareMetalClusterLoadBalancerBgpLbConfigArgsDict(TypedDict):
    address_pools: pulumi.Input[
        Sequence[
            pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigAddressPoolArgsDict]
        ]
    ]
    asn: pulumi.Input[_builtins.int]
    bgp_peer_configs: pulumi.Input[
        Sequence[
            pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigBgpPeerConfigArgsDict]
        ]
    ]
    load_balancer_node_pool_config: NotRequired[
        pulumi.Input[
            BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgsDict
        ]
    ]

@pulumi.input_type
class BareMetalClusterLoadBalancerBgpLbConfigArgs:
    def __init__(
        __self__,
        *,
        address_pools: pulumi.Input[
            Sequence[
                pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigAddressPoolArgs]
            ]
        ],
        asn: pulumi.Input[_builtins.int],
        bgp_peer_configs: pulumi.Input[
            Sequence[
                pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigBgpPeerConfigArgs]
            ]
        ],
        load_balancer_node_pool_config: Optional[
            pulumi.Input[
                BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressPools")
    def address_pools(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigAddressPoolArgs]]
    ]: ...
    @address_pools.setter
    def address_pools(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigAddressPoolArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def asn(self) -> pulumi.Input[_builtins.int]: ...
    @asn.setter
    def asn(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="bgpPeerConfigs")
    def bgp_peer_configs(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigBgpPeerConfigArgs]]
    ]: ...
    @bgp_peer_configs.setter
    def bgp_peer_configs(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[BareMetalClusterLoadBalancerBgpLbConfigBgpPeerConfigArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerNodePoolConfig")
    def load_balancer_node_pool_config(
        self,
    ) -> Optional[
        pulumi.Input[
            BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgs
        ]
    ]: ...
    @load_balancer_node_pool_config.setter
    def load_balancer_node_pool_config(
        self,
        value: Optional[
            pulumi.Input[
                BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgs
            ]
        ],
    ): ...

class BareMetalClusterLoadBalancerBgpLbConfigAddressPoolArgsDict(TypedDict):
    addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    pool: pulumi.Input[_builtins.str]
    avoid_buggy_ips: NotRequired[pulumi.Input[_builtins.bool]]
    manual_assign: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BareMetalClusterLoadBalancerBgpLbConfigAddressPoolArgs:
    def __init__(
        __self__,
        *,
        addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        pool: pulumi.Input[_builtins.str],
        avoid_buggy_ips: Optional[pulumi.Input[_builtins.bool]] = ...,
        manual_assign: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @addresses.setter
    def addresses(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def pool(self) -> pulumi.Input[_builtins.str]: ...
    @pool.setter
    def pool(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="avoidBuggyIps")
    def avoid_buggy_ips(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @avoid_buggy_ips.setter
    def avoid_buggy_ips(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="manualAssign")
    def manual_assign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manual_assign.setter
    def manual_assign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class BareMetalClusterLoadBalancerBgpLbConfigBgpPeerConfigArgsDict(TypedDict):
    asn: pulumi.Input[_builtins.int]
    ip_address: pulumi.Input[_builtins.str]
    control_plane_nodes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class BareMetalClusterLoadBalancerBgpLbConfigBgpPeerConfigArgs:
    def __init__(
        __self__,
        *,
        asn: pulumi.Input[_builtins.int],
        ip_address: pulumi.Input[_builtins.str],
        control_plane_nodes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def asn(self) -> pulumi.Input[_builtins.int]: ...
    @asn.setter
    def asn(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[_builtins.str]: ...
    @ip_address.setter
    def ip_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodes")
    def control_plane_nodes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @control_plane_nodes.setter
    def control_plane_nodes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgsDict(
    TypedDict
):
    node_pool_config: NotRequired[
        pulumi.Input[
            BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgsDict
        ]
    ]

@pulumi.input_type
class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        node_pool_config: Optional[
            pulumi.Input[
                BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(
        self,
    ) -> Optional[
        pulumi.Input[
            BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs
        ]
    ]: ...
    @node_pool_config.setter
    def node_pool_config(
        self,
        value: Optional[
            pulumi.Input[
                BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs
            ]
        ],
    ): ...

class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgsDict(
    TypedDict
):
    kubelet_config: NotRequired[
        pulumi.Input[
            BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgsDict
        ]
    ]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgsDict
                ]
            ]
        ]
    ]
    operating_system: NotRequired[pulumi.Input[_builtins.str]]
    taints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        kubelet_config: Optional[
            pulumi.Input[
                BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgs
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs
                    ]
                ]
            ]
        ] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        taints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(
        self,
    ) -> Optional[
        pulumi.Input[
            BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgs
        ]
    ]: ...
    @kubelet_config.setter
    def kubelet_config(
        self,
        value: Optional[
            pulumi.Input[
                BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs
                ]
            ]
        ]
    ]: ...
    @node_configs.setter
    def node_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs
                ]
            ]
        ]
    ]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs
                    ]
                ]
            ]
        ],
    ): ...

class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgsDict(
    TypedDict
):
    registry_burst: NotRequired[pulumi.Input[_builtins.int]]
    registry_pull_qps: NotRequired[pulumi.Input[_builtins.int]]
    serialize_image_pulls_disabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfigArgs:
    def __init__(
        __self__,
        *,
        registry_burst: Optional[pulumi.Input[_builtins.int]] = ...,
        registry_pull_qps: Optional[pulumi.Input[_builtins.int]] = ...,
        serialize_image_pulls_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registryBurst")
    def registry_burst(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @registry_burst.setter
    def registry_burst(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="registryPullQps")
    def registry_pull_qps(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @registry_pull_qps.setter
    def registry_pull_qps(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serializeImagePullsDisabled")
    def serialize_image_pulls_disabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @serialize_image_pulls_disabled.setter
    def serialize_image_pulls_disabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_ip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_ip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_ip.setter
    def node_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgsDict(
    TypedDict
):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs:
    def __init__(
        __self__,
        *,
        effect: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterLoadBalancerManualLbConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class BareMetalClusterLoadBalancerManualLbConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class BareMetalClusterLoadBalancerMetalLbConfigArgsDict(TypedDict):
    address_pools: pulumi.Input[
        Sequence[
            pulumi.Input[BareMetalClusterLoadBalancerMetalLbConfigAddressPoolArgsDict]
        ]
    ]
    load_balancer_node_pool_config: NotRequired[
        pulumi.Input[
            BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigArgsDict
        ]
    ]

@pulumi.input_type
class BareMetalClusterLoadBalancerMetalLbConfigArgs:
    def __init__(
        __self__,
        *,
        address_pools: pulumi.Input[
            Sequence[
                pulumi.Input[BareMetalClusterLoadBalancerMetalLbConfigAddressPoolArgs]
            ]
        ],
        load_balancer_node_pool_config: Optional[
            pulumi.Input[
                BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressPools")
    def address_pools(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[BareMetalClusterLoadBalancerMetalLbConfigAddressPoolArgs]]
    ]: ...
    @address_pools.setter
    def address_pools(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[BareMetalClusterLoadBalancerMetalLbConfigAddressPoolArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerNodePoolConfig")
    def load_balancer_node_pool_config(
        self,
    ) -> Optional[
        pulumi.Input[
            BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigArgs
        ]
    ]: ...
    @load_balancer_node_pool_config.setter
    def load_balancer_node_pool_config(
        self,
        value: Optional[
            pulumi.Input[
                BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigArgs
            ]
        ],
    ): ...

class BareMetalClusterLoadBalancerMetalLbConfigAddressPoolArgsDict(TypedDict):
    addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    pool: pulumi.Input[_builtins.str]
    avoid_buggy_ips: NotRequired[pulumi.Input[_builtins.bool]]
    manual_assign: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BareMetalClusterLoadBalancerMetalLbConfigAddressPoolArgs:
    def __init__(
        __self__,
        *,
        addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        pool: pulumi.Input[_builtins.str],
        avoid_buggy_ips: Optional[pulumi.Input[_builtins.bool]] = ...,
        manual_assign: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @addresses.setter
    def addresses(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def pool(self) -> pulumi.Input[_builtins.str]: ...
    @pool.setter
    def pool(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="avoidBuggyIps")
    def avoid_buggy_ips(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @avoid_buggy_ips.setter
    def avoid_buggy_ips(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="manualAssign")
    def manual_assign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manual_assign.setter
    def manual_assign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigArgsDict(
    TypedDict
):
    node_pool_config: NotRequired[
        pulumi.Input[
            BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgsDict
        ]
    ]

@pulumi.input_type
class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        node_pool_config: Optional[
            pulumi.Input[
                BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(
        self,
    ) -> Optional[
        pulumi.Input[
            BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs
        ]
    ]: ...
    @node_pool_config.setter
    def node_pool_config(
        self,
        value: Optional[
            pulumi.Input[
                BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs
            ]
        ],
    ): ...

class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgsDict
                ]
            ]
        ]
    ]
    operating_system: NotRequired[pulumi.Input[_builtins.str]]
    taints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs
                    ]
                ]
            ]
        ] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        taints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs
                ]
            ]
        ]
    ]: ...
    @node_configs.setter
    def node_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs
                ]
            ]
        ]
    ]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs
                    ]
                ]
            ]
        ],
    ): ...

class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_ip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfigArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_ip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_ip.setter
    def node_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgsDict(
    TypedDict
):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaintArgs:
    def __init__(
        __self__,
        *,
        effect: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterLoadBalancerPortConfigArgsDict(TypedDict):
    control_plane_load_balancer_port: pulumi.Input[_builtins.int]

@pulumi.input_type
class BareMetalClusterLoadBalancerPortConfigArgs:
    def __init__(
        __self__, *, control_plane_load_balancer_port: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneLoadBalancerPort")
    def control_plane_load_balancer_port(self) -> pulumi.Input[_builtins.int]: ...
    @control_plane_load_balancer_port.setter
    def control_plane_load_balancer_port(self, value: pulumi.Input[_builtins.int]): ...

class BareMetalClusterLoadBalancerVipConfigArgsDict(TypedDict):
    control_plane_vip: pulumi.Input[_builtins.str]
    ingress_vip: pulumi.Input[_builtins.str]

@pulumi.input_type
class BareMetalClusterLoadBalancerVipConfigArgs:
    def __init__(
        __self__,
        *,
        control_plane_vip: pulumi.Input[_builtins.str],
        ingress_vip: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneVip")
    def control_plane_vip(self) -> pulumi.Input[_builtins.str]: ...
    @control_plane_vip.setter
    def control_plane_vip(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ingressVip")
    def ingress_vip(self) -> pulumi.Input[_builtins.str]: ...
    @ingress_vip.setter
    def ingress_vip(self, value: pulumi.Input[_builtins.str]): ...

class BareMetalClusterMaintenanceConfigArgsDict(TypedDict):
    maintenance_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class BareMetalClusterMaintenanceConfigArgs:
    def __init__(
        __self__,
        *,
        maintenance_address_cidr_blocks: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceAddressCidrBlocks")
    def maintenance_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @maintenance_address_cidr_blocks.setter
    def maintenance_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class BareMetalClusterNetworkConfigArgsDict(TypedDict):
    advanced_networking: NotRequired[pulumi.Input[_builtins.bool]]
    island_mode_cidr: NotRequired[
        pulumi.Input[BareMetalClusterNetworkConfigIslandModeCidrArgsDict]
    ]
    multiple_network_interfaces_config: NotRequired[
        pulumi.Input[
            BareMetalClusterNetworkConfigMultipleNetworkInterfacesConfigArgsDict
        ]
    ]
    sr_iov_config: NotRequired[
        pulumi.Input[BareMetalClusterNetworkConfigSrIovConfigArgsDict]
    ]

@pulumi.input_type
class BareMetalClusterNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        advanced_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
        island_mode_cidr: Optional[
            pulumi.Input[BareMetalClusterNetworkConfigIslandModeCidrArgs]
        ] = ...,
        multiple_network_interfaces_config: Optional[
            pulumi.Input[
                BareMetalClusterNetworkConfigMultipleNetworkInterfacesConfigArgs
            ]
        ] = ...,
        sr_iov_config: Optional[
            pulumi.Input[BareMetalClusterNetworkConfigSrIovConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedNetworking")
    def advanced_networking(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @advanced_networking.setter
    def advanced_networking(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="islandModeCidr")
    def island_mode_cidr(
        self,
    ) -> Optional[pulumi.Input[BareMetalClusterNetworkConfigIslandModeCidrArgs]]: ...
    @island_mode_cidr.setter
    def island_mode_cidr(
        self,
        value: Optional[pulumi.Input[BareMetalClusterNetworkConfigIslandModeCidrArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multipleNetworkInterfacesConfig")
    def multiple_network_interfaces_config(
        self,
    ) -> Optional[
        pulumi.Input[BareMetalClusterNetworkConfigMultipleNetworkInterfacesConfigArgs]
    ]: ...
    @multiple_network_interfaces_config.setter
    def multiple_network_interfaces_config(
        self,
        value: Optional[
            pulumi.Input[
                BareMetalClusterNetworkConfigMultipleNetworkInterfacesConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="srIovConfig")
    def sr_iov_config(
        self,
    ) -> Optional[pulumi.Input[BareMetalClusterNetworkConfigSrIovConfigArgs]]: ...
    @sr_iov_config.setter
    def sr_iov_config(
        self,
        value: Optional[pulumi.Input[BareMetalClusterNetworkConfigSrIovConfigArgs]],
    ): ...

class BareMetalClusterNetworkConfigIslandModeCidrArgsDict(TypedDict):
    pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    service_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class BareMetalClusterNetworkConfigIslandModeCidrArgs:
    def __init__(
        __self__,
        *,
        pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        service_address_cidr_blocks: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @pod_address_cidr_blocks.setter
    def pod_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @service_address_cidr_blocks.setter
    def service_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class BareMetalClusterNetworkConfigMultipleNetworkInterfacesConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BareMetalClusterNetworkConfigMultipleNetworkInterfacesConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class BareMetalClusterNetworkConfigSrIovConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BareMetalClusterNetworkConfigSrIovConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class BareMetalClusterNodeAccessConfigArgsDict(TypedDict):
    login_user: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterNodeAccessConfigArgs:
    def __init__(
        __self__, *, login_user: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginUser")
    def login_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @login_user.setter
    def login_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterNodeConfigArgsDict(TypedDict):
    container_runtime: NotRequired[pulumi.Input[_builtins.str]]
    max_pods_per_node: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BareMetalClusterNodeConfigArgs:
    def __init__(
        __self__,
        *,
        container_runtime: Optional[pulumi.Input[_builtins.str]] = ...,
        max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerRuntime")
    def container_runtime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_runtime.setter
    def container_runtime(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods_per_node.setter
    def max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class BareMetalClusterOsEnvironmentConfigArgsDict(TypedDict):
    package_repo_excluded: pulumi.Input[_builtins.bool]

@pulumi.input_type
class BareMetalClusterOsEnvironmentConfigArgs:
    def __init__(
        __self__, *, package_repo_excluded: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="packageRepoExcluded")
    def package_repo_excluded(self) -> pulumi.Input[_builtins.bool]: ...
    @package_repo_excluded.setter
    def package_repo_excluded(self, value: pulumi.Input[_builtins.bool]): ...

class BareMetalClusterProxyArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    no_proxies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BareMetalClusterProxyArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        no_proxies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="noProxies")
    def no_proxies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @no_proxies.setter
    def no_proxies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BareMetalClusterSecurityConfigArgsDict(TypedDict):
    authorization: NotRequired[
        pulumi.Input[BareMetalClusterSecurityConfigAuthorizationArgsDict]
    ]

@pulumi.input_type
class BareMetalClusterSecurityConfigArgs:
    def __init__(
        __self__,
        *,
        authorization: Optional[
            pulumi.Input[BareMetalClusterSecurityConfigAuthorizationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authorization(
        self,
    ) -> Optional[pulumi.Input[BareMetalClusterSecurityConfigAuthorizationArgs]]: ...
    @authorization.setter
    def authorization(
        self,
        value: Optional[pulumi.Input[BareMetalClusterSecurityConfigAuthorizationArgs]],
    ): ...

class BareMetalClusterSecurityConfigAuthorizationArgsDict(TypedDict):
    admin_users: pulumi.Input[
        Sequence[
            pulumi.Input[BareMetalClusterSecurityConfigAuthorizationAdminUserArgsDict]
        ]
    ]

@pulumi.input_type
class BareMetalClusterSecurityConfigAuthorizationArgs:
    def __init__(
        __self__,
        *,
        admin_users: pulumi.Input[
            Sequence[
                pulumi.Input[BareMetalClusterSecurityConfigAuthorizationAdminUserArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[BareMetalClusterSecurityConfigAuthorizationAdminUserArgs]]
    ]: ...
    @admin_users.setter
    def admin_users(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[BareMetalClusterSecurityConfigAuthorizationAdminUserArgs]
            ]
        ],
    ): ...

class BareMetalClusterSecurityConfigAuthorizationAdminUserArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]

@pulumi.input_type
class BareMetalClusterSecurityConfigAuthorizationAdminUserArgs:
    def __init__(__self__, *, username: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class BareMetalClusterStatusArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BareMetalClusterStatusConditionArgsDict]]]
    ]
    error_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterStatusArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[BareMetalClusterStatusConditionArgs]]]
        ] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BareMetalClusterStatusConditionArgs]]]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BareMetalClusterStatusConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterStatusConditionArgsDict(TypedDict):
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterStatusConditionArgs:
    def __init__(
        __self__,
        *,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterStorageArgsDict(TypedDict):
    lvp_node_mounts_config: pulumi.Input[
        BareMetalClusterStorageLvpNodeMountsConfigArgsDict
    ]
    lvp_share_config: pulumi.Input[BareMetalClusterStorageLvpShareConfigArgsDict]

@pulumi.input_type
class BareMetalClusterStorageArgs:
    def __init__(
        __self__,
        *,
        lvp_node_mounts_config: pulumi.Input[
            BareMetalClusterStorageLvpNodeMountsConfigArgs
        ],
        lvp_share_config: pulumi.Input[BareMetalClusterStorageLvpShareConfigArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lvpNodeMountsConfig")
    def lvp_node_mounts_config(
        self,
    ) -> pulumi.Input[BareMetalClusterStorageLvpNodeMountsConfigArgs]: ...
    @lvp_node_mounts_config.setter
    def lvp_node_mounts_config(
        self, value: pulumi.Input[BareMetalClusterStorageLvpNodeMountsConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lvpShareConfig")
    def lvp_share_config(
        self,
    ) -> pulumi.Input[BareMetalClusterStorageLvpShareConfigArgs]: ...
    @lvp_share_config.setter
    def lvp_share_config(
        self, value: pulumi.Input[BareMetalClusterStorageLvpShareConfigArgs]
    ): ...

class BareMetalClusterStorageLvpNodeMountsConfigArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    storage_class: pulumi.Input[_builtins.str]

@pulumi.input_type
class BareMetalClusterStorageLvpNodeMountsConfigArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        storage_class: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]: ...
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): ...

class BareMetalClusterStorageLvpShareConfigArgsDict(TypedDict):
    lvp_config: pulumi.Input[BareMetalClusterStorageLvpShareConfigLvpConfigArgsDict]
    shared_path_pv_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BareMetalClusterStorageLvpShareConfigArgs:
    def __init__(
        __self__,
        *,
        lvp_config: pulumi.Input[BareMetalClusterStorageLvpShareConfigLvpConfigArgs],
        shared_path_pv_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lvpConfig")
    def lvp_config(
        self,
    ) -> pulumi.Input[BareMetalClusterStorageLvpShareConfigLvpConfigArgs]: ...
    @lvp_config.setter
    def lvp_config(
        self, value: pulumi.Input[BareMetalClusterStorageLvpShareConfigLvpConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedPathPvCount")
    def shared_path_pv_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shared_path_pv_count.setter
    def shared_path_pv_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class BareMetalClusterStorageLvpShareConfigLvpConfigArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    storage_class: pulumi.Input[_builtins.str]

@pulumi.input_type
class BareMetalClusterStorageLvpShareConfigLvpConfigArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        storage_class: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]: ...
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): ...

class BareMetalClusterUpgradePolicyArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterUpgradePolicyArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalClusterValidationCheckArgsDict(TypedDict):
    options: NotRequired[pulumi.Input[_builtins.str]]
    scenario: NotRequired[pulumi.Input[_builtins.str]]
    statuses: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalClusterValidationCheckStatusArgsDict]]
        ]
    ]

@pulumi.input_type
class BareMetalClusterValidationCheckArgs:
    def __init__(
        __self__,
        *,
        options: Optional[pulumi.Input[_builtins.str]] = ...,
        scenario: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalClusterValidationCheckStatusArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @options.setter
    def options(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scenario(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scenario.setter
    def scenario(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BareMetalClusterValidationCheckStatusArgs]]]
    ]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalClusterValidationCheckStatusArgs]]
            ]
        ],
    ): ...

class BareMetalClusterValidationCheckStatusArgsDict(TypedDict):
    results: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalClusterValidationCheckStatusResultArgsDict]]
        ]
    ]

@pulumi.input_type
class BareMetalClusterValidationCheckStatusArgs:
    def __init__(
        __self__,
        *,
        results: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalClusterValidationCheckStatusResultArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def results(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalClusterValidationCheckStatusResultArgs]]
        ]
    ]: ...
    @results.setter
    def results(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalClusterValidationCheckStatusResultArgs]]
            ]
        ],
    ): ...

class BareMetalClusterValidationCheckStatusResultArgsDict(TypedDict):
    category: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    details: NotRequired[pulumi.Input[_builtins.str]]
    options: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalClusterValidationCheckStatusResultArgs:
    def __init__(
        __self__,
        *,
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        details: Optional[pulumi.Input[_builtins.str]] = ...,
        options: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @options.setter
    def options(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalNodePoolNodePoolConfigArgsDict(TypedDict):
    node_configs: pulumi.Input[
        Sequence[pulumi.Input[BareMetalNodePoolNodePoolConfigNodeConfigArgsDict]]
    ]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    operating_system: NotRequired[pulumi.Input[_builtins.str]]
    taints: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[BareMetalNodePoolNodePoolConfigTaintArgsDict]]
        ]
    ]

@pulumi.input_type
class BareMetalNodePoolNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        node_configs: pulumi.Input[
            Sequence[pulumi.Input[BareMetalNodePoolNodePoolConfigNodeConfigArgs]]
        ],
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        taints: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalNodePoolNodePoolConfigTaintArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[BareMetalNodePoolNodePoolConfigNodeConfigArgs]]
    ]: ...
    @node_configs.setter
    def node_configs(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[BareMetalNodePoolNodePoolConfigNodeConfigArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BareMetalNodePoolNodePoolConfigTaintArgs]]]
    ]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BareMetalNodePoolNodePoolConfigTaintArgs]]
            ]
        ],
    ): ...

class BareMetalNodePoolNodePoolConfigNodeConfigArgsDict(TypedDict):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_ip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalNodePoolNodePoolConfigNodeConfigArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_ip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_ip.setter
    def node_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalNodePoolNodePoolConfigTaintArgsDict(TypedDict):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalNodePoolNodePoolConfigTaintArgs:
    def __init__(
        __self__,
        *,
        effect: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalNodePoolStatusArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BareMetalNodePoolStatusConditionArgsDict]]]
    ]
    error_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalNodePoolStatusArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[BareMetalNodePoolStatusConditionArgs]]]
        ] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BareMetalNodePoolStatusConditionArgs]]]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BareMetalNodePoolStatusConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BareMetalNodePoolStatusConditionArgsDict(TypedDict):
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BareMetalNodePoolStatusConditionArgs:
    def __init__(
        __self__,
        *,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterAntiAffinityGroupsArgsDict(TypedDict):
    aag_config_disabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class VMwareClusterAntiAffinityGroupsArgs:
    def __init__(
        __self__, *, aag_config_disabled: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aagConfigDisabled")
    def aag_config_disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @aag_config_disabled.setter
    def aag_config_disabled(self, value: pulumi.Input[_builtins.bool]): ...

class VMwareClusterAuthorizationArgsDict(TypedDict):
    admin_users: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VMwareClusterAuthorizationAdminUserArgsDict]]
        ]
    ]

@pulumi.input_type
class VMwareClusterAuthorizationArgs:
    def __init__(
        __self__,
        *,
        admin_users: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VMwareClusterAuthorizationAdminUserArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VMwareClusterAuthorizationAdminUserArgs]]]
    ]: ...
    @admin_users.setter
    def admin_users(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VMwareClusterAuthorizationAdminUserArgs]]
            ]
        ],
    ): ...

class VMwareClusterAuthorizationAdminUserArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]

@pulumi.input_type
class VMwareClusterAuthorizationAdminUserArgs:
    def __init__(__self__, *, username: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class VMwareClusterAutoRepairConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class VMwareClusterAutoRepairConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class VMwareClusterControlPlaneNodeArgsDict(TypedDict):
    auto_resize_config: NotRequired[
        pulumi.Input[VMwareClusterControlPlaneNodeAutoResizeConfigArgsDict]
    ]
    cpus: NotRequired[pulumi.Input[_builtins.int]]
    memory: NotRequired[pulumi.Input[_builtins.int]]
    replicas: NotRequired[pulumi.Input[_builtins.int]]
    vsphere_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VMwareClusterControlPlaneNodeVsphereConfigArgsDict]]
        ]
    ]

@pulumi.input_type
class VMwareClusterControlPlaneNodeArgs:
    def __init__(
        __self__,
        *,
        auto_resize_config: Optional[
            pulumi.Input[VMwareClusterControlPlaneNodeAutoResizeConfigArgs]
        ] = ...,
        cpus: Optional[pulumi.Input[_builtins.int]] = ...,
        memory: Optional[pulumi.Input[_builtins.int]] = ...,
        replicas: Optional[pulumi.Input[_builtins.int]] = ...,
        vsphere_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VMwareClusterControlPlaneNodeVsphereConfigArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoResizeConfig")
    def auto_resize_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterControlPlaneNodeAutoResizeConfigArgs]]: ...
    @auto_resize_config.setter
    def auto_resize_config(
        self,
        value: Optional[
            pulumi.Input[VMwareClusterControlPlaneNodeAutoResizeConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def cpus(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpus.setter
    def cpus(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="vsphereConfigs")
    def vsphere_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VMwareClusterControlPlaneNodeVsphereConfigArgs]]
        ]
    ]: ...
    @vsphere_configs.setter
    def vsphere_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VMwareClusterControlPlaneNodeVsphereConfigArgs]]
            ]
        ],
    ): ...

class VMwareClusterControlPlaneNodeAutoResizeConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class VMwareClusterControlPlaneNodeAutoResizeConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class VMwareClusterControlPlaneNodeVsphereConfigArgsDict(TypedDict):
    datastore: NotRequired[pulumi.Input[_builtins.str]]
    storage_policy_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterControlPlaneNodeVsphereConfigArgs:
    def __init__(
        __self__,
        *,
        datastore: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datastore.setter
    def datastore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storagePolicyName")
    def storage_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_policy_name.setter
    def storage_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterDataplaneV2ArgsDict(TypedDict):
    advanced_networking: NotRequired[pulumi.Input[_builtins.bool]]
    dataplane_v2_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    windows_dataplane_v2_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VMwareClusterDataplaneV2Args:
    def __init__(
        __self__,
        *,
        advanced_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
        dataplane_v2_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        windows_dataplane_v2_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedNetworking")
    def advanced_networking(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @advanced_networking.setter
    def advanced_networking(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dataplaneV2Enabled")
    def dataplane_v2_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dataplane_v2_enabled.setter
    def dataplane_v2_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="windowsDataplaneV2Enabled")
    def windows_dataplane_v2_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @windows_dataplane_v2_enabled.setter
    def windows_dataplane_v2_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class VMwareClusterFleetArgsDict(TypedDict):
    membership: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterFleetArgs:
    def __init__(
        __self__, *, membership: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterLoadBalancerArgsDict(TypedDict):
    f5_config: NotRequired[pulumi.Input[VMwareClusterLoadBalancerF5ConfigArgsDict]]
    manual_lb_config: NotRequired[
        pulumi.Input[VMwareClusterLoadBalancerManualLbConfigArgsDict]
    ]
    metal_lb_config: NotRequired[
        pulumi.Input[VMwareClusterLoadBalancerMetalLbConfigArgsDict]
    ]
    vip_config: NotRequired[pulumi.Input[VMwareClusterLoadBalancerVipConfigArgsDict]]

@pulumi.input_type
class VMwareClusterLoadBalancerArgs:
    def __init__(
        __self__,
        *,
        f5_config: Optional[pulumi.Input[VMwareClusterLoadBalancerF5ConfigArgs]] = ...,
        manual_lb_config: Optional[
            pulumi.Input[VMwareClusterLoadBalancerManualLbConfigArgs]
        ] = ...,
        metal_lb_config: Optional[
            pulumi.Input[VMwareClusterLoadBalancerMetalLbConfigArgs]
        ] = ...,
        vip_config: Optional[
            pulumi.Input[VMwareClusterLoadBalancerVipConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="f5Config")
    def f5_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterLoadBalancerF5ConfigArgs]]: ...
    @f5_config.setter
    def f5_config(
        self, value: Optional[pulumi.Input[VMwareClusterLoadBalancerF5ConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="manualLbConfig")
    def manual_lb_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterLoadBalancerManualLbConfigArgs]]: ...
    @manual_lb_config.setter
    def manual_lb_config(
        self, value: Optional[pulumi.Input[VMwareClusterLoadBalancerManualLbConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metalLbConfig")
    def metal_lb_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterLoadBalancerMetalLbConfigArgs]]: ...
    @metal_lb_config.setter
    def metal_lb_config(
        self, value: Optional[pulumi.Input[VMwareClusterLoadBalancerMetalLbConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vipConfig")
    def vip_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterLoadBalancerVipConfigArgs]]: ...
    @vip_config.setter
    def vip_config(
        self, value: Optional[pulumi.Input[VMwareClusterLoadBalancerVipConfigArgs]]
    ): ...

class VMwareClusterLoadBalancerF5ConfigArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    partition: NotRequired[pulumi.Input[_builtins.str]]
    snat_pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterLoadBalancerF5ConfigArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        partition: Optional[pulumi.Input[_builtins.str]] = ...,
        snat_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partition.setter
    def partition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snatPool")
    def snat_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snat_pool.setter
    def snat_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterLoadBalancerManualLbConfigArgsDict(TypedDict):
    control_plane_node_port: NotRequired[pulumi.Input[_builtins.int]]
    ingress_http_node_port: NotRequired[pulumi.Input[_builtins.int]]
    ingress_https_node_port: NotRequired[pulumi.Input[_builtins.int]]
    konnectivity_server_node_port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VMwareClusterLoadBalancerManualLbConfigArgs:
    def __init__(
        __self__,
        *,
        control_plane_node_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ingress_http_node_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ingress_https_node_port: Optional[pulumi.Input[_builtins.int]] = ...,
        konnectivity_server_node_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodePort")
    def control_plane_node_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @control_plane_node_port.setter
    def control_plane_node_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressHttpNodePort")
    def ingress_http_node_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ingress_http_node_port.setter
    def ingress_http_node_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressHttpsNodePort")
    def ingress_https_node_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ingress_https_node_port.setter
    def ingress_https_node_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="konnectivityServerNodePort")
    def konnectivity_server_node_port(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @konnectivity_server_node_port.setter
    def konnectivity_server_node_port(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class VMwareClusterLoadBalancerMetalLbConfigArgsDict(TypedDict):
    address_pools: pulumi.Input[
        Sequence[
            pulumi.Input[VMwareClusterLoadBalancerMetalLbConfigAddressPoolArgsDict]
        ]
    ]

@pulumi.input_type
class VMwareClusterLoadBalancerMetalLbConfigArgs:
    def __init__(
        __self__,
        *,
        address_pools: pulumi.Input[
            Sequence[
                pulumi.Input[VMwareClusterLoadBalancerMetalLbConfigAddressPoolArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressPools")
    def address_pools(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[VMwareClusterLoadBalancerMetalLbConfigAddressPoolArgs]]
    ]: ...
    @address_pools.setter
    def address_pools(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[VMwareClusterLoadBalancerMetalLbConfigAddressPoolArgs]
            ]
        ],
    ): ...

class VMwareClusterLoadBalancerMetalLbConfigAddressPoolArgsDict(TypedDict):
    addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    pool: pulumi.Input[_builtins.str]
    avoid_buggy_ips: NotRequired[pulumi.Input[_builtins.bool]]
    manual_assign: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VMwareClusterLoadBalancerMetalLbConfigAddressPoolArgs:
    def __init__(
        __self__,
        *,
        addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        pool: pulumi.Input[_builtins.str],
        avoid_buggy_ips: Optional[pulumi.Input[_builtins.bool]] = ...,
        manual_assign: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @addresses.setter
    def addresses(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def pool(self) -> pulumi.Input[_builtins.str]: ...
    @pool.setter
    def pool(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="avoidBuggyIps")
    def avoid_buggy_ips(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @avoid_buggy_ips.setter
    def avoid_buggy_ips(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="manualAssign")
    def manual_assign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manual_assign.setter
    def manual_assign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class VMwareClusterLoadBalancerVipConfigArgsDict(TypedDict):
    control_plane_vip: NotRequired[pulumi.Input[_builtins.str]]
    ingress_vip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterLoadBalancerVipConfigArgs:
    def __init__(
        __self__,
        *,
        control_plane_vip: Optional[pulumi.Input[_builtins.str]] = ...,
        ingress_vip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneVip")
    def control_plane_vip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @control_plane_vip.setter
    def control_plane_vip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressVip")
    def ingress_vip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingress_vip.setter
    def ingress_vip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterNetworkConfigArgsDict(TypedDict):
    pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    service_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    control_plane_v2_config: NotRequired[
        pulumi.Input[VMwareClusterNetworkConfigControlPlaneV2ConfigArgsDict]
    ]
    dhcp_ip_config: NotRequired[
        pulumi.Input[VMwareClusterNetworkConfigDhcpIpConfigArgsDict]
    ]
    host_config: NotRequired[pulumi.Input[VMwareClusterNetworkConfigHostConfigArgsDict]]
    static_ip_config: NotRequired[
        pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigArgsDict]
    ]
    vcenter_network: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        service_address_cidr_blocks: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
        control_plane_v2_config: Optional[
            pulumi.Input[VMwareClusterNetworkConfigControlPlaneV2ConfigArgs]
        ] = ...,
        dhcp_ip_config: Optional[
            pulumi.Input[VMwareClusterNetworkConfigDhcpIpConfigArgs]
        ] = ...,
        host_config: Optional[
            pulumi.Input[VMwareClusterNetworkConfigHostConfigArgs]
        ] = ...,
        static_ip_config: Optional[
            pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigArgs]
        ] = ...,
        vcenter_network: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @pod_address_cidr_blocks.setter
    def pod_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @service_address_cidr_blocks.setter
    def service_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneV2Config")
    def control_plane_v2_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterNetworkConfigControlPlaneV2ConfigArgs]]: ...
    @control_plane_v2_config.setter
    def control_plane_v2_config(
        self,
        value: Optional[
            pulumi.Input[VMwareClusterNetworkConfigControlPlaneV2ConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dhcpIpConfig")
    def dhcp_ip_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterNetworkConfigDhcpIpConfigArgs]]: ...
    @dhcp_ip_config.setter
    def dhcp_ip_config(
        self, value: Optional[pulumi.Input[VMwareClusterNetworkConfigDhcpIpConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostConfig")
    def host_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterNetworkConfigHostConfigArgs]]: ...
    @host_config.setter
    def host_config(
        self, value: Optional[pulumi.Input[VMwareClusterNetworkConfigHostConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="staticIpConfig")
    def static_ip_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigArgs]]: ...
    @static_ip_config.setter
    def static_ip_config(
        self,
        value: Optional[pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vcenterNetwork")
    def vcenter_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vcenter_network.setter
    def vcenter_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterNetworkConfigControlPlaneV2ConfigArgsDict(TypedDict):
    control_plane_ip_block: NotRequired[
        pulumi.Input[
            VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockArgsDict
        ]
    ]

@pulumi.input_type
class VMwareClusterNetworkConfigControlPlaneV2ConfigArgs:
    def __init__(
        __self__,
        *,
        control_plane_ip_block: Optional[
            pulumi.Input[
                VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneIpBlock")
    def control_plane_ip_block(
        self,
    ) -> Optional[
        pulumi.Input[
            VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockArgs
        ]
    ]: ...
    @control_plane_ip_block.setter
    def control_plane_ip_block(
        self,
        value: Optional[
            pulumi.Input[
                VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockArgs
            ]
        ],
    ): ...

class VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockArgsDict(
    TypedDict
):
    gateway: NotRequired[pulumi.Input[_builtins.str]]
    ips: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockIpArgsDict
                ]
            ]
        ]
    ]
    netmask: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockArgs:
    def __init__(
        __self__,
        *,
        gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        ips: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockIpArgs
                    ]
                ]
            ]
        ] = ...,
        netmask: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ips(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockIpArgs
                ]
            ]
        ]
    ]: ...
    @ips.setter
    def ips(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockIpArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def netmask(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @netmask.setter
    def netmask(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockIpArgsDict(
    TypedDict
):
    hostname: NotRequired[pulumi.Input[_builtins.str]]
    ip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockIpArgs:
    def __init__(
        __self__,
        *,
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        ip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip.setter
    def ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterNetworkConfigDhcpIpConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class VMwareClusterNetworkConfigDhcpIpConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class VMwareClusterNetworkConfigHostConfigArgsDict(TypedDict):
    dns_search_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ntp_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class VMwareClusterNetworkConfigHostConfigArgs:
    def __init__(
        __self__,
        *,
        dns_search_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ntp_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsSearchDomains")
    def dns_search_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_search_domains.setter
    def dns_search_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ntpServers")
    def ntp_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ntp_servers.setter
    def ntp_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class VMwareClusterNetworkConfigStaticIpConfigArgsDict(TypedDict):
    ip_blocks: pulumi.Input[
        Sequence[pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigIpBlockArgsDict]]
    ]

@pulumi.input_type
class VMwareClusterNetworkConfigStaticIpConfigArgs:
    def __init__(
        __self__,
        *,
        ip_blocks: pulumi.Input[
            Sequence[pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigIpBlockArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipBlocks")
    def ip_blocks(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigIpBlockArgs]]
    ]: ...
    @ip_blocks.setter
    def ip_blocks(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigIpBlockArgs]]
        ],
    ): ...

class VMwareClusterNetworkConfigStaticIpConfigIpBlockArgsDict(TypedDict):
    gateway: pulumi.Input[_builtins.str]
    ips: pulumi.Input[
        Sequence[
            pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigIpBlockIpArgsDict]
        ]
    ]
    netmask: pulumi.Input[_builtins.str]

@pulumi.input_type
class VMwareClusterNetworkConfigStaticIpConfigIpBlockArgs:
    def __init__(
        __self__,
        *,
        gateway: pulumi.Input[_builtins.str],
        ips: pulumi.Input[
            Sequence[
                pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigIpBlockIpArgs]
            ]
        ],
        netmask: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> pulumi.Input[_builtins.str]: ...
    @gateway.setter
    def gateway(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def ips(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigIpBlockIpArgs]]
    ]: ...
    @ips.setter
    def ips(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[VMwareClusterNetworkConfigStaticIpConfigIpBlockIpArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def netmask(self) -> pulumi.Input[_builtins.str]: ...
    @netmask.setter
    def netmask(self, value: pulumi.Input[_builtins.str]): ...

class VMwareClusterNetworkConfigStaticIpConfigIpBlockIpArgsDict(TypedDict):
    ip: pulumi.Input[_builtins.str]
    hostname: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterNetworkConfigStaticIpConfigIpBlockIpArgs:
    def __init__(
        __self__,
        *,
        ip: pulumi.Input[_builtins.str],
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> pulumi.Input[_builtins.str]: ...
    @ip.setter
    def ip(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterStatusArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VMwareClusterStatusConditionArgsDict]]]
    ]
    error_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterStatusArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareClusterStatusConditionArgs]]]
        ] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VMwareClusterStatusConditionArgs]]]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareClusterStatusConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterStatusConditionArgsDict(TypedDict):
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterStatusConditionArgs:
    def __init__(
        __self__,
        *,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterStorageArgsDict(TypedDict):
    vsphere_csi_disabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class VMwareClusterStorageArgs:
    def __init__(
        __self__, *, vsphere_csi_disabled: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vsphereCsiDisabled")
    def vsphere_csi_disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @vsphere_csi_disabled.setter
    def vsphere_csi_disabled(self, value: pulumi.Input[_builtins.bool]): ...

class VMwareClusterUpgradePolicyArgsDict(TypedDict):
    control_plane_only: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VMwareClusterUpgradePolicyArgs:
    def __init__(
        __self__, *, control_plane_only: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneOnly")
    def control_plane_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @control_plane_only.setter
    def control_plane_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class VMwareClusterValidationCheckArgsDict(TypedDict):
    options: NotRequired[pulumi.Input[_builtins.str]]
    scenario: NotRequired[pulumi.Input[_builtins.str]]
    statuses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VMwareClusterValidationCheckStatusArgsDict]]]
    ]

@pulumi.input_type
class VMwareClusterValidationCheckArgs:
    def __init__(
        __self__,
        *,
        options: Optional[pulumi.Input[_builtins.str]] = ...,
        scenario: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareClusterValidationCheckStatusArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @options.setter
    def options(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scenario(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scenario.setter
    def scenario(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VMwareClusterValidationCheckStatusArgs]]]
    ]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareClusterValidationCheckStatusArgs]]]
        ],
    ): ...

class VMwareClusterValidationCheckStatusArgsDict(TypedDict):
    results: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VMwareClusterValidationCheckStatusResultArgsDict]]
        ]
    ]

@pulumi.input_type
class VMwareClusterValidationCheckStatusArgs:
    def __init__(
        __self__,
        *,
        results: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VMwareClusterValidationCheckStatusResultArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def results(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VMwareClusterValidationCheckStatusResultArgs]]
        ]
    ]: ...
    @results.setter
    def results(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VMwareClusterValidationCheckStatusResultArgs]]
            ]
        ],
    ): ...

class VMwareClusterValidationCheckStatusResultArgsDict(TypedDict):
    category: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    details: NotRequired[pulumi.Input[_builtins.str]]
    options: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterValidationCheckStatusResultArgs:
    def __init__(
        __self__,
        *,
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        details: Optional[pulumi.Input[_builtins.str]] = ...,
        options: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @options.setter
    def options(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareClusterVcenterArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    ca_cert_data: NotRequired[pulumi.Input[_builtins.str]]
    cluster: NotRequired[pulumi.Input[_builtins.str]]
    datacenter: NotRequired[pulumi.Input[_builtins.str]]
    datastore: NotRequired[pulumi.Input[_builtins.str]]
    folder: NotRequired[pulumi.Input[_builtins.str]]
    resource_pool: NotRequired[pulumi.Input[_builtins.str]]
    storage_policy_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareClusterVcenterArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_cert_data: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        datacenter: Optional[pulumi.Input[_builtins.str]] = ...,
        datastore: Optional[pulumi.Input[_builtins.str]] = ...,
        folder: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertData")
    def ca_cert_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_cert_data.setter
    def ca_cert_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datastore.setter
    def datastore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourcePool")
    def resource_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_pool.setter
    def resource_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storagePolicyName")
    def storage_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_policy_name.setter
    def storage_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareNodePoolConfigArgsDict(TypedDict):
    image_type: pulumi.Input[_builtins.str]
    boot_disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    cpus: NotRequired[pulumi.Input[_builtins.int]]
    enable_load_balancer: NotRequired[pulumi.Input[_builtins.bool]]
    image: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    memory_mb: NotRequired[pulumi.Input[_builtins.int]]
    replicas: NotRequired[pulumi.Input[_builtins.int]]
    taints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolConfigTaintArgsDict]]]
    ]
    vsphere_config: NotRequired[pulumi.Input[VMwareNodePoolConfigVsphereConfigArgsDict]]

@pulumi.input_type
class VMwareNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        image_type: pulumi.Input[_builtins.str],
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        cpus: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_load_balancer: Optional[pulumi.Input[_builtins.bool]] = ...,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        memory_mb: Optional[pulumi.Input[_builtins.int]] = ...,
        replicas: Optional[pulumi.Input[_builtins.int]] = ...,
        taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolConfigTaintArgs]]]
        ] = ...,
        vsphere_config: Optional[
            pulumi.Input[VMwareNodePoolConfigVsphereConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> pulumi.Input[_builtins.str]: ...
    @image_type.setter
    def image_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def cpus(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpus.setter
    def cpus(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="enableLoadBalancer")
    def enable_load_balancer(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_load_balancer.setter
    def enable_load_balancer(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryMb")
    def memory_mb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_mb.setter
    def memory_mb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolConfigTaintArgs]]]
    ]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolConfigTaintArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vsphereConfig")
    def vsphere_config(
        self,
    ) -> Optional[pulumi.Input[VMwareNodePoolConfigVsphereConfigArgs]]: ...
    @vsphere_config.setter
    def vsphere_config(
        self, value: Optional[pulumi.Input[VMwareNodePoolConfigVsphereConfigArgs]]
    ): ...

class VMwareNodePoolConfigTaintArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    effect: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareNodePoolConfigTaintArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        effect: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareNodePoolConfigVsphereConfigArgsDict(TypedDict):
    datastore: NotRequired[pulumi.Input[_builtins.str]]
    host_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tags: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VMwareNodePoolConfigVsphereConfigTagArgsDict]]
        ]
    ]

@pulumi.input_type
class VMwareNodePoolConfigVsphereConfigArgs:
    def __init__(
        __self__,
        *,
        datastore: Optional[pulumi.Input[_builtins.str]] = ...,
        host_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VMwareNodePoolConfigVsphereConfigTagArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datastore.setter
    def datastore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostGroups")
    def host_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @host_groups.setter
    def host_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolConfigVsphereConfigTagArgs]]]
    ]: ...
    @tags.setter
    def tags(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VMwareNodePoolConfigVsphereConfigTagArgs]]
            ]
        ],
    ): ...

class VMwareNodePoolConfigVsphereConfigTagArgsDict(TypedDict):
    category: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareNodePoolConfigVsphereConfigTagArgs:
    def __init__(
        __self__,
        *,
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareNodePoolNodePoolAutoscalingArgsDict(TypedDict):
    max_replicas: pulumi.Input[_builtins.int]
    min_replicas: pulumi.Input[_builtins.int]

@pulumi.input_type
class VMwareNodePoolNodePoolAutoscalingArgs:
    def __init__(
        __self__,
        *,
        max_replicas: pulumi.Input[_builtins.int],
        min_replicas: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReplicas")
    def max_replicas(self) -> pulumi.Input[_builtins.int]: ...
    @max_replicas.setter
    def max_replicas(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minReplicas")
    def min_replicas(self) -> pulumi.Input[_builtins.int]: ...
    @min_replicas.setter
    def min_replicas(self, value: pulumi.Input[_builtins.int]): ...

class VMwareNodePoolStatusArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolStatusConditionArgsDict]]]
    ]
    error_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareNodePoolStatusArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolStatusConditionArgs]]]
        ] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolStatusConditionArgs]]]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolStatusConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareNodePoolStatusConditionArgsDict(TypedDict):
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareNodePoolStatusConditionArgs:
    def __init__(
        __self__,
        *,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterAddonNodeArgsDict(TypedDict):
    auto_resize_config: NotRequired[
        pulumi.Input[VmwareAdminClusterAddonNodeAutoResizeConfigArgsDict]
    ]

@pulumi.input_type
class VmwareAdminClusterAddonNodeArgs:
    def __init__(
        __self__,
        *,
        auto_resize_config: Optional[
            pulumi.Input[VmwareAdminClusterAddonNodeAutoResizeConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoResizeConfig")
    def auto_resize_config(
        self,
    ) -> Optional[pulumi.Input[VmwareAdminClusterAddonNodeAutoResizeConfigArgs]]: ...
    @auto_resize_config.setter
    def auto_resize_config(
        self,
        value: Optional[pulumi.Input[VmwareAdminClusterAddonNodeAutoResizeConfigArgs]],
    ): ...

class VmwareAdminClusterAddonNodeAutoResizeConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class VmwareAdminClusterAddonNodeAutoResizeConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class VmwareAdminClusterAntiAffinityGroupsArgsDict(TypedDict):
    aag_config_disabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class VmwareAdminClusterAntiAffinityGroupsArgs:
    def __init__(
        __self__, *, aag_config_disabled: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aagConfigDisabled")
    def aag_config_disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @aag_config_disabled.setter
    def aag_config_disabled(self, value: pulumi.Input[_builtins.bool]): ...

class VmwareAdminClusterAuthorizationArgsDict(TypedDict):
    viewer_users: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VmwareAdminClusterAuthorizationViewerUserArgsDict]]
        ]
    ]

@pulumi.input_type
class VmwareAdminClusterAuthorizationArgs:
    def __init__(
        __self__,
        *,
        viewer_users: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VmwareAdminClusterAuthorizationViewerUserArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="viewerUsers")
    def viewer_users(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VmwareAdminClusterAuthorizationViewerUserArgs]]
        ]
    ]: ...
    @viewer_users.setter
    def viewer_users(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VmwareAdminClusterAuthorizationViewerUserArgs]]
            ]
        ],
    ): ...

class VmwareAdminClusterAuthorizationViewerUserArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]

@pulumi.input_type
class VmwareAdminClusterAuthorizationViewerUserArgs:
    def __init__(__self__, *, username: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class VmwareAdminClusterAutoRepairConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class VmwareAdminClusterAutoRepairConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class VmwareAdminClusterControlPlaneNodeArgsDict(TypedDict):
    cpus: NotRequired[pulumi.Input[_builtins.int]]
    memory: NotRequired[pulumi.Input[_builtins.int]]
    replicas: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VmwareAdminClusterControlPlaneNodeArgs:
    def __init__(
        __self__,
        *,
        cpus: Optional[pulumi.Input[_builtins.int]] = ...,
        memory: Optional[pulumi.Input[_builtins.int]] = ...,
        replicas: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpus(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpus.setter
    def cpus(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class VmwareAdminClusterFleetArgsDict(TypedDict):
    membership: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterFleetArgs:
    def __init__(
        __self__, *, membership: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterLoadBalancerArgsDict(TypedDict):
    vip_config: pulumi.Input[VmwareAdminClusterLoadBalancerVipConfigArgsDict]
    f5_config: NotRequired[pulumi.Input[VmwareAdminClusterLoadBalancerF5ConfigArgsDict]]
    manual_lb_config: NotRequired[
        pulumi.Input[VmwareAdminClusterLoadBalancerManualLbConfigArgsDict]
    ]
    metal_lb_config: NotRequired[
        pulumi.Input[VmwareAdminClusterLoadBalancerMetalLbConfigArgsDict]
    ]

@pulumi.input_type
class VmwareAdminClusterLoadBalancerArgs:
    def __init__(
        __self__,
        *,
        vip_config: pulumi.Input[VmwareAdminClusterLoadBalancerVipConfigArgs],
        f5_config: Optional[
            pulumi.Input[VmwareAdminClusterLoadBalancerF5ConfigArgs]
        ] = ...,
        manual_lb_config: Optional[
            pulumi.Input[VmwareAdminClusterLoadBalancerManualLbConfigArgs]
        ] = ...,
        metal_lb_config: Optional[
            pulumi.Input[VmwareAdminClusterLoadBalancerMetalLbConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vipConfig")
    def vip_config(
        self,
    ) -> pulumi.Input[VmwareAdminClusterLoadBalancerVipConfigArgs]: ...
    @vip_config.setter
    def vip_config(
        self, value: pulumi.Input[VmwareAdminClusterLoadBalancerVipConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="f5Config")
    def f5_config(
        self,
    ) -> Optional[pulumi.Input[VmwareAdminClusterLoadBalancerF5ConfigArgs]]: ...
    @f5_config.setter
    def f5_config(
        self, value: Optional[pulumi.Input[VmwareAdminClusterLoadBalancerF5ConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="manualLbConfig")
    def manual_lb_config(
        self,
    ) -> Optional[pulumi.Input[VmwareAdminClusterLoadBalancerManualLbConfigArgs]]: ...
    @manual_lb_config.setter
    def manual_lb_config(
        self,
        value: Optional[pulumi.Input[VmwareAdminClusterLoadBalancerManualLbConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="metalLbConfig")
    def metal_lb_config(
        self,
    ) -> Optional[pulumi.Input[VmwareAdminClusterLoadBalancerMetalLbConfigArgs]]: ...
    @metal_lb_config.setter
    def metal_lb_config(
        self,
        value: Optional[pulumi.Input[VmwareAdminClusterLoadBalancerMetalLbConfigArgs]],
    ): ...

class VmwareAdminClusterLoadBalancerF5ConfigArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    partition: NotRequired[pulumi.Input[_builtins.str]]
    snat_pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterLoadBalancerF5ConfigArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        partition: Optional[pulumi.Input[_builtins.str]] = ...,
        snat_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partition.setter
    def partition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snatPool")
    def snat_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snat_pool.setter
    def snat_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterLoadBalancerManualLbConfigArgsDict(TypedDict):
    addons_node_port: NotRequired[pulumi.Input[_builtins.int]]
    control_plane_node_port: NotRequired[pulumi.Input[_builtins.int]]
    ingress_http_node_port: NotRequired[pulumi.Input[_builtins.int]]
    ingress_https_node_port: NotRequired[pulumi.Input[_builtins.int]]
    konnectivity_server_node_port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VmwareAdminClusterLoadBalancerManualLbConfigArgs:
    def __init__(
        __self__,
        *,
        addons_node_port: Optional[pulumi.Input[_builtins.int]] = ...,
        control_plane_node_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ingress_http_node_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ingress_https_node_port: Optional[pulumi.Input[_builtins.int]] = ...,
        konnectivity_server_node_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addonsNodePort")
    def addons_node_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @addons_node_port.setter
    def addons_node_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodePort")
    def control_plane_node_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @control_plane_node_port.setter
    def control_plane_node_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressHttpNodePort")
    def ingress_http_node_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ingress_http_node_port.setter
    def ingress_http_node_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressHttpsNodePort")
    def ingress_https_node_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ingress_https_node_port.setter
    def ingress_https_node_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="konnectivityServerNodePort")
    def konnectivity_server_node_port(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @konnectivity_server_node_port.setter
    def konnectivity_server_node_port(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class VmwareAdminClusterLoadBalancerMetalLbConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VmwareAdminClusterLoadBalancerMetalLbConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class VmwareAdminClusterLoadBalancerVipConfigArgsDict(TypedDict):
    control_plane_vip: pulumi.Input[_builtins.str]
    addons_vip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterLoadBalancerVipConfigArgs:
    def __init__(
        __self__,
        *,
        control_plane_vip: pulumi.Input[_builtins.str],
        addons_vip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneVip")
    def control_plane_vip(self) -> pulumi.Input[_builtins.str]: ...
    @control_plane_vip.setter
    def control_plane_vip(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addonsVip")
    def addons_vip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @addons_vip.setter
    def addons_vip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterNetworkConfigArgsDict(TypedDict):
    pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    service_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    dhcp_ip_config: NotRequired[
        pulumi.Input[VmwareAdminClusterNetworkConfigDhcpIpConfigArgsDict]
    ]
    ha_control_plane_config: NotRequired[
        pulumi.Input[VmwareAdminClusterNetworkConfigHaControlPlaneConfigArgsDict]
    ]
    host_config: NotRequired[
        pulumi.Input[VmwareAdminClusterNetworkConfigHostConfigArgsDict]
    ]
    static_ip_config: NotRequired[
        pulumi.Input[VmwareAdminClusterNetworkConfigStaticIpConfigArgsDict]
    ]
    vcenter_network: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        service_address_cidr_blocks: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
        dhcp_ip_config: Optional[
            pulumi.Input[VmwareAdminClusterNetworkConfigDhcpIpConfigArgs]
        ] = ...,
        ha_control_plane_config: Optional[
            pulumi.Input[VmwareAdminClusterNetworkConfigHaControlPlaneConfigArgs]
        ] = ...,
        host_config: Optional[
            pulumi.Input[VmwareAdminClusterNetworkConfigHostConfigArgs]
        ] = ...,
        static_ip_config: Optional[
            pulumi.Input[VmwareAdminClusterNetworkConfigStaticIpConfigArgs]
        ] = ...,
        vcenter_network: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @pod_address_cidr_blocks.setter
    def pod_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @service_address_cidr_blocks.setter
    def service_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dhcpIpConfig")
    def dhcp_ip_config(
        self,
    ) -> Optional[pulumi.Input[VmwareAdminClusterNetworkConfigDhcpIpConfigArgs]]: ...
    @dhcp_ip_config.setter
    def dhcp_ip_config(
        self,
        value: Optional[pulumi.Input[VmwareAdminClusterNetworkConfigDhcpIpConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="haControlPlaneConfig")
    def ha_control_plane_config(
        self,
    ) -> Optional[
        pulumi.Input[VmwareAdminClusterNetworkConfigHaControlPlaneConfigArgs]
    ]: ...
    @ha_control_plane_config.setter
    def ha_control_plane_config(
        self,
        value: Optional[
            pulumi.Input[VmwareAdminClusterNetworkConfigHaControlPlaneConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostConfig")
    def host_config(
        self,
    ) -> Optional[pulumi.Input[VmwareAdminClusterNetworkConfigHostConfigArgs]]: ...
    @host_config.setter
    def host_config(
        self,
        value: Optional[pulumi.Input[VmwareAdminClusterNetworkConfigHostConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="staticIpConfig")
    def static_ip_config(
        self,
    ) -> Optional[pulumi.Input[VmwareAdminClusterNetworkConfigStaticIpConfigArgs]]: ...
    @static_ip_config.setter
    def static_ip_config(
        self,
        value: Optional[
            pulumi.Input[VmwareAdminClusterNetworkConfigStaticIpConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vcenterNetwork")
    def vcenter_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vcenter_network.setter
    def vcenter_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterNetworkConfigDhcpIpConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class VmwareAdminClusterNetworkConfigDhcpIpConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class VmwareAdminClusterNetworkConfigHaControlPlaneConfigArgsDict(TypedDict):
    control_plane_ip_block: NotRequired[
        pulumi.Input[
            VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockArgsDict
        ]
    ]

@pulumi.input_type
class VmwareAdminClusterNetworkConfigHaControlPlaneConfigArgs:
    def __init__(
        __self__,
        *,
        control_plane_ip_block: Optional[
            pulumi.Input[
                VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneIpBlock")
    def control_plane_ip_block(
        self,
    ) -> Optional[
        pulumi.Input[
            VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockArgs
        ]
    ]: ...
    @control_plane_ip_block.setter
    def control_plane_ip_block(
        self,
        value: Optional[
            pulumi.Input[
                VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockArgs
            ]
        ],
    ): ...

class VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockArgsDict(
    TypedDict
):
    gateway: pulumi.Input[_builtins.str]
    ips: pulumi.Input[
        Sequence[
            pulumi.Input[
                VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockIpArgsDict
            ]
        ]
    ]
    netmask: pulumi.Input[_builtins.str]

@pulumi.input_type
class VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockArgs:
    def __init__(
        __self__,
        *,
        gateway: pulumi.Input[_builtins.str],
        ips: pulumi.Input[
            Sequence[
                pulumi.Input[
                    VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockIpArgs
                ]
            ]
        ],
        netmask: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> pulumi.Input[_builtins.str]: ...
    @gateway.setter
    def gateway(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def ips(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockIpArgs
            ]
        ]
    ]: ...
    @ips.setter
    def ips(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockIpArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def netmask(self) -> pulumi.Input[_builtins.str]: ...
    @netmask.setter
    def netmask(self, value: pulumi.Input[_builtins.str]): ...

class VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockIpArgsDict(
    TypedDict
):
    ip: pulumi.Input[_builtins.str]
    hostname: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockIpArgs:
    def __init__(
        __self__,
        *,
        ip: pulumi.Input[_builtins.str],
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> pulumi.Input[_builtins.str]: ...
    @ip.setter
    def ip(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterNetworkConfigHostConfigArgsDict(TypedDict):
    dns_search_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ntp_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class VmwareAdminClusterNetworkConfigHostConfigArgs:
    def __init__(
        __self__,
        *,
        dns_search_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ntp_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsSearchDomains")
    def dns_search_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_search_domains.setter
    def dns_search_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ntpServers")
    def ntp_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ntp_servers.setter
    def ntp_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class VmwareAdminClusterNetworkConfigStaticIpConfigArgsDict(TypedDict):
    ip_blocks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class VmwareAdminClusterNetworkConfigStaticIpConfigArgs:
    def __init__(
        __self__,
        *,
        ip_blocks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipBlocks")
    def ip_blocks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockArgs]
            ]
        ]
    ]: ...
    @ip_blocks.setter
    def ip_blocks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockArgs
                    ]
                ]
            ]
        ],
    ): ...

class VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockArgsDict(TypedDict):
    gateway: pulumi.Input[_builtins.str]
    ips: pulumi.Input[
        Sequence[
            pulumi.Input[VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockIpArgsDict]
        ]
    ]
    netmask: pulumi.Input[_builtins.str]

@pulumi.input_type
class VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockArgs:
    def __init__(
        __self__,
        *,
        gateway: pulumi.Input[_builtins.str],
        ips: pulumi.Input[
            Sequence[
                pulumi.Input[VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockIpArgs]
            ]
        ],
        netmask: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> pulumi.Input[_builtins.str]: ...
    @gateway.setter
    def gateway(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def ips(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockIpArgs]
        ]
    ]: ...
    @ips.setter
    def ips(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockIpArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def netmask(self) -> pulumi.Input[_builtins.str]: ...
    @netmask.setter
    def netmask(self, value: pulumi.Input[_builtins.str]): ...

class VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockIpArgsDict(TypedDict):
    ip: pulumi.Input[_builtins.str]
    hostname: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockIpArgs:
    def __init__(
        __self__,
        *,
        ip: pulumi.Input[_builtins.str],
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> pulumi.Input[_builtins.str]: ...
    @ip.setter
    def ip(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterPlatformConfigArgsDict(TypedDict):
    bundles: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigBundleArgsDict]]
        ]
    ]
    platform_version: NotRequired[pulumi.Input[_builtins.str]]
    required_platform_version: NotRequired[pulumi.Input[_builtins.str]]
    statuses: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigStatusArgsDict]]
        ]
    ]

@pulumi.input_type
class VmwareAdminClusterPlatformConfigArgs:
    def __init__(
        __self__,
        *,
        bundles: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigBundleArgs]]
            ]
        ] = ...,
        platform_version: Optional[pulumi.Input[_builtins.str]] = ...,
        required_platform_version: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigStatusArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bundles(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigBundleArgs]]]
    ]: ...
    @bundles.setter
    def bundles(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigBundleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiredPlatformVersion")
    def required_platform_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @required_platform_version.setter
    def required_platform_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigStatusArgs]]]
    ]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigStatusArgs]]
            ]
        ],
    ): ...

class VmwareAdminClusterPlatformConfigBundleArgsDict(TypedDict):
    statuses: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigBundleStatusArgsDict]]
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterPlatformConfigBundleArgs:
    def __init__(
        __self__,
        *,
        statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigBundleStatusArgs]]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigBundleStatusArgs]]
        ]
    ]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigBundleStatusArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterPlatformConfigBundleStatusArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    VmwareAdminClusterPlatformConfigBundleStatusConditionArgsDict
                ]
            ]
        ]
    ]
    error_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterPlatformConfigBundleStatusArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        VmwareAdminClusterPlatformConfigBundleStatusConditionArgs
                    ]
                ]
            ]
        ] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[VmwareAdminClusterPlatformConfigBundleStatusConditionArgs]
            ]
        ]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        VmwareAdminClusterPlatformConfigBundleStatusConditionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterPlatformConfigBundleStatusConditionArgsDict(TypedDict):
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterPlatformConfigBundleStatusConditionArgs:
    def __init__(
        __self__,
        *,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterPlatformConfigStatusArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[VmwareAdminClusterPlatformConfigStatusConditionArgsDict]
            ]
        ]
    ]
    error_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterPlatformConfigStatusArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[VmwareAdminClusterPlatformConfigStatusConditionArgs]
                ]
            ]
        ] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VmwareAdminClusterPlatformConfigStatusConditionArgs]]
        ]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[VmwareAdminClusterPlatformConfigStatusConditionArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterPlatformConfigStatusConditionArgsDict(TypedDict):
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterPlatformConfigStatusConditionArgs:
    def __init__(
        __self__,
        *,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterPrivateRegistryConfigArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    ca_cert: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterPrivateRegistryConfigArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_cert: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_cert.setter
    def ca_cert(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterProxyArgsDict(TypedDict):
    url: pulumi.Input[_builtins.str]
    no_proxy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterProxyArgs:
    def __init__(
        __self__,
        *,
        url: pulumi.Input[_builtins.str],
        no_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="noProxy")
    def no_proxy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @no_proxy.setter
    def no_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterStatusArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterStatusConditionArgsDict]]]
    ]
    error_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterStatusArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterStatusConditionArgs]]]
        ] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterStatusConditionArgs]]]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterStatusConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterStatusConditionArgsDict(TypedDict):
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterStatusConditionArgs:
    def __init__(
        __self__,
        *,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmwareAdminClusterVcenterArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    ca_cert_data: NotRequired[pulumi.Input[_builtins.str]]
    cluster: NotRequired[pulumi.Input[_builtins.str]]
    data_disk: NotRequired[pulumi.Input[_builtins.str]]
    datacenter: NotRequired[pulumi.Input[_builtins.str]]
    datastore: NotRequired[pulumi.Input[_builtins.str]]
    folder: NotRequired[pulumi.Input[_builtins.str]]
    resource_pool: NotRequired[pulumi.Input[_builtins.str]]
    storage_policy_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmwareAdminClusterVcenterArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_cert_data: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk: Optional[pulumi.Input[_builtins.str]] = ...,
        datacenter: Optional[pulumi.Input[_builtins.str]] = ...,
        datastore: Optional[pulumi.Input[_builtins.str]] = ...,
        folder: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertData")
    def ca_cert_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_cert_data.setter
    def ca_cert_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDisk")
    def data_disk(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_disk.setter
    def data_disk(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datastore.setter
    def datastore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourcePool")
    def resource_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_pool.setter
    def resource_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storagePolicyName")
    def storage_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_policy_name.setter
    def storage_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
