import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RuleArgs", "Rule"]

@pulumi.input_type
class RuleArgs:
    def __init__(
        __self__,
        *,
        profile_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        rule_set_name: pulumi.Input[_builtins.str],
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DeliveryRuleCacheExpirationActionArgs,
                            DeliveryRuleCacheKeyQueryStringActionArgs,
                            DeliveryRuleRequestHeaderActionArgs,
                            DeliveryRuleResponseHeaderActionArgs,
                            DeliveryRuleRouteConfigurationOverrideActionArgs,
                            OriginGroupOverrideActionArgs,
                            UrlRedirectActionArgs,
                            UrlRewriteActionArgs,
                            UrlSigningActionArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DeliveryRuleClientPortConditionArgs,
                            DeliveryRuleCookiesConditionArgs,
                            DeliveryRuleHostNameConditionArgs,
                            DeliveryRuleHttpVersionConditionArgs,
                            DeliveryRuleIsDeviceConditionArgs,
                            DeliveryRulePostArgsConditionArgs,
                            DeliveryRuleQueryStringConditionArgs,
                            DeliveryRuleRemoteAddressConditionArgs,
                            DeliveryRuleRequestBodyConditionArgs,
                            DeliveryRuleRequestHeaderConditionArgs,
                            DeliveryRuleRequestMethodConditionArgs,
                            DeliveryRuleRequestSchemeConditionArgs,
                            DeliveryRuleRequestUriConditionArgs,
                            DeliveryRuleServerPortConditionArgs,
                            DeliveryRuleSocketAddrConditionArgs,
                            DeliveryRuleSslProtocolConditionArgs,
                            DeliveryRuleUrlFileExtensionConditionArgs,
                            DeliveryRuleUrlFileNameConditionArgs,
                            DeliveryRuleUrlPathConditionArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        match_processing_behavior: Optional[
            pulumi.Input[Union[_builtins.str, MatchProcessingBehavior]]
        ] = ...,
        order: Optional[pulumi.Input[_builtins.int]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]: ...
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleSetName")
    def rule_set_name(self) -> pulumi.Input[_builtins.str]: ...
    @rule_set_name.setter
    def rule_set_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DeliveryRuleCacheExpirationActionArgs,
                        DeliveryRuleCacheKeyQueryStringActionArgs,
                        DeliveryRuleRequestHeaderActionArgs,
                        DeliveryRuleResponseHeaderActionArgs,
                        DeliveryRuleRouteConfigurationOverrideActionArgs,
                        OriginGroupOverrideActionArgs,
                        UrlRedirectActionArgs,
                        UrlRewriteActionArgs,
                        UrlSigningActionArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DeliveryRuleCacheExpirationActionArgs,
                            DeliveryRuleCacheKeyQueryStringActionArgs,
                            DeliveryRuleRequestHeaderActionArgs,
                            DeliveryRuleResponseHeaderActionArgs,
                            DeliveryRuleRouteConfigurationOverrideActionArgs,
                            OriginGroupOverrideActionArgs,
                            UrlRedirectActionArgs,
                            UrlRewriteActionArgs,
                            UrlSigningActionArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DeliveryRuleClientPortConditionArgs,
                        DeliveryRuleCookiesConditionArgs,
                        DeliveryRuleHostNameConditionArgs,
                        DeliveryRuleHttpVersionConditionArgs,
                        DeliveryRuleIsDeviceConditionArgs,
                        DeliveryRulePostArgsConditionArgs,
                        DeliveryRuleQueryStringConditionArgs,
                        DeliveryRuleRemoteAddressConditionArgs,
                        DeliveryRuleRequestBodyConditionArgs,
                        DeliveryRuleRequestHeaderConditionArgs,
                        DeliveryRuleRequestMethodConditionArgs,
                        DeliveryRuleRequestSchemeConditionArgs,
                        DeliveryRuleRequestUriConditionArgs,
                        DeliveryRuleServerPortConditionArgs,
                        DeliveryRuleSocketAddrConditionArgs,
                        DeliveryRuleSslProtocolConditionArgs,
                        DeliveryRuleUrlFileExtensionConditionArgs,
                        DeliveryRuleUrlFileNameConditionArgs,
                        DeliveryRuleUrlPathConditionArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DeliveryRuleClientPortConditionArgs,
                            DeliveryRuleCookiesConditionArgs,
                            DeliveryRuleHostNameConditionArgs,
                            DeliveryRuleHttpVersionConditionArgs,
                            DeliveryRuleIsDeviceConditionArgs,
                            DeliveryRulePostArgsConditionArgs,
                            DeliveryRuleQueryStringConditionArgs,
                            DeliveryRuleRemoteAddressConditionArgs,
                            DeliveryRuleRequestBodyConditionArgs,
                            DeliveryRuleRequestHeaderConditionArgs,
                            DeliveryRuleRequestMethodConditionArgs,
                            DeliveryRuleRequestSchemeConditionArgs,
                            DeliveryRuleRequestUriConditionArgs,
                            DeliveryRuleServerPortConditionArgs,
                            DeliveryRuleSocketAddrConditionArgs,
                            DeliveryRuleSslProtocolConditionArgs,
                            DeliveryRuleUrlFileExtensionConditionArgs,
                            DeliveryRuleUrlFileNameConditionArgs,
                            DeliveryRuleUrlPathConditionArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="matchProcessingBehavior")
    def match_processing_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MatchProcessingBehavior]]]: ...
    @match_processing_behavior.setter
    def match_processing_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, MatchProcessingBehavior]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:cdn:Rule")
class Rule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            Union[
                                DeliveryRuleCacheExpirationActionArgs,
                                DeliveryRuleCacheExpirationActionArgsDict,
                            ],
                            Union[
                                DeliveryRuleCacheKeyQueryStringActionArgs,
                                DeliveryRuleCacheKeyQueryStringActionArgsDict,
                            ],
                            Union[
                                DeliveryRuleRequestHeaderActionArgs,
                                DeliveryRuleRequestHeaderActionArgsDict,
                            ],
                            Union[
                                DeliveryRuleResponseHeaderActionArgs,
                                DeliveryRuleResponseHeaderActionArgsDict,
                            ],
                            Union[
                                DeliveryRuleRouteConfigurationOverrideActionArgs,
                                DeliveryRuleRouteConfigurationOverrideActionArgsDict,
                            ],
                            Union[
                                OriginGroupOverrideActionArgs,
                                OriginGroupOverrideActionArgsDict,
                            ],
                            Union[UrlRedirectActionArgs, UrlRedirectActionArgsDict],
                            Union[UrlRewriteActionArgs, UrlRewriteActionArgsDict],
                            Union[UrlSigningActionArgs, UrlSigningActionArgsDict],
                        ]
                    ]
                ]
            ]
        ] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            Union[
                                DeliveryRuleClientPortConditionArgs,
                                DeliveryRuleClientPortConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleCookiesConditionArgs,
                                DeliveryRuleCookiesConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleHostNameConditionArgs,
                                DeliveryRuleHostNameConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleHttpVersionConditionArgs,
                                DeliveryRuleHttpVersionConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleIsDeviceConditionArgs,
                                DeliveryRuleIsDeviceConditionArgsDict,
                            ],
                            Union[
                                DeliveryRulePostArgsConditionArgs,
                                DeliveryRulePostArgsConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleQueryStringConditionArgs,
                                DeliveryRuleQueryStringConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleRemoteAddressConditionArgs,
                                DeliveryRuleRemoteAddressConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleRequestBodyConditionArgs,
                                DeliveryRuleRequestBodyConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleRequestHeaderConditionArgs,
                                DeliveryRuleRequestHeaderConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleRequestMethodConditionArgs,
                                DeliveryRuleRequestMethodConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleRequestSchemeConditionArgs,
                                DeliveryRuleRequestSchemeConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleRequestUriConditionArgs,
                                DeliveryRuleRequestUriConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleServerPortConditionArgs,
                                DeliveryRuleServerPortConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleSocketAddrConditionArgs,
                                DeliveryRuleSocketAddrConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleSslProtocolConditionArgs,
                                DeliveryRuleSslProtocolConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleUrlFileExtensionConditionArgs,
                                DeliveryRuleUrlFileExtensionConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleUrlFileNameConditionArgs,
                                DeliveryRuleUrlFileNameConditionArgsDict,
                            ],
                            Union[
                                DeliveryRuleUrlPathConditionArgs,
                                DeliveryRuleUrlPathConditionArgsDict,
                            ],
                        ]
                    ]
                ]
            ]
        ] = ...,
        match_processing_behavior: Optional[
            pulumi.Input[Union[_builtins.str, MatchProcessingBehavior]]
        ] = ...,
        order: Optional[pulumi.Input[_builtins.int]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Rule: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Optional[Sequence[Any]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Optional[Sequence[Any]]]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchProcessingBehavior")
    def match_processing_behavior(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleSetName")
    def rule_set_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
