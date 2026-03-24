import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TargetSiteArgs", "TargetSite"]

@pulumi.input_type
class TargetSiteArgs:
    def __init__(
        __self__,
        *,
        data_store_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        provided_uri_pattern: pulumi.Input[_builtins.str],
        exact_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreId")
    def data_store_id(self) -> pulumi.Input[_builtins.str]: ...
    @data_store_id.setter
    def data_store_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="providedUriPattern")
    def provided_uri_pattern(self) -> pulumi.Input[_builtins.str]: ...
    @provided_uri_pattern.setter
    def provided_uri_pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exact_match.setter
    def exact_match(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _TargetSiteState:
    def __init__(
        __self__,
        *,
        data_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        exact_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        failure_reasons: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetSiteFailureReasonArgs]]]
        ] = ...,
        generated_uri_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        indexing_status: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        provided_uri_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        root_domain_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        site_verification_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetSiteSiteVerificationInfoArgs]]]
        ] = ...,
        target_site_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreId")
    def data_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_store_id.setter
    def data_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exact_match.setter
    def exact_match(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="failureReasons")
    def failure_reasons(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TargetSiteFailureReasonArgs]]]
    ]: ...
    @failure_reasons.setter
    def failure_reasons(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetSiteFailureReasonArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="generatedUriPattern")
    def generated_uri_pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generated_uri_pattern.setter
    def generated_uri_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="indexingStatus")
    def indexing_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @indexing_status.setter
    def indexing_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="providedUriPattern")
    def provided_uri_pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provided_uri_pattern.setter
    def provided_uri_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootDomainUri")
    def root_domain_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_domain_uri.setter
    def root_domain_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="siteVerificationInfos")
    def site_verification_infos(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TargetSiteSiteVerificationInfoArgs]]]
    ]: ...
    @site_verification_infos.setter
    def site_verification_infos(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetSiteSiteVerificationInfoArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetSiteId")
    def target_site_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_site_id.setter
    def target_site_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:discoveryengine/targetSite:TargetSite")
class TargetSite(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        exact_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        provided_uri_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TargetSiteArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        exact_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        failure_reasons: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TargetSiteFailureReasonArgs, TargetSiteFailureReasonArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        generated_uri_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        indexing_status: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        provided_uri_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        root_domain_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        site_verification_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TargetSiteSiteVerificationInfoArgs,
                            TargetSiteSiteVerificationInfoArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        target_site_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> TargetSite: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreId")
    def data_store_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="failureReasons")
    def failure_reasons(
        self,
    ) -> pulumi.Output[Sequence[outputs.TargetSiteFailureReason]]: ...
    @_builtins.property
    @pulumi.getter(name="generatedUriPattern")
    def generated_uri_pattern(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexingStatus")
    def indexing_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providedUriPattern")
    def provided_uri_pattern(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootDomainUri")
    def root_domain_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="siteVerificationInfos")
    def site_verification_infos(
        self,
    ) -> pulumi.Output[Sequence[outputs.TargetSiteSiteVerificationInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="targetSiteId")
    def target_site_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
