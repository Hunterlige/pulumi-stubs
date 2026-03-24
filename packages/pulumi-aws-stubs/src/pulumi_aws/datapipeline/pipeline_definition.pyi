import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PipelineDefinitionArgs", "PipelineDefinition"]

@pulumi.input_type
class PipelineDefinitionArgs:
    def __init__(
        __self__,
        *,
        pipeline_id: pulumi.Input[_builtins.str],
        pipeline_objects: pulumi.Input[
            Sequence[pulumi.Input[PipelineDefinitionPipelineObjectArgs]]
        ],
        parameter_objects: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterObjectArgs]]]
        ] = ...,
        parameter_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterValueArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> pulumi.Input[_builtins.str]: ...
    @pipeline_id.setter
    def pipeline_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineObjects")
    def pipeline_objects(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionPipelineObjectArgs]]]: ...
    @pipeline_objects.setter
    def pipeline_objects(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[PipelineDefinitionPipelineObjectArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parameterObjects")
    def parameter_objects(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterObjectArgs]]]
    ]: ...
    @parameter_objects.setter
    def parameter_objects(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterObjectArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parameterValues")
    def parameter_values(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterValueArgs]]]
    ]: ...
    @parameter_values.setter
    def parameter_values(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterValueArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PipelineDefinitionState:
    def __init__(
        __self__,
        *,
        parameter_objects: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterObjectArgs]]]
        ] = ...,
        parameter_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterValueArgs]]]
        ] = ...,
        pipeline_id: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_objects: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionPipelineObjectArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterObjects")
    def parameter_objects(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterObjectArgs]]]
    ]: ...
    @parameter_objects.setter
    def parameter_objects(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterObjectArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parameterValues")
    def parameter_values(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterValueArgs]]]
    ]: ...
    @parameter_values.setter
    def parameter_values(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionParameterValueArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pipeline_id.setter
    def pipeline_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineObjects")
    def pipeline_objects(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionPipelineObjectArgs]]]
    ]: ...
    @pipeline_objects.setter
    def pipeline_objects(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionPipelineObjectArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class PipelineDefinition(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        parameter_objects: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PipelineDefinitionParameterObjectArgs,
                            PipelineDefinitionParameterObjectArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        parameter_values: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PipelineDefinitionParameterValueArgs,
                            PipelineDefinitionParameterValueArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        pipeline_id: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_objects: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PipelineDefinitionPipelineObjectArgs,
                            PipelineDefinitionPipelineObjectArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PipelineDefinitionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        parameter_objects: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PipelineDefinitionParameterObjectArgs,
                            PipelineDefinitionParameterObjectArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        parameter_values: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PipelineDefinitionParameterValueArgs,
                            PipelineDefinitionParameterValueArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        pipeline_id: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_objects: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PipelineDefinitionPipelineObjectArgs,
                            PipelineDefinitionPipelineObjectArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PipelineDefinition: ...
    @_builtins.property
    @pulumi.getter(name="parameterObjects")
    def parameter_objects(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.PipelineDefinitionParameterObject]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="parameterValues")
    def parameter_values(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.PipelineDefinitionParameterValue]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pipelineObjects")
    def pipeline_objects(
        self,
    ) -> pulumi.Output[Sequence[outputs.PipelineDefinitionPipelineObject]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
