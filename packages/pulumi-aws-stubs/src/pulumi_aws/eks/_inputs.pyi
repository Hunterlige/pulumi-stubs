import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessPolicyAssociationAccessScopeArgs",
    "AccessPolicyAssociationAccessScopeArgsDict",
    "AddonPodIdentityAssociationArgs",
    "AddonPodIdentityAssociationArgsDict",
    "CapabilityConfigurationArgs",
    "CapabilityConfigurationArgsDict",
    "CapabilityConfigurationArgoCdArgs",
    "CapabilityConfigurationArgoCdArgsDict",
    "CapabilityConfigurationArgoCdAwsIdcArgs",
    "CapabilityConfigurationArgoCdAwsIdcArgsDict",
    "CapabilityConfigurationArgoCdNetworkAccessArgs",
    "CapabilityConfigurationArgoCdNetworkAccessArgsDict",
    "CapabilityConfigurationArgoCdRbacRoleMappingArgs",
    ...,
    ...,
    ...,
    "CapabilityTimeoutsArgs",
    "CapabilityTimeoutsArgsDict",
    "ClusterAccessConfigArgs",
    "ClusterAccessConfigArgsDict",
    "ClusterCertificateAuthorityArgs",
    "ClusterCertificateAuthorityArgsDict",
    "ClusterComputeConfigArgs",
    "ClusterComputeConfigArgsDict",
    "ClusterControlPlaneScalingConfigArgs",
    "ClusterControlPlaneScalingConfigArgsDict",
    "ClusterEncryptionConfigArgs",
    "ClusterEncryptionConfigArgsDict",
    "ClusterEncryptionConfigProviderArgs",
    "ClusterEncryptionConfigProviderArgsDict",
    "ClusterIdentityArgs",
    "ClusterIdentityArgsDict",
    "ClusterIdentityOidcArgs",
    "ClusterIdentityOidcArgsDict",
    "ClusterKubernetesNetworkConfigArgs",
    "ClusterKubernetesNetworkConfigArgsDict",
    ...,
    ...,
    "ClusterOutpostConfigArgs",
    "ClusterOutpostConfigArgsDict",
    "ClusterOutpostConfigControlPlanePlacementArgs",
    "ClusterOutpostConfigControlPlanePlacementArgsDict",
    "ClusterRemoteNetworkConfigArgs",
    "ClusterRemoteNetworkConfigArgsDict",
    "ClusterRemoteNetworkConfigRemoteNodeNetworksArgs",
    ...,
    "ClusterRemoteNetworkConfigRemotePodNetworksArgs",
    ...,
    "ClusterStorageConfigArgs",
    "ClusterStorageConfigArgsDict",
    "ClusterStorageConfigBlockStorageArgs",
    "ClusterStorageConfigBlockStorageArgsDict",
    "ClusterUpgradePolicyArgs",
    "ClusterUpgradePolicyArgsDict",
    "ClusterVpcConfigArgs",
    "ClusterVpcConfigArgsDict",
    "ClusterZonalShiftConfigArgs",
    "ClusterZonalShiftConfigArgsDict",
    "FargateProfileSelectorArgs",
    "FargateProfileSelectorArgsDict",
    "IdentityProviderConfigOidcArgs",
    "IdentityProviderConfigOidcArgsDict",
    "NodeGroupLaunchTemplateArgs",
    "NodeGroupLaunchTemplateArgsDict",
    "NodeGroupNodeRepairConfigArgs",
    "NodeGroupNodeRepairConfigArgsDict",
    ...,
    ...,
    "NodeGroupRemoteAccessArgs",
    "NodeGroupRemoteAccessArgsDict",
    "NodeGroupResourceArgs",
    "NodeGroupResourceArgsDict",
    "NodeGroupResourceAutoscalingGroupArgs",
    "NodeGroupResourceAutoscalingGroupArgsDict",
    "NodeGroupScalingConfigArgs",
    "NodeGroupScalingConfigArgsDict",
    "NodeGroupTaintArgs",
    "NodeGroupTaintArgsDict",
    "NodeGroupUpdateConfigArgs",
    "NodeGroupUpdateConfigArgsDict",
]

class AccessPolicyAssociationAccessScopeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    namespaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AccessPolicyAssociationAccessScopeArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespaces(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @namespaces.setter
    def namespaces(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AddonPodIdentityAssociationArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    service_account: pulumi.Input[_builtins.str]

@pulumi.input_type
class AddonPodIdentityAssociationArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        service_account: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Input[_builtins.str]: ...
    @service_account.setter
    def service_account(self, value: pulumi.Input[_builtins.str]): ...

class CapabilityConfigurationArgsDict(TypedDict):
    argo_cd: NotRequired[pulumi.Input[CapabilityConfigurationArgoCdArgsDict]]

@pulumi.input_type
class CapabilityConfigurationArgs:
    def __init__(
        __self__,
        *,
        argo_cd: Optional[pulumi.Input[CapabilityConfigurationArgoCdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="argoCd")
    def argo_cd(self) -> Optional[pulumi.Input[CapabilityConfigurationArgoCdArgs]]: ...
    @argo_cd.setter
    def argo_cd(
        self, value: Optional[pulumi.Input[CapabilityConfigurationArgoCdArgs]]
    ): ...

class CapabilityConfigurationArgoCdArgsDict(TypedDict):
    aws_idc: pulumi.Input[CapabilityConfigurationArgoCdAwsIdcArgsDict]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    network_access: NotRequired[
        pulumi.Input[CapabilityConfigurationArgoCdNetworkAccessArgsDict]
    ]
    rbac_role_mappings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[CapabilityConfigurationArgoCdRbacRoleMappingArgsDict]]
        ]
    ]
    server_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CapabilityConfigurationArgoCdArgs:
    def __init__(
        __self__,
        *,
        aws_idc: pulumi.Input[CapabilityConfigurationArgoCdAwsIdcArgs],
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        network_access: Optional[
            pulumi.Input[CapabilityConfigurationArgoCdNetworkAccessArgs]
        ] = ...,
        rbac_role_mappings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CapabilityConfigurationArgoCdRbacRoleMappingArgs]]
            ]
        ] = ...,
        server_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsIdc")
    def aws_idc(self) -> pulumi.Input[CapabilityConfigurationArgoCdAwsIdcArgs]: ...
    @aws_idc.setter
    def aws_idc(self, value: pulumi.Input[CapabilityConfigurationArgoCdAwsIdcArgs]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkAccess")
    def network_access(
        self,
    ) -> Optional[pulumi.Input[CapabilityConfigurationArgoCdNetworkAccessArgs]]: ...
    @network_access.setter
    def network_access(
        self,
        value: Optional[pulumi.Input[CapabilityConfigurationArgoCdNetworkAccessArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rbacRoleMappings")
    def rbac_role_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CapabilityConfigurationArgoCdRbacRoleMappingArgs]]
        ]
    ]: ...
    @rbac_role_mappings.setter
    def rbac_role_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CapabilityConfigurationArgoCdRbacRoleMappingArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverUrl")
    def server_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_url.setter
    def server_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CapabilityConfigurationArgoCdAwsIdcArgsDict(TypedDict):
    idc_instance_arn: pulumi.Input[_builtins.str]
    idc_managed_application_arn: NotRequired[pulumi.Input[_builtins.str]]
    idc_region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CapabilityConfigurationArgoCdAwsIdcArgs:
    def __init__(
        __self__,
        *,
        idc_instance_arn: pulumi.Input[_builtins.str],
        idc_managed_application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        idc_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idcInstanceArn")
    def idc_instance_arn(self) -> pulumi.Input[_builtins.str]: ...
    @idc_instance_arn.setter
    def idc_instance_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="idcManagedApplicationArn")
    def idc_managed_application_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idc_managed_application_arn.setter
    def idc_managed_application_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idcRegion")
    def idc_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idc_region.setter
    def idc_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CapabilityConfigurationArgoCdNetworkAccessArgsDict(TypedDict):
    vpce_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CapabilityConfigurationArgoCdNetworkAccessArgs:
    def __init__(
        __self__,
        *,
        vpce_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpceIds")
    def vpce_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpce_ids.setter
    def vpce_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CapabilityConfigurationArgoCdRbacRoleMappingArgsDict(TypedDict):
    identities: pulumi.Input[
        Sequence[
            pulumi.Input[CapabilityConfigurationArgoCdRbacRoleMappingIdentityArgsDict]
        ]
    ]
    role: pulumi.Input[_builtins.str]

@pulumi.input_type
class CapabilityConfigurationArgoCdRbacRoleMappingArgs:
    def __init__(
        __self__,
        *,
        identities: pulumi.Input[
            Sequence[
                pulumi.Input[CapabilityConfigurationArgoCdRbacRoleMappingIdentityArgs]
            ]
        ],
        role: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[CapabilityConfigurationArgoCdRbacRoleMappingIdentityArgs]]
    ]: ...
    @identities.setter
    def identities(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[CapabilityConfigurationArgoCdRbacRoleMappingIdentityArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...

class CapabilityConfigurationArgoCdRbacRoleMappingIdentityArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class CapabilityConfigurationArgoCdRbacRoleMappingIdentityArgs:
    def __init__(
        __self__, *, id: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class CapabilityTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CapabilityTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterAccessConfigArgsDict(TypedDict):
    authentication_mode: NotRequired[pulumi.Input[_builtins.str]]
    bootstrap_cluster_creator_admin_permissions: NotRequired[
        pulumi.Input[_builtins.bool]
    ]

@pulumi.input_type
class ClusterAccessConfigArgs:
    def __init__(
        __self__,
        *,
        authentication_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        bootstrap_cluster_creator_admin_permissions: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_mode.setter
    def authentication_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bootstrapClusterCreatorAdminPermissions")
    def bootstrap_cluster_creator_admin_permissions(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bootstrap_cluster_creator_admin_permissions.setter
    def bootstrap_cluster_creator_admin_permissions(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ClusterCertificateAuthorityArgsDict(TypedDict):
    data: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterCertificateAuthorityArgs:
    def __init__(
        __self__, *, data: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterComputeConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    node_pools: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    node_role_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterComputeConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        node_pools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        node_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="nodePools")
    def node_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @node_pools.setter
    def node_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeRoleArn")
    def node_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_role_arn.setter
    def node_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterControlPlaneScalingConfigArgsDict(TypedDict):
    tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterControlPlaneScalingConfigArgs:
    def __init__(
        __self__, *, tier: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterEncryptionConfigArgsDict(TypedDict):
    provider: pulumi.Input[ClusterEncryptionConfigProviderArgsDict]
    resources: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterEncryptionConfigArgs:
    def __init__(
        __self__,
        *,
        provider: pulumi.Input[ClusterEncryptionConfigProviderArgs],
        resources: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Input[ClusterEncryptionConfigProviderArgs]: ...
    @provider.setter
    def provider(self, value: pulumi.Input[ClusterEncryptionConfigProviderArgs]): ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @resources.setter
    def resources(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ClusterEncryptionConfigProviderArgsDict(TypedDict):
    key_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterEncryptionConfigProviderArgs:
    def __init__(__self__, *, key_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> pulumi.Input[_builtins.str]: ...
    @key_arn.setter
    def key_arn(self, value: pulumi.Input[_builtins.str]): ...

class ClusterIdentityArgsDict(TypedDict):
    oidcs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterIdentityOidcArgsDict]]]
    ]

@pulumi.input_type
class ClusterIdentityArgs:
    def __init__(
        __self__,
        *,
        oidcs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterIdentityOidcArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def oidcs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterIdentityOidcArgs]]]]: ...
    @oidcs.setter
    def oidcs(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterIdentityOidcArgs]]]],
    ): ...

class ClusterIdentityOidcArgsDict(TypedDict):
    issuer: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterIdentityOidcArgs:
    def __init__(
        __self__, *, issuer: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterKubernetesNetworkConfigArgsDict(TypedDict):
    elastic_load_balancing: NotRequired[
        pulumi.Input[ClusterKubernetesNetworkConfigElasticLoadBalancingArgsDict]
    ]
    ip_family: NotRequired[pulumi.Input[_builtins.str]]
    service_ipv4_cidr: NotRequired[pulumi.Input[_builtins.str]]
    service_ipv6_cidr: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterKubernetesNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        elastic_load_balancing: Optional[
            pulumi.Input[ClusterKubernetesNetworkConfigElasticLoadBalancingArgs]
        ] = ...,
        ip_family: Optional[pulumi.Input[_builtins.str]] = ...,
        service_ipv4_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        service_ipv6_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="elasticLoadBalancing")
    def elastic_load_balancing(
        self,
    ) -> Optional[
        pulumi.Input[ClusterKubernetesNetworkConfigElasticLoadBalancingArgs]
    ]: ...
    @elastic_load_balancing.setter
    def elastic_load_balancing(
        self,
        value: Optional[
            pulumi.Input[ClusterKubernetesNetworkConfigElasticLoadBalancingArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipFamily")
    def ip_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_family.setter
    def ip_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceIpv4Cidr")
    def service_ipv4_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_ipv4_cidr.setter
    def service_ipv4_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceIpv6Cidr")
    def service_ipv6_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_ipv6_cidr.setter
    def service_ipv6_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterKubernetesNetworkConfigElasticLoadBalancingArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterKubernetesNetworkConfigElasticLoadBalancingArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterOutpostConfigArgsDict(TypedDict):
    control_plane_instance_type: pulumi.Input[_builtins.str]
    outpost_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    control_plane_placement: NotRequired[
        pulumi.Input[ClusterOutpostConfigControlPlanePlacementArgsDict]
    ]

@pulumi.input_type
class ClusterOutpostConfigArgs:
    def __init__(
        __self__,
        *,
        control_plane_instance_type: pulumi.Input[_builtins.str],
        outpost_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        control_plane_placement: Optional[
            pulumi.Input[ClusterOutpostConfigControlPlanePlacementArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneInstanceType")
    def control_plane_instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @control_plane_instance_type.setter
    def control_plane_instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="outpostArns")
    def outpost_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @outpost_arns.setter
    def outpost_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="controlPlanePlacement")
    def control_plane_placement(
        self,
    ) -> Optional[pulumi.Input[ClusterOutpostConfigControlPlanePlacementArgs]]: ...
    @control_plane_placement.setter
    def control_plane_placement(
        self,
        value: Optional[pulumi.Input[ClusterOutpostConfigControlPlanePlacementArgs]],
    ): ...

class ClusterOutpostConfigControlPlanePlacementArgsDict(TypedDict):
    group_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterOutpostConfigControlPlanePlacementArgs:
    def __init__(__self__, *, group_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[_builtins.str]: ...
    @group_name.setter
    def group_name(self, value: pulumi.Input[_builtins.str]): ...

class ClusterRemoteNetworkConfigArgsDict(TypedDict):
    remote_node_networks: pulumi.Input[
        ClusterRemoteNetworkConfigRemoteNodeNetworksArgsDict
    ]
    remote_pod_networks: NotRequired[
        pulumi.Input[ClusterRemoteNetworkConfigRemotePodNetworksArgsDict]
    ]

@pulumi.input_type
class ClusterRemoteNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        remote_node_networks: pulumi.Input[
            ClusterRemoteNetworkConfigRemoteNodeNetworksArgs
        ],
        remote_pod_networks: Optional[
            pulumi.Input[ClusterRemoteNetworkConfigRemotePodNetworksArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="remoteNodeNetworks")
    def remote_node_networks(
        self,
    ) -> pulumi.Input[ClusterRemoteNetworkConfigRemoteNodeNetworksArgs]: ...
    @remote_node_networks.setter
    def remote_node_networks(
        self, value: pulumi.Input[ClusterRemoteNetworkConfigRemoteNodeNetworksArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="remotePodNetworks")
    def remote_pod_networks(
        self,
    ) -> Optional[pulumi.Input[ClusterRemoteNetworkConfigRemotePodNetworksArgs]]: ...
    @remote_pod_networks.setter
    def remote_pod_networks(
        self,
        value: Optional[pulumi.Input[ClusterRemoteNetworkConfigRemotePodNetworksArgs]],
    ): ...

class ClusterRemoteNetworkConfigRemoteNodeNetworksArgsDict(TypedDict):
    cidrs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterRemoteNetworkConfigRemoteNodeNetworksArgs:
    def __init__(
        __self__,
        *,
        cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidrs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cidrs.setter
    def cidrs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterRemoteNetworkConfigRemotePodNetworksArgsDict(TypedDict):
    cidrs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterRemoteNetworkConfigRemotePodNetworksArgs:
    def __init__(
        __self__,
        *,
        cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidrs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cidrs.setter
    def cidrs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterStorageConfigArgsDict(TypedDict):
    block_storage: NotRequired[pulumi.Input[ClusterStorageConfigBlockStorageArgsDict]]

@pulumi.input_type
class ClusterStorageConfigArgs:
    def __init__(
        __self__,
        *,
        block_storage: Optional[
            pulumi.Input[ClusterStorageConfigBlockStorageArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockStorage")
    def block_storage(
        self,
    ) -> Optional[pulumi.Input[ClusterStorageConfigBlockStorageArgs]]: ...
    @block_storage.setter
    def block_storage(
        self, value: Optional[pulumi.Input[ClusterStorageConfigBlockStorageArgs]]
    ): ...

class ClusterStorageConfigBlockStorageArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterStorageConfigBlockStorageArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterUpgradePolicyArgsDict(TypedDict):
    support_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterUpgradePolicyArgs:
    def __init__(
        __self__, *, support_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="supportType")
    def support_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @support_type.setter
    def support_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterVpcConfigArgsDict(TypedDict):
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    cluster_security_group_id: NotRequired[pulumi.Input[_builtins.str]]
    endpoint_private_access: NotRequired[pulumi.Input[_builtins.bool]]
    endpoint_public_access: NotRequired[pulumi.Input[_builtins.bool]]
    public_access_cidrs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterVpcConfigArgs:
    def __init__(
        __self__,
        *,
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        cluster_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_private_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_public_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        public_access_cidrs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterSecurityGroupId")
    def cluster_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_security_group_id.setter
    def cluster_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointPrivateAccess")
    def endpoint_private_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @endpoint_private_access.setter
    def endpoint_private_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointPublicAccess")
    def endpoint_public_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @endpoint_public_access.setter
    def endpoint_public_access(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="publicAccessCidrs")
    def public_access_cidrs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @public_access_cidrs.setter
    def public_access_cidrs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterZonalShiftConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterZonalShiftConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class FargateProfileSelectorArgsDict(TypedDict):
    namespace: pulumi.Input[_builtins.str]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FargateProfileSelectorArgs:
    def __init__(
        __self__,
        *,
        namespace: pulumi.Input[_builtins.str],
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class IdentityProviderConfigOidcArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    identity_provider_config_name: pulumi.Input[_builtins.str]
    issuer_url: pulumi.Input[_builtins.str]
    groups_claim: NotRequired[pulumi.Input[_builtins.str]]
    groups_prefix: NotRequired[pulumi.Input[_builtins.str]]
    required_claims: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    username_claim: NotRequired[pulumi.Input[_builtins.str]]
    username_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IdentityProviderConfigOidcArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        identity_provider_config_name: pulumi.Input[_builtins.str],
        issuer_url: pulumi.Input[_builtins.str],
        groups_claim: Optional[pulumi.Input[_builtins.str]] = ...,
        groups_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        required_claims: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        username_claim: Optional[pulumi.Input[_builtins.str]] = ...,
        username_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="identityProviderConfigName")
    def identity_provider_config_name(self) -> pulumi.Input[_builtins.str]: ...
    @identity_provider_config_name.setter
    def identity_provider_config_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="issuerUrl")
    def issuer_url(self) -> pulumi.Input[_builtins.str]: ...
    @issuer_url.setter
    def issuer_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupsClaim")
    def groups_claim(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @groups_claim.setter
    def groups_claim(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupsPrefix")
    def groups_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @groups_prefix.setter
    def groups_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiredClaims")
    def required_claims(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @required_claims.setter
    def required_claims(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usernameClaim")
    def username_claim(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username_claim.setter
    def username_claim(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="usernamePrefix")
    def username_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username_prefix.setter
    def username_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodeGroupLaunchTemplateArgsDict(TypedDict):
    version: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodeGroupLaunchTemplateArgs:
    def __init__(
        __self__,
        *,
        version: pulumi.Input[_builtins.str],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodeGroupNodeRepairConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    max_parallel_nodes_repaired_count: NotRequired[pulumi.Input[_builtins.int]]
    max_parallel_nodes_repaired_percentage: NotRequired[pulumi.Input[_builtins.int]]
    max_unhealthy_node_threshold_count: NotRequired[pulumi.Input[_builtins.int]]
    max_unhealthy_node_threshold_percentage: NotRequired[pulumi.Input[_builtins.int]]
    node_repair_config_overrides: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[NodeGroupNodeRepairConfigNodeRepairConfigOverrideArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class NodeGroupNodeRepairConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_parallel_nodes_repaired_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_parallel_nodes_repaired_percentage: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        max_unhealthy_node_threshold_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_unhealthy_node_threshold_percentage: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        node_repair_config_overrides: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[NodeGroupNodeRepairConfigNodeRepairConfigOverrideArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxParallelNodesRepairedCount")
    def max_parallel_nodes_repaired_count(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_parallel_nodes_repaired_count.setter
    def max_parallel_nodes_repaired_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxParallelNodesRepairedPercentage")
    def max_parallel_nodes_repaired_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_parallel_nodes_repaired_percentage.setter
    def max_parallel_nodes_repaired_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyNodeThresholdCount")
    def max_unhealthy_node_threshold_count(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unhealthy_node_threshold_count.setter
    def max_unhealthy_node_threshold_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyNodeThresholdPercentage")
    def max_unhealthy_node_threshold_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unhealthy_node_threshold_percentage.setter
    def max_unhealthy_node_threshold_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeRepairConfigOverrides")
    def node_repair_config_overrides(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[NodeGroupNodeRepairConfigNodeRepairConfigOverrideArgs]
            ]
        ]
    ]: ...
    @node_repair_config_overrides.setter
    def node_repair_config_overrides(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[NodeGroupNodeRepairConfigNodeRepairConfigOverrideArgs]
                ]
            ]
        ],
    ): ...

class NodeGroupNodeRepairConfigNodeRepairConfigOverrideArgsDict(TypedDict):
    min_repair_wait_time_mins: pulumi.Input[_builtins.int]
    node_monitoring_condition: pulumi.Input[_builtins.str]
    node_unhealthy_reason: pulumi.Input[_builtins.str]
    repair_action: pulumi.Input[_builtins.str]

@pulumi.input_type
class NodeGroupNodeRepairConfigNodeRepairConfigOverrideArgs:
    def __init__(
        __self__,
        *,
        min_repair_wait_time_mins: pulumi.Input[_builtins.int],
        node_monitoring_condition: pulumi.Input[_builtins.str],
        node_unhealthy_reason: pulumi.Input[_builtins.str],
        repair_action: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minRepairWaitTimeMins")
    def min_repair_wait_time_mins(self) -> pulumi.Input[_builtins.int]: ...
    @min_repair_wait_time_mins.setter
    def min_repair_wait_time_mins(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="nodeMonitoringCondition")
    def node_monitoring_condition(self) -> pulumi.Input[_builtins.str]: ...
    @node_monitoring_condition.setter
    def node_monitoring_condition(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nodeUnhealthyReason")
    def node_unhealthy_reason(self) -> pulumi.Input[_builtins.str]: ...
    @node_unhealthy_reason.setter
    def node_unhealthy_reason(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repairAction")
    def repair_action(self) -> pulumi.Input[_builtins.str]: ...
    @repair_action.setter
    def repair_action(self, value: pulumi.Input[_builtins.str]): ...

class NodeGroupRemoteAccessArgsDict(TypedDict):
    ec2_ssh_key: NotRequired[pulumi.Input[_builtins.str]]
    source_security_group_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class NodeGroupRemoteAccessArgs:
    def __init__(
        __self__,
        *,
        ec2_ssh_key: Optional[pulumi.Input[_builtins.str]] = ...,
        source_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ec2SshKey")
    def ec2_ssh_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ec2_ssh_key.setter
    def ec2_ssh_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroupIds")
    def source_security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_security_group_ids.setter
    def source_security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class NodeGroupResourceArgsDict(TypedDict):
    autoscaling_groups: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NodeGroupResourceAutoscalingGroupArgsDict]]]
    ]
    remote_access_security_group_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodeGroupResourceArgs:
    def __init__(
        __self__,
        *,
        autoscaling_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodeGroupResourceAutoscalingGroupArgs]]]
        ] = ...,
        remote_access_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingGroups")
    def autoscaling_groups(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NodeGroupResourceAutoscalingGroupArgs]]]
    ]: ...
    @autoscaling_groups.setter
    def autoscaling_groups(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodeGroupResourceAutoscalingGroupArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="remoteAccessSecurityGroupId")
    def remote_access_security_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remote_access_security_group_id.setter
    def remote_access_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class NodeGroupResourceAutoscalingGroupArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodeGroupResourceAutoscalingGroupArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodeGroupScalingConfigArgsDict(TypedDict):
    desired_size: pulumi.Input[_builtins.int]
    max_size: pulumi.Input[_builtins.int]
    min_size: pulumi.Input[_builtins.int]

@pulumi.input_type
class NodeGroupScalingConfigArgs:
    def __init__(
        __self__,
        *,
        desired_size: pulumi.Input[_builtins.int],
        max_size: pulumi.Input[_builtins.int],
        min_size: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredSize")
    def desired_size(self) -> pulumi.Input[_builtins.int]: ...
    @desired_size.setter
    def desired_size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Input[_builtins.int]: ...
    @max_size.setter
    def max_size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Input[_builtins.int]: ...
    @min_size.setter
    def min_size(self, value: pulumi.Input[_builtins.int]): ...

class NodeGroupTaintArgsDict(TypedDict):
    effect: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodeGroupTaintArgs:
    def __init__(
        __self__,
        *,
        effect: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> pulumi.Input[_builtins.str]: ...
    @effect.setter
    def effect(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodeGroupUpdateConfigArgsDict(TypedDict):
    max_unavailable: NotRequired[pulumi.Input[_builtins.int]]
    max_unavailable_percentage: NotRequired[pulumi.Input[_builtins.int]]
    update_strategy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodeGroupUpdateConfigArgs:
    def __init__(
        __self__,
        *,
        max_unavailable: Optional[pulumi.Input[_builtins.int]] = ...,
        max_unavailable_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        update_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unavailable.setter
    def max_unavailable(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailablePercentage")
    def max_unavailable_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unavailable_percentage.setter
    def max_unavailable_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_strategy.setter
    def update_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
