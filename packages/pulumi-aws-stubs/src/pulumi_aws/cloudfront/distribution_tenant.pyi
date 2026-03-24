import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DistributionTenantArgs", "DistributionTenant"]

@pulumi.input_type
class DistributionTenantArgs:
    def __init__(
        __self__,
        *,
        distribution_id: pulumi.Input[_builtins.str],
        connection_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customizations: Optional[
            pulumi.Input[DistributionTenantCustomizationsArgs]
        ] = ...,
        domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributionTenantDomainArgs]]]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        managed_certificate_request: Optional[
            pulumi.Input[DistributionTenantManagedCertificateRequestArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributionTenantParameterArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[DistributionTenantTimeoutsArgs]] = ...,
        wait_for_deployment: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="distributionId")
    def distribution_id(self) -> pulumi.Input[_builtins.str]: ...
    @distribution_id.setter
    def distribution_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectionGroupId")
    def connection_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_group_id.setter
    def connection_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def customizations(
        self,
    ) -> Optional[pulumi.Input[DistributionTenantCustomizationsArgs]]: ...
    @customizations.setter
    def customizations(
        self, value: Optional[pulumi.Input[DistributionTenantCustomizationsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def domains(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DistributionTenantDomainArgs]]]
    ]: ...
    @domains.setter
    def domains(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributionTenantDomainArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="managedCertificateRequest")
    def managed_certificate_request(
        self,
    ) -> Optional[pulumi.Input[DistributionTenantManagedCertificateRequestArgs]]: ...
    @managed_certificate_request.setter
    def managed_certificate_request(
        self,
        value: Optional[pulumi.Input[DistributionTenantManagedCertificateRequestArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DistributionTenantParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributionTenantParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DistributionTenantTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[DistributionTenantTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitForDeployment")
    def wait_for_deployment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_for_deployment.setter
    def wait_for_deployment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _DistributionTenantState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customizations: Optional[
            pulumi.Input[DistributionTenantCustomizationsArgs]
        ] = ...,
        distribution_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributionTenantDomainArgs]]]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_certificate_request: Optional[
            pulumi.Input[DistributionTenantManagedCertificateRequestArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributionTenantParameterArgs]]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[DistributionTenantTimeoutsArgs]] = ...,
        wait_for_deployment: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionGroupId")
    def connection_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_group_id.setter
    def connection_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def customizations(
        self,
    ) -> Optional[pulumi.Input[DistributionTenantCustomizationsArgs]]: ...
    @customizations.setter
    def customizations(
        self, value: Optional[pulumi.Input[DistributionTenantCustomizationsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="distributionId")
    def distribution_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distribution_id.setter
    def distribution_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domains(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DistributionTenantDomainArgs]]]
    ]: ...
    @domains.setter
    def domains(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributionTenantDomainArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedCertificateRequest")
    def managed_certificate_request(
        self,
    ) -> Optional[pulumi.Input[DistributionTenantManagedCertificateRequestArgs]]: ...
    @managed_certificate_request.setter
    def managed_certificate_request(
        self,
        value: Optional[pulumi.Input[DistributionTenantManagedCertificateRequestArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DistributionTenantParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributionTenantParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DistributionTenantTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[DistributionTenantTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitForDeployment")
    def wait_for_deployment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_for_deployment.setter
    def wait_for_deployment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token(...)
class DistributionTenant(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        connection_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customizations: Optional[
            pulumi.Input[
                Union[
                    DistributionTenantCustomizationsArgs,
                    DistributionTenantCustomizationsArgsDict,
                ]
            ]
        ] = ...,
        distribution_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domains: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DistributionTenantDomainArgs,
                            DistributionTenantDomainArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        managed_certificate_request: Optional[
            pulumi.Input[
                Union[
                    DistributionTenantManagedCertificateRequestArgs,
                    DistributionTenantManagedCertificateRequestArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DistributionTenantParameterArgs,
                            DistributionTenantParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    DistributionTenantTimeoutsArgs, DistributionTenantTimeoutsArgsDict
                ]
            ]
        ] = ...,
        wait_for_deployment: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DistributionTenantArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customizations: Optional[
            pulumi.Input[
                Union[
                    DistributionTenantCustomizationsArgs,
                    DistributionTenantCustomizationsArgsDict,
                ]
            ]
        ] = ...,
        distribution_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domains: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DistributionTenantDomainArgs,
                            DistributionTenantDomainArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_certificate_request: Optional[
            pulumi.Input[
                Union[
                    DistributionTenantManagedCertificateRequestArgs,
                    DistributionTenantManagedCertificateRequestArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DistributionTenantParameterArgs,
                            DistributionTenantParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    DistributionTenantTimeoutsArgs, DistributionTenantTimeoutsArgsDict
                ]
            ]
        ] = ...,
        wait_for_deployment: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> DistributionTenant: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionGroupId")
    def connection_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def customizations(
        self,
    ) -> pulumi.Output[Optional[outputs.DistributionTenantCustomizations]]: ...
    @_builtins.property
    @pulumi.getter(name="distributionId")
    def distribution_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def domains(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DistributionTenantDomain]]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedCertificateRequest")
    def managed_certificate_request(
        self,
    ) -> pulumi.Output[
        Optional[outputs.DistributionTenantManagedCertificateRequest]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DistributionTenantParameter]]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.DistributionTenantTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="waitForDeployment")
    def wait_for_deployment(self) -> pulumi.Output[_builtins.bool]: ...
