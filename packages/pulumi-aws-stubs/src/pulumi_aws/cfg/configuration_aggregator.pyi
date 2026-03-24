import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConfigurationAggregatorArgs", "ConfigurationAggregator"]

@pulumi.input_type
class ConfigurationAggregatorArgs:
    def __init__(
        __self__,
        *,
        account_aggregation_source: Optional[
            pulumi.Input[ConfigurationAggregatorAccountAggregationSourceArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_aggregation_source: Optional[
            pulumi.Input[ConfigurationAggregatorOrganizationAggregationSourceArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountAggregationSource")
    def account_aggregation_source(
        self,
    ) -> Optional[
        pulumi.Input[ConfigurationAggregatorAccountAggregationSourceArgs]
    ]: ...
    @account_aggregation_source.setter
    def account_aggregation_source(
        self,
        value: Optional[
            pulumi.Input[ConfigurationAggregatorAccountAggregationSourceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationAggregationSource")
    def organization_aggregation_source(
        self,
    ) -> Optional[
        pulumi.Input[ConfigurationAggregatorOrganizationAggregationSourceArgs]
    ]: ...
    @organization_aggregation_source.setter
    def organization_aggregation_source(
        self,
        value: Optional[
            pulumi.Input[ConfigurationAggregatorOrganizationAggregationSourceArgs]
        ],
    ): ...
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
class _ConfigurationAggregatorState:
    def __init__(
        __self__,
        *,
        account_aggregation_source: Optional[
            pulumi.Input[ConfigurationAggregatorAccountAggregationSourceArgs]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_aggregation_source: Optional[
            pulumi.Input[ConfigurationAggregatorOrganizationAggregationSourceArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountAggregationSource")
    def account_aggregation_source(
        self,
    ) -> Optional[
        pulumi.Input[ConfigurationAggregatorAccountAggregationSourceArgs]
    ]: ...
    @account_aggregation_source.setter
    def account_aggregation_source(
        self,
        value: Optional[
            pulumi.Input[ConfigurationAggregatorAccountAggregationSourceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationAggregationSource")
    def organization_aggregation_source(
        self,
    ) -> Optional[
        pulumi.Input[ConfigurationAggregatorOrganizationAggregationSourceArgs]
    ]: ...
    @organization_aggregation_source.setter
    def organization_aggregation_source(
        self,
        value: Optional[
            pulumi.Input[ConfigurationAggregatorOrganizationAggregationSourceArgs]
        ],
    ): ...
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

@pulumi.type_token(...)
class ConfigurationAggregator(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_aggregation_source: Optional[
            pulumi.Input[
                Union[
                    ConfigurationAggregatorAccountAggregationSourceArgs,
                    ConfigurationAggregatorAccountAggregationSourceArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_aggregation_source: Optional[
            pulumi.Input[
                Union[
                    ConfigurationAggregatorOrganizationAggregationSourceArgs,
                    ConfigurationAggregatorOrganizationAggregationSourceArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ConfigurationAggregatorArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_aggregation_source: Optional[
            pulumi.Input[
                Union[
                    ConfigurationAggregatorAccountAggregationSourceArgs,
                    ConfigurationAggregatorAccountAggregationSourceArgsDict,
                ]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_aggregation_source: Optional[
            pulumi.Input[
                Union[
                    ConfigurationAggregatorOrganizationAggregationSourceArgs,
                    ConfigurationAggregatorOrganizationAggregationSourceArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> ConfigurationAggregator: ...
    @_builtins.property
    @pulumi.getter(name="accountAggregationSource")
    def account_aggregation_source(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ConfigurationAggregatorAccountAggregationSource]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationAggregationSource")
    def organization_aggregation_source(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ConfigurationAggregatorOrganizationAggregationSource]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
