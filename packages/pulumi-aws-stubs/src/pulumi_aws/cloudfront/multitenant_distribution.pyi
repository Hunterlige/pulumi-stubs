import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MultitenantDistributionArgs", "MultitenantDistribution"]

@pulumi.input_type
class MultitenantDistributionArgs:
    def __init__(
        __self__,
        *,
        comment: pulumi.Input[_builtins.str],
        default_cache_behavior: pulumi.Input[
            MultitenantDistributionDefaultCacheBehaviorArgs
        ],
        enabled: pulumi.Input[_builtins.bool],
        tenant_config: pulumi.Input[MultitenantDistributionTenantConfigArgs],
        viewer_certificate: pulumi.Input[MultitenantDistributionViewerCertificateArgs],
        active_trusted_key_groups: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionActiveTrustedKeyGroupArgs]]
            ]
        ] = ...,
        cache_behaviors: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorArgs]]
            ]
        ] = ...,
        custom_error_responses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionCustomErrorResponseArgs]]
            ]
        ] = ...,
        default_root_object: Optional[pulumi.Input[_builtins.str]] = ...,
        http_version: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginGroupArgs]]]
        ] = ...,
        origins: Optional[
            pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginArgs]]]
        ] = ...,
        restrictions: Optional[
            pulumi.Input[MultitenantDistributionRestrictionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[MultitenantDistributionTimeoutsArgs]] = ...,
        web_acl_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Input[_builtins.str]: ...
    @comment.setter
    def comment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(
        self,
    ) -> pulumi.Input[MultitenantDistributionDefaultCacheBehaviorArgs]: ...
    @default_cache_behavior.setter
    def default_cache_behavior(
        self, value: pulumi.Input[MultitenantDistributionDefaultCacheBehaviorArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="tenantConfig")
    def tenant_config(
        self,
    ) -> pulumi.Input[MultitenantDistributionTenantConfigArgs]: ...
    @tenant_config.setter
    def tenant_config(
        self, value: pulumi.Input[MultitenantDistributionTenantConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="viewerCertificate")
    def viewer_certificate(
        self,
    ) -> pulumi.Input[MultitenantDistributionViewerCertificateArgs]: ...
    @viewer_certificate.setter
    def viewer_certificate(
        self, value: pulumi.Input[MultitenantDistributionViewerCertificateArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="activeTrustedKeyGroups")
    def active_trusted_key_groups(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[MultitenantDistributionActiveTrustedKeyGroupArgs]]
        ]
    ]: ...
    @active_trusted_key_groups.setter
    def active_trusted_key_groups(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionActiveTrustedKeyGroupArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cacheBehaviors")
    def cache_behaviors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorArgs]]]
    ]: ...
    @cache_behaviors.setter
    def cache_behaviors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customErrorResponses")
    def custom_error_responses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[MultitenantDistributionCustomErrorResponseArgs]]
        ]
    ]: ...
    @custom_error_responses.setter
    def custom_error_responses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionCustomErrorResponseArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultRootObject")
    def default_root_object(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_root_object.setter
    def default_root_object(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpVersion")
    def http_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_version.setter
    def http_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originGroups")
    def origin_groups(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginGroupArgs]]]
    ]: ...
    @origin_groups.setter
    def origin_groups(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginGroupArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def origins(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginArgs]]]
    ]: ...
    @origins.setter
    def origins(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def restrictions(
        self,
    ) -> Optional[pulumi.Input[MultitenantDistributionRestrictionsArgs]]: ...
    @restrictions.setter
    def restrictions(
        self, value: Optional[pulumi.Input[MultitenantDistributionRestrictionsArgs]]
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
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[MultitenantDistributionTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[MultitenantDistributionTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webAclId")
    def web_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_acl_id.setter
    def web_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _MultitenantDistributionState:
    def __init__(
        __self__,
        *,
        active_trusted_key_groups: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionActiveTrustedKeyGroupArgs]]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_behaviors: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorArgs]]
            ]
        ] = ...,
        caller_reference: Optional[pulumi.Input[_builtins.str]] = ...,
        comment: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_error_responses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionCustomErrorResponseArgs]]
            ]
        ] = ...,
        default_cache_behavior: Optional[
            pulumi.Input[MultitenantDistributionDefaultCacheBehaviorArgs]
        ] = ...,
        default_root_object: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        http_version: Optional[pulumi.Input[_builtins.str]] = ...,
        in_progress_invalidation_batches: Optional[pulumi.Input[_builtins.int]] = ...,
        last_modified_time: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginGroupArgs]]]
        ] = ...,
        origins: Optional[
            pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginArgs]]]
        ] = ...,
        restrictions: Optional[
            pulumi.Input[MultitenantDistributionRestrictionsArgs]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tenant_config: Optional[
            pulumi.Input[MultitenantDistributionTenantConfigArgs]
        ] = ...,
        timeouts: Optional[pulumi.Input[MultitenantDistributionTimeoutsArgs]] = ...,
        viewer_certificate: Optional[
            pulumi.Input[MultitenantDistributionViewerCertificateArgs]
        ] = ...,
        web_acl_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeTrustedKeyGroups")
    def active_trusted_key_groups(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[MultitenantDistributionActiveTrustedKeyGroupArgs]]
        ]
    ]: ...
    @active_trusted_key_groups.setter
    def active_trusted_key_groups(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionActiveTrustedKeyGroupArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheBehaviors")
    def cache_behaviors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorArgs]]]
    ]: ...
    @cache_behaviors.setter
    def cache_behaviors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @caller_reference.setter
    def caller_reference(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_mode.setter
    def connection_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customErrorResponses")
    def custom_error_responses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[MultitenantDistributionCustomErrorResponseArgs]]
        ]
    ]: ...
    @custom_error_responses.setter
    def custom_error_responses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MultitenantDistributionCustomErrorResponseArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(
        self,
    ) -> Optional[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorArgs]]: ...
    @default_cache_behavior.setter
    def default_cache_behavior(
        self,
        value: Optional[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultRootObject")
    def default_root_object(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_root_object.setter
    def default_root_object(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="httpVersion")
    def http_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_version.setter
    def http_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inProgressInvalidationBatches")
    def in_progress_invalidation_batches(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @in_progress_invalidation_batches.setter
    def in_progress_invalidation_batches(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originGroups")
    def origin_groups(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginGroupArgs]]]
    ]: ...
    @origin_groups.setter
    def origin_groups(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginGroupArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def origins(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginArgs]]]
    ]: ...
    @origins.setter
    def origins(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def restrictions(
        self,
    ) -> Optional[pulumi.Input[MultitenantDistributionRestrictionsArgs]]: ...
    @restrictions.setter
    def restrictions(
        self, value: Optional[pulumi.Input[MultitenantDistributionRestrictionsArgs]]
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
    @pulumi.getter(name="tenantConfig")
    def tenant_config(
        self,
    ) -> Optional[pulumi.Input[MultitenantDistributionTenantConfigArgs]]: ...
    @tenant_config.setter
    def tenant_config(
        self, value: Optional[pulumi.Input[MultitenantDistributionTenantConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[MultitenantDistributionTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[MultitenantDistributionTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="viewerCertificate")
    def viewer_certificate(
        self,
    ) -> Optional[pulumi.Input[MultitenantDistributionViewerCertificateArgs]]: ...
    @viewer_certificate.setter
    def viewer_certificate(
        self,
        value: Optional[pulumi.Input[MultitenantDistributionViewerCertificateArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webAclId")
    def web_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_acl_id.setter
    def web_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class MultitenantDistribution(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        active_trusted_key_groups: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MultitenantDistributionActiveTrustedKeyGroupArgs,
                            MultitenantDistributionActiveTrustedKeyGroupArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        cache_behaviors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MultitenantDistributionCacheBehaviorArgs,
                            MultitenantDistributionCacheBehaviorArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        comment: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_error_responses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MultitenantDistributionCustomErrorResponseArgs,
                            MultitenantDistributionCustomErrorResponseArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        default_cache_behavior: Optional[
            pulumi.Input[
                Union[
                    MultitenantDistributionDefaultCacheBehaviorArgs,
                    MultitenantDistributionDefaultCacheBehaviorArgsDict,
                ]
            ]
        ] = ...,
        default_root_object: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        http_version: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_groups: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MultitenantDistributionOriginGroupArgs,
                            MultitenantDistributionOriginGroupArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        origins: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MultitenantDistributionOriginArgs,
                            MultitenantDistributionOriginArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        restrictions: Optional[
            pulumi.Input[
                Union[
                    MultitenantDistributionRestrictionsArgs,
                    MultitenantDistributionRestrictionsArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tenant_config: Optional[
            pulumi.Input[
                Union[
                    MultitenantDistributionTenantConfigArgs,
                    MultitenantDistributionTenantConfigArgsDict,
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    MultitenantDistributionTimeoutsArgs,
                    MultitenantDistributionTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        viewer_certificate: Optional[
            pulumi.Input[
                Union[
                    MultitenantDistributionViewerCertificateArgs,
                    MultitenantDistributionViewerCertificateArgsDict,
                ]
            ]
        ] = ...,
        web_acl_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MultitenantDistributionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        active_trusted_key_groups: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MultitenantDistributionActiveTrustedKeyGroupArgs,
                            MultitenantDistributionActiveTrustedKeyGroupArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_behaviors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MultitenantDistributionCacheBehaviorArgs,
                            MultitenantDistributionCacheBehaviorArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        caller_reference: Optional[pulumi.Input[_builtins.str]] = ...,
        comment: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_error_responses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MultitenantDistributionCustomErrorResponseArgs,
                            MultitenantDistributionCustomErrorResponseArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        default_cache_behavior: Optional[
            pulumi.Input[
                Union[
                    MultitenantDistributionDefaultCacheBehaviorArgs,
                    MultitenantDistributionDefaultCacheBehaviorArgsDict,
                ]
            ]
        ] = ...,
        default_root_object: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        http_version: Optional[pulumi.Input[_builtins.str]] = ...,
        in_progress_invalidation_batches: Optional[pulumi.Input[_builtins.int]] = ...,
        last_modified_time: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_groups: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MultitenantDistributionOriginGroupArgs,
                            MultitenantDistributionOriginGroupArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        origins: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MultitenantDistributionOriginArgs,
                            MultitenantDistributionOriginArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        restrictions: Optional[
            pulumi.Input[
                Union[
                    MultitenantDistributionRestrictionsArgs,
                    MultitenantDistributionRestrictionsArgsDict,
                ]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tenant_config: Optional[
            pulumi.Input[
                Union[
                    MultitenantDistributionTenantConfigArgs,
                    MultitenantDistributionTenantConfigArgsDict,
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    MultitenantDistributionTimeoutsArgs,
                    MultitenantDistributionTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        viewer_certificate: Optional[
            pulumi.Input[
                Union[
                    MultitenantDistributionViewerCertificateArgs,
                    MultitenantDistributionViewerCertificateArgsDict,
                ]
            ]
        ] = ...,
        web_acl_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> MultitenantDistribution: ...
    @_builtins.property
    @pulumi.getter(name="activeTrustedKeyGroups")
    def active_trusted_key_groups(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.MultitenantDistributionActiveTrustedKeyGroup]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cacheBehaviors")
    def cache_behaviors(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.MultitenantDistributionCacheBehavior]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customErrorResponses")
    def custom_error_responses(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.MultitenantDistributionCustomErrorResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(
        self,
    ) -> pulumi.Output[outputs.MultitenantDistributionDefaultCacheBehavior]: ...
    @_builtins.property
    @pulumi.getter(name="defaultRootObject")
    def default_root_object(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpVersion")
    def http_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inProgressInvalidationBatches")
    def in_progress_invalidation_batches(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originGroups")
    def origin_groups(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.MultitenantDistributionOriginGroup]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def origins(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.MultitenantDistributionOrigin]]]: ...
    @_builtins.property
    @pulumi.getter
    def restrictions(
        self,
    ) -> pulumi.Output[Optional[outputs.MultitenantDistributionRestrictions]]: ...
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
    @pulumi.getter(name="tenantConfig")
    def tenant_config(
        self,
    ) -> pulumi.Output[outputs.MultitenantDistributionTenantConfig]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.MultitenantDistributionTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="viewerCertificate")
    def viewer_certificate(
        self,
    ) -> pulumi.Output[outputs.MultitenantDistributionViewerCertificate]: ...
    @_builtins.property
    @pulumi.getter(name="webAclId")
    def web_acl_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
