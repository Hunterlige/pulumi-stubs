import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServicePerimetersArgs", "ServicePerimeters"]

@pulumi.input_type
class ServicePerimetersArgs:
    def __init__(
        __self__,
        *,
        parent: pulumi.Input[_builtins.str],
        service_perimeters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServicePerimetersServicePerimeterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="servicePerimeters")
    def service_perimeters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServicePerimetersServicePerimeterArgs]]]
    ]: ...
    @service_perimeters.setter
    def service_perimeters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServicePerimetersServicePerimeterArgs]]]
        ],
    ): ...

@pulumi.input_type
class _ServicePerimetersState:
    def __init__(
        __self__,
        *,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        service_perimeters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServicePerimetersServicePerimeterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="servicePerimeters")
    def service_perimeters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServicePerimetersServicePerimeterArgs]]]
    ]: ...
    @service_perimeters.setter
    def service_perimeters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServicePerimetersServicePerimeterArgs]]]
        ],
    ): ...

@pulumi.type_token(...)
class ServicePerimeters(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        service_perimeters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ServicePerimetersServicePerimeterArgs,
                            ServicePerimetersServicePerimeterArgsDict,
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
        args: ServicePerimetersArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        service_perimeters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ServicePerimetersServicePerimeterArgs,
                            ServicePerimetersServicePerimeterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> ServicePerimeters: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="servicePerimeters")
    def service_perimeters(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ServicePerimetersServicePerimeter]]
    ]: ...
