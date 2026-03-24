import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebhookArgs", "Webhook"]

@pulumi.input_type
class WebhookArgs:
    def __init__(
        __self__,
        *,
        project_name: pulumi.Input[_builtins.str],
        branch_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        build_type: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebhookFilterGroupArgs]]]
        ] = ...,
        manual_creation: Optional[pulumi.Input[_builtins.bool]] = ...,
        pull_request_build_policy: Optional[
            pulumi.Input[WebhookPullRequestBuildPolicyArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_configuration: Optional[
            pulumi.Input[WebhookScopeConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[_builtins.str]: ...
    @project_name.setter
    def project_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="branchFilter")
    def branch_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch_filter.setter
    def branch_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="buildType")
    def build_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_type.setter
    def build_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filterGroups")
    def filter_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebhookFilterGroupArgs]]]]: ...
    @filter_groups.setter
    def filter_groups(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[WebhookFilterGroupArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manualCreation")
    def manual_creation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manual_creation.setter
    def manual_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pullRequestBuildPolicy")
    def pull_request_build_policy(
        self,
    ) -> Optional[pulumi.Input[WebhookPullRequestBuildPolicyArgs]]: ...
    @pull_request_build_policy.setter
    def pull_request_build_policy(
        self, value: Optional[pulumi.Input[WebhookPullRequestBuildPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scopeConfiguration")
    def scope_configuration(
        self,
    ) -> Optional[pulumi.Input[WebhookScopeConfigurationArgs]]: ...
    @scope_configuration.setter
    def scope_configuration(
        self, value: Optional[pulumi.Input[WebhookScopeConfigurationArgs]]
    ): ...

@pulumi.input_type
class _WebhookState:
    def __init__(
        __self__,
        *,
        branch_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        build_type: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebhookFilterGroupArgs]]]
        ] = ...,
        manual_creation: Optional[pulumi.Input[_builtins.bool]] = ...,
        payload_url: Optional[pulumi.Input[_builtins.str]] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        pull_request_build_policy: Optional[
            pulumi.Input[WebhookPullRequestBuildPolicyArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_configuration: Optional[
            pulumi.Input[WebhookScopeConfigurationArgs]
        ] = ...,
        secret: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchFilter")
    def branch_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch_filter.setter
    def branch_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="buildType")
    def build_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_type.setter
    def build_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filterGroups")
    def filter_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebhookFilterGroupArgs]]]]: ...
    @filter_groups.setter
    def filter_groups(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[WebhookFilterGroupArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manualCreation")
    def manual_creation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manual_creation.setter
    def manual_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="payloadUrl")
    def payload_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @payload_url.setter
    def payload_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pullRequestBuildPolicy")
    def pull_request_build_policy(
        self,
    ) -> Optional[pulumi.Input[WebhookPullRequestBuildPolicyArgs]]: ...
    @pull_request_build_policy.setter
    def pull_request_build_policy(
        self, value: Optional[pulumi.Input[WebhookPullRequestBuildPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scopeConfiguration")
    def scope_configuration(
        self,
    ) -> Optional[pulumi.Input[WebhookScopeConfigurationArgs]]: ...
    @scope_configuration.setter
    def scope_configuration(
        self, value: Optional[pulumi.Input[WebhookScopeConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret.setter
    def secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:codebuild/webhook:Webhook")
class Webhook(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        branch_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        build_type: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_groups: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[WebhookFilterGroupArgs, WebhookFilterGroupArgsDict]
                    ]
                ]
            ]
        ] = ...,
        manual_creation: Optional[pulumi.Input[_builtins.bool]] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        pull_request_build_policy: Optional[
            pulumi.Input[
                Union[
                    WebhookPullRequestBuildPolicyArgs,
                    WebhookPullRequestBuildPolicyArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_configuration: Optional[
            pulumi.Input[
                Union[WebhookScopeConfigurationArgs, WebhookScopeConfigurationArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebhookArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        branch_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        build_type: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_groups: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[WebhookFilterGroupArgs, WebhookFilterGroupArgsDict]
                    ]
                ]
            ]
        ] = ...,
        manual_creation: Optional[pulumi.Input[_builtins.bool]] = ...,
        payload_url: Optional[pulumi.Input[_builtins.str]] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        pull_request_build_policy: Optional[
            pulumi.Input[
                Union[
                    WebhookPullRequestBuildPolicyArgs,
                    WebhookPullRequestBuildPolicyArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_configuration: Optional[
            pulumi.Input[
                Union[WebhookScopeConfigurationArgs, WebhookScopeConfigurationArgsDict]
            ]
        ] = ...,
        secret: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Webhook: ...
    @_builtins.property
    @pulumi.getter(name="branchFilter")
    def branch_filter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="buildType")
    def build_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="filterGroups")
    def filter_groups(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.WebhookFilterGroup]]]: ...
    @_builtins.property
    @pulumi.getter(name="manualCreation")
    def manual_creation(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="payloadUrl")
    def payload_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pullRequestBuildPolicy")
    def pull_request_build_policy(
        self,
    ) -> pulumi.Output[outputs.WebhookPullRequestBuildPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scopeConfiguration")
    def scope_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.WebhookScopeConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]: ...
