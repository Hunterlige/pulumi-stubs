import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessLevelBasic",
    "AccessLevelBasicCondition",
    "AccessLevelBasicConditionDevicePolicy",
    "AccessLevelBasicConditionDevicePolicyOsConstraint",
    "AccessLevelBasicConditionVpcNetworkSource",
    ...,
    "AccessLevelConditionDevicePolicy",
    "AccessLevelConditionDevicePolicyOsConstraint",
    "AccessLevelConditionVpcNetworkSource",
    "AccessLevelConditionVpcNetworkSourceVpcSubnetwork",
    "AccessLevelCustom",
    "AccessLevelCustomExpr",
    "AccessLevelsAccessLevel",
    "AccessLevelsAccessLevelBasic",
    "AccessLevelsAccessLevelBasicCondition",
    "AccessLevelsAccessLevelBasicConditionDevicePolicy",
    ...,
    ...,
    ...,
    "AccessLevelsAccessLevelCustom",
    "AccessLevelsAccessLevelCustomExpr",
    "AccessPolicyIamBindingCondition",
    "AccessPolicyIamMemberCondition",
    "GcpUserAccessBindingScopedAccessSetting",
    ...,
    ...,
    ...,
    "GcpUserAccessBindingScopedAccessSettingScope",
    ...,
    ...,
    "GcpUserAccessBindingSessionSettings",
    "ServicePerimeterDryRunEgressPolicyEgressFrom",
    "ServicePerimeterDryRunEgressPolicyEgressFromSource",
    "ServicePerimeterDryRunEgressPolicyEgressTo",
    ...,
    ...,
    "ServicePerimeterDryRunIngressPolicyIngressFrom",
    ...,
    "ServicePerimeterDryRunIngressPolicyIngressTo",
    ...,
    ...,
    "ServicePerimeterEgressPolicyEgressFrom",
    "ServicePerimeterEgressPolicyEgressFromSource",
    "ServicePerimeterEgressPolicyEgressTo",
    "ServicePerimeterEgressPolicyEgressToOperation",
    ...,
    "ServicePerimeterIngressPolicyIngressFrom",
    "ServicePerimeterIngressPolicyIngressFromSource",
    "ServicePerimeterIngressPolicyIngressTo",
    "ServicePerimeterIngressPolicyIngressToOperation",
    ...,
    "ServicePerimeterSpec",
    "ServicePerimeterSpecEgressPolicy",
    "ServicePerimeterSpecEgressPolicyEgressFrom",
    "ServicePerimeterSpecEgressPolicyEgressFromSource",
    "ServicePerimeterSpecEgressPolicyEgressTo",
    "ServicePerimeterSpecEgressPolicyEgressToOperation",
    ...,
    "ServicePerimeterSpecIngressPolicy",
    "ServicePerimeterSpecIngressPolicyIngressFrom",
    "ServicePerimeterSpecIngressPolicyIngressFromSource",
    "ServicePerimeterSpecIngressPolicyIngressTo",
    ...,
    ...,
    "ServicePerimeterSpecVpcAccessibleServices",
    "ServicePerimeterStatus",
    "ServicePerimeterStatusEgressPolicy",
    "ServicePerimeterStatusEgressPolicyEgressFrom",
    "ServicePerimeterStatusEgressPolicyEgressFromSource",
    "ServicePerimeterStatusEgressPolicyEgressTo",
    ...,
    ...,
    "ServicePerimeterStatusIngressPolicy",
    "ServicePerimeterStatusIngressPolicyIngressFrom",
    ...,
    "ServicePerimeterStatusIngressPolicyIngressTo",
    ...,
    ...,
    "ServicePerimeterStatusVpcAccessibleServices",
    "ServicePerimetersServicePerimeter",
    "ServicePerimetersServicePerimeterSpec",
    "ServicePerimetersServicePerimeterSpecEgressPolicy",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ServicePerimetersServicePerimeterSpecIngressPolicy",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ServicePerimetersServicePerimeterStatus",
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
    "GetSupportedServiceSupportedMethodResult",
    "GetSupportedServicesSupportedServiceResult",
]

@pulumi.output_type
class AccessLevelBasic(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditions: Sequence[outputs.AccessLevelBasicCondition],
        combining_function: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.AccessLevelBasicCondition]: ...
    @_builtins.property
    @pulumi.getter(name="combiningFunction")
    def combining_function(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessLevelBasicCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        device_policy: Optional[outputs.AccessLevelBasicConditionDevicePolicy] = ...,
        ip_subnetworks: Optional[Sequence[_builtins.str]] = ...,
        members: Optional[Sequence[_builtins.str]] = ...,
        negate: Optional[_builtins.bool] = ...,
        regions: Optional[Sequence[_builtins.str]] = ...,
        required_access_levels: Optional[Sequence[_builtins.str]] = ...,
        vpc_network_sources: Optional[
            Sequence[outputs.AccessLevelBasicConditionVpcNetworkSource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="devicePolicy")
    def device_policy(
        self,
    ) -> Optional[outputs.AccessLevelBasicConditionDevicePolicy]: ...
    @_builtins.property
    @pulumi.getter(name="ipSubnetworks")
    def ip_subnetworks(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def negate(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requiredAccessLevels")
    def required_access_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcNetworkSources")
    def vpc_network_sources(
        self,
    ) -> Optional[Sequence[outputs.AccessLevelBasicConditionVpcNetworkSource]]: ...

@pulumi.output_type
class AccessLevelBasicConditionDevicePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_device_management_levels: Optional[Sequence[_builtins.str]] = ...,
        allowed_encryption_statuses: Optional[Sequence[_builtins.str]] = ...,
        os_constraints: Optional[
            Sequence[outputs.AccessLevelBasicConditionDevicePolicyOsConstraint]
        ] = ...,
        require_admin_approval: Optional[_builtins.bool] = ...,
        require_corp_owned: Optional[_builtins.bool] = ...,
        require_screen_lock: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedDeviceManagementLevels")
    def allowed_device_management_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedEncryptionStatuses")
    def allowed_encryption_statuses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="osConstraints")
    def os_constraints(
        self,
    ) -> Optional[
        Sequence[outputs.AccessLevelBasicConditionDevicePolicyOsConstraint]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requireAdminApproval")
    def require_admin_approval(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="requireCorpOwned")
    def require_corp_owned(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="requireScreenLock")
    def require_screen_lock(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AccessLevelBasicConditionDevicePolicyOsConstraint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_type: _builtins.str,
        minimum_version: Optional[_builtins.str] = ...,
        require_verified_chrome_os: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumVersion")
    def minimum_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requireVerifiedChromeOs")
    def require_verified_chrome_os(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AccessLevelBasicConditionVpcNetworkSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        vpc_subnetwork: Optional[
            outputs.AccessLevelBasicConditionVpcNetworkSourceVpcSubnetwork
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetwork")
    def vpc_subnetwork(
        self,
    ) -> Optional[outputs.AccessLevelBasicConditionVpcNetworkSourceVpcSubnetwork]: ...

@pulumi.output_type
class AccessLevelBasicConditionVpcNetworkSourceVpcSubnetwork(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network: _builtins.str,
        vpc_ip_subnetworks: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcIpSubnetworks")
    def vpc_ip_subnetworks(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AccessLevelConditionDevicePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_device_management_levels: Optional[Sequence[_builtins.str]] = ...,
        allowed_encryption_statuses: Optional[Sequence[_builtins.str]] = ...,
        os_constraints: Optional[
            Sequence[outputs.AccessLevelConditionDevicePolicyOsConstraint]
        ] = ...,
        require_admin_approval: Optional[_builtins.bool] = ...,
        require_corp_owned: Optional[_builtins.bool] = ...,
        require_screen_lock: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedDeviceManagementLevels")
    def allowed_device_management_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedEncryptionStatuses")
    def allowed_encryption_statuses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="osConstraints")
    def os_constraints(
        self,
    ) -> Optional[Sequence[outputs.AccessLevelConditionDevicePolicyOsConstraint]]: ...
    @_builtins.property
    @pulumi.getter(name="requireAdminApproval")
    def require_admin_approval(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="requireCorpOwned")
    def require_corp_owned(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="requireScreenLock")
    def require_screen_lock(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AccessLevelConditionDevicePolicyOsConstraint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_type: _builtins.str,
        minimum_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumVersion")
    def minimum_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessLevelConditionVpcNetworkSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        vpc_subnetwork: Optional[
            outputs.AccessLevelConditionVpcNetworkSourceVpcSubnetwork
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetwork")
    def vpc_subnetwork(
        self,
    ) -> Optional[outputs.AccessLevelConditionVpcNetworkSourceVpcSubnetwork]: ...

@pulumi.output_type
class AccessLevelConditionVpcNetworkSourceVpcSubnetwork(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network: _builtins.str,
        vpc_ip_subnetworks: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcIpSubnetworks")
    def vpc_ip_subnetworks(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AccessLevelCustom(dict):
    def __init__(__self__, *, expr: outputs.AccessLevelCustomExpr) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expr(self) -> outputs.AccessLevelCustomExpr: ...

@pulumi.output_type
class AccessLevelCustomExpr(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessLevelsAccessLevel(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        title: _builtins.str,
        basic: Optional[outputs.AccessLevelsAccessLevelBasic] = ...,
        custom: Optional[outputs.AccessLevelsAccessLevelCustom] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def basic(self) -> Optional[outputs.AccessLevelsAccessLevelBasic]: ...
    @_builtins.property
    @pulumi.getter
    def custom(self) -> Optional[outputs.AccessLevelsAccessLevelCustom]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessLevelsAccessLevelBasic(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditions: Sequence[outputs.AccessLevelsAccessLevelBasicCondition],
        combining_function: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.AccessLevelsAccessLevelBasicCondition]: ...
    @_builtins.property
    @pulumi.getter(name="combiningFunction")
    def combining_function(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessLevelsAccessLevelBasicCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        device_policy: Optional[
            outputs.AccessLevelsAccessLevelBasicConditionDevicePolicy
        ] = ...,
        ip_subnetworks: Optional[Sequence[_builtins.str]] = ...,
        members: Optional[Sequence[_builtins.str]] = ...,
        negate: Optional[_builtins.bool] = ...,
        regions: Optional[Sequence[_builtins.str]] = ...,
        required_access_levels: Optional[Sequence[_builtins.str]] = ...,
        vpc_network_sources: Optional[
            Sequence[outputs.AccessLevelsAccessLevelBasicConditionVpcNetworkSource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="devicePolicy")
    def device_policy(
        self,
    ) -> Optional[outputs.AccessLevelsAccessLevelBasicConditionDevicePolicy]: ...
    @_builtins.property
    @pulumi.getter(name="ipSubnetworks")
    def ip_subnetworks(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def negate(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requiredAccessLevels")
    def required_access_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcNetworkSources")
    def vpc_network_sources(
        self,
    ) -> Optional[
        Sequence[outputs.AccessLevelsAccessLevelBasicConditionVpcNetworkSource]
    ]: ...

@pulumi.output_type
class AccessLevelsAccessLevelBasicConditionDevicePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_device_management_levels: Optional[Sequence[_builtins.str]] = ...,
        allowed_encryption_statuses: Optional[Sequence[_builtins.str]] = ...,
        os_constraints: Optional[
            Sequence[
                outputs.AccessLevelsAccessLevelBasicConditionDevicePolicyOsConstraint
            ]
        ] = ...,
        require_admin_approval: Optional[_builtins.bool] = ...,
        require_corp_owned: Optional[_builtins.bool] = ...,
        require_screen_lock: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedDeviceManagementLevels")
    def allowed_device_management_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedEncryptionStatuses")
    def allowed_encryption_statuses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="osConstraints")
    def os_constraints(
        self,
    ) -> Optional[
        Sequence[outputs.AccessLevelsAccessLevelBasicConditionDevicePolicyOsConstraint]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requireAdminApproval")
    def require_admin_approval(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="requireCorpOwned")
    def require_corp_owned(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="requireScreenLock")
    def require_screen_lock(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AccessLevelsAccessLevelBasicConditionDevicePolicyOsConstraint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_type: _builtins.str,
        minimum_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumVersion")
    def minimum_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessLevelsAccessLevelBasicConditionVpcNetworkSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        vpc_subnetwork: Optional[
            outputs.AccessLevelsAccessLevelBasicConditionVpcNetworkSourceVpcSubnetwork
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetwork")
    def vpc_subnetwork(
        self,
    ) -> Optional[
        outputs.AccessLevelsAccessLevelBasicConditionVpcNetworkSourceVpcSubnetwork
    ]: ...

@pulumi.output_type
class AccessLevelsAccessLevelBasicConditionVpcNetworkSourceVpcSubnetwork(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network: _builtins.str,
        vpc_ip_subnetworks: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcIpSubnetworks")
    def vpc_ip_subnetworks(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AccessLevelsAccessLevelCustom(dict):
    def __init__(
        __self__, *, expr: outputs.AccessLevelsAccessLevelCustomExpr
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expr(self) -> outputs.AccessLevelsAccessLevelCustomExpr: ...

@pulumi.output_type
class AccessLevelsAccessLevelCustomExpr(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessPolicyIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessPolicyIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GcpUserAccessBindingScopedAccessSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        active_settings: Optional[
            outputs.GcpUserAccessBindingScopedAccessSettingActiveSettings
        ] = ...,
        dry_run_settings: Optional[
            outputs.GcpUserAccessBindingScopedAccessSettingDryRunSettings
        ] = ...,
        scope: Optional[outputs.GcpUserAccessBindingScopedAccessSettingScope] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeSettings")
    def active_settings(
        self,
    ) -> Optional[outputs.GcpUserAccessBindingScopedAccessSettingActiveSettings]: ...
    @_builtins.property
    @pulumi.getter(name="dryRunSettings")
    def dry_run_settings(
        self,
    ) -> Optional[outputs.GcpUserAccessBindingScopedAccessSettingDryRunSettings]: ...
    @_builtins.property
    @pulumi.getter
    def scope(
        self,
    ) -> Optional[outputs.GcpUserAccessBindingScopedAccessSettingScope]: ...

@pulumi.output_type
class GcpUserAccessBindingScopedAccessSettingActiveSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_levels: Optional[Sequence[_builtins.str]] = ...,
        session_settings: Optional[
            outputs.GcpUserAccessBindingScopedAccessSettingActiveSettingsSessionSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sessionSettings")
    def session_settings(
        self,
    ) -> Optional[
        outputs.GcpUserAccessBindingScopedAccessSettingActiveSettingsSessionSettings
    ]: ...

@pulumi.output_type
class GcpUserAccessBindingScopedAccessSettingActiveSettingsSessionSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_inactivity: Optional[_builtins.str] = ...,
        session_length: Optional[_builtins.str] = ...,
        session_length_enabled: Optional[_builtins.bool] = ...,
        session_reauth_method: Optional[_builtins.str] = ...,
        use_oidc_max_age: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInactivity")
    def max_inactivity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionLength")
    def session_length(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionLengthEnabled")
    def session_length_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sessionReauthMethod")
    def session_reauth_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useOidcMaxAge")
    def use_oidc_max_age(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GcpUserAccessBindingScopedAccessSettingDryRunSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, access_levels: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GcpUserAccessBindingScopedAccessSettingScope(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_scope: Optional[
            outputs.GcpUserAccessBindingScopedAccessSettingScopeClientScope
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientScope")
    def client_scope(
        self,
    ) -> Optional[outputs.GcpUserAccessBindingScopedAccessSettingScopeClientScope]: ...

@pulumi.output_type
class GcpUserAccessBindingScopedAccessSettingScopeClientScope(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        restricted_client_application: Optional[
            outputs.GcpUserAccessBindingScopedAccessSettingScopeClientScopeRestrictedClientApplication
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="restrictedClientApplication")
    def restricted_client_application(
        self,
    ) -> Optional[
        outputs.GcpUserAccessBindingScopedAccessSettingScopeClientScopeRestrictedClientApplication
    ]: ...

@pulumi.output_type
class GcpUserAccessBindingScopedAccessSettingScopeClientScopeRestrictedClientApplication(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GcpUserAccessBindingSessionSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_inactivity: Optional[_builtins.str] = ...,
        session_length: Optional[_builtins.str] = ...,
        session_length_enabled: Optional[_builtins.bool] = ...,
        session_reauth_method: Optional[_builtins.str] = ...,
        use_oidc_max_age: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInactivity")
    def max_inactivity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionLength")
    def session_length(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionLengthEnabled")
    def session_length_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sessionReauthMethod")
    def session_reauth_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useOidcMaxAge")
    def use_oidc_max_age(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ServicePerimeterDryRunEgressPolicyEgressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        source_restriction: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[outputs.ServicePerimeterDryRunEgressPolicyEgressFromSource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterDryRunEgressPolicyEgressFromSource]
    ]: ...

@pulumi.output_type
class ServicePerimeterDryRunEgressPolicyEgressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterDryRunEgressPolicyEgressTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        external_resources: Optional[Sequence[_builtins.str]] = ...,
        operations: Optional[
            Sequence[outputs.ServicePerimeterDryRunEgressPolicyEgressToOperation]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterDryRunEgressPolicyEgressToOperation]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimeterDryRunEgressPolicyEgressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimeterDryRunEgressPolicyEgressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimeterDryRunEgressPolicyEgressToOperationMethodSelector
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterDryRunEgressPolicyEgressToOperationMethodSelector(dict):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterDryRunIngressPolicyIngressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[outputs.ServicePerimeterDryRunIngressPolicyIngressFromSource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterDryRunIngressPolicyIngressFromSource]
    ]: ...

@pulumi.output_type
class ServicePerimeterDryRunIngressPolicyIngressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterDryRunIngressPolicyIngressTo(dict):
    def __init__(
        __self__,
        *,
        operations: Optional[
            Sequence[outputs.ServicePerimeterDryRunIngressPolicyIngressToOperation]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterDryRunIngressPolicyIngressToOperation]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimeterDryRunIngressPolicyIngressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimeterDryRunIngressPolicyIngressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimeterDryRunIngressPolicyIngressToOperationMethodSelector
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterDryRunIngressPolicyIngressToOperationMethodSelector(dict):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterEgressPolicyEgressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        source_restriction: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[outputs.ServicePerimeterEgressPolicyEgressFromSource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[Sequence[outputs.ServicePerimeterEgressPolicyEgressFromSource]]: ...

@pulumi.output_type
class ServicePerimeterEgressPolicyEgressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterEgressPolicyEgressTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        external_resources: Optional[Sequence[_builtins.str]] = ...,
        operations: Optional[
            Sequence[outputs.ServicePerimeterEgressPolicyEgressToOperation]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[Sequence[outputs.ServicePerimeterEgressPolicyEgressToOperation]]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimeterEgressPolicyEgressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimeterEgressPolicyEgressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterEgressPolicyEgressToOperationMethodSelector]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterEgressPolicyEgressToOperationMethodSelector(dict):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterIngressPolicyIngressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[outputs.ServicePerimeterIngressPolicyIngressFromSource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[Sequence[outputs.ServicePerimeterIngressPolicyIngressFromSource]]: ...

@pulumi.output_type
class ServicePerimeterIngressPolicyIngressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterIngressPolicyIngressTo(dict):
    def __init__(
        __self__,
        *,
        operations: Optional[
            Sequence[outputs.ServicePerimeterIngressPolicyIngressToOperation]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterIngressPolicyIngressToOperation]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimeterIngressPolicyIngressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimeterIngressPolicyIngressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterIngressPolicyIngressToOperationMethodSelector]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterIngressPolicyIngressToOperationMethodSelector(dict):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_levels: Optional[Sequence[_builtins.str]] = ...,
        egress_policies: Optional[
            Sequence[outputs.ServicePerimeterSpecEgressPolicy]
        ] = ...,
        ingress_policies: Optional[
            Sequence[outputs.ServicePerimeterSpecIngressPolicy]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        restricted_services: Optional[Sequence[_builtins.str]] = ...,
        vpc_accessible_services: Optional[
            outputs.ServicePerimeterSpecVpcAccessibleServices
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="egressPolicies")
    def egress_policies(
        self,
    ) -> Optional[Sequence[outputs.ServicePerimeterSpecEgressPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicies")
    def ingress_policies(
        self,
    ) -> Optional[Sequence[outputs.ServicePerimeterSpecIngressPolicy]]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="restrictedServices")
    def restricted_services(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessibleServices")
    def vpc_accessible_services(
        self,
    ) -> Optional[outputs.ServicePerimeterSpecVpcAccessibleServices]: ...

@pulumi.output_type
class ServicePerimeterSpecEgressPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        egress_from: Optional[outputs.ServicePerimeterSpecEgressPolicyEgressFrom] = ...,
        egress_to: Optional[outputs.ServicePerimeterSpecEgressPolicyEgressTo] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> Optional[outputs.ServicePerimeterSpecEgressPolicyEgressFrom]: ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[outputs.ServicePerimeterSpecEgressPolicyEgressTo]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterSpecEgressPolicyEgressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        source_restriction: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[outputs.ServicePerimeterSpecEgressPolicyEgressFromSource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterSpecEgressPolicyEgressFromSource]
    ]: ...

@pulumi.output_type
class ServicePerimeterSpecEgressPolicyEgressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterSpecEgressPolicyEgressTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        external_resources: Optional[Sequence[_builtins.str]] = ...,
        operations: Optional[
            Sequence[outputs.ServicePerimeterSpecEgressPolicyEgressToOperation]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterSpecEgressPolicyEgressToOperation]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimeterSpecEgressPolicyEgressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimeterSpecEgressPolicyEgressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimeterSpecEgressPolicyEgressToOperationMethodSelector
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterSpecEgressPolicyEgressToOperationMethodSelector(dict):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterSpecIngressPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ingress_from: Optional[
            outputs.ServicePerimeterSpecIngressPolicyIngressFrom
        ] = ...,
        ingress_to: Optional[outputs.ServicePerimeterSpecIngressPolicyIngressTo] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> Optional[outputs.ServicePerimeterSpecIngressPolicyIngressFrom]: ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> Optional[outputs.ServicePerimeterSpecIngressPolicyIngressTo]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterSpecIngressPolicyIngressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[outputs.ServicePerimeterSpecIngressPolicyIngressFromSource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterSpecIngressPolicyIngressFromSource]
    ]: ...

@pulumi.output_type
class ServicePerimeterSpecIngressPolicyIngressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterSpecIngressPolicyIngressTo(dict):
    def __init__(
        __self__,
        *,
        operations: Optional[
            Sequence[outputs.ServicePerimeterSpecIngressPolicyIngressToOperation]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterSpecIngressPolicyIngressToOperation]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimeterSpecIngressPolicyIngressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimeterSpecIngressPolicyIngressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimeterSpecIngressPolicyIngressToOperationMethodSelector
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterSpecIngressPolicyIngressToOperationMethodSelector(dict):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterSpecVpcAccessibleServices(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_services: Optional[Sequence[_builtins.str]] = ...,
        enable_restriction: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedServices")
    def allowed_services(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableRestriction")
    def enable_restriction(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ServicePerimeterStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_levels: Optional[Sequence[_builtins.str]] = ...,
        egress_policies: Optional[
            Sequence[outputs.ServicePerimeterStatusEgressPolicy]
        ] = ...,
        ingress_policies: Optional[
            Sequence[outputs.ServicePerimeterStatusIngressPolicy]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        restricted_services: Optional[Sequence[_builtins.str]] = ...,
        vpc_accessible_services: Optional[
            outputs.ServicePerimeterStatusVpcAccessibleServices
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="egressPolicies")
    def egress_policies(
        self,
    ) -> Optional[Sequence[outputs.ServicePerimeterStatusEgressPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicies")
    def ingress_policies(
        self,
    ) -> Optional[Sequence[outputs.ServicePerimeterStatusIngressPolicy]]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="restrictedServices")
    def restricted_services(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessibleServices")
    def vpc_accessible_services(
        self,
    ) -> Optional[outputs.ServicePerimeterStatusVpcAccessibleServices]: ...

@pulumi.output_type
class ServicePerimeterStatusEgressPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        egress_from: Optional[
            outputs.ServicePerimeterStatusEgressPolicyEgressFrom
        ] = ...,
        egress_to: Optional[outputs.ServicePerimeterStatusEgressPolicyEgressTo] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> Optional[outputs.ServicePerimeterStatusEgressPolicyEgressFrom]: ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[outputs.ServicePerimeterStatusEgressPolicyEgressTo]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterStatusEgressPolicyEgressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        source_restriction: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[outputs.ServicePerimeterStatusEgressPolicyEgressFromSource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterStatusEgressPolicyEgressFromSource]
    ]: ...

@pulumi.output_type
class ServicePerimeterStatusEgressPolicyEgressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterStatusEgressPolicyEgressTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        external_resources: Optional[Sequence[_builtins.str]] = ...,
        operations: Optional[
            Sequence[outputs.ServicePerimeterStatusEgressPolicyEgressToOperation]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterStatusEgressPolicyEgressToOperation]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimeterStatusEgressPolicyEgressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimeterStatusEgressPolicyEgressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimeterStatusEgressPolicyEgressToOperationMethodSelector
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterStatusEgressPolicyEgressToOperationMethodSelector(dict):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterStatusIngressPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ingress_from: Optional[
            outputs.ServicePerimeterStatusIngressPolicyIngressFrom
        ] = ...,
        ingress_to: Optional[
            outputs.ServicePerimeterStatusIngressPolicyIngressTo
        ] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> Optional[outputs.ServicePerimeterStatusIngressPolicyIngressFrom]: ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> Optional[outputs.ServicePerimeterStatusIngressPolicyIngressTo]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterStatusIngressPolicyIngressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[outputs.ServicePerimeterStatusIngressPolicyIngressFromSource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterStatusIngressPolicyIngressFromSource]
    ]: ...

@pulumi.output_type
class ServicePerimeterStatusIngressPolicyIngressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterStatusIngressPolicyIngressTo(dict):
    def __init__(
        __self__,
        *,
        operations: Optional[
            Sequence[outputs.ServicePerimeterStatusIngressPolicyIngressToOperation]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimeterStatusIngressPolicyIngressToOperation]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimeterStatusIngressPolicyIngressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimeterStatusIngressPolicyIngressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimeterStatusIngressPolicyIngressToOperationMethodSelector
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterStatusIngressPolicyIngressToOperationMethodSelector(dict):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimeterStatusVpcAccessibleServices(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_services: Optional[Sequence[_builtins.str]] = ...,
        enable_restriction: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedServices")
    def allowed_services(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableRestriction")
    def enable_restriction(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        title: _builtins.str,
        create_time: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        perimeter_type: Optional[_builtins.str] = ...,
        spec: Optional[outputs.ServicePerimetersServicePerimeterSpec] = ...,
        status: Optional[outputs.ServicePerimetersServicePerimeterStatus] = ...,
        update_time: Optional[_builtins.str] = ...,
        use_explicit_dry_run_spec: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="perimeterType")
    def perimeter_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[outputs.ServicePerimetersServicePerimeterSpec]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[outputs.ServicePerimetersServicePerimeterStatus]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useExplicitDryRunSpec")
    def use_explicit_dry_run_spec(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_levels: Optional[Sequence[_builtins.str]] = ...,
        egress_policies: Optional[
            Sequence[outputs.ServicePerimetersServicePerimeterSpecEgressPolicy]
        ] = ...,
        ingress_policies: Optional[
            Sequence[outputs.ServicePerimetersServicePerimeterSpecIngressPolicy]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        restricted_services: Optional[Sequence[_builtins.str]] = ...,
        vpc_accessible_services: Optional[
            outputs.ServicePerimetersServicePerimeterSpecVpcAccessibleServices
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="egressPolicies")
    def egress_policies(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimetersServicePerimeterSpecEgressPolicy]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicies")
    def ingress_policies(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimetersServicePerimeterSpecIngressPolicy]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="restrictedServices")
    def restricted_services(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessibleServices")
    def vpc_accessible_services(
        self,
    ) -> Optional[
        outputs.ServicePerimetersServicePerimeterSpecVpcAccessibleServices
    ]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecEgressPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        egress_from: Optional[
            outputs.ServicePerimetersServicePerimeterSpecEgressPolicyEgressFrom
        ] = ...,
        egress_to: Optional[
            outputs.ServicePerimetersServicePerimeterSpecEgressPolicyEgressTo
        ] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> Optional[
        outputs.ServicePerimetersServicePerimeterSpecEgressPolicyEgressFrom
    ]: ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[
        outputs.ServicePerimetersServicePerimeterSpecEgressPolicyEgressTo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecEgressPolicyEgressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        source_restriction: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromSource
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromSource
        ]
    ]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecEgressPolicyEgressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecEgressPolicyEgressTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        external_resources: Optional[Sequence[_builtins.str]] = ...,
        operations: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperation
            ]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperation
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationMethodSelector
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecEgressPolicyEgressToOperationMethodSelector(
    dict
):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecIngressPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ingress_from: Optional[
            outputs.ServicePerimetersServicePerimeterSpecIngressPolicyIngressFrom
        ] = ...,
        ingress_to: Optional[
            outputs.ServicePerimetersServicePerimeterSpecIngressPolicyIngressTo
        ] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> Optional[
        outputs.ServicePerimetersServicePerimeterSpecIngressPolicyIngressFrom
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> Optional[
        outputs.ServicePerimetersServicePerimeterSpecIngressPolicyIngressTo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecIngressPolicyIngressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromSource
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromSource
        ]
    ]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecIngressPolicyIngressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecIngressPolicyIngressTo(dict):
    def __init__(
        __self__,
        *,
        operations: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperation
            ]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperation
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationMethodSelector
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecIngressPolicyIngressToOperationMethodSelector(
    dict
):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterSpecVpcAccessibleServices(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_services: Optional[Sequence[_builtins.str]] = ...,
        enable_restriction: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedServices")
    def allowed_services(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableRestriction")
    def enable_restriction(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_levels: Optional[Sequence[_builtins.str]] = ...,
        egress_policies: Optional[
            Sequence[outputs.ServicePerimetersServicePerimeterStatusEgressPolicy]
        ] = ...,
        ingress_policies: Optional[
            Sequence[outputs.ServicePerimetersServicePerimeterStatusIngressPolicy]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        restricted_services: Optional[Sequence[_builtins.str]] = ...,
        vpc_accessible_services: Optional[
            outputs.ServicePerimetersServicePerimeterStatusVpcAccessibleServices
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="egressPolicies")
    def egress_policies(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimetersServicePerimeterStatusEgressPolicy]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicies")
    def ingress_policies(
        self,
    ) -> Optional[
        Sequence[outputs.ServicePerimetersServicePerimeterStatusIngressPolicy]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="restrictedServices")
    def restricted_services(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcAccessibleServices")
    def vpc_accessible_services(
        self,
    ) -> Optional[
        outputs.ServicePerimetersServicePerimeterStatusVpcAccessibleServices
    ]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusEgressPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        egress_from: Optional[
            outputs.ServicePerimetersServicePerimeterStatusEgressPolicyEgressFrom
        ] = ...,
        egress_to: Optional[
            outputs.ServicePerimetersServicePerimeterStatusEgressPolicyEgressTo
        ] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> Optional[
        outputs.ServicePerimetersServicePerimeterStatusEgressPolicyEgressFrom
    ]: ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[
        outputs.ServicePerimetersServicePerimeterStatusEgressPolicyEgressTo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusEgressPolicyEgressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        source_restriction: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromSource
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceRestriction")
    def source_restriction(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromSource
        ]
    ]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusEgressPolicyEgressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusEgressPolicyEgressTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        external_resources: Optional[Sequence[_builtins.str]] = ...,
        operations: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperation
            ]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalResources")
    def external_resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperation
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationMethodSelector
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusEgressPolicyEgressToOperationMethodSelector(
    dict
):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusIngressPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ingress_from: Optional[
            outputs.ServicePerimetersServicePerimeterStatusIngressPolicyIngressFrom
        ] = ...,
        ingress_to: Optional[
            outputs.ServicePerimetersServicePerimeterStatusIngressPolicyIngressTo
        ] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> Optional[
        outputs.ServicePerimetersServicePerimeterStatusIngressPolicyIngressFrom
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> Optional[
        outputs.ServicePerimetersServicePerimeterStatusIngressPolicyIngressTo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusIngressPolicyIngressFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identities: Optional[Sequence[_builtins.str]] = ...,
        identity_type: Optional[_builtins.str] = ...,
        sources: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromSource
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromSource
        ]
    ]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusIngressPolicyIngressFromSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_level: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusIngressPolicyIngressTo(dict):
    def __init__(
        __self__,
        *,
        operations: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperation
            ]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperation
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method_selectors: Optional[
            Sequence[
                outputs.ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationMethodSelector
            ]
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="methodSelectors")
    def method_selectors(
        self,
    ) -> Optional[
        Sequence[
            outputs.ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationMethodSelector
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusIngressPolicyIngressToOperationMethodSelector(
    dict
):
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        permission: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePerimetersServicePerimeterStatusVpcAccessibleServices(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_services: Optional[Sequence[_builtins.str]] = ...,
        enable_restriction: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedServices")
    def allowed_services(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableRestriction")
    def enable_restriction(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GetSupportedServiceSupportedMethodResult(dict):
    def __init__(
        __self__, *, method: _builtins.str, permission: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> _builtins.str: ...

@pulumi.output_type
class GetSupportedServicesSupportedServiceResult(dict):
    def __init__(
        __self__,
        *,
        available_on_restricted_vip: _builtins.bool,
        known_limitations: _builtins.bool,
        name: _builtins.str,
        service_support_stage: _builtins.str,
        support_stage: _builtins.str,
        title: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availableOnRestrictedVip")
    def available_on_restricted_vip(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="knownLimitations")
    def known_limitations(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceSupportStage")
    def service_support_stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportStage")
    def support_stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
