import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BucketWebsiteConfigurationArgs", "BucketWebsiteConfiguration"]

@pulumi.input_type
class BucketWebsiteConfigurationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        error_document: Optional[
            pulumi.Input[BucketWebsiteConfigurationErrorDocumentArgs]
        ] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        index_document: Optional[
            pulumi.Input[BucketWebsiteConfigurationIndexDocumentArgs]
        ] = ...,
        redirect_all_requests_to: Optional[
            pulumi.Input[BucketWebsiteConfigurationRedirectAllRequestsToArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rule_details: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketWebsiteConfigurationRoutingRuleArgs]]
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
    ) -> Optional[pulumi.Input[BucketWebsiteConfigurationErrorDocumentArgs]]: ...
    @error_document.setter
    def error_document(
        self, value: Optional[pulumi.Input[BucketWebsiteConfigurationErrorDocumentArgs]]
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
    ) -> Optional[pulumi.Input[BucketWebsiteConfigurationIndexDocumentArgs]]: ...
    @index_document.setter
    def index_document(
        self, value: Optional[pulumi.Input[BucketWebsiteConfigurationIndexDocumentArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(
        self,
    ) -> Optional[
        pulumi.Input[BucketWebsiteConfigurationRedirectAllRequestsToArgs]
    ]: ...
    @redirect_all_requests_to.setter
    def redirect_all_requests_to(
        self,
        value: Optional[
            pulumi.Input[BucketWebsiteConfigurationRedirectAllRequestsToArgs]
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
        pulumi.Input[Sequence[pulumi.Input[BucketWebsiteConfigurationRoutingRuleArgs]]]
    ]: ...
    @routing_rules.setter
    def routing_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketWebsiteConfigurationRoutingRuleArgs]]
            ]
        ],
    ): ...

@pulumi.input_type
class _BucketWebsiteConfigurationState:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        error_document: Optional[
            pulumi.Input[BucketWebsiteConfigurationErrorDocumentArgs]
        ] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        index_document: Optional[
            pulumi.Input[BucketWebsiteConfigurationIndexDocumentArgs]
        ] = ...,
        redirect_all_requests_to: Optional[
            pulumi.Input[BucketWebsiteConfigurationRedirectAllRequestsToArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rule_details: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketWebsiteConfigurationRoutingRuleArgs]]
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
    ) -> Optional[pulumi.Input[BucketWebsiteConfigurationErrorDocumentArgs]]: ...
    @error_document.setter
    def error_document(
        self, value: Optional[pulumi.Input[BucketWebsiteConfigurationErrorDocumentArgs]]
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
    ) -> Optional[pulumi.Input[BucketWebsiteConfigurationIndexDocumentArgs]]: ...
    @index_document.setter
    def index_document(
        self, value: Optional[pulumi.Input[BucketWebsiteConfigurationIndexDocumentArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(
        self,
    ) -> Optional[
        pulumi.Input[BucketWebsiteConfigurationRedirectAllRequestsToArgs]
    ]: ...
    @redirect_all_requests_to.setter
    def redirect_all_requests_to(
        self,
        value: Optional[
            pulumi.Input[BucketWebsiteConfigurationRedirectAllRequestsToArgs]
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
        pulumi.Input[Sequence[pulumi.Input[BucketWebsiteConfigurationRoutingRuleArgs]]]
    ]: ...
    @routing_rules.setter
    def routing_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketWebsiteConfigurationRoutingRuleArgs]]
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
class BucketWebsiteConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        error_document: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationErrorDocumentArgs,
                    BucketWebsiteConfigurationErrorDocumentArgsDict,
                ]
            ]
        ] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        index_document: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationIndexDocumentArgs,
                    BucketWebsiteConfigurationIndexDocumentArgsDict,
                ]
            ]
        ] = ...,
        redirect_all_requests_to: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationRedirectAllRequestsToArgs,
                    BucketWebsiteConfigurationRedirectAllRequestsToArgsDict,
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
                            BucketWebsiteConfigurationRoutingRuleArgs,
                            BucketWebsiteConfigurationRoutingRuleArgsDict,
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
        args: BucketWebsiteConfigurationArgs,
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
                    BucketWebsiteConfigurationErrorDocumentArgs,
                    BucketWebsiteConfigurationErrorDocumentArgsDict,
                ]
            ]
        ] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        index_document: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationIndexDocumentArgs,
                    BucketWebsiteConfigurationIndexDocumentArgsDict,
                ]
            ]
        ] = ...,
        redirect_all_requests_to: Optional[
            pulumi.Input[
                Union[
                    BucketWebsiteConfigurationRedirectAllRequestsToArgs,
                    BucketWebsiteConfigurationRedirectAllRequestsToArgsDict,
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
                            BucketWebsiteConfigurationRoutingRuleArgs,
                            BucketWebsiteConfigurationRoutingRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        website_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        website_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> BucketWebsiteConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorDocument")
    def error_document(
        self,
    ) -> pulumi.Output[Optional[outputs.BucketWebsiteConfigurationErrorDocument]]: ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="indexDocument")
    def index_document(
        self,
    ) -> pulumi.Output[Optional[outputs.BucketWebsiteConfigurationIndexDocument]]: ...
    @_builtins.property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(
        self,
    ) -> pulumi.Output[
        Optional[outputs.BucketWebsiteConfigurationRedirectAllRequestsTo]
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
    ) -> pulumi.Output[Sequence[outputs.BucketWebsiteConfigurationRoutingRule]]: ...
    @_builtins.property
    @pulumi.getter(name="websiteDomain")
    def website_domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="websiteEndpoint")
    def website_endpoint(self) -> pulumi.Output[_builtins.str]: ...
