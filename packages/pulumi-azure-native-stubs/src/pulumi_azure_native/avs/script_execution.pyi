import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ScriptExecutionArgs", "ScriptExecution"]

@pulumi.input_type
class ScriptExecutionArgs:
    def __init__(
        __self__,
        *,
        private_cloud_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        timeout: pulumi.Input[_builtins.str],
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        hidden_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PSCredentialExecutionParameterArgs,
                            ScriptSecureStringExecutionParameterArgs,
                            ScriptStringExecutionParameterArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        named_outputs: Optional[pulumi.Input[Mapping[str, Any]]] = ...,
        output: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PSCredentialExecutionParameterArgs,
                            ScriptSecureStringExecutionParameterArgs,
                            ScriptStringExecutionParameterArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        retention: Optional[pulumi.Input[_builtins.str]] = ...,
        script_cmdlet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        script_execution_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[_builtins.str]: ...
    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Input[_builtins.str]: ...
    @timeout.setter
    def timeout(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hiddenParameters")
    def hidden_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        PSCredentialExecutionParameterArgs,
                        ScriptSecureStringExecutionParameterArgs,
                        ScriptStringExecutionParameterArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @hidden_parameters.setter
    def hidden_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PSCredentialExecutionParameterArgs,
                            ScriptSecureStringExecutionParameterArgs,
                            ScriptStringExecutionParameterArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="namedOutputs")
    def named_outputs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]: ...
    @named_outputs.setter
    def named_outputs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]): ...
    @_builtins.property
    @pulumi.getter
    def output(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @output.setter
    def output(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        PSCredentialExecutionParameterArgs,
                        ScriptSecureStringExecutionParameterArgs,
                        ScriptStringExecutionParameterArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PSCredentialExecutionParameterArgs,
                            ScriptSecureStringExecutionParameterArgs,
                            ScriptStringExecutionParameterArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retention.setter
    def retention(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptCmdletId")
    def script_cmdlet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_cmdlet_id.setter
    def script_cmdlet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptExecutionName")
    def script_execution_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_execution_name.setter
    def script_execution_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:avs:ScriptExecution")
class ScriptExecution(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        hidden_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            Union[
                                PSCredentialExecutionParameterArgs,
                                PSCredentialExecutionParameterArgsDict,
                            ],
                            Union[
                                ScriptSecureStringExecutionParameterArgs,
                                ScriptSecureStringExecutionParameterArgsDict,
                            ],
                            Union[
                                ScriptStringExecutionParameterArgs,
                                ScriptStringExecutionParameterArgsDict,
                            ],
                        ]
                    ]
                ]
            ]
        ] = ...,
        named_outputs: Optional[pulumi.Input[Mapping[str, Any]]] = ...,
        output: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            Union[
                                PSCredentialExecutionParameterArgs,
                                PSCredentialExecutionParameterArgsDict,
                            ],
                            Union[
                                ScriptSecureStringExecutionParameterArgs,
                                ScriptSecureStringExecutionParameterArgsDict,
                            ],
                            Union[
                                ScriptStringExecutionParameterArgs,
                                ScriptStringExecutionParameterArgsDict,
                            ],
                        ]
                    ]
                ]
            ]
        ] = ...,
        private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        retention: Optional[pulumi.Input[_builtins.str]] = ...,
        script_cmdlet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        script_execution_name: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ScriptExecutionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ScriptExecution: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="finishedAt")
    def finished_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hiddenParameters")
    def hidden_parameters(self) -> pulumi.Output[Optional[Sequence[Any]]]: ...
    @_builtins.property
    @pulumi.getter
    def information(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namedOutputs")
    def named_outputs(self) -> pulumi.Output[Optional[Mapping[str, Any]]]: ...
    @_builtins.property
    @pulumi.getter
    def output(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence[Any]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scriptCmdletId")
    def script_cmdlet_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startedAt")
    def started_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="submittedAt")
    def submitted_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def warnings(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
