import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EnvironmentArgs", "Environment"]

@pulumi.input_type
class EnvironmentArgs:
    def __init__(
        __self__,
        *,
        domain_identifier: pulumi.Input[_builtins.str],
        profile_identifier: pulumi.Input[_builtins.str],
        project_identifier: pulumi.Input[_builtins.str],
        account_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        account_region: Optional[pulumi.Input[_builtins.str]] = ...,
        blueprint_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        glossary_terms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[EnvironmentTimeoutsArgs]] = ...,
        user_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentUserParameterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @domain_identifier.setter
    def domain_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="profileIdentifier")
    def profile_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @profile_identifier.setter
    def profile_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectIdentifier")
    def project_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @project_identifier.setter
    def project_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountIdentifier")
    def account_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_identifier.setter
    def account_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="accountRegion")
    def account_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_region.setter
    def account_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blueprintIdentifier")
    def blueprint_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blueprint_identifier.setter
    def blueprint_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="glossaryTerms")
    def glossary_terms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @glossary_terms.setter
    def glossary_terms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[EnvironmentTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[EnvironmentTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="userParameters")
    def user_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EnvironmentUserParameterArgs]]]
    ]: ...
    @user_parameters.setter
    def user_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentUserParameterArgs]]]
        ],
    ): ...

@pulumi.input_type
class _EnvironmentState:
    def __init__(
        __self__,
        *,
        account_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        account_region: Optional[pulumi.Input[_builtins.str]] = ...,
        blueprint_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        glossary_terms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        last_deployments: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentLastDeploymentArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        project_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentProvisionedResourceArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[EnvironmentTimeoutsArgs]] = ...,
        user_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentUserParameterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountIdentifier")
    def account_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_identifier.setter
    def account_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="accountRegion")
    def account_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_region.setter
    def account_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blueprintIdentifier")
    def blueprint_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blueprint_identifier.setter
    def blueprint_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_identifier.setter
    def domain_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="glossaryTerms")
    def glossary_terms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @glossary_terms.setter
    def glossary_terms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastDeployments")
    def last_deployments(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EnvironmentLastDeploymentArgs]]]
    ]: ...
    @last_deployments.setter
    def last_deployments(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentLastDeploymentArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profileIdentifier")
    def profile_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_identifier.setter
    def profile_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectIdentifier")
    def project_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_identifier.setter
    def project_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerEnvironment")
    def provider_environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider_environment.setter
    def provider_environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedResources")
    def provisioned_resources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EnvironmentProvisionedResourceArgs]]]
    ]: ...
    @provisioned_resources.setter
    def provisioned_resources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentProvisionedResourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[EnvironmentTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[EnvironmentTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="userParameters")
    def user_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EnvironmentUserParameterArgs]]]
    ]: ...
    @user_parameters.setter
    def user_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentUserParameterArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:datazone/environment:Environment")
class Environment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        account_region: Optional[pulumi.Input[_builtins.str]] = ...,
        blueprint_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        glossary_terms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        project_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[EnvironmentTimeoutsArgs, EnvironmentTimeoutsArgsDict]]
        ] = ...,
        user_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EnvironmentUserParameterArgs,
                            EnvironmentUserParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EnvironmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        account_region: Optional[pulumi.Input[_builtins.str]] = ...,
        blueprint_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        glossary_terms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        last_deployments: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EnvironmentLastDeploymentArgs,
                            EnvironmentLastDeploymentArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        project_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EnvironmentProvisionedResourceArgs,
                            EnvironmentProvisionedResourceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[EnvironmentTimeoutsArgs, EnvironmentTimeoutsArgsDict]]
        ] = ...,
        user_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EnvironmentUserParameterArgs,
                            EnvironmentUserParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> Environment: ...
    @_builtins.property
    @pulumi.getter(name="accountIdentifier")
    def account_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accountRegion")
    def account_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blueprintIdentifier")
    def blueprint_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="glossaryTerms")
    def glossary_terms(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="lastDeployments")
    def last_deployments(
        self,
    ) -> pulumi.Output[Sequence[outputs.EnvironmentLastDeployment]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="profileIdentifier")
    def profile_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectIdentifier")
    def project_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerEnvironment")
    def provider_environment(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedResources")
    def provisioned_resources(
        self,
    ) -> pulumi.Output[Sequence[outputs.EnvironmentProvisionedResource]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.EnvironmentTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="userParameters")
    def user_parameters(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.EnvironmentUserParameter]]]: ...
