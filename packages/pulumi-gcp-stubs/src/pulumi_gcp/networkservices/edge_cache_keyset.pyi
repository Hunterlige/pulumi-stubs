import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EdgeCacheKeysetArgs", "EdgeCacheKeyset"]

@pulumi.input_type
class EdgeCacheKeysetArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        public_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetPublicKeyArgs]]]
        ] = ...,
        validation_shared_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetValidationSharedKeyArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetPublicKeyArgs]]]
    ]: ...
    @public_keys.setter
    def public_keys(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetPublicKeyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationSharedKeys")
    def validation_shared_keys(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetValidationSharedKeyArgs]]]
    ]: ...
    @validation_shared_keys.setter
    def validation_shared_keys(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetValidationSharedKeyArgs]]]
        ],
    ): ...

@pulumi.input_type
class _EdgeCacheKeysetState:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        public_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetPublicKeyArgs]]]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        validation_shared_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetValidationSharedKeyArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetPublicKeyArgs]]]
    ]: ...
    @public_keys.setter
    def public_keys(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetPublicKeyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationSharedKeys")
    def validation_shared_keys(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetValidationSharedKeyArgs]]]
    ]: ...
    @validation_shared_keys.setter
    def validation_shared_keys(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EdgeCacheKeysetValidationSharedKeyArgs]]]
        ],
    ): ...

@pulumi.type_token(...)
class EdgeCacheKeyset(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        public_keys: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EdgeCacheKeysetPublicKeyArgs,
                            EdgeCacheKeysetPublicKeyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        validation_shared_keys: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EdgeCacheKeysetValidationSharedKeyArgs,
                            EdgeCacheKeysetValidationSharedKeyArgsDict,
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
        args: Optional[EdgeCacheKeysetArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        public_keys: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EdgeCacheKeysetPublicKeyArgs,
                            EdgeCacheKeysetPublicKeyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        validation_shared_keys: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EdgeCacheKeysetValidationSharedKeyArgs,
                            EdgeCacheKeysetValidationSharedKeyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> EdgeCacheKeyset: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.EdgeCacheKeysetPublicKey]]]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="validationSharedKeys")
    def validation_shared_keys(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.EdgeCacheKeysetValidationSharedKey]]
    ]: ...
