import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebAclArgs", "WebAcl"]

@pulumi.input_type
class WebAclArgs:
    def __init__(
        __self__,
        *,
        default_action: pulumi.Input[WebAclDefaultActionArgs],
        metric_name: pulumi.Input[_builtins.str],
        logging_configuration: Optional[
            pulumi.Input[WebAclLoggingConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Input[WebAclDefaultActionArgs]: ...
    @default_action.setter
    def default_action(self, value: pulumi.Input[WebAclDefaultActionArgs]): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> Optional[pulumi.Input[WebAclLoggingConfigurationArgs]]: ...
    @logging_configuration.setter
    def logging_configuration(
        self, value: Optional[pulumi.Input[WebAclLoggingConfigurationArgs]]
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
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]]
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

@pulumi.input_type
class _WebAclState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_action: Optional[pulumi.Input[WebAclDefaultActionArgs]] = ...,
        logging_configuration: Optional[
            pulumi.Input[WebAclLoggingConfigurationArgs]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[WebAclDefaultActionArgs]]: ...
    @default_action.setter
    def default_action(
        self, value: Optional[pulumi.Input[WebAclDefaultActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> Optional[pulumi.Input[WebAclLoggingConfigurationArgs]]: ...
    @logging_configuration.setter
    def logging_configuration(
        self, value: Optional[pulumi.Input[WebAclLoggingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]]
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:wafregional/webAcl:WebAcl")
class WebAcl(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        default_action: Optional[
            pulumi.Input[Union[WebAclDefaultActionArgs, WebAclDefaultActionArgsDict]]
        ] = ...,
        logging_configuration: Optional[
            pulumi.Input[
                Union[
                    WebAclLoggingConfigurationArgs, WebAclLoggingConfigurationArgsDict
                ]
            ]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[WebAclRuleArgs, WebAclRuleArgsDict]]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebAclArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_action: Optional[
            pulumi.Input[Union[WebAclDefaultActionArgs, WebAclDefaultActionArgsDict]]
        ] = ...,
        logging_configuration: Optional[
            pulumi.Input[
                Union[
                    WebAclLoggingConfigurationArgs, WebAclLoggingConfigurationArgsDict
                ]
            ]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[WebAclRuleArgs, WebAclRuleArgsDict]]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> WebAcl: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Output[outputs.WebAclDefaultAction]: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.WebAclLoggingConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[outputs.WebAclRule]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
