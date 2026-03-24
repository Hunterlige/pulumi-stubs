import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
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
        authentication: pulumi.Input[_builtins.str],
        filters: pulumi.Input[Sequence[pulumi.Input[WebhookFilterArgs]]],
        target_action: pulumi.Input[_builtins.str],
        target_pipeline: pulumi.Input[_builtins.str],
        authentication_configuration: Optional[
            pulumi.Input[WebhookAuthenticationConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> pulumi.Input[_builtins.str]: ...
    @authentication.setter
    def authentication(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> pulumi.Input[Sequence[pulumi.Input[WebhookFilterArgs]]]: ...
    @filters.setter
    def filters(
        self, value: pulumi.Input[Sequence[pulumi.Input[WebhookFilterArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAction")
    def target_action(self) -> pulumi.Input[_builtins.str]: ...
    @target_action.setter
    def target_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetPipeline")
    def target_pipeline(self) -> pulumi.Input[_builtins.str]: ...
    @target_pipeline.setter
    def target_pipeline(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> Optional[pulumi.Input[WebhookAuthenticationConfigurationArgs]]: ...
    @authentication_configuration.setter
    def authentication_configuration(
        self, value: Optional[pulumi.Input[WebhookAuthenticationConfigurationArgs]]
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
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _WebhookState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_configuration: Optional[
            pulumi.Input[WebhookAuthenticationConfigurationArgs]
        ] = ...,
        filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebhookFilterArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_action: Optional[pulumi.Input[_builtins.str]] = ...,
        target_pipeline: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> Optional[pulumi.Input[WebhookAuthenticationConfigurationArgs]]: ...
    @authentication_configuration.setter
    def authentication_configuration(
        self, value: Optional[pulumi.Input[WebhookAuthenticationConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebhookFilterArgs]]]]: ...
    @filters.setter
    def filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebhookFilterArgs]]]]
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
    @pulumi.getter(name="targetAction")
    def target_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_action.setter
    def target_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetPipeline")
    def target_pipeline(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_pipeline.setter
    def target_pipeline(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:codepipeline/webhook:Webhook")
class Webhook(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_configuration: Optional[
            pulumi.Input[
                Union[
                    WebhookAuthenticationConfigurationArgs,
                    WebhookAuthenticationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        filters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[WebhookFilterArgs, WebhookFilterArgsDict]]]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_action: Optional[pulumi.Input[_builtins.str]] = ...,
        target_pipeline: Optional[pulumi.Input[_builtins.str]] = ...,
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
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_configuration: Optional[
            pulumi.Input[
                Union[
                    WebhookAuthenticationConfigurationArgs,
                    WebhookAuthenticationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        filters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[WebhookFilterArgs, WebhookFilterArgsDict]]]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_action: Optional[pulumi.Input[_builtins.str]] = ...,
        target_pipeline: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Webhook: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.WebhookAuthenticationConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Sequence[outputs.WebhookFilter]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetAction")
    def target_action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetPipeline")
    def target_pipeline(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]: ...
