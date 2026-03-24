import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EnterpriseKeyAndroidSettingsArgs",
    "EnterpriseKeyAndroidSettingsArgsDict",
    "EnterpriseKeyIosSettingsArgs",
    "EnterpriseKeyIosSettingsArgsDict",
    "EnterpriseKeyTestingOptionsArgs",
    "EnterpriseKeyTestingOptionsArgsDict",
    "EnterpriseKeyWafSettingsArgs",
    "EnterpriseKeyWafSettingsArgsDict",
    "EnterpriseKeyWebSettingsArgs",
    "EnterpriseKeyWebSettingsArgsDict",
]

class EnterpriseKeyAndroidSettingsArgsDict(TypedDict):
    allow_all_package_names: NotRequired[pulumi.Input[_builtins.bool]]
    allowed_package_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class EnterpriseKeyAndroidSettingsArgs:
    def __init__(
        __self__,
        *,
        allow_all_package_names: Optional[pulumi.Input[_builtins.bool]] = ...,
        allowed_package_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowAllPackageNames")
    def allow_all_package_names(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_all_package_names.setter
    def allow_all_package_names(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedPackageNames")
    def allowed_package_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_package_names.setter
    def allowed_package_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EnterpriseKeyIosSettingsArgsDict(TypedDict):
    allow_all_bundle_ids: NotRequired[pulumi.Input[_builtins.bool]]
    allowed_bundle_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class EnterpriseKeyIosSettingsArgs:
    def __init__(
        __self__,
        *,
        allow_all_bundle_ids: Optional[pulumi.Input[_builtins.bool]] = ...,
        allowed_bundle_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowAllBundleIds")
    def allow_all_bundle_ids(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_all_bundle_ids.setter
    def allow_all_bundle_ids(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowedBundleIds")
    def allowed_bundle_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_bundle_ids.setter
    def allowed_bundle_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EnterpriseKeyTestingOptionsArgsDict(TypedDict):
    testing_challenge: NotRequired[pulumi.Input[_builtins.str]]
    testing_score: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class EnterpriseKeyTestingOptionsArgs:
    def __init__(
        __self__,
        *,
        testing_challenge: Optional[pulumi.Input[_builtins.str]] = ...,
        testing_score: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="testingChallenge")
    def testing_challenge(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @testing_challenge.setter
    def testing_challenge(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="testingScore")
    def testing_score(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @testing_score.setter
    def testing_score(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class EnterpriseKeyWafSettingsArgsDict(TypedDict):
    waf_feature: pulumi.Input[_builtins.str]
    waf_service: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EnterpriseKeyWafSettingsArgs:
    def __init__(
        __self__,
        *,
        waf_feature: pulumi.Input[_builtins.str],
        waf_service: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="wafFeature")
    def waf_feature(self) -> pulumi.Input[_builtins.str]: ...
    @waf_feature.setter
    def waf_feature(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wafService")
    def waf_service(self) -> pulumi.Input[_builtins.str]: ...
    @waf_service.setter
    def waf_service(self, value: pulumi.Input[_builtins.str]): ...

class EnterpriseKeyWebSettingsArgsDict(TypedDict):
    integration_type: pulumi.Input[_builtins.str]
    allow_all_domains: NotRequired[pulumi.Input[_builtins.bool]]
    allow_amp_traffic: NotRequired[pulumi.Input[_builtins.bool]]
    allowed_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    challenge_security_preference: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnterpriseKeyWebSettingsArgs:
    def __init__(
        __self__,
        *,
        integration_type: pulumi.Input[_builtins.str],
        allow_all_domains: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_amp_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        allowed_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        challenge_security_preference: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> pulumi.Input[_builtins.str]: ...
    @integration_type.setter
    def integration_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowAllDomains")
    def allow_all_domains(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_all_domains.setter
    def allow_all_domains(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowAmpTraffic")
    def allow_amp_traffic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_amp_traffic.setter
    def allow_amp_traffic(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowedDomains")
    def allowed_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_domains.setter
    def allowed_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="challengeSecurityPreference")
    def challenge_security_preference(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @challenge_security_preference.setter
    def challenge_security_preference(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
