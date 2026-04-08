import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkbookTemplateArgs", "WorkbookTemplate"]

@pulumi.input_type
class WorkbookTemplateArgs:
    def __init__(
        __self__,
        *,
        galleries: pulumi.Input[Sequence[pulumi.Input[WorkbookTemplateGalleryArgs]]],
        resource_group_name: pulumi.Input[_builtins.str],
        template_data: Any,
        author: Optional[pulumi.Input[_builtins.str]] = ...,
        localized: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Sequence[pulumi.Input[WorkbookTemplateLocalizedGalleryArgs]]
                    ],
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def galleries(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[WorkbookTemplateGalleryArgs]]]: ...
    @galleries.setter
    def galleries(
        self, value: pulumi.Input[Sequence[pulumi.Input[WorkbookTemplateGalleryArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="templateData")
    def template_data(self) -> Any: ...
    @template_data.setter
    def template_data(self, value: Any): ...
    @_builtins.property
    @pulumi.getter
    def author(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @author.setter
    def author(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def localized(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Sequence[pulumi.Input[WorkbookTemplateLocalizedGalleryArgs]]
                ],
            ]
        ]
    ]: ...
    @localized.setter
    def localized(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Sequence[pulumi.Input[WorkbookTemplateLocalizedGalleryArgs]]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:applicationinsights:WorkbookTemplate")
class WorkbookTemplate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        author: Optional[pulumi.Input[_builtins.str]] = ...,
        galleries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkbookTemplateGalleryArgs, WorkbookTemplateGalleryArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        localized: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Sequence[
                            pulumi.Input[
                                Union[
                                    WorkbookTemplateLocalizedGalleryArgs,
                                    WorkbookTemplateLocalizedGalleryArgsDict,
                                ]
                            ]
                        ]
                    ],
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        template_data: Optional[Any] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkbookTemplateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WorkbookTemplate: ...
    @_builtins.property
    @pulumi.getter
    def author(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def galleries(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkbookTemplateGalleryResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def localized(
        self,
    ) -> pulumi.Output[
        Optional[
            Mapping[str, Sequence[outputs.WorkbookTemplateLocalizedGalleryResponse]]
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="templateData")
    def template_data(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
