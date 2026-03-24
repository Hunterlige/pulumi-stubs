import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BucketNotificationArgs", "BucketNotification"]

@pulumi.input_type
class BucketNotificationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        eventbridge: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_functions: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationLambdaFunctionArgs]]]
        ] = ...,
        queues: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationQueueArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        topics: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationTopicArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def eventbridge(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @eventbridge.setter
    def eventbridge(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctions")
    def lambda_functions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BucketNotificationLambdaFunctionArgs]]]
    ]: ...
    @lambda_functions.setter
    def lambda_functions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationLambdaFunctionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def queues(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BucketNotificationQueueArgs]]]
    ]: ...
    @queues.setter
    def queues(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationQueueArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def topics(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BucketNotificationTopicArgs]]]
    ]: ...
    @topics.setter
    def topics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationTopicArgs]]]
        ],
    ): ...

@pulumi.input_type
class _BucketNotificationState:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        eventbridge: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_functions: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationLambdaFunctionArgs]]]
        ] = ...,
        queues: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationQueueArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        topics: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationTopicArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def eventbridge(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @eventbridge.setter
    def eventbridge(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctions")
    def lambda_functions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BucketNotificationLambdaFunctionArgs]]]
    ]: ...
    @lambda_functions.setter
    def lambda_functions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationLambdaFunctionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def queues(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BucketNotificationQueueArgs]]]
    ]: ...
    @queues.setter
    def queues(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationQueueArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def topics(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BucketNotificationTopicArgs]]]
    ]: ...
    @topics.setter
    def topics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketNotificationTopicArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:s3/bucketNotification:BucketNotification")
class BucketNotification(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        eventbridge: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_functions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketNotificationLambdaFunctionArgs,
                            BucketNotificationLambdaFunctionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        queues: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketNotificationQueueArgs, BucketNotificationQueueArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        topics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketNotificationTopicArgs, BucketNotificationTopicArgsDict
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
        args: BucketNotificationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        eventbridge: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_functions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketNotificationLambdaFunctionArgs,
                            BucketNotificationLambdaFunctionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        queues: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketNotificationQueueArgs, BucketNotificationQueueArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        topics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketNotificationTopicArgs, BucketNotificationTopicArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> BucketNotification: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def eventbridge(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctions")
    def lambda_functions(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.BucketNotificationLambdaFunction]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def queues(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.BucketNotificationQueue]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topics(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.BucketNotificationTopic]]]: ...
