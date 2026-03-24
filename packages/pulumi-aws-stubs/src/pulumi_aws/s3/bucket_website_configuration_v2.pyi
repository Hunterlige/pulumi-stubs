import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BucketWebsiteConfigurationV2Args", "BucketWebsiteConfigurationV2"]

@pulumi.input_type
class BucketWebsiteConfigurationV2Args:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        error_document: Optional[
            pulumi.Input[BucketWebsiteConfigurationV2ErrorDocumentArgs]
        ] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        index_document: Optional[
            pulumi.Input[BucketWebsiteConfigurationV2IndexDocumentArgs]
        ] = ...,
        redirect_all_requests_to: Optional[
            pulumi.Input[BucketWebsiteConfigurationV2RedirectAllRequestsToArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rule_details: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="errorDocument")
    def error_document(
        self,
    ) -> Optional[pulumi.Input[BucketWebsiteConfigurationV2ErrorDocumentArgs]]: ...
    @error_document.setter
    def error_document(
        self,
        value: Optional[pulumi.Input[BucketWebsiteConfigurationV2ErrorDocumentArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="indexDocument")
    def index_document(
        self,
    ) -> Optional[pulumi.Input[BucketWebsiteConfigurationV2IndexDocumentArgs]]: ...
    @index_document.setter
    def index_document(
        self,
        value: Optional[pulumi.Input[BucketWebsiteConfigurationV2IndexDocumentArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(
        self,
    ) -> Optional[
        pulumi.Input[BucketWebsiteConfigurationV2RedirectAllRequestsToArgs]
    ]: ...
    @redirect_all_requests_to.setter
    def redirect_all_requests_to(
        self,
        value: Optional[
            pulumi.Input[BucketWebsiteConfigurationV2RedirectAllRequestsToArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingRuleDetails")
    def routing_rule_details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_rule_details.setter
    def routing_rule_details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleArgs]]
        ]
    ]: ...
    @routing_rules.setter
    def routing_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleArgs]]
            ]
        ],
    ): ...

@pulumi.input_type
class _BucketWebsiteConfigurationV2State:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        error_document: Optional[
            pulumi.Input[BucketWebsiteConfigurationV2ErrorDocumentArgs]
        ] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        index_document: Optional[
            pulumi.Input[BucketWebsiteConfigurationV2IndexDocumentArgs]
        ] = ...,
        redirect_all_requests_to: Optional[
            pulumi.Input[BucketWebsiteConfigurationV2RedirectAllRequestsToArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rule_details: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleArgs]]
            ]
        ] = ...,
        website_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        website_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorDocument")
    def error_document(
        self,
    ) -> Optional[pulumi.Input[BucketWebsiteConfigurationV2ErrorDocumentArgs]]: ...
    @error_document.setter
    def error_document(
        self,
        value: Optional[pulumi.Input[BucketWebsiteConfigurationV2ErrorDocumentArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="indexDocument")
    def index_document(
        self,
    ) -> Optional[pulumi.Input[BucketWebsiteConfigurationV2IndexDocumentArgs]]: ...
    @index_document.setter
    def index_document(
        self,
        value: Optional[pulumi.Input[BucketWebsiteConfigurationV2IndexDocumentArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(
        self,
    ) -> Optional[
        pulumi.Input[BucketWebsiteConfigurationV2RedirectAllRequestsToArgs]
    ]: ...
    @redirect_all_requests_to.setter
    def redirect_all_requests_to(
        self,
        value: Optional[
            pulumi.Input[BucketWebsiteConfigurationV2RedirectAllRequestsToArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingRuleDetails")
    def routing_rule_details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_rule_details.setter
    def routing_rule_details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleArgs]]
        ]
    ]: ...
    @routing_rules.setter
    def routing_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="websiteDomain")
    def website_domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @website_domain.setter
    def website_domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="websiteEndpoint")
    def website_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @website_endpoint.setter
    def website_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class BucketWebsiteConfigurationV2(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        error_document: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationV2ErrorDocumentArgs,
                    BucketWebsiteConfigurationV2ErrorDocumentArgsDict,
                ]
            ]
        ] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        index_document: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationV2IndexDocumentArgs,
                    BucketWebsiteConfigurationV2IndexDocumentArgsDict,
                ]
            ]
        ] = ...,
        redirect_all_requests_to: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationV2RedirectAllRequestsToArgs,
                    BucketWebsiteConfigurationV2RedirectAllRequestsToArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rule_details: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketWebsiteConfigurationV2RoutingRuleArgs,
                            BucketWebsiteConfigurationV2RoutingRuleArgsDict,
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
        args: BucketWebsiteConfigurationV2Args,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        error_document: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationV2ErrorDocumentArgs,
                    BucketWebsiteConfigurationV2ErrorDocumentArgsDict,
                ]
            ]
        ] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        index_document: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationV2IndexDocumentArgs,
                    BucketWebsiteConfigurationV2IndexDocumentArgsDict,
                ]
            ]
        ] = ...,
        redirect_all_requests_to: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationV2RedirectAllRequestsToArgs,
                    BucketWebsiteConfigurationV2RedirectAllRequestsToArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rule_details: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketWebsiteConfigurationV2RoutingRuleArgs,
                            BucketWebsiteConfigurationV2RoutingRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        website_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        website_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> BucketWebsiteConfigurationV2: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorDocument")
    def error_document(
        self,
    ) -> pulumi.Output[Optional[outputs.BucketWebsiteConfigurationV2ErrorDocument]]: ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="indexDocument")
    def index_document(
        self,
    ) -> pulumi.Output[Optional[outputs.BucketWebsiteConfigurationV2IndexDocument]]: ...
    @_builtins.property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(
        self,
    ) -> pulumi.Output[
        Optional[outputs.BucketWebsiteConfigurationV2RedirectAllRequestsTo]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingRuleDetails")
    def routing_rule_details(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(
        self,
    ) -> pulumi.Output[Sequence[outputs.BucketWebsiteConfigurationV2RoutingRule]]: ...
    @_builtins.property
    @pulumi.getter(name="websiteDomain")
    def website_domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="websiteEndpoint")
    def website_endpoint(self) -> pulumi.Output[_builtins.str]: ...
