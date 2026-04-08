import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessLevelBasicArgs",
    "AccessLevelBasicArgsDict",
    "AccessLevelBasicConditionArgs",
    "AccessLevelBasicConditionArgsDict",
    "AccessLevelBasicConditionDevicePolicyArgs",
    "AccessLevelBasicConditionDevicePolicyArgsDict",
    ...,
    ...,
    "AccessLevelBasicConditionVpcNetworkSourceArgs",
    "AccessLevelBasicConditionVpcNetworkSourceArgsDict",
    ...,
    ...,
    "AccessLevelConditionDevicePolicyArgs",
    "AccessLevelConditionDevicePolicyArgsDict",
    "AccessLevelConditionDevicePolicyOsConstraintArgs",
    ...,
    "AccessLevelConditionVpcNetworkSourceArgs",
    "AccessLevelConditionVpcNetworkSourceArgsDict",
    ...,
    ...,
    "AccessLevelCustomArgs",
    "AccessLevelCustomArgsDict",
    "AccessLevelCustomExprArgs",
    "AccessLevelCustomExprArgsDict",
    "AccessLevelsAccessLevelArgs",
    "AccessLevelsAccessLevelArgsDict",
    "AccessLevelsAccessLevelBasicArgs",
    "AccessLevelsAccessLevelBasicArgsDict",
    "AccessLevelsAccessLevelBasicConditionArgs",
    "AccessLevelsAccessLevelBasicConditionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AccessLevelsAccessLevelCustomArgs",
    "AccessLevelsAccessLevelCustomArgsDict",
    "AccessLevelsAccessLevelCustomExprArgs",
    "AccessLevelsAccessLevelCustomExprArgsDict",
    "AccessPolicyIamBindingConditionArgs",
    "AccessPolicyIamBindingConditionArgsDict",
    "AccessPolicyIamMemberConditionArgs",
    "AccessPolicyIamMemberConditionArgsDict",
    "GcpUserAccessBindingScopedAccessSettingArgs",
    "GcpUserAccessBindingScopedAccessSettingArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GcpUserAccessBindingScopedAccessSettingScopeArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "GcpUserAccessBindingSessionSettingsArgs",
    "GcpUserAccessBindingSessionSettingsArgsDict",
    "ServicePerimeterDryRunEgressPolicyEgressFromArgs",
    ...,
    ...,
    ...,
    "ServicePerimeterDryRunEgressPolicyEgressToArgs",
    "ServicePerimeterDryRunEgressPolicyEgressToArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ServicePerimeterDryRunIngressPolicyIngressFromArgs",
    ...,
    ...,
    ...,
    "ServicePerimeterDryRunIngressPolicyIngressToArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ServicePerimeterEgressPolicyEgressFromArgs",
    "ServicePerimeterEgressPolicyEgressFromArgsDict",
    "ServicePerimeterEgressPolicyEgressFromSourceArgs",
    ...,
    "ServicePerimeterEgressPolicyEgressToArgs",
    "ServicePerimeterEgressPolicyEgressToArgsDict",
    "ServicePerimeterEgressPolicyEgressToOperationArgs",
    ...,
    ...,
    ...,
    "ServicePerimeterIngressPolicyIngressFromArgs",
    "ServicePerimeterIngressPolicyIngressFromArgsDict",
    "ServicePerimeterIngressPolicyIngressFromSourceArgs",
    ...,
    "ServicePerimeterIngressPolicyIngressToArgs",
    "ServicePerimeterIngressPolicyIngressToArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ServicePerimeterSpecArgs",
    "ServicePerimeterSpecArgsDict",
    "ServicePerimeterSpecEgressPolicyArgs",
    "ServicePerimeterSpecEgressPolicyArgsDict",
    "ServicePerimeterSpecEgressPolicyEgressFromArgs",
    "ServicePerimeterSpecEgressPolicyEgressFromArgsDict",
    ...,
    ...,
    "ServicePerimeterSpecEgressPolicyEgressToArgs",
    "ServicePerimeterSpecEgressPolicyEgressToArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ServicePerimeterSpecIngressPolicyArgs",
    "ServicePerimeterSpecIngressPolicyArgsDict",
    "ServicePerimeterSpecIngressPolicyIngressFromArgs",
    ...,
    ...,
    ...,
    "ServicePerimeterSpecIngressPolicyIngressToArgs",
    "ServicePerimeterSpecIngressPolicyIngressToArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ServicePerimeterSpecVpcAccessibleServicesArgs",
    "ServicePerimeterSpecVpcAccessibleServicesArgsDict",
    "ServicePerimeterStatusArgs",
    "ServicePerimeterStatusArgsDict",
    "ServicePerimeterStatusEgressPolicyArgs",
    "ServicePerimeterStatusEgressPolicyArgsDict",
    "ServicePerimeterStatusEgressPolicyEgressFromArgs",
    ...,
    ...,
    ...,
    "ServicePerimeterStatusEgressPolicyEgressToArgs",
    "ServicePerimeterStatusEgressPolicyEgressToArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ServicePerimeterStatusIngressPolicyArgs",
    "ServicePerimeterStatusIngressPolicyArgsDict",
    "ServicePerimeterStatusIngressPolicyIngressFromArgs",
    ...,
    ...,
    ...,
    "ServicePerimeterStatusIngressPolicyIngressToArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ServicePerimeterStatusVpcAccessibleServicesArgs",
    ...,
    "ServicePerimetersServicePerimeterArgs",
    "ServicePerimetersServicePerimeterArgsDict",
    "ServicePerimetersServicePerimeterSpecArgs",
    "ServicePerimetersServicePerimeterSpecArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ServicePerimetersServicePerimeterStatusArgs",
    "ServicePerimetersServicePerimeterStatusArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

class AccessLevelBasicArgsDict(TypedDict):
    conditions: pulumi.Input[Sequence[pulumi.Input[AccessLevelBasicConditionArgsDict]]]
    combining_function: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessLevelBasicArgs:
    def __init__(
        __self__,
        *,
        conditions: pulumi.Input[Sequence[pulumi.Input[AccessLevelBasicConditionArgs]]],
        combining_function: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[AccessLevelBasicConditionArgs]]]: ...
    @conditions.setter
    def conditions(
        self, value: pulumi.Input[Sequence[pulumi.Input[AccessLevelBasicConditionArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="combiningFunction")
    def combining_function(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @combining_function.setter
    def combining_function(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessLevelBasicConditionArgsDict(TypedDict):
    device_policy: NotRequired[
        pulumi.Input[AccessLevelBasicConditionDevicePolicyArgsDict]
    ]
    ip_subnetworks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    members: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate: NotRequired[pulumi.Input[_builtins.bool]]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    required_access_levels: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    vpc_network_sources: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AccessLevelBasicConditionVpcNetworkSourceArgsDict]]
        ]
    ]

@pulumi.input_type
class AccessLevelBasicConditionArgs:
    def __init__(
        __self__,
        *,
        device_policy: Optional[
            pulumi.Input[AccessLevelBasicConditionDevicePolicyArgs]
        ] = ...,
        ip_subnetworks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        negate: Optional[pulumi.Input[_builtins.bool]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        required_access_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_network_sources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AccessLevelBasicConditionVpcNetworkSourceArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="devicePolicy")
    def device_policy(
        self,
    ) -> Optional[pulumi.Input[AccessLevelBasicConditionDevicePolicyArgs]]: ...
    @device_policy.setter
    def device_policy(
        self, value: Optional[pulumi.Input[AccessLevelBasicConditionDevicePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipSubnetworks")
    def ip_subnetworks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_subnetworks.setter
    def ip_subnetworks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @members.setter
    def members(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def negate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @negate.setter
    def negate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredAccessLevels")
    def required_access_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_access_levels.setter
    def required_access_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcNetworkSources")
    def vpc_network_sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AccessLevelBasicConditionVpcNetworkSourceArgs]]
        ]
    ]: ...
    @vpc_network_sources.setter
    def vpc_network_sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AccessLevelBasicConditionVpcNetworkSourceArgs]]
            ]
        ],
    ): ...

class AccessLevelBasicConditionDevicePolicyArgsDict(TypedDict):
    allowed_device_management_levels: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    allowed_encryption_statuses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    os_constraints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AccessLevelBasicConditionDevicePolicyOsConstraintArgsDict]
            ]
        ]
    ]
    require_admin_approval: NotRequired[pulumi.Input[_builtins.bool]]
    require_corp_owned: NotRequired[pulumi.Input[_builtins.bool]]
    require_screen_lock: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AccessLevelBasicConditionDevicePolicyArgs:
    def __init__(
        __self__,
        *,
        allowed_device_management_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_encryption_statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        os_constraints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AccessLevelBasicConditionDevicePolicyOsConstraintArgs]
                ]
            ]
        ] = ...,
        require_admin_approval: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_corp_owned: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_screen_lock: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedDeviceManagementLevels")
    def allowed_device_management_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_device_management_levels.setter
    def allowed_device_management_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedEncryptionStatuses")
    def allowed_encryption_statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_encryption_statuses.setter
    def allowed_encryption_statuses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osConstraints")
    def os_constraints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AccessLevelBasicConditionDevicePolicyOsConstraintArgs]
            ]
        ]
    ]: ...
    @os_constraints.setter
    def os_constraints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AccessLevelBasicConditionDevicePolicyOsConstraintArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireAdminApproval")
    def require_admin_approval(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_admin_approval.setter
    def require_admin_approval(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requireCorpOwned")
    def require_corp_owned(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_corp_owned.setter
    def require_corp_owned(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requireScreenLock")
    def require_screen_lock(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_screen_lock.setter
    def require_screen_lock(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AccessLevelBasicConditionDevicePolicyOsConstraintArgsDict(TypedDict):
    os_type: pulumi.Input[_builtins.str]
    minimum_version: NotRequired[pulumi.Input[_builtins.str]]
    require_verified_chrome_os: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AccessLevelBasicConditionDevicePolicyOsConstraintArgs:
    def __init__(
        __self__,
        *,
        os_type: pulumi.Input[_builtins.str],
        minimum_version: Optional[pulumi.Input[_builtins.str]] = ...,
        require_verified_chrome_os: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[_builtins.str]: ...
    @os_type.setter
    def os_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="minimumVersion")
    def minimum_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_version.setter
    def minimum_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requireVerifiedChromeOs")
    def require_verified_chrome_os(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_verified_chrome_os.setter
    def require_verified_chrome_os(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AccessLevelBasicConditionVpcNetworkSourceArgsDict(TypedDict):
    vpc_subnetwork: NotRequired[
        pulumi.Input[AccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgsDict]
    ]

@pulumi.input_type
class AccessLevelBasicConditionVpcNetworkSourceArgs:
    def __init__(
        __self__,
        *,
        vpc_subnetwork: Optional[
            pulumi.Input[AccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetwork")
    def vpc_subnetwork(
        self,
    ) -> Optional[
        pulumi.Input[AccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgs]
    ]: ...
    @vpc_subnetwork.setter
    def vpc_subnetwork(
        self,
        value: Optional[
            pulumi.Input[AccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgs]
        ],
    ): ...

class AccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]
    vpc_ip_subnetworks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        vpc_ip_subnetworks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcIpSubnetworks")
    def vpc_ip_subnetworks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_ip_subnetworks.setter
    def vpc_ip_subnetworks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AccessLevelConditionDevicePolicyArgsDict(TypedDict):
    allowed_device_management_levels: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    allowed_encryption_statuses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    os_constraints: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AccessLevelConditionDevicePolicyOsConstraintArgsDict]]
        ]
    ]
    require_admin_approval: NotRequired[pulumi.Input[_builtins.bool]]
    require_corp_owned: NotRequired[pulumi.Input[_builtins.bool]]
    require_screen_lock: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AccessLevelConditionDevicePolicyArgs:
    def __init__(
        __self__,
        *,
        allowed_device_management_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_encryption_statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        os_constraints: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AccessLevelConditionDevicePolicyOsConstraintArgs]]
            ]
        ] = ...,
        require_admin_approval: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_corp_owned: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_screen_lock: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedDeviceManagementLevels")
    def allowed_device_management_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_device_management_levels.setter
    def allowed_device_management_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedEncryptionStatuses")
    def allowed_encryption_statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_encryption_statuses.setter
    def allowed_encryption_statuses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osConstraints")
    def os_constraints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AccessLevelConditionDevicePolicyOsConstraintArgs]]
        ]
    ]: ...
    @os_constraints.setter
    def os_constraints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AccessLevelConditionDevicePolicyOsConstraintArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireAdminApproval")
    def require_admin_approval(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_admin_approval.setter
    def require_admin_approval(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requireCorpOwned")
    def require_corp_owned(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_corp_owned.setter
    def require_corp_owned(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requireScreenLock")
    def require_screen_lock(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_screen_lock.setter
    def require_screen_lock(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AccessLevelConditionDevicePolicyOsConstraintArgsDict(TypedDict):
    os_type: pulumi.Input[_builtins.str]
    minimum_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessLevelConditionDevicePolicyOsConstraintArgs:
    def __init__(
        __self__,
        *,
        os_type: pulumi.Input[_builtins.str],
        minimum_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[_builtins.str]: ...
    @os_type.setter
    def os_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="minimumVersion")
    def minimum_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_version.setter
    def minimum_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessLevelConditionVpcNetworkSourceArgsDict(TypedDict):
    vpc_subnetwork: NotRequired[
        pulumi.Input[AccessLevelConditionVpcNetworkSourceVpcSubnetworkArgsDict]
    ]

@pulumi.input_type
class AccessLevelConditionVpcNetworkSourceArgs:
    def __init__(
        __self__,
        *,
        vpc_subnetwork: Optional[
            pulumi.Input[AccessLevelConditionVpcNetworkSourceVpcSubnetworkArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetwork")
    def vpc_subnetwork(
        self,
    ) -> Optional[
        pulumi.Input[AccessLevelConditionVpcNetworkSourceVpcSubnetworkArgs]
    ]: ...
    @vpc_subnetwork.setter
    def vpc_subnetwork(
        self,
        value: Optional[
            pulumi.Input[AccessLevelConditionVpcNetworkSourceVpcSubnetworkArgs]
        ],
    ): ...

class AccessLevelConditionVpcNetworkSourceVpcSubnetworkArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]
    vpc_ip_subnetworks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AccessLevelConditionVpcNetworkSourceVpcSubnetworkArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        vpc_ip_subnetworks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcIpSubnetworks")
    def vpc_ip_subnetworks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_ip_subnetworks.setter
    def vpc_ip_subnetworks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AccessLevelCustomArgsDict(TypedDict):
    expr: pulumi.Input[AccessLevelCustomExprArgsDict]

@pulumi.input_type
class AccessLevelCustomArgs:
    def __init__(
        __self__, *, expr: pulumi.Input[AccessLevelCustomExprArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expr(self) -> pulumi.Input[AccessLevelCustomExprArgs]: ...
    @expr.setter
    def expr(self, value: pulumi.Input[AccessLevelCustomExprArgs]): ...

class AccessLevelCustomExprArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessLevelCustomExprArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessLevelsAccessLevelArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    basic: NotRequired[pulumi.Input[AccessLevelsAccessLevelBasicArgsDict]]
    custom: NotRequired[pulumi.Input[AccessLevelsAccessLevelCustomArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessLevelsAccessLevelArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        basic: Optional[pulumi.Input[AccessLevelsAccessLevelBasicArgs]] = ...,
        custom: Optional[pulumi.Input[AccessLevelsAccessLevelCustomArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def basic(self) -> Optional[pulumi.Input[AccessLevelsAccessLevelBasicArgs]]: ...
    @basic.setter
    def basic(
        self, value: Optional[pulumi.Input[AccessLevelsAccessLevelBasicArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input[AccessLevelsAccessLevelCustomArgs]]: ...
    @custom.setter
    def custom(
        self, value: Optional[pulumi.Input[AccessLevelsAccessLevelCustomArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessLevelsAccessLevelBasicArgsDict(TypedDict):
    conditions: pulumi.Input[
        Sequence[pulumi.Input[AccessLevelsAccessLevelBasicConditionArgsDict]]
    ]
    combining_function: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessLevelsAccessLevelBasicArgs:
    def __init__(
        __self__,
        *,
        conditions: pulumi.Input[
            Sequence[pulumi.Input[AccessLevelsAccessLevelBasicConditionArgs]]
        ],
        combining_function: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[AccessLevelsAccessLevelBasicConditionArgs]]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[AccessLevelsAccessLevelBasicConditionArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="combiningFunction")
    def combining_function(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @combining_function.setter
    def combining_function(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessLevelsAccessLevelBasicConditionArgsDict(TypedDict):
    device_policy: NotRequired[
        pulumi.Input[AccessLevelsAccessLevelBasicConditionDevicePolicyArgsDict]
    ]
    ip_subnetworks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    members: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate: NotRequired[pulumi.Input[_builtins.bool]]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    required_access_levels: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    vpc_network_sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AccessLevelsAccessLevelBasicConditionVpcNetworkSourceArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AccessLevelsAccessLevelBasicConditionArgs:
    def __init__(
        __self__,
        *,
        device_policy: Optional[
            pulumi.Input[AccessLevelsAccessLevelBasicConditionDevicePolicyArgs]
        ] = ...,
        ip_subnetworks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        negate: Optional[pulumi.Input[_builtins.bool]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        required_access_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_network_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AccessLevelsAccessLevelBasicConditionVpcNetworkSourceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="devicePolicy")
    def device_policy(
        self,
    ) -> Optional[
        pulumi.Input[AccessLevelsAccessLevelBasicConditionDevicePolicyArgs]
    ]: ...
    @device_policy.setter
    def device_policy(
        self,
        value: Optional[
            pulumi.Input[AccessLevelsAccessLevelBasicConditionDevicePolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipSubnetworks")
    def ip_subnetworks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_subnetworks.setter
    def ip_subnetworks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @members.setter
    def members(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def negate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @negate.setter
    def negate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredAccessLevels")
    def required_access_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_access_levels.setter
    def required_access_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcNetworkSources")
    def vpc_network_sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AccessLevelsAccessLevelBasicConditionVpcNetworkSourceArgs]
            ]
        ]
    ]: ...
    @vpc_network_sources.setter
    def vpc_network_sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AccessLevelsAccessLevelBasicConditionVpcNetworkSourceArgs
                    ]
                ]
            ]
        ],
    ): ...

class AccessLevelsAccessLevelBasicConditionDevicePolicyArgsDict(TypedDict):
    allowed_device_management_levels: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    allowed_encryption_statuses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    os_constraints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AccessLevelsAccessLevelBasicConditionDevicePolicyOsConstraintArgsDict
                ]
            ]
        ]
    ]
    require_admin_approval: NotRequired[pulumi.Input[_builtins.bool]]
    require_corp_owned: NotRequired[pulumi.Input[_builtins.bool]]
    require_screen_lock: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AccessLevelsAccessLevelBasicConditionDevicePolicyArgs:
    def __init__(
        __self__,
        *,
        allowed_device_management_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_encryption_statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        os_constraints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AccessLevelsAccessLevelBasicConditionDevicePolicyOsConstraintArgs
                    ]
                ]
            ]
        ] = ...,
        require_admin_approval: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_corp_owned: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_screen_lock: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedDeviceManagementLevels")
    def allowed_device_management_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_device_management_levels.setter
    def allowed_device_management_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedEncryptionStatuses")
    def allowed_encryption_statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_encryption_statuses.setter
    def allowed_encryption_statuses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osConstraints")
    def os_constraints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AccessLevelsAccessLevelBasicConditionDevicePolicyOsConstraintArgs
                ]
            ]
        ]
    ]: ...
    @os_constraints.setter
    def os_constraints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AccessLevelsAccessLevelBasicConditionDevicePolicyOsConstraintArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireAdminApproval")
    def require_admin_approval(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_admin_approval.setter
    def require_admin_approval(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requireCorpOwned")
    def require_corp_owned(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_corp_owned.setter
    def require_corp_owned(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requireScreenLock")
    def require_screen_lock(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_screen_lock.setter
    def require_screen_lock(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AccessLevelsAccessLevelBasicConditionDevicePolicyOsConstraintArgsDict(TypedDict):
    os_type: pulumi.Input[_builtins.str]
    minimum_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessLevelsAccessLevelBasicConditionDevicePolicyOsConstraintArgs:
    def __init__(
        __self__,
        *,
        os_type: pulumi.Input[_builtins.str],
        minimum_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[_builtins.str]: ...
    @os_type.setter
    def os_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="minimumVersion")
    def minimum_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_version.setter
    def minimum_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessLevelsAccessLevelBasicConditionVpcNetworkSourceArgsDict(TypedDict):
    vpc_subnetwork: NotRequired[
        pulumi.Input[
            AccessLevelsAccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgsDict
        ]
    ]

@pulumi.input_type
class AccessLevelsAccessLevelBasicConditionVpcNetworkSourceArgs:
    def __init__(
        __self__,
        *,
        vpc_subnetwork: Optional[
            pulumi.Input[
                AccessLevelsAccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetwork")
    def vpc_subnetwork(
        self,
    ) -> Optional[
        pulumi.Input[
            AccessLevelsAccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgs
        ]
    ]: ...
    @vpc_subnetwork.setter
    def vpc_subnetwork(
        self,
        value: Optional[
            pulumi.Input[
                AccessLevelsAccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgs
            ]
        ],
    ): ...

class AccessLevelsAccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgsDict(
    TypedDict
):
    network: pulumi.Input[_builtins.str]
    vpc_ip_subnetworks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AccessLevelsAccessLevelBasicConditionVpcNetworkSourceVpcSubnetworkArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        vpc_ip_subnetworks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcIpSubnetworks")
    def vpc_ip_subnetworks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_ip_subnetworks.setter
    def vpc_ip_subnetworks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AccessLevelsAccessLevelCustomArgsDict(TypedDict):
    expr: pulumi.Input[AccessLevelsAccessLevelCustomExprArgsDict]

@pulumi.input_type
class AccessLevelsAccessLevelCustomArgs:
    def __init__(
        __self__, *, expr: pulumi.Input[AccessLevelsAccessLevelCustomExprArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expr(self) -> pulumi.Input[AccessLevelsAccessLevelCustomExprArgs]: ...
    @expr.setter
    def expr(self, value: pulumi.Input[AccessLevelsAccessLevelCustomExprArgs]): ...

class AccessLevelsAccessLevelCustomExprArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessLevelsAccessLevelCustomExprArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessPolicyIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessPolicyIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessPolicyIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessPolicyIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GcpUserAccessBindingScopedAccessSettingArgsDict(TypedDict):
    active_settings: NotRequired[
        pulumi.Input[GcpUserAccessBindingScopedAccessSettingActiveSettingsArgsDict]
    ]
    dry_run_settings: NotRequired[
        pulumi.Input[GcpUserAccessBindingScopedAccessSettingDryRunSettingsArgsDict]
    ]
    scope: NotRequired[
        pulumi.Input[GcpUserAccessBindingScopedAccessSettingScopeArgsDict]
    ]

@pulumi.input_type
class GcpUserAccessBindingScopedAccessSettingArgs:
    def __init__(
        __self__,
        *,
        active_settings: Optional[
            pulumi.Input[GcpUserAccessBindingScopedAccessSettingActiveSettingsArgs]
        ] = ...,
        dry_run_settings: Optional[
            pulumi.Input[GcpUserAccessBindingScopedAccessSettingDryRunSettingsArgs]
        ] = ...,
        scope: Optional[
            pulumi.Input[GcpUserAccessBindingScopedAccessSettingScopeArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeSettings")
    def active_settings(
        self,
    ) -> Optional[
        pulumi.Input[GcpUserAccessBindingScopedAccessSettingActiveSettingsArgs]
    ]: ...
    @active_settings.setter
    def active_settings(
        self,
        value: Optional[
            pulumi.Input[GcpUserAccessBindingScopedAccessSettingActiveSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dryRunSettings")
    def dry_run_settings(
        self,
    ) -> Optional[
        pulumi.Input[GcpUserAccessBindingScopedAccessSettingDryRunSettingsArgs]
    ]: ...
    @dry_run_settings.setter
    def dry_run_settings(
        self,
        value: Optional[
            pulumi.Input[GcpUserAccessBindingScopedAccessSettingDryRunSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(
        self,
    ) -> Optional[pulumi.Input[GcpUserAccessBindingScopedAccessSettingScopeArgs]]: ...
    @scope.setter
    def scope(
        self,
        value: Optional[pulumi.Input[GcpUserAccessBindingScopedAccessSettingScopeArgs]],
    ): ...

class GcpUserAccessBindingScopedAccessSettingActiveSettingsArgsDict(TypedDict):
    access_levels: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    session_settings: NotRequired[
        pulumi.Input[
            GcpUserAccessBindingScopedAccessSettingActiveSettingsSessionSettingsArgsDict
        ]
    ]

@pulumi.input_type
class GcpUserAccessBindingScopedAccessSettingActiveSettingsArgs:
    def __init__(
        __self__,
        *,
        access_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        session_settings: Optional[
            pulumi.Input[
                GcpUserAccessBindingScopedAccessSettingActiveSettingsSessionSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @access_levels.setter
    def access_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sessionSettings")
    def session_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            GcpUserAccessBindingScopedAccessSettingActiveSettingsSessionSettingsArgs
        ]
    ]: ...
    @session_settings.setter
    def session_settings(
        self,
        value: Optional[
            pulumi.Input[
                GcpUserAccessBindingScopedAccessSettingActiveSettingsSessionSettingsArgs
            ]
        ],
    ): ...

class GcpUserAccessBindingScopedAccessSettingActiveSettingsSessionSettingsArgsDict(
    TypedDict
):
    max_inactivity: NotRequired[pulumi.Input[_builtins.str]]
    session_length: NotRequired[pulumi.Input[_builtins.str]]
    session_length_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    session_reauth_method: NotRequired[pulumi.Input[_builtins.str]]
    use_oidc_max_age: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class GcpUserAccessBindingScopedAccessSettingActiveSettingsSessionSettingsArgs:
    def __init__(
        __self__,
        *,
        max_inactivity: Optional[pulumi.Input[_builtins.str]] = ...,
        session_length: Optional[pulumi.Input[_builtins.str]] = ...,
        session_length_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        session_reauth_method: Optional[pulumi.Input[_builtins.str]] = ...,
        use_oidc_max_age: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInactivity")
    def max_inactivity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_inactivity.setter
    def max_inactivity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionLength")
    def session_length(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_length.setter
    def session_length(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionLengthEnabled")
    def session_length_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @session_length_enabled.setter
    def session_length_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionReauthMethod")
    def session_reauth_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_reauth_method.setter
    def session_reauth_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useOidcMaxAge")
    def use_oidc_max_age(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_oidc_max_age.setter
    def use_oidc_max_age(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GcpUserAccessBindingScopedAccessSettingDryRunSettingsArgsDict(TypedDict):
    access_levels: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GcpUserAccessBindingScopedAccessSettingDryRunSettingsArgs:
    def __init__(
        __self__, *, access_levels: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_levels.setter
    def access_levels(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GcpUserAccessBindingScopedAccessSettingScopeArgsDict(TypedDict):
    client_scope: NotRequired[
        pulumi.Input[GcpUserAccessBindingScopedAccessSettingScopeClientScopeArgsDict]
    ]

@pulumi.input_type
class GcpUserAccessBindingScopedAccessSettingScopeArgs:
    def __init__(
        __self__,
        *,
        client_scope: Optional[
            pulumi.Input[GcpUserAccessBindingScopedAccessSettingScopeClientScopeArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientScope")
    def client_scope(
        self,
    ) -> Optional[
        pulumi.Input[GcpUserAccessBindingScopedAccessSettingScopeClientScopeArgs]
    ]: ...
    @client_scope.setter
    def client_scope(
        self,
        value: Optional[
            pulumi.Input[GcpUserAccessBindingScopedAccessSettingScopeClientScopeArgs]
        ],
    ): ...

class GcpUserAccessBindingScopedAccessSettingScopeClientScopeArgsDict(TypedDict):
    restricted_client_application: NotRequired[
        pulumi.Input[
            GcpUserAccessBindingScopedAccessSettingScopeClientScopeRestrictedClientApplicationArgsDict
        ]
    ]

@pulumi.input_type
class GcpUserAccessBindingScopedAccessSettingScopeClientScopeArgs:
    def __init__(
        __self__,
        *,
        restricted_client_application: Optional[
            pulumi.Input[
                GcpUserAccessBindingScopedAccessSettingScopeClientScopeRestrictedClientApplicationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="restrictedClientApplication")
    def restricted_client_application(
        self,
    ) -> Optional[
        pulumi.Input[
            GcpUserAccessBindingScopedAccessSettingScopeClientScopeRestrictedClientApplicationArgs
        ]
    ]: ...
    @restricted_client_application.setter
    def restricted_client_application(
        self,
        value: Optional[
            pulumi.Input[
                GcpUserAccessBindingScopedAccessSettingScopeClientScopeRestrictedClientApplicationArgs
            ]
        ],
    ): ...

class GcpUserAccessBindingScopedAccessSettingScopeClientScopeRestrictedClientApplicationArgsDict(
    TypedDict
):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GcpUserAccessBindingScopedAccessSettingScopeClientScopeRestrictedClientApplicationArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GcpUserAccessBindingSessionSettingsArgsDict(TypedDict):
    max_inactivity: NotRequired[pulumi.Input[_builtins.str]]
    session_length: NotRequired[pulumi.Input[_builtins.str]]
    session_length_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    session_reauth_method: NotRequired[pulumi.Input[_builtins.str]]
    use_oidc_max_age: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class GcpUserAccessBindingSessionSettingsArgs:
    def __init__(
        __self__,
        *,
        max_inactivity: Optional[pulumi.Input[_builtins.str]] = ...,
        session_length: Optional[pulumi.Input[_builtins.str]] = ...,
        session_length_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        session_reauth_method: Optional[pulumi.Input[_builtins.str]] = ...,
        use_oidc_max_age: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInactivity")
    def max_inactivity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_inactivity.setter
    def max_inactivity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionLength")
    def session_length(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_length.setter
    def session_length(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionLengthEnabled")
    def session_length_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @session_length_enabled.setter
    def session_length_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionReauthMethod")
    def session_reauth_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_reauth_method.setter
    def session_reauth_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useOidcMaxAge")
    def use_oidc_max_age(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_oidc_max_age.setter
    def use_oidc_max_age(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServicePerimeterDryRunEgressPolicyEgressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    source_restriction: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressFromSourceArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimeterDryRunEgressPolicyEgressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_restriction: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressFromSourceArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_restriction.setter
    def source_restriction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressFromSourceArgs]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressFromSourceArgs]
                ]
            ]
        ],
    ): ...

class ServicePerimeterDryRunEgressPolicyEgressFromSourceArgsDict(TypedDict):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterDryRunEgressPolicyEgressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterDryRunEgressPolicyEgressToArgsDict(TypedDict):
    external_resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterDryRunEgressPolicyEgressToOperationArgsDict
                ]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimeterDryRunEgressPolicyEgressToArgs:
    def __init__(
        __self__,
        *,
        external_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterDryRunEgressPolicyEgressToOperationArgs
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @external_resources.setter
    def external_resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressToOperationArgs]
            ]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterDryRunEgressPolicyEgressToOperationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimeterDryRunEgressPolicyEgressToOperationArgsDict(TypedDict):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterDryRunEgressPolicyEgressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterDryRunEgressPolicyEgressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterDryRunEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterDryRunEgressPolicyEgressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterDryRunEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterDryRunEgressPolicyEgressToOperationMethodSelectorArgsDict(
    TypedDict
):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterDryRunEgressPolicyEgressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterDryRunIngressPolicyIngressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterDryRunIngressPolicyIngressFromSourceArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimeterDryRunIngressPolicyIngressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterDryRunIngressPolicyIngressFromSourceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterDryRunIngressPolicyIngressFromSourceArgs]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterDryRunIngressPolicyIngressFromSourceArgs
                    ]
                ]
            ]
        ],
    ): ...

class ServicePerimeterDryRunIngressPolicyIngressFromSourceArgsDict(TypedDict):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterDryRunIngressPolicyIngressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterDryRunIngressPolicyIngressToArgsDict(TypedDict):
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterDryRunIngressPolicyIngressToOperationArgsDict
                ]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimeterDryRunIngressPolicyIngressToArgs:
    def __init__(
        __self__,
        *,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterDryRunIngressPolicyIngressToOperationArgs
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterDryRunIngressPolicyIngressToOperationArgs]
            ]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterDryRunIngressPolicyIngressToOperationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimeterDryRunIngressPolicyIngressToOperationArgsDict(TypedDict):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterDryRunIngressPolicyIngressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterDryRunIngressPolicyIngressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterDryRunIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterDryRunIngressPolicyIngressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterDryRunIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterDryRunIngressPolicyIngressToOperationMethodSelectorArgsDict(
    TypedDict
):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterDryRunIngressPolicyIngressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterEgressPolicyEgressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    source_restriction: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServicePerimeterEgressPolicyEgressFromSourceArgsDict]]
        ]
    ]

@pulumi.input_type
class ServicePerimeterEgressPolicyEgressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_restriction: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServicePerimeterEgressPolicyEgressFromSourceArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_restriction.setter
    def source_restriction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServicePerimeterEgressPolicyEgressFromSourceArgs]]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServicePerimeterEgressPolicyEgressFromSourceArgs]]
            ]
        ],
    ): ...

class ServicePerimeterEgressPolicyEgressFromSourceArgsDict(TypedDict):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterEgressPolicyEgressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterEgressPolicyEgressToArgsDict(TypedDict):
    external_resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterEgressPolicyEgressToOperationArgsDict]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimeterEgressPolicyEgressToArgs:
    def __init__(
        __self__,
        *,
        external_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterEgressPolicyEgressToOperationArgs]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @external_resources.setter
    def external_resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServicePerimeterEgressPolicyEgressToOperationArgs]]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterEgressPolicyEgressToOperationArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimeterEgressPolicyEgressToOperationArgsDict(TypedDict):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterEgressPolicyEgressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterEgressPolicyEgressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterEgressPolicyEgressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterEgressPolicyEgressToOperationMethodSelectorArgsDict(TypedDict):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterEgressPolicyEgressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterIngressPolicyIngressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterIngressPolicyIngressFromSourceArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimeterIngressPolicyIngressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterIngressPolicyIngressFromSourceArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServicePerimeterIngressPolicyIngressFromSourceArgs]]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterIngressPolicyIngressFromSourceArgs]
                ]
            ]
        ],
    ): ...

class ServicePerimeterIngressPolicyIngressFromSourceArgsDict(TypedDict):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterIngressPolicyIngressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterIngressPolicyIngressToArgsDict(TypedDict):
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterIngressPolicyIngressToOperationArgsDict]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimeterIngressPolicyIngressToArgs:
    def __init__(
        __self__,
        *,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterIngressPolicyIngressToOperationArgs]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServicePerimeterIngressPolicyIngressToOperationArgs]]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterIngressPolicyIngressToOperationArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimeterIngressPolicyIngressToOperationArgsDict(TypedDict):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterIngressPolicyIngressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterIngressPolicyIngressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterIngressPolicyIngressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterIngressPolicyIngressToOperationMethodSelectorArgsDict(TypedDict):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterIngressPolicyIngressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterSpecArgsDict(TypedDict):
    access_levels: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    egress_policies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServicePerimeterSpecEgressPolicyArgsDict]]]
    ]
    ingress_policies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServicePerimeterSpecIngressPolicyArgsDict]]]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    restricted_services: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    vpc_accessible_services: NotRequired[
        pulumi.Input[ServicePerimeterSpecVpcAccessibleServicesArgsDict]
    ]

@pulumi.input_type
class ServicePerimeterSpecArgs:
    def __init__(
        __self__,
        *,
        access_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        egress_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServicePerimeterSpecEgressPolicyArgs]]]
        ] = ...,
        ingress_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServicePerimeterSpecIngressPolicyArgs]]]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        restricted_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_accessible_services: Optional[
            pulumi.Input[ServicePerimeterSpecVpcAccessibleServicesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @access_levels.setter
    def access_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressPolicies")
    def egress_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServicePerimeterSpecEgressPolicyArgs]]]
    ]: ...
    @egress_policies.setter
    def egress_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServicePerimeterSpecEgressPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicies")
    def ingress_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServicePerimeterSpecIngressPolicyArgs]]]
    ]: ...
    @ingress_policies.setter
    def ingress_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServicePerimeterSpecIngressPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restrictedServices")
    def restricted_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @restricted_services.setter
    def restricted_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessibleServices")
    def vpc_accessible_services(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterSpecVpcAccessibleServicesArgs]]: ...
    @vpc_accessible_services.setter
    def vpc_accessible_services(
        self,
        value: Optional[pulumi.Input[ServicePerimeterSpecVpcAccessibleServicesArgs]],
    ): ...

class ServicePerimeterSpecEgressPolicyArgsDict(TypedDict):
    egress_from: NotRequired[
        pulumi.Input[ServicePerimeterSpecEgressPolicyEgressFromArgsDict]
    ]
    egress_to: NotRequired[
        pulumi.Input[ServicePerimeterSpecEgressPolicyEgressToArgsDict]
    ]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterSpecEgressPolicyArgs:
    def __init__(
        __self__,
        *,
        egress_from: Optional[
            pulumi.Input[ServicePerimeterSpecEgressPolicyEgressFromArgs]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[ServicePerimeterSpecEgressPolicyEgressToArgs]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterSpecEgressPolicyEgressFromArgs]]: ...
    @egress_from.setter
    def egress_from(
        self,
        value: Optional[pulumi.Input[ServicePerimeterSpecEgressPolicyEgressFromArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterSpecEgressPolicyEgressToArgs]]: ...
    @egress_to.setter
    def egress_to(
        self,
        value: Optional[pulumi.Input[ServicePerimeterSpecEgressPolicyEgressToArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterSpecEgressPolicyEgressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    source_restriction: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterSpecEgressPolicyEgressFromSourceArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimeterSpecEgressPolicyEgressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_restriction: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterSpecEgressPolicyEgressFromSourceArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_restriction.setter
    def source_restriction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServicePerimeterSpecEgressPolicyEgressFromSourceArgs]]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterSpecEgressPolicyEgressFromSourceArgs]
                ]
            ]
        ],
    ): ...

class ServicePerimeterSpecEgressPolicyEgressFromSourceArgsDict(TypedDict):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterSpecEgressPolicyEgressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterSpecEgressPolicyEgressToArgsDict(TypedDict):
    external_resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterSpecEgressPolicyEgressToOperationArgsDict]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimeterSpecEgressPolicyEgressToArgs:
    def __init__(
        __self__,
        *,
        external_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterSpecEgressPolicyEgressToOperationArgs]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @external_resources.setter
    def external_resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterSpecEgressPolicyEgressToOperationArgs]
            ]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterSpecEgressPolicyEgressToOperationArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimeterSpecEgressPolicyEgressToOperationArgsDict(TypedDict):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterSpecEgressPolicyEgressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgsDict(
    TypedDict
):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterSpecIngressPolicyArgsDict(TypedDict):
    ingress_from: NotRequired[
        pulumi.Input[ServicePerimeterSpecIngressPolicyIngressFromArgsDict]
    ]
    ingress_to: NotRequired[
        pulumi.Input[ServicePerimeterSpecIngressPolicyIngressToArgsDict]
    ]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterSpecIngressPolicyArgs:
    def __init__(
        __self__,
        *,
        ingress_from: Optional[
            pulumi.Input[ServicePerimeterSpecIngressPolicyIngressFromArgs]
        ] = ...,
        ingress_to: Optional[
            pulumi.Input[ServicePerimeterSpecIngressPolicyIngressToArgs]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterSpecIngressPolicyIngressFromArgs]]: ...
    @ingress_from.setter
    def ingress_from(
        self,
        value: Optional[pulumi.Input[ServicePerimeterSpecIngressPolicyIngressFromArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterSpecIngressPolicyIngressToArgs]]: ...
    @ingress_to.setter
    def ingress_to(
        self,
        value: Optional[pulumi.Input[ServicePerimeterSpecIngressPolicyIngressToArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterSpecIngressPolicyIngressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterSpecIngressPolicyIngressFromSourceArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimeterSpecIngressPolicyIngressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterSpecIngressPolicyIngressFromSourceArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterSpecIngressPolicyIngressFromSourceArgs]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterSpecIngressPolicyIngressFromSourceArgs]
                ]
            ]
        ],
    ): ...

class ServicePerimeterSpecIngressPolicyIngressFromSourceArgsDict(TypedDict):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterSpecIngressPolicyIngressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterSpecIngressPolicyIngressToArgsDict(TypedDict):
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterSpecIngressPolicyIngressToOperationArgsDict
                ]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimeterSpecIngressPolicyIngressToArgs:
    def __init__(
        __self__,
        *,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterSpecIngressPolicyIngressToOperationArgs
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterSpecIngressPolicyIngressToOperationArgs]
            ]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterSpecIngressPolicyIngressToOperationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimeterSpecIngressPolicyIngressToOperationArgsDict(TypedDict):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterSpecIngressPolicyIngressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgsDict(
    TypedDict
):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterSpecVpcAccessibleServicesArgsDict(TypedDict):
    allowed_services: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enable_restriction: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServicePerimeterSpecVpcAccessibleServicesArgs:
    def __init__(
        __self__,
        *,
        allowed_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_restriction: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedServices")
    def allowed_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_services.setter
    def allowed_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableRestriction")
    def enable_restriction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_restriction.setter
    def enable_restriction(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServicePerimeterStatusArgsDict(TypedDict):
    access_levels: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    egress_policies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServicePerimeterStatusEgressPolicyArgsDict]]]
    ]
    ingress_policies: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServicePerimeterStatusIngressPolicyArgsDict]]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    restricted_services: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    vpc_accessible_services: NotRequired[
        pulumi.Input[ServicePerimeterStatusVpcAccessibleServicesArgsDict]
    ]

@pulumi.input_type
class ServicePerimeterStatusArgs:
    def __init__(
        __self__,
        *,
        access_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        egress_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServicePerimeterStatusEgressPolicyArgs]]]
        ] = ...,
        ingress_policies: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServicePerimeterStatusIngressPolicyArgs]]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        restricted_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_accessible_services: Optional[
            pulumi.Input[ServicePerimeterStatusVpcAccessibleServicesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @access_levels.setter
    def access_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressPolicies")
    def egress_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServicePerimeterStatusEgressPolicyArgs]]]
    ]: ...
    @egress_policies.setter
    def egress_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServicePerimeterStatusEgressPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicies")
    def ingress_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServicePerimeterStatusIngressPolicyArgs]]]
    ]: ...
    @ingress_policies.setter
    def ingress_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServicePerimeterStatusIngressPolicyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restrictedServices")
    def restricted_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @restricted_services.setter
    def restricted_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessibleServices")
    def vpc_accessible_services(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterStatusVpcAccessibleServicesArgs]]: ...
    @vpc_accessible_services.setter
    def vpc_accessible_services(
        self,
        value: Optional[pulumi.Input[ServicePerimeterStatusVpcAccessibleServicesArgs]],
    ): ...

class ServicePerimeterStatusEgressPolicyArgsDict(TypedDict):
    egress_from: NotRequired[
        pulumi.Input[ServicePerimeterStatusEgressPolicyEgressFromArgsDict]
    ]
    egress_to: NotRequired[
        pulumi.Input[ServicePerimeterStatusEgressPolicyEgressToArgsDict]
    ]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterStatusEgressPolicyArgs:
    def __init__(
        __self__,
        *,
        egress_from: Optional[
            pulumi.Input[ServicePerimeterStatusEgressPolicyEgressFromArgs]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[ServicePerimeterStatusEgressPolicyEgressToArgs]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterStatusEgressPolicyEgressFromArgs]]: ...
    @egress_from.setter
    def egress_from(
        self,
        value: Optional[pulumi.Input[ServicePerimeterStatusEgressPolicyEgressFromArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterStatusEgressPolicyEgressToArgs]]: ...
    @egress_to.setter
    def egress_to(
        self,
        value: Optional[pulumi.Input[ServicePerimeterStatusEgressPolicyEgressToArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterStatusEgressPolicyEgressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    source_restriction: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterStatusEgressPolicyEgressFromSourceArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimeterStatusEgressPolicyEgressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_restriction: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterStatusEgressPolicyEgressFromSourceArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_restriction.setter
    def source_restriction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterStatusEgressPolicyEgressFromSourceArgs]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimeterStatusEgressPolicyEgressFromSourceArgs]
                ]
            ]
        ],
    ): ...

class ServicePerimeterStatusEgressPolicyEgressFromSourceArgsDict(TypedDict):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterStatusEgressPolicyEgressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterStatusEgressPolicyEgressToArgsDict(TypedDict):
    external_resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterStatusEgressPolicyEgressToOperationArgsDict
                ]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimeterStatusEgressPolicyEgressToArgs:
    def __init__(
        __self__,
        *,
        external_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterStatusEgressPolicyEgressToOperationArgs
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @external_resources.setter
    def external_resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterStatusEgressPolicyEgressToOperationArgs]
            ]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterStatusEgressPolicyEgressToOperationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimeterStatusEgressPolicyEgressToOperationArgsDict(TypedDict):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterStatusEgressPolicyEgressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgsDict(
    TypedDict
):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterStatusIngressPolicyArgsDict(TypedDict):
    ingress_from: NotRequired[
        pulumi.Input[ServicePerimeterStatusIngressPolicyIngressFromArgsDict]
    ]
    ingress_to: NotRequired[
        pulumi.Input[ServicePerimeterStatusIngressPolicyIngressToArgsDict]
    ]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterStatusIngressPolicyArgs:
    def __init__(
        __self__,
        *,
        ingress_from: Optional[
            pulumi.Input[ServicePerimeterStatusIngressPolicyIngressFromArgs]
        ] = ...,
        ingress_to: Optional[
            pulumi.Input[ServicePerimeterStatusIngressPolicyIngressToArgs]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterStatusIngressPolicyIngressFromArgs]]: ...
    @ingress_from.setter
    def ingress_from(
        self,
        value: Optional[
            pulumi.Input[ServicePerimeterStatusIngressPolicyIngressFromArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterStatusIngressPolicyIngressToArgs]]: ...
    @ingress_to.setter
    def ingress_to(
        self,
        value: Optional[pulumi.Input[ServicePerimeterStatusIngressPolicyIngressToArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterStatusIngressPolicyIngressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterStatusIngressPolicyIngressFromSourceArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimeterStatusIngressPolicyIngressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterStatusIngressPolicyIngressFromSourceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterStatusIngressPolicyIngressFromSourceArgs]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterStatusIngressPolicyIngressFromSourceArgs
                    ]
                ]
            ]
        ],
    ): ...

class ServicePerimeterStatusIngressPolicyIngressFromSourceArgsDict(TypedDict):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterStatusIngressPolicyIngressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterStatusIngressPolicyIngressToArgsDict(TypedDict):
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterStatusIngressPolicyIngressToOperationArgsDict
                ]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimeterStatusIngressPolicyIngressToArgs:
    def __init__(
        __self__,
        *,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterStatusIngressPolicyIngressToOperationArgs
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimeterStatusIngressPolicyIngressToOperationArgs]
            ]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterStatusIngressPolicyIngressToOperationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimeterStatusIngressPolicyIngressToOperationArgsDict(TypedDict):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterStatusIngressPolicyIngressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgsDict(
    TypedDict
):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimeterStatusVpcAccessibleServicesArgsDict(TypedDict):
    allowed_services: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enable_restriction: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServicePerimeterStatusVpcAccessibleServicesArgs:
    def __init__(
        __self__,
        *,
        allowed_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_restriction: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedServices")
    def allowed_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_services.setter
    def allowed_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableRestriction")
    def enable_restriction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_restriction.setter
    def enable_restriction(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServicePerimetersServicePerimeterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    perimeter_type: NotRequired[pulumi.Input[_builtins.str]]
    spec: NotRequired[pulumi.Input[ServicePerimetersServicePerimeterSpecArgsDict]]
    status: NotRequired[pulumi.Input[ServicePerimetersServicePerimeterStatusArgsDict]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    use_explicit_dry_run_spec: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServicePerimetersServicePerimeterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        perimeter_type: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[pulumi.Input[ServicePerimetersServicePerimeterSpecArgs]] = ...,
        status: Optional[
            pulumi.Input[ServicePerimetersServicePerimeterStatusArgs]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        use_explicit_dry_run_spec: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="perimeterType")
    def perimeter_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @perimeter_type.setter
    def perimeter_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def spec(
        self,
    ) -> Optional[pulumi.Input[ServicePerimetersServicePerimeterSpecArgs]]: ...
    @spec.setter
    def spec(
        self, value: Optional[pulumi.Input[ServicePerimetersServicePerimeterSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[ServicePerimetersServicePerimeterStatusArgs]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[ServicePerimetersServicePerimeterStatusArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useExplicitDryRunSpec")
    def use_explicit_dry_run_spec(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_explicit_dry_run_spec.setter
    def use_explicit_dry_run_spec(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ServicePerimetersServicePerimeterSpecArgsDict(TypedDict):
    access_levels: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    egress_policies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimetersServicePerimeterSpecEgressPolicyArgsDict]
            ]
        ]
    ]
    ingress_policies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimetersServicePerimeterSpecIngressPolicyArgsDict]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    restricted_services: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    vpc_accessible_services: NotRequired[
        pulumi.Input[ServicePerimetersServicePerimeterSpecVpcAccessibleServicesArgsDict]
    ]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecArgs:
    def __init__(
        __self__,
        *,
        access_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        egress_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimetersServicePerimeterSpecEgressPolicyArgs]
                ]
            ]
        ] = ...,
        ingress_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimetersServicePerimeterSpecIngressPolicyArgs]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        restricted_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_accessible_services: Optional[
            pulumi.Input[ServicePerimetersServicePerimeterSpecVpcAccessibleServicesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @access_levels.setter
    def access_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressPolicies")
    def egress_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimetersServicePerimeterSpecEgressPolicyArgs]
            ]
        ]
    ]: ...
    @egress_policies.setter
    def egress_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimetersServicePerimeterSpecEgressPolicyArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicies")
    def ingress_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimetersServicePerimeterSpecIngressPolicyArgs]
            ]
        ]
    ]: ...
    @ingress_policies.setter
    def ingress_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ServicePerimetersServicePerimeterSpecIngressPolicyArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restrictedServices")
    def restricted_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @restricted_services.setter
    def restricted_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessibleServices")
    def vpc_accessible_services(
        self,
    ) -> Optional[
        pulumi.Input[ServicePerimetersServicePerimeterSpecVpcAccessibleServicesArgs]
    ]: ...
    @vpc_accessible_services.setter
    def vpc_accessible_services(
        self,
        value: Optional[
            pulumi.Input[ServicePerimetersServicePerimeterSpecVpcAccessibleServicesArgs]
        ],
    ): ...

class ServicePerimetersServicePerimeterSpecEgressPolicyArgsDict(TypedDict):
    egress_from: NotRequired[
        pulumi.Input[
            ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromArgsDict
        ]
    ]
    egress_to: NotRequired[
        pulumi.Input[ServicePerimetersServicePerimeterSpecEgressPolicyEgressToArgsDict]
    ]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecEgressPolicyArgs:
    def __init__(
        __self__,
        *,
        egress_from: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromArgs
            ]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[ServicePerimetersServicePerimeterSpecEgressPolicyEgressToArgs]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> Optional[
        pulumi.Input[ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromArgs]
    ]: ...
    @egress_from.setter
    def egress_from(
        self,
        value: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[
        pulumi.Input[ServicePerimetersServicePerimeterSpecEgressPolicyEgressToArgs]
    ]: ...
    @egress_to.setter
    def egress_to(
        self,
        value: Optional[
            pulumi.Input[ServicePerimetersServicePerimeterSpecEgressPolicyEgressToArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    source_restriction: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromSourceArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_restriction: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromSourceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_restriction.setter
    def source_restriction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromSourceArgs
                ]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromSourceArgs
                    ]
                ]
            ]
        ],
    ): ...

class ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromSourceArgsDict(
    TypedDict
):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterSpecEgressPolicyEgressToArgsDict(TypedDict):
    external_resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationArgsDict
                ]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecEgressPolicyEgressToArgs:
    def __init__(
        __self__,
        *,
        external_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationArgs
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @external_resources.setter
    def external_resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationArgs
                ]
            ]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationArgsDict(
    TypedDict
):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgsDict(
    TypedDict
):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterSpecIngressPolicyArgsDict(TypedDict):
    ingress_from: NotRequired[
        pulumi.Input[
            ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromArgsDict
        ]
    ]
    ingress_to: NotRequired[
        pulumi.Input[
            ServicePerimetersServicePerimeterSpecIngressPolicyIngressToArgsDict
        ]
    ]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecIngressPolicyArgs:
    def __init__(
        __self__,
        *,
        ingress_from: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromArgs
            ]
        ] = ...,
        ingress_to: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterSpecIngressPolicyIngressToArgs
            ]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> Optional[
        pulumi.Input[ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromArgs]
    ]: ...
    @ingress_from.setter
    def ingress_from(
        self,
        value: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> Optional[
        pulumi.Input[ServicePerimetersServicePerimeterSpecIngressPolicyIngressToArgs]
    ]: ...
    @ingress_to.setter
    def ingress_to(
        self,
        value: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterSpecIngressPolicyIngressToArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromSourceArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromSourceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromSourceArgs
                ]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromSourceArgs
                    ]
                ]
            ]
        ],
    ): ...

class ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromSourceArgsDict(
    TypedDict
):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterSpecIngressPolicyIngressToArgsDict(TypedDict):
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationArgsDict
                ]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecIngressPolicyIngressToArgs:
    def __init__(
        __self__,
        *,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationArgs
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationArgs
                ]
            ]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationArgsDict(
    TypedDict
):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgsDict(
    TypedDict
):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterSpecVpcAccessibleServicesArgsDict(TypedDict):
    allowed_services: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enable_restriction: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServicePerimetersServicePerimeterSpecVpcAccessibleServicesArgs:
    def __init__(
        __self__,
        *,
        allowed_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_restriction: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedServices")
    def allowed_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_services.setter
    def allowed_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableRestriction")
    def enable_restriction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_restriction.setter
    def enable_restriction(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServicePerimetersServicePerimeterStatusArgsDict(TypedDict):
    access_levels: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    egress_policies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusEgressPolicyArgsDict
                ]
            ]
        ]
    ]
    ingress_policies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusIngressPolicyArgsDict
                ]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    restricted_services: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    vpc_accessible_services: NotRequired[
        pulumi.Input[
            ServicePerimetersServicePerimeterStatusVpcAccessibleServicesArgsDict
        ]
    ]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusArgs:
    def __init__(
        __self__,
        *,
        access_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        egress_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusEgressPolicyArgs
                    ]
                ]
            ]
        ] = ...,
        ingress_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusIngressPolicyArgs
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        restricted_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_accessible_services: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterStatusVpcAccessibleServicesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @access_levels.setter
    def access_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressPolicies")
    def egress_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimetersServicePerimeterStatusEgressPolicyArgs]
            ]
        ]
    ]: ...
    @egress_policies.setter
    def egress_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusEgressPolicyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicies")
    def ingress_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServicePerimetersServicePerimeterStatusIngressPolicyArgs]
            ]
        ]
    ]: ...
    @ingress_policies.setter
    def ingress_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusIngressPolicyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restrictedServices")
    def restricted_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @restricted_services.setter
    def restricted_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessibleServices")
    def vpc_accessible_services(
        self,
    ) -> Optional[
        pulumi.Input[ServicePerimetersServicePerimeterStatusVpcAccessibleServicesArgs]
    ]: ...
    @vpc_accessible_services.setter
    def vpc_accessible_services(
        self,
        value: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterStatusVpcAccessibleServicesArgs
            ]
        ],
    ): ...

class ServicePerimetersServicePerimeterStatusEgressPolicyArgsDict(TypedDict):
    egress_from: NotRequired[
        pulumi.Input[
            ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromArgsDict
        ]
    ]
    egress_to: NotRequired[
        pulumi.Input[
            ServicePerimetersServicePerimeterStatusEgressPolicyEgressToArgsDict
        ]
    ]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusEgressPolicyArgs:
    def __init__(
        __self__,
        *,
        egress_from: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromArgs
            ]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterStatusEgressPolicyEgressToArgs
            ]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> Optional[
        pulumi.Input[ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromArgs]
    ]: ...
    @egress_from.setter
    def egress_from(
        self,
        value: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[
        pulumi.Input[ServicePerimetersServicePerimeterStatusEgressPolicyEgressToArgs]
    ]: ...
    @egress_to.setter
    def egress_to(
        self,
        value: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterStatusEgressPolicyEgressToArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromArgsDict(TypedDict):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    source_restriction: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromSourceArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_restriction: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromSourceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_restriction.setter
    def source_restriction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromSourceArgs
                ]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromSourceArgs
                    ]
                ]
            ]
        ],
    ): ...

class ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromSourceArgsDict(
    TypedDict
):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterStatusEgressPolicyEgressToArgsDict(TypedDict):
    external_resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationArgsDict
                ]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusEgressPolicyEgressToArgs:
    def __init__(
        __self__,
        *,
        external_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationArgs
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @external_resources.setter
    def external_resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationArgs
                ]
            ]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationArgsDict(
    TypedDict
):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgsDict(
    TypedDict
):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterStatusIngressPolicyArgsDict(TypedDict):
    ingress_from: NotRequired[
        pulumi.Input[
            ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromArgsDict
        ]
    ]
    ingress_to: NotRequired[
        pulumi.Input[
            ServicePerimetersServicePerimeterStatusIngressPolicyIngressToArgsDict
        ]
    ]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusIngressPolicyArgs:
    def __init__(
        __self__,
        *,
        ingress_from: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromArgs
            ]
        ] = ...,
        ingress_to: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterStatusIngressPolicyIngressToArgs
            ]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> Optional[
        pulumi.Input[
            ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromArgs
        ]
    ]: ...
    @ingress_from.setter
    def ingress_from(
        self,
        value: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> Optional[
        pulumi.Input[ServicePerimetersServicePerimeterStatusIngressPolicyIngressToArgs]
    ]: ...
    @ingress_to.setter
    def ingress_to(
        self,
        value: Optional[
            pulumi.Input[
                ServicePerimetersServicePerimeterStatusIngressPolicyIngressToArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromArgsDict(
    TypedDict
):
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity_type: NotRequired[pulumi.Input[_builtins.str]]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromSourceArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromArgs:
    def __init__(
        __self__,
        *,
        identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromSourceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @identities.setter
    def identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromSourceArgs
                ]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromSourceArgs
                    ]
                ]
            ]
        ],
    ): ...

class ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromSourceArgsDict(
    TypedDict
):
    access_level: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromSourceArgs:
    def __init__(
        __self__,
        *,
        access_level: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterStatusIngressPolicyIngressToArgsDict(TypedDict):
    operations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationArgsDict
                ]
            ]
        ]
    ]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusIngressPolicyIngressToArgs:
    def __init__(
        __self__,
        *,
        operations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationArgs
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationArgs
                ]
            ]
        ]
    ]: ...
    @operations.setter
    def operations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationArgsDict(
    TypedDict
):
    method_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgsDict
                ]
            ]
        ]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationArgs:
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgs
                ]
            ]
        ]
    ]: ...
    @method_selectors.setter
    def method_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgsDict(
    TypedDict
):
    method: NotRequired[pulumi.Input[_builtins.str]]
    permission: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationMethodSelectorArgs:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePerimetersServicePerimeterStatusVpcAccessibleServicesArgsDict(TypedDict):
    allowed_services: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enable_restriction: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServicePerimetersServicePerimeterStatusVpcAccessibleServicesArgs:
    def __init__(
        __self__,
        *,
        allowed_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_restriction: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedServices")
    def allowed_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_services.setter
    def allowed_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableRestriction")
    def enable_restriction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_restriction.setter
    def enable_restriction(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
