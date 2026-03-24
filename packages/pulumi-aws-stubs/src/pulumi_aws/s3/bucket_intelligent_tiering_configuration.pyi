import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BucketIntelligentTieringConfigurationArgs",
    "BucketIntelligentTieringConfiguration",
]

@pulumi.input_type
class BucketIntelligentTieringConfigurationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        tierings: pulumi.Input[
            Sequence[pulumi.Input[BucketIntelligentTieringConfigurationTieringArgs]]
        ],
        filter: Optional[
            pulumi.Input[BucketIntelligentTieringConfigurationFilterArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tierings(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[BucketIntelligentTieringConfigurationTieringArgs]]
    ]: ...
    @tierings.setter
    def tierings(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[BucketIntelligentTieringConfigurationTieringArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> Optional[pulumi.Input[BucketIntelligentTieringConfigurationFilterArgs]]: ...
    @filter.setter
    def filter(
        self,
        value: Optional[pulumi.Input[BucketIntelligentTieringConfigurationFilterArgs]],
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
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _BucketIntelligentTieringConfigurationState:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[BucketIntelligentTieringConfigurationFilterArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tierings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketIntelligentTieringConfigurationTieringArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> Optional[pulumi.Input[BucketIntelligentTieringConfigurationFilterArgs]]: ...
    @filter.setter
    def filter(
        self,
        value: Optional[pulumi.Input[BucketIntelligentTieringConfigurationFilterArgs]],
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
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tierings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BucketIntelligentTieringConfigurationTieringArgs]]
        ]
    ]: ...
    @tierings.setter
    def tierings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketIntelligentTieringConfigurationTieringArgs]]
            ]
        ],
    ): ...

@pulumi.type_token(...)
class BucketIntelligentTieringConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[
                Union[
                    BucketIntelligentTieringConfigurationFilterArgs,
                    BucketIntelligentTieringConfigurationFilterArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tierings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketIntelligentTieringConfigurationTieringArgs,
                            BucketIntelligentTieringConfigurationTieringArgsDict,
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
        args: BucketIntelligentTieringConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[
                Union[
                    BucketIntelligentTieringConfigurationFilterArgs,
                    BucketIntelligentTieringConfigurationFilterArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tierings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketIntelligentTieringConfigurationTieringArgs,
                            BucketIntelligentTieringConfigurationTieringArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> BucketIntelligentTieringConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> pulumi.Output[
        Optional[outputs.BucketIntelligentTieringConfigurationFilter]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tierings(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.BucketIntelligentTieringConfigurationTiering]
    ]: ...
