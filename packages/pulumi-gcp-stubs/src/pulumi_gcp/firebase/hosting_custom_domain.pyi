import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["HostingCustomDomainArgs", "HostingCustomDomain"]

@pulumi.input_type
class HostingCustomDomainArgs:
    def __init__(
        __self__,
        *,
        custom_domain: pulumi.Input[_builtins.str],
        site_id: pulumi.Input[_builtins.str],
        cert_preference: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        redirect_target: Optional[pulumi.Input[_builtins.str]] = ...,
        wait_dns_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> pulumi.Input[_builtins.str]: ...
    @custom_domain.setter
    def custom_domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Input[_builtins.str]: ...
    @site_id.setter
    def site_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certPreference")
    def cert_preference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert_preference.setter
    def cert_preference(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redirectTarget")
    def redirect_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redirect_target.setter
    def redirect_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="waitDnsVerification")
    def wait_dns_verification(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_dns_verification.setter
    def wait_dns_verification(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _HostingCustomDomainState:
    def __init__(
        __self__,
        *,
        cert_preference: Optional[pulumi.Input[_builtins.str]] = ...,
        certs: Optional[
            pulumi.Input[Sequence[pulumi.Input[HostingCustomDomainCertArgs]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        host_state: Optional[pulumi.Input[_builtins.str]] = ...,
        issues: Optional[
            pulumi.Input[Sequence[pulumi.Input[HostingCustomDomainIssueArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ownership_state: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        redirect_target: Optional[pulumi.Input[_builtins.str]] = ...,
        required_dns_updates: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[HostingCustomDomainRequiredDnsUpdateArgs]]
            ]
        ] = ...,
        site_id: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        wait_dns_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certPreference")
    def cert_preference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert_preference.setter
    def cert_preference(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def certs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[HostingCustomDomainCertArgs]]]
    ]: ...
    @certs.setter
    def certs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[HostingCustomDomainCertArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_domain.setter
    def custom_domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostState")
    def host_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_state.setter
    def host_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def issues(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[HostingCustomDomainIssueArgs]]]
    ]: ...
    @issues.setter
    def issues(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[HostingCustomDomainIssueArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownershipState")
    def ownership_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ownership_state.setter
    def ownership_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="redirectTarget")
    def redirect_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redirect_target.setter
    def redirect_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiredDnsUpdates")
    def required_dns_updates(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[HostingCustomDomainRequiredDnsUpdateArgs]]]
    ]: ...
    @required_dns_updates.setter
    def required_dns_updates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[HostingCustomDomainRequiredDnsUpdateArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="waitDnsVerification")
    def wait_dns_verification(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_dns_verification.setter
    def wait_dns_verification(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token(...)
class HostingCustomDomain(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cert_preference: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        redirect_target: Optional[pulumi.Input[_builtins.str]] = ...,
        site_id: Optional[pulumi.Input[_builtins.str]] = ...,
        wait_dns_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: HostingCustomDomainArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cert_preference: Optional[pulumi.Input[_builtins.str]] = ...,
        certs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            HostingCustomDomainCertArgs, HostingCustomDomainCertArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        host_state: Optional[pulumi.Input[_builtins.str]] = ...,
        issues: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            HostingCustomDomainIssueArgs,
                            HostingCustomDomainIssueArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ownership_state: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        redirect_target: Optional[pulumi.Input[_builtins.str]] = ...,
        required_dns_updates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            HostingCustomDomainRequiredDnsUpdateArgs,
                            HostingCustomDomainRequiredDnsUpdateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        site_id: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        wait_dns_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> HostingCustomDomain: ...
    @_builtins.property
    @pulumi.getter(name="certPreference")
    def cert_preference(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def certs(self) -> pulumi.Output[Sequence[outputs.HostingCustomDomainCert]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostState")
    def host_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def issues(self) -> pulumi.Output[Sequence[outputs.HostingCustomDomainIssue]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownershipState")
    def ownership_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="redirectTarget")
    def redirect_target(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requiredDnsUpdates")
    def required_dns_updates(
        self,
    ) -> pulumi.Output[Sequence[outputs.HostingCustomDomainRequiredDnsUpdate]]: ...
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="waitDnsVerification")
    def wait_dns_verification(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
